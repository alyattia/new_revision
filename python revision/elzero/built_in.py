from functools import reduce

x = [1,2,3,4,5,6,7,8,9, 21, 4,2,4, 2, 1,4, 5,3, -19]

if all(x):
  print("all elements of x are true")
elif any(x):
  print("there is at least one element in x is true")
else:
  print("there is no elements true")


print(bin(0))# convert the arg to the computer language (0011001)

print(id(x))# get the id of the element from the data

print(sum(x, 0))# add all the list el and start from index 0

print(round(1.23456789, 2))# round to the nearest

print(list(range(0,6,2))) #range(start, end, step)

print("hello", "ali", "was gibt's", sep=" | ")

print(abs(-4018.13)) # the distance between the num and 0 (absolute value)

print(pow(2, 4, 10))# 2*2*2*2 % 10

print(min(x))# minmum value
print(max(x))# maximum value



"""
------------Map & Filter & Reduce function-------------
- it is a foreach loop but it saves the return in var
"""


words = ["apple", "banana", "cherry"]
def format_word(word):
  return f"- {word} -"

# the map is exactly a foreach loop but saves the values in a var
fromated = list(map(format_word, words))
second_formated = list(map(lambda word: f"* {word} *", words))

# the filter iterate on the array like the map and foreach but it checks if a condition is true return the current obj else don't
# will loop on the list and when it smaller than 5 (True) return the current num
filter_nums = list(filter(lambda num: num < 5, x))

# will loop and at the begining the result is index 0 and the current is index 2 then in the second loop the result becomes the return from the first loop and current is index 3 and so on until the end
sum_nums = reduce(lambda result, current: current + result, x)
# this will check every time if the
greatest_num = reduce(lambda prev, current: prev if prev > current else current, x)

# def get_greatest_num(num1, num2):
#   num1 if num1 > num2 else num2

print(fromated)
print(second_formated)
print(filter_nums)
print(sum_nums)
print(greatest_num)

""" --------- the end :) ---------"""

"""--------- enumerate -----------"""

myskills = ['Python', 'Java', 'js', 'react']

myskills_counter = enumerate(myskills)# enuerate(iterable, start)

print(dict(myskills_counter))
for count, skill in enumerate(myskills):
  print(count, skill)


print(help(enumerate))# get a help for a function from the documantation