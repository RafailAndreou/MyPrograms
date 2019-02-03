import pygame
from pygame import mixer
import time
from tkinter import *
from tkinter import filedialog
from pynput.keyboard import Key,Controller,Listener
from multiprocessing import Process
import threading



keys = {}
Sounds = {}

class Program:
    def __init__(self,master):
        pygame.init()
        master.title('Music player')
        master.geometry('900x300+300+200')
        master.configure(background = 'black')

        self.Play_Button = Button(master,text = 'Play music', command = self.play)
        self.Stop_Music = Button(master,text = 'Stop music' , command = self.stop)
        self.Queue = Button(master,text = 'Queue music',command = self.queue)
        self.Open_Beats = Button(master,text = 'Studio Beats',command = self.studio)

        self.Play_Button.grid(row = 1)
        self.Stop_Music.grid(row = 1, column = 1)
        self.Queue.grid(row = 1,column = 2)
        self.Open_Beats.grid(row = 1,column = 3)

        self.Menubar = Menu(master)
        self.filemenu = Menu(self.Menubar,tearoff=0)
        self.filemenu.add_command(label = 'Open...',command = self.File)
        self.Menubar.add_cascade(label = 'File',menu = self.filemenu)
        master.config(menu=self.Menubar)

    def play(self):
        try:
            pygame.init()
            mixer.music.load(filename)
            mixer.music.play()
        except (NameError, pygame.error) as error:
            pass

    def stop(self):
        mixer.music.stop()

    def File(self):
        global filename
        filename = filedialog.askopenfilename(title = 'Select File')

    def queue(self):
        try:
            queuefile = filedialog.askopenfilename(title = 'Select Queue file')
            mixer.music.queue(queuefile)
        except pygame.error:
            pass

    def studio(self):
        studio = Tk()
        studio.title('Studio Beats')
        studio.geometry('600x300+300+200')
        self.beat = []
        for i in range(25):
            self.beat.append(Button(studio,text = '' +str(i),command = lambda i=i:self.set(i)))
            self.beat[i].grid(row = 1 ,column=i)
            i+=1

        studio.update()

        def on_key(key):
            print(key)

        with Listener(on_press = on_key) as listener:
            listener.join()
        


    def set(self,i):
        Sound = filedialog.askopenfilename(title = '{} button'.format(str(i)))
        Sounds[Sound] = i
        def on_press(key):
            print('{0} pressed'.format(key))
            for beat in self.beat:
                keys[key] = i

            return False

        with Listener(on_press = on_press) as listener:
            listener.join()


root = Tk()
x = Program(root)
root.mainloop()
