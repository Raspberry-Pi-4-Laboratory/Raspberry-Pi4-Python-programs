# Scroll lcd text Python Program
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
# jumper wire = 4+2 for the Rasp fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# Scroll lcd text Python program:

# This Raspberry Pi 4 Python program
# allows users to create scrolling lcd
# text the easy way!

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

from time import sleep as wait
import RPi.GPIO as GPIO,drivers

title='SCROLL LCD TEXT:'
text=('SCROLL LCD TEXT THE EASY WAY! ',
      'SCROLLING LCD TEXT IS SO EASY NOW... ',
      'BY Joseph C. Richardson, GitHub.com ')

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen

while True:
    try:
        display.lcd_clear() 
        for x in range(3):
            display.lcd_display_string(title,1)
            display.lcd_display_string(text[x],2)
            wait(.5)
            for i in range(len(text[x])):
                display.lcd_display_string(
                text[x][i:i+16],2)
                wait(0.2)               
        
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

'''remove comment quotes

# The easier Python program example:

text=('SCROLLING LCD TEXT MADE SIMLPLE! ')

while True:
    display.lcd_display_string(
    ' RASPBERRY Pi 4',1)
    for i in range(len(text)-1+1):        
        display.lcd_display_string(
        text[i:i+16],2)
        wait(0.2)
        
remove comment quotes'''
