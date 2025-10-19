import streamlit as st
import math

# ========================
# Fungsi Perhitungan
# ========================
def hitung_penjumlahan(a, b):
    return a + b

def hitung_pengurangan(a, b):
    return a - b

def hitung_perkalian(a, b):
    return a * b

def hitung_pembagian(a, b):
    if b == 0:
        return "Tidak bisa membagi dengan nol."
    return a / b

def hitung_pangkat(a, b):
    return a ** b

def hitung_persentase(nilai, total):
    if total == 0:
        return "Total tidak boleh nol."
    return (nilai / total) * 100

def hitung_akar_kuadrat(a):
    if a < 0:
        return "Tidak bisa menghitung akar kuadrat dari angka negatif."
    return math.sqrt(a)

def hitung_akar_pangkat_n(a, n):
    if n == 0:
        return "Nilai pangkat akar tidak boleh nol."
    if a < 0 and n % 2 == 0:
        return "Tidak bisa menghitung akar genap dari angka negatif."
    return a ** (1 / n)

def hitung_modulus(a, b):
    if b == 0:
        return "Tidak bisa melakukan modulus dengan nol."
    return a % b

def hitung_logaritma(a):
    if a <= 0:
        return "Logaritma hanya bisa untuk angka > 0."
    return math.log10(a)

def hitung_trigonometri(fungsi, sudut):
    rad = math.radians(sudut)
    if fungsi == "sin":
        return math.sin(rad)
    elif fungsi == "cos":
        return math.cos(rad)
    elif fungsi == "tan":
        return math.tan(rad)

# ========================
# Aplikasi Streamlit
# ========================
st.title("Kalkulator Lengkap")
st.write("Pilih operasi matematika di bawah ini dan masukkan angka yang diperlukan.")

# Pilih operasi
operasi = st.selectbox(
    "Pilih operasi:",
    [
        "Penjumlahan",
        "Pengurangan",
        "Perkalian",
        "Pembagian",
        "Pangkat",
        "Persentase",
        "Akar Kuadrat",
        "Akar Pangkat-n",
        "Modulus (Sisa Bagi)",
        "Logaritma (Basis 10)",
        "Trigonometri (sin, cos, tan)"
    ]
)

hasil = None

# Input berdasarkan operasi
if operasi in ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian", "Modulus (Sisa Bagi)"]:
    a = st.number_input("Masukkan angka pertama:", value=0.0, step=0.01)
    b = st.number_input("Masukkan angka kedua:", value=0.0, step=0.01)
    if st.button("Hitung"):
        if operasi == "Penjumlahan":
            hasil = hitung_penjumlahan(a, b)
        elif operasi == "Pengurangan":
            hasil = hitung_pengurangan(a, b)
        elif operasi == "Perkalian":
            hasil = hitung_perkalian(a, b)
        elif operasi == "Pembagian":
            hasil = hitung_pembagian(a, b)
        elif operasi == "Modulus (Sisa Bagi)":
            hasil = hitung_modulus(a, b)

elif operasi == "Pangkat":
    a = st.number_input("Masukkan angka (basis):", value=0.0, step=0.01)
    b = st.number_input("Masukkan pangkat:", value=0.0, step=0.01)
    if st.button("Hitung"):
        hasil = hitung_pangkat(a, b)

elif operasi == "Persentase":
    nilai = st.number_input("Masukkan nilai:", value=0.0, step=0.01)
    total = st.number_input("Masukkan total:", value=0.0, step=0.01)
    if st.button("Hitung"):
        hasil = hitung_persentase(nilai, total)

elif operasi == "Akar Kuadrat":
    a = st.number_input("Masukkan angka:", value=0.0, step=0.01)
    if st.button("Hitung"):
        hasil = hitung_akar_kuadrat(a)

elif operasi == "Akar Pangkat-n":
    a = st.number_input("Masukkan angka:", value=0.0, step=0.01)
    n = st.number_input("Masukkan nilai pangkat akar (contoh: 3 untuk akar kubik):", value=1.0, step=0.01)
    if st.button("Hitung"):
        hasil = hitung_akar_pangkat_n(a, n)

elif operasi == "Logaritma (Basis 10)":
    a = st.number_input("Masukkan angka:", value=1.0, step=0.01)
    if st.button("Hitung"):
        hasil = hitung_logaritma(a)

elif operasi == "Trigonometri (sin, cos, tan)":
    fungsi = st.selectbox("Pilih fungsi:", ["sin", "cos", "tan"])
    sudut = st.number_input("Masukkan sudut dalam derajat:", value=0.0, step=0.01)
    if st.button("Hitung"):
        hasil = hitung_trigonometri(fungsi, sudut)

# Tampilkan hasil
if hasil is not None:
    if isinstance(hasil, str):
        st.error(hasil)
    else:
        st.success(f"Hasil: {hasil:.4f}" if isinstance(hasil, float) else f"Hasil: {hasil}")

st.write("---")
st.write("Terima kasih sudah menggunakan kalkulator ini!")
