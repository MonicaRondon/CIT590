#GUI Practice 1
from tkinter import *
top = Tk()
def main():
    global lab, chk, chkvar, ent, txt
    Button(top, text="Here is a button",\
    command = Button).pack()
    lab = Label(top, text="This is a label", width = 20)
    lab.pack()
    chkvar = IntVar()
    chk = Checkbutton(top, text = "This is a checkbox",\
     variable = chkvar)
    chk.pack()
    ent = Entry(top, width = 25)
    ent.pack()
    txt = Text(top, width = 25, height = 3)
    txt.pack()
    mainloop()
main()