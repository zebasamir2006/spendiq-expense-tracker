import streamlit as st
import pandas as pd

from expense import add_expense, view_expenses
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


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Expense Tracker",
    layout="wide"
)

st.title("💰 SpendIQ")
st.subheader("Smart Expense Tracker • Finance Dashboard")
st.caption("Track your spending, analyze trends, and manage money smartly.")


# ---------------- SIDEBAR MENU ----------------
menu = ["Add Expense", "View Expenses", "Analytics", "Charts", "Export CSV"]
choice = st.sidebar.selectbox("Menu", menu)


# ================= ADD EXPENSE =================
if choice == "Add Expense":
    st.subheader("➕ Add Expense")

    col1, col2 = st.columns(2)

    with col1:
        title = st.text_input("Title")

    with col2:
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")

    col3, col4 = st.columns(2)

    with col3:
        category = st.text_input("Category")

    with col4:
        date = st.text_input("Date (YYYY-MM-DD)")

    if st.button("Add Expense"):
        if title and category and date:
            add_expense(title, amount, category, date)
            st.success("✅ Expense Added Successfully!")
        else:
            st.error("❌ Please fill all fields")


# ================= VIEW EXPENSES =================
elif choice == "View Expenses":
    st.subheader("📋 All Expenses")

    data = view_expenses()

    if data and len(data) > 0:
        df = pd.DataFrame(
            data,
            columns=["ID", "Title", "Amount", "Category", "Date"]
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No expenses found in database")


# ================= ANALYTICS (FIXED + BEAUTIFUL) =================
elif choice == "Analytics":
    st.subheader("📊 Analytics Dashboard")

    # ---------- FIXED METRICS ----------
    highest = highest_expense()
    lowest = lowest_expense()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💰 Total Expenses", total_expenses())

    with col2:
        if highest:
            st.metric("🏆 Highest Expense", highest[2])
        else:
            st.metric("🏆 Highest Expense", 0)

    with col3:
        if lowest:
            st.metric("📉 Lowest Expense", lowest[2])
        else:
            st.metric("📉 Lowest Expense", 0)

    st.divider()

    # ---------- CATEGORY ----------
    st.markdown("## 📂 Category Breakdown")

    category_data = category_wise_expenses()

    if category_data:
        df_cat = pd.DataFrame(category_data, columns=["Category", "Total Amount"])
        st.dataframe(df_cat, use_container_width=True)
    else:
        st.warning("No category data found")

    st.divider()

    # ---------- MONTHLY ----------
    st.markdown("## 📅 Monthly Summary")

    monthly_data = monthly_summary()

    if monthly_data:
        df_month = pd.DataFrame(monthly_data, columns=["Month", "Total Amount"])
        st.dataframe(df_month, use_container_width=True)
    else:
        st.warning("No monthly data found")


# ================= CHARTS =================
elif choice == "Charts":
    st.subheader("📈 Charts Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📊 Bar Chart"):
            category_bar_chart()

    with col2:
        if st.button("🥧 Pie Chart"):
            category_pie_chart()

    with col3:
        if st.button("📉 Line Chart"):
            monthly_line_chart()


# ================= EXPORT =================
elif choice == "Export CSV":
    st.subheader("⬇ Export Data")

    if st.button("Download CSV"):
        export_to_csv()
        st.success("✅ Export completed successfully!")