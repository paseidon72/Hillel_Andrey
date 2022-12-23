import tkinter as tk

# Создает объект окна.
window = tk.Tk()


# Создает обработчик событий.
def handle_keypress(event):
    """Выводит символ, связанный с нажатой клавишей"""
    print(event.char)


# Запускает обработчик событий.
window.mainloop()

# window = tk.Tk()
#
#
# def handle_keypress(event):
#     """Выводит символ, связанный с нажатой клавишей"""
#     print(event.char)
#
#
# # Связывает событие нажатия клавиши с handle_keypress()
# window.bind("<Key>", handle_keypress)
#
# window.mainloop()