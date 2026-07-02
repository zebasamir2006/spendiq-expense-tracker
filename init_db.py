import sqlite3

def create_connection():
    conn = sqlite3.connect("database/expense_tracker.db")
    return conn


def create_table():
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        amount REAL,
        category TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    print("Table created successfully")