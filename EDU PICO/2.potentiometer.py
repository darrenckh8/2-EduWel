import time # Used to pause the program for a short time.
import board # Helps us refer to the correct pins on the board.                                                       
from analogio import AnalogIn # Allows us to interact with the potentiometer (analog input).                                                  

potentio = AnalogIn(board.GP28) # Create an variable called potentio that represents the potentiometer connected to pin 28.

while True: # Create an infinite loop that will run forever.
    voltage = (potentio.value * 1) / 65535 # Read the value of the potentiometer and convert it to a voltage value.
    print(voltage) # Print the voltage value to the console.
    time.sleep(0.1) # Pause the program for 0.1 seconds.




