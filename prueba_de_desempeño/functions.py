def add_new_student(students,name,id,age,course,state):
    while id <= 0:
        try:
            if id <= 0:
                print("ID can not be 0 or negative")
                id = int(input("Enter student's id: "))
        except ValueError:
            print("ID muste be a numerical value")
            id = int(input("Enter student's ID: "))

    while age <= 0:
        try:
            if age <= 0:
                print("age can not be 0 or negative.")
                age = int(input("Enter the student's age: "))
        except ValueError:
            print("Age must be a numerical value")
            age = int(input("Enter the student's age: "))

    student = {
        "name": name,
        "id" : id,
        "age": age,
        "course": course,
        "state": state,
    }
    students.append(student)
    return True
    
def show_students(students):
    if not students:
        print("Students is empty.")
        return
    for student in students:
        print(f"Name: {student['name']} | id: {student['id']} | age: {student['age']} | course: {student['course']} | state: {student['state']}")

def search_student(students, id):
    for student in students:
        if student['id'] == id:
            return student
    return None

    
def update_inf_student(students,id,new_age=None,new_course=None,new_state=None):
    student = search_student(students,id)
    if student is None:
        return False
    
    if new_age is not None:
        while new_age <= 0:
            print("Age can not be 0 or negative")
            try:
                new_age = int(input("Enter the new age: "))

            except ValueError:
                print("Age must be a numerical value")
    if new_age is not None:
        student["age"] = new_age

    if new_course is not None:
        student["course"] = new_course

    if new_state is not None:
        student["state"] = new_state

    return True

def delete_student(students, id):
    student = search_student(students,id)
    if student is None:
        return False
    
    students.remove(student)
    return True
