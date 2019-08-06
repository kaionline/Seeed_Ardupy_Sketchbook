from grove import grove_led
import board
import time

led = grove_led(board.D0)
led.value = 0

while True:
    led.value = not led.value
    time.sleep(1)
