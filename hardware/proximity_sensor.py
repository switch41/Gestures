import serial

class ProximitySensor:
    def __init__(self, config):
        self.config = config
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 9600)
        except:
            self.ser = None
            
    def user_present(self):
        if self.ser:
            self.ser.write(b'STATUS\n')
            return self.ser.readline().decode().strip() == 'PRESENT'
        return True  # Fallback for mock

class MockProximitySensor:
    def user_present(self):
        return True