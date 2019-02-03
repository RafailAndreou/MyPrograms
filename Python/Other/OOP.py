class Program(object):
    password = ("rafailg9")
    Input = input("Password: ")
    def __init__(self):
        if self.Input == self.password:
            while True:
                print("\n \n")
                command = input("Γράψε Lista εάν θες να δείς την λιστά, \n del εάν θες να διαγράψεις την λίστα \n και Input εάν θες να προσθέσεις κάτι στην λίστα: ")
                if command == ("Input"):
                    Lista = input("Τι θες να προσθέσεις στην λίστα: ")
                    print("Προστέθηκε επιτυχώς")
                elif command == ("Lista"):
                    print(Lista)
                elif command == ("del"):
                    for i in Lista:
                        del i
                else:
                    print("There is no command",command)
                    
            else:
                print("Wrong Password")

    
x = Program()






    

        
        
            
