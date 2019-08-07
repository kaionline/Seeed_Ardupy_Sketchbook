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

