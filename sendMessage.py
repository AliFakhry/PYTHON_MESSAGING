import smtplib, ssl
from providers import PROVIDERS
import requests
import json
from Message_Review import init_message

def send_msg(number, carrier, name, company):

    pass
#
#     message = init_message(number, carrier, name, company)
#     provider = return_carrier(number)
#     if not provider == False:
#         sender_credentials = ("fakhrysms@gmail.com", "edojjjulohwtcgmd")
#         send_sms_via_email(number, message, provider, sender_credentials)

def return_carrier(number):

    request_url = "https://api.telnyx.com/v1/phone_number/1"
    request_url += number
    html = requests.get(request_url).text
    data = json.loads(html)
    carrier = data["carrier"]["name"]
    carrier = carrier.lower()

    if "t-mobile" in carrier or "omnipoint" in carrier or "ultra" in carrier or "metro" in carrier:
        return "T-Mobile"
    elif "sprint" in carrier:
        return "Sprint"
    elif "verizon" in carrier:
        return "Verizon"
    elif "cingular wireless" in carrier or "at&t" in carrier or "cricket" in carrier or "southwestern" in carrier:
        return "AT&T"
    elif "boost" in carrier:
        return "Boost Mobile"
    elif "google" in carrier:
        return "Google Project Fi"
    else:
        return False

def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'
    email_message = f"To:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)