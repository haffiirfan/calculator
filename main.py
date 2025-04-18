import streamlit as st

# Title
st.title("🧮 Mouse-Only Calculator")

# Initialize session state for expression
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Helper function to append characters to the expression
def add_to_expression(value):
    st.session_state.expression += str(value)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)
    except Exception:
        st.session_state.expression = "Error"

# Display the current expression
st.text_input("Expression", value=st.session_state.expression, key="display", disabled=True)

# Layout: Define 5 rows of buttons
for row in [
    ["7", "8", "9", "Clear"],
    ["4", "5", "6", "+"],       # ✅ Plus button added
    ["1", "2", "3", "-"],       # ✅ Minus button added
    ["0", ".", "=", "*"],       # ✅ Multiply button added
    ["/", "%", "//", "()"]      # ✅ Divide button added
]:
    cols = st.columns(4)
    for i, label in enumerate(row):
        if label == "=":
            cols[i].button(label, on_click=evaluate_expression)
        elif label == "Clear":
            cols[i].button(label, on_click=lambda: st.session_state.update({"expression": ""}))
        else:
            cols[i].button(label, on_click=add_to_expression, args=(label,))

