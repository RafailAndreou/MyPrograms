from tkinter import *
from tkinter import filedialog

class Program:
    def __init__(self,master):
        master.title("Menu")
        master.geometry('900x300+300+200')

        self.Menubar = Menu(master)
        self.filemenu = Menu(self.Menubar,tearoff = 0)
        self.Menubar.add_cascade(label = "File",menu=self.filemenu)
        self.filemenu.add_command(label = "Open...",command = self.File)
        master.config(menu=self.Menubar)

    def File(self):
        global filename
        filename = filedialog.askopenfilename(title = 'Select Words File')

root = Tk()
x = Program(root)
