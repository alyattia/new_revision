# """
# ! all the data in python are objects
# use type() to know the type of something
#
# special charecters:-
# \b backspace
# \ => new line and escape character
# \n => new line
# \r => replace "abc\r123" = output => "123abc"
# \t => make tap between letters
# \xhh
# """

text = "hello world my name is ali"

print(text[0:6])
print(text[:6])
print(text[6:])
print(text[::2])# make him yfwet space so the output will be => "hlowrd"
print(len(text))
print(text.strip()) #remove spaces from behind and forword "   hey   " => "hey"
print(text.rstrip())#remove spaces forword "   hey   " => "   hey"
print(text.lstrip())#remove spaces from behind "   hey   " => "hey   "
print(text.strip('#'))#remove hashes from behind and forword "###hey###" => "hey"

print(text.title()) # make every first letter of every word capital
print(text.istitle())
print(text.capitalize()) # make the first letter capital
print(text.upper())#make every letter upercase
print(text.isupper())
print(text.lower())#make every letter lower case
print(text.islower())
print(text.swapcase()) # swape every case "AlisS" => "aLISs"

num1, num2, num3 = '1', '11', '111'

print(num1.zfill(3))# will make it "001" bec you entered in the brackets 3 so 3 digits


print(text.split(' ')) # make it list from every space
print(text.split(' ', 2)) # maxsplit is num 2 make it make split only 2 times
print(text.rsplit(' ', 2)) # like the above but from the right


a = "helloe" #len == 5
# make it len 8 (if it is smaller) and subsitude the missing with #
print(a.center(8, "#"))


print(a.index('e')) #show me the index of that letter
print(a.find('e')) #the same but don't make error if the letter not found
print(text.count("l")) #how many "l" in the string ==> 4
print(text.count("l", 5, 25)) #how many "l" in the string from index 5 to index 25 ==> 2

print(a.startswith('h')) # => True
print(a.endswith('h')) # => False
print(a.startswith('h', 3)) # from index 3 starts with "h"?

b = "ali22"
c = "ali"

print(b.isalpha())
print(b.isalnum())



e = "hello ali i am the manger ali"
list = ['ali', 'obad', 'rehab', 'eyad']

f = e.replace('ali', 'obad', 2)
listString = ', '.join(list)



num = 19
print("my name is {}".format("ali"))
print("my name is {}".format(c))
# s=string d=number f=float
print("my name is {:s} and my age is {:d} my rank is {:f}".format(c, num, 2.5))
