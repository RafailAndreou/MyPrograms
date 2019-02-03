from tkinter import *

root = Tk()
def callback(event):
    frame.focus_set()
    pass
    

def key(event):
    print('pressed' ,repr(event.char))

frame = Frame(root,width = 200,height = 200)

frame.bind('<Key>',key)
frame.bind("<Button-1>",callback)
frame.pack()






root.mainloop()
