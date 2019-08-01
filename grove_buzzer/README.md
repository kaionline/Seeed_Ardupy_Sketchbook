# Introduction
Buzzer can connect to digital output to generate alarm-like sound, it can also be connected to an analog pulse-width modulation output to generate various tones and effects.

- [Grove - Buzzer](https://www.seeedstudio.com/Grove-Buzzer.html)
- [Grove - Red LED Button](https://www.seeedstudio.com/Grove-Red-LED-Button.html)
- [Grove - Blue LED Button](https://www.seeedstudio.com/Grove-Blue-LED-Button-p-3104.html)
- [Grove - Yellow LED Button](https://www.seeedstudio.com/Grove-Yellow-LED-Button-p-3101.html)
- [Grove - Button(P)](https://www.seeedstudio.com/Grove-Button-P.html)
- [Grove - Button](https://www.seeedstudio.com/Grove-Button-p-766.html)
- [Grove - Mech Keycap](https://www.seeedstudio.com/Grove-Mech-Keycap.html)

## Usage Example
Do you want to experience the feeling of generating a telegram?

```python
from grove import grove_buzzer
from grove import grove_button
import board
import time

buzzer = grove_buzzer(board.D0)
button = grove_button(board.D1)

while True:
    buzzer.value = button.value
```

## Contributing

If you have any good suggestions or comments, you can send issues or PR us.

