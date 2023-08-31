import pickle
import uuid
from config import path_prefix

class PickleDataManager:
    def __init__(self, filename):
        self.filename = path_prefix + filename

    def get_devices(self):
        devices = {}
        try:
            with open(self.filename, 'rb') as f:
                while True:
                    try:
                        devices = pickle.load(f)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("File not found")
            return devices
        return devices
    
    def get_device(self, guid):
        devices = self.get_devices()
        try:
            return devices[guid]
        except KeyError:
            return None

    def save_data(self, device):
        devices = self.get_devices()
        devices[device.guid] = device
        with open(self.filename, 'wb') as f:
            pickle.dump(devices, f)

    def as_dict(self):
        temp = {}
        for k,v in self.get_devices().items():
            temp[k] = v.__dict__
        return temp

def get_guid():
    return uuid.uuid4()