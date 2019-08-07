# Introduction
This Temperature&Humidity sensor provides a pre-calibrated digital output. A unique capacitive sensor element measures relative humidity and the temperature is measured by a negative temperature coefficient (NTC) thermistor. It has excellent reliability and long term stability. Please note that this sensor will not work for temperatures below 0 degree.

- [Grove - Temperature & Humidity Sensor (DHT11)](https://www.seeedstudio.com/Grove-Temperature-Humidity-Sensor-DHT11.html)

## Usage Example

```python
from grove import grove_temperature_humidity_sensor
from grove import ic
import board
import time

dth = grove_temperature_humidity_sensor(board.D0, ic.DHT11)

while True:
    print ("Current temperature is", dth.temperature)
    print ("Current humidity is", dth.humidity)
    time.sleep(1)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
