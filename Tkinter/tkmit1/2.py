import re
from tkinter import *
from tkinter import ttk

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
# name_label = ttk.Label(frame, text="Введите имя")
# name_label.pack(anchor=NW)
#
# name_entry = ttk.Entry(frame)
# name_entry.pack(anchor=NW)
#
# frame.pack(anchor=NW, fill=X, padx=5, pady=5)
#
# root.mainloop()

# def create_frame(label_text):
#     frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
#     # добавляем на фрейм метку
#     label = ttk.Label(frame, text=label_text)
#     label.pack(anchor=NW)
#     # добавляем на фрейм текстовое поле
#     entry = ttk.Entry(frame)
#     entry.pack(anchor=NW)
#     # возвращаем фрейм из функции
#     return frame
#
#
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# name_frame = create_frame("Введите имя")
# name_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
#
# email_frame = create_frame("Введите email")
# email_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
#
# root.mainloop()


root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

languages = ["Python", "JavaScript", "C#", "Java"]
languages_var = Variable(value=languages)

languages_listbox = Listbox(listvariable=languages_var)

languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)

root.mainloop()