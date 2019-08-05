from grove import grove_magnet_switch
import board
import time

magnet_switch = grove_magnet_switch(board.SCL)

while True:
    print (magnet_switch.value)
