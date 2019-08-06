# Introduction

Transmission of information via an infrared transmission and receiving device.
But it's still not good enough, it can't verify whether the data is correct or not, 
are you interested in trying this question?

- [Grove - Infrared Emitter](https://www.seeedstudio.com/Grove-Infrared-Emitter.html)
- [Grove - Infrared Receiver](https://www.seeedstudio.com/Grove-Infrared-Receiver.html)

## Notice

Keeping the infrared transmitter and receiver closer together, 
shaking the sensor when the signal is sent can cause data errors, 
restarting the program will resolve the issue

The light flashes when the infrared receiver receives data, 
if it does not, the source may be too far away from the receiver or the signal is blocked

## Usage Example - FlameSensor


We connect flame sensor to board A, and load this script in device.

```python
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
```
## Usage Example - InfraredEmitter

Next step is connect infrared emitter to board B, and load this script in device.

```python
from grove import grove_led
import board
import time

led     = grove_led(board.D0)
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
```
## Contributing
If you have any good suggestions or comments, you can send issues or PR us.
