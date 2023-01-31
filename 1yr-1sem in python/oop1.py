from tkinter import *
from tkinter import ttk

gui = Tk()

gui.title("Hello")
h = 500
w = 500
ws = gui.winfo_screenwidth()
hs = gui.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

label = ttk.label(gui, text="CHARACTER", font=('Arial', 20, 'bold'))


gui.geometry('%dx%d+%d+%d' % (w,h,x,y))
gui.mainloop()


class charaterOne:
    def __init__(self, name, lvl, power):
        self.name = name
        self.lvl = lvl
        self.power = power
    def playername(self):
        print(self.name)

    def playerlvl(self):
        print(self.lvl)

    def playerpwr(self):
        print(self.power)
charone = charaterOne("Jhay","13","Magic")
charone.playername()
charone.playerlvl()
charone.playerpwr()

