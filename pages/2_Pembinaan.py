import streamlit as st

st.set_page_config(layout='wide')

with st.container(border=True):
    with st.container(border=True):
        with st.container(border=True):
            

            st.subheader(':green[Portal Literasi dan Identifikasi Statistik Sektoral] \
                        dalam rangka :orange[Nganjang Jabar Caang]', divider='rainbow')

st.divider()
with st.container(border=True):
    st.subheader(":blue[Bentuk Pembinaan]")
    st.caption('Petunjuk Teknis Pembinaan Statistik Sektoral Hal. 38 - 41')
    with st.expander('Bimbingan Teknis (Bimtek)'):
        st.info('Bimtek atau bimbingan teknis merupakan suatu layanan bimbingan dan \
                penyuluhan teknis yang diberikan oleh tenaga ahli atau profesional di \
                bidangnya dengan tujuan meningkatkan kualitas sumber daya manusia \
                (SDM). Pembinaan statistik sektoral yang bersifat teknis dapat diberikan BPS \
                ke K/L/Pemda dalam bentuk bimtek sehingga substansi pembinaan bisa \
                lebih detail. Sebagai contoh “Bimbingan Teknis Pengolahan Data Statistik”.')
        
    with st.expander('Seminar/Webinar'):
        st.success('Seminar adalah pertemuan untuk membahas suatu topik yang dipimpin \
                oleh ahli/narasumber. Seminar bertujuan untuk membahas atau bertukar \
                pikiran mengenai suatu permasalahan ilmiah atau topik tertentu. Webinar \
                adalah seminar atau beragam presentasi yang dilakukan dengan media \
                internet. Pembinaan statistik sektoral dalam bentuk seminar/webinar bisa \
                menjadi pilihan yang tepat untuk substansi pembinaan yang bersifat tematik \
                dan dengan peserta yang massive, misal: “Webinar Pemanfaatan Big Data \
                untuk Penyediaan Data Statistik”.')
        
    with st.expander('Asistensi'):
        st.warning('Asistensi adalah kegiatan mengasisteni atau membantu seseorang dalam \
                tugas profesionalnya. Dalam pembinaan asistensi bisa berupa pendampingan \
                dalam proses pelaksanaan kegiatan statistik baik pada tahapan perencanaan, \
                pengolahan, analisis, dan lain sebagainya. Sebagai contoh “Asistensi \
                Penyusunan Daftar Data”.')
        
    with st.expander('Focus Group Discussion (FGD)'):
        st.info('Focus Group Discussion (FGD) adalah diskusi sistematis dan terarah pada \
                suatu kelompok untuk membahas suatu masalah tertentu yang dipandu oleh \
                moderator. Tujuan FGD adalah menyamakan persepsi mengenai topik atau \
                isu tertentu sehingga tercapai kesepakatan mengenai topik tersebut. Dalam \
                statistik FGD dapat dilaksanakan misalnya dalam Forum Data di wilayah \
                masing-masing dengan K/L/D/I terkait.')
        
    with st.expander('Rapat Koordinasi'):
        st.success('Rapat koordinasi merupakan kegiatan yang dilaksanakan untuk \
                mencapai suatu tujuan bersama dengan peran aktif masing-masing pihak \
                yang terlibat. Rapat koordinasi dapat dilakukan sebagai langkah awal dalam \
                pembinaan statistik. Rapat koordinasi juga lebih cocok dilakukan untuk \
                pembinaan pada level pengambil kebijakan (pimpinan).')
        
    with st.expander('Workshop'):
        st.warning('Workshop atau lokakarya diartikan sebagai kegiatan yang didalamnya \
                terdapat beberapa orang dengan keahlian tertentu yang membagikan \
                pengetahuan atau pelatihan kepada peserta yang terlibat. Sekelompok orang \
                terlibat dalam diskusi aktif mengenai suatu topik tertentu beserta ada \
                praktek yang dilakukan. Pembinaan statistik dalam bentuk workshop dapat \
                dilakukan untuk substansi pembinaan yang sifatnya teknis, sehingga ada \
                praktek pengerjaannya. Sebagai contoh: Workshop Metadata dimana ada \
                penjelasan teknis beserta dengan praktek pengisian metadata pada aplikasi \
                Indonesia Data Hub (INDAH).')
        
    with st.expander('Coaching Clinic'):
        st.info('Coaching clinic adalah sebuah proses bimbingan singkat, berupa kegiatan \
                yang berfungsi untuk penguasaan ilmu pengetahuan dan peningkatan kinerja \
                sumber daya manusia (SDM). Pada dasarnya definisi coaching lebih pada \
                pendampingan antara satu coach dengan individu yang membutuhkan \
                bimbingan sehingga mendapatkan hasil peningkatan skill dan pemikiran \
                individu terkait. Pada pembinaan statistik sektoral coaching clinic dapat \
                dilaksanakan terkait peningkatan kemampuan SDM dari instansi pusat atau \
                pemerintah daerah dalam penyelenggaraan kegiatan statistik.')
    
    with st.expander('Konsultasi'):
        st.success('Konsultasi merupakan dialog atau diskusi yang didalamnya terdapat \
                aktifitas berbagi dan bertukar informasi dengan tujuan pihak yang \
                melakukan konsultasi mengetahui lebih dalam tentang suatu tema atau topik \
                tertentu. Dalam KBBI konsultasi adalah pertukaran pikiran untuk \
                mendapatkan kesimpulan (nasihat, saran, dan sebagainya) yang sebaik-baiknya. \
                Konsultasi bisa diberikan terkait dengan penyelenggaraan ataupun \
                data hasil kegiatan statistik. Sebagai contoh konsultasi rancangan standar \
                data statistik yang akan diajukan walidata pemerintah daerah ke walidata \
                K/L teknis pengampunya.')
        
    with st.expander('Audiensi'):
        st.warning('Audiensi menurut kamus besar bahasa indonesia adalah kunjungan \
                kehormatan, atau arti lainnya adalah pengunjung atau pendengar suatu \
                ceramah dan sebagainya. Audiensi memiliki artian erat dengan konsultasi, \
                sosialisasi dengan tujuan untuk memberikan pemahaman terkait topik atau \
                tema tertentu. Topik atau tema yang terkait dengan penyelenggaraan statistik \
                sektoral dapat menjadi pembahasan dalam audiensi pembinaan. Sebagai \
                contoh Diskominfo Kabupaten Pangandaran melakukan kunjungan kerja ke \
                BPS Pusat untuk audiensi perihal pengajuan pemetaan urusan statistik di \
                wilayahnya.')
        
    with st.expander('Konsolidasi'):
        st.info('Konsolidasi menurut kamus besar bahasa Indonesia adalah perbuatan \
                memperteguh atau memperkuat (hubungan, persatuan, dan sebagainya). \
                Dalam kaitannya dengan dengan pembinaan konsolidasi bisa dilaksanakan \
                dalam upaya meningkatkan komitmen dalam pelaksanaan satu data \
                Indonesia dan penyelenggaraan statistik yang berkualitas. Sebagai contoh: \
                BPS melakukan konsolidasi angka/data statistik sektoral dengan OPD untuk \
                kebutuhan penyusunan Daerah Dalam Angka.')
        
    with st.expander('Knowledge Sharing'):
        st.success('Menurut Chen (2001), knowledge sharing adalah komunikasi \
                interpersonal yang melibatkan komunikasi dan penerimaan pengetahuan \
                dari orang lain, dan salah satu cara utama untuk mentransfer pengetahuan \
                adalah seperti interaksi manusia. Bentuk ini merupakan bentuk transfer \
                dengan interaksi sosial yang menciptakan dasar umum bahwa terdapat \
                kebutuhan untuk kerja sama. Sebagai contoh: BPS mengundang narasumber \
                dari Sekretariat SDI Bappenas untuk memberikan knowledge sharing tentang \
                Kode Referensi.')
        
    with st.expander('Pameran'):
        st.warning('Pameran merupakan kegiatan penyajian suatu karya atau produk untuk \
                dikomunikasikan sehingga dapat diapresiasi oleh pihak lain. Pameran juga \
                dapat diartikan sebagai kegiatan promosi sehingga produk yang dihasilkan \
                dapat dikenal oleh khalayak. Pameran terkait dengan pembinaan adalah jika \
                produk atau pelaksanaan pameran diperuntukan kepada instansi pusat atau \
                pemerintah daerah sehingga pemahaman terkait dengan pembinaan dapat \
                diterima secara luas.')
        
    with st.expander('Pendidikan dan Pelatihan (Diklat)'):
        st.info('Diklat adalah proses belajar mengajar yang bertujuan untuk \
                meningkatkan pengetahuan seseorang. Diklat merupakan salah satu cara \
                untuk meningkatkan kualitas sumber daya manusia (SDM). Pembinaan \
                statistik sektoral dapat dilaksanakan dalam bentuk Diklat Statistik Sektoral \
                yang diselenggarakan oleh Pusdiklat BPS ataupun oleh lembaga lainnya yang \
                memiliki kewenangan dalam menyelenggarakan diklat sesuai ketentuan yang \
                berlaku.')
        
# st.divider()

# with st.container(border=True):

#     st.subheader('Materi Pembinaan Statistik Sektoral', divider='green')

#     with st.expander('PROSES BISNIS STATISTIK'):
#         kolom1, kolom2, kolom3 = st.columns(3)
#         with kolom1:
#             st.link_button("Dasar-dasar Statistik", url="https://drive.google.com/file/d/1cmB7U6qWBQYrG_5sUiuKJyz4EDb20IL5/preview")

#             st.link_button("Perencanaan Kegiatan", url="https://drive.google.com/file/d/1Ocu8Kwz10WeQeRaS2FaAdLlKCGrWaQKo/preview")

#             st.link_button("Perancangan Kegiatan", url="https://drive.google.com/file/d/1XT98Jg_G1jbAT3yNeTz1gTvQkMrjUwZA/preview")

#         with kolom2:
#             st.link_button("Pengumpulan Data", url="https://drive.google.com/file/d/1EqRNPp19xhPI7Njc_yEii2QQvBV2WPb1/preview")

#             st.link_button("Pengolahan Data", url="https://drive.google.com/file/d/18TFFNbZaDUt9JJkMalDhlynYP4--7ZlE/preview")

#             st.link_button("Analisis Statistik", url="https://drive.google.com/file/d/1Gakcm7etk2V-YQ-PFkC51Rbf3oO1kvXN/preview")

#         with kolom3:
#             st.link_button("Diseminasi dan Evaluasi", url="https://drive.google.com/file/d/1WLuE8fo5vu3QADpTPuYKJQUTQdY6Xs6P/preview")
            
#             st.link_button("Contoh Kegiatan Statistik", url="https://drive.google.com/file/d/18Em1hySNdkAoEt4YJysUblFd0eQGOIwX/preview")
            
#             st.link_button("Metadata Statistik", url="https://drive.google.com/file/d/1fngDi4qmpwTMlX83AkqUk9PydQguFq-W/preview")
            

#     with st.expander('PENYELENGGARAAN STATISTIK SEKTORAL'):
#         kolom1, kolom2, kolom3 = st.columns(3)
#         with kolom1:
#             st.link_button("Satu Data Indonesia", url="https://drive.google.com/file/d/1STnvC6GOmaImybDi5PdJwStine-kTXw2/view?usp=sharing")

#             st.link_button("Kualitas Data", url="https://drive.google.com/file/d/1MXduD16UdSjHK9zCU_GloQ1bnSaawi4u/view?usp=sharing")

#             st.link_button("Proses Bisnis Statistik", url="https://drive.google.com/file/d/1rGRIdKws-JnF8qW4mlw60NYljeqzq1of/view?usp=sharing")

#         with kolom2:
#             st.link_button("Kelembagaan", url="https://drive.google.com/file/d/1e8eTnj2jA968pUJy1_cNyh9cKSMoCJDk/view?usp=sharing")

#             st.link_button("Sistem Statistik Nasional", url="https://drive.google.com/file/d/1AMdjtkt4rkze9oW3zyi0pKouEy2291kM/view?usp=sharing")

#             st.link_button("Standar Data", url="https://drive.google.com/file/d/1Q6CNMjJAiQlPS-aqcf4_PkyDp2KsxtU0/view?usp=sharing")

#         with kolom3:
#             st.link_button("Rekomendasi Survei", url="https://drive.google.com/file/d/1aY9eLyVRtZ84lOcl1fjVaCrqohCI6L7Z/view?usp=sharing")
            
#             st.link_button("Big Data", url="https://drive.google.com/file/d/1jb7YOLwRHlWvXAYoZF5q60oMaOtYZ_70/view?usp=sharing")
            
#             st.link_button("Manajemen Kualitas", url="https://drive.google.com/file/d/1w6YVhX4ZnjzuiKy6GVHEpHG0cmWPLaPe/view?usp=sharing")

st.divider()
with st.container(border=True):
    with st.container(border=True):
        st.link_button("Laporan Pembinaan Tim PSS", url="https://webapps.bps.go.id/rujukan/pembinaan/public/")
        
st.divider()
st.caption('Tim PSS @BPS Provinsi Jawa Barat')