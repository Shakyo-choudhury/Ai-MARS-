from email import message
import smtplib
from  email.message import EmailMessage
from my_inputs import talk, take_command
from my_send_email import send_email
email_list={'shakyo':'officialshakyo@gmail.com', 'moumita': 'moumita.deb.choudhury@gmail.com'}
def get_email_info():
    talk('to whom do you want to send the mail')
    name=take_command()
    receiver= email_list[name]
    print(receiver)
    talk("what is the subject of your email")
    subject=take_command()
    talk("tell me your message")
    message=take_command()
    send_email(receiver, subject, message)
    talk("email sent")
if __name__==("__main__"):
    get_email_info()