def iterate_DB(cluster, mycol):

    curr_list = []

    for val in mycol.find():
        curr_list.append(val["name"])

    return curr_list