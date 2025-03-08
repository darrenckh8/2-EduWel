import board                                                                #type: ignore
import time  # Helps us use the board and time functions                    #type: ignore
from pwmio import PWMOut  # Used to control the PWM output                  #type: ignore
# Used to control the servo motor by setting the angle
from adafruit_motor import servo                                            #type: ignore

PWM_Servo1 = PWMOut(board.GP6, frequency=50)  # Sets the PWM output to GP6
PWM_Servo2 = PWMOut(board.GP7, frequency=50)  # Sets the PWM output to GP7
# Sets the servo motor to the PWM output
servo1 = servo.Servo(PWM_Servo1, min_pulse=500, max_pulse=2500)
# Sets the servo motor to the PWM output
servo2 = servo.Servo(PWM_Servo2, min_pulse=500, max_pulse=2500)

position = [0, 45, 90, 135, 180]  # Sets the position of the servo motor

while True:  # Creates an infinite loop
    for angle in position:  # Loops through the position of the servo
        servo1.angle = angle  # Sets the angle of the servo motor to the position
        servo2.angle = angle  # Sets the angle of the servo motor to the position
        print("degree moving to", angle)  # Prints the angle of the servo motor
        time.sleep(3)  # Waits for 3 seconds
