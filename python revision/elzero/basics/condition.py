country = input("Enter your country: ")
name = input("And your name: ").strip().capitalize()
names = ['Ali', "Boda", "Rehab", "Eyad"]

# one line if condition
if country == "Egypt": print("ebn balady")
elif country == "Austria": print("ely me2klany")
else: print("ma3rfk4")


# short if condition
print("ebn balady" if country == "Egypt" else "ma3rafak4")
print("habibi" if name in names else "ma3rafak4")
print("msh mn el 3elah" if name not in names else "3elah")


dic = {
  "js": {
    "main": "100%",
    "react": "80%",
  },
  "html": {
    "main": "100%",
    "pugjs": "60%"
  }
}

for k, v in dic.items():
  print(f"progress for {k} is: ")

  for child_k, child_v in v.items():
    print(f"{child_k} => {child_v}")


"""----------make for loop--------"""
nums = [1, 2, 3, 4]

for num in nums:
  print(num)

# same as the above
my_iterator = iter(nums)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))