from sendMessage import send_msg

def add_database(name,mycol):

    input_val = {
        "name": str(name),
    }

    mycol.insert_one(input_val)