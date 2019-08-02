# Introduction
Grove-Line finder is designed for line-following robot. It has an IR emitting LED and an IR sensitive phototransistor. It can output digital signal to a microcontroller so that the robot can follow a black line on white background, or vice versa.

- [Grove - Line Finder](https://www.seeedstudio.com/Grove-Line-Finder-v1-1.html)

## Usage Example
You can try to point the sensor at reflective objects and non-reflective objects, respectively.

```python
from grove import grove_line_finder
import board
import time

line_finder = grove_line_finder(board.D0)

while True:
    if line_finder.value:
        print ("black line detected.")
    else:
        print ("white line detected.")
    time.sleep(1)
```

## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
