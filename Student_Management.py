# Student Management System

students = {}

# add student function
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    students[roll] = {
        "name": name,
        "age": age
    }

    print("✅ Student added successfully")


# view students
def view_students():
    if not students:
        print("No students found")
        return

    print("\nStudent List:")
    for roll, info in students.items():
        print(f"Roll: {roll}, Name: {info['name']}, Age: {info['age']}")


# search student
def search_student():
    roll = input("Enter Roll Number to search: ")

    if roll in students:
        print("Student found:")
        print(students[roll])
    else:
        print("❌ Student not found")


# delete student
def delete_student():
    roll = input("Enter Roll Number to delete: ")

    if roll in students:
        del students[roll]
        print("🗑 Student deleted")
    else:
        print("Student not found")


# main menu
while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")