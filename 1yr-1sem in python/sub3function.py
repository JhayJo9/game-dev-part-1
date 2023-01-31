from tkinter import *
from tkinter import ttk

def login_popup():
    gui = Tk()
    gui.title("Notif")
    gui.geometry('300x80')
    label = ttk.Label(gui, text="You log in!!!!", font=('Arial', '20'))

    label.pack()
    gui.mainloop()


# login_popup()

def wrongpass():
    gui = Tk()
    gui.title("Notif")
    gui.geometry('300x50')
    label = ttk.Label(gui, text="Wrong password!!!", font=('Arial', '20'))

    label.pack()
    gui.mainloop()


# wrongpass