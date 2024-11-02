import board # Helps us refer to the correct pins on the board.                             
import time # Used to pause the program for a short time.                                    
import neopixel # Allows us to interact with the neopixel RGB LED.                           

num_pixels = 1 # Set the number of pixels to 1.
pixel_pin = board.GP14 # Set the pin connected to the neopixel RGB LED to pin 14.

# Create a variable called pixels that represents the neopixel RGB LED connected to pin 14.
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2) 

while True: # Create an infinite loop that will run forever.
    pixels.fill((255, 255, 255)) # Turn on the neopixel RGB LED to white.
    time.sleep(1) # Pause the program for 1 second.
    
