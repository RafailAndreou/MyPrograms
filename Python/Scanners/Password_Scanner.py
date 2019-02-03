
import os, time, glob, shutil

Working_file_path = "D:"

Desktop_path = "c:" + os.sep + os.path.join(os.environ["HOMEPATH"], "Desktop")

Document_path = "c:" + os.sep + os.path.join(os.environ["HOMEPATH"], "Documents")

counter = 1

print ("        All Desktop files        ")

time.sleep(2)

for file in os.listdir(Desktop_path):
    print(file)

time.sleep(2)

print("        All  Desktop files that have the word pass        ")

time.sleep(2)

os.chdir(Desktop_path)

for file in glob.glob('pass*'):
    print(file)
    shutil.copy(file,Working_file_path)
    
time.sleep(2)
    
print("        All Document files        ")

time.sleep(2)

for file in os.listdir(Document_path):
    print (file)

time.sleep(2)

print("        All  Document  files that have the word pass        ")

time.sleep(2)

os.chdir(Document_path)

for file in glob.glob('pass*'):
    print (file)
    shutil.copy(file,Working_file_path )

 

os.chdir(Working_file_path)
    
for file in glob.glob('pass*'):
    os.rename(file,str(counter)+'.txt')
    counter += 1
