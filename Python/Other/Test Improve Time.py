import time
from tkinter import *

class Program:
    def __init__(self,master):
        master.geometry("600x500+500+200")
        master.title("Βαλέ προγραμμά επιτέλους")
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
        global value
        for i in range(7):
            Buttons = self.button = Button(master,text = "     ", command = self.code)
            Buttons.grid(row=3,column = i+1)
        for I in range(7):
            E = self.entry = Entry(master)
            E.grid(row = 2,column = I+1)
            value = E.get()
    def code(self):
        global value
        print(value)
            
                
root = Tk()
Program(root)
