```python
import openai
from docucraft_ai.utils.config import config
from docucraft_ai.utils.error_handling import handleError
from docucraft_ai.utils.logging import logEvent

openai.api_key = config['openai_api_key']

def generate_document(prompt, max_tokens=1000):
    try:
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=max_tokens
        )
        logEvent('documentGenerated', {'prompt': prompt, 'max_tokens': max_tokens})
        return response.choices[0].text.strip()
    except Exception as e:
        handleError(e)
        return None
```