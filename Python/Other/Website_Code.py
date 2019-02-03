import urllib.request
import os

Desktop_Path = "C:" + os.sep + os.path.join(os.environ["HOMEPATH"],"Desktop")

Url = input("What is the url of the website you want: ")

Code = urllib.request.urlopen(Url)

print(Code.read())

File = ("What is the name of the file you want to download: ")

os.chdir(Desktop_Path)

Download = urllib.request.urlretrieve(Url,File)



