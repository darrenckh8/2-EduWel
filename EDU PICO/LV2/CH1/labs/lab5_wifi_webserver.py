import wifi
import socketpool
from adafruit_httpserver import Server, Request, Response

WIFI_SSID = "mmchyy"
WIFI_PASSWORD = "mm001971"

print("Connecting to Wi-Fi...")
wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
print("Connected! IP:", wifi.radio.ipv4_address)

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static")

relay_on = False
motor_on = False

def get_html():
    return f"""<html><body>
    <h2>Smart Home Status</h2>
    <p>Relay: {'ON' if relay_on else 'OFF'}</p>
    <p>DC Motor: {'ON' if motor_on else 'OFF'}</p>
    </body></html>"""

@server.route("/")
def base(request: Request):
    return Response(request, get_html(), content_type='text/html')

server.start(str(wifi.radio.ipv4_address), port=80)
print("Server running at:", wifi.radio.ipv4_address)

while True:
    server.poll()
