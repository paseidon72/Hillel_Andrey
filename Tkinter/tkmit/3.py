from tkinter import *
from tkinter import ttk

# root = Tk()
# # root.title("METANIT.COM")
# # root.geometry("250x200")
# #
# # # стандартная кнопка
# # btn = ttk.Button(text="Button")
# # btn.pack()
# #
# # root.mainloop()

# clicks = 0
#
#
# def click_button():
#     global clicks
#     clicks += 1
#     # изменяем текст на кнопке
#     btn["text"] = f"Clicks {clicks}"
#
#
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x150")
#
# btn = ttk.Button(text="Click Me", command=click_button)
# btn.pack()
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# btn = ttk.Button(text="Click me")
# btn.pack(expand=True)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# btn1 = ttk.Button(text="BOTTOM")
# btn1.pack(side=BOTTOM)
#
# btn2 = ttk.Button(text="RIGHT")
# btn2.pack(side=RIGHT)
#
# btn3 = ttk.Button(text="LEFT")
# btn3.pack(side=LEFT)

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)

for r in range(3):
    for c in range(3):
        btn = ttk.Button(text=f"({r},{c})")
        btn.grid(row=r, column=c)

root.mainloop()

btn4 = ttk.Button(text="TOP")
btn4.pack(side=TOP)

root.mainloop()