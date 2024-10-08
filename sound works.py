import time,RPi.GPIO as GPIO

passbuzz_pin=31,29

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(passbuzz_pin[0],GPIO.OUT)
GPIO.setup(passbuzz_pin[1],GPIO.OUT)
passbuzz1=GPIO.PWM(passbuzz_pin[0],400)
passbuzz2=GPIO.PWM(passbuzz_pin[1],400)

def pb1():
    passbuzz1.start(50)
    for i in range(1):        
        for x in range(50,300):
            passbuzz1.ChangeFrequency(x)
            time.sleep(.004)
        for x in range(300,50,-1):
            passbuzz1.ChangeFrequency(x)
            time.sleep(.004)
            
    passbuzz1.stop(50)
    
def pb2():
    passbuzz2.start(50)
    for i in range(1):
        for x in range(50,300):
            passbuzz2.ChangeFrequency(x)
            time.sleep(.004)
        for x in range(300,50,-1):
            passbuzz2.ChangeFrequency(x)
            time.sleep(.004)
            
    passbuzz2.stop(50)

pb1()
pb2()
GPIO.cleanup()