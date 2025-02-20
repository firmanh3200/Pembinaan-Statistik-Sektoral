import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

tusijf = pd.read_excel('data/tusijf.xlsx')
tahapan = tusijf['Tahapan Kegiatan'].unique()

with st.container(border=True):
    with st.container(border=True):
        with st.container(border=True):
            

            st.subheader(':green[Portal Literasi dan Identifikasi Statistik Sektoral] \
                        dalam rangka :orange[Nganjang Jabar Caang]', divider='rainbow')

st.divider()

with st.container(border=True):

    st.subheader('TAHAPAN PELAKSANAAN')

    with st.expander('Perencanaan Data'):
        st.success('Mengidentifikasi kebutuhan data daerah sesuai dengan kebutuhan perencanaan pembangunan daerah.')
        st.warning('Dikoordinasikan oleh Walidata (Diskominfo) dengan melibatkan Produsen Data dari perangkat daerah.')
        with st.container(border=True):
            st.info('Kaitan dengan Tusi JF Berdasarkan PerMenPAN-RB 12 dan 13 Tahun 2022')
            df1 = tusijf[tusijf['kode'] == 'A']
            tahapan1 = df1['Tahapan Kegiatan'].unique()    
            tahap1 = st.selectbox('Pilih Tahapan Kegiatan', tahapan1, key='tahap1')
            if tahap1:
                df1a = df1[df1['Tahapan Kegiatan'] == tahap1]
                st.table(df1a)
            
    with st.expander('Pengumpulan Data'):
        st.success('Meminta rekomendasi kepada Pembina Data.')
        st.warning('Mengumpulkan data yang telah diidentifikasi sesuai dengan kebutuhan.')
        st.info('Dikoordinasikan oleh Walidata dengan melibatkan Produsen Data dari perangkat daerah.')
        with st.container(border=True):
            st.success('Kaitan dengan Tusi JF Berdasarkan PerMenPAN-RB 12 dan 13 Tahun 2022')
            df1 = tusijf[tusijf['kode'] == 'B']
            tahapan1 = df1['Pelaksana'].unique()    
            tahap1 = st.selectbox('Pilih Pelaksana Kegiatan', tahapan1, key='tahap2')
            if tahap1:
                df1a = df1[df1['Pelaksana'] == tahap1]
                st.table(df1a)
                
    with st.expander('Pemeriksaan Data'):
        st.success('Memeriksa kesesuaian data yang telah dikumpulkan dengan prinsip Satu Data Indonesia.')
        st.warning('Pemeriksaan ini memastikan bahwa data yang dihasilkan dapat dipertanggungjawabkan dan sesuai dengan standar yang ditetapkan.')
        st.success('Menyusun metadata untuk setiap data yang dikumpulkan. Metadata ini mencakup informasi tentang sumber data, metode pengumpulan, dan kualitas data.')
        st.warning('Metadata membantu dalam memastikan interoperabilitas dan penggunaan data yang lebih efektif.')
        with st.container(border=True):
            st.info('Kaitan dengan Tusi JF Berdasarkan PerMenPAN-RB 12 dan 13 Tahun 2022')
            df1 = tusijf[tusijf['kode'] == 'C']
            tahapan1 = df1['Tahapan Kegiatan'].unique()    
            tahap1 = st.selectbox('Pilih Tahapan Kegiatan', tahapan1, key='tahap3')
            if tahap1:
                df1a = df1[df1['Tahapan Kegiatan'] == tahap1]
                st.table(df1a)
        
    with st.expander('Penyebarluasan Data'):
        st.success('Menyebarluaskan data melalui Portal Satu Data Indonesia sehingga dapat diakses oleh instansi pusat dan daerah.')
        st.warning('Data yang disebarluaskan harus memenuhi standar dan prinsip Satu Data Indonesia.')
        with st.container(border=True):
            st.info('Kaitan dengan Tusi JF Berdasarkan PerMenPAN-RB 12 dan 13 Tahun 2022')
            df1 = tusijf[tusijf['kode'] == 'D']
            tahapan1 = df1['Tahapan Kegiatan'].unique()    
            tahap1 = st.selectbox('Pilih Tahapan Kegiatan', tahapan1, key='tahap4')
            if tahap1:
                df1a = df1[df1['Tahapan Kegiatan'] == tahap1]
                st.table(df1a)
                
    with st.expander('Monitoring dan Evaluasi'):
        st.success('Melakukan monitoring dan evaluasi terhadap pelaksanaan Satu Data di tingkat daerah.')
        st.warning('Evaluasi ini bertujuan untuk memastikan bahwa data yang dihasilkan terus memenuhi standar dan dapat digunakan untuk perencanaan pembangunan yang lebih baik.')
        st.success('Mengadakan rapat koordinasi secara berkala untuk membahas dan menyelesaikan berbagai isu terkait data.')
        st.warning('Rapat ini juga digunakan untuk menyepakati langkah-langkah strategis dalam pengelolaan data di daerah.')
        with st.container(border=True):
            st.info('Kaitan dengan Tusi JF Berdasarkan PerMenPAN-RB 12 dan 13 Tahun 2022')
            df1 = tusijf[tusijf['kode'] == 'E']
            tahapan1 = df1['Tahapan Kegiatan'].unique()    
            tahap1 = st.selectbox('Pilih Tahapan Kegiatan', tahapan1, key='tahap5')
            if tahap1:
                df1a = df1[df1['Tahapan Kegiatan'] == tahap1]
                st.table(df1a)     
    
    st.success('Tahapan-tahapan ini dirancang untuk memastikan bahwa \
        data yang dihasilkan oleh pemerintah daerah dapat digunakan \
            secara efektif dalam perencanaan dan evaluasi pembangunan.')

st.divider()
st.caption('Tim PSS @BPS Provinsi Jawa Barat')