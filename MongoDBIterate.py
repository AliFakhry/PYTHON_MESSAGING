from pymongo import MongoClient

def iterate_DB(cluster):

    client = MongoClient(cluster)

    mydb = client["myFirstDatabase"]
    mycol = mydb["myFirstDatabase"]

    for val in mycol.find():
        print(val["name"], int(val["number"]))