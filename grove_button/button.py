from grove import grove_led
from grove import grove_button
import board
import time

btn = grove_button(board.SCL)
led = grove_led(board.D2)

while True:
    if btn.value:
        led.value = 1
    else:
        led.value = 0
