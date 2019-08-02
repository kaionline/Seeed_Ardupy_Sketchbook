# Introduction
The Hall sensor is based on Hall Effect, which is the production of a voltage difference across an electrical conductor, transverse to an electric current in the conductor and a magnetic field perpendicular to the current.

- [Grove - Holl Sensor](https://www.seeedstudio.com/Grove-Hall-Sensor-p-965.html)

## Usage Example
You can try to get close to the sensor with a magnet.

```python
from grove import grove_hall_sensor
import board
import time

hall_sensor = grove_hall_sensor(board.D0)

while True:
    if hall_sensor.value: #negative logical
        print ("not detected.")
    else:
        print ("detected.")
    time.sleep(1)
```

## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
