from tkinter import *

class Program:
    def __init__(self, master):
        master.geometry("400x400+500+300")
        self.label = Label(master, text="Password: ")
        self.label.pack()
        global entry
        entry = self.e= Entry(master)
        entry.pack()
        s = entry.get()
        self.Button = Button(master, text="Entry", command=self.List)
        self.Button.pack()
    def List(self):
        s = entry.get()
        if s == "Password":
            self.Label = Label(root,text="Γράψε list εάν θες να δείς την λιστά, \n del εάν θες να διαγράψεις την λίστα "
                                         "\n και add εάν θες να προσθέσεις κάτι στην λίστα: ")
            self.Label.pack()
            global entry1
            entry1 = self.Entry = Entry(root)
            entry1.pack()
            self.Button1 = Button(root, text="Entry", command = self.Commands)
            self.Button1.pack()
        else:
            self.Label = Label(root, text=s+" is not the password")
            self.Label.pack()
    def Commands(self):
        s1 = entry1.get()
        if s1 == "add":
            self.Label1 = Label(root, text="Type what do you want to add in your list")
            self.Label1.pack()
            global Add_Entry
            Add_Entry = self.Add_Entry = Entry(root)
            Add_Entry.pack()
            self.Button2 = Button(root, text="Entry", command = self.add)
            self.Button2.pack()
        elif s1 == "list":
            File = open("New_File.txt","r")
            Read = File.read()
            self.List = Label(root, text = Read)
            self.List.pack()
            File.close()
        elif s1 == "del":
            File = open("New_File.txt" , "w")
            
    def add(self):
        global S_Add
        S_Add = Add_Entry.get()
        File = open("New_File.txt", "a")
        File.write(S_Add)
        File.close()
        
        
root = Tk()
x = Program(root)
root.mainloop

