from grove import grove_flame
import board
import time

flame   = grove_flame(board.D0)
clock   = 0.1
epsilon = clock / 3
H       = 1
L       = 0

def get_value():
    #because flame.value is L when detected a signal
    #is negtive logical
    if flame.value:
        return L
    return H
    
def wait_for(level):
    while True:
        if get_value() == level:
            break

def wait_start_token():
    wait_for(H)
    wait_for(L)
    print ("start")

def wait_end_token():
    wait_for(L)

#We're using the Manchester encoding.
def get_bit():
    temp = get_value()
    time.sleep(clock + epsilon)
    if temp == get_value():
        wait_for(not temp)
        return H
    else:
        wait_for(temp)
        return L

def get_byte():
    data = 0
    for i in range(0, 8):
        data = (data << 1) | get_bit()
    return data

while True:
    wait_start_token()
    while True:
        value = get_byte()
        if value == 0:
            break
        print (chr(value), end='')
    wait_end_token()
