import requests
import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

with st.container(border=True):
    with st.container(border=True):
        with st.container(border=True):
            

            st.subheader(':green[Portal Literasi dan Identifikasi Statistik Sektoral] \
                        dalam rangka :orange[Nganjang Jabar Caang]', divider='rainbow')

st.divider()

with st.container(border=True):

    st.subheader('DAFTAR DATA STATISTIK SEKTORAL JAWA BARAT')

    st.success('Sumber: API Open Data Jabar')
    st.info('Statistik sektoral adalah statistik yang pemanfaatannya ditujukan untuk memenuhi \
                kebutuhan instansi tertentu dalam rangka penyelenggaraan tugas-tugas pemerintahan \
                    dan pembangunan yang merupakan tugas pokok instansi yang bersangkutan.')
    st.warning('Kamus Besar Bahasa Indonesia (KBBI) menjelaskan bahwa indikator \
    merupakan sesuatu yang dapat memberikan petunjuk atau \
    keterangan. Indikator juga bisa diartikan sebagai setiap ciri, \
    karakteristik, atau ukuran yang bisa menunjukkan perubahan yang \
    terjadi pada sebuah bidang tertentu.')

    st.success('Suatu indikator biasanya diawali dengan kata Jumlah, Persentase, Proporsi, Rasio, Indeks, Angka, atau Tingkat')

    # URL yang diberikan
    url2 = 'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=%5B%22mdate%3Adesc%22%5D&limit=25&skip=0&where=%5B%22dataset_class_id%3D3%22%2C%5B%22regional_id%3D1%22%5D%5D'

    all_data = []

    while True:
        # Mengambil data dari URL
        response = requests.get(url2)
        
        # Memeriksa apakah respons berhasil
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break
        
        try:
            data = response.json()
        except ValueError:
            print("Error: Tidak dapat mengurai JSON")
            break
        
        # Memeriksa apakah ada data yang diambil
        if not data['data']:
            break
        
        # Menambahkan data ke dalam list all_data
        all_data += data['data']
        
        # Memperbarui URL untuk halaman berikutnya
        skip_value = len(all_data)
        url2 = f'https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=%5B%22mdate%3Adesc%22%5D&limit=25&skip={skip_value}&where=%5B%22dataset_class_id%3D3%22%2C%5B%22regional_id%3D1%22%5D%5D'

    # Mengambil name, organisasi_name, Dimensi Dataset Awal dan Dimensi Dataset Akhir
    filtered_data = []
    for item in all_data:
        filtered_item = {
            'Data/ Indikator': item.get('name'),
            'Dari': next((meta['value'] for meta in item.get('metadata', []) if meta['key'] == 'Dimensi Dataset Awal'), None),
            'Sampai': next((meta['value'] for meta in item.get('metadata', []) if meta['key'] == 'Dimensi Dataset Akhir'), None),
            'Produsen Data': item.get('nama_skpd')    
        }
        filtered_data.append(filtered_item)

    # Mengonversi data ke DataFrame pandas
    df = pd.DataFrame(filtered_data)
    df = df[df['Produsen Data'] != 'BADAN PUSAT STATISTIK']
    df = df[df['Produsen Data'] != 'INSTANSI VERTIKAL DAN KEMENTERIAN']

    df2 = df.copy()
    df2 = df2.sort_values(by='Produsen Data')

    opd = df2['Produsen Data'].unique()

with st.container(border=True):
    opd_terpilih = st.selectbox('Filter Produsen Data', opd)

    if opd_terpilih:
        df3 = df2[df2['Produsen Data'] == opd_terpilih]
        jumlah_baris = df3.shape[0]
        df3 = df3.sort_values(by='Data/ Indikator')
        
        st.dataframe(df3, use_container_width=True, hide_index=True)
        st.caption('Sumber: https://opendata.jabarprov.go.id/id/dataset')
        
        with st.expander('PERTANYAAN PENTING'):
            st.info(f'PERTANYAAN UNTUK {jumlah_baris} DATA/ INDIKATOR TERSEBUT:')
            st.caption('1. Dihasilkan oleh Bidang apa saja?')
            st.caption('2. Dihasilkan dari kegiatan apa?')
            st.caption('3. Bagaimana proses untuk menghasilkan data tersebut?')
            st.caption('4. Apakah melakukan survei mandiri?')
            st.caption('5. Apakah kegiatan tersebut sudah memiliki Nomor Rekomendasi Statistik?')
            st.caption('6. Apakah sudah tersedia Metadata Statistik Kegiatan?')
            st.caption('7. Apakah sudah tersedia Metadata Statistik Indikator?')
            st.caption('8. Apakah sudah tersedia Metadata Statistik Variabel?')
            st.caption('9. Apakah dikemas dalam bentuk laporan dan dianalisis?')

st.subheader('', divider='green')
        
with st.container(border=True):
    st.warning(f'REKOMENDASI DAN METADATA STATISTIK {opd_terpilih} JAWA BARAT')

    with st.expander(f'Daftar Metadata Statistik {opd_terpilih} JAWA BARAT pada SIRUSA'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D={opd_terpilih}+Jawa+Barat" width="100%" height="600" style="border:none;"></iframe>
        """

        st.info(f'Daftar Metadata Statistik {opd_terpilih} JAWA BARAT pada SIRUSA')
        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D={opd_terpilih}+Jawa+Barat')

    with st.expander(f'Daftar Rekomendasi Statistik {opd_terpilih} JAWA BARAT pada Romantik'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://romantik.web.bps.go.id/rekomendasi-terbit?search={opd_terpilih}+Jawa+Barat" width="100%" height="600" style="border:none;"></iframe>
        """

        st.info(f'Daftar Rekomendasi Statistik {opd_terpilih} JAWA BARAT pada Romantik')
        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://romantik.web.bps.go.id/rekomendasi-terbit?search={opd_terpilih}+Jawa+Barat')

st.subheader('', divider='green')

with st.container(border=True):
    st.success('REFERENSI METADATA DAN REKOMENDASI')

    with st.expander(f'Contoh Metadata Statistik {opd_terpilih} di Pemerintah Daerah lain'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D={opd_terpilih}" width="100%" height="600" style="border:none;"></iframe>
        """

        st.warning(f'Contoh Metadata Statistik {opd_terpilih} di Pemerintah Daerah lain')
        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://sirusa.web.bps.go.id/metadata/site/search?SearchForm%5Bkategori%5D=&SearchForm%5Bkeyword%5D={opd_terpilih}')

    with st.expander(f'Contoh Rancangan Kegiatan Statistik {opd_terpilih} di Pemerintah Daerah lain'):
        st.success(f'Contoh Rancangan Kegiatan {opd_terpilih} selindo')
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://romantik.web.bps.go.id/rekomendasi-terbit?search={opd_terpilih}" width="100%" height="600" style="border:none;"></iframe>
        """

        st.warning(f'Contoh Rancangan Kegiatan Statistik {opd_terpilih} di Pemerintah Daerah lain')
        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://romantik.web.bps.go.id/rekomendasi-terbit?search={opd_terpilih}')

st.divider()
st.caption('Tim PSS @BPS Provinsi Jawa Barat')