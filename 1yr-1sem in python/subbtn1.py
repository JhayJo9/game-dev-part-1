from tkinter import *
from tkinter import ttk
from subbtn1function import button1
gui = Tk()
gui.title("buttonss")
gui.geometry('300x300')


# btn1 = Button(gui, height=2, width=5, text="1")


btn2 = Button(gui, height=2, width=5, text="2", command=lambda: button1())

# btn1.pack()
btn2.pack()

gui.mainloop()