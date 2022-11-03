#  Write a Python program to find the second lowest grade of any student(s) from the given names and grades 
# of each student using lists and lambda. Input number of students, names and grades of each student. 
# 
# Input number of students: 5
# Name: S ROY
# Grade: 1
# Name: B BOSE
# Grade: 3
# Name: N KAR
# Grade: 2
# Name: C DUTTA
# Grade: 1
# Name: G GHOSH
# Grade: 1
# Names and Grades of all students:
# [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
# Second lowest grade: 2.0
# Names:
# N KAR

student_info = []
total_students = int(input('Enter number of students: '))
for i in range(total_students):
    name = input('Name: ')
    grade = float(input('Grade: '))
    student_info.append([name,grade])

print('Names and Grades of all students: ')
print(student_info)
# student_info = [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 1.0], ['C DUTTA', 2.0], ['G GHOSH', 2.0]]

# get the unique grades and sort them in ascending order
unique_grades = list(set(map(lambda x: x[1], student_info)))
unique_grades.sort()
second_lowest_grade = unique_grades[1]

sec_low_students = filter(lambda x: x if x[1] == second_lowest_grade else '', student_info)

for i in sec_low_students:
    print('second lowest grade: ',i[1],', Name: ',i[0])
# print()


# ------------------Other Solution---------------------
students = []
sec_name = []
second_low = 0
n = int(input("Input number of students: "))
for _ in range(n):
   s_name = input("Name: ")
   score = float(input("Grade: "))
   students.append([s_name,score])
print("\nNames and Grades of all students:")
print(students)
# n = 5
# students = [['S ROY', 2.0], ['B BOSE', 3.0], ['N KAR', 1.0], ['C DUTTA', 2.0], ['G GHOSH', 2.0]]

order =sorted(students, key = lambda x: int(x[1]))
print(order)
for i in range(n):
   if order[i][1] != order[0][1]:
       second_low = order[i][1]
       break
print("\nSecond lowest grade: ",second_low)
sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()
print("\nNames:")
for s_name in sec_student_name:
   print(s_name)