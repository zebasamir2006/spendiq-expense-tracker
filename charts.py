import matplotlib.pyplot as plt
import streamlit as st
from analytics import category_wise_expenses, monthly_summary


def category_bar_chart():
    data = category_wise_expenses()

    if not data:
        st.warning("No data")
        return

    categories = [i[0] for i in data]
    amounts = [i[1] for i in data]

    fig, ax = plt.subplots()
    ax.bar(categories, amounts)

    st.pyplot(fig)


def category_pie_chart():
    data = category_wise_expenses()

    if not data:
        st.warning("No data")
        return

    categories = [i[0] for i in data]
    amounts = [i[1] for i in data]

    fig, ax = plt.subplots()
    ax.pie(amounts, labels=categories, autopct="%1.1f%%")

    st.pyplot(fig)


def monthly_line_chart():
    data = monthly_summary()

    if not data:
        st.warning("No data")
        return

    months = [i[0] for i in data]
    amounts = [i[1] for i in data]

    fig, ax = plt.subplots()
    ax.plot(months, amounts, marker="o")

    st.pyplot(fig)