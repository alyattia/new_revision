"""
- the sets are not ordered and not indexed every time you print a set it will be with diff. order
- so you can't make slicing in tuples (slice is list[0:2])
- you can only put the immuatble data inside it

- all elements of it are unique so if there is dublicates it will automaticly remove them
"""


# you can't put list or dic in the set
tuples_lesson = {"ali", 100, 2.99, True, ("only", "tuples are allowed")}
a = {"ali", 100, 2.99, True}
b = {"rehab", "obad", "ali", 100}

# a.clear()
c = a.union(b)# the union must be added to an var
same_as_above = a | b # same as the above
# a.update(b)# this will add b to a
# a.update([["ay7aga", "sss"]]) # will add the elements inside the list to the set

b.add("eyad")
e = b.copy()
b.remove("obad")# it will show err if the el is not found
a.discard("alssi") #the discard will not give error if it didn't find the el
c.pop()# the pop() here removes a random el

print(c)
# only shows elments from the original set
print(a.difference(b)) # show me all the NOT common elements from the original set
print(a-b) # same as the above one
#it will show elements from the original and the other set
print(a.symmetric_difference(b))# show me all the NOT common between 2 sets
print(a^b)# same as the above one
# a.difference_update(b)# will remove all the common elements from the original set
# a.symmetric_difference_update(b)
print(a)

print('-'*40)
print(a.intersection(b)) # get all the common elements
print(a & b) # same as the above one
a.intersection_update(b) #change the original set to the comment el between the 2 sets
print(a)

print('-'*40)
print(a.issubset(b)) # checks if all the el in b are in a
print(a.issuperset(b)) # checks if all the el in a are in b
print(a.isdisjoint(b)) # checks if there is aslun any common elements or not

