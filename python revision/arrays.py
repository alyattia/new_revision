# grades = []

# print(grades)
# for i in range(0,4):
#   grade = input("Enter a grade: ")
#   grades.append(int(grade))

# print(grades)


grades = [85, 98, 75, 65, 48, 59, 88, 75, 99, 42]

search = int(input("Enter a grade to search: "))
for i in range(0, len(grades)):
  if grades[i] == search: 
    print(f"Grade found at index {i}")
    break
  elif i+1 == len(grades):
    print("There is no such a grade")