from tkinter import *
from tkinter import ttk

gui = Tk()
gui.title("GUI")
gui.geometry('300x300')
label = ttk.Label(gui, text="GUI", font=("arial", "20", "bold"),wraplength=100)

def function2():
	print("hello")


display = Button(gui, height = 2, width= 5, text="Log in", command = lambda: function2())
display.pack()
label.pack()
gui.mainloop()