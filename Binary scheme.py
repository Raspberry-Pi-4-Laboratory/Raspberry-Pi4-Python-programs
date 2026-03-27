
# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

latch=35
data_bit=37
clock=33
''''''''''''''''''''''''''''''''''''''''''
control_shift=data_bit,latch,clock

for i in control_shift:
    GPIO.setup(i,GPIO.OUT)

for i in range(24):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)    
   
for i in range(16777215,8388607,-1):                                   
    for j in range(24):
        GPIO.output(latch,0)
        GPIO.output(data_bit,int(f'{i:b}'[j])-1)
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    time.sleep(.5)         

for i in range(8388608,16777216):                        
    for j in range(24):
        GPIO.output(latch,0)
        GPIO.output(data_bit,int(f'{i:b}'[j]))
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    time.sleep(.5)
    
for i in range(24):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
    
GPIO.cleanup()