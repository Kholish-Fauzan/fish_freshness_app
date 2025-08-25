# utils/navigation.py
import streamlit as st

def sidebar_nav():
    st.sidebar.title("Navigasi Aplikasi")
    st.sidebar.markdown("---")
    st.sidebar.page_link("app.py", label="Beranda", icon="🏠")
    st.sidebar.page_link("pages/1_📚_Cara_Penggunaan.py", label="📚 Cara Penggunaan")
    st.sidebar.page_link("pages/2_ℹ️_Tentang_Aplikasi.py", label="ℹ️ Tentang Aplikasi")
    st.sidebar.markdown("---")