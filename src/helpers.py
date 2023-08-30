import pickle
import uuid
from config import path_prefix

class PickleDataManager:
    def __init__(self, filename):
        self.filename = path_prefix + filename

    def get_devices(self):
        data = []
        try:
            with open(self.filename, 'rb') as f:
                while True:
                    try:
                        obj = pickle.load(f)
                        data.append(obj)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("File not found")
        return data
    
    def get_device(self, guid):
        data = []
        try:
            with open(self.filename, 'rb') as f:
                while True:
                    try:
                        obj = pickle.load(f)
                        if str(obj.guid) == guid:
                            return obj
                        data.append(obj)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("File not found")

    def save_data(self, data: any):
        with open(self.filename, 'ab') as f:
            pickle.dump(data, f)

def get_guid():
    return uuid.uuid4()