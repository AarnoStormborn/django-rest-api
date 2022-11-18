import requests

endpoint1 = "http://127.0.0.1:8000/api/products/"

data = {
    "title":"Hello Hello Hello"
}

post_response = requests.post(endpoint1, json=data)
print(post_response.json())