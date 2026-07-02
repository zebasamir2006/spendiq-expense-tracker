from database.db import create_connection


def total_expenses():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    conn.close()
    return total or 0


def category_wise_expenses():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    data = cursor.fetchall()
    conn.close()

    return data


def highest_expense():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses ORDER BY amount DESC LIMIT 1")
    row = cursor.fetchone()

    conn.close()
    return row


def lowest_expense():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses ORDER BY amount ASC LIMIT 1")
    row = cursor.fetchone()

    conn.close()
    return row


def monthly_summary():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT substr(date,1,7), SUM(amount)
        FROM expenses
        GROUP BY substr(date,1,7)
        ORDER BY substr(date,1,7)
    """)

    data = cursor.fetchall()
    conn.close()

    return data