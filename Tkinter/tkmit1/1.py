from tkinter import *
from tkinter import ttk

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# position = {"padx": 6, "pady": 6, "anchor": NW}
#
# python = "Python"
# java = "Java"
# javascript = "JavaScript"
#
# lang = StringVar(value=java)  # по умолчанию будет выбран элемент с value=java
#
# header = ttk.Label(textvariable=lang)
# header.pack(**position)
#
# python_btn = ttk.Radiobutton(text=python, value=python, variable=lang)
# python_btn.pack(**position)
#
# javascript_btn = ttk.Radiobutton(text=javascript, value=javascript, variable=lang)
# javascript_btn.pack(**position)
#
# java_btn = ttk.Radiobutton(text=java, value=java, variable=lang)
# java_btn.pack(**position)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# position = {"padx": 6, "pady": 6, "anchor": NW}
# languages = ["Python", "JavaScript", "Java", "C#"]
# selected_language = StringVar()  # по умолчанию ничего не выборанно
#
# header = ttk.Label(text="Выберите язык")
# header.pack(**position)
#
#
# def select():
#     header.config(text=f"Выбран {selected_language.get()}")
#
#
# for lang in languages:
#     lang_btn = ttk.Radiobutton(text=lang, value=lang, variable=selected_language, command=select)
#     lang_btn.pack(**position)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# position = {"padx": 6, "pady": 6, "anchor": NW}
#
# python = "Python"
# java = "Java"
# csharp = "C#"
#
# lang = StringVar(value=java)  # по умолчанию будет выбран элемент с value=java
#
# header = ttk.Label(textvariable=lang)
# header.pack(**position)
#
# python_img = PhotoImage(file="./python_sm.png")
# csharp_img = PhotoImage(file="./csharp_sm.png")
# java_img = PhotoImage(file="./java_sm.png")
#
# python_btn = ttk.Radiobutton(value=python, variable=lang, image=python_img)
# python_btn.pack(**position)
#
# csharp_btn = ttk.Radiobutton(value=csharp, variable=lang, image=csharp_img)
# csharp_btn.pack(**position)
#
# java_btn = ttk.Radiobutton(value=java, variable=lang, image=java_img)
# java_btn.pack(**position)
#
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

position = {"padx": 6, "pady": 6, "anchor": NW}

languages = [
    {"name": "Python", "img": PhotoImage(file="./python_sm.png")},
    {"name": "C#", "img": PhotoImage(file="./csharp_sm.png")},
    {"name": "Java", "img": PhotoImage(file="./java_sm.png")}
]

lang = StringVar(value=languages[0]["name"])  # по умолчанию будет выбран элемент с value=python

header = ttk.Label(textvariable=lang)
header.pack(**position)

for l in languages:
    btn = ttk.Radiobutton(value=l["name"], text=l["name"], variable=lang, image=l["img"], compound="top")
    btn.pack(**position)

root.mainloop()