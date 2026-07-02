import tkinter as tk

# ---------------- CLEAR SCREEN FUNCTION ----------------
def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# ---------------- DASHBOARD PAGE ----------------
def show_dashboard(app_state):
    main = app_state["main"]
    clear(main)

    # Title
    tk.Label(
        main,
        text="📊 Dashboard",
        font=("Arial", 26, "bold"),
        bg="white"
    ).pack(pady=20)

    # ---------------- CARDS AREA ----------------
    cards_frame = tk.Frame(main, bg="white")
    cards_frame.pack(pady=20)

    # Card 1 - Total Income
    card1 = tk.Frame(cards_frame, bg="#e8f8f5", width=200, height=100)
    card1.grid(row=0, column=0, padx=15)

    tk.Label(card1, text="Total Income", font=("Arial", 12, "bold"), bg="#e8f8f5").pack(pady=10)
    tk.Label(card1, text="₹0", font=("Arial", 16), bg="#e8f8f5").pack()

    # Card 2 - Total Expense
    card2 = tk.Frame(cards_frame, bg="#fdecea", width=200, height=100)
    card2.grid(row=0, column=1, padx=15)

    tk.Label(card2, text="Total Expense", font=("Arial", 12, "bold"), bg="#fdecea").pack(pady=10)
    tk.Label(card2, text="₹0", font=("Arial", 16), bg="#fdecea").pack()

    # Card 3 - Balance
    card3 = tk.Frame(cards_frame, bg="#eaf2ff", width=200, height=100)
    card3.grid(row=0, column=2, padx=15)

    tk.Label(card3, text="Balance", font=("Arial", 12, "bold"), bg="#eaf2ff").pack(pady=10)
    tk.Label(card3, text="₹0", font=("Arial", 16), bg="#eaf2ff").pack()