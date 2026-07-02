import tkinter as tk
from tkinter import messagebox
from database.db import create_connection


def clear(frame):
    for w in frame.winfo_children():
        w.destroy()


def save_expense(amount, category, date, note=""):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO expenses (title, amount, category, date)
        VALUES (?, ?, ?, ?)
    """, (note, amount, category, date))

    conn.commit()
    conn.close()


def show_add_expense(app_state):
    main = app_state["main"]
    clear(main)

    tk.Label(main, text="➕ Add Expense", font=("Arial", 22)).pack()

    amount_entry = tk.Entry(main)
    amount_entry.pack()

    category_entry = tk.Entry(main)
    category_entry.pack()

    date_entry = tk.Entry(main)
    date_entry.pack()

    note_entry = tk.Entry(main)
    note_entry.pack()

    def submit():
        try:
            amount = float(amount_entry.get())
        except:
            messagebox.showerror("Error", "Amount must be number")
            return

        save_expense(amount, category_entry.get(), date_entry.get(), note_entry.get())
        messagebox.showinfo("Success", "Added!")

    tk.Button(main, text="Save", command=submit).pack()