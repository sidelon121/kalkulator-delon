import streamlit as st
import math

# ========================
# Konfigurasi Tampilan
# ========================
st.set_page_config(page_title="Kalkulator Lengkap", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #f5f5f5;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #1e1e1e;
        color: white;
        border-radius: 12px;
        padding: 18px 25px;
        font-size: 18px;
        margin: 4px;
        transition: 0.2s;
        border: 1px solid #333;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #333;
        transform: scale(1.05);
    }
    .result-box {
        background-color: #1a1a1a;
        border-radius: 10px;
        padding: 20px;
        text-align: right;
        font-size: 24px;
        color: #00FFAA;
        border: 1px solid #333;
    }
    </style>
""", unsafe_allow_html=True)

# ========================
# Header
# ========================
st.title("🧮 Kalkulator Lengkap")
st.caption("Mode: Dark | Tampilan: Horizontal Mobile Style")

# ========================
# Input Angka
# ========================
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Angka 1", step=1.0, format="%.2f", key="a")
with col2:
    b = st.number_input("Angka 2", step=1.0, format="%.2f", key="b")

# ========================
# Tombol Operasi
# ========================
st.markdown("### Pilih Operasi:")
row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)

hasil = None

# Baris 1
if row1[0].button("+"):
    hasil = int(a) + int(b)
if row1[1].button("-"):
    hasil = int(a) - int(b)
if row1[2].button("×"):
    hasil = int(a) * int(b)
if row1[3].button("÷"):
    if b == 0:
        hasil = "Error: Tidak bisa bagi 0"
    else:
        hasil = round(int(a) / int(b), 4)

# Baris 2
if row2[0].button("xʸ"):
    hasil = int(a) ** int(b)
if row2[1].button("√x"):
    if a < 0:
        hasil = "Error: Akar negatif"
    else:
        hasil = round(math.sqrt(a), 4)
if row2[2].button("xⁿ√"):
    if b == 0:
        hasil = "Error: Pangkat nol"
    else:
        hasil = round(a ** (1 / b), 4)
if row2[3].button("log₁₀"):
    if a <= 0:
        hasil = "Error: log hanya untuk x>0"
    else:
        hasil = round(math.log10(a), 4)

# Baris 3 (Trigonometri)
if row3[0].button("sin"):
    hasil = round(math.sin(math.radians(a)), 6)
if row3[1].button("cos"):
    hasil = round(math.cos(math.radians(a)), 6)
if row3[2].button("tan"):
    hasil = round(math.tan(math.radians(a)), 6)
if row3[3].button("%"):
    if b == 0:
        hasil = "Error: total nol"
    else:
        hasil = round((a / b) * 100, 2)

# ========================
# Hasil
# ========================
if hasil is not None:
    st.markdown("---")
    st.markdown(f"<div class='result-box'>Hasil: {hasil}</div>", unsafe_allow_html=True)
