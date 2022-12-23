from tkinter import *
from tkinter import ttk

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# # создаем набор вкладок
# notebook = ttk.Notebook()
# notebook.pack(expand=True, fill=BOTH)
#
# # создаем пару фреймвов
# frame1 = ttk.Frame(notebook)
# frame2 = ttk.Frame(notebook)
#
# frame1.pack(fill=BOTH, expand=True)
# frame2.pack(fill=BOTH, expand=True)
#
# # добавляем фреймы в качестве вкладок
# notebook.add(frame1, text="Python")
# notebook.add(frame2, text="Java")
#
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)

python_logo = PhotoImage(file="./python_mc.png")
java_logo = PhotoImage(file="./java_mc.png")
# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Python", image=python_logo, compound=LEFT)
notebook.add(frame2, text="Java", image=java_logo, compound=LEFT)

root.mainloop()