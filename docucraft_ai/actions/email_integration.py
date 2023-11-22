```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from docucraft_ai.utils.config import config
from docucraft_ai.utils.logging import logger

def send_email(document, recipient_email):
    try:
        # Setup the email
        msg = MIMEMultipart()
        msg['From'] = config['email']['sender']
        msg['To'] = recipient_email
        msg['Subject'] = "DocuCraft AI Generated Document"

        # Attach the document as a text
        msg.attach(MIMEText(document, 'plain'))

        # Connect to the mail server
        server = smtplib.SMTP(config['email']['smtp_server'], config['email']['smtp_port'])
        server.starttls()

        # Login to the email account
        server.login(config['email']['sender'], config['email']['password'])

        # Send the email
        server.send_message(msg)

        # Disconnect from the server
        server.quit()

        logger.info(f"Email sent to {recipient_email}")

    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        raise e
```