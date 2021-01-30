from flask import Flask,request, json,jsonify
import os 
import requests

app = Flask(__name__)


@app.route('/api/v1/clay', methods=['GET'])
def micheal_json():
    micheal_info = os.path.join(app.static_folder, 'data', 'Micheal.json')
     with open(micheal_info, 'r') as json_data:
          json_info = json.load(json_data)
          return jsonify(json_info)


@app.route('/')
def index():
    return 'Hello Team edge!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
