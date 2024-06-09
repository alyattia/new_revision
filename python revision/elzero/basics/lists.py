"""
- the list can have more than one data type
- the list are muatable yaany can be changed
"""
a = ['ali', 'obad', 'apple', 'banana', 'kiwi', 'mama', 'eyad', 'ay7aga']
b = [1, 5, 3, 2, 6, 5, 7, 6]
c = ['apple', 'banana', 2, 4, 10.5, True, ['ali', 19]]

a[0] = "alli"
a[-1] = [] # this edits the last index of the list and leaves it empty so removing it
b[0:3] = [2, 3, 5] # edits the list to the following
b[0:3] = [1, 5] # you can also edit them with lower or higher number of elements as you like


print(a[1])
print(a[-2]) # last index from the end

print(a[1:4])# get from index 1 to 3 and don't count 4
print(a[:2]) # from 0 to 2
print(a[1:]) # from 1 to the end
print(a[1:4:2]) # from i 1 to i 4 and move 2 steps => ['obad', 'banana']
print(a[::2]) # from i 0 to the end (bec you didn't define any of them between the dots) and move 2 steps



# methods
e = ['ali', 'obad', 'apple', 'banana', 'kiwi', 'mama', 'eyad', 'ay7aga']
f = [1, 5, 3, 2, 6, 5, 7, 6]
g = ['apple', 'banana', 2, 4, 10.5, True, ['ali', 19]]

h = g.copy()

e.append('rehab') # will add smth at the end
e.insert(1, 'saleh') # will add smth at the index you want
e.append(['mohsen', 'abdo'])# will add the list to the list
e.extend(['ali', 'nour'])# will add the elements in the list to the list
e.remove('ali') # will remove the first "ali" from the list
print(e.pop(3))# will remove this index from the list and return it
f.sort(reverse=True)# if there is a mixed list will be error
f.reverse()# reverse the list
# e.clear()

print(e.count('ali'))
print(e.index('ali'))

print('----------------------------')
print(e)
print()


