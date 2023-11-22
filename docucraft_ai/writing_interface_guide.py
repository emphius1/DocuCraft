```python
class WritingInterface:
    def __init__(self):
        self.current_document = None

    def create_new_document(self, document_name):
        self.current_document = Document(document_name)
        return self.current_document

    def load_existing_document(self, document_name):
        self.current_document = fetchDocument(document_name)
        return self.current_document

    def save_current_document(self):
        if self.current_document:
            self.current_document.save()
        else:
            raise Exception("No document is currently loaded.")

    def edit_current_document(self, text):
        if self.current_document:
            self.current_document.add_text(text)
        else:
            raise Exception("No document is currently loaded.")

    def format_current_document(self, format_type):
        if self.current_document:
            self.current_document.format(format_type)
        else:
            raise Exception("No document is currently loaded.")

class Document:
    def __init__(self, name):
        self.name = name
        self.text = ""

    def add_text(self, text):
        self.text += text

    def save(self):
        # Save the document to a file or database
        pass

    def format(self, format_type):
        # Apply the specified format to the document
        pass

def fetchDocument(document_name):
    # Fetch the document from a file or database
    pass
```