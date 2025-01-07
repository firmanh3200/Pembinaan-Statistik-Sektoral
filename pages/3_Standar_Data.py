import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout='wide')

with st.container(border=True):
    with st.container(border=True):
        with st.container(border=True):
            st.title('... :green[PLISS] :orange[Nganjang] ...')

            st.subheader(':green[Portal Literasi dan Identifikasi Statistik Sektoral] \
                        dalam rangka :orange[Nganjang Jabar Caang]', divider='rainbow')

st.divider()

with st.container(border=True):

    st.subheader('STANDAR DATA STATISTIK NASIONAL')
    st.success('Berdasarkan Keputusan Kepala Badan Pusat Statistik Nomor 850 Tahun 2023')
    st.caption('Lihat SDDS: https://indah.bps.go.id/standar-data-statistik-nasional')

    # Fungsi untuk mendapatkan data dari API dengan paginasi
    def get_all_data(base_url):
        all_data = []
        page = 0
        while True:
            url = f"{base_url}&page={page}"
            response = requests.get(url)
            data = response.json()
            if not data['content']:
                break
            all_data.extend(data['content'])
            page += 1
        return all_data

    # URL dasar API
    base_url = 'https://indah-api.bps.go.id/api/standar-data-statistik-nasional-2023?tipe=1&size=100'

    # Mendapatkan semua data
    all_data = get_all_data(base_url)

    # Mengonversi data menjadi DataFrame
    df = pd.DataFrame(all_data)

    st.dataframe(df, hide_index=True, use_container_width=True)
    
st.divider()
st.caption('Tim PSS @BPS Provinsi Jawa Barat')