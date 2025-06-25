
import requests
import time

URL = 'http://localhost:5000/charge'

for i in range(20):
    resp = requests.post(URL, json={'vehicle_id': i})
    print(f"Request {i}: {resp.json()}")
    time.sleep(0.1)
