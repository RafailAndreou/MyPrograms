import time
from tkinter import *

class Program:
    def __init__(self,master):
        master.geometry("600x500+500+200")
        master.title("Βαλε προγραμμά στην ζωή σου επιτέλους")
        Monday = self.label = Label(master,text ="Δευτέρα")
        Monday.grid(row = 1,column = 1)
        Tuesday = self.label1 = Label(master,text = "Τρίτη")
        Tuesday.grid(row = 1,column = 2)
        Wednesday = self.label2 = Label(master,text = "Τετάρτη")
        Wednesday.grid(row = 1,column = 3)
        Thursday = self.label3 = Label(master,text = "Πέμπτη")
        Thursday.grid(row = 1, column = 4)
        Friday = self.label4 = Label(master,text = "Παρασκευή")
        Friday.grid(row = 1, column = 5)
        Saturday = self.label5= Label(master,text = "Σάββατο")
        Saturday.grid(row = 1,column = 6)
        Sunday = self.label6 = Label(master,text = "Κυριακή")
        Sunday.grid(row = 1,column = 7)
        Monday_Button = self.button = Button(master,text = "      ")
        Monday_Button.grid(row = 3,column = 1)
        Tuesday_Button = self.button1= Button(master, text = "      ")
        Tuesday_Button.grid(row = 3, column = 2)
        Wednesday_Button= self.button2 = Button(master,text = "      ")
        Wednesday_Button.grid(row = 3,column = 3)
        Thursday_Button = self.button3 = Button(master,text = "      ")
        Thursday_Button.grid(row=3,column=4)
        Friday_Button = self.button4 = Button(master,text = "      ")
        Friday_Button.grid(row=3,column=5)
        Saturday_Button = self.button5= Button(master,text = "      ")
        Saturday_Button.grid(row=3,column=6)
        Sunday_Button = self.button6 = Button(master,text = "      ")
        Sunday_Button.grid(row=3,column = 7)
        

        






root = Tk()

x = Program(root)

root.mainloop()

