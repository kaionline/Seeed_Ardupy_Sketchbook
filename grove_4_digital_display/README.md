# Introduction
Grove - 4-Digit Display module is a 12-pin module. In this module, we utilise a TM1637 to scale down the number of controlling pins to 2. That is to say, it controls both the content and the luminance via only 2 digital pins of Arduino or Seeeduino. For projects that require alpha-numeric display, this can be a nice choice.

- [Grove - 4 Digital Display](https://www.seeedstudio.com/grove-4digital-display-p-1198.html)

## Usage Example

```python
from grove import grove_4_digital_display
import board
import time

nixie_tube = grove_4_digital_display(board.D0, board.D1)
nixie_tube.show_colon = True

while True:
    for s in range(60, -1, -1):
        for ss in range(59, -1, -1):
            value = s * 100 + ss
            nixie_tube.display(value)
            time.sleep(0.01)
        nixie_tube.show_colon = not nixie_tube.show_colon 
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
