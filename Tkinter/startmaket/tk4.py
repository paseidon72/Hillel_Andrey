import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=40, height=25, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=60, height=25, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=80, height=25, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame4 = tk.Frame(master=window, width=100, height=25, bg="green")
frame4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()

window = tk.Tk()

# frame1 = tk.Frame(master=window, height=100, bg="red")
# frame1.pack(fill=tk.X)
#
# frame2 = tk.Frame(master=window, height=50, bg="yellow")
# frame2.pack(fill=tk.X)
#
# frame3 = tk.Frame(master=window, height=25, bg="blue")
# frame3.pack(fill=tk.X)
#
# window.mainloop()

# window = tk.Tk()
#
# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack()
#
# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack()
#
# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack()
#
# window.mainloop()

# window = tk.Tk()
#
# frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
# frame1.pack(fill=tk.Y, side=tk.LEFT)
#
# frame2 = tk.Frame(master=window, width=100, bg="yellow")
# frame2.pack(fill=tk.Y, side=tk.LEFT)
#
# frame3 = tk.Frame(master=window, width=50, bg="blue")
# frame3.pack(fill=tk.Y, side=tk.LEFT)
#
# window.mainloop()