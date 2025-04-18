import board
import digitalio
import wifi
import socketpool
import time
from adafruit_httpserver import Server, Request, Response, POST

# 📶 Enter your Wi-Fi credentials here
WIFI_SSID = "Home Office@unifi"
WIFI_PASSWORD = "244466666Abc"

def setup_wifi_sta():
    print("Connecting to Wi-Fi...")
    wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
    print("Connected to Wi-Fi.")
    print("IP address:", wifi.radio.ipv4_address)
    pool = socketpool.SocketPool(wifi.radio)
    return pool

def setup_relay():
    print("Setting up relay on GP22...")
    relay = digitalio.DigitalInOut(board.GP22)
    relay.direction = digitalio.Direction.OUTPUT
    print("Relay ready.")
    return relay

def light_on(relay):
    print("Light ON")
    relay.value = True

def light_off(relay):
    print("Light OFF")
    relay.value = False

def webpage():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>USB Relay Control</title>
    </head>
    <body>
    <h2>USB Relay Light Control</h2>
    <form method="POST">
      <button type="submit" name="action" value="light_on">Light On</button>
      <button type="submit" name="action" value="light_off">Light Off</button>
    </form>
    </body>
    </html>
    """
    return html

def setup_server(pool, relay):
    print("Setting up HTTP server...")
    server = Server(pool, "/static")

    @server.route("/")
    def base(request: Request):
        print("Received GET request at /")
        return Response(request, f"{webpage()}", content_type='text/html')

    @server.route("/", POST)
    def buttonpress(request: Request):
        print("Received POST request at /")
        raw_text = request.raw_request.decode("utf8")
        print("Raw POST data:", raw_text)

        if "action=light_on" in raw_text:
            light_on(relay)
        elif "action=light_off" in raw_text:
            light_off(relay)
        else:
            print("Unknown action")

        return Response(request, f"{webpage()}", content_type='text/html')

    server.start(str(wifi.radio.ipv4_address), port=8080)
    print("Server started. Access it at: http://%s" % wifi.radio.ipv4_address)
    return server

try:
    print("----- Starting USB Relay Control -----")
    pool = setup_wifi_sta()
    relay = setup_relay()
    server = setup_server(pool, relay)

    # Debug LED
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT

    print("Entering main loop...")
    while True:
        server.poll()
        led.value = not led.value  # Blink onboard LED
        time.sleep(1)

except Exception as e:
    print(">>> ERROR <<<")
    print(e)

