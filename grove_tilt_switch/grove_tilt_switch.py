from grove import grove_tilt_switch
import board
import time

tilt_switch = grove_tilt_switch(board.D0)

while True:
    print (tilt_switch.value)
    time.sleep(0.2)
