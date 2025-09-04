import wifi
import socketpool
from adafruit_httpserver import Server, Request, Response, POST

WIFI_SSID = "your_ssid"
WIFI_PASSWORD = "your_password"

wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static")

led_state = False

def get_html():
    return f"""<html><body>
    <h2>Web Control</h2>
    <form method='POST'>
    <button type='submit' name='action' value='toggle'>Toggle LED</button>
    </form>
    <p>LED State: {'ON' if led_state else 'OFF'}</p>
    </body></html>"""

@server.route("/", POST)
def buttonpress(request: Request):
    global led_state
    led_state = not led_state
    return Response(request, get_html(), content_type='text/html')

@server.route("/")
def base(request: Request):
    return Response(request, get_html(), content_type='text/html')

server.start(str(wifi.radio.ipv4_address), port=80)
print("Server running at:", wifi.radio.ipv4_address)

while True:
    server.poll()
