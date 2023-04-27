from microbit import *
import time
import radio
radio.config(group=1)
radio.on()
while True:
    message = radio.receive()
    if message:
        if message.lower() == 'yes':
            display.show(Image.YES)
            time.sleep(5000)
        if message.lower() == 'no':
            display.show(Image.NO)
            time.sleep(5000)
            
    

