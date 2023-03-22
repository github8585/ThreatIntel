import requests
import json

# collect the threat intellicence data from the API endpoint and store it in their respective variables
url = 'https://www.virustotal.com/api/v3/files/c386396ec70db3608075b5fbfaac4ab1ccaa86ba05a68ab393ec551eb66c3e00'
headers = {'x-apikey': '6a9b731b043700d70c9fa646d490e7dcd8132107d76bc8e46bd84b2b438308c7'}

# make a request to the API endpoint
response = requests.get(url, headers=headers)

# create a function that request to the API Point and saves the data in a json file and saves it in the current directory
def threat():
    with open('threat.json', 'w') as f:
        json.dump(response.json(), f, indent=4)

# call the function
threat()


