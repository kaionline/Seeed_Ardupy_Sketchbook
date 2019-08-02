from grove import grove_hall_sensor
import board
import time

hall_sensor = grove_hall_sensor(board.D0)

while True:
    if hall_sensor.value: #negative logical
        print ("not detected.")
    else:
        print ("detected.")
    time.sleep(1)
