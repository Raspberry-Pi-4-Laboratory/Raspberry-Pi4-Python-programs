
# Two Row Sixteen Character LCD Display Input Setup

# black wire = GND
# red wire = VCC (3.3V)
# yellow wire = SCL (Clock Pulse)
# blue wire = SDA (Data Stream)

import RPi.GPIO as GPIO
import drivers

GPIO.setmode(GPIO.BOARD)  # breadboard method
GPIO.setwarnings(False)  # disable setwarnings
display = drivers.Lcd()  # enable the LCD display

display.lcd_clear() # clear the LCD screen
display.lcd_display_string(title,1)

display.lcd_display_string('Print text strings in row one.',1)
display.lcd_display_string('Print text strings in row two.',2)

try:
  pass
except KeyboardInterrupt:
  display.lcd_clear()
  display.lcd_backlight(0)
  GPIO.cleanup()  # GPIO.cleanup() sets all GPIO pins to LOW/OFF
