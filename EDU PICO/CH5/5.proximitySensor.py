import board
import busio
import neopixel
from adafruit_apds9960.apds9960 import APDS9960

i2c = busio.I2C(board.GP5, board.GP4)
apds = APDS9960(i2c)
pixel = neopixel.NeoPixel(board.GP14, 5, brightness=0.3)
apds.enable_proximity = True

while True:
    proximity = apds.proximity
    print("Proximity:", proximity)

    if proximity == 0:
        pixel[0] = (0, 0, 0)
        pixel[1] = (0, 0, 0)
        pixel[2] = (0, 0, 0)
        pixel[3] = (0, 0, 0)
        pixel[4] = (0, 0, 0)
    elif proximity < 51:
        pixel[0] = (0, 255, 0)
        pixel[1] = (0, 0, 0)
        pixel[2] = (0, 0, 0)
        pixel[3] = (0, 0, 0)
        pixel[4] = (0, 0, 0)
    elif proximity < 102:
        pixel[0] = (128, 255, 0)
        pixel[1] = (128, 255, 0)
        pixel[2] = (0, 0, 0)
        pixel[3] = (0, 0, 0)
        pixel[4] = (0, 0, 0)
    elif proximity < 153:
        pixel[0] = (255, 255, 0)
        pixel[1] = (255, 255, 0)
        pixel[2] = (255, 255, 0)
        pixel[3] = (0, 0, 0)
        pixel[4] = (0, 0, 0)
    elif proximity < 204:
        pixel[0] = (255, 128, 0)
        pixel[1] = (255, 128, 0)
        pixel[2] = (255, 128, 0)
        pixel[3] = (255, 128, 0)
        pixel[4] = (0, 0, 0)
    elif proximity < 255:
        pixel[0] = (255, 0, 0)
        pixel[1] = (255, 0, 0)
        pixel[2] = (255, 0, 0)
        pixel[3] = (255, 0, 0)
        pixel[4] = (255, 0, 0)
