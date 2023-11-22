```python
import logging

class ErrorHandling:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.ERROR)
        handler = logging.FileHandler('docucraft_ai.log')
        handler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self, error):
        self.logger.error(error)

    def handle_error(self, error):
        self.log_error(error)
        return {"status": "error", "message": str(error)}
```
This code creates a class `ErrorHandling` that handles errors by logging them and returning a response with the error message. The `log_error` method logs the error, and the `handle_error` method calls `log_error` and then returns a response. The logger is set to log errors to a file named 'docucraft_ai.log'.