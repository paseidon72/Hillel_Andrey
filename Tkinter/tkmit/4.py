from tkinter import *
from tkinter import ttk

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
#
# def entered(event):
#     btn["text"] = "Entered"
#
#
# def left(event):
#     btn["text"] = "Left"
#
#
# btn = ttk.Button(text="Click")
# btn.pack(anchor=CENTER, expand=1)
#
# btn.bind("<Enter>", entered)
# btn.bind("<Leave>", left)
#
# root.mainloop()

# clicks = 0
#
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")


# def clicked(event):
#     global clicks
#     clicks = clicks + 1
#     btn["text"] = f"{clicks} Yes"
#
#
# btn = ttk.Button(text="Click")
# btn.pack(anchor=CENTER, expand=1)
#
# # привязка события к кнопкам ttk.Button
# root.bind_class("TButton", "<Double-ButtonPress-1>", clicked)
#
# root.mainloop()

def show_message():
    label["text"] = entry.get()  # получаем введенный текст


root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()