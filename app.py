import streamlit as st
import pandas as pd
from PIL import Image
from utils.predictor import predict_image
import plotly.express as px
from utils.navigation import sidebar_nav

# 1. Konfigurasi Halaman & Gaya Kustom
st.set_page_config(
    page_title="🐟 Deteksi Kesegaran Ikan 🌊",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Menambahkan CSS kustom
st.markdown("""
<style>
div[data-testid="stSidebarNav"] > ul:first-of-type {
    display: none;
}
/* CSS lainnya tetap sama */
.st-emotion-cache-1j0wgbx {
    padding-top: 1rem;
}
.st-emotion-cache-1215b2o {
    padding-bottom: 1rem;
}
.st-emotion-cache-1090333 h1 {
    font-size: 2.7rem;
    color: #1976d2;
    text-align: center;
}
.st-emotion-cache-1090333 h3 {
    text-align: center;
    color: #424242;
}
.st-emotion-cache-1090333 h2 {
    color: #212121;
}
.st-emotion-cache-1j98q2k {
    background-color: #e3f2fd;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 6px 12px 0 rgba(0,0,0,0.15);
    margin-bottom: 1rem;
}
.prediction-box-fresh {
    background-color: #81c784;
    color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
}
.prediction-box-nonfresh {
    background-color: #e57373;
    color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
}
.suggestion-box {
    background-color: #f5f5f5;
    color: #424242;
    padding: 18px;
    border-radius: 10px;
    border: 1px solid #e0e0e0;
    margin-top: 15px;
    text-align: center;
}
.image-container {
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

sidebar_nav()

# 3. Judul dan Deskripsi Interaktif
st.title("🐟 Selamat Datang di Aplikasi Deteksi Kesegaran Ikan! 🌊")
st.markdown("---")
st.markdown("Hai! 👋 Aplikasi ini dirancang untuk membantu Anda memprediksi tingkat kesegaran ikan hanya dengan mengunggah gambar mata ikan. Teknologi *deep learning* canggih di balik layar akan menganalisis gambar dan memberikan hasilnya dalam sekejap.")
st.markdown("---")

# --- Bagian Input ---
col_upload, col_result = st.columns([0.4, 0.6])

# Inisialisasi variabel untuk gambar yang diunggah/diambil
image = None
uploaded_file = None
camera_photo = None

with col_upload:
    st.subheader("Pilih Input Gambar")
    
    tab_file_uploader, tab_camera_input = st.tabs(["Unggah Gambar", "Ambil Foto dari Kamera"])
    
    with tab_file_uploader:
        uploaded_file = st.file_uploader(
            "Pilih gambar mata ikan...",
            type=["jpg", "jpeg", "png"],
            help="Pastikan gambar fokus pada mata ikan untuk hasil terbaik."
        )
    
    with tab_camera_input:
        camera_photo = st.camera_input("Ambil foto")
    
    # Menentukan gambar mana yang akan diproses
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Gambar Ikan yang Diunggah.', use_container_width=True)
    elif camera_photo is not None:
        image = Image.open(camera_photo)
        st.image(image, caption='Foto dari Kamera.', use_container_width=True)


with col_result:
    if image is not None:
        with st.spinner("Sedang menganalisis gambar mata ikan..."):
            predicted_label, confidence_percentage, confidence_scores = predict_image(image)

        st.header("✨ Hasil Analisis ✨")
        confidence = float(confidence_percentage)

        if predicted_label == "Segar":
            st.markdown(f"<div class='prediction-box-fresh'><h3>✅ Segar!</h3><p>Model sangat yakin (<strong>{confidence_percentage:.2f}%</strong>) bahwa ikan ini segar.</p></div>", unsafe_allow_html=True)
            if confidence > 90:
                suggestion = "Selamat! Ikan ini super segar dan berkualitas tinggi. Cocok untuk segera diolah atau disimpan dengan baik."
            elif confidence >= 80:
                suggestion = "Ikan ini masih sangat segar. Nikmati kualitasnya dengan segera atau simpan dengan benar untuk beberapa hari ke depan."
            else:
                suggestion = "Ikan ini cukup segar, namun disarankan untuk segera dikonsumsi untuk rasa dan kualitas terbaik. Perhatikan juga kondisi fisik ikan secara manual."
            st.markdown(f"<div class='suggestion-box'><strong>💡 Saran:</strong> {suggestion}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='prediction-box-nonfresh'><h3>❌ Tidak Segar.</h3><p>Model mendeteksi (<strong>{confidence_percentage:.2f}%</strong>) bahwa ikan ini tidak segar.</p></div>", unsafe_allow_html=True)
            suggestion = "Demi keamanan dan kesehatan Anda, sangat disarankan untuk tidak mengonsumsi ikan ini."
            st.markdown(f"<div class='suggestion-box'><strong>⚠️ Saran:</strong> {suggestion}</div>", unsafe_allow_html=True)

        st.subheader("📊 Perbandingan Probabilitas")
        df = pd.DataFrame(
            confidence_scores.items(),
            columns=['Kelas', 'Probabilitas']
        )
        fig = px.bar(df, x='Kelas', y='Probabilitas', color='Kelas',
                     color_discrete_map={'Segar': '#4caf50', 'Tidak Segar': '#e57373'},
                     labels={'Probabilitas': 'Tingkat Keyakinan', 'Kelas': 'Kategori'},
                     title="Probabilitas Kesegaran")
        fig.update_layout(xaxis_title="Kategori", yaxis_title="Tingkat Keyakinan",
                         dragmode=False)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Silakan unggah gambar atau ambil foto di sebelah kiri untuk melihat hasil analisis.")
    
st.markdown("---")
st.markdown("Dibuat dengan ❤️ menggunakan Streamlit, TensorFlow Lite, dan banyak semangat!")