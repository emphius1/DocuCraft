```python
import requests
from docucraft_ai.utils import config, logger, validation

class EcommerceInteraction:
    def __init__(self):
        self.api_key = config.get('ecommerce_api_key')
        self.base_url = config.get('ecommerce_base_url')

    def order_supplies(self, order_details):
        """
        Order supplies related to documentation from an e-commerce platform.
        """
        try:
            validation.validateData(order_details, 'OrderDetailsSchema')
            headers = {'Authorization': f'Bearer {self.api_key}'}
            response = requests.post(f'{self.base_url}/orders', headers=headers, json=order_details)

            if response.status_code != 200:
                logger.logEvent('EcommerceInteraction', 'Failed to order supplies', 'error')
                return None

            logger.logEvent('EcommerceInteraction', 'Successfully ordered supplies', 'info')
            return response.json()

        except Exception as e:
            logger.logEvent('EcommerceInteraction', str(e), 'error')
            return None

    def check_order_status(self, order_id):
        """
        Check the status of an order on the e-commerce platform.
        """
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'}
            response = requests.get(f'{self.base_url}/orders/{order_id}', headers=headers)

            if response.status_code != 200:
                logger.logEvent('EcommerceInteraction', 'Failed to check order status', 'error')
                return None

            logger.logEvent('EcommerceInteraction', 'Successfully checked order status', 'info')
            return response.json()

        except Exception as e:
            logger.logEvent('EcommerceInteraction', str(e), 'error')
            return None
```