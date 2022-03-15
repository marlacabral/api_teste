import requests
from pprint import pprint
_print = print


url = 'https://jsonplaceholder.typicode.com/users'

user_data = {
    "nome" : "marla",
    "password" : "123",
    "email" : "marla@email.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.text)
    print(response.json())



else:
    print(response.status_code)
    print(response.reason)
    print(response.text)