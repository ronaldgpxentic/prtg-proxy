from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Datos de tu cuenta PRTG Cloud
PRTG_HOST = "https://reporteria.my-prtg.com"
USERNAME = "ronaldgpxentic@gmail.com"
PASSHASH = "3851515788"

@app.route("/")
def index():
    return {"status": "online", "info": "PRTG Proxy working"}

@app.route("/sensors")
def get_sensors():
    url = f"{PRTG_HOST}/api/table.json"
    params = {
        "content": "sensors",
        "columns": "objid,group,device,sensor,lastvalue,status,message",
        "username": USERNAME,
        "passhash": PASSHASH
    }
    response = requests.get(url, params=params)
    return jsonify(response.json())
