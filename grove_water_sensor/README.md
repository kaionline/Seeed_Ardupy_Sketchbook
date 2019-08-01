# Introduction
The water sensor indicates whether the sensor is dry, damp or completely immersed in water by measuring conductivity.

- [Grove - Water Sensor](https://www.seeedstudio.com/Grove-Water-Sensor.html)

## Usage Example
This script can calculate how wet the sensor is.

```python
from grove import grove_water_sensor
import board
import time
import math

presence = grove_water_sensor(board.A0)

def get_percentage_of_moisture():
    return (1023.0 - presence.value) / 1023 * 100

while True:
    print ('current percentage of moisture is {:.2f}%'.format(get_percentage_of_moisture()))
    time.sleep(1)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
