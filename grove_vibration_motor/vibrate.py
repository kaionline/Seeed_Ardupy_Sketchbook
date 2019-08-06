from grove import grove_vibration_motor
import board
import time

vibration_motor = grove_vibration_motor(board.D0)
vibration_motor.value = 0

while True:
    vibration_motor.value = not vibration_motor.value
    time.sleep(1)
