
from flask import Flask, request, jsonify

app = Flask(__name__)

load = 0

@app.route('/charge', methods=['POST'])
def charge():
    global load
    load += 1
    return jsonify({'status': 'charging', 'current_load': load})

@app.route('/metrics', methods=['GET'])
def metrics():
    return f"substation_load {load}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
