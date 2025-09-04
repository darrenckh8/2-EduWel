import board, time, busio, digitalio, simpleio, math, array
import adafruit_ssd1306, adafruit_ahtx0
from analogio import AnalogIn
from adafruit_apds9960.apds9960 import APDS9960
import audiobusio

# ───── Setup ─────
i2c = busio.I2C(board.GP5, board.GP4)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
pot = AnalogIn(board.GP28)
buzzer_pin = board.GP21

# Buttons
button_A = digitalio.DigitalInOut(board.GP0)
button_B = digitalio.DigitalInOut(board.GP1)
for btn in (button_A, button_B):
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP

# Sensors
try:
    aht = adafruit_ahtx0.AHTx0(i2c)
except:
    aht = None
    print("AHT20 not found")

try:
    apds = APDS9960(i2c)
    apds.enable_color = True
    apds.enable_proximity = True
except:
    apds = None
    print("APDS9960 not found")

try:
    mic = audiobusio.PDMIn(board.GP3, board.GP2, sample_rate=16000, bit_depth=16)
    samples = array.array('H', [0] * 1024)
except:
    mic = None
    print("Microphone not found")

# ───── State ─────
screen_index = 0
last_button_time = 0
screens = ["Environment", "Proximity & Color", "Audio & Controls"]
data = {}

# ───── Utility Functions ─────
def log10(x): 
    return math.log(x) / math.log(10)

def buzz(freq=1000, dur=0.1): simpleio.tone(buzzer_pin, freq, dur)

def normalized_rms(values):
    minbuf = sum(values) / len(values)
    samples_sum = sum(float(sample - minbuf) * (sample - minbuf) for sample in values)
    return math.sqrt(samples_sum / len(values))

def check_button(button):
    global last_button_time
    now = time.monotonic()
    if not button.value and now - last_button_time > 0.1:
        last_button_time = now
        return True
    return False

def update_sensors():
    data["uptime"] = time.monotonic()
    data["pot"] = pot.value
    data["pot_pct"] = (pot.value / 65535) * 100
    data["temp"] = aht.temperature if aht else None
    data["humid"] = aht.relative_humidity if aht else None

    if apds:
        data["prox"] = apds.proximity
        r, g, b, c = apds.color_data
        data.update({"r": r, "g": g, "b": b, "c": c})
    else:
        data.update({"prox": None, "r": 0, "g": 0, "b": 0, "c": 0})

    if mic:
        try:
            mic.record(samples, len(samples))
            magnitude = normalized_rms(samples)
            if magnitude > 0:
                data["sound_db"] = 20 * log10(magnitude)
            else:
                data["sound_db"] = 0
        except Exception as e:
            print(f"Mic error: {e}")
            data["sound_db"] = 0
    else:
        data["sound_db"] = 0

def dominant_color():
    r, g, b = data["r"], data["g"], data["b"]
    return max(("Red", r), ("Green", g), ("Blue", b), key=lambda x: x[1])[0]

# ───── Screens ─────
def screen_env():
    oled.fill(0)
    oled.text("ENVIRONMENT", 20, 0, 1)
    oled.hline(0, 10, 128, 1)
    oled.text(f"Temp: {data['temp']:.1f}C" if aht else "Temp: N/A", 0, 15, 1)
    oled.text(f"Humidity: {data['humid']:.0f}%" if aht else "Humidity: N/A", 0, 25, 1)
    oled.text(f"Sound: {data['sound_db']:.0f}dB" if mic and data['sound_db'] is not None else "Sound: N/A", 0, 35, 1)
    oled.text(f"[1/3] A:Next B:Buzz", 0, 55, 1)
    oled.show()

def screen_color():
    oled.fill(0)
    oled.text("PROXIMITY & COLOR", 5, 0, 1)
    oled.hline(0, 10, 128, 1)
    oled.text(f"Distance: {data['prox']}" if apds else "Distance: N/A", 0, 15, 1)
    oled.text(f"Color: {dominant_color()}" if apds else "Color: N/A", 0, 25, 1)
    if apds:
        oled.text(f"R:{data['r']//10} G:{data['g']//10} B:{data['b']//10}", 0, 35, 1)
    oled.text(f"[2/3] A:Next B:Buzz", 0, 55, 1)
    oled.show()

def screen_controls():
    oled.fill(0)
    oled.text("AUDIO & CONTROLS", 5, 0, 1)
    oled.hline(0, 10, 128, 1)
    oled.text(f"Pot: {data['pot_pct']:.0f}%", 0, 15, 1)
    oled.rect(0, 25, 82, 8, 1)
    bar = int((data["pot_pct"] / 100) * 80)
    if bar > 0: oled.fill_rect(1, 26, bar, 6, 1)
    a = "Rel" if button_A.value else "Pre"
    b = "Rel" if button_B.value else "Pre"
    oled.text(f"A:{a} B:{b}", 0, 37, 1)
    oled.text(f"[3/3] A:Next B:Buzz", 0, 55, 1)
    oled.show()

screen_funcs = [screen_env, screen_color, screen_controls]

# ───── Main Loop ─────
print("Multi-Sensor Dashboard Starting...")
buzz()

while True:
    update_sensors()
    if check_button(button_A):
        screen_index = (screen_index + 1) % 3
        buzz(1000)
        print(f"Screen: {screens[screen_index]}")
    if check_button(button_B):
        buzz(1500)
        time.sleep(0.05)
        buzz(1200)
        print("Buzzer test")
    screen_funcs[screen_index]()
    time.sleep(0.1)
