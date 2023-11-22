```python
import requests
from docucraft_ai.utils.error_handling import handleError
from docucraft_ai.utils.logging import logEvent

def publishContent(document, config):
    """
    Function to publish a document to a content management system or a website.
    """
    try:
        # Extract the API endpoint and the API key from the config
        api_endpoint = config['content_publishing']['api_endpoint']
        api_key = config['content_publishing']['api_key']

        # Prepare the headers for the API request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        # Prepare the payload for the API request
        payload = {
            'title': document['title'],
            'content': document['content']
        }

        # Make the API request to publish the document
        response = requests.post(api_endpoint, headers=headers, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            logEvent('documentPublished', document['title'])
            return True
        else:
            handleError('publishContent', response.status_code, response.text)
            return False

    except Exception as e:
        handleError('publishContent', type(e).__name__, str(e))
        return False
```