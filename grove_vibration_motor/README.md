# Introduction
This is a mini vibration motor suitable as a non-audible indicator. When the input is HIGH, the motor will vibrate just like your cell phone on silent mode.

- [Grove - Vibration Motor](https://www.seeedstudio.com/Grove-Vibration-Motor-p-839.html)

## Usage Example

```python
from grove import grove_vibration_motor
import board
import time

vibration_motor = grove_vibration_motor(board.D0)
vibration_motor.value = 0

while True:
    vibration_motor.value = not vibration_motor.value
    time.sleep(1)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
