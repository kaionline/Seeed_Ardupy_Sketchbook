# Introduction
This is a Grove interface compatible Magnetic switch module. It is based on encapsulated dry reed switch CT10. CT10 is single-pole, single throw (SPST) type, having normally open ruthenium contacts. The sensor is a double-ended type and may be actuated with an electromagnet, a permanent magnet or a combination of both. The magnetic switch is a wonderful tool for designers who would like to turn a circuit on and off based on proximity.

- [Grove - Magnetic switch](https://www.seeedstudio.com/Grove-Magnetic-Switch-p-744.html)

## Usage Example

```python
from grove import grove_magnet_switch
import board
import time

magnet_switch = grove_magnet_switch(board.SCL)

while True:
    print (magnet_switch.value)
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
