# Introduction
The Grove-Tilt Switch is the equivalent of a button, and is used as a digital input. Inside the tilt switch is a pair of balls that make contact with the pins when the case is upright. Tilt the case over and the balls don't touch, thus not making a connection. It is wired to the SIG line, NC is not used on this Grove.

- [Grove - Tilt Switch](https://www.seeedstudio.com/Grove-Tilt-Switch-p-771.html)

## Usage Example

```python
from grove import grove_tilt_switch
import board
import time

tilt_switch = grove_tilt_switch(board.SCL)

while True:
    print (tilt_switch.value)
    time.sleep(0.2)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
