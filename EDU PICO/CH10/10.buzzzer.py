import board # Helps us refer to the correct pins on the board.                                   #type: ignore
import simpleio # Allows us to use simpleio.tone() to generate sound.                             #type: ignore

buzzer_pin = board.GP21 # Create a variable called buzzer_pin that represents pin 21 on the board.

while True: # Create an infinite loop that will run forever.
    simpleio.tone(buzzer_pin,523,1) # Play a tone of 523 Hz for 1 second.
    simpleio.tone(buzzer_pin,587,1) # Play a tone of 587 Hz for 1 second.
    simpleio.tone(buzzer_pin,659,1) # Play a tone of 659 Hz for 1 second.
    simpleio.tone(buzzer_pin,784,1) # Play a tone of 784 Hz for 1 second.
    simpleio.tone(buzzer_pin,0,1)   # Stop playing the tone for 1 second.


import board # Helps us refer to the correct pins on the board.                                  #type: ignore
import time # Allows us to use time.sleep() to pause the program.                                #type: ignore
import digitalio # Allows us to interact with the digital pins on the board.                     #type: ignore
import simpleio # Allows us to use simpleio.tone() to generate sound.                            #type: ignore

button_A= digitalio.DigitalInOut(board.GP0) # Create a variable called button_A that represents pin 0 on the board.
button_A.direction= digitalio.Direction.INPUT # Set the direction of button_A to input.
button_A.pull = digitalio.Pull.UP # Enable the pull-up resistor for button_A.
 
button_B= digitalio.DigitalInOut(board.GP1) # Create a variable called button_B that represents pin 1 on the board.
button_B.direction =digitalio.Direction.INPUT # Set the direction of button_B to input.
button_B.pull = digitalio.Pull.UP # Enable the pull-up resistor for button_B.

buzzer= board.GP21  # Create a variable called buzzer that represents pin 21 on the board.

while True: # Create an infinite loop that will run forever.
    if not button_A.value: # Check if button_A is pressed.
        print("oh,someones comming") # Print a message to the console.
        simpleio.tone(buzzer,440,1) # Play a tone of 440 Hz for 1 second.
        time.sleep(0.3) # Pause the program for 0.3 seconds.
    if not button_B.value: # Check if button_B is pressed.
        print("open the door to great guests") # Print a message to the console.
        simpleio.tone(buzzer,0,2) # Stop playing the tone for 2 seconds.
        time.sleep(0.3) # Pause the program for 0.3 seconds.
