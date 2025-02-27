# GUIDELINES
# 1. Install Docker
# 2. Create container
# docker run --rm --it -p 3000:80 -p 2525:25 rnwood/smt4dev

from email.message import EmailMessage
import smtplib

my_email = EmailMessage()

my_email["from"] = "Aye"
my_email["to"] = "test@test.com"
my_email["subject"] = "Hello from Python"
my_email.set_content("Hey! How are you doing?!")

with smtplib.SMTP(host="127.0.0.1", port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was sent!")
