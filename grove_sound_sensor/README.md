# Introduction
Sound Sensor can detect the sound intensity of the environment.

- [Grove - Sound Sensor](https://www.seeedstudio.com/Grove-Sound-Sensor.html)

## Usage Example
Please make a noise to view the change of the value.

```python
from grove import grove_sound_sensor
import board
import time

sound_sensor = grove_sound_sensor(board.A0)

while True:
    sum = 0
    for i in range(0, 32):
        sum += sound_sensor.value
    avg = sum / 32
    print (avg)
    time.sleep(0.01)
```

## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
