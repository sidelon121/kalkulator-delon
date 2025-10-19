import streamlit as st
import math

# Inisialisasi session state
if 'expression' not in st.session_state:
    st.session_state.expression = ""
if 'history' not in st.session_state:
    st.session_state.history = []

def update_expression(char):
    if char in ['+', '-', '*', '/', '^', '%']:
        if st.session_state.expression and not st.session_state.expression[-1] in ['+', '-', '*', '/', '^', '%']:
            st.session_state.expression += char
    elif char == '←':
        st.session_state.expression = st.session_state.expression[:-1]
    elif char == 'C':
        st.session_state.expression = ""
    elif char == '=':
        calculate()
    elif char == '√':
        calculate_sqrt()
    elif char in ['sin', 'cos', 'tan', 'log']:
        calculate_trig_log(char)
    else:
        st.session_state.expression += char

def calculate():
    try:
        if st.session_state.expression and '=' not in st.session_state.expression:
            # Parse ekspresi sederhana (misal: 5+3)
            parts = st.session_state.expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('^', ' ** ').replace('%', ' % ').split()
            if len(parts) == 3:
                a, op, b = float(parts[0]), parts[1], float(parts[2])
                if op == '+':
                    result = a + b
                elif op == '-':
                    result = a - b
                elif op == '*':
                    result = a * b
                elif op == '/':
                    if b == 0:
                        raise ZeroDivisionError
                    result = a / b
                elif op == '**':
                    result = a ** b
                elif op == '%':
                    result = (a / b) * 100
                op_str = f"{st.session_state.expression} = {result}"
                st.session_state.history.append(op_str)
                st.session_state.expression = str(result)
            else:
                st.error("Ekspresi tidak valid.")
    except ZeroDivisionError:
        st.error("Tidak bisa membagi dengan nol.")
    except Exception as e:
        st.error(f"Error: {str(e)}")

def calculate_sqrt():
    try:
        num = float(st.session_state.expression)
        if num < 0:
            raise ValueError("Akar kuadrat dari angka negatif tidak valid.")
        result = math.sqrt(num)
        op_str = f"√{st.session_state.expression} = {result}"
        st.session_state.history.append(op_str)
        st.session_state.expression = str(result)
    except ValueError as e:
        st.error(str(e))

def calculate_trig_log(func):
    try:
        num = float(st.session_state.expression)
        if func == 'sin':
            result = math.sin(math.radians(num))
            op_str = f"sin({st.session_state.expression}°) = {result}"
        elif func == 'cos':
            result = math.cos(math.radians(num))
            op_str = f"cos({st.session_state.expression}°) = {result}"
        elif func == 'tan':
            result = math.tan(math.radians(num))
            op_str = f"tan({st.session_state.expression}°) = {result}"
        elif func == 'log':
            if num <= 0:
                raise ValueError("Logaritma hanya untuk angka > 0.")
            result = math.log10(num)
            op_str = f"log10({st.session_state.expression}) = {result}"
        st.session_state.history.append(op_str)
        st.session_state.expression = str(result)
    except ValueError as e:
        st.error(str(e))

# UI Streamlit
st.title("Kalkulator Mobile Web")

# Display
st.text_input("Display", value=st.session_state.expression, key="display", disabled=True)

# Tombol-tombol dalam grid
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("7"): update_expression("7")
    if st.button("4"): update_expression("4")
    if st.button("1"): update_expression("1")
    if st.button("0"): update_expression("0")
    if st.button("C"): update_expression("C")
    if st.button("sin"): update_expression("sin")

with col2:
    if st.button("8"): update_expression("8")
    if st.button("5"): update_expression("5")
    if st.button("2"): update_expression("2")
    if st.button("."): update_expression(".")
    if st.button("←"): update_expression("←")
    if st.button("cos"): update_expression("cos")

with col3:
    if st.button("9"): update_expression("9")
    if st.button("6"): update_expression("6")
    if st.button("3"): update_expression("3")
    if st.button("="): update_expression("=")
    if st.button("√"): update_expression("√")
    if st.button("tan"): update_expression("tan")

with col4:
    if st.button("/"): update_expression("/")
    if st.button("*"): update_expression("*")
    if st.button("-"): update_expression("-")
    if st.button("+"): update_expression("+")
    if st.button("^"): update_expression("^")
    if st.button("log"): update_expression("log")

# Riwayat
st.subheader("Riwayat Perhitungan")
if st.session_state.history:
    for item in st.session_state.history[-10:]:  # Tampilkan 10 terakhir
        st.write(item)
else:
    st.write("Belum ada riwayat.")
