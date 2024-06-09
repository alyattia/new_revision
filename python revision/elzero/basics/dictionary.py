"""
- keys must be immuatble
"""

user = {
    "name": "obad",
    "age": 19,
    "skills": ["java", "python"],
    "rating": 4.5,
    1: "mohamed ramadan",
    #the name will change to obad auto bec you can't put more than one key so it will take the value of the last one
    "name": "Ali",
    "friends": {
        1: {"name": "Obad", "age": 17},
        2: {"name": "Mama", "age": 45},
        2: {"name": "Eyad", "age": 7},
    }
}


print(user["name"])
print(user["friends"][1])
print(user.get("age"))# both are the same
print(user.keys())
print(user.values())
print(len(user))# len of the dict
print(user.setdefault("isActive", True))# will see if this key exist get it and if not make it True
print(user.popitem()) # will return the last added element
print(user.items()) # will return a list of tuples with the dict items

# user.clear()
user["country"] = "egypt"
# user.update("country", "egypt") # same as above
user2 = user.copy()


a = ("name", "age")
b = ['ali', 19]

print(dict.fromkeys(a, b))


