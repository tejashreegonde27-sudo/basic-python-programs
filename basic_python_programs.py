# Grade Checker Program

score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Student Grades Program

students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Display All Grades")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added successfully.")

    elif choice == 2:
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == 3:
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == 4:
        break

    else:
        print("Invalid choice.")


# Write to a File

file = open("sample.txt", "w")
file.write("Hello, this file is created using Python.\n")
file.write("Writing data into a file using write().")
file.close()

print("Data written to file successfully.")



# Read from a File

file = open("sample.txt", "r")
content = file.read()
file.close()

print("File Content:")
print(content)
