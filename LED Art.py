# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Respberry Pi 4 = 1
# breadboard = 1
# RGB LED = 1
# LEDs = 12
# 220 ohm resistor = 15
# jumper wire = 15+2 for the Rasp pi fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# Raspberry Pi 4 Python program example:

# Here are some function samples of blinking
# and breathing leds.

# First, place ten red leds in a single
# row. Next, place two yellow leds, one
# on each end of the ten red leds. Next
# leave some room for the RGB led, which
# will take three 220 ohm resistors on
# each positive node. Make sure the longer
# node is either in 3v or ground. My RGB
# led takes the 3v pin on the Ras pi. Now
# place RGB led right smack in the middle
# of the red leds.

# Note: if your RGB takes 3v, then make sure
# you don't place its three resistors on the
# ground rails, where all the red leds resistors
# are located. Instead, make sure you have
# jumper wires connected to three GPIO pins
# either in front of each of the three resistors
# or behind them. I keep my jumper wires behind
# all my resistors as much as I can. It looks
# less confusing and neat at the same time.
# However, in my case, my jumper wires are all
# behind my leds, but not behind my resistors.
# My RGB shows the example I like best. All
# depending on your breadboard layout is what
# matters the most. Try to layout your work
# like you want it, but make sure you set up
# everything to connect the way you want.
# Yet, why not use one ground wire to feed all
# your ten red leds, instead of having all kinds
# of extra ground wires connected to each led.
# Sometimes, you've just got to go for the
# betterment of the two setups, I've tried so
# far. That's why I cannot stick my jumper
# wires right behind my resistors, like I like
# them to be. But instead, I took the betterment
# of the two and simply placed my jumpers
# directly in front of all my resistors, except
# for the RGB led, which has its own 3v supply.
# All the other 12 leds including the yellow
# leds, all have their resistors connected
# to the ground rail on my breadboard setup.
# In all, you get to play with 13 leds, when
# you consider the RGB led as the 13th.

# I hope other Raspberry Pi owners will like
# this Python program to get them going into
# the Raspberry Pi, no matter what kind; I
# have a Ras Pi 4. I just got it, but I'm
# Hooooked!!!!!!!!

# Note: I will be doing a video about my
# breadboard and jumper wire layout in the
# near future. This video will show you
# how to use this Raspberry Pi 4 Python
# program example with the very same bread-
# board layout, I use so you can follow
# right along with my video example.

import RPi.GPIO as GPIO
from time import sleep as wait

# Breadboard Metod:
# Actual GPIO Pinouts

red_leds=[11,13,15,19,21,23,29,31,33,35]

yellow_leds=[7,37]

RGB_led=[18,16,12]

RGB_mix=[[18,12],[18,16],[16,12]]

RGB_logic=[18,16,12,[18,16],
[18,12],[12,16],[18,16,12,16]]

hz=500 # LED dimmer herz value

led_speed=.1

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

for i in red_leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)
    
for i in RGB_led:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)
    
for i in yellow_leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)
    
def RGB_led_twinkle():
    
    for i in range(7):
        GPIO.output(RGB_logic[i],0)
        wait(led_speed)
        GPIO.output(RGB_logic[i],1)
        
    for i in range(5,-1,-1):
        GPIO.output(RGB_logic[i],0)
        wait(led_speed)
        GPIO.output(RGB_logic[i],1)

def red_leds_flash():

    for i in range(5):
        for j in red_leds:
            GPIO.output(j,1)
            
        for j in yellow_leds:
            GPIO.output(j,0)            
        GPIO.output(RGB_led[0],0)
        wait(led_speed)

        for j in red_leds:
            GPIO.output(j,0)
            
        for j in yellow_leds:
            GPIO.output(j,1)
        GPIO.output(RGB_mix[1],0)
        wait(led_speed)
        
        for j in yellow_leds:
            GPIO.output(j,0)
        GPIO.output(RGB_mix[1],1)
        
def red_led_single_right():
    
        for i in yellow_leds:
            GPIO.output(i,1)
        GPIO.output(RGB_led[0],0)
    
        for i in range(9,-1,-1):
            GPIO.output(red_leds[i],1)        
            wait(led_speed)
            GPIO.output(red_leds[i],0)
            
        for i in yellow_leds:
            GPIO.output(i,0)
        GPIO.output(RGB_led[0],1)
        
def red_led_single_left():
    
        for i in yellow_leds:
            GPIO.output(i,1)
        GPIO.output(RGB_led[0],0)
    
        for i in range(10):
            GPIO.output(red_leds[i],1)        
            wait(led_speed)
            GPIO.output(red_leds[i],0)
            
        for i in yellow_leds:
            GPIO.output(i,0)
        GPIO.output(RGB_led[0],1)
        
def red_leds_side_to_side_right():
    
    for i in yellow_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_led[0],0)

    for i in range(9,-1,-1):
        GPIO.output(red_leds[i],1)
        wait(led_speed)
        
    for i in yellow_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[1],0)

    for i in range(9,-1,-1):
        GPIO.output(red_leds[i],0)
        wait(led_speed)
        
    GPIO.output(RGB_mix[1],1)
    
def red_leds_side_to_side_left():
    
    for i in yellow_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_led[0],0)

    for i in range(10):
        GPIO.output(red_leds[i],1)
        wait(led_speed)
        
    for i in yellow_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[1],0)

    for i in red_leds:
        GPIO.output(i,0)
        wait(led_speed)
        
    GPIO.output(RGB_mix[1],1)
    
def red_leds_inward():
    
    for i in yellow_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_led[0],0)

    for i in range(5):
        GPIO.output(red_leds[0+i],1)
        GPIO.output(red_leds[9-i],1)
        wait(led_speed)
        
    for i in yellow_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[1],0)
        
    for i in range(5):
        GPIO.output(red_leds[0+i],0)
        GPIO.output(red_leds[9-i],0)
        wait(led_speed)
        
    GPIO.output(RGB_mix[1],1)
    
def red_leds_outward():
    
    for i in yellow_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_led[0],0)

    for i in range(4,-1,-1):
        GPIO.output(red_leds[0+i],1)
        GPIO.output(red_leds[9-i],1)
        wait(led_speed)
        
    for i in yellow_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[1],0)
        
    for i in range(4,-1,-1):
        GPIO.output(red_leds[0+i],0)
        GPIO.output(red_leds[9-i],0)
        wait(led_speed)
        
    GPIO.output(RGB_mix[1],1)

def red_leds_collision_inward():
    
    for i in yellow_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_led[0],0)

    for i in range(5):
        GPIO.output(red_leds[0+i],1)
        GPIO.output(red_leds[9-i],1)
        wait(led_speed)
        GPIO.output(red_leds[0+i],0)
        GPIO.output(red_leds[9-i],0)
        
    for i in yellow_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[0],1)
    
def red_leds_collision_outward():
    
    for i in yellow_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_led[0],0)

    for i in range(4,-1,-1):
        GPIO.output(red_leds[0+i],1)
        GPIO.output(red_leds[9-i],1)
        wait(led_speed)
        GPIO.output(red_leds[0+i],0)
        GPIO.output(red_leds[9-i],0)
        
    for i in yellow_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[0],1)
    
def red_leds_follow():
    
    for i in range(5):
        for j in range(0,10,2):
            GPIO.output(red_leds[j],1)
            
        GPIO.output(RGB_led[0],0)            
        GPIO.output(yellow_leds[1],1)
        wait(led_speed)
        
        for i in red_leds:
            GPIO.output(i,0)
            
        GPIO.output(RGB_mix[1],0)   
        GPIO.output(yellow_leds[1],0)
        
        for j in range(9,-1,-2):
            GPIO.output(red_leds[j],1)
         
        GPIO.output(RGB_mix[1],0)
        GPIO.output(yellow_leds[0],1)
        wait(led_speed)
        
        for j in red_leds:
            GPIO.output(j,0)
            
        GPIO.output(RGB_mix[1],1)   
        GPIO.output(yellow_leds[0],0)
        
def red_led_single_right_inverse():
    
        for i in red_leds:
            GPIO.output(i,1)
    
        GPIO.output(RGB_mix[1],0)
    
        for i in range(9,-1,-1):
            GPIO.output(red_leds[i],0)        
            wait(led_speed)
            GPIO.output(red_leds[i],1)
            
        for i in red_leds:
            GPIO.output(i,0)            
        for i in yellow_leds:
            GPIO.output(i,0)
        GPIO.output(RGB_mix[1],1)

def red_led_single_left_inverse():
    
        for i in red_leds:
            GPIO.output(i,1)
            
        GPIO.output(RGB_mix[1],0)
    
        for i in range(10):
            GPIO.output(red_leds[i],0)        
            wait(led_speed)
            GPIO.output(red_leds[i],1)
            
        for i in red_leds:
            GPIO.output(i,0)   
        for i in yellow_leds:
            GPIO.output(i,0)
        GPIO.output(RGB_mix[1],1)
        
def red_leds_collision_inward_inverse():
    
    for i in red_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_mix[1],0)

    for i in range(5):
        GPIO.output(red_leds[0+i],0)
        GPIO.output(red_leds[9-i],0)
        wait(led_speed)
        GPIO.output(red_leds[0+i],1)
        GPIO.output(red_leds[9-i],1)
        
    for i in red_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[1],1)

def red_leds_collision_outward_inverse():
    
    for i in red_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_mix[1],0)

    for i in range(4,-1,-1):
        GPIO.output(red_leds[0+i],0)
        GPIO.output(red_leds[9-i],0)
        wait(led_speed)
        GPIO.output(red_leds[0+i],1)
        GPIO.output(red_leds[9-i],1)
        
    for i in red_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[1],1)

def red_leds_stack_right():
    
    for i in range(10):
        GPIO.output(yellow_leds[0],0)
        GPIO.output(yellow_leds[1],0)
        GPIO.output(RGB_mix[1],0)
        for j in range(9,i-1,-1):
            GPIO.output(red_leds[j],1)        
            wait(led_speed)
            GPIO.output(yellow_leds[0],1)
            GPIO.output(yellow_leds[1],1)
            GPIO.output(RGB_mix[1],1)
            GPIO.output(RGB_led[0],0)
            GPIO.output(red_leds[j],0)
            
        GPIO.output(red_leds[j],1)
        for i in yellow_leds:
            GPIO.output(i,0)
        GPIO.output(RGB_led[0],1)
        
    for i in red_leds:
        GPIO.output(i,0)

def red_leds_stack_left():
    
    for i in range(10):
        GPIO.output(yellow_leds[0],0)
        GPIO.output(yellow_leds[1],0)
        GPIO.output(RGB_mix[1],0)
        for j in range(10-i):
            GPIO.output(red_leds[j],1)        
            wait(led_speed)
            GPIO.output(yellow_leds[0],1)
            GPIO.output(yellow_leds[1],1)
            GPIO.output(RGB_mix[1],1)
            GPIO.output(RGB_led[0],0)
            GPIO.output(red_leds[j],0)
            
        GPIO.output(red_leds[j],1)
        for i in yellow_leds:
            GPIO.output(i,0)
        GPIO.output(RGB_led[0],1)
        
    for i in red_leds:
        GPIO.output(i,0)
        
def red_leds_stack_inward():
    
    for i in range(5):
        GPIO.output(yellow_leds[0],0)
        GPIO.output(yellow_leds[1],0)
        GPIO.output(RGB_mix[1],0)
        for j in range(5-i):
            GPIO.output(red_leds[0+j],1)
            GPIO.output(red_leds[9-j],1)
            wait(led_speed)
            GPIO.output(yellow_leds[0],1)
            GPIO.output(yellow_leds[1],1)
            GPIO.output(RGB_mix[1],1)
            GPIO.output(RGB_led[0],0)
            GPIO.output(red_leds[0+j],0)
            GPIO.output(red_leds[9-j],0)
            
        GPIO.output(red_leds[j],1)
        GPIO.output(red_leds[9-j],1)
        for i in yellow_leds:
            GPIO.output(i,0)
        GPIO.output(RGB_led[0],1)
        
    for i in red_leds:
        GPIO.output(i,0)
        
def red_leds_stack_outward():
    
    for i in range(5):
        GPIO.output(yellow_leds[0],0)
        GPIO.output(yellow_leds[1],0)
        GPIO.output(RGB_mix[1],0)
        for j in range(4,i-1,-1):
            GPIO.output(red_leds[0+j],1)
            GPIO.output(red_leds[9-j],1)
            wait(led_speed)
            GPIO.output(yellow_leds[0],1)
            GPIO.output(yellow_leds[1],1)
            GPIO.output(RGB_mix[1],1)
            GPIO.output(RGB_led[0],0)
            GPIO.output(red_leds[0+j],0)
            GPIO.output(red_leds[9-j],0)
            
        GPIO.output(red_leds[j],1)
        GPIO.output(red_leds[9-j],1)
        for i in yellow_leds:
            GPIO.output(i,0)
        GPIO.output(RGB_led[0],1)
        
    for i in red_leds:
        GPIO.output(i,0)

def red_leds_breathe():
    
    a0=GPIO.PWM(red_leds[0],hz)
    a1=GPIO.PWM(red_leds[1],hz)
    a2=GPIO.PWM(red_leds[2],hz)
    a3=GPIO.PWM(red_leds[3],hz)
    a4=GPIO.PWM(red_leds[4],hz)
    a5=GPIO.PWM(red_leds[5],hz)
    a6=GPIO.PWM(red_leds[6],hz)
    a7=GPIO.PWM(red_leds[7],hz)
    a8=GPIO.PWM(red_leds[8],hz)
    a9=GPIO.PWM(red_leds[9],hz)    

    dimmer=(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9)

    GPIO.output(RGB_led[0],0)
    for i in range(0,100,2):
        for j in dimmer:
            j.start(0)
            j.ChangeDutyCycle(i)
        for i in yellow_leds:
            GPIO.output(i,1)
            wait(.02)

    for i in range(100,-1,-2):
        GPIO.output(RGB_mix[1],0)
        for j in dimmer:
            j.start(0)
            j.ChangeDutyCycle(i)
        for i in yellow_leds:
            GPIO.output(i,0)
            wait(.02)
        GPIO.output(RGB_mix[1],1)
            
red_leds_breathe()
RGB_led_twinkle()
red_leds_flash()
    
led_functions=[
    red_led_single_left,
    red_led_single_right_inverse,
    red_leds_side_to_side_left,
    red_leds_side_to_side_right,
    red_leds_follow,
    red_leds_collision_inward,
    red_leds_collision_outward_inverse,
    red_leds_inward,
    red_leds_outward,
    red_leds_collision_inward_inverse,
    red_leds_collision_outward,
    red_leds_stack_inward,
    red_leds_stack_outward,
    red_leds_stack_left,
    red_leds_stack_right,
    ]

print('You used',len(led_functions),
      'LED Functions:')

while True:
    try:
        for i in led_functions:
            i()
            
# Note: it is recomended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF

    except KeyboardInterrupt:
        print('\nStop program Execution/run:')
        print('cleanup/release all GPIO pinouts \
to LOW state.')
        GPIO.cleanup()
        break
