import requests
import json

url = 'https://www.virustotal.com/api/v3/files/file_id'
headers = {'x-apikey': 'api-key'}

response = requests.get(url, headers=headers)

def threat():
    with open('threat.json', 'w') as f:
        json.dump(response.json(), f, indent=4)
        
threat()


