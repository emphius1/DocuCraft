```python
import os
from google.cloud import storage

class DocumentRetrieval:
    def __init__(self):
        self.storage_client = storage.Client()
        self.bucket_name = os.getenv('CLOUD_STORAGE_BUCKET')

    def retrieve_document(self, document_name):
        bucket = self.storage_client.get_bucket(self.bucket_name)
        blob = storage.Blob(document_name, bucket)
        content = blob.download_as_text()
        return content

    def list_documents(self):
        bucket = self.storage_client.get_bucket(self.bucket_name)
        blobs = bucket.list_blobs()
        document_names = [blob.name for blob in blobs]
        return document_names
```