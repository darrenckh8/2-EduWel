import time
import os
import board
import digitalio
import audiomp3
import audiopwmio

# Setup buttons
buttonA = digitalio.DigitalInOut(board.GP0)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.UP

buttonB = digitalio.DigitalInOut(board.GP1)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.UP

# Setup audio output
dac = audiopwmio.PWMAudioOut(left_channel=board.GP20, right_channel=board.GP21)

# Detect MP3 files in /music
song_array = [file for file in os.listdir("/music") if file.endswith(".mp3")]
song_array.sort()

# Load MP3 file
def load_mp3(file_name):
    return audiomp3.MP3Decoder(open("/music/" + file_name, "rb"))

# Handle no files
if not song_array:
    print("No MP3 files found in /music folder.")
    while True:
        pass

# State variables
counter = 0
playing = False
paused = False
button_hold_threshold = 0.5  # Seconds

print("Press Button A to Play/Pause")
print("Press Button B to Skip/Go Back")

# Button press detection
def check_button(button):
    """Returns 'short', 'long', or None depending on how long the button is pressed."""
    if not button.value:
        time.sleep(0.01)  # Debounce
        start_time = time.monotonic()
        while not button.value:
            time.sleep(0.01)
        duration = time.monotonic() - start_time
        return "long" if duration >= button_hold_threshold else "short"
    return None

while True:
    actionA = check_button(buttonA)
    actionB = check_button(buttonB)

    # Button A: Play/Pause or Start
    if actionA == "short":
        if not playing:
            print(f"Playing: {song_array[counter]}")
            dac.play(load_mp3(song_array[counter]), loop=False)
            playing = True
            paused = False
        elif playing and not paused and actionA == "short":
            print("Paused.")
            dac.pause()
            paused = True
        elif playing and paused and actionA == "short":
            print("Resuming...")
            dac.resume()
            paused = False
        time.sleep(0.2)
        
    if actionA == "long":
        counter = 0
        playing = False
        paused = False
        print("Playback Stopped")
        dac.stop()
        time.sleep(0.2)

    # Button B: Next/Previous track
    if actionB == "short":
        counter = (counter + 1) % len(song_array)
        print(f"Next Track: {song_array[counter]}")
        dac.play(load_mp3(song_array[counter]), loop=False)
        playing = True
        paused = False
        if counter == 0:
            print("Wrapped to first track.")
        time.sleep(0.2)

    elif actionB == "long":
        counter = (counter - 1) % len(song_array)
        print(f"Previous Track: {song_array[counter]}")
        dac.play(load_mp3(song_array[counter]), loop=False)
        playing = True
        paused = False
        if counter == len(song_array) - 1:
            print("Wrapped to last track.")
        time.sleep(0.2)

    # Auto play next track when finished
    if playing and not dac.playing and not paused:
        print("Playback finished.")
        counter = (counter + 1) % len(song_array)
        print(f"Auto-playing: {song_array[counter]}")
        dac.play(load_mp3(song_array[counter]), loop=False)
        playing = True
        time.sleep(0.2)

