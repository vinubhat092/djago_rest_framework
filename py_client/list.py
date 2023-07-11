import requests


from getpass import getpass
username = input("what is your username?\n")
password = getpass("what is your password\n")
auth_endpoint = "http://127.0.0.1:8000/api/auth/"

auth_response = requests.post(auth_endpoint,json={'username':"vinayak",'password':password})

print("ds",auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization":f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/products/"
    get_response = requests.get(endpoint,headers=headers)

print(get_response.text)
print(get_response.status_code)
print(get_response.json())