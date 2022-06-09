import openpyxl
from MongoDB import add_database
from sendMessage import send_msg
from sendMessage import return_carrier
import os

def iterate_excel(mycol, company, curr_names, email, password):

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
        cust_name = sh.cell(row = j, column= customers_index[1]).value
        cust_number = (sh.cell(row = j, column=numebrs_index[1]).value)
        if cust_name == None or cust_number == None:
            continue
        else:
            new_str = ""
            for i in cust_number:
                if i.isdigit():
                    new_str = new_str + i
            cust_total = (cust_name, new_str)
            if cust_name not in curr_names:
                try:
                    add_database(cust_name, mycol)
                    send_msg(new_str, return_carrier(new_str), cust_name, company, email, password)
                except:
                    continue

    print("\n")
