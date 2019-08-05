# Introduction
The Grove-Relay module is a digital normally-open switch. Through it, you can control circuit of high voltage with low voltage, say 5V on the controller. There is an indicator LED on the board, which will light up when the controlled terminals get closed.

- [Grove - Relay](https://www.seeedstudio.com/Grove-Relay-p-769.html)
- [Grove - Red LED Button](https://www.seeedstudio.com/Grove-Red-LED-Button.html)
- [Grove - Blue LED Button](https://www.seeedstudio.com/Grove-Blue-LED-Button-p-3104.html)
- [Grove - Yellow LED Button](https://www.seeedstudio.com/Grove-Yellow-LED-Button-p-3101.html)
- [Grove - Button(P)](https://www.seeedstudio.com/Grove-Button-P.html)
- [Grove - Button](https://www.seeedstudio.com/Grove-Button-p-766.html)
- [Grove - Mech Keycap](https://www.seeedstudio.com/Grove-Mech-Keycap.html)
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

```python
from grove import grove_button
from grove import grove_relay
import board
import time

button = grove_button(board.D0)
relay = grove_relay(board.D1)

while True:
    relay.value = button.value
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
