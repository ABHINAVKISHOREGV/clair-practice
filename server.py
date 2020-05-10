from flask import Flask,jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

cors = CORS(app , resources = {
    r"/*":{
        "Access-Control-Allow-Origin":"*",
        "Access-Control-Allow-Headers":"Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With",
        "Access-Control-Allow-Methods":"POST",
        "Access-Control-Max-Age":"3600"}
    })

@app.route('/')
def home():
    with open('/tmp/artifacts/result.json', "r") as f:
        data= json.load(f) 
    data = jsonify(data)
    return data
app.run()
