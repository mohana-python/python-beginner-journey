#Add student details
#Store marks
#Calculate average
#Assign grade
#Display all students

students = []

n = int(input("How many students do you want to enter? "))

for i in range(n):
    print(f"\nStudent {i+1}")

    name = input("Enter name: ")
    python_marks = int(input("Enter Python marks: "))
    math_marks = int(input("Enter Math marks: "))
    english_marks = int(input("Enter English marks: "))

    total = python_marks + math_marks + english_marks
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "D"

    student = {
        "name": name,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)

print("\n===== STUDENT REPORT =====")

for s in students:
    print("\nName:", s["name"])
    print("Total:", s["total"])
    print("Average:", round(s["average"], 2))
    print("Grade:", s["grade"])

