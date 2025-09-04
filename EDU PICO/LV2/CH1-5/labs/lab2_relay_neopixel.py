import board
import digitalio
import neopixel
import time

def setup_button(pin):
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    return btn

button_toggle = setup_button(board.GP1)
relay = digitalio.DigitalInOut(board.GP22)
relay.direction = digitalio.Direction.OUTPUT
pixels = neopixel.NeoPixel(board.GP14, 2, brightness=0.2)

relay_on = False
last_button_toggle, last_toggle_time = True, 0

while True:
    now = time.monotonic()
    if not button_toggle.value and last_button_toggle and (now - last_toggle_time > 0.25):
        relay_on = not relay_on
        relay.value = relay_on
        pixels[0] = (0, 255, 0) if relay_on else (0, 0, 0)
        print("Relay is now", "ON" if relay_on else "OFF")
        last_toggle_time = now
    last_button_toggle = button_toggle.value
    time.sleep(0.01)
