import openpyxl
from MongoDBInsert import add_database
import os

def iterate_excel(mycol, company, curr_names):

    open_str = os.path.expanduser(f"~/Downloads/GetFeedback/{company}/Customers.xlsx")
    excel_sheet = openpyxl.load_workbook(open_str)
    sh = excel_sheet.active

    customers_index = False
    numebrs_index = False
    start_index = False


    for i in range(1, sh.max_row + 1):
        for j in range(1, sh.max_column + 1):
            if sh.cell(row = i, column= j).value == "Customer":
                customers_index = (i+1,j)
                start_index = i+1
            if sh.cell(row = i, column= j).value == "Phone Numbers":
                numebrs_index = (i+1, j)
                start_index = i+1

    for j in range(start_index, sh.max_row+1):
        print(j)
        cust_name = sh.cell(row = j, column= customers_index[1]).value
        cust_number = sh.cell(row = j, column=numebrs_index[1]).value
        cust_total = (cust_name, cust_number)
        print(cust_total)

    print("\n")
