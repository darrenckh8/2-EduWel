import board
import wifi
import socketpool
import time
import busio
import ssl
import adafruit_requests
import adafruit_ssd1306

WIFI_SSID = ""
WIFI_PASSWORD = ""
WEATHER_API_KEY = ""
WEATHER_LOCATION = "kuala%20lumpur"

i2c = busio.I2C(board.GP5, board.GP4)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

weather_data = None
last_update = None

def fetch_weather_data():
    global weather_data, last_update
    try:
        url = f"https://api.tomorrow.io/v4/weather/realtime?location={WEATHER_LOCATION}&apikey={WEATHER_API_KEY}"
        print(f"Fetching weather data from: {url}")
        response = requests_session.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            last_update = time.monotonic()
            print("Weather data updated successfully")
            return True
        else:
            print(f"Error fetching weather data: {response.status_code}")
            return False
    except Exception as e:
        print(f"Exception fetching weather data: {e}")
        return False

def display_weather_on_oled():
    oled.fill(0)
    if weather_data is None:
        oled.text("Weather Data", 10, 10, 1)
        oled.text("Unavailable", 15, 25, 1)
        oled.text("Check API key", 5, 40, 1)
        oled.show()
        return
    try:
        data = weather_data['data']
        values = data['values']
        location = weather_data['location']
        temp_c = values['temperature']
        weather_codes = {
            1000: "Clear", 1100: "Mostly Clear", 1101: "Partly Cloudy",
            1102: "Mostly Cloudy", 1001: "Cloudy", 2000: "Fog",
            4000: "Drizzle", 4001: "Rain", 5000: "Snow",
            6000: "Freezing Drizzle", 6001: "Freezing Rain",
            7000: "Ice Pellets", 8000: "Thunderstorm"
        }
        weather_desc = weather_codes.get(values['weatherCode'], "Unknown")
        oled.text(f"{location['name']}", 0, 0, 1)
        oled.text(f"Temp: {temp_c:.1f}C", 0, 12, 1)
        oled.text(f"{weather_desc}", 0, 24, 1)
        oled.text(f"Humidity: {values['humidity']}%", 0, 36, 1)
        oled.text(f"Wind: {values['windSpeed']:.1f}m/s", 0, 48, 1)
        oled.show()
    except Exception as e:
        oled.text("Error:", 10, 10, 1)
        oled.text("Processing", 15, 25, 1)
        oled.text("Weather Data", 10, 40, 1)
        oled.show()

def display_loading():
    oled.fill(0)
    oled.text("Loading...", 25, 20, 1)
    oled.text("Weather Data", 10, 35, 1)
    oled.show()

def display_error(message):
    oled.fill(0)
    oled.text("Error:", 30, 15, 1)
    oled.text(message, 0, 30, 1)
    oled.show()

print("Connecting to Wi-Fi...")
wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
print(f"Connected! IP: {wifi.radio.ipv4_address}")
pool = socketpool.SocketPool(wifi.radio)

ssl_context = ssl.create_default_context()
requests_session = adafruit_requests.Session(pool, ssl_context)

print("Fetching initial weather data...")
display_loading()
fetch_weather_data()

screen_index = 0
last_screen_change = time.monotonic()
SCREEN_DURATION = 5

try:
    while True:
        current_time = time.monotonic()
        if last_update is None or (current_time - last_update) > 600:
            print("Auto-refreshing weather data...")
            display_loading()
            fetch_weather_data()
        if current_time - last_screen_change > SCREEN_DURATION:
            if weather_data is not None:
                try:
                    data = weather_data['data']
                    values = data['values']
                    location = weather_data['location']
                    oled.fill(0)
                    if screen_index == 0:
                        temp_c = values['temperature']
                        weather_codes = {
                            1000: "Clear", 1100: "Mostly Clear", 1101: "Partly Cloudy",
                            1102: "Mostly Cloudy", 1001: "Cloudy", 2000: "Fog",
                            4000: "Drizzle", 4001: "Rain", 5000: "Snow",
                            6000: "Freezing Drizzle", 6001: "Freezing Rain",
                            7000: "Ice Pellets", 8000: "Thunderstorm"
                        }
                        weather_desc = weather_codes.get(values['weatherCode'], "Unknown")
                        oled.text(f"{location['name']}", 0, 0, 1)
                        oled.text(f"Temp: {temp_c:.1f}C", 0, 12, 1)
                        oled.text(f"{weather_desc}", 0, 24, 1)
                        oled.text(f"Humidity: {values['humidity']}%", 0, 36, 1)
                        oled.text(f"Wind: {values['windSpeed']:.1f}m/s", 0, 48, 1)
                    elif screen_index == 1:
                        oled.text("Weather Details", 5, 0, 1)
                        oled.text(f"Feels: {values['temperatureApparent']:.1f}C", 0, 12, 1)
                        oled.text(f"Wind Dir: {values['windDirection']}deg", 0, 24, 1)
                        oled.text(f"Pressure:", 0, 36, 1)
                        oled.text(f"  {values['pressureSeaLevel']:.0f}hPa", 0, 48, 1)
                    elif screen_index == 2:
                        oled.text("More Details", 10, 0, 1)
                        oled.text(f"Visibility:", 0, 12, 1)
                        oled.text(f"  {values['visibility']}Km", 0, 24, 1)
                        oled.text(f"UV Index: {values['uvIndex']}", 0, 36, 1)
                        oled.text(f"Clouds: {values['cloudCover']}%", 0, 48, 1)
                    oled.show()
                    screen_index = (screen_index + 1) % 3
                    last_screen_change = current_time
                except Exception as e:
                    display_error("Data Error")
                    print(f"Display error: {e}")
            else:
                display_error("No Data")
        time.sleep(0.1)
except Exception as e:
    print(">>> ERROR <<<")
    print(e)
    display_error("System Error")
