# Introduction
LED Button integrates Led and Button together

- [Grove - Red Led Button](https://www.seeedstudio.com/Grove-Red-LED-Button.html)
- [Grove - Blue Led Button](https://www.seeedstudio.com/Grove-Blue-LED-Button.html)
- [Grove - Yellow Led Button](https://www.seeedstudio.com/Grove-Yellow-LED-Button.html)

## Notice
SIG1 and SIG2 are defined on the back of LED Button device. 
SIG1 connect to LED signal line.
SIG2 connect to button signal line.

## Usage Example
It is really useful to use the LED to show the status of the button.

```python
from grove import grove_led
from grove import grove_button
import board
import time

led = grove_led(board.D0)
led.value = 0
button = grove_button(board.D1)
    
while True:
    while True:
        if button.value != 0:
            break
            
    while True:
        time.sleep(0.1) #filter out jitter interference
        if button.value == 0:
            break
    led.value = not led.value
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
