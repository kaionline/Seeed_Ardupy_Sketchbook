# Introduction
The Grove - Vibration Sensor (SW-420) is a high sensitivity non-directional vibration sensor. When the module is stable, the circuit is turned on and the output is high. When the movement or vibration occurs, the circuit will be briefly disconnected and output low. At the same time, you can also adjust the sensitivity according to your own needs.

- [Grove - Vibration Sensor (SW-420)](https://www.seeedstudio.com/Grove-Vibration-Sensor-SW-420-p-3158.html)

## Usage Example

```python
from grove import grove_vibration_sensor
import board
import time

vibration = grove_vibration_sensor(board.D0)

while True:
    print ("no vibration:", vibration.value)
    time.sleep(1)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
