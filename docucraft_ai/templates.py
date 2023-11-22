```python
class TemplateSchema:
    def __init__(self, title, body, format):
        self.title = title
        self.body = body
        self.format = format

document_templates = {
    "report": TemplateSchema(
        title="Report Title",
        body="This is a placeholder for the report body.",
        format="pdf"
    ),
    "letter": TemplateSchema(
        title="Letter Title",
        body="This is a placeholder for the letter body.",
        format="docx"
    ),
    "code_documentation": TemplateSchema(
        title="Code Documentation Title",
        body="This is a placeholder for the code documentation body.",
        format="md"
    )
}

def select_template(template_name):
    if template_name in document_templates:
        return document_templates[template_name]
    else:
        raise ValueError(f"No template found for {template_name}")
```