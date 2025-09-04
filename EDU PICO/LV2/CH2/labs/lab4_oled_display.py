import board
import busio
import adafruit_ssd1306
import adafruit_ahtx0
from adafruit_apds9960.apds9960 import APDS9960
import audiobusio
import array
import math
import time

i2c = busio.I2C(board.GP5, board.GP4)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
AHT_sensor = adafruit_ahtx0.AHTx0(i2c)
apds = APDS9960(i2c)
apds.enable_color = True
mic = audiobusio.PDMIn(board.GP3, board.GP2, sample_rate=16000, bit_depth=16)
samples = array.array('H', [0] * 1024)

def log10(x):
    return math.log(x) / math.log(10)

def normalized_rms(values):
    minbuf = sum(values) / len(values)
    samples_sum = sum(float(sample - minbuf) * (sample - minbuf) for sample in values)
    return math.sqrt(samples_sum / len(values))

while True:
    temperature = AHT_sensor.temperature
    humidity = AHT_sensor.relative_humidity
    r, g, b, c = apds.color_data
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    sound_level_dB = 20 * log10(magnitude) if magnitude > 0 else 0

    oled.fill(0)
    oled.text(f"Temp: {temperature:.1f}C", 0, 0, 1)
    oled.text(f"Hum: {humidity:.1f}%", 0, 12, 1)
    oled.text(f"Sound: {sound_level_dB:.1f}dB", 0, 24, 1)
    oled.text(f"Light: {c}", 0, 36, 1)
    oled.show()
    time.sleep(1)
