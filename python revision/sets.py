# a set automatily removes the dublicates like the other 4 below
# a set is not ordered at all you can find every time a different order
# you can insert tuples inside the set but you can't insert arrays
my_set = {1,2,3,4, 4}

new_set = my_set.intersection({1, 2, 3})

print(new_set)
