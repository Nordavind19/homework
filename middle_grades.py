grades=[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students={'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
mid_grades={}
students_list = sorted(students)
for student, grade_list in zip(students_list, grades):
    mid_grades[student] = sum(grade_list) / len(grade_list)
print(mid_grades)







