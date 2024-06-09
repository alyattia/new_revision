"""
- __name__ and __main__ those are built in variables and when the __name__ is equal to
__main__ that means that the file is running directly without importings
"""
import string
import random

print(__name__)

# make random serial number
print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

def genrate_serial(count):
  all_chars = string.ascii_letters + string.digits
  all_chars_len = len(all_chars)

  serial_list = []
  while count > 0:
    random_number = random.randint(0,all_chars_len - 1)
    random_char = all_chars[random_number]
    serial_list.append(random_char)
    count -= 1
  return ''.join(serial_list)


print('-'*40)
print(genrate_serial(30))