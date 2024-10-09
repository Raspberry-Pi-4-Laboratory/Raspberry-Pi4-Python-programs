# Two Passive Buzzers Python program example:

# Created by Joseph C. Richardson, GitHub.com

# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Raspberry Pi 4 = 1
# breadboard = 1 or more depending 
# 3V passive buzzer = 2
# PNP S8550D331 transistor = 2
# 1K ohm resistor = 2
# jumper wire = 8 +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# Two Passive Buzzers Python program example:

# This Raspberry Pi 4 Python program allows
# users to have tons of fun, while learning
# how passive buzzers work.

# We will use the breadboard method:

# GPIO.setmode(GPIO.BOARD)

# This method is for the GPIO pinouts
# not the GPIO numbers, such as BCM

# You can also use the Broadcom SOC
# Channel method if you prefer:

# GPIO.setmode(GPIO.BCM)
# This allows GPIO numbers, not GPIO
# pinouts, such as the breadboard
# method illustrates in our Python
# program example.

import time,RPi.GPIO as GPIO,threading

passbuzz_pin=31,29

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(passbuzz_pin[0],GPIO.OUT)
GPIO.setup(passbuzz_pin[1],GPIO.OUT)
passbuzz1=GPIO.PWM(passbuzz_pin[0],400)
passbuzz2=GPIO.PWM(passbuzz_pin[1],400)

def passive_buzzer1():
    
    while True:
        passbuzz1.start(50)
                
        for i in range(400,500):
            passbuzz1.ChangeFrequency(i)
            time.sleep(.004)
        for i in range(500,400,-1):
            passbuzz1.ChangeFrequency(i)
            time.sleep(.004)
            
        passbuzz1.stop(50)
    
def passive_buzzer2():
    
    while True:
        passbuzz2.start(50)

        for i in range(50,1000):
            passbuzz2.ChangeFrequency(i)
            time.sleep(.004)
        for i in range(1000,50,-1):
            passbuzz2.ChangeFrequency(i)
            time.sleep(.004)
            
        passbuzz2.stop(50)
    
a=threading.Thread(target=passive_buzzer1)
b=threading.Thread(target=passive_buzzer2)

a.start()
b.start()
