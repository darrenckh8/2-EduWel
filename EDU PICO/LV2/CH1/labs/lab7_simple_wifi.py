import wifi
import time

WIFI_SSID = "your_ssid"
WIFI_PASSWORD = "your_password"

while True:
    try:
        print("Connecting to Wi-Fi...")
        wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
        print("Connected! IP:", wifi.radio.ipv4_address)
        break
    except Exception as e:
        print("Wi-Fi connection failed:", e)
        time.sleep(2)
