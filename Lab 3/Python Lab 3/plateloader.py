import serial
import time


class PlateLoader:
    def __init__(self, port="/dev/ttyACM0"):
        self.port = port
        self.ser = None

    def connect(self):
        self.ser = serial.Serial(port = self.port, baudrate = 19200, timeout = 15)
        time.sleep(1)
        self.ser.reset_input_buffer()
        
    def disconnect(self):
        self.ser.close()

    def send_command(self, command):
        self.ser.reset_input_buffer
        message_bytes = (command + "\n").encode()
        self.ser.write(message_bytes)

        response_bytes = self.ser.readline()
        response = response_bytes.decode().strip()
        return response

if __name__ == "__main__":
    print("Quick PlateLoader Testing")
    loader = PlateLoader()
    loader.connect()
    response = loader.send_command("RESET")
    print("Response: ", response)
    loader.disconnect()