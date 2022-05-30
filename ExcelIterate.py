import openpyxl
from MongoDBInsert import add_database

def iterate_excel(cluster):

    excel_sheet = openpyxl.load_workbook("Excel_Test.xlsx")

    sh = excel_sheet.active

    for i in range(2, sh.max_row + 1):
        new_arr = []
        print("\n")
        print("Row ", i-1, " data :")
        for j in range(1, sh.max_column + 1):
            cell_obj = sh.cell(row=i, column=j)
            new_arr.append(str(cell_obj.value))
            print(cell_obj.value, end=" ")

        add_database(cluster, new_arr[0], new_arr[1])

    print("\n")