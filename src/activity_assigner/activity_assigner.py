import xlrd

import sys
import random

from models.student import Student

def find_section(sheet=None, identifier=""):
    index = 0

    while(str(sheet.cell_value(index, 0)).lower() != identifier.lower()):
        index += 1

        if (index > sheet.nrows):
            return -1

    return index

def create_choices(sheet=None, index=0):
    # Initialize the choices
    choices = {}

    index = find_section(sheet=sheet, identifier="Options") + 1
    cell_value = sheet.cell_value(index, 0)
    while (cell_value != "Students" and cell_value != ''):
        choices[cell_value] = sheet.cell_value(index, 1)
        index += 1
        cell_value = sheet.cell_value(index, 0)

    return choices

def create_students(sheet=None, index=0, choices={}):
    # Create the students and add the choices for each
    students = []

    num_choices = sheet.ncols - 1
    num_students = sheet.nrows - len(choices) - 2

    index = find_section(sheet=sheet, identifier="Students") + 1
    cell_value = sheet.cell_value(index, 0)

    for i in range(num_students):
        cell_value = sheet.cell(index, 0).value

        students.append(Student(name=cell_value))

        for j in range(num_choices):
            choice = sheet.cell_value(index, j + 1)
            students[i].add_choice(choice=choice, rank=j)

        index += 1

    return students

def assign_choice(students=[], choices={}):
    random.shuffle(students)

    # Assign students to choices based son rankings
    assigned_students = []

    for i in range(len(students)):
        student = students[i]

        assigned = student.get_assigned()
        for choice in student.get_choices():
            if choice not in assigned and choice in choices:
                rank = len(student.assigned)
                student.add_assigned(choice=choice, rank=rank)

                # Update allowance
                curr_allowance = choices[choice] - 1
                choices[choice] = curr_allowance

                if curr_allowance == 0:
                    del choices[choice]

                break

        # Shift to assigned students
        assigned_students.append(student)

    students = assigned_students

def write_assignments(students=[]):
    # Write assignments to file
    write_loc = "./write_results.csv"

    for student in students:
        print(student.name, end='')

        for assignment in student.get_assigned():
            print(',' + assignment, end='')

        print()

# read_loc = sys.argv[1] if len(sys.argv) > 1 else input("Enter file name: ")
read_loc = sys.argv[1] if len(sys.argv) > 1 else "./src/activity_assigner/test/test.xlsx"

wb = xlrd.open_workbook(read_loc)
sheet = wb.sheet_by_index(0)

choices = create_choices(sheet=sheet)

print(choices)

students = create_students(sheet=sheet, choices=choices)
# random.shuffle(students)

for i in range(2):
    assign_choice(students=students, choices=choices)

    students.reverse()

write_assignments(students=students)

print(choices)