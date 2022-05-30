import smtplib, ssl
from providers import PROVIDERS
import requests
import json
from pymongo import MongoClient
from MongoDBIterate import iterate_DB
from MongoDBInsert import add_database
from ExcelIterate import iterate_excel

def return_carrier(number):

    request_url = "https://api.telnyx.com/v1/phone_number/1"
    request_url += number
    html = requests.get(request_url).text
    data = json.loads(html)
    carrier = data["carrier"]["name"]
    carrier = carrier.lower()

    if "t-mobile" in carrier or "omnipoint" in carrier:
        return "T-Mobile"
    elif "verizon" in carrier:
        return "Verizon"
    elif "cingular wireless" in carrier or "at&t" in carrier:
        return "AT&T"

def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
    subject: str = "AUTOMATED MESSAGE:"
):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)

def main():

    password = input("MongoDB Password: ")
    cluster = f"mongodb+srv://Phone_Data:{password}@cluster0.xzech.mongodb.net/?retryWrites=true&w=majority"

    iterate_excel(cluster)

    number = input("PHONE NUMBER: ")
    message = "HI!"
    provider = return_carrier(number)

    print(provider)

    sender_credentials = ("fakhrysms@gmail.com", "edojjjulohwtcgmd")

    send_sms_via_email(number, message, provider, sender_credentials)


if __name__ == "__main__":
    main()