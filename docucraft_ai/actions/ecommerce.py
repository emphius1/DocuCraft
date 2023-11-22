```python
import requests

class EcommerceInteraction:
    def __init__(self, api_key):
        self.api_key = api_key

    def order_supplies(self, item_id, quantity):
        url = f"https://ecommerceapi.com/order?item_id={item_id}&quantity={quantity}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to order supplies: {response.text}")

    def get_order_status(self, order_id):
        url = f"https://ecommerceapi.com/order/{order_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get order status: {response.text}")
```