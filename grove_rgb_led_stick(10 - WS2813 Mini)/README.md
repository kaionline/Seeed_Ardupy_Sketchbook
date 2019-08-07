# Introduction
We integrated 10 full-color RGB LEDs on this stick, with only one signal pin you can control all 10 LEDs easily. All the LEDs are WS2813 Mini, which is an intelligent control and high cost-effective LED. What's more, the WS2813 support signal break-point continuous transmission, which means you can continue to use other leds with one led be broken.

You can use this little stick create hundreds of thausands light effect, we hope it will bring you more fun.
- [Grove - RGB LED Stick (10 - WS2813 Mini)](https://www.seeedstudio.com/Grove-RGB-LED-Stick-10-WS2813-Min-p-3226.html)

## Usage Example

```python
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
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
