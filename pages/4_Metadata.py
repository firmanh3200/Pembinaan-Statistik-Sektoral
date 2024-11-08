import streamlit as st

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')

st.subheader('METADATA STATISTIK')
st.success('Berdasarkan Sistem Rujukan Statistik')

st.link_button("Metadata Statistik Dasar", url="https://sirusa.bps.go.id/sirusa/index.php/dasar/index")

st.link_button("Metadata Statistik Sektoral", url="https://sirusa.bps.go.id/sirusa/index.php/sektoral/index")

st.link_button("Metadata Statistik Khusus", url="https://sirusa.bps.go.id/sirusa/index.php/khusus/index")

st.link_button("Glosarium", url="https://sirusa.bps.go.id/sirusa/index.php/istilah/index")

st.link_button("Tata Cara Pelaksanaan Survei", url="https://sirusa.bps.go.id/sirusa/index.php/solusi/page?view=konsep&tab=1")