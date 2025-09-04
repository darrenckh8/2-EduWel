import board
import busio
import adafruit_ssd1306
import time

i2c = busio.I2C(board.GP5, board.GP4)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

menu_items = ['Relay', 'DC Motor']
selected_index = 0
relay_on = False
motor_on = False

while True:
    oled.fill(0)
    oled.text("Smart Home Panel", 10, 0, 1)
    for i, item in enumerate(menu_items):
        prefix = '>' if i == selected_index else ' '
        state = 'ON' if (relay_on if i == 0 else motor_on) else 'OFF'
        oled.text(f"{prefix} {item}: {state}", 0, 15 + i*15, 1)
    oled.show()
    time.sleep(0.5)
