
# DREADNAUGHT FEAR NOT PROJECT Python program example:

# Learn how to build the Dreadnaught Fear Not Project. Please
# note: this Raspberry Pi 4 project and Python programming
# examples might not be recommended for the novice/beginner.

# Created by Joseph C. Richardson, on GitHub.com

# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Raspberry Pi 4 = 1
# breadboard = 5 or more depending
# 74HC595 shift register = 2
# I²C LCD1602 LCD display = 1
# 5V passive buzzer = 2
# 5V active buzzer = 1
# PNP transistor = 3
# 1kΩ resister for PNP transistor = 3
# logic power = on, 0
# or if you like:
# NPN transistor = 3
# 10kΩ ohm resister for NPN transistor = 3
# logic power = on, 1
# LED (Light-Emitting Diode) = 18
# LED RGB (Red, Green, Blue) = 2
# 220Ω ohm resistor = 24
# jumper wire = approx. 61 or more +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for the Raspberry Pi 4
# fan, while in use/operation.

# Dreadnaught Fear Not Project Python program example:

# This Raspberry Pi 4 Python program allows
# users to have tons of fun, while learning
# how two 8b 74HC595 shift registers work.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# import functions:

import RPi.GPIO as GPIO,drivers,threading,random
from sixteen_bit_LED_intro import*
from time import sleep as wait

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

display = drivers.Lcd()
display_text = display.lcd_display_string

display.lcd_clear()
display.lcd_backlight(0)

active_buzz_pin = 29
passive_buzz_pin = 31,37

GPIO.setup(active_buzz_pin,GPIO.OUT)
GPIO.setup(passive_buzz_pin[0],GPIO.OUT)
GPIO.setup(passive_buzz_pin[1],GPIO.OUT)

passive_buzzer1 = GPIO.PWM(passive_buzz_pin[0],400)
passive_buzzer2 = GPIO.PWM(passive_buzz_pin[1],400)

# Create variables for the SER, SRCLK and the RCLK.

# You can rename all these variables to any names you wish,
# but keep in mind that you must also rename any variables
# in your program as well. Click the Find and Replace command
# on the IDLE menu to make any renaming changes faster to cover
# any variables you want to rename. However, you should stick
# to meaningful names, so other programmers can learn and
# understand what's happening throughout the program's
# execution/run.

SER = 15
SRCLK = 11
RCLK = 13

# SER (Serial Data Input)
# SRCLK (Shift Register Clock)
# RCLK (Register Clock/Latch)

# Change the SER to a 1 for on and a 0 for off.

# SER lets the data come in.
# SRCLK seats the data
# RCLK opens the latch to release the data

control_shift = SER,SRCLK,RCLK

for i in control_shift:GPIO.setup(i,GPIO.OUT)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
msb = 65_535,65_536
lsb = 32_767,32_768

led_speed = 0.0000006,.08,1

beep_on = '''
GPIO.output(active_buzz_pin,1)
'''
beep_off = '''
GPIO.output(active_buzz_pin,0)
'''
stop_program_message = '''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(16):
    GPIO.output(SER,0)
    GPIO.output(SRCLK,1)
    wait(led_speed[0])
    GPIO.output(SRCLK,0)
GPIO.output(RCLK,1)
wait(led_speed[0])
GPIO.output(RCLK,0)

display.lcd_backlight(1)

def passive_buzz1():

    for i in range(1,45):
        passive_buzzer1.start(50)
        randfreq = random.randint(1,1000)
        passive_buzzer1.ChangeFrequency(randfreq)
        wait(.1)
        randfreq = random.randint(1,1000)
        passive_buzzer1.ChangeFrequency(randfreq)
        wait(.2)

        passive_buzzer1.stop(50)
        wait(.001)

def passive_buzz2():

    for i in range(1,45):
        passive_buzzer2.start(50)
        randfreq = random.randint(1,2000)
        passive_buzzer2.ChangeFrequency(randfreq)
        wait(.1)
        randfreq = random.randint(1,2000)
        passive_buzzer2.ChangeFrequency(randfreq)
        wait(.2)

        passive_buzzer2.stop(50)
        wait(.001)

def led_show():
    for i in leds:
        for j in range(16):
            GPIO.output(SER,int(i[j]))
            GPIO.output(SRCLK,1)
            wait(led_speed[0])
            GPIO.output(SRCLK,0)
        GPIO.output(RCLK,1)
        wait(led_speed[0])
        GPIO.output(RCLK,0)
        wait(led_speed[1])

    for x in range(135):
        for i in runners:
            for j in range(16):
                GPIO.output(SER,int(i[j]))
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
            GPIO.output(RCLK,1)
            wait(led_speed[0])
            GPIO.output(RCLK,0)
            wait(led_speed[1])

    for i in range(16):
        GPIO.output(SER,0)
        GPIO.output(SRCLK,1)
        wait(led_speed[0])
        GPIO.output(SRCLK,0)
    GPIO.output(RCLK,1)
    wait(led_speed[0])
    GPIO.output(RCLK,0)

a = threading.Thread(target = passive_buzz1,daemon = True)
b = threading.Thread(target = passive_buzz2,daemon = True)
c = threading.Thread(target = led_show,daemon = True)

c.start()

title1 = ('<<<<<<<JCR>>>>>>')
text1 = ('JOSHUA.COMPUTERS.READ/INFORMATION ',
        'Serious Computing for Curious Minds... ')

title2 = ('A Dedication to:')
text2 = ('My Mom: Joan Mary. Daniels ',
         'My Brother: James Harold. Richardson ',
         'My friend: Brian Di Pierro ',
         'LEECRAFT Communications Devices ',
         'To those, who made me who I am today... ')

breach = 'DREADNAUGHT BREACH:'
DREADNAUGHT_error = 'ERROR: Critical'
bin_heap = 'Binary Heap 401'
override = 'Error Override:'
DREADNAUGHT = 'DREADNAUGHT SYST'
online = 'DREADNAUGHT ONLN'
active = 'DREADNAUGHT ACT!'
protocol = 'Act Protocol:'
selfaware = '  Self aware!!'
welcome = '  DREADNAUGHT  '
fear_not = 'FEAR NOT PROJECT'

values = (
    breach,DREADNAUGHT_error,
    bin_heap,override,
    DREADNAUGHT,online,active)

for x in range(2):
    print(title1,'\n',text1[x])
    display_text(title1,1)
    display_text(text1[x],2)
    wait(1)
    for i in range(len(text1[x])):
        display_text(text1[x][i:i+16],2)
        wait(0.2)

for x in range(5):
    print(title2,'\n',text2[x])
    display_text(title2,1)
    display_text(text2[x],2)
    wait(1)
    for i in range(len(text2[x])):
        display_text(text2[x][i:i+16],2)
        wait(0.2)

a.start()
b.start()

for x in values:
    randwait = random.randint(0,1)
    display.lcd_clear()
    display.lcd_backlight(1)
    print(x)
    display_text(x,1)
    wait(randwait)
    display.lcd_backlight(0)
    wait(randwait)

for i in range(3):
    display.lcd_clear()
    display.lcd_backlight(1)
    wait(1)
    print(protocol,'\n',selfaware)
    display_text(protocol,1)
    display_text(selfaware,2)
    wait(1)

display.lcd_clear()
display_text(welcome,1)
display_text(fear_not,2)
wait(3)
display.lcd_clear()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def binary_bits_default():

    for i in range(16):
        GPIO.output(SER,0)
        GPIO.output(SRCLK,1)
        wait(led_speed[0])
        GPIO.output(SRCLK,0)
    GPIO.output(RCLK,1)
    wait(led_speed[0])
    GPIO.output(RCLK,0)

    try:
        for i in range(msb[0],lsb[0],-1):
            bin = f'{i:b}'
            display_text(f'{msb[0]-i:016b}',1)
            display_text(str(len(f'{msb[0]-i:b}'))+f' BITS = +{msb[0]-i}',2)
            print('\n'+str(len(f'{msb[0]-i:b}')),
                  f'bits = Bin: {msb[0]-i:016b} =\n\n'
                  f'Hex: +{msb[0]-i:X}\n'
                  f'Oct: +{msb[0]-i:o}\n'
                  f'Dec: +{msb[0]-i:,}')
            for j in range(16):
                exec(beep_on)
                GPIO.output(SER,int(bin[j])-1)
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
            GPIO.output(RCLK,1)
            wait(led_speed[0])
            GPIO.output(RCLK,0)
            exec(beep_off)
            wait(led_speed[2])

        for i in range(lsb[1],msb[1]):
            bin = f'{i:b}'
            display_text(f'{i:016b}',1)
            display_text(str(len(f'{msb[0]:b}'))+f' BITS = +{i}',2)
            print('\n'+str(len(f'{msb[0]:b}')),
                  f'bits = Bin: {i:016b} =\n\n'
                  f'Hex: +{i:X}\n'
                  f'Oct: +{i:o}\n'
                  f'Dec: +{i:,}')
            for j in range(16):
                exec(beep_on)
                GPIO.output(SER,int(bin[j]))
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
            GPIO.output(RCLK,1)
            wait(led_speed[0])
            GPIO.output(RCLK,0)
            exec(beep_off)
            wait(led_speed[2])

    except KeyboardInterrupt:
        exec(stop_program_message)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def binary_bits_inverse():

    for i in range(16):
        GPIO.output(SER,0)
        GPIO.output(SRCLK,1)
        wait(led_speed[0])
        GPIO.output(SRCLK,0)
    GPIO.output(RCLK,1)
    wait(led_speed[0])
    GPIO.output(RCLK,0)

    try:
        for i in range(msb[0],lsb[0],-1):
            bin = f'{i:b}'
            display_text(f'{(i & 0xffff):016b}',1)
            display_text(str(len(f'{msb[0]-i:b}'))+f' BITS = -{msb[0]-i}',2)
            print('\n'+str(len(f'{msb[0]-i:b}')),
                  f'bits = Bin: {(i & 0xffff):016b} =\n\n'
                  f'Hex: -{msb[0]-i:X}\n'
                  f'Oct: -{msb[0]-i:o}\n'
                  f'Dec: -{msb[0]-i:,}')
            for j in range(16):
                exec(beep_on)
                GPIO.output(SER,int(bin[j]))
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
            GPIO.output(RCLK,1)
            wait(led_speed[0])
            GPIO.output(RCLK,0)
            exec(beep_off)
            wait(led_speed[2])

        for i in range(lsb[1],msb[1]):
            bin = f'{i:b}'
            display_text(f'{(i & 0xffff):016b}',1)
            display_text(str(len(f'{msb[0]:b}'))+f' BITS = -{i}',2)
            print('\n'+str(len(f'{msb[0]:b}')),
                  f'bits = Bin: {(i & 0xffff):016b} =\n\n'
                  f'Hex: -{i:X}\n'
                  f'Oct: -{i:o}\n'
                  f'Dec: -{i:,}')
            for j in range(16):
                exec(beep_on)
                GPIO.output(SER,int(bin[j])-1)
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
            GPIO.output(RCLK,1)
            wait(led_speed[0])
            GPIO.output(RCLK,0)
            exec(beep_off)
            wait(led_speed[2])

    except KeyboardInterrupt:
        exec(stop_program_message)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def binary_bits_mirror():

    for i in range(16):
        GPIO.output(SER,0)
        GPIO.output(SRCLK,1)
        wait(led_speed[0])
        GPIO.output(SRCLK,0)
    GPIO.output(RCLK,1)
    wait(led_speed[0])
    GPIO.output(RCLK,0)

    try:
        for i in range(msb[0],lsb[0],-1):
            bin = f'{i:b}'
            rev = f'{msb[0]-i:016b}'[::-1]
            display_text(f'{rev}',1)
            display_text(str(len(f'{msb[0]-i:b}'))+f' BITS = +{msb[0]-i}',2)
            print('\n'+str(len(f'{msb[0]-i:b}')),
                  f'bits = Bin: {rev} =\n\n'
                  f'Hex: +{msb[0]-i:X}\n'
                  f'Oct: +{msb[0]-i:o}\n'
                  f'Dec: +{msb[0]-i:,}')
            for j in range(15,-1,-1):
                exec(beep_on)
                GPIO.output(SER,int(bin[j])-1)
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
            GPIO.output(RCLK,1)
            wait(led_speed[0])
            GPIO.output(RCLK,0)
            exec(beep_off)
            wait(led_speed[2])

        for i in range(lsb[1],msb[1]):
            bin = f'{i:b}'
            rev = f'{i:016b}'[::-1]
            display_text(f'{rev}',1)
            display_text(str(len(f'{msb[0]:b}'))+f' BITS = +{i}',2)
            print('\n'+str(len(f'{msb[0]:b}')),
                  f'bits = Bin: {rev} =\n\n'
                  f'Hex: +{i:X}\n'
                  f'Oct: +{i:o}\n'
                  f'Dec: +{i:,}')
            for j in range(15,-1,-1):
                exec(beep_on)
                GPIO.output(SER,int(bin[j]))
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
            GPIO.output(RCLK,1)
            wait(led_speed[0])
            GPIO.output(RCLK,0)
            exec(beep_off)
            wait(led_speed[2])

    except KeyboardInterrupt:
        exec(stop_program_message)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def binary_bits_mirror_inverse():

    for i in range(16):
        GPIO.output(SER,0)
        GPIO.output(SRCLK,1)
        wait(led_speed[0])
        GPIO.output(SRCLK,0)
    GPIO.output(RCLK,1)
    wait(led_speed[0])
    GPIO.output(RCLK,0)

    try:
        for i in range(msb[0],lsb[0],-1):
            bin = f'{i:b}'
            rev = f'{(i & 0xffff):016b}'[::-1]
            display_text(f'{rev}',1)
            display_text(str(len(f'{msb[0]-i:b}'))+f' BITS = -{msb[0]-i}',2)
            print('\n'+str(len(f'{msb[0]-i:b}')),
                  f'bits = Bin: {rev} =\n\n'
                  f'Hex: -{msb[0]-i:X}\n'
                  f'Oct: -{msb[0]-i:o}\n'
                  f'Dec: -{msb[0]-i:,}')
            for j in range(15,-1,-1):
                exec(beep_on)
                GPIO.output(SER,int(bin[j]))
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
            GPIO.output(RCLK,1)
            wait(led_speed[0])
            GPIO.output(RCLK,0)
            exec(beep_off)
            wait(led_speed[2])

        for i in range(lsb[1],msb[1]):
            bin = f'{i:b}'
            rev = f'{(i & 0xffff):016b}'[::-1]
            display_text(f'{rev}',1)
            display_text(str(len(f'{msb[0]:b}'))+f' BITS = -{i}',2)
            print('\n'+str(len(f'{msb[0]:b}')),
                  f'bits = Bin: {rev} =\n\n'
                  f'Hex: -{i:X}\n'
                  f'Oct: -{i:o}\n'
                  f'Dec: -{i:,}')
            for j in range(15,-1,-1):
                exec(beep_on)
                GPIO.output(SER,int(bin[j])-1)
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
            GPIO.output(RCLK,1)
            wait(led_speed[0])
            GPIO.output(RCLK,0)
            exec(beep_off)
            wait(led_speed[2])

    except KeyboardInterrupt:
        exec(stop_program_message)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def binary_bits_flow_default():

    for i in range(16):
        GPIO.output(SER,0)
        GPIO.output(SRCLK,1)
        wait(led_speed[0])
        GPIO.output(SRCLK,0)
    GPIO.output(RCLK,1)
    wait(led_speed[0])
    GPIO.output(RCLK,0)

    try:
        for i in range(msb[0],lsb[0],-1):
            bin = f'{i:b}'
            display_text(f'{msb[0]-i:016b}',1)
            display_text(str(len(f'{msb[0]-i:b}'))+f' BITS = +{msb[0]-i}',2)
            print('\n'+str(len(f'{msb[0]-i:b}')),
                  f'bits = Bin: {msb[0]-i:016b} =\n\n'
                  f'Hex: +{msb[0]-i:X}\n'
                  f'Oct: +{msb[0]-i:o}\n'
                  f'Dec: +{msb[0]-i:,}')
            for j in range(16):
                exec(beep_off)
                GPIO.output(SER,int(bin[j])-1)
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
                GPIO.output(RCLK,1)
                wait(led_speed[0])
                GPIO.output(RCLK,0)
                exec(beep_off)
                wait(led_speed[1])

        for i in range(lsb[1],msb[1]):
            bin = f'{i:016b}'
            display_text(f'{msb[0]:b}',1)
            display_text(str(len(f'{msb[0]:b}'))+f' BITS = +{i}',2)
            print('\n'+str(len(f'{msb[0]:b}')),
                  f'bits = Bin: {i:016b} =\n\n'
                  f'Hex: +{i:X}\n'
                  f'Oct: +{i:o}\n'
                  f'Dec: +{i:,}')
            for j in range(16):
                exec(beep_off)
                GPIO.output(SER,int(bin[j]))
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
                GPIO.output(RCLK,1)
                wait(led_speed[0])
                GPIO.output(RCLK,0)
                exec(beep_off)
                wait(led_speed[1])

    except KeyboardInterrupt:
        exec(stop_program_message)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def binary_bits_flow_default_inverse():

    for i in range(16):
        GPIO.output(SER,0)
        GPIO.output(SRCLK,1)
        wait(led_speed[0])
        GPIO.output(SRCLK,0)
    GPIO.output(RCLK,1)
    wait(led_speed[0])
    GPIO.output(RCLK,0)

    try:
        for i in range(msb[0],lsb[0],-1):
            bin = f'{i:b}'
            display_text(f'{(i & 0xffff):016b}',1)
            display_text(str(len(f'{msb[0]-i:b}'))+f' BITS = -{msb[0]-i}',2)
            print('\n'+str(len(f'{msb[0]-i:b}')),
                  f'bits = Bin: {(i & 0xffff):016b} =\n\n'
                  f'Hex: -{msb[0]-i:X}\n'
                  f'Oct: -{msb[0]-i:o}\n'
                  f'Dec: -{msb[0]-i:,}')
            for j in range(16):
                exec(beep_off)
                GPIO.output(SER,int(bin[j]))
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
                GPIO.output(RCLK,1)
                wait(led_speed[0])
                GPIO.output(RCLK,0)
                exec(beep_off)
                wait(led_speed[1])

        for i in range(lsb[1],msb[1]):
            bin = f'{i:b}'
            display_text(f'{(i & 0xffff):016b}',1)
            display_text(str(len(f'{msb[0]:b}'))+f' BITS = -{i}',2)
            print('\n'+str(len(f'{msb[0]:b}')),
                  f'bits = Bin: {(i & 0xffff):016b} =\n\n'
                  f'Hex: -{i:X}\n'
                  f'Oct: -{i:o}\n'
                  f'Dec: -{i:,}')
            for j in range(16):
                exec(beep_off)
                GPIO.output(SER,int(bin[j])-1)
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
                GPIO.output(RCLK,1)
                wait(led_speed[0])
                GPIO.output(RCLK,0)
                exec(beep_off)
                wait(led_speed[1])

    except KeyboardInterrupt:
        exec(stop_program_message)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
binary_bits_trix = [
    binary_bits_default,
    binary_bits_inverse,
    binary_bits_mirror,
    binary_bits_mirror_inverse,
    binary_bits_flow_default,
    binary_bits_flow_default_inverse]

# Create an IndexError handler to
# cut off the buzzers, should you call
# an index value higher than [5].

# Note: index values always start at index zero
# not index one. Keep this in mind, should you
# accidentally call an index value higher than
# the index range.

try:
    binary_bits_trix[0]()
except IndexError:
    print('index value exceeds index range limit')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# When testing only, turn SER off = 0 to keep all the GPIO pins
# in the off state. Once your masterpiece is created, you can
# turn SER on = 1 to watch your masterpiece stay lit up after
# it counts all the way up to 65535. Good luck if you can watch
# it all. Because it's going to take quite a long time to watch it
# count. It takes a whole twenty one hours to count to the
# sixteen bit number, 65535. However, this makes for a great
# conversational piece while it's running for others to gaze at
# and see how a real computer works far behind the scenes of
# what a computer truly is. It's pure science. Not mystical magic...

# Please note: Some floating bits/LEDs will remain on, when
# pressing ctrl+c The 74HC595 shift registers do not shut down
# some of the LEDs, due to a value of 1, which gets caught in the
# resulting on state, while some other LEDs remain caught in the
# resulting off state. However, once you unleash your masterpiece,
# all the LEDs will turn on and stay on, once the counter reaches
# 1111111111111111 = FFFF = human decimal system value 65535.

for i in range(16):
    GPIO.output(SER,1)  # When testing only, turn SER off = 0
    GPIO.output(SRCLK,1)
    wait(led_speed[0])
    GPIO.output(SRCLK,0)
GPIO.output(RCLK,1)
wait(led_speed[0])
GPIO.output(RCLK,0)

input()  # Press Enter to exit this Raspberry pi 4 Python program

display.lcd_clear()
display.lcd_backlight(0)

# Create a while loop to keep floating bits/LEDs in the off, zero state.

while True:
    for i in range(16):
        GPIO.output(SER,0)
        GPIO.output(SRCLK,1)
        wait(led_speed[0])
        GPIO.output(SRCLK,0)
    GPIO.output(RCLK,1)
    wait(led_speed[0])
    GPIO.output(RCLK,0)

GPIO.cleanup() # GPI.cleanup() sets all GPIO pins to LOW/OFF state
