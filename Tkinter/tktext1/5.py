from tkinter import *
from tkinter import ttk

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# # устанавливаем тему "classic"
# ttk.Style().theme_use("classic")
#
# ttk.Button(text="Click").pack(anchor=CENTER, expand=1)
#
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

# выбранная тема
selected_theme = StringVar()
style = ttk.Style()


# изменение текущей темы
def change_theme():
    style.theme_use(selected_theme.get())


ttk.Label(textvariable=selected_theme, font="Helvetica 13").pack(anchor=NW)

for theme in style.theme_names():
    ttk.Radiobutton(text=theme,
                    value=theme,
                    variable=selected_theme,
                    command=change_theme).pack(anchor=NW)

root.mainloop()