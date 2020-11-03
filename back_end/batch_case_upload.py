import requests
import json

url='http://localhost:8001/create/civil_cases/'
with open('civil_cases.json') as json_file:
    data = json.load(json_file)

    for d in data:
            print(requests.post(url, data=d).status_code)

url='http://localhost:8001/create/crim_cases/'
with open('crim_cases.json') as json_file:
    data = json.load(json_file)

    for d in data:
            print(requests.post(url, data=d).status_code)
