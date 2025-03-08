import time # Allows us to use time.sleep() to pause the program.                                  #type: ignore
import board # Helps us refer to the correct pins on the board.                                    #type: ignore
import busio # Allows us to interact with the I2C bus.                                             #type: ignore
import digitalio # Allows us to interact with the digital pins on the board.                       #type: ignore
import audiomp3 # Allows us to decode and play MP3 files.                                          #type: ignore
import audiopwmio # Allows us to interact with the audio output pins on the board.                 #type: ignore
from adafruit_apds9960.apds9960 import APDS9960 # Allows us to interact with the APDS9960 sensor.  #type: ignore

i2c = busio.I2C(board.GP5, board.GP4) # Create a variable called i2c that represents the I2C bus connected to pins 5 and 4.
multi_sensor = APDS9960(i2c) # Create a variable called multi_sensor that represents the APDS9960 sensor connected to the I2C bus.
multi_sensor.enable_proximity = True # Enable proximity detection on the APDS9960 sensor.
multi_sensor.enable_gesture = True # Enable gesture detection on the APDS9960 sensor.

buttonA = digitalio.DigitalInOut(board.GP0) # Create a variable called buttonA that represents pin 0 on the board.
buttonA.direction = digitalio.Direction.INPUT # Set the direction of buttonA to input.
buttonA.pull = digitalio.Pull.UP # Enable the pull-up resistor for buttonA.

buttonB = digitalio.DigitalInOut(board.GP1) # Create a variable called buttonB that represents pin 1 on the board.
buttonB.direction = digitalio.Direction.INPUT # Set the direction of buttonB to input.
buttonB.pull = digitalio.Pull.UP # Enable the pull-up resistor for buttonB.

# Create a variable called dac that represents the PWM audio output connected to pins 20 and 21.
dac = audiopwmio.PWMAudioOut(left_channel=board.GP20, right_channel=board.GP21)

# List of MP3 Files
song_array = ["music_1.mp3", "music_2.mp3", "music_3.mp3", "music_4.mp3"]

# Function to Load MP3 Files
def load_mp3(file_name):
    return audiomp3.MP3Decoder(open("/music/" + file_name, "rb"))

# Initialize Music Playlist
mp3Array = [load_mp3(song) for song in song_array]
counter = 0
start_song = False

print("Press Button A to Start Music")
print("Press Button B for Controls Menu")

while True:
    gesture = multi_sensor.gesture() # Get Gesture Data

    if not buttonA.value:  # Button A Pressed
        start_song = True
        print(f"Playing: {song_array[counter]}")
        dac.play(mp3Array[counter])

    if not buttonB.value:  # Button B Pressed
        print("\n=== Controls Menu ===")
        print("Slide Down  : Pause")
        print("Slide Up    : Play")
        print("Slide Right : Next Track")
        print("Slide Left  : Previous Track")

    if start_song:
        if gesture == 1:  # Slide Up → Resume
            print("Resuming...")
            dac.resume()

        elif gesture == 2:  # Slide Down → Pause
            print("Paused.")
            dac.pause()

        elif gesture == 3:  # Slide Left → Previous Track
            counter = (counter - 1) % len(mp3Array)
            print(f"Previous Track: {song_array[counter]}")
            dac.play(mp3Array[counter])

        elif gesture == 4:  # Slide Right → Next Track
            counter = (counter + 1) % len(mp3Array)
            print(f"Next Track: {song_array[counter]}")
            dac.play(mp3Array[counter])

        # Auto-play next song when the current one ends
        if not dac.playing:
            counter = (counter + 1) % len(mp3Array)
            print(f"Auto-playing next track: {song_array[counter]}")
            dac.play(mp3Array[counter])
