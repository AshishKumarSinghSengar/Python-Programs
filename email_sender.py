import smtplib

to=input("Enter the email of recipent\n")

subject=input("Enter subject\n")

content=input("Enter your message\n")

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()   
    server.starttls()
    server.login('sendEmail@gmail.com','1234')
    server.sendEmail('sendEmail@gmail.com',to,content)
    server.close()

sendEmail(to,content)