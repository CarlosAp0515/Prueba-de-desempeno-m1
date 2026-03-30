from files import *
from functions import *
from helpers import *

students = load_csv("Students.csv")
if students is None:
    students = []

option = ""

while option != "6":
    print("\n-----------Students database----------------\n")
    option = input("\nSelect an option.\n"
                    "1. Register a new student. \n"
                    "2. Consult the list of students.\n"
                    "3. search for a student using their ID.\n"
                    "4. Update the studen't information.\n"
                    "5. elimate students\n" 
                    "6. Exit.\n"
                     ": " )
    if option == "1":
        name =input("Enter the student's name: ").capitalize().strip()
        id = enter_id()
        age = enter_age()
        course = input("Enter the student's course or program: ").strip()
        state = input("Enter the student's state (active/inactive): ").strip()
        add_new_student(students,name,id,age,course,state)
        print("\nstudent successfully added.\n")
    elif option == "2":
        show_students(students)
    elif option == "3":
        id = enter_id()
        student = search_student(students,id)     
        if student:
            print(f"Student found: name: {student['name']} | id: {student['id']} | age: {student['age']} | course: {student['course']} | state: {student['state']}")
        else:
            print("Student not found")

    elif option == "4":

        id = enter_id()

        new_age_input = input("Enter the new student's age: ").strip()
        new_course_input = input("Enter the new student's course or program: ").strip()
        new_state_input = input("Enter the new student's state(active/inactive): ").strip()


        new_age = int(input("Rectify the new age: ")) if new_age_input != "" else None
        new_course = input("Rectify the new student's course or program: ") if new_course_input != "" else None
        new_state = input("Rectify the new student's state (active/inactive): ") if new_state_input != "" else None


        update = update_inf_student(students,id,new_age,new_course,new_state)

        if update:
            print("The student has been successfully updated")
        else:
            print("Student not found")
    elif option == "5":
        id = int(input("Enter the ID that you want to delete: "))

        delete = delete_student(students, id)

        if delete:
            print("Student has been sucessfully removed.")
        else:
            print("Student not found")
    elif option == "6":
        save_csv(students,"students.csv")
        print("HAVE A GOOD DAY!!!")
    else:
        print("Invalid option")




