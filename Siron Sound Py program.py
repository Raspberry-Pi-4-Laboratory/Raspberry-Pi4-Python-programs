import time,RPI.GPIO as GPIO

buzzpin=11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzpin,GPIO.OUT)
buzz=GPIO.PWM(buzzpin,400)

buzz.start(50)
try:
    while True:        
        for i in range(50,1000):
            buzz.ChangeFrequency(i)
            time.sleep(.001)
            
        for i in range(1000,50,-1):
            buzz.ChangeFrequency(i)
            time.sleep(.001)
except KeyboardInterrupt:
    GPIO.cleanup()
