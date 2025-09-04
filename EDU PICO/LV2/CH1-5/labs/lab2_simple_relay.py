import board
import digitalio
import time

button = digitalio.DigitalInOut(board.GP0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

relay = digitalio.DigitalInOut(board.GP22)
relay.direction = digitalio.Direction.OUTPUT

relay_on = False
last_state = True
last_time = 0

while True:
    now = time.monotonic()
    if not button.value and last_state and (now - last_time > 0.25):
        relay_on = not relay_on
        relay.value = relay_on
        print("Relay is now", "ON" if relay_on else "OFF")
        last_time = now
    last_state = button.value
    time.sleep(0.01)
