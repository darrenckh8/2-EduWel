import board
import digitalio
import time

button = digitalio.DigitalInOut(board.GP0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

last_state = True
last_time = 0

while True:
    now = time.monotonic()
    if not button.value and last_state and (now - last_time > 0.25):
        print("Button pressed!")
        last_time = now
    last_state = button.value
    time.sleep(0.01)
