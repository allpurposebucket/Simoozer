from flask import Flask

app = Flask(__name__)

@app.route("/devices")
def get_devices():
    return "device 1, device 3"

if __name__ == "__main__":
    app.run()