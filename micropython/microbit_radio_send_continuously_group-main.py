# Send Continuously to a Group
from microbit import *
import time
import radio
radio.config(group=1)
radio.on()
while True:
    radio.send("Hello")
    

        
    

