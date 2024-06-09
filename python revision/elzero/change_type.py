my_int = 10
my_string = "ali"
string_num = "11"
my_float = 2.99
my_bool = True
my_list = [1,2,3,4,5,6,7,8,9]
my_tuple = (1,2,3,4,5,6,7,8,9)
my_set = {1,2,3,4,5,6,7,8,9}
my_dictionary = {"name": "one", "age": "two"}

str(my_int)
a = int(string_num)
print(tuple(my_list))
print(tuple(my_set))# the set will be in a random order
print(tuple(my_dictionary))# => ('name', 'age')

print('-'*40)

print(list(my_tuple))
print(list(my_set))# the set will be in a random order
print(list(my_dictionary))# => ['name', 'age']

print('-'*40)

print(set(my_list))
print(set(my_tuple))
print(set(my_dictionary))# => {'name', 'age'}

print('-'*40)

# print(dict(my_string)) # can't be
# print(dict(string_num))# can't be
# print(dict(my_list))# can't be
# print(dict(my_tuple))# can't be
dict_tuple = (('name', 'ali'), ('age', 19))
dict_list = [('name', 'ali'), ('age', 19)]
print(dict(dict_tuple))
print(dict(dict_list))
# print(dict(my_set))# can't be

