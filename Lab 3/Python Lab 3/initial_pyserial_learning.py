import serial
import time

ser = serial.Serial("/dev/ttyACM0", 19200, timeout=10)

time.sleep(1.0) # Necessary sometimes :)

ser.reset_input_buffer()
message = "RESET"
message_bytes = (message + "\n").encode()

ser.write(message_bytes)

response_bytes = ser.readline()
print(response_bytes)
response = response_bytes.decode().strip()
print(response)


ser.close()