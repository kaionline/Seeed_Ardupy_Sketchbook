from grove import grove_vibration_sensor
import board
import time

vibration = grove_vibration_sensor(board.D0)

while True:
    print ("no vibration:", vibration.value)
    time.sleep(1)

