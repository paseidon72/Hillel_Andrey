import tkinter as tk

# window = tk.Tk()
#
# label = tk.Label(
#     text="Привет, Tkinter!",
#     fg="white",
#     bg="black",
#     width=20,
#     height=20
# )
#
# label.pack()
# window.mainloop()


window = tk.Tk()

entry = tk.Entry(width=40)
entry.pack()

entry.insert(0, "What is your name?")

window.mainloop()