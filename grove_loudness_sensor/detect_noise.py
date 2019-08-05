from grove import grove_loudness_sensor
import board
import time

noise = grove_loudness_sensor(board.A0)

while True:
    print (noise.value)
    time.sleep(0.2)
