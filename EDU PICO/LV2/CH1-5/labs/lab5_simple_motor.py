import board
from pwmio import PWMOut
from adafruit_motor import motor
from analogio import AnalogIn
import time

pot = AnalogIn(board.GP28)
PWM_M2A = PWMOut(board.GP12, frequency=10000)
PWM_M2B = PWMOut(board.GP13, frequency=10000)
dc_motor = motor.DCMotor(PWM_M2A, PWM_M2B)

while True:
    throttle = pot.value / 65535
    dc_motor.throttle = throttle
    print(f"Throttle: {throttle:.2f}")
    time.sleep(0.1)
