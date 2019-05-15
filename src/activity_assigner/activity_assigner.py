import sys
import random

from models.student import Student

# Create the students and add the choices for each
def create_students(choice_list=None, choices={}):
    students = []

    choice_list.readline()

    num_student = 0
    for line in choice_list:
        cells = line.split(",")

        email = cells[1].strip("\"")
        last_name = cells[2].strip("\"")
        first_name = cells[3].strip("\"")

        students.append(Student(email=email, first_name=first_name, last_name=last_name))

        # Add and create new choices
        student_choices = cells[4:]
        for i in range(len(student_choices)):
            choice = student_choices[i]
            
            # Strip newlines and quotes
            choice = choice[0:len(choice) - 1] if choice[len(choice) - 1] == '\n' else choice
            choice = choice[1:len(choice) - 1]

            students[num_student].add_choice(choice=choice, rank=i)

            if not choice in choices:
                choices[choice] = 0

        num_student += 1

    return students

# Set the limits of each choice
def set_choice_limits(choices={}):
    for choice in choices:
        choices[choice] = int(input("[" + choice + "] Enter the number of spots available: "))

# Assign students to choices based on rankings
def assign_choice(students=[], choices={}):
    random.shuffle(students)

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
    students.reverse()

# Write assignments to file
def write_assignments(students=[], num_choices=0):
    write_loc = input("Enter save location: ")

    f = open(write_loc, "w")

    f.write("Email,Last Name,First Name")

    for i in range(num_choices):
        f.write(",Choice " + str(i + 1))

    f.write('\n')

    for student in students:
        f.write(student.email + ',')
        f.write(student.last_name + ',')
        f.write(student.first_name)

        for assignment in student.get_assigned():
            f.write(',' + assignment)

        f.write('\n')

    f.close()

read_loc = sys.argv[1] if len(sys.argv) > 1 else input("Enter file name: ")

choices = {}

with open(read_loc) as choice_list:
    students = create_students(choice_list=choice_list, choices=choices)

set_choice_limits(choices=choices)

NUM_CHOICES = 2
for i in range(NUM_CHOICES):
    assign_choice(students=students, choices=choices)

write_assignments(students=students, num_choices=NUM_CHOICES)

print(choices)