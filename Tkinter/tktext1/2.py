from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

label = ttk.Label(text="Hello World")
label.pack(anchor=NW, padx=10, pady=10)


def font_changed(font):
    label["font"] = font


def select_font():
    root.tk.call("tk", "fontchooser", "configure", "-font", label["font"], "-command", root.register(font_changed))
    root.tk.call("tk", "fontchooser", "show")


open_button = ttk.Button(text="Выбрать шрифт", command=select_font)
open_button.pack(anchor=NW, padx=10, pady=10)

root.mainloop()