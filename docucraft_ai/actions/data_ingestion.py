```python
import requests
from docucraft_ai.utils.validation import validateData
from docucraft_ai.utils.error_handling import handleError
from docucraft_ai.utils.logging import logEvent

def ingestData(url, schema):
    """
    Function to ingest data from a given URL and validate it against a provided schema.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        handleError(err)
        return None

    data = response.json()

    if not validateData(data, schema):
        logEvent(f"Data from {url} did not match the provided schema.")
        return None

    logEvent(f"Data successfully ingested from {url}.")
    return data
```