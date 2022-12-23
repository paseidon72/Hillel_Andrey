from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# languages = ["Python", "C#", "Java", "JavaScript"]
# # по умолчанию будет выбран первый элемент из languages
# languages_var = StringVar(value=languages[0])
#
# label = ttk.Label(textvariable=languages_var)
# label.pack(anchor=NW, padx=6, pady=6)
#
# combobox = ttk.Combobox(textvariable=languages_var, values=languages)
# combobox.pack(anchor=NW, padx=6, pady=6)
#
# print(combobox.get())
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
#
# def selected(event):
#     # получаем выделенный элемент
#     selection = combobox.get()
#     print(selection)
#     label["text"] = f"вы выбрали: {selection}"
#
#
# languages = ["Python", "C#", "Java", "JavaScript"]
# label = ttk.Label()
# label.pack(anchor=NW, fill=X, padx=5, pady=5)
#
# combobox = ttk.Combobox(values=languages, state="readonly")
# combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
# combobox.bind("<<ComboboxSelected>>", selected)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x250")
#
# verticalScale = ttk.Scale(orient=VERTICAL, length=200, from_=1.0, to=100.0, value=50)
# verticalScale.pack()
#
# horizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, value=30)
# horizontalScale.pack()
#
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")


def change(newVal):
    #label["text"] = newVal
    float_value = float(newVal)  # получаем из строки значение float
    int_value = round(float_value)  # округляем до целочисленного значения
    label["text"] = int_value
    # или так
    # label["text"] = scale.get()


label = ttk.Label()
label.pack(anchor=NW)

scale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, command=change)
scale.pack(anchor=NW)

root.mainloop()