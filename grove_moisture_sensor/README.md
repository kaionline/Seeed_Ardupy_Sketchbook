# Introduction
This Moisture Senor can be used for detecting the moisture of soil or judge if there is water around the sensor.  
In modern agriculture, we can accurately control drip irrigation by detecting soil moisture content.

- [Grove - Moisture Senser](https://www.seeedstudio.com/Grove-Moisture-Sensor.html)

## Usage Example
You can try to insert the sensor into the soil to detect the moisture.

```python
from grove import grove_moisture_sensor
import board
import time

moisture_sensor = grove_moisture_sensor(board.A0)

while True:
    print (moisture_sensor.value)
    time.sleep(1)
```

## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
