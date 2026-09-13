import streamlit as st
#pembuatan title halaman
st.set_page_config(page_title="cv_app", page_icon=":guardsman:", layout="wide")

#membuat sidebar untuk menginput data
st.sidebar.title("pengaturan profil")
st.sidebar.write("masukan data diri anda di bawah ini: ")

#komponen input teks
nama = st.sidebar.text_input("Nama Lengkap", "Muhammad Suyuthi Yahya")
nim = st.sidebar.text_input("NIM", "2530801098")
jurusan = st.sidebar.selectbox("jurusan", ["Informatika"])

# Komponen Input Teks Area (Multi-baris)
deskripsi = st.sidebar.text_area("Deskripsi Singkat (Bio)", "saya adalah mahasiswa jurusan informatika yang memimliki minat di bidang pengetahuan komputer dan teknoligi informasi.")
pengalaman = st.sidebar.text_area("Pengalaman Organisasi", "saya pernah menjadi anggota dewan ambalan di sman 1 sukahaji")

#Komponen Upload File (Gambar)
foto_profil = st.sidebar.file_uploader("Unggah Foto Profil (Opsional)", type=['jpg', 'jpeg', 'png'])

## - AREA UTAMA (MAIN DASHBOARD) -
st.title("🎓 Curriculum Vitae Digital")
st.markdown(" -") # Membuat garis pembatas horizontal

# 3. Membuat Layout 2 Kolom (Kiri untuk Teks, Kanan untuk Foto)
kolom_kiri, kolom_kanan = st.columns([2, 1])
with kolom_kiri:
    # Menampilkan data menggunakan Typography Streamlit
    st.header(nama)
    st.subheader(f"{jurusan} | NIM: {nim}")
    st.write(deskripsi)   
    
with kolom_kanan:
    # Menampilkan foto jika user mengunggahnya
    if foto_profil is not None:
        st.image(foto_profil, width=200, caption="Foto Profil")
    else:
        st.info("Belum ada foto yang diunggah.")

with kolom_kiri:
    st.subheader("Pengalaman Organisasi")
    st.write(pengalaman)
    # TUGAS 3: Checkbox & Text Area Kondisional Magang/Sertifikasi
    punya_magang = st.sidebar.checkbox("Punya Pengalaman Magang/Sertifikasi?")
    detail_magang = ""
    if punya_magang:
        detail_magang = st.sidebar.text_area("Detail Magang / Sertifikasi:")
        
# - BAGIAN KEAHLIAN (SKILLS) -
st.markdown("### ️ Keahlian Teknis")
# Sidebar slider untuk mengatur level skill
st.sidebar.markdown(" -")
st.sidebar.subheader("Atur Kemahiran Skill")
skill_python = st.sidebar.slider("Python", 0, 100)
skill_web = st.sidebar.slider("Web Development", 0, 100)
skill_db = st.sidebar.slider("Database", 0, 100)

# Menampilkan indikator visual (Progress Bar) di halaman utama
st.write(" *Python *")
st.progress(skill_python)
st.write(" *Web Development (HTML/CSS) *")
st.progress(skill_web)
st.write(" *Database (SQL) *")
st.progress(skill_db)

#bagian pengalaman
st.markdown("### Pengalaman Magang / Sertifikasi")
if punya_magang:
    if detail_magang:
        st.success(f"*Detail Pengalaman / Sertifikasi:*\n\n{detail_magang}")
    else:
        st.info("Silakan isi detail pengalaman magang/sertifikasi di sidebar.")
else:
    st.write("Tidak ada pengalaman magang/sertifikasi.")

st.markdown("---")

# - BAGIAN KONTAK -
st.markdown("### 📬 Hubungi Saya")
with st.expander("Klik untuk melihat detail kontak"):
    st.write(f"📧 Email: {nama.lower().replace(' ', '')}muhammadsuyuthiyahya@gmail.com")
    st.write("🔗 LinkedIn: linkedin.com/in/Muhammad Suyuthi Yahya")
    st.write("🐙 GitHub: github.com/sythiyhya")
    
    st.markdown("---")
data_cv = f"Nama: {nama}\nNIM: {nim}\nJurusan: {jurusan}"

st.download_button(
    label="Download Data CV",
    data=data_cv,
    file_name="cv_data.txt",
    mime="text/plain"
)