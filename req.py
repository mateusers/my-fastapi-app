import requests

resp = requests.post('http://127.0.0.1:8000/multiply', json={'number':15})

print(resp)