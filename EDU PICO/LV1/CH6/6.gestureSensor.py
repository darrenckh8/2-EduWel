import board
import busio
from adafruit_apds9960.apds9960 import APDS9960
import neopixel
import time

i2c = busio.I2C(board.GP5, board.GP4)
apds = APDS9960(i2c)
apds.enable_gesture = True
apds.enable_proximity = True

num_pixels = 1
pixel_pin = board.GP14
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)

forward_count = 0
backward_count = 0
left_count = 0
right_count = 0

while True:
    gesture_value = apds.gesture()
    
    if gesture_value == 1:
        forward_count += 1
        print(f"The plane moves forward (Forward count: {forward_count})")
        pixels.fill((0, 255, 0))
        time.sleep(1)
        
    elif gesture_value == 2:
        backward_count += 1
        print(f"The plane moves backward (Backward count: {backward_count})")
        pixels.fill((255, 0, 0))
        time.sleep(1)
        
    elif gesture_value == 3:
        left_count += 1
        print(f"The plane turned left (Left count: {left_count})")
        pixels.fill((0, 0, 255))
        time.sleep(1)
        
    elif gesture_value == 4:
        right_count += 1
        print(f"The plane turned right (Right count: {right_count})")
        pixels.fill((255, 255, 0))
        time.sleep(1)
        
    pixels.fill((0, 0, 0))
