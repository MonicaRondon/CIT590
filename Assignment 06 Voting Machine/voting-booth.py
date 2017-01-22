"""this is a program which records, tracks and totals votes for the most
important policy issue in the 2016 Presidential Election. The "Voting Booth"
votes are recorded, tracked and the winning total identified for five policy 
issues: 1) Economy 2) National Security 3) Climate Change 4) Criminal Justice
 Reform and 5) Deficit. """

from tkinter import *

top = Tk()

class VotingButton:
    """Blueprint for the creation of VotingButton objects including the
vote function"""
    def __init__(self, Booth, Buttontext, frame, row):
        """Intialiser that creates VotingButtons objects with the parameters 
        Booth,Buttontext, frame and row"""
        Button(frame, text = Buttontext, width = 40, command = self.Vote).grid(\
         row = row, column = 0)
        self.numberofvoteslabel = Label(frame, text = "0", width = 20)
        self.numberofvoteslabel.grid( row = row, column = 1)
        self.numberofvotes = 0 
        self.Buttontext = Buttontext
        self.Booth = Booth

    def Vote(self):
        """Increases the number of votes associated with each individual 
        VotingButton, compares  the votes associated with each 
        individual VotingButton with all other buttons in the list to see if 
        the individual VotingButton has the max votes and if there is a tie"""
        self.numberofvotes += 1
        self.numberofvoteslabel.config(text = self.numberofvotes)
        for btn in self.Booth.Buttons:
            if self.numberofvotes < self.Booth.maximum_votes:
                return
            if self.numberofvotes == btn.numberofvotes and self.Buttontext\
             != btn.Buttontext:
                self.Booth.currentwinnerlabel.config(text = "Tied")
                return
        self.Booth.maximum_votes = self.numberofvotes
        self.Booth.currentwinnerlabel.config(text = self.Buttontext)

class VotingBooth:
    """Creates the blueprint for the VotingBooth object which dependent upon 
    the VotingButton classe"""
    def __init__(self):
        """Intialiser - this creates a complete VotingBooth"""
        top["bg"] = "light gray"
        frame1 = Frame(top, bg = "light gray")
        frame1.grid(row = 0, column = 0)
        Label(frame1, text = "Vote for the most important policy issue of the\
 2016 election!", bg = "light gray", padx = 10, pady = 10).grid()
        frame2 = Frame(top, bg = "gray")
        frame2.grid( row = 1, column = 0)
        Label(frame2, text = "Policy Issue", height = 2, width = 40).grid(row\
         = 0, column = 0)
        Label(frame2, text = "Votes", height = 2, width = 20).grid(row = 0,\
         column = 1)
        self.Buttons = []
        """below the self paramater maps onto the Booth parameter in the 
        VotingButton class, passing the self reference to the VotingBooth
        class as the Booth field instance"""
        self.Buttons.append(VotingButton(self, "Economy", frame2, 1))
        self.Buttons.append(VotingButton(self, "National Security", frame2, 2))
        self.Buttons.append(VotingButton(self, "Climate Change", frame2, 3))
        self.Buttons.append(VotingButton(self, "Criminal Justice Reform", \
        frame2, 4))
        self.Buttons.append(VotingButton(self, "Deficit", frame2, 5))
        self.maximum_votes = 0
        Label(frame2, text = "Winner so far...", width = 40).grid(row = 6,\
         column = 0)
        self.currentwinnerlabel = Label(frame2, text = "Tied", width = 20)
        self.currentwinnerlabel.grid( row = 6, column = 1)
        mainloop()

VotingBooth()
