import streamlit as st

st.title("Park Kontrol Formu")

# Soru etiketi
st.subheader("Lambaların tümü çalışıyor mu?")

# Evet / Hayır seçimi (radio button)
durum = st.radio(
    "Durumu seç:",
    ("Evet", "Hayır")
)

# Açıklama text box
aciklama = st.text_area("Açıklama (isteğe bağlı):")

# Kaydet butonu
if st.button("Kaydet"):
    st.write("**Seçilen Durum:**", durum)
    
    if aciklama.strip():
        st.write("**Açıklama:**", aciklama)
    else:
        st.write("_Açıklama girilmedi._")