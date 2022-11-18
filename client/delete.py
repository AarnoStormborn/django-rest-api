import requests

prod_id = int(input("Product ID: "))

endpoint1 = f"http://127.0.0.1:8000/api/products/delete/{prod_id}"

post_response = requests.delete(endpoint1)
print(post_response.status_code)