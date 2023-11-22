```python
# Import necessary modules
from docucraft_ai.utils.logging import logger

class CommandKeyMap:
    def __init__(self):
        self.command_map = {
            'W': self.up,
            'A': self.left,
            'S': self.down,
            'D': self.right
        }

    def up(self):
        logger.info("Moving up in the document")

    def down(self):
        logger.info("Moving down in the document")

    def left(self):
        logger.info("Moving left in the document")

    def right(self):
        logger.info("Moving right in the document")

    def execute_command(self, command_key):
        if command_key in self.command_map:
            self.command_map[command_key]()
        else:
            logger.error(f"Invalid command key: {command_key}")
```
