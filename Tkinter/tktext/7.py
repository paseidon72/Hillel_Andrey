from tkinter import *
from tkinter import ttk

# root = Tk()
# # root.title("METANIT.COM")
# # root.geometry("250x200")
# #
# #
# # def click():
# #     window = Tk()
# #     window.title("Новое окно")
# #     window.geometry("250x200")
# #     label = ttk.Label(window, text="Принципиально новое окно")
# #     label.pack(anchor=CENTER, expand=1)
# #     close_button = ttk.Button(window, text="Закрыть окно", command=lambda: window.destroy())
# #     close_button.pack(anchor="center", expand=1)
# #
# #
# # button = ttk.Button(text="Создать окно", command=click)
# # button.pack(anchor=CENTER, expand=1)
# #
# # root.mainloop()

# class Window(Tk):
#     def __init__(self):
#         super().__init__()
#
#         # конфигурация окна
#         self.title("Новое окно")
#         self.geometry("250x200")
#
#         # определение кнопки
#         self.button = ttk.Button(self, text="закрыть")
#         self.button["command"] = self.button_clicked
#         self.button.pack(anchor="center", expand=1)
#
#
#     def button_clicked(self):
#         self.destroy()
#
#
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
#
# def click():
#     window = Window()
#
#
# open_button = ttk.Button(text="Создать окно", command=click)
# open_button.pack(anchor="center", expand=1)
#
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")


def dismiss(window):
    window.grab_release()
    window.destroy()


def click():
    window = Toplevel()
    window.title("Новое окно")
    window.geometry("250x200")
    window.protocol("WM_DELETE_WINDOW", lambda: dismiss(window))  # перехватываем нажатие на крестик
    close_button = ttk.Button(window, text="Закрыть окно", command=lambda: dismiss(window))
    close_button.pack(anchor="center", expand=1)
    window.grab_set()  # захватываем пользовательский ввод


open_button = ttk.Button(text="Создать окно", command=click)
open_button.pack(anchor="center", expand=1)

root.mainloop()