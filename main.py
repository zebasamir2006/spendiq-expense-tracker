from expense import add_expense, view_expenses, update_expense, delete_expense
from analytics import (
    total_expenses,
    category_wise_expenses,
    highest_expense,
    lowest_expense,
    monthly_summary
)
from charts import (
    category_bar_chart,
    category_pie_chart,
    monthly_line_chart
)
from exports.export import export_to_csv


while True:
    print("\n========== SMART EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Analytics")
    print("6. Charts")
    print("7. Export to CSV")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter title: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")

        add_expense(title, amount, category, date)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        expense_id = int(input("Enter Expense ID: "))
        title = input("Enter new title: ")
        amount = float(input("Enter new amount: "))
        category = input("Enter new category: ")
        date = input("Enter new date (YYYY-MM-DD): ")

        update_expense(expense_id, title, amount, category, date)

    elif choice == "4":
        expense_id = int(input("Enter Expense ID to delete: "))
        delete_expense(expense_id)

    elif choice == "5":
        print("\n------ ANALYTICS ------")
        total_expenses()
        category_wise_expenses()
        highest_expense()
        lowest_expense()
        monthly_summary()

    elif choice == "6":
        print("\n1. Bar Chart")
        print("2. Pie Chart")
        print("3. Monthly Line Chart")

        chart_choice = input("Choose a chart: ")

        if chart_choice == "1":
            category_bar_chart()
        elif chart_choice == "2":
            category_pie_chart()
        elif chart_choice == "3":
            monthly_line_chart()
        else:
            print("Invalid choice!")

    elif choice == "7":
        export_to_csv()

    elif choice == "8":
        print("Thank you for using Smart Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")