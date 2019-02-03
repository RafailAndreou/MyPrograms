import os, sys
 
Name = input("Give the file name: ")
 
divider  = int(input("Give the divide number: "))
 
Size = os.path.getsize(Name)
 
bytes_per_file = Size // divider
 
if bytes_per_file == 0:
    print("The file is very small and can't be divited to",divider,"parts.")
    sys.exit()
 
 
counter = 1
 
read_file = open(Name, 'rb')
 
 
while True:
 
    max_bytes = read_file.read(bytes_per_file)

    if not max_bytes:
        break
 
    write_file = open(str(counter) , 'wb')
 
    write_file.write(max_bytes)
 
    write_file.close()
 
    counter += 1
 
 
read_file.close()
 
print("The file", "Name", "divided successfully!")
