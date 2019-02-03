import os

Desktop_Path = "C:" + os.sep + os.path.join(os.environ["HOMEPATH"],"Desktop")

os.chdir(Desktop_Path)

Words = open("Words.txt","r")

x = Words.readlines()

Words.close()

for word in x:
    Words1 = print(word.upper())






