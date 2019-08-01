from grove import grove_led
from grove import grove_light_sensor
import board
import time

led = grove_led(board.D0)
brightness = grove_light_sensor(board.A0)

def get_percentage_of_brightness():
    return float(brightness.value) / 1023 * 100

while True:
    led.value = get_percentage_of_brightness() < 10.0
    time.sleep(1)
