Password=("Lista")

x = input("Password: ")

if x == Password:
    Input = input("Γράψε τι θές να προσθέσεις: ")
    Lista = input("Γράψε Lista εάν θες να δείς την λιστά, \n del εάν θες να διαγράψεις την λίστα: ")
    if Lista == ("Lista"):
        print(Input)
    elif Lista == ("del"):
        for i in Input:
            del i
else:
    print("Wrong password")


    
