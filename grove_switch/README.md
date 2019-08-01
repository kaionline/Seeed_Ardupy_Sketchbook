# Introduction
Switch is a common component in electronic circuit, It is our partner on the way to circuit learning.

- [Grove - Switch](https://www.seeedstudio.com/Grove-Switch-P-p-1252.html)
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
Sometimes the switch acts as an authorized role, which can control both the next level of input and the upper level of output.

```python
from grove import grove_led
from grove import grove_switch
import board

led = grove_led(board.D0)
switch = grove_switch(board.D1)

while True:
    led.value = switch.value
```

## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
