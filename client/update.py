import requests

endpoint1 = "http://127.0.0.1:8000/api/products/update/1"

data={
    "title":"Hello Hell",
    "price":45
}

post_response = requests.put(endpoint1, json=data)
print(post_response.json())