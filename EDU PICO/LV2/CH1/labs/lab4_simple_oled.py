import board
import busio
import adafruit_ssd1306
import time

i2c = busio.I2C(board.GP5, board.GP4)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

counter = 0
while True:
    oled.fill(0)
    oled.text("Hello OLED!", 0, 0, 1)
    oled.text(f"Counter: {counter}", 0, 20, 1)
    oled.show()
    counter += 1
    time.sleep(1)
