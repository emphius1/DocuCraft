```python
from marshmallow import Schema, fields, ValidationError

class DocumentSchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    format = fields.Str(required=True)
    author = fields.Str(required=True)

class CommandSchema(Schema):
    command = fields.Str(required=True)
    parameters = fields.Dict(required=True)

class ActionSchema(Schema):
    action = fields.Str(required=True)
    parameters = fields.Dict(required=True)

def validate_data(schema, data):
    try:
        schema.load(data)
    except ValidationError as e:
        return False, e.messages
    return True, None
```