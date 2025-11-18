import streamlit as py
import pandas as pd
import matplotlib.pyplot as plt

st.title("Personal Expense Tracker")

# Initilaize 
if 'expenses' not in st.session_state:
  st.session_state.expenses = pd.Dataframe(columns=['Date','Category','Amount','Description'])

# Create sth
with st.form["expense_form"):
  st.subheader("Add New Expense")
  date = st.date_input("Date")
  category = st.selectbox("Category",["Food","Transport","Entertainment","Bills","Other"]) 
  amount = st.number_input("Amount", min_value=0.0, step=0.01)
  description = st.text_input("Description")

submitted = st.form_submit_button("Add Expense")

# Error handling 
if submitted:
  new_expense = pd.Dataframe({
    'Date': [date],
    'Category': [category],
    'AMount': [amount],
    'Description': [description]
  })
  st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)
  st.success("Expense added successfully!")

if not st.session_state.expenses.empty:
  st.subheader("Your Expenses")
  st.dataframe(st.session_state.expenses)
  
  st.subheader("Summary")
  total_spent = st.session_state.expenses['Amount'].sum()  # Python method
  st.write(f"Total Spent: ${total_spent:.2f}")

# Chart
  category_totals = st.session_state.expenses.groupby('Category')['Amount'].sum()   # group data based on criteria eg. category 

# NOT IN EXAM
  fig, ax = plt.subplot(figsize = (10,6))
  ax.pie(category_totals.values, labels=category_totals.index, autopct='%1.1f%%')
  ax.set_title("Expenses by Category")
  st.pyplot(fig)
  
