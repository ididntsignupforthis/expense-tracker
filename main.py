from app.expense_manager import add_expense, get_expenses
from app.report import show_report

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Report")
    print("3. Exit")
    print("4. Show number of expenses")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Category: ")
        amount = float(input("Amount: "))
        add_expense(category, amount)

    elif choice == "2":
        expenses = get_expenses()
        show_report(expenses)
    elif choice == "4":
        expenses = get_expenses()
        print(f"Total expenses recorded: {len(expenses)}")
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")