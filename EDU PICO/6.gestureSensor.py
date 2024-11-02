import board  # Helps us refer to the correct pins on the board.                                        #type: ignore
import busio  # Allows us to interact with the I2C bus.                                                 #type: ignore
from adafruit_apds9960.apds9960 import APDS9960 # Allows us to interact with the APDS9960 sensor.       #type: ignore                                                    

i2c = busio.I2C(board.GP5, board.GP4) #setup I2C
apds = APDS9960(i2c) #setup the sensor
apds.enable_gesture = True #enable gesture
apds.enable_proximity = True #enable proximity

while True: # Create an infinite loop that will run forever.
    gesture_value = apds.gesture() # Read the gesture data from the APDS9960 sensor.
    if gesture_value == 1: # Check if the gesture is moving forward.
        print("The plane move forward")
    elif gesture_value == 2: # Check if the gesture is moving backward.
        print("The plane move backward")
    elif gesture_value == 3: # Check if the gesture is moving to the left.
        print("The plane turned to the left")
    elif gesture_value == 4: # Check if the gesture is moving to the right.
        print("The plane turned to the right")
