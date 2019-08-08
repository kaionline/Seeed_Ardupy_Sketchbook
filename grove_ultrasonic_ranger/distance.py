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

