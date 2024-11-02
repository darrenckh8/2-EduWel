import board # Import the board library.
import time # Import the time library. 
import busio # Import the busio library.
import adafruit_ssd1306 # Import the necessary libraries.
import neopixel  # Import the necessary libraries.
from pwmio import PWMOut  # Import the PWMOut class from the pwmio library.
# Import the motor class from the adafruit_motor library.
from adafruit_motor import motor
# Import the AnalogIn class from the analogio library.
from analogio import AnalogIn

# Create a variable called POT that represents the potentiometer connected to pin 28.
POT = AnalogIn(board.GP28)
# Create a variable called i2c that represents the I2C bus connected to pins 5 and 4.
i2c = busio.I2C(board.GP5, board.GP4)
# Create a variable called oled that represents the OLED display with a resolution of 128x64 connected to the I2C bus.
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Create a variable called PWM_M2A that represents the PWM output connected to pin 12.
PWM_M2A = PWMOut(board.GP12, frequency=10000)
# Create a variable called PWM_M2B that represents the PWM output connected to pin 13.
PWM_M2B = PWMOut(board.GP13, frequency=10000)
# Create a variable called motor that represents the DC motor connected to the PWM outputs.
motor = motor.DCMotor(PWM_M2A, PWM_M2B)

# Create a variable called pixels that represents the NeoPixel strip connected to pin 14.
pixels = neopixel.NeoPixel(board.GP14, 5, brightness=0.2)
pixels.fill((0, 0, 0))  # Turn off all the pixels.

blink_interval = 0.1  # Set the interval between blinks to 0.1 seconds.
# Create a variable called last_blink_time that stores the time of the last blink.
last_blink_time = time.time()
# Create a variable called is_on that stores the state of the pixels.
is_on = False


# Create a function called blink_pixels that toggles the state of the pixels.
def blink_pixels(pixels):
    global is_on  # Use the global keyword to access the is_on variable.
    if is_on:  # Check if the pixels are currently on.
        pixels.fill((0, 0, 0))  # Turn off the pixels.
    else:  # If the pixels are off.
        pixels.fill((255, 0, 0))  # Turn on the pixels.
    is_on = not is_on  # Toggle the state of the pixels.


while True:  # Create an infinite loop that will run forever.
    current_time = time.time() # Get the current time.
    speed = (POT.value * 1) / 65535 # Read the value of the potentiometer and convert it to a speed value.
    speedSTR = str(speed) # Convert the speed value to a string.
    oled.fill(0) # Clear the OLED display.
    oled.text(f'Speed = {speedSTR}', 20, 25, 1) # Display the speed value on the OLED display.
    oled.show() # Update the OLED display.
    print(speed) # Print the speed value to the console.

    motor.throttle = speed # Set the speed of the motor to the speed value.

    if speed < 0.1: # Check if the speed is less than 0.1.
        pixels[0] = (0, 0, 0)
        pixels[1] = (0, 0, 0)
        pixels[2] = (0, 0, 0)
        pixels[3] = (0, 0, 0)
        pixels[4] = (0, 0, 0)
    elif speed < 0.2: # Check if the speed is less than 0.2.
        pixels[0] = (0, 255, 0)
        pixels[1] = (0, 0, 0)
        pixels[2] = (0, 0, 0)
        pixels[3] = (0, 0, 0)
        pixels[4] = (0, 0, 0)
    elif speed < 0.4: # Check if the speed is less than 0.4.
        pixels[0] = (0, 255, 0)
        pixels[1] = (255, 255, 0)
        pixels[2] = (0, 0, 0)
        pixels[3] = (0, 0, 0)
        pixels[4] = (0, 0, 0)
    elif speed < 0.6: # Check if the speed is less than 0.6.
        pixels[0] = (0, 255, 0)
        pixels[1] = (255, 255, 0)
        pixels[2] = (255, 255, 0)
        pixels[3] = (0, 0, 0)
        pixels[4] = (0, 0, 0)
    elif speed < 0.8: # Check if the speed is less than 0.8.
        pixels[0] = (0, 255, 0)
        pixels[1] = (255, 255, 0)
        pixels[2] = (255, 255, 0)
        pixels[3] = (255, 255, 0)
        pixels[4] = (0, 0, 0)
    elif speed < 0.9: # Check if the speed is less than 0.9.
        pixels[0] = (255, 0, 0)
        pixels[1] = (255, 0, 0)
        pixels[2] = (255, 0, 0)
        pixels[3] = (255, 0, 0)
        pixels[4] = (255, 0, 0)

    else: # If the speed is greater than or equal to 0.9.
        if current_time - last_blink_time >= blink_interval:
            blink_pixels(pixels)
            last_blink_time = current_time
