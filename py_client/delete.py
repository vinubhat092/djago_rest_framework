import requests

product_id = input("what is the product is you want to use")
print("dad",product_id)
try:
    product_id = int(product_id)
    print("dad",product_id)
except:
    product_id = None
    print(f"{product_id} not a valid id")
if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

get_response = requests.delete(endpoint)


print(get_response.status_code,get_response.status_code==204)
