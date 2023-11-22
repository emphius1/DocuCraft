```python
class MainMenu:
    def __init__(self):
        self.menu_options = {
            "1": {
                "name": "Create Document",
                "command": "createDocument",
                "description": "Create a new document using a predefined template."
            },
            "2": {
                "name": "Edit Document",
                "command": "editDocument",
                "description": "Edit an existing document."
            },
            "3": {
                "name": "Save Document",
                "command": "saveDocument",
                "description": "Save the current document."
            },
            "4": {
                "name": "Load Document",
                "command": "loadDocument",
                "description": "Load a document from storage."
            },
            "5": {
                "name": "Publish Document",
                "command": "publishDocument",
                "description": "Publish the current document to a content management system."
            },
            "6": {
                "name": "Send Document via Email",
                "command": "sendEmail",
                "description": "Send the current document via email."
            },
            "7": {
                "name": "Interact with E-commerce",
                "command": "interactWithEcommerce",
                "description": "Interact with e-commerce platforms for documentation-related services."
            },
            "8": {
                "name": "Exit",
                "command": "exit",
                "description": "Exit the application."
            }
        }

    def display_menu(self):
        print("\nMain Menu:")
        for key, option in self.menu_options.items():
            print(f"{key}. {option['name']}: {option['description']}")

    def get_command(self, option_key):
        return self.menu_options.get(option_key, {}).get('command', None)
```