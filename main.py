from MongoDB import iterate_DB
from ExcelIterate import iterate_excel
from MongoDB import add_database
from pymongo import MongoClient
from sendMessage import send_msg
from sendMessage import return_carrier

def main():

    password = input("MongoDB Password: ")
    cluster = f"mongodb+srv://Phone_Data:{password}@cluster0.xzech.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(cluster)
    mydb = client["Names"]
    mycol = ""
    prevdb = ""
    email = ""
    pass_word = ""

    send_type = input("TEST OR REAL: ")
    company = input("COMPANY: ")
    if send_type == "TEST":
        if company == "Test":
            mycol = mydb["Test"]
            number = input("PHONE NUMBER: ")
            carrier = return_carrier(number)
            send_msg(number, carrier, "Test", "Exceptional Cleaning")
            add_database("Test", mycol)
        else:
            if company == "Clean and Beyond":
                mycol = mydb["Beyond"]
            elif company == "We Clean Everything":
                mycol = mydb["WCE"]
            elif company == "Bridge City Cleaning":
                mycol = mydb["Bridge"]
                prevdb = mydb["Bridge_Initial"]
                email = "bridgecitycleaningsms@gmail.com"
                pass_word = "yyunsmbscqsjfsez"
                number = input("PHONE NUMBER: ")
                name = input("NAME: ")
                carrier = return_carrier(number)
                send_msg(number, carrier, name, company, email, pass_word)
                add_database(name, mycol)
            elif company == "Exceptional Cleaning":
                mycol = mydb["Exceptional"]
                prevdb = mydb["Exceptional_Cleaning"]
                email = "exceptionalcleaningsms@gmail.com"
                pass_word = "kdwwpdqaegahtafv"
                number = input("PHONE NUMBER: ")
                name = input("NAME: ")
                carrier = return_carrier(number)
                send_msg(number, carrier, name, company, email, pass_word)
                add_database(name, mycol)
    else:
        if company == "Clean and Beyond":
            mycol = mydb["Beyond"]
        elif company == "We Clean Everything":
            mycol = mydb["WCE"]
        elif company == "Bridge City Cleaning":
            mycol = mydb["Bridge"]
            prevdb = mydb["Bridge_Initial"]
            email = "bridgecitycleaningsms@gmail.com"
            pass_word = "yyunsmbscqsjfsez"
        elif company == "Exceptional Cleaning":
            mycol = mydb["Exceptional"]
            prevdb = mydb["Exceptional_Cleaning"]
            email = "exceptionalcleaningsms@gmail.com"
            pass_word = "jhoedjjxlzysgxqq"

    try:
        clear_database = input("CLEAR DATA BASE: ")
        if clear_database == "YES":
            mycol.delete_many({})
    except:
        print("NO DB.")

    send_message = input("SEND MESSAGES (YES/NO) : ")
    if send_message == "YES":
        if send_type != "TEST":
            current_names = iterate_DB(mycol)
            iterate_excel(mycol, prevdb, company, current_names, email, pass_word)

if __name__ == "__main__":
    main()