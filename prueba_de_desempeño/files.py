#CSV function to save the data
def save_csv(students, road):
    if not students:
        print("Students is empty")
        return False

    try: 
        with open(road,"w") as file:
            file.write("name id, age, course, state \n ")

            for student in students:
                file.write(f"{student['name']},{student['id']},{student['age']},{student['course']},{student['state']}\n")
        return True
    except Exception as e:
        print("Error:", e)
        return False
#CSV function to load the data        
def load_csv(road):
    students = []
    try:
        with open(road, "r") as file:
            next(file)
            
            for line in file:
                line = line.strip()
                
                if not line:
                    continue
                
                data = line.split(",")
                
                student = {
                    "name": data[0],
                    "id": int(data[1]),
                    "age": int(data[2]),
                    "course": data[3],
                    "state": data[4]
                }
                students.append(student)
        return students
    except Exception as e:
        print("Error:", e)
        return []
