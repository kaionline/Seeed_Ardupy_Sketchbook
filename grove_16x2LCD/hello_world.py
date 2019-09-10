from grove import grove_16x2_lcd
import time

lcd = grove_16x2_lcd()
lcd.print("Hello world.")
lcd.is_blink_cursor = True
i = 0

while True:
    lcd.set_cursor(1, 2) #column 1, row 2
    lcd.print(i)
    time.sleep(0.5)
    i = i + 1
