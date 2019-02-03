import os, glob, shutil, time

Working_File_Path = "D:"

Image_File_Path = "c:" + os.sep + os.path.join(os.environ["HOMEPATH"], "Pictures")

Counter = 1

print("      All Images names     ")

time.sleep(2)

for file in os.listdir(Image_File_Path):
    print(file)

os.chdir(Image_File_Path)

for file in glob.glob("*.jpg"):
    shutil.copy(file,Working_File_Path)

os.chdir(Working_File_Path)

for file in glob.glob("*.jpg"):
    os.rename(file, str(Counter)+ ".jpg")
    Counter += 1

Counter = 1              

os.chdir(Image_File_Path)

for file in glob.glob("gif"):
    shutil.copy(file, Working_file_Path)

os.chdir(Working_File_Path)              

for file in glob.glob("*.gif"):
    os.rename(file, str(Counter) + ".gif")
              
os.chdir(Image_File_Path)

for file in glob.glob("*.png"):
    shutil.copy(file, Working_File_Path)

os.chdir(Working_File_Path)

for file in glob.glob("*.png"):
    os.rename(file, str(counter)+ ".png")

print(      "All Images have copy succesfull      ")


              
              
    
    
    







