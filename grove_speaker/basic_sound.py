from grove import grove_speaker
import board
import time

sound = grove_speaker(board.D0)
sound.value = 0
base = [1911, 1702, 1516, 1431, 1275, 1136, 1012]

def play(index):
    i = 0
    value = base[index]
    
    while i < 200:
        sound.value = not sound.value
        time.sleep_us(value)
        i = i + 1

while True:
    i = 0
    while i < 7:
        play(i)
        time.sleep(0.5)
        i = i + 1

