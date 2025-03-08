import board
import time  # Allows us to use the board and time functions      #type: ignore
from pwmio import PWMOut  # Allows us to use the PWMOut function         #type: ignore
# Allows us to use the motor function  #type: ignore
from adafruit_motor import motor
# Allows us to use the AnalogIn function  #type: ignore
from analogio import AnalogIn

POT = AnalogIn(board.GP28)  # Sets the potentiometer to GP28
PWM_M2A = PWMOut(board.GP12, frequency=10000)  # Sets the PWM output to GP12
PWM_M2B = PWMOut(board.GP13, frequency=10000)  # Sets the PWM output to GP13
dc_motor = motor.DCMotor(PWM_M2A, PWM_M2B)  # Sets the motor to the PWM outputs

while True:  # Creates a infinite loop
    # Sets the speed of the motor to the value of the potentiometer
    speed = (POT.value * 1) / 65535
    print(speed)  # Prints the speed of the motor
    dc_motor.throttle = speed  # Sets the throttle of the motor to the speed
    time.sleep(0.1)  # Waits for 0.1 seconds
