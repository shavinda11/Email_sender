import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'shavinda_p@hotmail.com'
email['to'] = 'ishadi.up@gmail.com'
email['subject'] = 'You won my love!'

email.set_content(html.substitute(name = 'Ishadi ❤❤❤'), 'html')

with smtplib.SMTP(host='smtp.Outlook.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('shavinda_p@hotmail.com', 'imalawyer2023')
    smtp.send_message(email)
    print('all good boss')