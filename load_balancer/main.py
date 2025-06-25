
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SUBSTATIONS = ['http://substation1:7000', 'http://substation2:7000']

@app.route('/route', methods=['POST'])
def route():
    loads = []
    for url in SUBSTATIONS:
        try:
            resp = requests.get(f"{url}/metrics")
            load = int(resp.text.split('substation_load ')[1].split('\n')[0])
            loads.append((load, url))
        except:
            loads.append((9999, url))
    _, target = min(loads, key=lambda x: x[0])
    resp = requests.post(f"{target}/charge", json=request.json)
    return jsonify({'routed_to': target, 'result': resp.json()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
