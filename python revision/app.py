# print("hello world")
# name = "ali" #string
age = int(input("How old are you: ")) #int
salary = int(input("Your salary: ")) #int
money = 3.5 #float
taken = False #boolean
name = input("Enter your name: ")
"""
? the input automatlicly coverts to string"""
# family_members = int(input("how many family members: "))

print("-----------------")
print("Name: " + name)
print("Age: " + str(age))
# print(family_members)


if age < 18:
  print("you are joung")
elif age >=18 and age < 40:
  print("you are medium")
# elif age >=18 or age < 40:
#   print("you are medium")
else:
  print("you are old")

message = "can drive" if age >= 18 else "cannot drive"
print(message)


print("while loop")
i = 1
while i <= 5:
  print(i)
  i += 1

print("for loop")
for letter in "Python zft":
  print(letter)


def caluculate_nett_salary(age, salary = 0):
  net_salary = 0
  if age <= 21:
    if salary > 1500 and salary <= 2000:
      net_salary = salary - 200
    elif salary > 2000:
      net_salary = salary - 400
    else:
      net_salary = salary
  else:
    if salary > 1500 and salary <= 2000:
      net_salary = salary - 300
    elif salary > 2000:
      net_salary = salary - 600
    else:
      net_salary = salary - 100
  return net_salary


print("----------------------------")
print(caluculate_nett_salary(age, salary))

