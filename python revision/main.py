name = "ali"
age = 17
# indentation
print(f'hello i am {name} i have {age} years old')


# del string    // to delete element




s = "hello world"

# capitalize the first letters s.capitalize()
# capitalize all letters s.upper()
# lower case all letters s.lower()
# swape all the letters' cases s.swapcase()

# s.len() get the legnth of the string
# s.replace("world", everyone) // replace
# s.count('h') // get how many letter h in the string
# s.startswith() check if it starts with
# s.endwith() check if it end with

# s.split() make it array
# s.find("r") make it array





number = [1,2,3,4,5,6]
fruits = ['apples', 'oranges', 'grapes', 'pears']

# fruits[1]  // get index 1
# fruits[1] = blueberry // change index 1 to blueberry
# 'apples' in fruits  // check if apples is in fruit array
# len(fruits)  // get the legnth
# fruits.append("mangos")  // add element to the list
# fruits.remove("mangos")
# fruits.insert(2, "mangos") // add mangos in index 2
# fruits.pop(2) // remove index 2
# fruits.reverse()
# fruits.sort()  // sort alphabetical
# fruits.sort(reverse=true)





# tuple is an unchangeable list

# create tuple
fruitsTuple = ('apples', 'banans', 'oranges')

# you must put a comma if it is a single value
fruitsTuple2 = ('singe value',)





# objects
person = {
    'first_name': 'ali',
    'last_name': 'zaghloule',
    'age': 17
}

# person['first_name']  // get the first_name prop
# person.get('first_name')  // get the first_name prop

# person['phone'] = 10 // add a phone prop

# person.keys()  // get all props
# person.items()  // get all pros and items in a tuple
# del person['age']  // remove the age prop
# person.pop('age')  // remove the age prop

# person2 = person.copy()  // make a copy






 


# functions

def sayhello(name='person'): 
    return f'hello {name}'

getsum = lambda num1,num2 : num1 + num2

print(sayhello('ali'))
print(getsum(1,2))





# conditions
x = 15
y = 15

if x > y:
    print(f'{x} is bigger than {y}')
elif x < y:
    print(f'{y} is bigger than {x}')
else:
    print(f'{x} is equale to {y}')












