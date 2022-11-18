import requests

endpoint1 = "http://127.0.0.1:8000/api/products/1"
endpoint2 = "http://127.0.0.1:8000/api/products/mixinlist/1"

post_response = requests.post(endpoint2)
print(post_response.json())