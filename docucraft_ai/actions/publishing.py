```python
import requests

class ContentPublisher:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def publish_document(self, document_content, document_title):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        data = {
            'title': document_title,
            'content': document_content
        }

        response = requests.post(f'{self.base_url}/publish', headers=headers, json=data)

        if response.status_code == 200:
            print(f"Document '{document_title}' has been successfully published.")
        else:
            print(f"Failed to publish document '{document_title}'. Error: {response.text}")
```
This Python code defines a class `ContentPublisher` that can be used to publish documents to a content management system or a website. The `publish_document` method sends a POST request to the `/publish` endpoint of the API, passing the document content and title in the request body. The API key is included in the request headers for authentication. If the request is successful, a success message is printed. If the request fails, an error message is printed.