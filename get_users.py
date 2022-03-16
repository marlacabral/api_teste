import requests
from pprint import pprint
_print = print
print = pprint

def main():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url=url)

    newList = []

    if response.status_code >= 200 and response.status_code <= 299:
        
        response_data = response.json()
        for user in response_data:
            new = user["name"]
            newList.append(new)
            newList.sort()
            user = response_data
        print(newList)
    else:
        print(response.status_code)
        print(response.reason)
        print(response.text)
print("===========================")
main()


def city():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url=url)

    cityList = []

    if response.status_code >= 200 and response.status_code <= 299:
        
        response_data = response.json()
        for city in response_data:
            new = city["address"] ["city"]
            cityList.append(new)
            city = response_data
        print(cityList)
    else:
        print(response.status_code)
        print(response.reason)
        print(response.text)
print("===========================")
city()





def userName():

    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url=url)

    emailList = []
    word = "biz"
    
    if response.status_code >= 200 and response.status_code <= 299:
        
        response_data = response.json()
        
        for email in response_data:
            emailList.append(email['username'])
            emailList.append(email['email'])
            email = response_data
        
        print(emailList[0:2]) 
        print(emailList[12:14]) 
        print(emailList[18:20])        
    else:
        print(response.status_code)
        print(response.reason)
        print(response.text)
print("===========================")

userName()