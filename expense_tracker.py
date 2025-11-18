import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Personal Expense Tracker")

# Initialize
if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])

# Create form
with st.form("expense_form"):
    st.subheader("Add New Expense")
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Other"])
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    description = st.text_input("Description")

    submitted = st.form_submit_button("Add Expense")

    # Error handling
    if submitted:
        new_expense = pd.DataFrame({
            'Date': [date],
            'Category': [category],
            'Amount': [amount],     # corrected key name
            'Description': [description]
        })
        st.session_state.expenses = pd.concat(
            [st.session_state.expenses, new_expense],
            ignore_index=True
        )
        st.success("Expense added successfully!")

# Display data
if not st.session_state.expenses.empty:
    st.subheader("Your Expenses")
    st.dataframe(st.session_state.expenses)

    st.subheader("Summary")
    total_spent = st.session_state.expenses['Amount'].sum()
    st.write(f"Total Spent: ${total_spent:.2f}")

    # Chart
    category_totals = st.session_state.expenses.groupby('Category')['Amount'].sum
