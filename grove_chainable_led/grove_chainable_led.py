from grove import grove_chainable_led
import board
import time

rgb_led = grove_chainable_led(board.D0, board.D1, 1) #clock, data, led_numbers

while True:
    rgb_led.set_rgb(0, 255, 0, 0)
    time.sleep(2)
    rgb_led.set_rgb(0, 0, 255, 0)
    time.sleep(2)
    rgb_led.set_rgb(0, 0, 0, 255)
    time.sleep(2)
    rgb_led.set_rgb(0, 0, 255, 255)
    time.sleep(2)
    rgb_led.set_rgb(0, 255, 0, 255)
    time.sleep(2)
    rgb_led.set_rgb(0, 255, 255, 0)
    time.sleep(2)
    rgb_led.set_rgb(0, 255, 255, 255)
    time.sleep(2)
