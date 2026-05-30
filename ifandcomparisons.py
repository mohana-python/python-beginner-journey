#age checker
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#Even or Odd
num=int(input("Enter a number:"))
if num %2 ==0:
    print("Even number")
else:
    print("Odd number")

#Student Grade Calculator

marks=int(input("Enter your marks: "))
if marks > 100 or marks < 0:
    print("Invalid marks")
elif marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Grade D")