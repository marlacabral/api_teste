import requests
from pprint import pprint
_print = print
print = pprint

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url=url)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    response_data = response.json()
    for user in response_data:
        print(user["name"])
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)