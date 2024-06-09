"""
the "*" is like the "..." in js
the "*" makes *Arg in a fun(), so it expects that you will enter a tuple of arguments
the "**" makes **KwArg in a fun(), but this expects that you enter a dictionary
"""

def add(eq_type= "add", *nums):
  print(type(nums))

  total = 0

  for num in nums:
    try:
      int(num)
    except:
      return "Invalid number"

  for i in range(0, len(nums)):
    if eq_type == "add":
      total += int(nums[i])
    elif eq_type == "sub":
      total -= int(nums[i])
    elif eq_type == "multi":
      total *= int(nums[i])
    else:
      return "Invalid equation type"
  return f"the total is {total}"

eq_type = input("Enter the quation type: ")

nums = input('Enter the number: ').strip().split(',')
for i in range(0, len(nums)):
  nums[i] = nums[i].strip()

print(add(eq_type, *nums))
# print(add('add', 1, 2, 3)) # same as the above


def dict_fun(**my_dict):
  print(type(my_dict))
  for key, value in my_dict.items():
    print(f"{key} => {value}")


user = {
  "name": "Ali",
  "age": 19,
  "country": "Egypt"
}

print(dict_fun(**user))
print(dict_fun(name="ALi", age=19, country="Egypt")) #same as the above




x = 1

def change_global_scopt():
  global x
  x = "I changed the global scop var from a fun hahaha"

change_global_scopt()
print(f'x from global scopt is {x}')




# recursive funciton (fun btnady nafsha gwa nafsha)


test_word =  "WWWoooorrrldd"
# this fun removes the repeated letters from a fun
def cleanWord(word):
  print(f"word at the beginning {word} and len {len(word)}")
  # if the word already consists of 1 letter
  if len(word) == 1:
    print(f"el 5olasa {word}")
    return word


  if word[0] == word[1]: #1.W==W 2.W==W 3.W==o (WWWoooorrrldd)
    print(f"word after the 1st condition {word}")
    return cleanWord(word[1:])

  print(f"word before last return {word}")
  print(f"word[0] {word[0]} and word[1:] {word[1:]}")
  return word[0] + cleanWord(word[1:])
  #stash = "W"

print(cleanWord(test_word))




"""
----------Lambda function (Anonymous function)-----------
- you can use it inline
- use it only with small tasks
- it is used to return data from another function
- it must be one expresiton not a block of code
"""

def sayHello(name): return f"Hello {name}"

hello = lambda name, age: f"Hello {name} with age {age}" # same as the above





users = {
  1: {
    "name": "Ali",
    "age": 19
  },
  2: {
    "name": "Obad",
    "age": 17
  }
}

