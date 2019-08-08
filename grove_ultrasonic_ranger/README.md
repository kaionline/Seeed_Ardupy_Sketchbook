# Introduction
This Grove - Ultrasonic ranger is a non-contact distance measurement module which works at 40KHz. When we provide a pulse trigger signal with more than 10uS through singal pin, the Grove_Ultrasonic_Ranger will issue 8 cycles of 40kHz cycle level and detect the echo. The pulse width of the echo signal is proportional to the measured distance. Here is the formula: Distance = echo signal high time * Sound speed (340M/S)/2. Grove_Ultrasonic_Ranger's trig and echo singal share 1 SIG pin.

- [Grove - Ultrasonic ranger](https://www.seeedstudio.com/Grove-Ultrasonic-Ranger-p-960.html)

## Usage Example

```python
from grove import grove_ultra_ranger
import board
import time

ur = grove_ultra_ranger(board.D0)

while True:
    #error:
    #    print ("The distance to obstacles in front is:", ur.cm, "cm", ur.inch, "inches")
    #    the second value (ur.inch) will got zero.
    #reason:
    #    there is a need for some time delay between two adjacent data acquisition
    print ("The distance to obstacles in front is:", ur.cm, "cm")
    #print ("The distance to obstacles in front is:", ur.inch, "inches")
    time.sleep(1)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
