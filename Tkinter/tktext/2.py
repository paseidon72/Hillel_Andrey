from tkinter import *
from tkinter import ttk

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
#
# def get_selection():
#     label["text"] = editor.selection_get()
#
#
# def clear_selection():
#     editor.selection_clear()
#
#
# editor = Text(height=5)
# editor.pack(fill=X)
#
# label = ttk.Label()
# label.pack(anchor=NW)
#
# get_button = ttk.Button(text="Get selection", command=get_selection)
# get_button.pack(side=LEFT)
# clear_button = ttk.Button(text="Clear", command=clear_selection)
# clear_button.pack(side=RIGHT)
#
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

editor = Text(wrap="none")
editor.pack(expand=1, fill=BOTH)
editor.insert("1.0", "Hello ")
# создаем тег highlightline и прикрепляем его к символам 1.0 до 1.2
editor.tag_add("highlightline", "1.0", "1.2")
# добавляем текст, к которому применяется тег highlightline
editor.insert("end", "World", "highlightline")
editor.insert("end", "\nHello All!")
# устанавливаем стили тега highlightline
editor.tag_configure("highlightline", background="#ccc", foreground="red", font="TkFixedFont", relief="raised")

root.mainloop()