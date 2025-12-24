#command ini sudah sukses di akses di lokal host dan network


import streamlit as st

st.title("Innotech Libry Institute Smart Training Assistant")
st.markdown("Asisten Peserta Pelatihan")
st.markdown("Tutor Materi INLISLite Ver 3.2")
st.markdown("FAQ Lembaga dan Pelatihan")
st.markdown("Pendamping Belajar Mandiri Kepustakawanan")

user_name = st.text_input("Masukan Nama Anda")
user_age = st.slider("Masukan Usia Anda")
submit_button = st.button("submit")

if submit_button:
    st.markdown(f"Selamat Datang ke Perpustakaan Innotech Libry Institute {user_name}!")
    st.markdown("Selamat Menjelajah dunia perpustakaan yang Menyenangkan")
