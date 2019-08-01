from grove import grove_led
from grove import grove_switch
import board

led = grove_led(board.D0)
switch = grove_switch(board.D1)

while True:
    led.value = switch.value
