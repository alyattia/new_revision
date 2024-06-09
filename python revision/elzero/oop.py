"""
Attributes: sefat like name, age, and so. if you took the car example so the attr is the color, price, and so
Methods: is the functionality so in the car ex it is the walking stopping, and so
class: is the teplate that you create many objects from
"""
from abc import ABCMeta, abstractmethod

class Car:
  # the init is a magic methods or dunder methods and it intializes the data for the obj you will creat
  # the self bt3ood 3la el obj that you will make from the class

  cars_num = 0
  not_allowed_names = ["Ford", "Porch"]
  def __init__(self, name, year, price=0, id=0, id2=0):
    self.name = name
    # to use a var from inside the class just use the Class.variable
    if self.name in Car.not_allowed_names:
      raise NameError("This car is not valid")
    self.year = year
    self.price = price
    self._id = id # protected method: can access it only from inside the class or subclasses
    self.__id = id # private method: can access it only from inside this class
    Car.cars_num += 1

  def discount(self):
    if self.price > 0:
      if self.price > 50000:
        self.price -= 2000
      else:
        self.price -= 1000
    else:
      return "the care has no price"

  def delete_car(self):
    Car.cars_num -= 1

  # to deal with private and protected attributes (encapsulation)
  # the property decorator makes this fun() be dealed with as property (attribute) not as function we are using it with funcs that are returning only a thing
  @property
  def get_id(self):
    return self._id
  def set_id(self, new_id):
    self._id = new_id

  # the magic method __str__ returns human readable info
  def __str__(self):
    return f"name is {self.name}, year is {self.year}, price is {self.price}"

  # the return from this fun will return when you use len(Car)
  def __len__(self):
    return Car.cars_num

  # this is a class method that has access on the class itself and deals with it and this "cls is the class itself"
  @classmethod
  def show_cars_availble(cls):
    return cls.cars_num

  # this is a static method it don't has access on the class or the instance but related to the class
  @staticmethod
  def say_hello():
    print("Hello")






car1 = Car("BMW", 2019, 55000)
car2 = Car("Wolkswagen", 2021, 20000)
car3 = Car("Fords", 2021, 20000)

print(dir(car1))
print('-'*40)

car1.discount()
Car.discount(car3)# same as the above here the car3 is the self but python makes that automaticly
print(car1.price)
print(car3.name)
print(Car.cars_num)
Car.__init__(car3, 'BYD', 2014, 10000)
print(car3.name)
print(Car.show_cars_availble())
print(car3.__class__)# to see which the class the object belongs to
print("ali".__class__)
print(car3.__str__())
print("ali".__str__())


# inheritance to inerit all the things from a specific class
class MyCar(Car):
  # if you defined an __init__ so like that you are overwritting the base class's init to prevent make
  def __init__(self, name, year, price, amount):
    # Car.__init__(self, name, year, price)# create instance from base class method 1
    super().__init__(name, year, price)
    self.amount = amount

car5 = MyCar("BMW", 2019, 100000, 24)
print(car5.name)


class Another_car(MyCar):
  def __init__(self, name, year, price, amount):
    super().__init__(name, year, price, amount)

car6 = Another_car("5ara", 2019, 10, 2)
print(car6.amount)


# Abstract class: is a class that actually don't do anything but you can inherit classes from it
class Abstract_class(metaclass=ABCMeta):
  # this func has acutally no functionalities but it is here to use it from inherited classes
  @abstractmethod
  def from_inherits(self):
    pass



