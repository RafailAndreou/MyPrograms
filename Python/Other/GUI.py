from tkinter import *

class Program:

    def __init__(self,master):
        self.Button = Button(master, text = "Button", command = self.Main)
        self.Button.pack()
    
    def main(self):
        password = ("rafailg9")
        Input = input("Password: ")
        while 1:
            
            if  Input == password:
                print("\n \n")
                command = input("Γράψε Lista εάν θες να δείς την λιστά, \n del εάν θες να διαγράψεις την λίστα \n και Input εάν θες να προσθέσεις κάτι στην λίστα: ")
                if command == "Input":
                    lista = input("Τι θες να προσθέσεις στην λίστα: ")
                    print("Προστέθηκε επιτυχώς")
                elif command == ("Lista"):
                    print(lista)
                elif command == ("del"):
                    for i in lista:
                        del i
                else:
                    print("There is no command", command)
                    
            else:
                print("Wrong Password")


root = Tk()
x = Program(root)
root.mainloop
