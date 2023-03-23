import requests
import json

url = 'https://www.virustotal.com/api/v3/files/c386396ec70db3608075b5fbfaac4ab1ccaa86ba05a68ab393ec551eb66c3e00'
headers = {'x-apikey': '6a9b731b043700d70c9fa646d490e7dcd8132107d76bc8e46bd84b2b438308c7'}

response = requests.get(url, headers=headers)

def threat():
    with open('threat.json', 'w') as f:
        json.dump(response.json(), f, indent=4)
        
threat()


