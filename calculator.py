import streamlit as st

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error: Division by zero"
        result /= num
    return result

def calculator():
    st.title("Calculator")
    action = st.radio("Select an operation", ('Addition', 'Subtraction', 'Multiplication', 'Division'))

    num_count = st.number_input("How many numbers do you want to calculate with?", 2, 4, 2)

    numbers = []
    for i in range(num_count):
        num = st.number_input(f"Enter number {i + 1}:")
        numbers.append(num)

    if st.button("Calculate"):
        if action == 'Addition':
            result = add(numbers)
        elif action == 'Subtraction':
            result = subtract(numbers)
        elif action == 'Multiplication':
            result = multiply(numbers)
        else:
            result = divide(numbers)

        st.write(f"Result: {result}")

    if st.button("Clear"):
        st.text_input("Result", value="")

if __name__ == '__main__':
    calculator()
