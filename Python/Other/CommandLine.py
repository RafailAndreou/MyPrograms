import os,shutil

MyNotes = ("")

print("Help(): See all commands")

print("")

print("Example(): Get example for a command")

def Help():
    print("cd(): Change working  directory")
    print("")
    print("rename(): Rename a file or directory")
    print("")
    print("rmdir(): Remove a directory")
    print("")
    print("rmfile(): Remove a file")
    print("")
    print("copy(): Copy a file or a directory")
    print("")
    print("copytree(): Copy a directory tree")
    print("")
    print("list(): To get all the files-folders of you working directory")
    print("")
    print("notepad() Write your notes")
    print("")
    print("notes() To see your notes")
    print("")
    print("open() open a file from your working directory")

try:
    def Example():
        command = input("Put the command that you want an example: ")
        if command == "cd()":
            print("cd-example: cd()\n Put the path you want to change: c:\\Windows\\system32")
        elif command == "rename()":
            print ("rename-example: rename() \n Put your file name and the new name: test.py, 1.py")
        elif command == "rmdir()":
            print("rmdir-example \n Put the directory you want to remove: test")
        elif command == "rmfile()":
            print("rmfile-example \n Put the file you want to remove: test.py")
        elif command == "copy()":
            print("copy-example \n Put the file and then the path you want to copy: test, c:\\Users")
        elif command == "copytree()":
            print("copytree-example: \n Put the directory tree and then the path you want to copy: test, c:\\Windows\\system")
        elif command == ("list()"):
            print("list-example: \n That's easy you don't want example")
        elif command == "notepad()":
            print("notepad-example: \n Type your notes: Hello World")
        elif command == "notes()":
            print("notes-example: \n Hello World")
        else:
            print("open-example: \n test.py")
except Exception as e:
    print(e)

try:       
    def cd():
        cd = input("Put the path you want to change: ")
        os.chdir(cd)
        print(os.getcwd())
except Exception as e:
    print(e)
    
try:    
    def rename():
        rename = input("Put your file name and the new name: ")
        os.rename(rename)
        print(os.getcwd())
except Exception as e:
    print(e)
    
try:
    def rmdir():
        rmdir = input("Put the directory you want to remove: ")
        os.rmdir(rmdir)
        print(os.getcwd())
except Exception as e:
    print (e)
    
try:    
    def rmfile():
        rmfile = input("Put the file you want to remove: ")
        os.remove(rmfile)
        print(os.getcwd())
except Exception as e:
    print(e)
  
try:   
    def copy():
        copy = input("Put the file and then the path you want to copy: ")
        shutil.copy(copy)
        print(os.getcwd())
except Exception as e:
    print(e)
    
try: 
    def copytree():
        copytree = input("Put the directory tree and then the path you want to copy: ")
        shutil.copytree(copytree)
        print(os.getcwd())
except Exception as e:
    print(e)
    
def list():
    print(os.listdir(os.getcwd()))
    print(os.getcwd())
    
try:
    def notepad():
        global MyNotes
        MyNotes = input("""Type your notes: """)
        print(os.getcwd())
except Exception as e:
    print(e)
    
def notes():
    global MyNotes
    print (MyNotes)
    print(os.getcwd())
    
try:
    def open():
        OpenFile = input("Put the file that you want to open: ")
        os.startfile(OpenFile)
        print (os.getcwd())
except Exception as e:
    print(e)





    

    
    
    
    





    
    



    
    



































    
    
    
        



    

    
