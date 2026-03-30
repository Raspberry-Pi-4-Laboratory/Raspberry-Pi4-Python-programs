# JCR-U2T6NL (Universal 2 Timer 0.0000006 Nanosecond  Latch)

# 74HC595 Shift Register Layout, complete with timings between the SRCLK and the RCLK latch.

import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BOARD)  # breadboard method
GPIO.setwarnings(False)  # disable setwarnings

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

for i in control_shift:GPIO.setup(i,GPIO.OUT)  # setup desired GPIO pinouts
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# One Byte, One 74HC595 Shift Register

msb = 255,256 # most significant bits
lsb = 127,128 # least significant bits

for i in range(8):
    GPIO.output(SER,1)  # Keep these line of code indented.
    GPIO.output(SRCLK,1)
    time.sleep(0.0000006)
    GPIO.output(SRCLK,0)
GPIO.output(RCLK,1)  # Keep these lines of code outer indented.
time.sleep(0.0000006)
GPIO.output(RCLK,0)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Two Bytes = One Word, Two 74HC595 Shift Registers

msb = 65_535,65_536 # most significant bits
lsb = 32_767,32_768 # least significant bits

for i in range(16):
    GPIO.output(SER,1)  # Keep these line of code indented.
    GPIO.output(SRCLK,1)
    time.sleep(0.0000006)
    GPIO.output(SRCLK,0)
GPIO.output(RCLK,1)  # Keep these lines of code outer indented.
time.sleep(0.0000006)
GPIO.output(RCLK,0)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Three Bytes = One Word and One Byte, Three 74HC595 Shift Registers

msb = 16_777_215,16_777_216  # most significant bits
lsb = 8_388_607,8_388_608  # least significant bits

for i in range(24):
    GPIO.output(SER,1)  # Keep these line of code indented.
    GPIO.output(SRCLK,1)
    time.sleep(0.0000006)
    GPIO.output(SRCLK,0)
GPIO.output(RCLK,1)  # Keep these lines of code outer indented.
time.sleep(0.0000006)
GPIO.output(RCLK,0)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Four Bytes = Two Words, Four 74HC595 Shift Registers

msb = 4294_967_295,4294_967_296  # most significant bits
lsb = 2147_483_647,2147_483_648  # least significant bits

for i in range(32):
    GPIO.output(SER,1)  # Keep these line of code indented.
    GPIO.output(SRCLK,1)
    time.sleep(0.0000006)
    GPIO.output(SRCLK,0)
GPIO.output(RCLK,1)  # Keep these lines of code outer indented.
time.sleep(0.0000006)
GPIO.output(RCLK,0)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Five Bytes = Two Words and One Byte, Five 74HC595 Shift Registers

msb = 10995_1162_7775,10995_1162_7776  # most significant bits
lsb = 5497_5581_3887,5497_5581_3888  # least significant bits

for i in range(40):
    GPIO.output(SER,1)  # Keep these line of code indented.
    GPIO.output(SRCLK,1)
    time.sleep(0.0000006)
    GPIO.output(SRCLK,0)
GPIO.output(RCLK,1)  # Keep these lines of code outer indented.
time.sleep(0.0000006)
GPIO.output(RCLK,0)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Six Bytes = 3 Words, Six 74HC595 Shift Registers

msb = 28147_49767_10655,28147_49767_10656  # most significant bits
lsb = 14073_74883_55327,14073_74883_55328  # least significant bits

for i in range(48):
    GPIO.output(SER,1)  # Keep these line of code indented.
    GPIO.output(SRCLK,1)
    time.sleep(0.0000006)
    GPIO.output(SRCLK,0)
GPIO.output(RCLK,1)  # Keep these lines of code outer indented.
time.sleep(0.0000006)
GPIO.output(RCLK,0)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Byte Calculation for 34HC595 Shift Registers.

shift_registers = 0,1,2,3,4,5,6  # default tuple

msb = int(pow(256,shift_registers[6]))
lsb = int(msb/2)
msb_lsb = f'{msb-1},{msb}\n{lsb-1},{lsb}'

print(msb_lsb)
