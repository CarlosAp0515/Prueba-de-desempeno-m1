sw = True
def enter_id():
    while sw is not False:
        try:
            id = int(input("Enter student's id: "))
            if id <= 0:
                print("ID can't be negative or 0.")
            else:
                return id
        except ValueError:
            print("ID must be a numerical value")

def enter_age():
    while sw is not False:
        try:
            age = int(input("Enter student's age: "))
            if age <= 0:
                print("Age can't be negative or 0.")
            else:
                return age
        except ValueError:
            print("Age must be a numerical value")