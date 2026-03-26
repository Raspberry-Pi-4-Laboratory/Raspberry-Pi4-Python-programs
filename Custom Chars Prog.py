import drivers
from time import sleep

display = drivers.Lcd()

c = drivers.CustomCharacters(display)

c.char_1_data = ['11111',
                  '00100',
                  '00100',
                  '00100',
                  '00100',
                  '00100',
                  '10100',
                  '11100']

c.char_2_data = ['11111',
                  '10001',
                  '10000',
                  '10000',
                  '10000',
                  '10000',
                  '10001',
                  '11111']

c.char_3_data = ['11111',
                  '10001',
                  '10001',
                  '11111',
                  '11000',
                  '10100',
                  '10010',
                  '10001']

c.load_custom_characters_data()
display.lcd_display_extended_string(
'     {0x00}{0x01}{0x02}',1)
