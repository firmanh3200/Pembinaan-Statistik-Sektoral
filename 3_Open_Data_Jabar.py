import streamlit as st
import pandas as pd
import requests

def get_data_from_api(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Memicu error untuk kode status HTTP yang buruk
    return response.json()

st.set_page_config(layout="wide")
st.title("Data Dataset Jawa Barat")

api_url = "https://data.jabarprov.go.id/api-backend/dataset/list?search=&sort=%5B%22mdate%3Adesc%22%5D&limit=5000&skip=0&where=%5B%22dataset_class_id%3D3%22%2C%5B%22regional_id%3D1%22%5D%5D"

try:
    data_json = get_data_from_api(api_url)
    datasets = data_json.get("data", [])

    processed_data = []
    for item in datasets:
        name = item.get("name")
        nama_skpd = item.get("nama_skpd")

        dimensi_awal = None
        dimensi_akhir = None

        for metadata_item in item.get("metadata", []):
            if metadata_item.get("key") == "Dimensi Dataset Awal":
                dimensi_awal = metadata_item.get("value")
            elif metadata_item.get("key") == "Dimensi Dataset Akhir":
                dimensi_akhir = metadata_item.get("value")

        processed_data.append({
            "name": name,
            "Dimensi Dataset Awal": dimensi_awal,
            "Dimensi Dataset Akhir": dimensi_akhir,
            "nama_skpd": nama_skpd
        })

    df = pd.DataFrame(processed_data)

    st.sidebar.header("Filter Data")
    all_skpd = ["Semua"] + sorted(df["nama_skpd"].dropna().unique().tolist())
    selected_skpd = st.sidebar.selectbox("Pilih SKPD", all_skpd)

    if selected_skpd != "Semua":
        df_filtered = df[df["nama_skpd"] == selected_skpd]
    else:
        df_filtered = df

    st.subheader("Tabel Data Dataset")
    st.dataframe(df_filtered)

except requests.exceptions.RequestException as e:
    st.error(f"Gagal mengambil data dari API: {e}. Coba periksa dokumentasi API atau hubungi penyedia API.")
except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")