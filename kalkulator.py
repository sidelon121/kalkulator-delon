import streamlit as st
import random
import time

# Judul aplikasi
st.set_page_config(page_title="Game Tebak Angka", page_icon="🎮", layout="centered")
st.title("🎯 Game Tebak Angka by Farhan")

# --- Inisialisasi session state ---
if "angka_rahasia" not in st.session_state:
    st.session_state.angka_rahasia = None
if "percobaan" not in st.session_state:
    st.session_state.percobaan = 0
if "maks_tebakan" not in st.session_state:
    st.session_state.maks_tebakan = 0
if "batas" not in st.session_state:
    st.session_state.batas = 0
if "skor" not in st.session_state:
    st.session_state.skor = 0
if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

# --- Pilih level kesulitan ---
st.sidebar.header("⚙️ Pengaturan Game")
level = st.sidebar.radio("Pilih Level Kesulitan:", ["Mudah", "Sedang", "Sulit"])

# Atur level
if level == "Mudah":
    batas = 10
    maks_tebakan = 5
elif level == "Sedang":
    batas = 50
    maks_tebakan = 7
else:
    batas = 100
    maks_tebakan = 10

# Tombol mulai game
if st.sidebar.button("Mulai Game Baru 🎮"):
    st.session_state.angka_rahasia = random.randint(1, batas)
    st.session_state.percobaan = 0
    st.session_state.maks_tebakan = maks_tebakan
    st.session_state.batas = batas
    st.session_state.skor = 0
    st.success(f"Game dimulai! Tebak angka antara 1 hingga {batas}.")

# Jika game sudah dimulai
if st.session_state.angka_rahasia:
    st.markdown(f"🎲 **Tebak angka antara 1 hingga {st.session_state.batas}**")
    st.markdown(f"💡 Kesempatan tersisa: {st.session_state.maks_tebakan - st.session_state.percobaan}")

    angka_user = st.number_input("Masukkan tebakan kamu:", min_value=1, max_value=st.session_state.batas, step=1)

    if st.button("Tebak Sekarang!"):
        st.session_state.percobaan += 1
        angka_rahasia = st.session_state.angka_rahasia

        if angka_user == angka_rahasia:
            skor_tambahan = (st.session_state.maks_tebakan - st.session_state.percobaan + 1) * 10
            st.session_state.skor += skor_tambahan
            st.success(f"🎉 Benar! Angkanya adalah {angka_rahasia}.")
            st.balloons()
            st.session_state.riwayat.append(
                {"Level": level, "Percobaan": st.session_state.percobaan, "Skor": st.session_state.skor}
            )
            st.session_state.angka_rahasia = None  # reset game

        elif angka_user < angka_rahasia:
            st.warning("📉 Angka kamu terlalu kecil.")
        else:
            st.warning("📈 Angka kamu terlalu besar.")

        # Jika kesempatan habis
        if st.session_state.percobaan >= st.session_state.maks_tebakan and st.session_state.angka_rahasia:
            st.error(f"😢 Kesempatan habis! Angka yang benar adalah {angka_rahasia}.")
            st.session_state.riwayat.append(
                {"Level": level, "Percobaan": st.session_state.percobaan, "Skor": st.session_state.skor}
            )
            st.session_state.angka_rahasia = None

# --- Riwayat Skor ---
if st.session_state.riwayat:
    st.subheader("📜 Riwayat Permainan")
    st.table(st.session_state.riwayat)

# --- Tombol reset semua data ---
if st.sidebar.button("🔄 Reset Semua Data"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.success("Semua data berhasil direset.")
