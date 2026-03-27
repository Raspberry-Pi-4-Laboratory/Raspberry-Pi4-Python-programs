# My second Raspberry Pi 4 Python program
# example:

# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Respberry Pi 4 = 1
# breadboard = 1
# LCD display = 1
# RGB LED = 1
# LEDs = 13
# 220 ohm resistor = 16
# jumper wire = 20+2 for the Rasp pi fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# GPIO PIN NUMBER HELP Python program:

# This Raspberry Pi 4 Python program
# allows users to input pin numbers
# and learn where the GPIO pins are
# with LED indicators that flash three
# times showing where the GPIO pinouts
# reside. Next follow the wires.

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
# program example:

import RPi.GPIO as GPIO,drivers
from time import sleep as wait

# Breadboard Metod:
# Actual GPIO Pinouts

pins1=[7,11,13,15,19,21,23,29,31,33,35,37,32]

pins2=[18,16,12]

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen

for i in pins1:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)
    
for i in pins2:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)
    
# Start creating text with the LCD display

display.lcd_backlight(1)

display.lcd_display_string(
'PIN NUMBER HELP:',1)
wait(3)
display.lcd_clear()

display.lcd_display_string(
'GPIO.setmode',1)
display.lcd_display_string(
'(GPIO.BOARD)',2)
wait(3)
display.lcd_clear()
   
while True:
    try:
        display.lcd_clear()
        display.lcd_display_string(
        'AND PRESS ENTER:',2)
        message=int(input(
        display.lcd_display_string(
        'TYPE PIN NUMBER ',1)))
        
        display.lcd_clear()
        display.lcd_display_string(
        f'PIN NUMBER ({message})',1)
        display.lcd_display_string(
        f'FLASH = 3 TIMES:',2)
        
        for i in range(3):
            GPIO.output(message,1)    
            wait(1)
            GPIO.output(message,0)
            wait(1)
        for i in pins2:
            GPIO.output(i,1)
            
# Note: it is recomended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF           
            
    except KeyboardInterrupt:
        print('\nStop program Execution/run:')
        print('cleanup/release all GPIO pinouts \
to LOW state.')
        display.lcd_clear()
        display.lcd_backlight(0)
        GPIO.cleanup()
        break
    
    except BaseException:
        display.lcd_clear()
        display.lcd_display_string(
        'PIN NOT IN USE:',1)
        wait(2)
