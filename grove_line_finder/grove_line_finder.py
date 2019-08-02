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
