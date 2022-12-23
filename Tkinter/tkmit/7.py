from tkinter import *
from tkinter import ttk

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x150")
#
# message = StringVar()
#
# label = ttk.Label(textvariable=message)
# label.pack(anchor=NW, padx=6, pady=6)
#
# entry = ttk.Entry(textvariable=message)
# entry.pack(anchor=NW, padx=6, pady=6)
#
# button = ttk.Button(textvariable=message)
# button.pack(side=LEFT, anchor=N, padx=6, pady=6)
#
# root.mainloop()

# def click_button():
#     value = clicks.get()  # получаем значение
#     clicks.set(value + 1)  # устанавливаем новое значение
#
#
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x150")
#
# clicks = IntVar(value=0)  # значение по умолчанию
#
# btn = ttk.Button(textvariable=clicks, command=click_button)
# btn.pack(anchor=CENTER, expand=1)
#
# root.mainloop()

def check(*args):
    print(name)
    if name.get() == "admin":
        result.set("запрещенное имя")
    else:
        result.set("норм")


root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

name = StringVar()
result = StringVar()

name_entry = ttk.Entry(textvariable=name)
name_entry.pack(padx=5, pady=5, anchor=NW)

check_label = ttk.Label(textvariable=result)
check_label.pack(padx=5, pady=5, anchor=NW)

# отслеживаем изменение значения переменной name
name.trace_add("write", check)

root.mainloop()