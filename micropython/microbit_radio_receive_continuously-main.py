from microbit import *
import time
import radio
radio.config(group=1)
radio.on()
while True:
    message = radio.receive()
    if message:
        print(message)
    

        
    

