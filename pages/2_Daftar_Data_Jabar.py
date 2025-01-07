import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

with st.container(border=True):
    with st.container(border=True):
        with st.container(border=True):
            st.title('... :green[PLISS] :orange[Nganjang] ...')

            st.subheader(':green[Portal Literasi dan Identifikasi Statistik Sektoral] \
                        dalam rangka :orange[Nganjang Jabar Caang]', divider='rainbow')

st.divider()

with st.container(border=True):
    st.title('DAFTAR DATA JABAR')
    st.success('Berdasarkan Keputusan Gubernur Jawa Barat Nomor: 050/Kep.960-BAPP/2023 tentang \
        Daftar Data Daerah dan Data Prioritas Daerah Tahun 2024-2026')

    data = pd.read_csv('data/daftar-data-jabar.csv')

    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = data['PENGHASIL DATA'].value_counts().reset_index()
        df2_counts.columns = ['PENGHASIL DATA', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['PENGHASIL DATA'], values='count')
        
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        

    opd = data['PENGHASIL DATA'].unique()

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = data[data['PENGHASIL DATA'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
st.divider()
st.caption('Tim PSS @BPS Provinsi Jawa Barat')