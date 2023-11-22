```python
# docucraft_ai/pseudo_code_command_list.py

# This file contains a list of pseudo-code style commands that the user can input, 
# along with expected outcomes for each command.

pseudo_code_commands = {
    "create_document": {
        "command": "create_document('Document Title', 'Document Type')",
        "description": "Creates a new document with the specified title and type.",
        "example": "create_document('Project Proposal', 'Proposal')"
    },
    "add_section": {
        "command": "add_section('Section Title')",
        "description": "Adds a new section to the current document with the specified title.",
        "example": "add_section('Introduction')"
    },
    "add_text": {
        "command": "add_text('Text Content')",
        "description": "Adds the specified text to the current section of the document.",
        "example": "add_text('This is the first paragraph of the introduction.')"
    },
    "save_document": {
        "command": "save_document()",
        "description": "Saves the current state of the document.",
        "example": "save_document()"
    },
    "export_document": {
        "command": "export_document('Export Format')",
        "description": "Exports the document in the specified format.",
        "example": "export_document('PDF')"
    }
}

def get_command_list():
    return pseudo_code_commands
```