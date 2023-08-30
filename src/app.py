from flask import Flask, request, render_template, make_response, send_from_directory
from helpers import PickleDataManager, get_guid
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
    return make_response(p.get_data(), 200)

@app.route("/register", methods=["POST"])
def register():
    p = PickleDataManager("devices.pickle")
    guid = str(get_guid())
    p.save_data(guid)
    return make_response(json.dumps({'success':True}), 200, {'ContentType':'application/json'})

@app.route("/issuetask", methods=["POST"])
def issue():
    return make_response(json.dumps({'success':True}), 200, {'ContentType':'application/json'})

@app.route("/listtasks", methods=["POST"])
def list_tasks():
    return make_response("task 1, task 2", 200)

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