def add_database(cust_total, mycol):

    input_val = {
        "Name": str(cust_total[0]),
        "Number": str(cust_total[1])
    }

    mycol.insert_one(input_val)

def iterate_DB(mycol):

    curr_list = []
    for val in mycol.find():
        curr_list.append(val["Name"])

    return curr_list

def find_num(mycol, name):
    for val in mycol.find():
        if val["Name"] == name:
            return val["Number"]