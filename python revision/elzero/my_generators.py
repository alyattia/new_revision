"""
[1] Generator is a Function With "yield" Keyword Instead of "return"
[2] It Support Iteration and Return Generator Iterator By Calling "yield"
[3] Generator Function Can Have one or More "yield"
[4] By Using next() It Resume From Where It Called "yield" Not From Begining
[5] When Called, Its Not Start Automatically, Its Only Give You The Control
"""

def my_generator():
  yield 1
  yield 2
  yield 3
  yield 4

myGen = my_generator()

# when you press next it prints the next yield every time
print(next(myGen))
print(next(myGen))
for num in myGen:
  print(num)# => 3, 4 // only 3 and 4 because you already used the 1st and 2nd yields with values 1 and 2