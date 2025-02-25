# GUIDELINES
# 1. Install Docker
# 2. Create container
# docker run --rm --it -p 3000:80 -p 2525:25 rnwood/smt4dev
# 3. Create HTML template in the templates folder
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Email</title>
# </head>
# <body>
#     <h1>Greetings email</h1>
#     <h2>Hello $name, how are you?</h2>
#     <h3>Let's go out $date</h3>
# </body>
# </html>

from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

html_template = Template(Path('templates/template.html').read_text())

html_content = html_template.substitute({'name': 'Bogdan', 'date': 'Sunday'})

my_email = EmailMessage()

my_email['from'] = 'Bogdan'
my_email['to'] = 'test@test.com'
my_email['subject'] = "Hello from Python"
my_email.set_content(html_content, 'html')

with smtplib.SMTP(host='127.0.0.1', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was sent!")
