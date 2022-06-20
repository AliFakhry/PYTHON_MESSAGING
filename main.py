from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from parse_cond import primary

def submit(mongo_entry, type_entry, com_entry, clear_entry, send_entry, phone_entry, name_entry, ws):
    if mongo_entry == "" or type_entry == "" or com_entry == "" or clear_entry == "" or (send_entry == "" and type_entry != "TEST"):
        messagebox.showinfo("Information Issue", "FILL ALL THE FIELDS")
    else:
        if type_entry == "TEST" and com_entry != "BETA" and com_entry != "TEST":
            if phone_entry == "" or name_entry == "":
                messagebox.showinfo("Information Issue", "FILL ALL THE FIELDS (TEST)")
            else:
                ws.destroy()
                primary(mongo_entry, type_entry, com_entry, clear_entry, send_entry, phone_entry, name_entry)
        elif type_entry == "TEST" and com_entry == "TEST":
            if phone_entry == "":
                messagebox.showinfo("Information Issue", "FILL ALL THE FIELDS (TEST)")
            else:
                ws.destroy()
                primary(mongo_entry, type_entry, com_entry, clear_entry, send_entry, phone_entry, name_entry)
        elif type_entry == "TEST" and com_entry == "BETA":
            ws.destroy()
            primary(mongo_entry, type_entry, com_entry, clear_entry, send_entry, phone_entry, name_entry)

def main():

    ws = Tk()
    ws.title('Run Program')
    ws.geometry('940x500')

    main_frame = Frame(ws, relief = SOLID)

    left_frame = Frame(main_frame)
    left_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

    right_frame = Frame(main_frame)
    right_frame.grid(row = 0, column = 1,padx= 10, pady = 10)

    bottom_grid = Frame(main_frame)
    bottom_grid.grid(row = 1, column = 1, padx=10, pady=10, sticky = E)


    mongo_Pass = Label(left_frame, text="MongoDB password").grid(row=0, column=0, sticky=W, pady=10)
    send_type = Label(left_frame, text="Send type (REAL/TEST)").grid(row=1, column=0, sticky = W, pady=10)
    company = Label(left_frame, text="Company (or BETA/TEST)").grid(row=2, column=0, sticky = W, pady=10)
    clear_DB = Label(left_frame, text="Clear database").grid(row=3, column=0, sticky = W, pady=10)
    send_msg = Label(left_frame, text="Send messages").grid(row=4, column=0, sticky = W, pady=10)
    phone_input = Label(left_frame, text="Phone (Test)").grid(row=5, column=0, sticky = W, pady=10)
    name_input = Label(left_frame, text="Name (Test)").grid(row=6, column=0, sticky = W, pady=10)


    mongo_entry = Entry(right_frame)
    mongo_entry.grid(row=0, column=0, pady=7, padx=10)

    type_entry = Entry(right_frame)
    type_entry.grid(row=1, column=0, pady=7, padx=10)

    com_entry = Entry(right_frame)
    com_entry.grid(row=2, column=0, pady=7, padx=10)

    clear_entry = Entry(right_frame)
    clear_entry.grid(row=3, column=0, pady=7, padx=10)

    send_entry = Entry(right_frame)
    send_entry.grid(row=4, column=0, pady=7, padx=10)

    phone_entry = Entry(right_frame)
    phone_entry.grid(row=5, column=0, pady=7, padx=10)

    name_entry = Entry(right_frame)
    name_entry.grid(row=6, column=0, pady=7, padx=10)


    sub_button = Button(bottom_grid, text= "Submit", command=lambda :submit(mongo_entry.get(), type_entry.get(),
                                                                            com_entry.get(), clear_entry.get(),
                                                                            send_entry.get(), phone_entry.get(),
                                                                            name_entry.get(), ws))
    sub_button.grid(row =3, column = 0, sticky = E, padx = 10)

    main_frame.pack(expand = 1)

    ws.mainloop()


if __name__ == '__main__':
    main()