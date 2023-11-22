```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for DocuCraft AI."""

    # General Config
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = os.getenv('DEBUG', False)

    # Document Config
    DOCUMENT_STORAGE_PATH = os.getenv('DOCUMENT_STORAGE_PATH', './documents')

    # API Config
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_API_URL = os.getenv('OPENAI_API_URL', 'https://api.openai.com/v1/assistants')

    # Email Config
    EMAIL_SERVER = os.getenv('EMAIL_SERVER')
    EMAIL_PORT = os.getenv('EMAIL_PORT')
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', True)
    EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

    # E-commerce Config
    ECOMMERCE_API_KEY = os.getenv('ECOMMERCE_API_KEY')
    ECOMMERCE_API_URL = os.getenv('ECOMMERCE_API_URL')

config = Config()
```