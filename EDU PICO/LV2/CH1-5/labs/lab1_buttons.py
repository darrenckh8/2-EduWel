import board
import digitalio
import time

def setup_button(pin):
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    return btn

button_sel = setup_button(board.GP0)
button_toggle = setup_button(board.GP1)

menu_items = ['Relay', 'DC Motor']
selected_index = 0
last_button_sel, last_sel_time = True, 0
last_button_toggle, last_toggle_time = True, 0

while True:
    now = time.monotonic()
    # Selection button
    if not button_sel.value and last_button_sel and (now - last_sel_time > 0.25):
        selected_index = (selected_index + 1) % len(menu_items)
        print("Selected:", menu_items[selected_index])
        last_sel_time = now
    last_button_sel = button_sel.value

    # Toggle button
    if not button_toggle.value and last_button_toggle and (now - last_toggle_time > 0.25):
        print("Toggled:", menu_items[selected_index])
        last_toggle_time = now
    last_button_toggle = button_toggle.value

    time.sleep(0.01)
