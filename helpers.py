import pickle

def get_data():
    data = ""
    f = open('data.pickle', 'rb')
    while True:
        try:
            data = pickle.load(f)
        except EOFError:
            print("Done reading")
            break
    f.close()
    return data

def save_data(data):
    objList = []
    with open('data.pickle', 'rb+') as f:
        while True:
            try:
                L = pickle.load(f)
                objList.append(L)
            except EOFError:
                print("Done writing")
                break

        f.seek(0)
        f.truncate()

        for i in range(len(objList)):
            pickle.dump(objList[i], f)
        


save_data("test")
print(get_data())