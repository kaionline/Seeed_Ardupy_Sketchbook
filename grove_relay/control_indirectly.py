from grove import grove_button
from grove import grove_relay
import board
import time

button = grove_button(board.D0)
relay = grove_relay(board.D1)

while True:
    relay.value = button.value
