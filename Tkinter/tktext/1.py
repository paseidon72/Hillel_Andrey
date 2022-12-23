from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x150")
#
# st = ScrolledText(root, width=50, height=10)
# st.pack(fill=BOTH, side=LEFT, expand=True)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("300x200")
#
# editor = Text(height=5)
# editor.pack(anchor=N, fill=X)
#
# label = ttk.Label()
# label.pack(anchor=N, fill=BOTH)
#
#
# def get_text():
#     label["text"] = editor.get("1.0", "end")
#
#
# button = ttk.Button(text="Click", command=get_text)
# button.pack(side=BOTTOM)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("300x200")
#
# editor = Text(height=10)
# editor.pack(anchor=N, fill=BOTH)
#
#
# def delete_text():
#     editor.delete("1.0", END)
#
#
# button = ttk.Button(text="Clear", command=delete_text)
# button.pack(side=BOTTOM)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("300x200")
#
# editor = Text(height=10)
# editor.pack(anchor=N, fill=BOTH)
# editor.insert("1.0", "мама мыла раму")
#
#
# def edit_text():
#     editor.replace("1.0", "1.4", "дама")
#
#
# button = ttk.Button(text="Replace", command=edit_text)
# button.pack(side=BOTTOM)
#
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

editor = Text(undo=True)
editor.grid(column=0, columnspan=2, row=0, sticky=NSEW)


def undo():
    editor.edit_undo()


def redo():
    editor.edit_redo()


redo_button = ttk.Button(text="Undo", command=undo)
redo_button.grid(column=0, row=1)
clear_button = ttk.Button(text="Redo", command=redo)
clear_button.grid(column=1, row=1)

root.mainloop()