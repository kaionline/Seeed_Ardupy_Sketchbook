# Introduction
The Grove - Loudness Sensor is designed to detect the sound of environment. Based on LM2904 amplifier and a built-in microphone, it amplifies and filters the high frequency signal that received from the microphone, and outputs a positive envelop. This is used for Arduino’s signal acquisition. The output value depends on the level of sound input. In order to avoid unnecessary signal disturbances, input signal will go through two times’ filtering inside the module. There is a screw potentiometer that enables manual adjustments to the output gain.

- [Grove - Loudness Sensor](www.seeedstudio.com/Grove-Loudness-Sensor-p-1382.html)

## Usage Example

```python
from grove import grove_loudness_sensor
import board
import time

noise = grove_loudness_sensor(board.A0)

while True:
    print (noise.value)
    time.sleep(0.2)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
