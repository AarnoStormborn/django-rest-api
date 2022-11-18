import requests

endpoint1 = "http://127.0.0.1:8000/api/apihome"
endpoint2 = "http://127.0.0.1:8000/api/apimodel"
endpoint3 = "http://127.0.0.1:8000/api/restapiview"
endpoint4 = "http://127.0.0.1:8000/api/restapipost"


# get_response = requests.get(endpoint3, params={"abc":123}, json={"query": "Hello World"}) # Making HTTP GET request to this endpoint
# print(get_response.text)
# print(get_response.json())
# print(get_response.status_code)

post_response = requests.post(endpoint4, json={"title":"BlahBlahBlah", "content":"BLAH", "price":250})
print(post_response.json())