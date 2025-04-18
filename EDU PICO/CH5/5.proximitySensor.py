import board  # Helps us refer to the correct pins on the board.
import time  # Used to pause the program for a short time.
import busio  # Allows us to interact with the I2C bus.
import neopixel

# Allows us to interact with the APDS9960 sensor.
from adafruit_apds9960.apds9960 import APDS9960

# Create a variable called i2c that represents the I2C bus connected to pins 5 and 4.
i2c = busio.I2C(board.GP5, board.GP4)
# Create a variable called apds that represents the APDS9960 sensor connected to the I2C bus.
apds = APDS9960(i2c)
pixel = neopixel.NeoPixel(board.GP14, 5, brightness=0.5)
# Enable proximity detection on the APDS9960 sensor.
apds.enable_proximity = True

while True:  # Create an infinite loop that will run forever.
    # Read the proximity data from the APDS9960 sensor.
    proximity = apds.proximity
    print("Proximity:", proximity)  # Print the proximity data to the console.

    if proximity == 0:
        pixel[0] = (0, 0, 0)
        pixel[1] = (0, 0, 0)
        pixel[2] = (0, 0, 0)
        pixel[3] = (0, 0, 0)
        pixel[4] = (0, 0, 0)
    elif proximity < 51:
        pixel[0] = (255, 0, 0)
        pixel[1] = (0, 0, 0)
        pixel[2] = (0, 0, 0)
        pixel[3] = (0, 0, 0)
        pixel[4] = (0, 0, 0)

    elif proximity < 102:
        pixel[0] = (255, 0, 0)
        pixel[1] = (255, 0, 0)
        pixel[2] = (0, 0, 0)
        pixel[3] = (0, 0, 0)
        pixel[4] = (0, 0, 0)

    elif proximity < 153:
        pixel[0] = (255, 0, 0)
        pixel[1] = (255, 0, 0)
        pixel[2] = (255, 0, 0)
        pixel[3] = (0, 0, 0)
        pixel[4] = (0, 0, 0)

    elif proximity < 204:
        pixel[0] = (255, 0, 0)
        pixel[1] = (255, 0, 0)
        pixel[2] = (255, 0, 0)
        pixel[3] = (255, 0, 0)
        pixel[4] = (0, 0, 0)

    elif proximity < 255:
        pixel[0] = (255, 0, 0)
        pixel[1] = (255, 0, 0)
        pixel[2] = (255, 0, 0)
        pixel[3] = (255, 0, 0)
        pixel[4] = (255, 0, 0)

    time.sleep(0.8)  # Pause the program for 0.8 seconds.
