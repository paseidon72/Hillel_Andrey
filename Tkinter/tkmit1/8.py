from tkinter import *
from tkinter import ttk

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x150")
#
# # вертикальный Progressbar
# ttk.Progressbar(orient="vertical", length=100, value=40).pack(pady=5)
#
# # горизонтальный Progressbar
# ttk.Progressbar(orient="horizontal", length=150, value=20).pack(pady=5)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x150")
#
# value_var = IntVar(value=30)
#
# progressbar = ttk.Progressbar(orient="horizontal", variable=value_var)
# progressbar.pack(fill=X, padx=6, pady=6)
#
# label = ttk.Label(textvariable=value_var)
# label.pack(anchor=NW, padx=6, pady=6)
#
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x150")
#
# value_var = IntVar()
#
# progressbar = ttk.Progressbar(orient="horizontal", variable=value_var)
# progressbar.pack(fill=X, padx=6, pady=6)
#
# label = ttk.Label(textvariable=value_var)
# label.pack(anchor=NW, padx=6, pady=6)
#
#
# def start(): progressbar.start(1000)  # запускаем progressbar
#
#
# def stop(): progressbar.stop()  # останавливаем progressbar
#
#
# start_btn = ttk.Button(text="Start", command=start)
# start_btn.pack(anchor=SW, side=LEFT, padx=6, pady=6)
# stop_btn = ttk.Button(text="Stop", command=stop)
# stop_btn.pack(anchor=SE, side=RIGHT, padx=6, pady=6)
#
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x150")

progressbar = ttk.Progressbar(orient="horizontal", mode="indeterminate")
progressbar.pack(fill=X, padx=10, pady=10)

start_btn = ttk.Button(text="Start", command=progressbar.start)
start_btn.pack(anchor=SW, side=LEFT, padx=10, pady=10)

stop_btn = ttk.Button(text="Stop", command=progressbar.stop)
stop_btn.pack(anchor=SE, side=RIGHT, padx=10, pady=10)

root.mainloop()