import streamlit as st
import numpy as np

# App Title
st.title("🧮 Multi-Number Calculator")

st.markdown("Enter numbers separated by commas (e.g., `2, 5, 10`)")

# User input
input_str = st.text_input("Enter numbers:")

# Choose operation
operation = st.selectbox("Choose an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Button to calculate
if st.button("Calculate"):
    try:
        # Parse input into list of floats
        numbers = [float(num.strip()) for num in input_str.split(",") if num.strip()]

        if not numbers:
            st.warning("Please enter at least one number.")
        else:
            result = None
            if operation == "Addition":
                result = sum(numbers)
            elif operation == "Subtraction":
                result = numbers[0] - sum(numbers[1:]) if len(numbers) > 1 else numbers[0]
            elif operation == "Multiplication":
                result = np.prod(numbers)
            elif operation == "Division":
                try:
                    result = numbers[0]
                    for num in numbers[1:]:
                        result /= num
                except ZeroDivisionError:
                    st.error("Division by zero is not allowed.")
                    result = None

            if result is not None:
                st.success(f"Result: {result}")
    except ValueError:
        st.error("Please enter valid numbers separated by commas.")
print("panileda ra enduku ra mee amma baabulu neeku feesulu katti school ki pampishte nuvvemo maths nerchukovaa ra pandi pirraloda dobbey poyi normal ga calculate chesuko po ra bafoon")