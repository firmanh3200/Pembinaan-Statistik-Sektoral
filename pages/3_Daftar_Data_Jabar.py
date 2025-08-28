import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(layout='wide')

with st.container(border=True):
    with st.container(border=True):
        with st.container(border=True):
            

            st.subheader(':green[Portal Literasi dan Identifikasi Statistik Sektoral] \
                        dalam rangka :orange[Nganjang Jabar Caang]', divider='rainbow')

st.divider()

with st.container(border=True):
    st.title('DAFTAR DATA JABAR')
    st.success('Berdasarkan Keputusan Gubernur Jawa Barat Nomor: 050/Kep.960-BAPP/2023 tentang \
        Daftar Data Daerah dan Data Prioritas Daerah Tahun 2024-2026')

    data = pd.read_csv('https://raw.githubusercontent.com/firmanh3200/Pembinaan-Statistik-Sektoral/refs/heads/main/data/daftar-data-jabar.csv')

    kol1, kol2 = st.columns([2,4])
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = data['PENGHASIL DATA'].value_counts().reset_index()
        df2_counts.columns = ['PENGHASIL DATA', 'count']
        df2_counts = df2_counts.sort_values(by='PENGHASIL DATA')

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['PENGHASIL DATA'], values='count')
        
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True, hide_index=True)
        

    opd = data['PENGHASIL DATA'].unique()

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = data[data['PENGHASIL DATA'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
st.divider()

with st.expander('Indikator Kinerja Daerah'):
    st.subheader('Indikator Kinerja Daerah Provinsi Jawa Barat')
    st.warning('Peraturan Gubernur Jawa Barat Nomor 25 Tahun 2023 tentang \
        Rencana Pembangunan Daerah Provinsi Jawa Barat 2024-2026')
    
    ikd = pd.read_excel('data/ikd jabar.xlsx')
    
    df = pd.DataFrame(ikd)
    df = df[['INDIKATOR KINERJA DAERAH', 'SATUAN', 'BIDANG URUSAN', 'PERANGKAT DAERAH']]
    df = df.sort_values(by='PERANGKAT DAERAH')
    opd = df['PERANGKAT DAERAH']. unique()
    
    terpilih = st.selectbox('Filter Perangkat Daerah', opd)
    
    if terpilih:
        df3 = df[df['PERANGKAT DAERAH'] == terpilih]
        df4 = df3.sort_values(by='INDIKATOR KINERJA DAERAH')
        
        st.dataframe(df4, hide_index=True, use_container_width=True)

with st.expander('Data SIPD'):
    st.subheader('Data Statistik Sektoral Daerah di SIPD')
    st.warning('Sumber: https://sipd.go.id/ewalidata/54050dab11e0f218cf632ec8478dbc71755a65e7/?m=public_dssd_tabel')
    
    # SIPD Jabar
    # url2 = 'https://sipd.go.id/ewalidata/54050dab11e0f218cf632ec8478dbc71755a65e7/?m=public_dssd_tabel&f=ajax_get_indikator&m=public_dssd_tabel&kodelokasi=3200&tahun_awal=2017&tahun_akhir=2025&satuan=&terisi=1&draw=2&start=0&length=10000&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1736296738070'

    # response2 = requests.get(url2)

    # data2 = response2.json()

    # df2 = pd.DataFrame(data2['data'])
    # df2 = df2.sort_values(by='kodeindikator')
    # del df2['depth']
    # del df2['path']
    # del df2['subkegiatan']
    
    # # Mengambil kata pertama dari kolom 'satuan'
    # df2['satuan'] = df2['satuan'].str.split('<').str[0]
    # df2['urai'] = df2['urai'].str.split('&').str[0]
    
    # st.dataframe(df2, use_container_width=True, hide_index=True)

    
st.divider()
st.caption('Tim PSS @BPS Provinsi Jawa Barat')