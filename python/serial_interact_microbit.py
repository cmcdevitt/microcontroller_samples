import serial
import time
import os

# Not necessary
os.system("clear") 

# Serial Communication with a Micro:bit
# The Micro:bit microPython is waiting for input(), echoing it back and looping

ser = serial.Serial('/dev/cu.usbmodem1412',115200,timeout=1)
# Close any existing sessions
ser.close()
ser.open()
#print(f"Serial: {ser}")
# Grab the opening line from the other end
start_msg = ser.readline()
print(f"{start_msg} len:{len(start_msg)}\n")
# Send to an echo program. '\r' end of line for receving end
ser.write("hi\r".encode())
# Read Response
first_read = ser.readline()
print(f"First Read: {first_read} len:{len(first_read)}\n")
# Other wise we could read the message twice
ser.reset_input_buffer()

# Found in miniterm.py
# data = self.serial.read(self.serial.in_waiting or 1)
# Loop through an wait until other end is finished sending
buf_last = 0
buf_current = 0
while ser.in_waiting == 0: #first byte received
    pass
# wait until the input buffer is no longer receiving
buf_current = ser.in_waiting
while buf_current != buf_last:
    buf_last = buf_current
    time.sleep(.100)
    buf_current = ser.in_waiting

# maybe a better way would be to check for /r or /rn?

print(f"Finally! {buf_current}")
print(f"{ser.readline()}")

# Get and send a dynamic response
next_answer = input("Now what? \n")
ser.write(f"{next_answer}\r".encode())
print(f"out: yep{ser.readline()}")

      








