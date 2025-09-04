import board
import digitalio
import neopixel
import time

button = digitalio.DigitalInOut(board.GP0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

pixels = neopixel.NeoPixel(board.GP14, 2, brightness=0.2)

color_on = (0, 255, 0)
color_off = (0, 0, 0)
state = False
last_state = True
last_time = 0

while True:
    now = time.monotonic()
    if not button.value and last_state and (now - last_time > 0.25):
        state = not state
        pixels[0] = color_on if state else color_off
        last_time = now
    last_state = button.value
    time.sleep(0.01)
