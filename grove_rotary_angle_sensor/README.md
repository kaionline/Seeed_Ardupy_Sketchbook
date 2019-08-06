# Introduction
The rotary angle sensor produces analog output between 0 and Vcc (5V DC with Seeeduino) on its D1 connector. The D2 connector is not used. The angular range is 300 degrees with a linear change in value. The resistance value is 10k ohms, This may also be known as a “potentiometer ”.

- [Grove - Rotary Angle Sensor](https://www.seeedstudio.com/Grove-Rotary-Angle-Sensor-p-770.html)

## Usage Example

```python
from grove import grove_loudness_sensor
import board
import time

rotary_angle = grove_loudness_sensor(board.A0)

def get_angle():
    return rotary_angle.value * 360 / 1023

while True:
    print ("Current rotary angle is", get_angle())
    time.sleep(1)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
