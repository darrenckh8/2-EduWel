import board
import time
import array
import math
import audiobusio
import neopixel  # Import NeoPixel library

# Set up the microphone
mic = audiobusio.PDMIn(board.GP3, board.GP2, sample_rate=16000, bit_depth=16)
samples = array.array('H', [0] * 1024)  # Reduced sample size for faster updates

# Set up the NeoPixel LED
num_pixels = 1
pixel_pin = board.GP14
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)
pixels.fill((0, 0, 0))  # Start with the LED off

# Function to calculate log base 10
def log10(x):
    return math.log(x) / math.log(10)

# Function to calculate the normalized root mean square (RMS)
def normalized_rms(values):
    # Step 1: Compute the mean (average) of the samples
    minbuf = sum(values) / len(values)  # Average background noise level
    
    # Step 2: Subtract the mean from each sample and square the result
    samples_sum = sum(float(sample - minbuf) * (sample - minbuf) for sample in values)
    
    # Step 3: Compute the square root of the mean of squared differences (RMS formula)
    return math.sqrt(samples_sum / len(values))

# Clap detection parameters
CLAP_THRESHOLD = 60  # Adjust this based on testing (minimum dB level for a clap)
CLAP_TIME_WINDOW = 2  # Maximum time between two claps to be counted as a "double clap"
last_clap_time = 0  # Time of last detected clap
clap_count = 0  # Number of claps detected
led_on = False  # Track LED state (on/off)

while True:
    mic.record(samples, len(samples))  # Record audio samples
    magnitude = normalized_rms(samples)  # Compute the RMS magnitude
    
    if magnitude > 0:
        # Convert RMS to decibels (dB) using the formula: dB = 20 * log10(RMS)
        sound_level_dB = 20 * log10(magnitude)
        print(f"Sound Level(dB): {sound_level_dB:.2f}")  # Print dB level
        
        # Detect a clap if the sound level exceeds the threshold
        if sound_level_dB > CLAP_THRESHOLD:
            current_time = time.monotonic()  # Get current time
            
            # Check if the clap happened within the allowed time window
            if current_time - last_clap_time < CLAP_TIME_WINDOW:
                clap_count += 1  # Increment clap count
            else:
                clap_count = 1  # Reset clap count if too much time has passed
            
            last_clap_time = current_time  # Update last clap time
            
            # Toggle the LED if two claps are detected within the time window
            if clap_count == 2:
                led_on = not led_on  # Toggle state
                pixels.fill((255, 255, 255) if led_on else (0, 0, 0))  # Turn LED on/off
                print("Double Clap Detected! Toggling NeoPixel")
                clap_count = 0  # Reset clap count after toggling
    
    time.sleep(0.01)  # Short delay for real-time responsiveness

