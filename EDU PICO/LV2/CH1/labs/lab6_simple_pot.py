import board
from analogio import AnalogIn
import time

pot = AnalogIn(board.GP28)

while True:
    value = pot.value
    print("Potentiometer value:", value)
    time.sleep(0.1)
