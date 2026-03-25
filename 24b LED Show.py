import RPi.GPIO as GPIO,random
from LED_Show_Strings_Only import*
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

SER = 15
RCLK = 13
SRCLK = 11

led_speed = 0.0000001,0.05,1  # pause duration

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')
'''
control_shift = SER,RCLK,SRCLK

for i in control_shift:GPIO.setup(i,GPIO.OUT) # setup desired GPIO pinouts

for i in range(24):
    GPIO.output(SER,0)
    GPIO.output(SRCLK,1)
    wait(led_speed[0])
    GPIO.output(SRCLK,0)
GPIO.output(RCLK,1)
wait(led_speed[0])
GPIO.output(RCLK,0)

def LED_intro():
    
    for i in led_intro:        
        for j in range(24):
            GPIO.output(SER,int(i[j]))
            GPIO.output(SRCLK,1)
            wait(led_speed[0])
            GPIO.output(SRCLK,0)
        GPIO.output(RCLK,1)
        wait(led_speed[0])
        GPIO.output(RCLK,0)
        wait(led_speed[2])
        
def LED_show():
    
    for i in led_show:
        for j in range(24):
            GPIO.output(SER,int(i[j]))
            GPIO.output(SRCLK,1)
            wait(led_speed[0])
            GPIO.output(SRCLK,0)
        GPIO.output(RCLK,1)
        wait(led_speed[0])
        GPIO.output(RCLK,0)
        wait(led_speed[1])

def LED_show_reverse():
    
    led_show.reverse()       
    for i in led_show:
        for j in range(24):               
            GPIO.output(SER,int(i[j])-1)
            GPIO.output(SRCLK,1)
            wait(led_speed[0])
            GPIO.output(SRCLK,0)
        GPIO.output(RCLK,1)
        wait(led_speed[0])
        GPIO.output(RCLK,0)
        wait(led_speed[1])
        
def LED_show_random():
    
    for i in range(100):
        for j in range(24):
            randvalue = random.randint(0,1)
            GPIO.output(SER,randvalue)
            GPIO.output(SRCLK,1)
            wait(led_speed[0])
            GPIO.output(SRCLK,0)
        GPIO.output(RCLK,1)
        wait(led_speed[0])
        GPIO.output(RCLK,0)
        wait(led_speed[1])
        
def LED_show_flow_random():
    
    for i in range(5):
        for j in range(24):
            randvalue = random.randint(0,1)
            GPIO.output(SER,randvalue)
            GPIO.output(SRCLK,1)
            wait(led_speed[0])
            GPIO.output(SRCLK,0)
            GPIO.output(RCLK,1)
            wait(led_speed[0])
            GPIO.output(RCLK,0)
            wait(led_speed[1])
            
def LED_flicker_flasher1():
    
    for x in range(10):
        for i in flicker_flash:
            for j in range(24):               
                GPIO.output(SER,int(i[j]))
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
            GPIO.output(RCLK,1)
            wait(led_speed[0])
            GPIO.output(RCLK,0)
            wait(led_speed[1])
            
def LED_flicker_flasher2():
    
    for x in range(10):
        for i in flicker_flash:
            for j in range(24):               
                GPIO.output(SER,int(i[j]))
                GPIO.output(SRCLK,1)
                wait(led_speed[0])
                GPIO.output(SRCLK,0)
            GPIO.output(RCLK,1)
            wait(led_speed[0])
            GPIO.output(RCLK,0)
            wait(led_speed[1])
            
def the_end():
    
    for i in led_intro:
        for j in range(24):
            GPIO.output(SER,int(i[j])-1)
            GPIO.output(SRCLK,1)
            wait(led_speed[0])
            GPIO.output(SRCLK,0)
        GPIO.output(RCLK,1)
        wait(led_speed[0])
        GPIO.output(RCLK,0)
        wait(led_speed[2])
        
led_functions = (
    LED_intro,
    LED_flicker_flasher1,
    LED_show,
    LED_show_reverse,
    LED_show_random,
    LED_show_flow_random,
    LED_flicker_flasher2,
    the_end)

for i in led_functions:i()

for i in range(24):
    GPIO.output(SER,0)
    GPIO.output(SRCLK,1)
    wait(led_speed[0])
    GPIO.output(SRCLK,0)
GPIO.output(RCLK,1)
wait(led_speed[0])
GPIO.output(RCLK,0)

GPIO.cleanup()  # # GPI.cleanup() sets all GPIO pins to LOW/OFF state
