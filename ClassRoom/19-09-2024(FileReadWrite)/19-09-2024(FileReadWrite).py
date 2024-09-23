#create file handel

filename="people-100.csv"

# file=open(filename,"w")

#write data in file
# file.write("hello, this is a text!!")

# #save and close file
# file.close()

file = open(filename, "r")

file.close()

rows=file.split("\n")

for row in rows:
    print(f"row is {row}")

# fileContent = file.read()
# print(fileContent)  
# file.close()