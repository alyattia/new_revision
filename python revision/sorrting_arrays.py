grades = [12, 54, 21, 100, -4, 65, 87, 34, 44, 54, 5]

# bubble sort algorithm to sort from lowest to highest
# length = len(grades)
# for i in range(0, length-1):
#   for compare in range(length-i-1):
#     current_grade = grades[compare]
#     second_grade = grades[compare+1]
#     if current_grade > second_grade:
#       grades[compare] = second_grade
#       grades[compare+1] = current_grade

# or you can einfach make so
grades.append(13) # will put it at the end
print(grades)
grades.sort(reverse=True)
print(grades)