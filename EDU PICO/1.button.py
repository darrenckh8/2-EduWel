import board             # Helps us refer to the correct pins on the board.                                                       
import digitalio         # Allows us to interact with the buttons (digital inputs).                           
import time              # Used to pause the program for a short time.                              

button_A = digitalio.DigitalInOut(board.GP0) # Create a variable called button_A that represents the button connected to pin 0.
button_B = digitalio.DigitalInOut(board.GP1) # Create a variable called button_B that represents the button connected to pin 1.

button_A.direction = digitalio.Direction.INPUT # Set the direction of button_A to be an input.
button_B.direction = digitalio.Direction.INPUT # Set the direction of button_B to be an input.

button_B.pull = digitalio.Pull.UP # Enable the pull-up resistor for button_B.
button_A.pull = digitalio.Pull.UP # Enable the pull-up resistor for button_A.

while True: # Create an infinite loop that will run forever.
    if not button_B.value: # Check if button B is pressed.
        print("Button B is pressed") # Print a message to the console.
        time.sleep(0.3) # Pause the program for 0.3 seconds.
    elif not button_A.value: # Check if button A is pressed.
        print("Button A is pressed") # Print a message to the console.
        time.sleep(0.3) # Pause the program for 0.3 seconds.



