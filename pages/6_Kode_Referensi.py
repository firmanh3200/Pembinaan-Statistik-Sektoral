import streamlit as st

st.set_page_config(layout='wide')

with st.container(border=True):
    with st.container(border=True):
        with st.container(border=True):
            st.title('... :green[PLISS] :orange[Nganjang] ...')

            st.subheader(':green[Portal Literasi dan Identifikasi Statistik Sektoral] \
                        dalam rangka :orange[Nganjang Jabar Caang]', divider='rainbow')

st.divider()

with st.container(border=True):

    st.subheader('KODE REFERENSI')

    # Daftar opsi dan URL yang sesuai
    pilihan = {
        "Kesehatan": "https://data.go.id/list-data-kode-referensi-info/2",
        "Perlindungan Sosial": "https://data.go.id/list-data-kode-referensi-info/3",
        "Ekonomi": "https://data.go.id/list-data-kode-referensi-info/4",
        "Lingkungan": "https://data.go.id/list-data-kode-referensi-info/7",
        "Budaya": "https://data.go.id/list-data-kode-referensi-info/9",
        "Agama": "https://data.go.id/list-data-kode-referensi-info/10",
        "Wilayah Administrasi Pemerintahan dan Pulau": "https://data.go.id/list-data-kode-referensi-info/1",
        "Industri": "https://data.go.id/list-data-kode-referensi-info/5",
        "KBLI": "https://data.go.id/list-data-kode-referensi-info/6",
        "Sumber Daya Alam": "https://data.go.id/list-data-kode-referensi-info/8",
        "Pembangunan Daerah": "https://data.go.id/list-data-kode-referensi-info/11",
        "Pendidikan": "https://data.go.id/list-data-kode-referensi-info/12",
        "Ketenagakerjaan": "https://data.go.id/list-data-kode-referensi-info/13",
        "Pemerintahan Umum": "https://data.go.id/list-data-kode-referensi-info/14",
        "Pertahanan": "https://data.go.id/list-data-kode-referensi-info/15",
        "Luar Negeri": "https://data.go.id/list-data-kode-referensi-info/16",
    }

    # Membuat dropdown
    selected_option = st.selectbox("Pilih Kategori:", list(pilihan.keys()))

    # Tombol untuk membuka URL di tab baru
    if st.button("Buka Tautan"):
        url = pilihan[selected_option]
        st.markdown(f'<a href="{url}" target="_blank">Klik di sini untuk membuka Kode Referensi Kategori {selected_option}</a>', unsafe_allow_html=True)

st.subheader('', divider='orange')

with st.container(border=True):
    st.subheader('Implementasi Kode Referensi')
    
    # PPATK
    with st.expander('PPATK'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://satudata.ppatk.go.id/pages/kode-referensi-dan-data-induk" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://satudata.ppatk.go.id/pages/kode-referensi-dan-data-induk')

    # Kemenkes
    with st.expander('Kementerian Kesehatan'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://opendata.karanganyarkab.go.id/dataset/7ccf725f-0461-4ca4-84aa-80c0c0b1dc4b/resource/729c486c-ca16-4b14-8170-330b2349887c/download/2022-kepmenkes-nomor-hk.01.07_menkes_223_2022.pdf" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://opendata.karanganyarkab.go.id/dataset/7ccf725f-0461-4ca4-84aa-80c0c0b1dc4b/resource/729c486c-ca16-4b14-8170-330b2349887c/download/2022-kepmenkes-nomor-hk.01.07_menkes_223_2022.pdf')

    # Kemendikbudristek
    with st.expander('Kemendikbudristek'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://referensi.data.kemdikbud.go.id/" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://referensi.data.kemdikbud.go.id/')

    # Kementerian Keuangan
    with st.expander('Kementerian Keuangan'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://www.satudja.kemenkeu.go.id/pandu/modul/referensi/" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://www.satudja.kemenkeu.go.id/pandu/modul/referensi/')

    # Klasifikasi Statistik
    with st.expander('Klasifikasi Statistik'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://sibaku.bps.go.id/sibaku/tentangkls" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://sibaku.bps.go.id/sibaku/tentangkls')

    # Kemaritiman
    with st.expander('Kemaritiman dan Investasi'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://jdih.maritim.go.id/kamushukum/kode-referensi" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://jdih.maritim.go.id/kamushukum/kode-referensi')

    # BIG
    with st.expander('Badan Informasi Geospasial'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://katalog.data.go.id/dataset/administrasi_ar_desakel2" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://katalog.data.go.id/dataset/administrasi_ar_desakel2')

    # Perencanaan Pembangunan
    with st.expander('Kodefikasi Perencanaan Pembangunan Daerah'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://api-e-database.kemendagri.go.id/uploads/foto/1719908195420.pdf" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://api-e-database.kemendagri.go.id/uploads/foto/1719908195420.pdf')

    # Kode Wilayah Kemendagri
    with st.expander('Kode Wilayah Administrasi Pemerintahan'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://api-e-database.kemendagri.go.id/uploads/foto/1715587369092.pdf" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://api-e-database.kemendagri.go.id/uploads/foto/1715587369092.pdf')

    # Perhubungan
    with st.expander('Kementerian Perhubungan'):
        # Embed URL in an iframe
        iframe_code = f"""
        <iframe src="https://portaldata.kemenhub.go.id/kode-referensi" width="100%" height="600" style="border:none;"></iframe>
        """

        st.markdown(iframe_code, unsafe_allow_html=True)
        st.caption(f'Sumber: https://portaldata.kemenhub.go.id/kode-referensi')
    
    

            
st.caption('Baca Pedoman: https://drive.google.com/file/d/1B37k_35MENcx6MQ5UWmnV-EleC-derH0/view?usp=sharing')

st.divider()
st.caption('Tim PSS @BPS Provinsi Jawa Barat')