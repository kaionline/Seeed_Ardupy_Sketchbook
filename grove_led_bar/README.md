# Introduction
Grove – LED Bar is comprised of a 10 segment LED gauge bar and an MY9221 LED controlling chip. It can be used as an indicator for remaining battery life, voltage, water level, music volume or other values that require a gradient display. There are 10 LED bars in the LED bar graph: one red, one yellow, one light green, and seven green bars. Demo code is available to get you up and running quickly. It lights up the LEDs sequentially from red to green, so the entire bar graph is lit up in the end. Want to go further? Go ahead and code your own effect.

- [Grove - Led Bar](https://www.seeedstudio.com/Grove-LED-Bar-v2-0.html)

## Usage Example

```python
from grove import grove_led_bar
import board
import time

led_bar = grove_led_bar(board.D0, board.D1) #clock, data
i = 0

while True:
    i = i + 1
    led_bar.set_bits(i)
    time.sleep(0.05)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
