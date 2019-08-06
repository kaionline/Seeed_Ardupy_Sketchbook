# Introduction
This sensor allows you to sense motion, usually human movement in its range. Simply connect it to Grove - Base shield and program it, when anyone moves in its detecting range, the sensor will output HIGH on its SIG pin.

- [Grove - PIR Motion Sensor](https://www.seeedstudio.com/Grove-PIR-Motion-Sensor-p-802.html)

## Usage Example

```python
from grove import grove_pir_motion_sensor
import board
import time

pir_motion = grove_pir_motion_sensor(board.D0)

while True:
    if pir_motion.value:
        print("enter detect range.")
    else:
        print("level detect range.")
    time.sleep(0.5)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
