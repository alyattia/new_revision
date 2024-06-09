import datetime

print(datetime.datetime.now())# current date
print(datetime.datetime.now().month)# current date
print(datetime.datetime.now().day)# current date
print(datetime.datetime.now().time().hour)# current date

# min and max time
print(datetime.datetime.min)
print(datetime.datetime.max)

birthday = datetime.datetime(2005, 9, 22)
currentdate = datetime.datetime.now()

print(f"I lived for {(currentdate-birthday).days} days")

# formating date and time go to https://strftime.org/
my_birthday = datetime.datetime(2005, 9, 22)
eyad_birthday = datetime.datetime(2017, 2, 23)
oabd_birthday = datetime.datetime(2007, 4, 1)

print(eyad_birthday.strftime("%A %d.%b.%Y"))
print(oabd_birthday.strftime("%A %d %b %Y"))
