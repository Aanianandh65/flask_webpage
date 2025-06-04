import os

FILENAME = "students.txt"

def add_student():
    with open(FILENAME, "a") as file:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        file.write(f"{roll},{name},{marks}\n")
    print("✅ Student added successfully.\n")

def view_students():
    if not os.path.exists(FILENAME):
        print("❌ No records found.\n")
        return

    with open(FILENAME, "r") as file:
        print("\n🎓 All Student Records:")
        print("----------------------------")
        for line in file:
            roll, name, marks = line.strip().split(",")
            print(f"Roll No: {roll} | Name: {name} | Marks: {marks}")
        print()

def search_student():
    roll_no = input("Enter Roll Number to search: ")
    found = False
    with open(FILENAME, "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            if roll == roll_no:
                print(f"\n✅ Found:\nName: {name}, Marks: {marks}\n")
                found = True
                break
    if not found:
        print("❌ Student not found.\n")

def delete_student():
    roll_no = input("Enter Roll Number to delete: ")
    lines = []
    found = False
    with open(FILENAME, "r") as file:
        lines = file.readlines()

    with open(FILENAME, "w") as file:
        for line in lines:
            roll, name, marks = line.strip().split(",")
            if roll != roll_no:
                file.write(line)
            else:
                found = True

    if found:
        print("✅ Student deleted successfully.\n")
    else:
        print("❌ Student not found.\n")

def menu():
    while True:
        print("📘 Student Record System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting... Bye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

# Run the application
if __name__ == "__main__":
    menu()
