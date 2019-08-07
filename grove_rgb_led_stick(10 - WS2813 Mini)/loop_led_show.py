from grove import grove_rgb_led_strip
import board
import time

count_of_led = 10
strip = grove_rgb_led_strip(board.SCL, count_of_led)
strip.set_brightness(255)

while True:
    no = 1
    strip.clear()
    strip.update()
    while no <= count_of_led:
        strip.set_pix_color(no, 0x00ff00) #green
        strip.update()
        time.sleep(0.1)
        no = no + 1

