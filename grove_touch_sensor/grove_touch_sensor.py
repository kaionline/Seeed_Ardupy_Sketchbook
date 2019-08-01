from grove import grove_led
from grove import grove_touch_sensor
import board
import time

led = grove_led(board.D0)
led.value = 0
touch = grove_touch_sensor(board.D1)

while True:
    while True:
        if touch.value != 0:
            break

    led.value = not led.value

    while True:
        if touch.value == 0:
            break
