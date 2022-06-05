import openpyxl
from MongoDBInsert import add_database
import os

def iterate_excel(cluster, mycol):

    open_str = os.path.expanduser("~/Downloads/GetFeedback/Customers.xlsx")
    excel_sheet = openpyxl.load_workbook(open_str)
    sh = excel_sheet.active

    for i in range(6, sh.max_row + 1):
        print("\n")
        for j in range(2, sh.max_column + 1):
            test_obj = sh.cell(row=5, column=j)
            if str(test_obj.value) == "Customer":
                cell_obj = sh.cell(row=i, column=j)
                add_database(cluster, cell_obj.value, mycol)

    print("\n")
