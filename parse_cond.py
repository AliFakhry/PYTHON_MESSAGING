from MongoDB import iterate_DB
from ExcelIterate import iterate_excel
from MongoDB import add_database
from pymongo import MongoClient
from sendMessage import send_msg
from sendMessage import return_carrier

def primary(mongo_entry, type_entry, com_entry, clear_entry, send_entry, phone_entry, name_entry):

    cluster = f""
    client = MongoClient(cluster)
    mydb = client["Names"]
    mycol = ""
    prevdb = ""
    email = ""
    pass_word = ""

    if type_entry == "TEST":
        if com_entry == "BETA":
            try:
                mycol = mydb["Beta"]
                current_names = iterate_DB(mycol)
            except:
                current_names = []
            email = ""
            pass_word = ""
            prevdb = mydb[""]
            iterate_excel(mycol, prevdb, com_entry, current_names, email, pass_word)
        elif com_entry == "Test":
            mycol = mydb["Test"]
            carrier = return_carrier(phone_entry)
            send_msg(phone_entry, carrier, "Test", "")
            add_database("Test", mycol)
        else:
            if com_entry == "":
                mycol = mydb[""]
            elif com_entry == "":
                mycol = mydb[""]
            elif com_entry == "":
                mycol = mydb[""]
                prevdb = mydb[""]
                email = ""
                pass_word = ""
                carrier = return_carrier(phone_entry)
                send_msg(phone_entry, carrier, name_entry, com_entry, email, pass_word)
                add_database((name_entry,phone_entry), mycol)
            elif com_entry == "":
                mycol = mydb[""]
                prevdb = mydb[""]
                email = ""
                pass_word = ""
                carrier = return_carrier(phone_entry)
                send_msg(phone_entry, carrier, name_entry, com_entry, email, pass_word)
                add_database((name_entry,phone_entry), mycol)
    elif type_entry == "REAL":
        if com_entry == "":
            mycol = mydb[""]
        elif com_entry == "":
            mycol = mydb[""]
        elif com_entry == "":
            mycol = mydb[""]
            prevdb = mydb[""]
            email = ""
            pass_word = ""
        elif com_entry == "":
            mycol = mydb[""]
            prevdb = mydb[""]
            email = ""
            pass_word = ""

    try:
        if clear_entry == "YES":
            mycol.delete_many({})
    except:
        print("NO DB.")

    if send_entry == "YES":
        if type_entry != "TEST":
            current_names = iterate_DB(mycol)
            iterate_excel(mycol, prevdb, com_entry, current_names, email, pass_word)
