from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

# tree = ttk.Treeview(show="tree")
# tree.pack(expand=1, fill=BOTH)
tree = ttk.Treeview()
# установка заголовка
tree.heading("#0", text="Отделы", anchor=NW)
tree.pack(expand=1, fill=BOTH)

# добавляем отделы
tree.insert("", END, iid=1, text="Административный отдел", open=True)
tree.insert("", END, iid=2, text="IT-отдел")
tree.insert("", END, iid=3, text="Отдел продаж")

# добавим сотрудников отдела
tree.insert(1, index=END, text="Tom")
tree.insert(2, index=END, text="Bob")
tree.insert(2, index=END, text="Sam")

root.mainloop()