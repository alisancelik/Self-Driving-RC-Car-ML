import socket
import time


class CaptureSensorDataTest(object):
    def __init__(self):
        self.server_address = socket.socket()
        self.server_address.bind(('192.168.1.28', 8002))
        self.server_address.listen(1)
        self.connection, self.client_address = self.server_address.accept()
        self.capture_data()

    def capture_data(self):
        try:
            print("Connection from: ", format(self.client_address))
            start = time.time()

            while True:
                sensor_data = float(self.connection.recv(1024))
                print("Distance: %0.1f cm" % sensor_data)

                # Test for 1 min
                if time.time() - start > 10:
                    break
        finally:
            self.connection.close()
            self.server_address.close()


if __name__ == '__main__':
    CaptureSensorDataTest()
