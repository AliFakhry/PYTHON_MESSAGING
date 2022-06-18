from tkinter import *
from tkinter.ttk import *
import tkinter as tk

def main():

    ws = Tk()
    ws.title('Email System')
    ws.geometry('940x500')

    variable = StringVar()
    gender = ('Male', 'Female', 'Other')
    variable.set(gender[0])

    main_frame = Frame(ws, relief = SOLID)

    left_frame = Frame(main_frame)
    left_frame.grid(row = 1, column = 0, padx = 10, pady = 10)

    right_frame = Frame(main_frame)
    right_frame.grid(row = 1, column = 1,padx= 10, pady = 10)

    email_label = Label(left_frame, text="Enter Email").grid(row=0, column=0, sticky=W, pady=10)
    pass_label = Label(left_frame, text="Enter Password").grid(row=1, column=0, sticky = W, pady=10)

    reg_na = Entry(right_frame)
    reg_na.grid(row=0, column=0, pady=10, padx=10)

    reg_em = Entry(right_frame)
    reg_em.grid(row=1, column=0, pady=10, padx=10)
    
    main_frame.pack(expand = 1)

    ws.mainloop()


if __name__ == '__main__':
    main()