from flask import Flask, request, render_template, make_response, send_from_directory
from helpers import PickleDataManager, get_guid
from device import Device
import json
import os

app = Flask(__name__)

@app.route("/testing")
def testing():
    return make_response(json.dumps({'success':True}), 200)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html"), 200

@app.route("/devices", methods=["GET"])
def list_devices():
    p = PickleDataManager("devices.pickle")
    return make_response(p.as_dict(), 200)

@app.route("/register", methods=["POST"])
def register():
    p = PickleDataManager("devices.pickle")
    guid = str(get_guid())
    device = Device(guid)
    p.save_data(device)
    return make_response(json.dumps({'success':True}), 200, {'ContentType':'application/json'})

@app.route("/issuetask", methods=["POST"])
def issue():
    p = PickleDataManager("devices.pickle")
    guid = request.form.get("guid")
    task = request.form.get("task")
    print("User entered task: " + task)
    device = p.get_device(guid)
    print("Before: ", device.tasks)
    device.tasks.append(task)
    print(device.tasks)
    p.save_data(device)
    return make_response(json.dumps({'success':True}), 200, {'ContentType':'application/json'})

@app.route("/listtasks", methods=["POST"])
def list_tasks():
    p = PickleDataManager("devices.pickle")
    guid = request.form.get("guid")
    device = p.get_device(guid)
    if (device == None):
        return make_response("Device not found", 400)
    return make_response([device.tasks, device.guid], 200)

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html", error_code=404, error_text="Not Found"), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("error.html", error_code=405, error_text="Method Not Allowed"), 405

@app.route('/favicon.ico') 
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)