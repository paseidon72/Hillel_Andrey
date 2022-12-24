from tkinter import *
from tkinter import ttk

# root = Tk()
# # root.title("METANIT.COM")
# # root.geometry("250x250")
# #
# # red = "red"
# # blue = "blue"
# # green = "green"
# # selected_color = StringVar(value=red)
# #
# # canvas = Canvas(bg="white", width=250, height=150)
# # canvas.pack(anchor=NW)
# #
# # canvas.create_rectangle((10, 80, 130, 130), fill=selected_color.get(), outline="black", tags="house")
# # canvas.create_polygon((10, 80), (70, 30), (130, 80), fill=selected_color.get(), outline="black", tags="house")
# #
# #
# # def select():
# #     canvas.itemconfigure("house", fill=selected_color.get())
# #
# #
# # ttk.Radiobutton(text=red, value=red, variable=selected_color, command=select, padding=6).pack(anchor=NW)
# # ttk.Radiobutton(text=blue, value=blue, variable=selected_color, command=select, padding=6).pack(anchor=NW)
# # ttk.Radiobutton(text=green, value=green, variable=selected_color, command=select, padding=6).pack(anchor=NW)
# #
# # root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

canvas = Canvas(bg="white", width=250, height=150)
canvas.pack(fill=BOTH, expand=1)

# размеры прямоугольника
big_size = (60, 60, 150, 150)
small_size = (60, 60, 100, 100)


# обработчики событий
def make_big(event):
    canvas.coords(id, big_size)


def make_small(event):
    canvas.coords(id, small_size)


id = canvas.create_rectangle(small_size, fill="red")
# привязка событий к элементу с идентификатором id
canvas.tag_bind(id, "<Enter>", make_big)
canvas.tag_bind(id, "<Leave>", make_small)

root.mainloop()