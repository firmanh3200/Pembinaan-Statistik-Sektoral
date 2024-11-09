import streamlit as st
import pandas as pd
import requests
import lxml

st.set_page_config(layout='wide')
st.title('Contoh Scrapping Data')

st.success('Menu Daftar Data adalah contoh Web Scrapping dari Open Data Jabar.')
st.warning('Berikut adalah beberapa contoh Web Scrapping yang mungkin akan bermanfaat untuk Pekerjaan sehari-hari.')

with st.expander('DATA REALISASI APBD'):
    st.success('Data diambil dari Sistem Informasi Keuangan Daerah (SIKD) / Web djpk.kemenkeu.go.id')
    
    bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    tahun = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
    wilayah = {
        '00': 'Jawa Barat',
        '03': 'Bogor',
        '14': 'Sukabumi',
        '05': 'Cianjur',
        '01': 'Bandung',
        '07': 'Garut',
        '16': 'Bekasi',
        '04': 'Ciamis',
        '10': 'Kuningan',
        '06': 'Cirebon',
        '11': 'Majalengka',
        '15': 'Sumedang',
        '08': 'Indramayu',
        '13': 'Subang',
        '12': 'Purwakarta',
        '09': 'Karawang',
        '02': 'Bekasi',
        '26': 'Bandung Barat',
        '27': 'Pangandaran',
        '19': 'Kota Bogor',
        '22': 'Kota Sukabumi',
        '17': 'Kota Bandung',
        '20': 'Kota Cirebon',
        '18': 'Kota Bekasi',
        '21': 'Kota Depok',
        '24': 'Kota Cimahi',
        '23': 'Kota Tasikmalaya',
        '25': 'Kota Banjar'
    }
    # Membuat list nama untuk ditampilkan di selectbox
    nama_list = list(wilayah.values())

    # Membuat selectbox dengan nama
    kol1, kol2, kol3 = st.columns(3)
    with kol1:
        wilayah_terpilih = st.selectbox('Pilih Wilayah:', nama_list)
    with kol2:
        tahun_terpilih = st.selectbox('Pilih Tahun', tahun)
    with kol3:
        bulan_terpilih = st.selectbox('Pilih Bulan', bulan)
    
    # Mendapatkan kode berdasarkan nama yang dipilih
    kode_terpilih = [kode for kode, nama in wilayah.items() if nama == wilayah_terpilih][0]
    
    if wilayah_terpilih and tahun_terpilih and bulan_terpilih:
        url = f'https://djpk.kemenkeu.go.id/portal/data/apbd?periode={bulan_terpilih}&tahun={tahun_terpilih}&provinsi=10&pemda={kode_terpilih}'
        
        # Membaca tabel HTML dari URL dan mengubahnya menjadi dataframe pandas
        dataframes = pd.read_html(url)
        
        df = dataframes[0]
        del df['Unnamed: 0']
        
        st.write(f'Realisasi APBD {wilayah_terpilih}, Bulan {bulan_terpilih}, Tahun {tahun_terpilih}')
        st.dataframe(df, hide_index=True, use_container_width=True)
        
        url2 = f'https://djpk.kemenkeu.go.id/portal/csv_apbd?type=apbd&periode={bulan_terpilih}&tahun={tahun_terpilih}&provinsi=10&pemda={kode_terpilih}'
        st.link_button('Unduh Data dalam bentuk CSV', f'{url2}')
        st.link_button('Kunjungi Web DJPK', f'https://djpk.kemenkeu.go.id/portal/data/apbd?periode={bulan_terpilih}&tahun={tahun_terpilih}&provinsi=10&pemda={kode_terpilih}')
        

with st.expander('SCRAPPING DATA KEMENDESA'):
    st.success('Mengambil data dari s.id/kemendesa.go.id')
    kabkot = {
        '3201': 'Bogor',
        '3202': 'Sukabumi',
        '3203': 'Cianjur',
        '3204': 'Bandung',
        '3205': 'Garut',
        '3206': 'Tasikmalaya',
        '3207': 'Ciamis',
        '3208': 'Kuningan',
        '3209': 'Cirebon',
        '3210': 'Majalengka',
        '3211': 'Sumedang', 
        '3212': 'Indramayu',
        '3213': 'Subang',
        '3214': 'Purwakarta',
        '3215': 'Karawang',
        '3216': 'Bekasi',
        '3217': 'Bandung Barat',
        '3218': 'Pangandaran',
        '3271': 'Kota Bogor',
        '3272': 'Kota Sukabumi',
        '3273': 'Kota Bandung',
        '3274': 'Kota Cirebon',
        '3275': 'Kota Bekasi',
        '3276': 'Kota Depok',
        '3277': 'Kota Cimahi',
        '3278': 'Kota Tasikmalaya',
        '3279': 'Kota Banjar'
    }
    
    kabkot_list = list(kabkot.values())
    kabkot_terpilih = st.selectbox('Pilih Wilayah:', kabkot_list, key='kemendesa')
    idterpilih = [kode for kode, nama in kabkot.items() if nama == kabkot_terpilih][0]
    
    if wilayah_terpilih:
        url = f'https://sid.kemendesa.go.id/region/selected?code={idterpilih}&param=district'
        
        response = requests.get(url)
        data = response.json()
        
        df = pd.DataFrame(data)
        st.dataframe(df)
        
        kec = st.selectbox('Filter Kecamatan untuk Menampilkan Daftar Desa dan Alamat Websitenya', df['kdkecamatan'], key='kemendesa2')
        
        if kec:
            url3 = f'https://sid.kemendesa.go.id/population-statistic/data?location_code=&province_id=32&city_id={idterpilih}&district_id={kec}&village_id=&on=village-web'
            
            response2 = requests.get(url3)
            data2 = response2.json()
            
            df2 = pd.DataFrame(data2['village'])
            
            st.dataframe(df2, use_container_width=True, hide_index=True)
            st.caption('Catatan: Kemendesa tidak menampilkan Data Kelurahan')
            
            url4 = f'https://sid.kemendesa.go.id/region/selected?code={kec}&param=village'
            
            response4 = requests.get(url4)
            data4 = response4.json()
            
            df4 = pd.DataFrame(data4)
            st.dataframe(df4, use_container_width=True, hide_index=True)
            