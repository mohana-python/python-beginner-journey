#Takes student name
#Takes marks
#Calculates grade (A/B/C/D)
#Displays a clean result

#Taking input from user
student_name = str((input("Enter Student Name: ")))
marks = int(input("Enter Your Marks: "))

print("\n===== STUDENT RESULT =====")
print("Studnet Name: ",student_name)
print("Marks: ",str(marks))

#checking marks and giving grade
if marks > 100 or marks < 0:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade A (Excellent)")
elif marks >= 75:
    print("Grade B (Good)")
elif marks >=50:
    print("Grade C (Average)")
elif marks >=35:
    print("Grade D (Below Average)")
else:
    print("You Failed - Needs Improvement")
