FILE_PATH = "data/expenses.txt"

def add_expense(category, amount):
    with open(FILE_PATH, "a") as file:
        file.write(f"{category},{amount}\n")

def get_expenses():
    expenses = []

    try:
        with open(FILE_PATH, "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                expenses.append({
                    "category": category,
                    "amount": float(amount)
                })

    except FileNotFoundError:
        pass

    return expenses