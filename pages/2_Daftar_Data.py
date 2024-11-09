import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')

#st.header(':blue[Perpres No. 39 Tahun 2019]', divider='green')

st.subheader('DAFTAR DATA STATISTIK SEKTORAL')

wilayah = ['Jawa Barat', 'Bogor', 'Sukabumi', 'Cianjur', 'Bandung', 'Garut', 'Tasikmalaya', 'Ciamis',
           'Kuningan', 'Cirebon', 'Majalengka', 'Sumedang', 'Indramayu', 'Subang', 'Purwakarta',
           'Karawang', 'Bekasi', 'Bandung Barat', 'Pangandaran', 'Kota Bogor', 'Kota Sukabumi',
           'Kota Bandung', 'Kota Cirebon', 'Kota Bekasi', 'Kota Depok', 'Kota Cimahi',
           'Kota Tasikmalaya', 'Kota Banjar']

st.success('Kondisi Real Time Open Data Jabar')

wilayah_terpilih = st.selectbox("Pilih Wilayah", wilayah)

# 3200
if wilayah_terpilih == 'Jawa Barat':
    # URL yang diberikan
    url1 = "https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=%5B%22mdate%3Adesc%22%5D&limit=5000&skip=0&where=%5B%22dataset_class_id%3D3%22%2C%5B%22regional_id%3D1%22%5D%5D"
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=1"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('PUSAT', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3201
if wilayah_terpilih == 'Bogor':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=8"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3202
if wilayah_terpilih == 'Sukabumi':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=9"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3203
if wilayah_terpilih == 'Cianjur':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=10"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3204
if wilayah_terpilih == 'Bandung':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=17"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3205
if wilayah_terpilih == 'Garut':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=20"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3206
if wilayah_terpilih == 'Tasikmalaya':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=21"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3207
if wilayah_terpilih == 'Ciamis':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=22"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3208
if wilayah_terpilih == 'Kuningan':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=23"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3209
if wilayah_terpilih == 'Cirebon':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=24"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3210
if wilayah_terpilih == 'Majalengka':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=25"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3211
if wilayah_terpilih == 'Sumedang':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=26"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3212
if wilayah_terpilih == 'Indramayu':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=27"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3213
if wilayah_terpilih == 'Subang':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=28"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3214
if wilayah_terpilih == 'Purwakarta':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=29"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3215
if wilayah_terpilih == 'Karawang':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=30"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3216
if wilayah_terpilih == 'Bekasi':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=31"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3217
if wilayah_terpilih == 'Bandung Barat':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=32"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3218
if wilayah_terpilih == 'Pangandaran':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=6"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3271
if wilayah_terpilih == 'Kota Bogor':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=7"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3272
if wilayah_terpilih == 'Kota Sukabumi':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=11"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3273
if wilayah_terpilih == 'Kota Bandung':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=12"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3274
if wilayah_terpilih == 'Kota Cirebon':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=13"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3275
if wilayah_terpilih == 'Kota Bekasi':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=14"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3276
if wilayah_terpilih == 'Kota Depok':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=15"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3277
if wilayah_terpilih == 'Kota Cimahi':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=16"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3278
if wilayah_terpilih == 'Kota Tasikmalaya':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=18"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')

    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
# 3279
if wilayah_terpilih == 'Kota Banjar':
    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=19"]]'

    # Mengambil data dari URL
    response = requests.get(url2)
    data = response.json()

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(data['data'])

    kolom_dipakai = ['nama_skpd', 'name']

    df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
    
    st.subheader(f'Jumlah Data per Produsen Data di Pemda {wilayah_terpilih}')
    kol1, kol2 = st.columns(2)
    with kol1:
        # Menghitung jumlah kemunculan setiap nama_skpd
        df2_counts = df2['nama_skpd'].value_counts().reset_index()
        df2_counts.columns = ['nama_skpd', 'count']

        # Membuat chart
        fig = px.sunburst(df2_counts, path=['nama_skpd'], values='count')
        # Menambahkan nilai count ke dalam label
        fig.update_traces(textinfo='label+value')
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)
    with kol2:
        with st.container(border=True):
            st.dataframe(df2_counts, use_container_width=True)
        
    df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

    opd = df2['nama_skpd'].unique()

    df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

    st.subheader("", divider='rainbow')
    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
st.subheader("", divider='green')
with st.expander('BAHAN PEMBAHASAN FORUM SATU DATA:'):
    st.warning('Data-data tersebut dihasilkan dari kegiatan apa (MS-Keg)?')
    st.info('Apakah kegiatan tersebut sudah meminta Rekomendasi Pembina Data?')
    st.success('Adakah data publik lain yang dihasilkan selain Daftar Data di atas?')
    st.warning('Data mana saja yang termasuk Data Prioritas Daerah?')
    st.info('Data mana saja yang akan dihasilkan kembali di tahun depan?')
    st.success('Apakah data-data tersebut sudah mengacu pada Standar Data Statistik Nasional?')
    st.warning('Apakah sudah tersedia metadata (Kegiatan, Indikator, Variabel)?')
    st.info('Data mana saja yang sudah mengacu pada Data Induk Kementerian Pengampu?')

st.divider()
st.write('@BPS Provinsi Jawa Barat')