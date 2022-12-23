from tkinter import *
from tkinter import messagebox

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x150")
#
# root.option_add("*tearOff", FALSE)
#
# main_menu = Menu()
#
# file_menu = Menu()
# file_menu.add_command(label="New")
# file_menu.add_command(label="Save")
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit")
#
# main_menu.add_cascade(label="File", menu=file_menu)
# main_menu.add_cascade(label="Edit")
# main_menu.add_cascade(label="View")
#
# root.config(menu=main_menu)
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x150")
#
# root.option_add("*tearOff", FALSE)
#
# main_menu = Menu()
# file_menu = Menu()
# settings_menu = Menu()
#
# settings_menu.add_command(label="Save")
# settings_menu.add_command(label="Open")
#
# file_menu.add_cascade(label="Settings", menu=settings_menu)
# file_menu.add_separator()
# file_menu.add_command(label="Exit")
#
# main_menu.add_cascade(label="File", menu=file_menu)
#
# root.config(menu=main_menu)
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x150")

root.option_add("*tearOff", FALSE)


def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")


main_menu = Menu()

main_menu.add_cascade(label="File", command=edit_click)
main_menu.add_cascade(label="Edit", command=edit_click)
main_menu.add_cascade(label="View", command=edit_click)

root.config(menu=main_menu)
root.mainloop()