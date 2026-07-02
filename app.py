import tkinter as tk
from ui.dashboard import show_dashboard

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Smart Expense Tracker")
root.geometry("1000x600")
root.config(bg="white")

# ---------------- SIDEBAR ----------------
sidebar = tk.Frame(root, bg="#2ecc71", width=200)
sidebar.pack(side="left", fill="y")

# ---------------- MAIN AREA ----------------
main_area = tk.Frame(root, bg="white")
main_area.pack(side="right", expand=True, fill="both")

# We store main_area so other pages can use it
app_state = {
    "main": main_area
}

# ---------------- NAV FUNCTIONS ----------------
def open_dashboard():
    show_dashboard(app_state)

# ---------------- BUTTONS ----------------
tk.Label(sidebar, text="MENU", bg="#2ecc71", fg="white", font=("Arial", 16, "bold")).pack(pady=20)

tk.Button(
    sidebar,
    text="Dashboard",
    command=open_dashboard,
    bg="white",
    fg="black",
    width=20
).pack(pady=10)

# ---------------- DEFAULT PAGE ----------------
show_dashboard(app_state)

# ---------------- RUN APP ----------------
root.mainloop()