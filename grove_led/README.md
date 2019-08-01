# Introduction
Grove LED is one of the simplest digital output modules, We have many different forms of Grove LED, this driver can drive them completely.

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
This expample contains all the grove_led API. Each line of code is very simple, hope you like it

```python
from grove import grove_led
import board
import time

led = grove_led(board.D13)

while True:
    led.value = 1
    time.sleep(1)
    led.value = 0
    time.sleep(1)
```

## Contributing
If you have any good suggestions or comments, you can send issues or PR us.
