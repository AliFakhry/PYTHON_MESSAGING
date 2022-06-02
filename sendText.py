from main import return_carrier
from main import send_sms_via_email

def send_msg(number):

    message = "Hi"
    provider = return_carrier(number)
    sender_credentials = ("fakhrysms@gmail.com", "edojjjulohwtcgmd")
    send_sms_via_email(number, message, provider, sender_credentials)