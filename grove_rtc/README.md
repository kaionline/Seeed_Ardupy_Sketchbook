# Introduction
The RTC module is based on the clock chip DS1307, which supports the I2C protocol. It utilizes a Lithium cell battery (CR1225). The clock/calendar provides seconds, minutes, hours, day, date, month, and year. The end of the month date is automatically adjusted for months with fewer than 31 days, including corrections for leap years. The clock operates in either the 24-hour or 12-hour format with AM/PM indicator. And it is valid up to 2100. In order to gain a robust performance, you must put a 3-Volt CR1225 lithium cell in the battery-holder. If you use the primary power only, the module may not work normally, because the crystal may not oscillate.


- [Grove - RTC](https://www.seeedstudio.com/Grove-RTC-p-758.html)

## Usage Example

```python
from grove import grove_rtc
from grove import datetime
import time

rtc = grove_rtc()
rtc.stop()
rtc.datetime = datetime(
    year = 2019, 
    month = 8, 
    day = 7, 
    hour = 14, 
    minute = 45, 
    second = 44
)
rtc.start()

while True:
    tim = rtc.datetime
    print ("Now:" + str(tim.hour) + ":" + str(tim.minute) + ":" + str(tim.second))
    time.sleep(1)

```
## Contributing

If you have any good suggestions or comments, you can send issues or PR us.
