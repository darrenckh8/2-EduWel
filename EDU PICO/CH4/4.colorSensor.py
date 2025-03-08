import board  # Helps us refer to the correct pins on the board.                            
import time  # Used to pause the program for a short time.                                  
import busio  # Allows us to interact with the I2C bus.                                     
import neopixel  # Allows us to interact with the neopixel RGB LED.                         
# Allows us to interact with the APDS9960 sensor.                                           
from adafruit_apds9960.apds9960 import APDS9960                                             

num_pixels = 5  # Set the number of pixels to 5.
# Set the pin connected to the neopixel RGB LED to pin 14.
pixel_pin = board.GP14
# Create a variable called pixels that represents the neopixel RGB LED connected to pin 14.
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)

# Create a variable called i2c that represents the I2C bus connected to pins 5 and 4.
i2c = busio.I2C(board.GP5, board.GP4)
# Create a variable called apds that represents the APDS9960 sensor connected to the I2C bus.
apds = APDS9960(i2c)
apds.enable_color = True  # Enable color detection on the APDS9960 sensor.

while True:  # Create an infinite loop that will run forever.
    pixels.fill((255, 255, 255))
    # Read the color data from the APDS9960 sensor.
    r, g, b, c = apds.color_data
    # Print the color data to the console.
    print(f"red:{r},green:{g},blue: {b}, clear: {c}")
    if r > g and r > b:  # Check if the red value is greater than the green and blue values.
        print("Red Detected")
    elif g > r and g > b:  # Check if the green value is greater than the red and blue values.
        print("Green Detected")
    else:  # If the red and green values are not the highest.
        print("Blue Detected")
    time.sleep(1)  # Pause the program for 1 second.



    
