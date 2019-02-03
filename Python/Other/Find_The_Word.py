import fnmatch
import os

print("""Κανόνες:

Εάν δεν ξέρετε κάποιο γραμμα βάρτε ένα ερωτηματικό(?),
για να είναι ευκολότερο να βρούμε τις πιθανές απαντήσεις""")

print("")

print("Πρέπει τα γράμματα που θα δίνεται να είναι κεφάλαια")

print("")
        
Desktop_Path = ("D:\Scripts\Python\Other")

os.chdir(Desktop_Path)

Number = input("Πόσα είναι τα γράμματα της λέξης: ")

if Number == "4":
    First_Letter = input("Ποιο είναι το πρώτο γραμμα: ")
    Second_Letter = input("Ποιο είναι το δεύτερο γράμμα: ")
    Third_Letter = input("Ποιο είναι το τρίτο γράμμα: ")
    Fourth_Letter = input("Ποιο είναι το τέταρτο γράμμα: ")

    Number_4 = First_Letter + Second_Letter + Third_Letter + Fourth_Letter

    Words = open("Words.txt","r")

    Read_Words = Words.read()

    Answers = open("Answers.txt","w")

    Words.close()

    for Word in fnmatch.filter(Read_Words,Number_4):
        print(Word)
        Answers.write(Word)
        

elif Number == "5":
    First_Letter = input("Ποιο είναι το πρώτο γραμμα: ")
    Second_Letter = input("Ποιο είναι το δεύτερο γράμμα: ")
    Third_Letter = input("Ποιο είναι το τρίτο γράμμα: ")
    Fourth_Letter = input("Ποιο είναι το τέταρτο γράμμα: ")
    Fifth_Letter = input("Ποιο είναι το πέμπτο γράμμα: ")

    Number_5 = First_Letter + Second_Letter + Third_Letter + Fourth_Letter + Fifth_Letter

    Words = open("Words.txt","r")

    Read_Words = Words.read()

    Answers = open("Answers.txt","w")

    Words.close()

    for Word in fnmatch.filter(Read_Words,Number_5):
        print(Word)
        Answers.write(Word)
        
elif Number == "6":
    First_Letter = input("Ποιο είναι το πρώτο γραμμα: ")
    Second_Letter = input("Ποιο είναι το δεύτερο γράμμα: ")
    Third_Letter = input("Ποιο είναι το τρίτο γράμμα: ")
    Fourth_Letter = input("Ποιο είναι το τέταρτο γράμμα: ")
    Fifth_Letter = input("Ποιο είναι το πέμπτο γράμμα: ")
    Sixth_Letter = input("Ποιο είναι το έκτο γράμμα: ")

    Number_6 = First_Letter + Second_Letter + Third_Letter + Fourth_Letter + Fifth_Letter + Sixth_Letter

    Words = open("Words.txt","r")

    Read_Words = Words.read()

    Answers = open("Answers.txt","w")

    Words.close()

    for Word in fnmatch.filter(Read_Words,Number_6):
        print(Word)
        Answers.write(Word)

elif Number == "7":
    First_Letter = input("Ποιο είναι το πρώτο γράμμα: ")
    Second_Letter = input("Ποιο είναι το δεύτερο γράμμα: ")
    Third_Letter = input("Ποιο είναι το τρίτο γράμμα: ")
    Fourth_Letter = input("Ποιο είναι το τέταρτο γράμμα: ")
    Fifth_Letter = input("Ποιο είναι το πέμπτο γράμμα: ")
    Sixth_Letter = input("Ποιο είναι το έκτο γράμμα: ")
    Seventh_Letter = input("Ποιο είναι το έβδομο γράμμα: ")

    Number_7 = First_Letter + Second_Letter + Third_Letter + Fourth_Letter+ Fifth_Letter + Sixth_Letter + Seventh_Letter

    Words = open("greek.txt","r")

    Read_Words = Words.read()

    Answers = open("Answers.txt","w")

    Words.close()

    for Word in fnmatch.filter(Read_Words,Number_7):
        print(Word)
        Answers.write(Word)

elif Number == "8":
    First_Letter = input("Ποιο είναι το πρώτο γράμμα: ")
    Second_Letter = input("Ποιο είναι το δεύτερο γράμμα: ")
    Third_Letter = input("Ποιο είναι το τρίτο γράμμα: ")
    Fourth_Letter = input("Ποιο είναι το τέταρτο γράμμα: ")
    Fifth_Letter = input("Ποιο είναι το πέμπτο γράμμα: ")
    Sixth_Letter = input("Ποιο είναι το έκτο γράμμα: ")
    Seventh_Letter = input("Ποιο είναι το έβδομο γράμμα: ")
    Eighth_Letter = input("Ποιο είναι το όγδοο γράμμα: ")

    Number_8 = First_Letter + Second_Letter + Third_Letter + Fourth_Letter+ Fifth_Letter + Sixth_Letter + Seventh_Letter + Eighth_Letter

    Words = open("Words.txt","r")

    Read_Words = Words.read()

    Answers = open("Answers.txt","w")

    Words.close()

    for Word in fnmatch.filter(Read_Words,Number_8):
        print(Word)
        Answers.write(Word)

elif Number == "9":
    First_Letter = input("Ποιο είναι το πρώτο γράμμα: ")
    Second_Letter = input("Ποιο είναι το δεύτερο γράμμα: ")
    Third_Letter = input("Ποιο είναι το τρίτο γράμμα: ")
    Fourth_Letter = input("Ποιο είναι το τέταρτο γράμμα: ")
    Fifth_Letter = input("Ποιο είναι το πέμπτο γράμμα: ")
    Sixth_Letter = input("Ποιο είναι το έκτο γράμμα: ")
    Seventh_Letter = input("Ποιο είναι το έβδομο γράμμα: ")
    Eighth_Letter = input("Ποιο είναι το όγδοο γράμμα: ")
    Ninth_Letter = input("Ποιο είναι το ένατο γράμμα: ")

    Number_9 = First_Letter + Second_Letter + Third_Letter + Fourth_Letter+ Fifth_Letter + Sixth_Letter + Seventh_Letter + Eighth_Letter + Ninth_Letter

    Words = open("Words.txt","r")

    Read_Words = Words.read()

    Answers = open("Answers.txt","w")

    Words.close()

    for Word in fnmatch.filter(Read_Words,Number_9):
        print(Word)
        Answers.write(Word)

elif Number == "10":
    First_Letter = input("Ποιο είναι το πρώτο γράμμα: ")
    Second_Letter = input("Ποιο είναι το δεύτερο γράμμα: ")
    Third_Letter = input("Ποιο είναι το τρίτο γράμμα: ")
    Fourth_Letter = input("Ποιο είναι το τέταρτο γράμμα: ")
    Fifth_Letter = input("Ποιο είναι το πέμπτο γράμμα: ")
    Sixth_Letter = input("Ποιο είναι το έκτο γράμμα: ")
    Seventh_Letter = input("Ποιο είναι το έβδομο γράμμα: ")
    Eighth_Letter = input("Ποιο είναι το όγδοο γράμμα: ")
    Ninth_Letter = input("Ποιο είναι το ένατο γράμμα: ")
    Tenth_Letter = input("Ποιο είναι το δέκατο γράμμα: ")

    Number_10 = First_Letter + Second_Letter + Third_Letter + Fourth_Letter+ Fifth_Letter + Sixth_Letter + Seventh_Letter + Eighth_Letter + Ninth_Letter + Tenth_Letter

    Words = open("Words.txt","r")

    Read_Words = Words.read()

    Answers = open("Answers.txt","w")

    Words.close()

    for Word in fnmatch.filter(Read_Words,Number_10):
        print(Word)
        Answers.write(Word)

elif Number == "11":
    First_Letter = input("Ποιο είναι το πρώτο γράμμα: ")
    Second_Letter = input("Ποιο είναι το δεύτερο γράμμα: ")
    Third_Letter = input("Ποιο είναι το τρίτο γράμμα: ")
    Fourth_Letter = input("Ποιο είναι το τέταρτο γράμμα: ")
    Fifth_Letter = input("Ποιο είναι το πέμπτο γράμμα: ")
    Sixth_Letter = input("Ποιο είναι το έκτο γράμμα: ")
    Seventh_Letter = input("Ποιο είναι το έβδομο γράμμα: ")
    Eighth_Letter = input("Ποιο είναι το όγδοο γράμμα: ")
    Ninth_Letter = input("Ποιο είναι το ένατο γράμμα: ")
    Tenth_Letter = input("Ποιο είναι το δέκατο γράμμα: ")
    Eleventh_Letter = input("Ποιο είναι το δεκάτο γράμμα: ")

    Number_11 = First_Letter + Second_Letter + Third_Letter + Fourth_Letter+ Fifth_Letter + Sixth_Letter + Seventh_Letter + Eighth_Letter + Ninth_Letter + Tenth_Letter + Eleventh_Letter

    Words = open("Words.txt","r")

    Read_Words = Words.read()

    Answers = open("Answers.txt","w")

    Words.close()

    for Word in fnmatch.filter(Read_Words,Number_11):
        print(Word)
        Answers.write(Word)

elif Number == "12":
    First_Letter = input("Ποιο είναι το πρώτο γράμμα: ")
    Second_Letter = input("Ποιο είναι το δεύτερο γράμμα: ")
    Third_Letter = input("Ποιο είναι το τρίτο γράμμα: ")
    Fourth_Letter = input("Ποιο είναι το τέταρτο γράμμα: ")
    Fifth_Letter = input("Ποιο είναι το πέμπτο γράμμα: ")
    Sixth_Letter = input("Ποιο είναι το έκτο γράμμα: ")
    Seventh_Letter = input("Ποιο είναι το έβδομο γράμμα: ")
    Eighth_Letter = input("Ποιο είναι το όγδοο γράμμα: ")
    Ninth_Letter = input("Ποιο είναι το ένατο γράμμα: ")
    Tenth_Letter = input("Ποιο είναι το δέκατο γράμμα: ")
    Eleventh_Letter = input("Ποιο είναι το δεκάτο γράμμα: ")
    Twelfth_Letter = input("Ποιο είναι το δωδέκατο γράμμα: ")

    Number_12 = First_Letter + Second_Letter + Third_Letter + Fourth_Letter+ Fifth_Letter + Sixth_Letter + Seventh_Letter + Eighth_Letter + Ninth_Letter + Tenth_Letter + Eleventh_Letter + Twelfth_Letter

    Words = open("Words.txt","r")

    Read_Words = Words.read()

    Answers = open("Answers.txt","w")

    Words.close()

    for Word in fnmatch.filter(Read_Words,Number_12):
        print(Word)
        Answers.write(Word)

elif Number == "13":
    First_Letter = input("Ποιο είναι το πρώτο γράμμα: ")
    Second_Letter = input("Ποιο είναι το δεύτερο γράμμα: ")
    Third_Letter = input("Ποιο είναι το τρίτο γράμμα: ")
    Fourth_Letter = input("Ποιο είναι το τέταρτο γράμμα: ")
    Fifth_Letter = input("Ποιο είναι το πέμπτο γράμμα: ")
    Sixth_Letter = input("Ποιο είναι το έκτο γράμμα: ")
    Seventh_Letter = input("Ποιο είναι το έβδομο γράμμα: ")
    Eighth_Letter = input("Ποιο είναι το όγδοο γράμμα: ")
    Ninth_Letter = input("Ποιο είναι το ένατο γράμμα: ")
    Tenth_Letter = input("Ποιο είναι το δέκατο γράμμα: ")
    Eleventh_Letter = input("Ποιο είναι το δεκάτο γράμμα: ")
    Twelfth_Letter = input("Ποιο είναι το δωδέκατο γράμμα: ")
    Thirthteenth_Letter = input("Ποιο είναι το δεκατο τρίτο: ")

    Number_13 = First_Letter + Second_Letter + Third_Letter + Fourth_Letter+ Fifth_Letter + Sixth_Letter + Seventh_Letter + Eighth_Letter + Ninth_Letter + Tenth_Letter + Eleventh_Letter + Twelfth_Letter + Thirthteenth_Letter

    Words = open("Words.txt","r")

    Read_Words = Words.read()

    Answers = open("Answers.txt","w")

    Words.close()

    for Word in fnmatch.filter(Read_Words,Number_13):
        print(Word)
        Answers.write(Word)

elif Number == "14":
    First_Letter = input("Ποιο είναι το πρώτο γράμμα: ")
    Second_Letter = input("Ποιο είναι το δεύτερο γράμμα: ")
    Third_Letter = input("Ποιο είναι το τρίτο γράμμα: ")
    Fourth_Letter = input("Ποιο είναι το τέταρτο γράμμα: ")
    Fifth_Letter = input("Ποιο είναι το πέμπτο γράμμα: ")
    Sixth_Letter = input("Ποιο είναι το έκτο γράμμα: ")
    Seventh_Letter = input("Ποιο είναι το έβδομο γράμμα: ")
    Eighth_Letter = input("Ποιο είναι το όγδοο γράμμα: ")
    Ninth_Letter = input("Ποιο είναι το ένατο γράμμα: ")
    Tenth_Letter = input("Ποιο είναι το δέκατο γράμμα: ")
    Eleventh_Letter = input("Ποιο είναι το δεκάτο γράμμα: ")
    Twelfth_Letter = input("Ποιο είναι το δωδέκατο γράμμα: " )  
    Thirthteenth_Letter = input("Ποιο είναι το δεκατο τρίτο: ")
    Fourteenth_Letter = input("Ποιο ειναι το δεκατο τετάρτο: ")

    Number_14 = First_Letter + Second_Letter + Third_Letter + Fourth_Letter+ Fifth_Letter + Sixth_Letter + Seventh_Letter + Eighth_Letter + Ninth_Letter + Tenth_Letter + Eleventh_Letter + Twelfth_Letter + Thirthteenth_Letter + Fourteenth_Letter

    Words = open("greek.txt","r")

    Read_Words = Words.read()

    Answers = open("Answers.txt","w")

    Words.close()

    for Word in fnmatch.filter(Read_Words,Number_14):
        print(Word)
        Answers.write(Word)

elif Number == "15":
    First_Letter = input("Ποιο είναι το πρώτο γράμμα: ")
    Second_Letter = input("Ποιο είναι το δεύτερο γράμμα: ")
    Third_Letter = input("Ποιο είναι το τρίτο γράμμα: ")
    Fourth_Letter = input("Ποιο είναι το τέταρτο γράμμα: ")
    Fifth_Letter = input("Ποιο είναι το πέμπτο γράμμα: ")
    Sixth_Letter = input("Ποιο είναι το έκτο γράμμα: ")
    Seventh_Letter = input("Ποιο είναι το έβδομο γράμμα: ")
    Eighth_Letter = input("Ποιο είναι το όγδοο γράμμα: ")
    Ninth_Letter = input("Ποιο είναι το ένατο γράμμα: ")
    Tenth_Letter = input("Ποιο είναι το δέκατο γράμμα: ")
    Eleventh_Letter = input("Ποιο είναι το δεκάτο γράμμα: ")
    Twelfth_Letter = input("Ποιο είναι το δωδέκατο γράμμα: ")
    Thirthteenth_Letter = input("Ποιο είναι το δεκατο τρίτο: ")
    Fourteenth_Letter = input("Ποιο ειναι το δεκατο τετάρτο: ")
    Fifteenth_Letter = input("Ποιο είναι το δεκατο πέμπτο: ")

    Number_15 = First_Letter + Second_Letter + Third_Letter + Fourth_Letter+ Fifth_Letter + Sixth_Letter + Seventh_Letter + Eighth_Letter + Ninth_Letter + Tenth_Letter + Eleventh_Letter + Twelfth_Letter + Thirthteenth_Letter + Fourteenth_Letter + Fifteenth_Letter

    Words = open("Words.txt","r")

    Read_Words = Words.read()

    Answers = open("Answers.txt","w")

    Words.close()

    for Word in fnmatch.filter(Read_Words,Number_15):
        print(Word)
        Answers.write(Word)
    
    
    
    
    
    
    
    
    
    


        

