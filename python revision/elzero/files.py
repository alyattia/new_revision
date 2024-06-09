"""
----File handling---
"a" => append => open file and add something in there and create file if not exist
"r" => Read => [Defualt value] open file for read and give error if not exist
"w" => Write => open file for writing and create file if not exist
"x" => Creat => create file and give error if exists
"""
# when you are dealing with pathes make raro string => r"Z:\blabla\sython.py"

import os

print(os.getcwd()) # get the main current working directory
print(os.path.abspath(__file__)) # get the current abslute path "Z:\programing\python revision\elzero\files.py"
print(os.path.dirname(os.path.abspath(__file__)))# takes the file and gets the folder

# os.chdir("path") # changes the current working dir

print("-"*40)
myfile = open("test.py", 'r')

myfile.seek(4)# read the file from the 4th byte

print(myfile)
print(myfile.name)
print(myfile.mode)
print(myfile.encoding)

print("-"*40)
# print(myfile.read())
# print(myfile.readline())# read only one line
# print(myfile.readlines())# return an array of lines

# from the el esool "best practice" to close the file after finishing
myfile.close()



# write deletes all what in the file and put what you said
# append adds on the file
write_file = open("./write_file.txt", "w")

my_list = ["\nali\n", "bob\n", "charlie\n"]

write_file.write("a = 'ali'")
write_file.writelines(my_list)
print(write_file.tell()) # the place of the cursor

write_file.close()

# os.remove("./write_file.txt")# delete a file