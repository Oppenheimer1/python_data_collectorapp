from email.mime.text import MIMEText
import smtplib

# Change the below from_email and from_password to your email and password and allow apps to access your email for access
def send_email(email, height):
    from_email="email@gmail.com"
    from_password="mypassword"
    to_email=email

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>" % height

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
