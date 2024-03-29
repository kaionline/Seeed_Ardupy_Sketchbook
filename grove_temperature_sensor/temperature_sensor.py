from analogio import grove_temperature
import board
import time
import math

temperature = grove_temperature(board.A0)

def get_temperature():
    raw_value = temperature.value
    value = (1023 - raw_value) * 10000 / raw_value
    value = 1 / (math.log(value / 10000) / value + 1 / 298.15) - 273.15
    return value

while True:
    print ('current temperature is ', get_temperature())
    time.sleep(1)
