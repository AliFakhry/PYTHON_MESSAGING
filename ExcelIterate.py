import openpyxl
from MongoDBInsert import add_database
from pymongo import MongoClient

def iterate_excel(cluster):

    client = MongoClient(cluster)
    mydb = client["myFirstDatabase"]
    mycol = mydb["myFirstDatabase"]

    mycol.delete_many({})

    excel_sheet = openpyxl.load_workbook("Excel_Test.xlsx")

    sh = excel_sheet.active

    #PPBSa4f3ZwPlI0NC

    for i in range(2, sh.max_row + 1):
        new_arr = []
        print("\n")
        for j in range(1, sh.max_column + 1):
            test_obj = sh.cell(row=1, column=j)
            if str(test_obj.value) == "Name" or str(test_obj.value) == "Number":
                cell_obj = sh.cell(row=i, column=j)
                new_arr.append(str(cell_obj.value))
        add_database(cluster, new_arr[0], new_arr[1])

    print("\n")
