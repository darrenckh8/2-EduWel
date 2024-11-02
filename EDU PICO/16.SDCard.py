import time #Allows us to add delays in the program, controlling the rate of data logging.                      #type: ignore
import board #Used to access the specific pin layout of the Raspberry Pi Pico.                                  #type: ignore 
import busio #Used to set up the SPI communication bus for the SD card.                                         #type:ignore
import sdcardio #Provides the tools to interact with SD cards.                                                  #type:ignore
import storage #Helps with file system management, allowing us to mount the SD card.                            #type:ignore
import digitalio #Enables control of digital pins.                                                              #type:ignore
import microcontroller #Accesses onboard features like the temperature sensor.                                  #type:ignore
import os #Allows us to check file size and file handling functions.

led = digitalio.DigitalInOut(board.LED) #Creates an object to control the built-in LED.
led.switch_to_output() #Sets the LED to output mode so it can be turned on or off.

spi = busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16)
#spi: Sets up the SPI bus for communication with the SD card.
#GP18: Clock line (SCK).
#GP19: Data line for sending data (MOSI).
#GP16: Data line for receiving data (MISO).
cs = board.GP17 #Sets GP17 as the chip select (CS) pin, allowing us to select the SD card.


sd = sdcardio.SDCard(spi, cs) #Initializes the SD card using the SPI bus and CS pin.
vfs = storage.VfsFat(sd) 
#Creates a VfsFat object for reading and writing to the FAT file system on the SD card.
storage.mount(vfs, '/sd') 
#Mounts the SD card to the file path '/sd' so that it can be accessed by the code.

sd_dir = '/sd/' #Sets the directory path for the SD card.
file_name = 'temperature.csv' #Specifies the file name, temperature.csv, for logging data.
max_file_size = 100*10**6  
#Sets a maximum file size of 100MB for the CSV file to prevent it from growing too large.
#100x10^6(MB) = 100MB

with open(sd_dir+file_name, "a") as datalog: 
    """Opens the file in append mode ("a") to continuously add new data to the end 
    of the file without overwriting existing data."""
    
    while True:
        file_size = os.stat(sd_dir+file_name)[6] 
        """To get the file size of temperature.csv to keep track of the file's size.
        the [6] accesses the seventh element in the tuple returned by os.stat(). 
        This tuple contains various file properties, such as file permissions, 
        last modified times, and file size. In many systems, the file size in bytes is 
        stored in the seventh element (index 6) of this tuple."""
        
        if file_size < max_file_size: 
            """Checks if the file size is less than 100MB. If it is, 
            data will continue to be logged; otherwise, logging will stop."""

            temp = microcontroller.cpu.temperature 
            """Reads the temperature from the CPU’s onboard sensor."""

            datalog.write('{0:.1f}\n'.format(temp)) 
            """Writes the temperature to the file, formatted to one decimal place, 
            followed by a newline."""

            datalog.flush()
            """Forces the data to be saved to the SD card immediately, 
            which ensures each entry is recorded even if the program stops unexpectedly."""

            led.value = not led.value 
            """Toggles the LED on and off to indicate that data is being logged."""

            time.sleep(1)
            """Pauses the program for 1 second before logging the next data point."""

        else: 
            led.value = True
            """If the file reaches 100MB, the LED stays on continuously to indicate 
            that logging has stopped."""
