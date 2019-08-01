from grove import grove_buzzer
from grove import grove_button
import board
import time

buzzer = grove_buzzer(board.D0)
button = grove_button(board.D1)

while True:
    buzzer.value = button.value
