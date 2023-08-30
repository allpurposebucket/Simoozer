import pickle
import uuid

class PickleDataManager:
    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        data = []
        try:
            with open(self.filename, 'rb') as f:
                while True:
                    try:
                        obj = pickle.load(f)
                        data.append(obj)
                        print(data)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("File not found")
        return data

    def save_data(self, data: any):
        with open(self.filename, 'ab') as f:
            pickle.dump(data, f)

def get_guid():
    return uuid.uuid4()