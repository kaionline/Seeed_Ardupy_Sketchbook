from grove import grove_led_bar
import board
import time

led_bar = grove_led_bar(board.D0, board.D1) #clock, data
i = 0

while True:
    i = i + 1
    led_bar.set_bits(i)
    time.sleep(0.05)

