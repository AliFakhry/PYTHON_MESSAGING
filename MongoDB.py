def add_database(name,mycol):

    input_val = {
        "name": str(name),
    }

    mycol.insert_one(input_val)

def iterate_DB(mycol):

    curr_list = []
    for val in mycol.find():
        curr_list.append(val["name"])

    return curr_list