import streamlit as st

def garis():
    st.markdown("<hr style='border:1px solid #bbb;'>", unsafe_allow_html=True)

def keluar():
    garis()
    st.success("Terima kasih sudah menggunakan kalkulator sederhana ini.\nSampai jumpa lagi!")
    st.stop()

def app_penjumlahan():
    garis()
    st.markdown("<h4 style='text-align:center;'>OPERASI PENJUMLAHAN</h4>", unsafe_allow_html=True)
    garis()
    angka1 = st.number_input("Masukkan angka pertama", key="penjumlahan1")
    angka2 = st.number_input("Masukkan angka kedua", key="penjumlahan2")
    if st.button("Hitung Penjumlahan"):
        hasil = angka1 + angka2
        st.success(f"Hasil dari {angka1} ditambah {angka2} adalah {hasil}")

def app_pengurangan():
    garis()
    st.markdown("<h4 style='text-align:center;'>OPERASI PENGURANGAN</h4>", unsafe_allow_html=True)
    garis()
    angka1 = st.number_input("Masukkan angka pertama", key="pengurangan1")
    angka2 = st.number_input("Masukkan angka kedua", key="pengurangan2")
    if st.button("Hitung Pengurangan"):
        hasil = angka1 - angka2
        st.success(f"Hasil dari {angka1} dikurangi {angka2} adalah {hasil}")

def app_perkalian():
    garis()
    st.markdown("<h4 style='text-align:center;'>OPERASI PERKALIAN</h4>", unsafe_allow_html=True)
    garis()
    angka1 = st.number_input("Masukkan angka pertama", key="perkalian1")
    angka2 = st.number_input("Masukkan angka kedua", key="perkalian2")
    if st.button("Hitung Perkalian"):
        hasil = angka1 * angka2
        st.success(f"Hasil dari {angka1} dikali {angka2} adalah {hasil}")

def app_pembagian():
    garis()
    st.markdown("<h4 style='text-align:center;'>OPERASI PEMBAGIAN</h4>", unsafe_allow_html=True)
    garis()
    angka1 = st.number_input("Masukkan angka pertama", key="pembagian1")
    angka2 = st.number_input("Masukkan angka kedua", key="pembagian2")
    if st.button("Hitung Pembagian"):
        if angka2 == 0:
            st.error("Tidak bisa membagi dengan nol.")
        else:
            hasil = angka1 / angka2
            st.success(f"Hasil dari {angka1} dibagi {angka2} adalah {hasil}")

def app_pangkat():
    garis()
    st.markdown("<h4 style='text-align:center;'>OPERASI PANGKAT</h4>", unsafe_allow_html=True)
    garis()
    angka1 = st.number_input("Masukkan angka", key="pangkat1")
    angka2 = st.number_input("Masukkan pangkat", key="pangkat2")
    if st.button("Hitung Pangkat"):
        hasil = angka1 ** angka2
        st.success(f"Hasil dari {angka1} pangkat {angka2} adalah {hasil}")

def app_persentase():
    garis()
    st.markdown("<h4 style='text-align:center;'>OPERASI PERSENTASE</h4>", unsafe_allow_html=True)
    garis()
    bagian = st.number_input("Masukkan nilai (bagian)", key="persentase1")
    total = st.number_input("Masukkan total", key="persentase2")
    if st.button("Hitung Persentase"):
        if total == 0:
            st.error("Total nilai tidak boleh nol.")
        else:
            hasil = (bagian / total) * 100
            st.success(f"{bagian} dari {total} adalah {hasil}%")

def app_menu():
    st.markdown("<h2 style='text-align:center;'>KALKULATOR SEDERHANA DELON</h2>", unsafe_allow_html=True)
    garis()
    st.markdown("""
    <div style='text-align:center;'>
    <b>Pilih operasi:</b><br>
    <span style='display:inline-block;width:45%;text-align:left;'>+  : Penjumlahan</span>
    <span style='display:inline-block;width:45%;text-align:right;'>x  : Perkalian</span><br>
    <span style='display:inline-block;width:45%;text-align:left;'>-  : Pengurangan</span>
    <span style='display:inline-block;width:45%;text-align:right;'>/  : Pembagian</span><br>
    <span style='display:inline-block;width:45%;text-align:left;'>** : Pangkat</span>
    <span style='display:inline-block;width:45%;text-align:right;'>%  : Persentase</span><br>
    <span style='display:inline-block;width:100%;text-align:center;'>#  : Keluar</span>
    </div>
    """, unsafe_allow_html=True)
    garis()
    operasi = st.selectbox(
        "Masukkan pilihan:",
        ("+", "-", "x", "/", "**", "%", "#"),
        format_func=lambda x: {
            "+": "Penjumlahan (+)",
            "-": "Pengurangan (-)",
            "x": "Perkalian (x)",
            "/": "Pembagian (/)",
            "**": "Pangkat (**)",
            "%": "Persentase (%)",
            "#": "Keluar"
        }[x]
    )

    if operasi == "+":
        app_penjumlahan()
    elif operasi == "-":
        app_pengurangan()
    elif operasi == "x":
        app_perkalian()
    elif operasi == "/":
        app_pembagian()
    elif operasi == "**":
        app_pangkat()
    elif operasi == "%":
        app_persentase()
    elif operasi == "#":
        keluar()

app_menu()