from grove import grove_pir_motion_sensor
import board
import time

pir_motion = grove_pir_motion_sensor(board.D0)

while True:
    if pir_motion.value:
        print("enter detect range.")
    else:
        print("level detect range.")
    time.sleep(0.5)
