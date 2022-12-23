from tkinter import *
from tkinter import ttk

# root = Tk()  # создаем корневой объект - окно
# root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
# root.geometry("300x250")  # устанавливаем размеры окна
#
# label = Label(text="Hello METANIT.COM")  # создаем текстовую метку
# label.pack()  # размещаем метку в окне
#
# root.mainloop()
# def finish():
#     root.destroy()  # ручное закрытие окна и всего приложения
#     print("Закрытие приложения")
#
#
# root = Tk()
# root.geometry("250x200")
#
# root.title("Hello METANIT.COM")
# root.protocol("WM_DELETE_WINDOW", finish)
#
# root.mainloop()
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# btn = Button(text="Click")  # создаем кнопку из пакета ttk
# btn.pack()  # размещаем кнопку в окне
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# btn = ttk.Button(text="Click")  # создаем кнопку из пакета ttk
# btn.pack()  # размещаем кнопку в окне
#
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x150")

btn = ttk.Button()
btn.pack()
# устанавливаем параметр text
#btn.config(text="Send Email")
btn["text"] = "Send"
# получаем значение параметра text
btnText = btn["text"]
print(btnText)

root.mainloop()