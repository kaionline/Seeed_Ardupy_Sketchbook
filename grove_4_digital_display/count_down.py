from grove import grove_4_digital_display
import board
import time

nixie_tube = grove_4_digital_display(board.D0, board.D1)
nixie_tube.show_colon = True

while True:
    for s in range(60, -1, -1):
        for ss in range(59, -1, -1):
            value = s * 100 + ss
            nixie_tube.display(value)
            time.sleep(0.01)
        nixie_tube.show_colon = not nixie_tube.show_colon 
