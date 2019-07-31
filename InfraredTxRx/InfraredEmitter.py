from grove import grove_led
import board
import time

led     = grove_led(board.SCL)
clock   = 0.1
H       = 1
L       = 0

def set_bit(level):
    if level == H:
        time.sleep(clock * 2)
    else:
        time.sleep(clock)
        led.value = not led.value
        time.sleep(clock)
    led.value = not led.value

def start_token():
    time.sleep(clock)
    led.value = H
    time.sleep(clock)
    led.value = L

def end_token():
    time.sleep(clock)
    if led.value:
        led.value = L
        time.sleep(clock)

def send_byte(value):
    for i in range(0, 8):
        bit = value & 0x80 != 0
        set_bit(bit)
        value = value << 1

def send_string(value):
    for char in value:
        send_byte(ord(char))
    send_byte(0x00) #end string

while True:
    start_token()
    send_string('I Love Coding.')
    end_token()
