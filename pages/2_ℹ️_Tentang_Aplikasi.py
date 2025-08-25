import streamlit as st
from utils.navigation import sidebar_nav

# Konfigurasi halaman
st.set_page_config(
    page_title="Tentang Aplikasi",
    page_icon="ℹ️",
    layout="centered"
)

# Panggil fungsi navigasi
sidebar_nav()

# --- CSS Kustom ---
st.markdown("""
<style>
/* Kode untuk menyembunyikan navigasi bawaan */
div[data-testid="stSidebarNav"] > ul:first-of-type {
    display: none;
}

/* Gaya umum untuk semua elemen di halaman ini */
.main-container {
    padding: 2rem;
    background-color: #f8f9fa;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    /* Tambahkan jarak di bawah setiap kontainer */
    margin-bottom: 20px;
}

/* Gaya untuk judul h3 */
h3 {
    color: #007bff;
    border-bottom: none;
    padding-bottom: 0;
    margin-top: 2rem;
}

/* Gaya untuk daftar (ul) */
ul {
    list-style-type: none;
    padding-left: 0;
}

/* Gaya untuk item daftar (li) */
li {
    background-color: #e9ecef;
    margin-bottom: 0.5rem;
    padding: 0.75rem;
    border-radius: 5px;
    transition: transform 0.2s;
}

li:hover {
    transform: scale(1.02);
}

/* Gaya untuk paragraf (p) */
p {
    line-height: 1.6;
    color: #333;
}
</style>
""", unsafe_allow_html=True)
# --- Akhir dari CSS Kustom ---

st.title("ℹ️ Tentang Aplikasi")
st.markdown("---")

# Menggunakan markdown terpisah untuk setiap bagian
# dan memastikan setiap bagian memiliki kelas 'main-container'
st.markdown("""
<div class="main-container">
    <h3>Tujuan Aplikasi</h3>
    <p>Aplikasi ini dikembangkan untuk memberikan solusi cepat dan mudah dalam mendeteksi kesegaran ikan. Dengan menggunakan teknologi visi komputer dan model <i>deep learning</i> yang telah dilatih pada dataset gambar mata ikan, aplikasi ini dapat membantu individu maupun bisnis perikanan dalam menjaga kualitas produk mereka.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-container">
    <h3>Teknologi yang Digunakan</h3>
    <ul>
        <li><b>Streamlit:</b> Digunakan untuk membangun antarmuka web yang interaktif.</li>
        <li><b>TensorFlow Lite:</b> Model <i>deep learning</i> kami dikonversi ke format TFLite untuk memastikan performa yang cepat dan efisien.</li>
        <li><b>VGG16 Fine-tuned:</b> Model dasar yang digunakan adalah VGG16 yang dimodifikasi (fine-tuned) untuk tugas klasifikasi ini.</li>
        <li><b>Plotly Express:</b> Digunakan untuk membuat visualisasi data yang interaktif dan informatif.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-container">
    <h3>Pengembang</h3>
    <p>Aplikasi ini adalah proyek yang dikembangkan sebagai bagian dari eksperimen dan pembelajaran dalam bidang <i>Machine Learning Operations (MLOps)</i>.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.write("Terima kasih telah menggunakan aplikasi ini!")