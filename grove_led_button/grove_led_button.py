from grove import grove_led
from grove import grove_button
import board
import time

led = grove_led(board.D0)
led.value = 0
button = grove_button(board.D1)
    
while True:
    while True:
        if button.value != 0:
            break
            
    while True:
        time.sleep(0.1) #filter out jitter interference
        if button.value == 0:
            break
    led.value = not led.value
