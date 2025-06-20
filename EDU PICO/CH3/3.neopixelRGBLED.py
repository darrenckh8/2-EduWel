import board
import time
import digitalio
from analogio import AnalogIn
import neopixel

# Setup for potentiometer (CH2)
pot = AnalogIn(board.GP28)

# Setup for button (CH1)
button = digitalio.DigitalInOut(board.GP0)  # Use GP0 for button
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Setup for NeoPixel RGB LED (CH3)
pixel_pin = board.GP14
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)

# State for color selection: 0=R, 1=G, 2=B
color_select = 0
color_names = ['Red', 'Green', 'Blue']
color = [0, 0, 0]

last_button = True

while True:
    # Read button (active low)
    current_button = button.value
    if not current_button and last_button:
        color_select = (color_select + 1) % 3  # Cycle R->G->B->R
        print(f"Selected: {color_names[color_select]}")
        time.sleep(0.2)  # Debounce
    last_button = current_button

    # Read potentiometer and scale to 0-255
    pot_value = int((pot.value * 255) / 65535)
    color[color_select] = pot_value

    # Set NeoPixel color
    pixels.fill(tuple(color))

    print(f"R: {color[0]}, G: {color[1]}, B: {color[2]} (Selected: {color_names[color_select]})")
    time.sleep(0.05)
