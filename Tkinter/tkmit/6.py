from tkinter import *
from tkinter import ttk
import re


def is_valid(newval):
    result = re.match("^\+{0,1}\d{0,12}$", newval) is not None
    if not result and len(newval) <= 13:
        errmsg.set("Номер телефона должен быть в формате +xxxxxxxxxxx, где x представляет цифру")
    else:
        errmsg.set("")
    return result


def display():
    label["text"] = phone_entry.get()


def clear():
    phone_entry.delete(0, END)

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

check = (root.register(is_valid), "%P")

errmsg = StringVar()

phone_entry = ttk.Entry(validate="key", validatecommand=check)
phone_entry.pack(padx=5, pady=5, anchor=NW)

error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.pack(padx=5, pady=5, anchor=NW)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
display_button = ttk.Button(text="Display", command=display)
display_button.pack(side=LEFT, anchor=N, padx=6, pady=6)

clear_button = ttk.Button(text="Clear", command=clear)
clear_button.pack(side=LEFT, anchor=N, padx=6, pady=6)

root.mainloop()