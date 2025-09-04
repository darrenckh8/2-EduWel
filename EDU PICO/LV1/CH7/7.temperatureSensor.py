import board # Helps us refer to the correct pins on the board.                                 #type: ignore
import busio # Allows us to interact with the I2C bus.                                          #type: ignore
import adafruit_ahtx0 # Allows us to interact with the AHT20 sensor.                            #type: ignore

# Create a variable called i2c that represents the I2C bus connected to pins 5 and 4.
i2c = busio.I2C(board.GP5, board.GP4) 
# Create a variable called AHT_sensor that represents the AHT20 sensor connected to the I2C bus.
AHT_sensor = adafruit_ahtx0.AHTx0(i2c) 

while True: # Create an infinite loop that will run forever.
    temperature = AHT_sensor.temperature # Read the temperature data from the AHT20 sensor.
    humidity = AHT_sensor.relative_humidity # Read the humidity data from the AHT20 sensor.
    # Print the temperature and humidity data to the console.
    print(f"Temperature={temperature:.2f} c Humidity={humidity:.2f} %")
