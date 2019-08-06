# Introduction
3-Axis Digital Accelerometer is the key part in projects like orientation detection, gesture detection and Motion detection. This 3-Axis Digital Accelerometer(±1.5g) is based on Freescale's low power consumption module, MMA7660FC. It features up to 10,000g high shock survivability and configurable Samples per Second rate. For generous applications that don't require too large measurement range, this is a great choice because it's durable, energy saving and cost-efficient.

- [Grove - 3-Axis Digital Accelerometer](https://www.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer-1-5g-p-765.html)

## Usage Example

```python
from grove import grove_3ada
import board
import time

ada = grove_3ada(board.D0)

while True:
    print (
        "x =", ada.x, ",",
        "y =", ada.y, ",", 
        "z =", ada.z
    )
    print (
        "x-a =", ada.x_acceleration, "g,", 
        "y-a =", ada.y_acceleration, "g,", 
        "z-a =", ada.z_acceleration)
    time.sleep(1)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
