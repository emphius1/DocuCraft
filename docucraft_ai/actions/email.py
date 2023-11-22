```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to, from_email, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to, text)
    server.quit()

def receive_feedback(from_email, password, to):
    server = smtplib.IMAP4_SSL("imap.gmail.com")
    server.login(from_email, password)
    server.select('inbox')
    result, data = server.uid('search', None, "ALL")
    latest_email_uid = data[0].split()[-1]
    result, email_data = server.uid('fetch', latest_email_uid, '(BODY.PEEK[TEXT])')
    raw_email = email_data[0][1].decode("utf-8")
    server.logout()

    return raw_email

def incorporate_changes(document, feedback):
    # This is a placeholder function. The actual implementation would depend on the structure of the document and the feedback.
    # For example, if the document and feedback are both text files, this function could simply append the feedback to the document.
    with open(document, 'a') as f:
        f.write('\n' + feedback)
```
