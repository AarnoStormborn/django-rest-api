import requests

endpoint1 = "http://127.0.0.1:8000/api/apihome"
endpoint2 = "http://127.0.0.1:8000/api/apimodel"
endpoint3 = "http://127.0.0.1:8000/api/restapiview"


get_response = requests.get(endpoint3, params={"abc":123}, json={"query": "Hello World"}) # Making HTTP GET request to this endpoint
# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)