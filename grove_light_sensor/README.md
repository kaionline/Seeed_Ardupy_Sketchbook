# Introduction
The Grove Light sensor integrates a photo-resistor(light dependent resistor) to detect the intensity of light.

- [Grove - Light Sensor](https://www.seeedstudio.com/Grove-Light-Sensor-v1-2.html)
- [Grove - Red Led Button](https://www.seeedstudio.com/Grove-Red-LED-Button.html)
- [Grove - Blue Led Button](https://www.seeedstudio.com/Grove-Blue-LED-Button.html)
- [Grove - Yellow Led Button](https://www.seeedstudio.com/Grove-Yellow-LED-Button.html)

## Usage Example
The maximum brightness value can be obtained by the vertical illumination of the light on the sensor-plane.  
Like modern street lamps, lighting can be automatically controlled by the light intensity of the current environment  

```python
from grove import grove_led
from grove import grove_light_sensor
import board
import time

led = grove_led(board.D0)
brightness = grove_light_sensor(board.A0)

def get_percentage_of_brightness():
    return float(brightness.value) / 1023 * 100

while True:
    led.value = get_percentage_of_brightness() < 10.0
    time.sleep(1)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
