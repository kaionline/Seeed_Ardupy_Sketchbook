# Introduction
Touch Sensor enables you to replace press with touch.

- [Grove - Touch Sensor](https://www.seeedstudio.com/Grove-Touch-Sensor.html)

## Usage Example
It's worth trying to turn on or off the lights in a touch-of-touch way.

```python
from grove import grove_led
from grove import grove_touch_sensor
import board
import time

led = grove_led(board.D0)
led.value = 0
touch = grove_touch_sensor(board.D1)

while True:
    while True:
        if touch.value != 0:
            break

    led.value = not led.value

    while True:
        if touch.value == 0:
            break
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
