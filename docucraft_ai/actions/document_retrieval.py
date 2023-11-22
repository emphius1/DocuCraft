```python
import requests
from docucraft_ai.utils.error_handling import handleError
from docucraft_ai.utils.logging import logEvent

def fetchDocument(document_id):
    """
    Fetches a document from a cloud storage service based on the document_id.
    """
    try:
        # Assuming the cloud storage service is Google Drive
        # and we have the API key in the config file
        url = f"https://www.googleapis.com/drive/v3/files/{document_id}?key={config['GOOGLE_DRIVE_API_KEY']}"
        response = requests.get(url)
        response.raise_for_status()

        logEvent(f"Document with ID {document_id} fetched successfully.")
        return response.json()

    except requests.exceptions.HTTPError as err:
        handleError(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        handleError(f"Error occurred: {err}")
```