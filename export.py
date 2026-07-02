import csv
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db import create_connection

def export_to_csv():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    conn.close()

    with open("exports/expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow(["ID", "Title", "Amount", "Category", "Date"])

        # Data
        writer.writerows(expenses)

    print("Expenses exported successfully to exports/expenses.csv")


if __name__ == "__main__":
    export_to_csv()