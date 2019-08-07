from grove import grove_temperature_humidity_sensor
from grove import ic
import board
import time

dth = grove_temperature_humidity_sensor(board.D0, ic.DHT11)

while True:
    print ("Current temperature is", dth.temperature)
    print ("Current humidity is", dth.humidity)
    time.sleep(1)

