import board  # Helps us refer to the correct pins on the board.                                        #type: ignore
import busio  # Allows us to interact with the I2C bus.                                                 #type: ignore
from adafruit_apds9960.apds9960 import APDS9960 # Allows us to interact with the APDS9960 sensor.       #type: ignore
import neopixel  # Allows us to interact with the NeoPixel RGB LED.
import time  # Import time module to add delays.

i2c = busio.I2C(board.GP5, board.GP4) #setup I2C
apds = APDS9960(i2c) #setup the sensor
apds.enable_gesture = True #enable gesture
apds.enable_proximity = True #enable proximity

# Setup NeoPixel RGB LED
num_pixels = 1  # Set the number of pixels to 1.
pixel_pin = board.GP14  # Set the pin connected to the NeoPixel RGB LED to pin 14.
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)

while True:  # Create an infinite loop that will run forever.
    gesture_value = apds.gesture()  # Read the gesture data from the APDS9960 sensor.
    if gesture_value == 1:  # Check if the gesture is moving forward.
        print("The plane move forward")
        pixels.fill((0, 255, 0))  # Set NeoPixel to green.
        time.sleep(2)  # Keep the LED on for 2 seconds.
    elif gesture_value == 2:  # Check if the gesture is moving backward.
        print("The plane move backward")
        pixels.fill((255, 0, 0))  # Set NeoPixel to red.
        time.sleep(2)  # Keep the LED on for 2 seconds.
    elif gesture_value == 3:  # Check if the gesture is moving to the left.
        print("The plane turned to the left")
        pixels.fill((0, 0, 255))  # Set NeoPixel to blue.
        time.sleep(2)  # Keep the LED on for 2 seconds.
    elif gesture_value == 4:  # Check if the gesture is moving to the right.
        print("The plane turned to the right")
        pixels.fill((255, 255, 0))  # Set NeoPixel to yellow.
        time.sleep(2)  # Keep the LED on for 2 seconds.
    else:
        pixels.fill((0, 0, 0))  # Turn off NeoPixel if no gesture is detected.
