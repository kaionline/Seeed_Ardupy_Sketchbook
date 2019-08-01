# Introduction
Touch Sensor enables you to replace press with touch.

- [Grove - Touch Sensor](https://www.seeedstudio.com/Grove-Touch-Sensor.html)
- [Grove - Purple LED (3mm)](https://www.seeedstudio.com/Grove-Purple-LED-3mm-p-1143.html)
- [Grove - Multi Color Flash LED (5mm)](https://www.seeedstudio.com/Grove-Multi-Color-Flash-LED-5m-p-1141.html)
- [Grove - LED](https://www.seeedstudio.com/Grove-LED-p-767.html)
- [Grove - Red LED](https://www.seeedstudio.com/Grove-Red-LED-p-1142.html)
- [Grove - Blue LED](https://www.seeedstudio.com/Grove-Blue-LED.html)
- [Grove - White LED](https://www.seeedstudio.com/Grove-White-LED-p-1140.html)
- [Grove - Green LED](https://www.seeedstudio.com/Grove-Green-LED.html)
- [Grove - Red LED Button](https://www.seeedstudio.com/Grove-Red-LED-Button.html)
- [Grove - Blue LED Button](https://www.seeedstudio.com/Grove-Blue-LED-Button-p-3104.html)
- [Grove - Yellow LED Button](https://www.seeedstudio.com/Grove-Yellow-LED-Button-p-3101.html)

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
