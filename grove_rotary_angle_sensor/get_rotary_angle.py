from grove import grove_loudness_sensor
import board
import time

rotary_angle = grove_loudness_sensor(board.A0)

def get_angle():
    return rotary_angle.value * 360 / 1023

while True:
    print ("Current rotary angle is", get_angle())
    time.sleep(1)

