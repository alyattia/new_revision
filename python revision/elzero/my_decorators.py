"""
- decorators is a high order function (takes a fun as a param)
- decorators takes your function and make something before it and after it
so it decorats the function
"""
from time import time
"""-----------explanation-------------"""
# def my_decorator(fun):
#   def nestedFun(name):
#     names = ["ali", "rehab", "obad", "eyad"]
#     if name not in names:
#       print("warning you are not family")
#     fun(name)
#   return nestedFun
#
#
# @my_decorator
# def sayHello(name):
#   print(f"hallo {name}")
#
#
# sayHello(input("What is your name: "))


"""---------speed test----------"""
# def speedTest(fun):
#   def wrapper():
#     start = time()
#     fun()
#     end = time()
#     print("The function took", end - start, "")
#   return wrapper
#
# @speedTest
# def test_fun():
#   for i in range(0, 1000000):
#     print(i)
#
# test_fun()



"""---------Zip----------"""
# takes the length of the smaller list and make it so
list1 = [1,2,3,4,5]
list2 = ["a", "b", "c"]
my_zip = zip(list1, list2)
for item in my_zip:
  print(item)
  # => (1, 'a')
  # (2, 'b')
  # (3, 'c')
print('-'*40)

tuple1 = ('man', 'women', 'boy', 'girl')
dict1 = {'name':'ali', 'age':19, 'city':'New York'}

for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):
  print(f"List 1 item: {item1}")
  print(f"List 2 item: {item2}")
  print(f"tuple 1 item: {item3}")
  print(f"dict 1 value: {dict1[item4]}")
