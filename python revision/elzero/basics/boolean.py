# those are the true data
print(bool(2))
print(bool(['rehab', 'obad']))
print(bool('ali'))
print(bool(True))

print('-'*40)

# those are the false values
print(bool(''))
print(bool(0))
print(bool(False))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(None))

print('-'*40)

age = 19
name = "ali"
country = "Egypt"

print(age == 19 and name == "ali" and country == "Egypt")
print(age == 19 and name == "ali" or country == "Egypt")
print(not age > 18)

print('-'*40)

print(10 == 10)
print(10 != 11)
