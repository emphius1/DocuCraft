```python
from marshmallow import Schema, fields

class CommandSchema(Schema):
    command_name = fields.Str(required=True)
    command_description = fields.Str(required=True)
    command_output = fields.Str(required=True)

user_commands = {}

def process_command(command_input):
    command_schema = CommandSchema()
    try:
        command = command_schema.load(command_input)
        if command['command_name'] in user_commands:
            return user_commands[command['command_name']](command)
        else:
            raise ValueError(f"Command {command['command_name']} not found.")
    except Exception as e:
        return str(e)

def add_command(command_name, command_function):
    if command_name not in user_commands:
        user_commands[command_name] = command_function
    else:
        raise ValueError(f"Command {command_name} already exists.")

def remove_command(command_name):
    if command_name in user_commands:
        del user_commands[command_name]
    else:
        raise ValueError(f"Command {command_name} not found.")
```