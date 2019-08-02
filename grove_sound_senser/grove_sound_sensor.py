from grove import grove_sound_sensor
import board
import time

sound_sensor = grove_sound_sensor(board.A0)

while True:
    sum = 0
    for i in range(0, 32):
        sum += sound_sensor.value
    avg = sum / 32
    print (avg)
    time.sleep(0.01)
