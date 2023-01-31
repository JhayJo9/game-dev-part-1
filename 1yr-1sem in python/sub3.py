from tkinter import *
from tkinter import ttk
from sub3function import login_popup
from sub3function import wrongpass
gui = Tk()

gui.title("Sublime")
gui.geometry('300x300')

label = ttk.Label(gui,text="Hello", font=("arial", "18", "bold"),wraplength=100)

def inputfromuser():
	INPUT2 = inputtext2.get("1.0","end-1c")
	print(INPUT2)

	if INPUT2 == "141":
		login_popup()
	elif INPUT2 == "virus":
		for x in range(5):
			wrongpass()
	else:
		wrongpass()

label2 = ttk.Label(gui, text="Sublime log in!!!", font=('Arial','20','bold'))
label3 = ttk.Label(gui,text="Username",font=("Arial", "20",))
inputtext2 = Text(gui, height=2, width=20, bg="wheat")
label4 = ttk.Label(gui, text="Password", font=("arial", "20"))
inputtext1 = Text(gui,height=2,width=20,bg="wheat")

# Output = Text(gui, height=2, width = 20, bg = "wheat")


display = Button(gui, height=2, width=5, text="Log in", command=lambda: inputfromuser())
# display1 = Button(gui, height=2, width=5, text="Log in", command=lambda: login_popup())
# display2 = Button(gui, height=2, width=5, text="Log in", command=lambda: wrongpass())


label.pack()
label2.pack()
label3.pack()
inputtext1.pack()
label4.pack()
inputtext2.pack()
display.pack()
# display1.pack()
# display2.pack()
# Output.pack()
gui.mainloop()
