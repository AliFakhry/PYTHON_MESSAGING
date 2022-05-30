from pymongo import MongoClient

def add_database(cluster, name, number):

    client = MongoClient(cluster)

    mydb = client["myFirstDatabase"]
    mycol = mydb["myFirstDatabase"]

    input_val = {
        "name": str(name),
        "number": str(number),
    }

    mycol.insert_one(input_val)