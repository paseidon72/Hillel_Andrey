from tkinter import *
from tkinter import ttk

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# spinbox = ttk.Spinbox(from_=1.0, to=100.0)
# spinbox.pack(anchor=NW)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
#
# def change():
#     label["text"] = spinbox.get()
#
#
# label = ttk.Label()
# label.pack(anchor=NW)
#
# spinbox = ttk.Spinbox(from_=1.0, to=100.0, command=change)
# spinbox.pack(anchor=NW)
#
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x150")

spinbox_var = StringVar()

languages = ["Python", "JavaScript", "C#", "Java", "C++"]

label = ttk.Label(textvariable=spinbox_var)
label.pack(anchor=NW)

spinbox = ttk.Spinbox(textvariable=spinbox_var, values=languages)
spinbox.pack(anchor=NW)

root.mainloop()