from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# enabled = IntVar()
#
# enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled)
# enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
#
# enabled_label = ttk.Label(textvariable=enabled)
# enabled_label.pack(padx=6, pady=6, anchor=NW)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
#
# def checkbutton_changed():
#     if enabled.get() == 1:
#         showinfo(title="Info", message="Включено")
#     else:
#         showinfo(title="Info", message="Отключено")
#
#
# enabled = IntVar()
#
# enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled, command=checkbutton_changed)
# enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
#
# def checkbutton_changed():
#     showinfo(title="Info", message=enabled.get())
#
#
# enabled = StringVar()
#
# enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled, offvalue="Отключено", onvalue="Включено",
#                                       command=checkbutton_changed)
# enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# enabled_on = "Включено"
# enabled_off = "Отключено"
# enabled = StringVar(value=enabled_on)
#
# enabled_checkbutton = ttk.Checkbutton(textvariable=enabled, variable=enabled, offvalue=enabled_off, onvalue=enabled_on)
# enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
#
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")


def select():
    result = "Выбрано: "
    if python.get() == 1: result = f"{result} Python"
    if javascript.get() == 1: result = f"{result} JavaScript"
    if java.get() == 1: result = f"{result} Java"
    languages.set(result)


position = {"padx": 6, "pady": 6, "anchor": NW}

languages = StringVar()
languages_label = ttk.Label(textvariable=languages)
languages_label.pack(**position)

python = IntVar()
python_checkbutton = ttk.Checkbutton(text="Python", variable=python, command=select)
python_checkbutton.pack(**position)

javascript = IntVar()
javascript_checkbutton = ttk.Checkbutton(text="JavaScript", variable=javascript, command=select)
javascript_checkbutton.pack(**position)

java = IntVar()
java_checkbutton = ttk.Checkbutton(text="Java", variable=java, command=select)
java_checkbutton.pack(**position)

root.mainloop()