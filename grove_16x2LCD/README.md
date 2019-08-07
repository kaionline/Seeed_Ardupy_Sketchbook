# Introduction
The Grove - LCD RGB Backlight has been well received since its inception. Based on customer feedback, now, we bring more cost-effective monochrome backlight derivative for you, i.e., Except for RGB backlights, these three products are almost identical to the the Grove - LCD RGB Backlight, they are all 16 characters wide, 2 rows with high brightness backlight.

- [Grove - 16 x 2 LCD (Black on Yellow)](https://www.seeedstudio.com/Grove-16-x-2-LCD-Black-on-Yellow-p-3198.html)
- [Grove - 16 x 2 LCD (Black on Red)](https://www.seeedstudio.com/Grove-16-x-2-LCD-Black-on-Red-p-3197.html)
- [Grove - 16 x 2 LCD (White on Blue)](https://www.seeedstudio.com/Grove-16-x-2-LCD-White-on-Blue-p-3196.html)

## Usage Example

```python
from grove import grove_16x2_lcd
import time

lcd = grove_16x2_lcd()
lcd.print("Hello world.")
lcd.is_show_cursor = True
i = 0

while True:
    lcd.set_cursor(0, 1) #column 0, row 1
    lcd.print(i)
    time.sleep(0.5)
    i = i + 1
```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
