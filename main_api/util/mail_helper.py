from main_api import sg
import os
from sendgrid.helpers.mail import *

def send_email(receiver):
    from_email = Email("leongjinqwen@gmail.com")
    to_email = Email(receiver)
    subject = "Thanks for signing up!"
    content = Content("text/html", f"<h1>Welcome to Photofy,</h1> <br/>More features coming soon!<br/><h1>Photofy</h1>")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

def reset_password_email(user,user_password):
    from_email = Email("leongjinqwen@gmail.com")
    to_email = Email(user.email)
    subject = "Reset your password"
    content = Content("text/html", f"<h1>Dear {user.username},</h1><br/>Here is your new password <h4>{user_password}</h4>Remember to update it after login to your account.<br/><br/><h1>Photofy</h1>")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    
        
