def show_report(expenses):

    if not expenses:
        print("No expenses recorded.")
        return

    total = 0

    print("\nExpense Report")
    print("-" * 20)

    for expense in expenses:
        print(
            f"{expense['category']}: ₹{expense['amount']}"
        )
        total += expense["amount"]

    print("-" * 20)
    print(f"Total Spent: ₹{total}")