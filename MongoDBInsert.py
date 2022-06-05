def add_database(cluster, name,mycol):


    input_val = {
        "name": str(name),
    }

    mycol.insert_one(input_val)