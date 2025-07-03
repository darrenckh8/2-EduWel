# USE SIM AT WOKWI.COM 

from machine import Pin
from time import sleep

# LED connected to GP15
led = Pin(15, Pin.OUT)

while True:
    led.value(1)  # Turn LED on
    sleep(1)      # Wait for 1 second
    led.value(0)  # Turn LED off
    sleep(1)      # Wait for 1 second


from machine import Pin
from time import sleep

# RGB LED pins (connected to GP16, GP17, GP18)
red = Pin(16, Pin.OUT)
green = Pin(17, Pin.OUT)
blue = Pin(18, Pin.OUT)

def set_rgb(r, g, b):
    red.value(r)
    green.value(g)
    blue.value(b)

while True:
    set_rgb(1, 0, 0)  # Red
    sleep(1)
    set_rgb(0, 1, 0)  # Green
    sleep(1)
    set_rgb(0, 0, 1)  # Blue
    sleep(1)
    set_rgb(1, 1, 1)  # White (all colors)
    sleep(1)
    set_rgb(0, 0, 0)  # Off
    sleep(1)


from machine import Pin
from time import sleep

# LED on GP15 and button on GP14
led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:  # Button pressed
        led.value(1)         # Turn on LED
    else:
        led.value(0)         # Turn off LED
    sleep(0.1)               # Small delay to avoid bouncing


from machine import Pin
from time import sleep

# LED on GP15 and switch on GP13
led = Pin(15, Pin.OUT)
switch = Pin(13, Pin.IN, Pin.PULL_DOWN)

while True:
    if switch.value() == 1:  # Switch on
        led.value(1)         # Turn on LED
    else:
        led.value(0)         # Turn off LED
    sleep(0.1)


from machine import Pin, ADC, PWM
from time import sleep

# Potentiometer on GP26 (ADC) and LED on GP15 (PWM)
pot = ADC(Pin(26))  # Analog input from potentiometer
led = PWM(Pin(15))  # PWM output to control LED brightness
led.freq(1000)      # Set PWM frequency

while True:
    pot_value = pot.read_u16()  # Read potentiometer value (0-65535)
    led.duty_u16(pot_value)     # Set LED brightness
    sleep(0.1)



from machine import Pin
from time import sleep

# Traffic light LEDs (Red on GP20, Yellow on GP21, Green on GP22)
red_light = Pin(20, Pin.OUT)
yellow_light = Pin(21, Pin.OUT)
green_light = Pin(22, Pin.OUT)

while True:
    # Red light on
    red_light.value(1)
    sleep(2)
    red_light.value(0)
    
    # Yellow light on
    yellow_light.value(1)
    sleep(1)
    yellow_light.value(0)
    
    # Green light on
    green_light.value(1)
    sleep(2)
    green_light.value(0)


from machine import Pin, PWM
from time import sleep

# Buzzer on GP19
buzzer = PWM(Pin(19))

# Function to play a sound at a given frequency and duration
def play_buzzer(freq, duration):
    buzzer.freq(freq)
    buzzer.duty_u16(32768)  # 50% duty cycle
    sleep(duration)
    buzzer.duty_u16(0)      # Turn off buzzer

while True:
    play_buzzer(1000, 0.5)  # Play at 1 kHz for 0.5 seconds
    sleep(1)                # Wait for 1 second
