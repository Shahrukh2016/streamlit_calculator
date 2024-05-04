import streamlit as st

with st.form("operation", clear_on_submit=True):
    col1, col2 = st.columns(2)
    x = col1.number_input(label="Enter your first number:")
    y = col2.number_input(label="Enter your second number:")
    op = st.text_input(label="Enter your mathematical operator: ")
    status = st.form_submit_button("Calculate")

    if status: 
        result = None
        if op == '+':
            result = x + y
        elif op == '-':
            result = x - y
        elif op == '*':
            result = x * y
        elif op == '/':
            if y != 0:
                result = x / y
            else:
                st.error("Error: Division by zero!")
        else:
            st.error("Error: Invalid operator!")

        if result is not None:
            st.markdown(f"Result: {result}")
