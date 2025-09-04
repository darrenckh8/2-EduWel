import board
import busio
from adafruit_apds9960.apds9960 import APDS9960
import time

i2c = busio.I2C(board.GP5, board.GP4)
apds = APDS9960(i2c)
apds.enable_color = True

while True:
    r, g, b, c = apds.color_data
    print(f"Light Level (clear): {c}")
    time.sleep(1)
