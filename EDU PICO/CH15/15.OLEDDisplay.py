import board #allows us to use the pins on the board
import busio #allows us to use the I2C protocol
import time #allows us to use the sleep function
import adafruit_ssd1306 #allows us to use the OLED display

i2c = busio.I2C(board.GP5, board.GP4) #create an I2C object
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c) #create an OLED object

while True:
    # --- Basic text display ---
    oled.fill(0) #clear the display
    oled.invert(True) #invert the display
    oled.text("Hello,world", 40, 20, 1) #display text
    oled.text("How are you?", 40, 35, 1) #display text
    oled.show() #update the display
    time.sleep(2)

    # --- Drawing shapes ---
    oled.fill(0)
    oled.rect(10, 10, 50, 30, 1) #draw rectangle (x, y, width, height, color)
    oled.fill_rect(70, 10, 40, 20, 1) #draw filled rectangle
    oled.hline(0, 50, 128, 1) #draw horizontal line
    oled.vline(64, 0, 64, 1) #draw vertical line
    oled.pixel(120, 60, 1) #draw a single pixel
    oled.show()
    time.sleep(2)

    # --- Scrolling text example ---
    oled.fill(0)
    message = "Scrolling Text Demo"
    for x in range(128, -len(message)*8, -2):  # 8 pixels per character
        oled.fill(0)
        oled.text(message, x, 30, 1)
        oled.show()
        time.sleep(0.03)

    # --- Simple animation: moving dot ---
    oled.fill(0)
    for x in range(0, 128, 4):
        oled.fill(0)
        oled.pixel(x, 32, 1)
        oled.show()
        time.sleep(0.05)

    # --- Power management ---
    oled.fill(0)
    oled.text("Turning off...", 10, 30, 1)
    oled.show()
    time.sleep(1)
    oled.poweroff()
    time.sleep(1)
    oled.poweron()
    oled.fill(0)
    oled.text("Display On!", 20, 30, 1)
    oled.show()
    time.sleep(2)

    # --- Extra: Combining graphics and text ---
    oled.fill(0)
    oled.rect(0, 0, 128, 64, 1) # border
    oled.text("All features!", 20, 10, 1)
    oled.hline(10, 30, 108, 1)
    oled.fill_rect(54, 40, 20, 10, 1)
    oled.text(":-)", 58, 42, 0) # text in negative (black on white)
    oled.show()
    time.sleep(2)

    # --- Toggle inversion demo ---
    oled.fill(0)
    oled.invert(False)
    oled.text("Normal mode", 20, 50, 1)
    oled.show()
    time.sleep(1)
    oled.invert(True)
    oled.fill(0)
    oled.text("Inverted mode", 20, 50, 1)
    oled.show()
    time.sleep(1)
    oled.invert(False)

    # --- Partial clear demo ---
    oled.fill(0)
    oled.text("Partial clear below", 10, 10, 1)
    oled.fill_rect(20, 20, 40, 20, 1) # draw filled box
    oled.show()
    time.sleep(1)
    oled.fill_rect(20, 20, 40, 20, 0) # clear that box
    oled.show()
    time.sleep(1)

    # --- Simple bar graph demo ---
    oled.fill(0)
    oled.text("Bar graph:", 0, 0, 1)
    for i in range(0, 100, 10):
        oled.fill_rect(10 + i, 60 - i//2, 8, i//2, 1)
    oled.show()
    time.sleep(2)