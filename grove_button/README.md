# Introduction

The Button is probably the most used input device and can be seen in every corner of our lives. We also offer a lot of different types of buttons.


- [Grove - Red LED Button](https://www.seeedstudio.com/Grove-Red-LED-Button.html)
- [Grove - Blue LED Button](https://www.seeedstudio.com/Grove-Blue-LED-Button-p-3104.html)
- [Grove - Yellow LED Button](https://www.seeedstudio.com/Grove-Yellow-LED-Button-p-3101.html)
- [Grove - Button(P)](https://www.seeedstudio.com/Grove-Button-P.html)
- [Grove - Button](https://www.seeedstudio.com/Grove-Button-p-766.html)
- [Grove - Mech Keycap](https://www.seeedstudio.com/Grove-Mech-Keycap.html)

## Usage Example

The Led will light when keep the key pressed and will go out when the button is released.

```
from grove import grove_led
from grove import grove_button
import board
import time

button = grove_button(board.D6)
led = grove_led(board.D2)

while True:
    if button.value:
        led.value = 1
    else:
        led.value = 0
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
