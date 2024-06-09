x = 10

if x < 0:
  raise Exception(f"leider {x} ist negativ")

try:
  number = int(input("enter a number: "))
except:
  print("invalid number")
else: # if there is no errors
  print(number)
finally: # this will happen anyways if there is an error or not
  print("this will happen anyways")