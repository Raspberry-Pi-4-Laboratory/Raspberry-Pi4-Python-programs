import time,RPi.GPIO as GPIO,threading,random

passbuzz_pin = 31,29

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(passbuzz_pin[0],GPIO.OUT)
GPIO.setup(passbuzz_pin[1],GPIO.OUT)
passbuzz1 = GPIO.PWM(passbuzz_pin[0],400)
passbuzz2 = GPIO.PWM(passbuzz_pin[1],400)

def passive_buzzer1():    
    
    while True:
        passbuzz1.start(50)
        randfreq = random.randint(1,1500)
        passbuzz1.ChangeFrequency(randfreq)
        time.sleep(.1)
        randfreq = random.randint(1,1500)
        passbuzz1.ChangeFrequency(randfreq)
        time.sleep(.1)
            
        passbuzz1.stop(50)
        time.sleep(.02)
                
def passive_buzzer2():    
    
    while True:
        passbuzz2.start(50)
        randfreq = random.randint(1,1500)
        passbuzz2.ChangeFrequency(randfreq)
        time.sleep(.1)
        randfreq = random.randint(1,1500)
        passbuzz2.ChangeFrequency(randfreq)
        time.sleep(.1)
            
        passbuzz2.stop(50)
        time.sleep(.02)
   
a = threading.Thread(target = passive_buzzer1)
b = threading.Thread(target = passive_buzzer2)

a.start()
b.start()
