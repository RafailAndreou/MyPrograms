from tkinter import *
import os
class program:
    def __init__(self,master):
        self.label = Label(master , text = "Με ποια λέξη θες να κάνει ομοιοκαταληξεία")
        self.label.pack()
        global entry
        entry = self.entry = Entry()
        entry.pack()
        self.Button = Button(master, text = "Τέλος", command = self.find)
        self.Button.pack()
    def find(self):
        os.chdir("F:\\Scripts")
        Word = entry.get()
        vowels = ["Α","Ε","Ι","Ο","Υ","Ω","Η","ΟΥ","ΕΙ","ΕΥ","ΑΙ","ΑΥ","ΟΙ"] 
        Num = 0
        Num1 = 0
        for i in Word:
            if i in vowels:
                Num += 1
                
        rhyme = Word[-2:]
        File = open("greek.txt", encoding = "utf8")
        Words = File.readlines()
        scrollbar = self.scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT,fill = Y)
        listbox = self.listbox = Listbox(root)
        listbox.pack()
        listbox.insert(END,"Λέξεις που βρέθηκαν")
        
        for List_Word in Words:
            Word_Rhyme = List_Word[-3:-1]
            if Word_Rhyme == rhyme:
                for I in List_Word:
                    if I in vowels:
                        Num1 += 1
                if Num1 == Num:
                    listbox.insert(END, List_Word)
                Num1 = 0
        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command=listbox.yview)
                
        File.close()
            


root = Tk()
x = program(root)
root.mainloop()
