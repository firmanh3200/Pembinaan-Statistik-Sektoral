import streamlit as st
import pandas as pd

lke = pd.read_excel('data/lke-epss.xlsx', dtype={'KodeInd':'str'})
kematangan = pd.read_excel('data/kematangan.xlsx')

st.set_page_config(layout='wide')

with st.container(border=True):
    with st.container(border=True):
        with st.container(border=True):
            

            st.subheader(':green[Portal Literasi dan Identifikasi Statistik Sektoral] \
                        dalam rangka :orange[Nganjang Jabar Caang]', divider='rainbow')

st.divider()

with st.container(border=True):
    
    st.subheader('Evaluasi Penyelenggaraan Statistik Sektoral', divider='rainbow')

    with st.expander('TINGKAT KEMATANGAN'):
        st.success(':red[RINTISAN]:  penyelenggaraan statistik sektoral dilakukan \
                    :red[tanpa perencanaan dan sewaktu-waktu]')
        
        st.info(':red[TERKELOLA]: penyelenggaraan statistik sektoral sudah \
                dilakukan sesuai dengan fungsi manajemen dan \
                diterapkan pada :red[sebagian unit kerja] dalam organisasi')
        
        st.warning(':red[TERDEFINISI]: penyelenggaraan statistik sektoral sudah \
                dilakukan sesuai dengan fungsi manajemen yang \
                sesuai pedoman/standar dan diterapkan pada \
                semua unit kerja dalam organisasi')
        
        st.success(':red[TERPADU DAN TERUKUR]: penyelenggaraan statistik sektoral telah \
                dilakukan secara terpadu dan telah berkontribusi \
                pada kinerja organisasi. Kinerja Penyelenggaraan \
                Statistik Sektoral dapat diukur melalui kegiatan \
                :red[reviu dan evaluasi pada setiap proses]')
        
        st.info(':red[OPTIMUM]: penyelenggaraan statistik sektoral telah \
                dilakukan :red[peningkatan kualitas secara \
                berkesinambungan] berdasarkan hasil reviu dan \
                evaluasi')
        
    with st.expander('PRINSIP SDI'):
        lke1 = lke[lke['Domain'] == 'Prinsip SDI']
        st.dataframe(lke1, hide_index=True, use_container_width=True)
        
        st.divider()
        kematangan1 = kematangan[kematangan['Kode'] == 1]
        indikator = kematangan1['Indikator'].unique()
        indterpilih = st.selectbox('Pilih Indikator', indikator)
        
        if indterpilih:
            kematangan1a = kematangan1[kematangan1['Indikator'] == indterpilih]
            st.table(kematangan1a)
        
        lke1a = lke1[lke1['Indikator'] == indterpilih]    
        penjelasan = lke1a['Penjelasan Indikator'].to_list()
        st.success('Penjelasan Indikator')
        st.write(penjelasan)
        
    with st.expander('KUALITAS DATA'):
        lke2 = lke[lke['Domain'] == 'Kualitas Data']
        st.dataframe(lke2, hide_index=True, use_container_width=True)
        
        st.divider()
        kematangan2 = kematangan[kematangan['Kode'] == 2]
        indikator = kematangan2['Indikator'].unique()
        indterpilih = st.selectbox('Pilih Indikator', indikator)
        
        if indterpilih:
            kematangan2a = kematangan2[kematangan2['Indikator'] == indterpilih]
            st.table(kematangan2a)
            
        lke2a = lke2[lke2['Indikator'] == indterpilih]    
        penjelasan = lke2a['Penjelasan Indikator'].to_list()
        st.success('Penjelasan Indikator')
        st.write(penjelasan)
        
    with st.expander('PROSES BISNIS STATISTIK'):
        lke3 = lke[lke['Domain'] == 'Proses Bisnis Statistik']
        st.dataframe(lke3, hide_index=True, use_container_width=True)
        
        st.divider()
        kematangan3 = kematangan[kematangan['Kode'] == 3]
        indikator = kematangan3['Indikator'].unique()
        indterpilih = st.selectbox('Pilih Indikator', indikator)
        
        if indterpilih:
            kematangan3a = kematangan3[kematangan3['Indikator'] == indterpilih]
            st.table(kematangan3a)
            
        lke3a = lke3[lke3['Indikator'] == indterpilih]    
        penjelasan = lke3a['Penjelasan Indikator'].to_list()
        st.success('Penjelasan Indikator')
        st.write(penjelasan)
        
    with st.expander('KELEMBAGAAN'):
        lke4 = lke[lke['Domain'] == 'Kelembagaan']
        st.dataframe(lke4, hide_index=True, use_container_width=True)
        
        st.divider()
        kematangan4 = kematangan[kematangan['Kode'] == 4]
        indikator = kematangan4['Indikator'].unique()
        indterpilih = st.selectbox('Pilih Indikator', indikator)
        
        if indterpilih:
            kematangan4a = kematangan4[kematangan4['Indikator'] == indterpilih]
            st.table(kematangan4a)
            
        lke4a = lke4[lke4['Indikator'] == indterpilih]    
        penjelasan = lke4a['Penjelasan Indikator'].to_list()
        st.success('Penjelasan Indikator')
        st.write(penjelasan)
        
    with st.expander('STATISTIK NASIONAL'):
        lke5 = lke[lke['Domain'] == 'Statistik Nasional']
        st.dataframe(lke5, hide_index=True, use_container_width=True)
        
        st.divider()
        kematangan5 = kematangan[kematangan['Kode'] == 5]
        indikator = kematangan5['Indikator'].unique()
        indterpilih = st.selectbox('Pilih Indikator', indikator)
        
        if indterpilih:
            kematangan5a = kematangan5[kematangan5['Indikator'] == indterpilih]
            st.table(kematangan5a)
            
        lke5a = lke5[lke5['Indikator'] == indterpilih]    
        penjelasan = lke5a['Penjelasan Indikator'].to_list()
        st.success('Penjelasan Indikator')
        st.write(penjelasan)

    st.subheader('', divider='green')

    st.success('Baca Pedoman: https://drive.google.com/file/d/1B37k_35MENcx6MQ5UWmnV-EleC-derH0/view?usp=sharing')

st.warning("Anda dapat bertanya tentang epss pada bot di bawah.")

# Menambahkan widget Galichat
chat_script = """
<script
  src="https://widget.galichat.com/gali-embeded.min.js" 
  chat-hash="rlmgak3bta8qcma3e4p5rs" 
  defer>
</script>
"""

# Menyisipkan kode HTML ke dalam aplikasi Streamlit
st.components.v1.html(chat_script, height=600)

st.divider()
st.caption('Tim PSS @BPS Provinsi Jawa Barat')