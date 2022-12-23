from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")


def selected(event):
    # получаем индексы выделенных элементов
    selected_indices = languages_listbox.curselection()
    # получаем сами выделенные элементы
    selected_langs = ",".join([languages_listbox.get(i) for i in selected_indices])
    msg = f"вы выбрали: {selected_langs}"
    selection_label["text"] = msg


languages = ["Python", "JavaScript", "C#", "Java"]
languages_var = Variable(value=languages)

selection_label = ttk.Label()
selection_label.pack(anchor=NW, fill=X, padx=5, pady=5)

languages_listbox = Listbox(listvariable=languages_var, selectmode=EXTENDED)
languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
languages_listbox.bind("<<ListboxSelect>>", selected)

root.mainloop()