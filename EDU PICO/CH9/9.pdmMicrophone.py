import board # Helps us refer to the correct pins on the board.                                   #type: ignore
import time # Allows us to use time.sleep() to pause the program.                                 #type: ignore 
import array # Allows us to create an array to store the audio data.                              #type: ignore 
import math # Allows us to use mathematical functions like log10().                               #type: ignore
import audiobusio # Allows us to interact with the PDM microphone.                                #type: ignore

# Create a variable called mic that represents the PDM microphone connected to pins 3 and 2.
mic = audiobusio.PDMIn(board.GP3, board.GP2, sample_rate=16000, bit_depth=16) 

# Create an array called samples that can store 6000 audio samples.
samples = array.array('H', [0]*6000)

# Create a function called log10 that calculates the logarithm of a number to the base 10.
def log10(x):
    return math.log(x)/math.log(10)

# Create a function called normalized_rms that calculates the normalized root mean square of a list of values.
def normalized_rms(values):
    minbuf = sum(values)/len(values)
    samples_sum = sum(float(sample-minbuf)*(sample - minbuf)
                      for sample in values)
    return math.sqrt(samples_sum/len(values))

# Create an infinite loop that will run forever.
# Inside the loop, record 6000 audio samples from the PDM microphone.
# Calculate the normalized root mean square of the audio samples.
# If the magnitude is greater than 0, calculate the sound level in decibels.
# Otherwise, print a message saying the magnitude is too small to calculate dB.
while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    if magnitude > 0:
        sound_level_dB = 20*log10(magnitude)
        print(f"sound Level(dB):{sound_level_dB:.2f}")
    else:
        print("Magnitude is too small to calculate dB.")
        time.sleep(0.1)
