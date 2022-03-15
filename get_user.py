import requests
from pprint import pprint
_print = print
print = pprint

url = 'https://jsonplaceholder.typicode.com/users/10'

user_data = {
    
}

response = requests.get(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    
    response_data = response.json()
    print(response_data)
    print(response_data['name'])
    print(response_data['email'])


else:
    print(response.status_code)
    print(response.reason)
    print(response.text)