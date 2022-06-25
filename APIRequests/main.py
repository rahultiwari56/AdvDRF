import requests
# URL = "http://127.0.0.1:8000/api/stuinfo/"
URL = "http://127.0.0.1:8000/api/stuinfo/2"

resp = requests.get(url = URL)
data = resp.json()

print(data)