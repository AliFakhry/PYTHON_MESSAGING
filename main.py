import smtplib, ssl
from providers import PROVIDERS
import requests
import json
from MongoDBIterate import iterate_DB
from ExcelIterate import iterate_excel
from Message_Review import init_message
from pymongo import MongoClient

def main():

    company = input("Enter the company: ")
    password = input("MongoDB Password: ")
    cluster = f"mongodb+srv://Phone_Data:{password}@cluster0.xzech.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(cluster)
    mydb = client["Names"]

    if company == "Beyond":
        mycol = mydb["Beyond"]
    elif company == "WCE":
        mycol = mydb["WCE"]
    elif company == "Bridge":
        mycol = mydb["Bridge"]
    elif company == "Exceptional":
        mycol = mydb["Exceptional"]

    mycol.delete_many({})
    current_names = iterate_DB(mycol)

    iterate_excel(mycol, company, current_names)

    phone_num = str(input("INPUT PHONE NUMBER: "))

if __name__ == "__main__":
    main()