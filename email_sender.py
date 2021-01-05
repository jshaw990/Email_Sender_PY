# email sender

import smtplib 
from email.message import EmailMessage
from string import Template 
from pathlib import Path 
from datetime import datetime 

now = datetime.now()

current_time = now.strftime('%H:%M')

html = Template(Path('index.html').read_text())
email = EmailMessage() 
email['from'] = 'Jayden Shaw' # Substitute your from name
email['to'] = 'jayden.shaw@gmail.com' # Substitute your to email
email['subject'] = ('Test Message ' + current_time)

email.set_content(html.substitute({
    'name': 'Jayden', # Substitute your to name
    'time': current_time
    }), 'html') 

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() 
    # Subsitute your SMTP Email and Password 
    smtp.login('jayden.shaw.dev@gmail.com', 'python3Script') 
    smtp.send_message(email)
    print('Operation completed. Email sent successfully')