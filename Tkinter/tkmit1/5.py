from tkinter import *
from tkinter import ttk

# languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
#              "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C",
#              "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran"]
#
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# languages_var = StringVar(value=languages)
# listbox = Listbox(listvariable=languages_var)
# listbox.pack(side=LEFT, fill=BOTH, expand=1)
#
# scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# listbox["yscrollcommand"] = scrollbar.set
#
# root.mainloop()

languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go",
             "T-SQL", "PL-SQL", "Typescript"]

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

languages_var = StringVar(value=languages)
listbox = Listbox(listvariable=languages_var)
listbox.pack(expand=1, fill=BOTH)
# сдвигаем скрол на 1 элемент внизу
listbox.yview_scroll(number=1, what="units")

root.mainloop()