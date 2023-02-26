import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'sender's email'
email['to'] = 'email of the person sending'
email['subject'] = 'You won my love!'

email.set_content(html.substitute(name = 'description'), 'html')

with smtplib.SMTP(host='smtp.Outlook.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('user-email', 'password')
    smtp.send_message(email)
    print('all good boss')
