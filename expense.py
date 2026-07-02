from database.db import create_connection

# Add expense
def add_expense(title, amount, category, date):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (title, amount, category, date)
        VALUES (?, ?, ?, ?)
    """, (title, amount, category, date))

    conn.commit()
    conn.close()
    print("Expense added successfully!")


# View expenses

def view_expenses():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()
    return rows


# Update
def update_expense(expense_id, title, amount, category, date):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE expenses
        SET title=?, amount=?, category=?, date=?
        WHERE id=?
    """, (title, amount, category, date, expense_id))

    conn.commit()
    conn.close()
    print("Expense updated")


# Delete
def delete_expense(expense_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))

    conn.commit()
    conn.close()
    print("Expense deleted")