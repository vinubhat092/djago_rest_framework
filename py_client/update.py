import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update/"

get_response = requests.put(endpoint,params={"abc":123}, json={"title": "hello my old friend"})

print(get_response.text)
print(get_response.status_code)
print(get_response.json())