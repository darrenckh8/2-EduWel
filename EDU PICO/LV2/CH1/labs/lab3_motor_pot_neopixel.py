import board
from pwmio import PWMOut
from adafruit_motor import motor
from analogio import AnalogIn
import neopixel
import time

pot = AnalogIn(board.GP28)
PWM_M2A = PWMOut(board.GP12, frequency=10000)
PWM_M2B = PWMOut(board.GP13, frequency=10000)
dc_motor = motor.DCMotor(PWM_M2A, PWM_M2B)
pixels = neopixel.NeoPixel(board.GP14, 2, brightness=0.2)

def update_motor_pixel(throttle):
    if throttle < 0.5:
        r, g = int(2 * throttle * 255), 255
    else:
        r, g = 255, int(255 - 2 * (throttle - 0.5) * 510)
    pixels[1] = (r, g, 0)

while True:
    throttle = pot.value / 65535
    dc_motor.throttle = throttle
    update_motor_pixel(throttle)
    print(f"Throttle: {throttle:.2f}")
    time.sleep(0.1)
