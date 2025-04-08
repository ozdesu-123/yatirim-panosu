import streamlit as st
import json
import os
from datetime import datetime, date
import pandas as pd

# 🎨 CSS stilini yükle
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🛠️ Sayfa ayarları
st.title("💸 Cüzdanım+ – Gelir Gider Takibi")

# 📁 Veri dosyası yolu
DATA_FILE = "pages/veriler/cuzdanim_veri.json"

# 📦 JSON dosyası yoksa oluştur
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# 📤 Veri kaydet
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# 📥 Veri yükle
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# ➕ Yeni kayıt formu
st.subheader("📥 Yeni Kayıt Ekle")
with st.form("kayıt_formu"):
    col1, col2, col3 = st.columns(3)
    with col1:
        tur = st.radio("İşlem Türü", ["Gelir", "Gider"])
    with col2:
        kategori = st.text_input("Kategori (örn: Maaş, Market)")
    with col3:
        tutar = st.number_input("Tutar (₺)", min_value=0.0, step=1.0)

    aciklama = st.text_area("Açıklama (isteğe bağlı)")
    tarih = st.date_input("Tarih", value=date.today())
    gönder = st.form_submit_button("💾 Kaydet")

    if gönder:
        data = load_data()
        yeni_kayit = {
            "id": datetime.now().strftime("%Y%m%d%H%M%S"),
            "tarih": str(tarih),
            "tur": tur,
            "kategori": kategori,
            "tutar": tutar,
            "aciklama": aciklama
        }
        data.append(yeni_kayit)
        save_data(data)
        st.success("✅ Kayıt eklendi!")
        st.experimental_rerun()

# 📋 Kayıtları Listele
st.subheader("📊 Kayıtlarım")
data = load_data()

if data:
    for i, entry in enumerate(data):
        col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])
        with col1:
            st.markdown(f"📅 **{entry['tarih']}**")
        with col2:
            st.markdown(f"📂 **{entry['kategori']}**")
        with col3:
            st.markdown(f"💰 **{entry['tutar']} ₺**")
        with col4:
            st.markdown(f"🧾 **{entry['tur']}**")
        with col5:
            if st.button("🗑️", key=f"sil_{i}"):
                data.pop(i)
                save_data(data)
                st.success("❌ Kayıt silindi!")
                st.rerun()

    # 📈 Aylık Gelir-Gider Özeti
    st.subheader("📈 Aylık Gelir-Gider Özeti")
    df = pd.DataFrame(data)
    df["tarih"] = pd.to_datetime(df["tarih"])
    df["ay"] = df["tarih"].dt.to_period("M").astype(str)
    summary = df.groupby(["ay", "tur"])["tutar"].sum().unstack().fillna(0)
    st.bar_chart(summary)
else:
    st.info("Henüz bir kayıt yok. Yukarıdan eklemeyi deneyebilirsin.")

# 👣 Alt Bilgi
st.markdown("""
<hr style="border: 1px solid #ccc; margin-top: 40px;">
<div style='text-align: center; color: gray;'>Mavi Soft Studios • Cüzdanım+ 💰</div>
""", unsafe_allow_html=True)