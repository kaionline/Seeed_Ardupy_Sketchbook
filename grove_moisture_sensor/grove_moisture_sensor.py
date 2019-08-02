from grove import grove_moisture_sensor
import board
import time

moisture_sensor = grove_moisture_sensor(board.A0)

while True:
    print (moisture_sensor.value)
    time.sleep(1)

