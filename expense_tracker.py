expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append({
            "name": name,
            "amount": amount
        })

        print("Expense added successfully!")

    elif choice == "2":
        print("\n===== All Expenses =====")

        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for expense in expenses:
                print(expense["name"], ":", expense["amount"])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("Total Expense:", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")
