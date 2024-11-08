import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout='wide')

st.title(':green[SATU DATA INDONESIA]')

st.header(':blue[Perpres No. 39 Tahun 2019]', divider='green')

st.subheader('DAFTAR DATA STATISTIK SEKTORAL')
st.success('Kondisi Real Time Open Data Jabar')
# URL yang diberikan
url1 = "https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=%5B%22mdate%3Adesc%22%5D&limit=5000&skip=0&where=%5B%22dataset_class_id%3D3%22%2C%5B%22regional_id%3D1%22%5D%5D"
url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=["mdate:desc"]&limit=5000&skip=0&where=["dataset_class_id=3",["regional_id=1"]]'

# Mengambil data dari URL
response = requests.get(url2)
data = response.json()

# Mengonversi data ke DataFrame pandas
df = pd.DataFrame(data['data'])

kolom_dipakai = ['nama_skpd', 'name']

df2 = df[~df['nama_skpd'].str.contains('BADAN PUSAT STATISTIK', case=False, na=False)]
df2 = df[kolom_dipakai].sort_values(by='nama_skpd')

opd = df2['nama_skpd'].unique()

df2 = df2.rename(columns={'nama_skpd':'Produsen Data', 'name':'Data yang Dihasilkan'})

opd_terpilih = st.selectbox('Filter Produsen Data', opd)

if opd_terpilih:
    df3 = df2[df2['Produsen Data'] == opd_terpilih]
    st.dataframe(df3, use_container_width=True, hide_index=True)