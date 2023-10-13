import streamlit as st

def add(n, m):
    return n + m

def sub(n, m):
    return n - m

def mul(n, m):
    return n * m

def div(n, m):
    if m == 0:
        return "Error: Division by zero"
    return n / m

def calculator():
    st.title("Calculator")
    action = st.radio("Select an operation", ('Addition', 'Subtraction', 'Multiplication', 'Division'))

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    if st.button("Calculate"):
        if action == 'Addition':
            result = add(num1, num2)
        elif action == 'Subtraction':
            result = sub(num1, num2)
        elif action == 'Multiplication':
            result = mul(num1, num2)
        else:
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = div(num1, num2)

        st.write(f"Result: {result}")

    if st.button("Clear"):
        st.text_input("Result", value="")

if __name__ == '__main__':
    calculator()