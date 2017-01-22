#GUI Practice 1
from tkinter import *
top = Tk()

top["bg"] = "white"
frame1 = Frame(top, bg = "light gray")
frame1.pack(side = RIGHT)
Button(frame1, text = "First Button",fg = "green").grid(row = 1, column = 1)
Button(frame1, text = "Second Button", fg = "blue").grid(row = 2, column = 2)
Button(frame1, text = "Third Button", fg = "cyan").grid(row = 3, column = 3)

frame2 = Frame(top, bg = "white")
frame2.pack(side = LEFT)
Button(frame2, text = "Fourth Button").pack(side = TOP)
Button(frame2, text = "Fith Button").pack(side="top")
Button(frame2, text = "Last Button").pack(side=TOP, fill=BOTH)
mainloop()

### within a class
def __init__(self, name):
    self.name = name

