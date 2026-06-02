categories = []
expenses = []

for i in range(1, 4):
    category = input(f"Enter Category {i}: ")
    categories.append(category)

    expense = float(input(f"Enter Expense {i}: "))
    expenses.append(expense)

total = sum(expenses)
highest = max(expenses)
average_expense = total / len(expenses)

print("\n===== EXPENSE REPORT =====")

for i in range(len(categories)):
    print(categories[i], "- $", expenses[i])

print("\nTotal Spending: $", total)
print("Highest Expense: $", highest)
print("Average Expense: $", round(average_expense, 2))

