import board #allows us to use the pins on the board
import busio #allows us to use the I2C protocol
import time #allows us to use the sleep function
import adafruit_ssd1306 #allows us to use the OLED display

i2c = busio.I2C(board.GP5, board.GP4) #create an I2C object
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c) #create an OLED object

oled.fill(0) #clear the display
oled.invert(True) #invert the display
oled.text("Hello,world", 40, 20, 1) #display text
oled.text("How are you?", 40, 35, 1) #display text
oled.show() #update the display