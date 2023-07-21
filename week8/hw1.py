students = ['John', 'Peter', 'Mary', 'Jane', 'Tom', 'Jerry', 'Alice', 'Bob']
departments = ['IT', 'GD', 'IT', 'Biz', 'Biz', 'GD', 'IT', 'GD']
GPAs = [3.5, 3.0, 3.2, 3.6, 3.8, 3.9, 3.7, 3.4]

# Enter student name, find student and print his/her GPA and department
def find_student():
    name = input('Enter student name: ')
    for i in range(len(students)):
        if students[i] == name:
            print(f'{name}: GPA = {GPAs[i]}, department {departments[i]}')
# Enter department name, find students in that department and print their names and GPAs
def find_student_in_dept():
    dept = input('Enter department name: ')
    print('Students in department', dept)
    for i in range(len(departments)):
        if departments[i] == dept:
            print(f'{students[i]}: GPA = {GPAs[i]}')
# Find best student (highest GPA)
# Enter a GPA, count how many students have GPA >= that GPA
def count_better():
    count = 0
    gpa = float(input('Enter a GPA: '))
    for g in GPAs:
        if g >= gpa:
            count += 1
    print(f'{count} students have GPA >= {gpa}')
# Calculate average GPA of students in all departments
# Calculate average GPA of students in each department
def average_dept():
    sum_gpa_it = 0
    count_it = 0
    sum_gpa_gd = 0
    count_gd = 0
    sum_gpa_biz = 0
    count_biz = 0
    for i in range(len(departments)):
        if departments[i] == 'IT':
            sum_gpa_it += GPAs[i]
            count_it += 1
        elif departments[i] == 'GD':
            sum_gpa_gd += GPAs[i]
            count_gd += 1
        else:
            sum_gpa_biz += GPAs[i]
            count_biz += 1
    print(f'Average GPA of IT students: {sum_gpa_it/count_it:.2f}')
    print(f'Average GPA of GD students: {sum_gpa_gd/count_gd:.2f}')
    print(f'Average GPA of Biz students: {sum_gpa_biz/count_biz:.2f}')
#find_student()
#find_student_in_dept()
#count_better()
average_dept()