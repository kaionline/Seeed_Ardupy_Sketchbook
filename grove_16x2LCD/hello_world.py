from grove import grove_16x2_lcd
import time

lcd = grove_16x2_lcd()
lcd.print("Hello world.")
lcd.is_show_cursor = True
i = 0

while True:
    lcd.set_cursor(0, 1) #column 0, row 1
    lcd.print(i)
    time.sleep(0.5)
    i = i + 1
