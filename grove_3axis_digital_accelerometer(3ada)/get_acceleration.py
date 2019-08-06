from grove import grove_3ada
import board
import time

ada = grove_3ada(board.D0)

while True:
    print (
        "x =", ada.x, ",",
        "y =", ada.y, ",", 
        "z =", ada.z
    )
    print (
        "x-a =", ada.x_acceleration, "g,", 
        "y-a =", ada.y_acceleration, "g,", 
        "z-a =", ada.z_acceleration)
    time.sleep(1)
