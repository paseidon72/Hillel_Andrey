from tkinter import *
from tkinter import ttk

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("300x250")
#
# canvas = Canvas(bg="white", width=250, height=200)
# canvas.pack(anchor=CENTER, expand=1)
#
# canvas.create_line(10, 10, 200, 50, activefill="red", fill="blue", dash=2)
# canvas.create_line(10, 50, 200, 90, activefill="red", fill="blue", dash=2)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("300x250")
#
# canvas = Canvas(bg="white", width=250, height=200)
# canvas.pack(anchor=CENTER, expand=1)
#
# canvas.create_rectangle(10, 20, 200, 60, fill="#80CBC4", outline="#004D40")
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# h = ttk.Scrollbar(orient=HORIZONTAL)
# v = ttk.Scrollbar(orient=VERTICAL)
# canvas = Canvas(scrollregion=(0, 0, 1000, 1000), bg="white", yscrollcommand=v.set, xscrollcommand=h.set)
# h["command"] = canvas.xview
# v["command"] = canvas.yview
#
# canvas.grid(column=0, row=0, sticky=(N, W, E, S))
# h.grid(column=0, row=1, sticky=(W, E))
# v.grid(column=1, row=0, sticky=(N, S))
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)
#
# canvas.create_rectangle(10, 10, 300, 300, fill="red")
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("300x250")
#
# y = 0
# direction = -10
# btn_height = 40
# canvas_height = 200
#
# canvas = Canvas(bg="white", width=250, height=canvas_height)
# canvas.pack(anchor=CENTER, expand=1)
#
#
# def cliked_button():
#     global y, direction
#     if y >= canvas_height - btn_height or y <= 0:
#         direction = direction * -1
#     y = y + direction
#     canvas.coords(btnId, 10, y)
#
#
# btn = ttk.Button(text="Click", command=cliked_button)
# btnId = canvas.create_window(10, y, anchor=NW, window=btn, width=100, height=btn_height)
#
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("300x250")

red = "red"
blue = "blue"

selected_color = StringVar(value=red)

canvas = Canvas(bg="white", width=250, height=150)
canvas.pack(anchor=CENTER, expand=1)


def select():
    canvas.itemconfigure(line, fill=selected_color.get())


red_btn = ttk.Radiobutton(text=red, value=red, variable=selected_color, command=select, padding=6)
red_btn.pack(anchor=NW)
blue_btn = ttk.Radiobutton(text=blue, value=blue, variable=selected_color, command=select, padding=6)
blue_btn.pack(anchor=NW)

line = canvas.create_line(10, 10, 200, 100, fill=selected_color.get())

root.mainloop()