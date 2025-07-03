import board
import time
import digitalio
from analogio import AnalogIn
import neopixel

pot = AnalogIn(board.GP28)

button = digitalio.DigitalInOut(board.GP0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

pixel_pin = board.GP14
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)

color_select = 0
color_names = ['Red', 'Green', 'Blue']
color = [0, 0, 0]

last_button = True

while True:
    current_button = button.value
    if not current_button and last_button:
        color_select = (color_select + 1) % 3
        print(f"Selected: {color_names[color_select]}")
        time.sleep(0.2)
    last_button = current_button

    pot_value = int((pot.value * 255) / 65535)
    color[color_select] = pot_value

    pixels.fill(tuple(color))

    print(f"R: {color[0]}, G: {color[1]}, B: {color[2]} (Selected: {color_names[color_select]})")
    time.sleep(0.05)
