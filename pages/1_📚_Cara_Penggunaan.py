import streamlit as st
from utils.navigation import sidebar_nav

# Tambahkan CSS untuk kustomisasi font navigasi
st.markdown("""
<style>
div[data-testid="stSidebarNav"] > ul:first-of-type {
    display: none;
}
.st-emotion-cache-128v172 .st-emotion-cache-j9x991 {
    font-size: 1.25rem !important;
    font-weight: bold;
    color: #007bff;
}
</style>
""", unsafe_allow_html=True)


st.set_page_config(
    page_title="Cara Penggunaan",
    page_icon="📚",
    layout="centered"
)

sidebar_nav()

st.title("📚 Cara Menggunakan Aplikasi")
st.markdown("---")

st.markdown("""
<div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px;">
    <h3>Panduan Langkah-demi-Langkah</h3>
    <ol>
        <li><b>Unggah Gambar atau Ambil Foto:</b> Pada halaman utama, Anda memiliki dua pilihan. Pilih metode yang paling nyaman bagi Anda.</li>
        <li><b>Pilih Gambar Mata Ikan:</b> Pastikan gambar yang Anda unggah atau ambil berfokus pada mata ikan. Semakin jelas gambar mata ikan, semakin akurat hasil prediksinya.</li>
        <li><b>Tunggu Analisis:</b> Setelah Anda mengunggah atau mengambil gambar, aplikasi akan secara otomatis memprosesnya. Tunggu beberapa saat hingga hasilnya muncul.</li>
        <li><b>Lihat Hasil:</b> Hasil prediksi akan ditampilkan di sisi kanan, termasuk label "Segar" atau "Tidak Segar", persentase keyakinan, dan saran yang disesuaikan.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

st.header("Contoh Gambar")
st.info("Berikut adalah contoh gambar mata ikan yang cocok untuk analisis dan gambar yang tidak cocok.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.image("assets/gambar_baik_1.jpg", caption="Gambar yang Jelas dan Fokus", use_container_width=True)

with col2:
    st.image("assets/gambar_buruk_1.jpg", caption="Gambar yang Buruk (Tidak Fokus)", use_container_width=True)

st.markdown("---")
st.write("Jika Anda memiliki pertanyaan, silakan kunjungi halaman Tentang Aplikasi.")