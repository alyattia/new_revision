"""
tuples are immutable so you can't edit anything in a tuple
"""

a = ('ali', 'obad', 'rehab', 'eyad', 'abdo', 'ali', True, 12, 4.44)

# a[2] = 'abo hemed' # geht nicht

print(a[1:4])

# to make a tuple with one element just put "," after the element
b = ('ali',)
print(len(b))


# tuple destruct
c = ('ali', 'body', 'mama', 'eggs', 'eyad')

# d, e, f, g = c #now every letter is a var with the tuple element
# if there is more than 4 values in the tuple there will be an error
# so to solve that just make
d, e, f, _, g = c

print(f"d={d} - e={e} - f={f} - g={g}")




