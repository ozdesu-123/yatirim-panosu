import streamlit as st
from datetime import datetime
yil = datetime.now().year

# ✅ Sayfa ayarları
st.set_page_config(page_title="💜 Yatırım Panosu", layout="wide")

# 🎨 Stil dosyası
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🏠 Başlık ve hoş geldin mesajı
st.title("💜 Hayal ve Yatırım Panosuna Hoş Geldin")
st.markdown("## Finansal yolculuğuna başlamak için mükemmel bir zaman ✨")

# 📋 Bilgilendirme kutusu
st.markdown("""
<div style='background-color:#f0f2f6; padding: 20px; border-radius: 10px; font-size: 16px;'>
✨ Soldaki menüden dilediğin modüle göz at, finansal yolculuğuna yön ver!

- 📦 Portföyüm  
- 💰 Altın & Döviz  
- 📈 Borsa Takibi  
- 🔔 Alarm Sistemi  
- 📰 Ekonomik Haberler  

</div>
""", unsafe_allow_html=True)

# 💭 İlham verici mesaj
st.markdown("""
<div style='text-align: center; margin-top: 30px;'>
    <div style='font-size: 32px; font-weight: bold; margin-bottom: 10px;'>Cebindeki Dünya 💸</div>
    <div style='font-size: 16px; color: #666;'>Hayallerin kadar güzelsin. Birikimlerinle kendine yeni bir dünya kurabilirsin. 🌿</div>
</div>
""", unsafe_allow_html=True)

# 🌸 Footer
st.markdown(f"""
<hr style="margin-top: 50px;">

<div style="background-color: #f3f0f9; padding: 20px; border-radius: 12px; text-align: center; color: #5e4b8b; font-family: 'Arial', sans-serif;">
    <p style="font-size: 14px; margin: 5px;">
        💻 Geliştiren: <a href="https://github.com/mavisoftstudios" style="color: #7b5fa3; text-decoration: none;">Mavi Soft Studios</a> | 
        📷 <a href="https://instagram.com/hayalpanosuapp" style="color: #7b5fa3; text-decoration: none;">@hayalpanosuapp</a> | 
        ☕ <a href="https://buymeacoffee.com/mavisoftstudios" style="color: #7b5fa3; text-decoration: none;">Yol arkadaşım olur musun? 🌙</a>
    </p>
</div>

<hr style='margin-top:30px; margin-bottom:20px; border: none; height: 2px; background: linear-gradient(to right, #f8d6f0, #eecff2, #f8d6f0);'>

<div style='text-align:center; font-family: "Merriweather", serif;'>
    <p style='color:#A45EE5; font-size:14px; animation: pulse 2s infinite;'>
        © {yil} Yatırım Panosu. Tüm hakları saklıdır. 💙
    </p>
    <p style='font-size:12px; color:#999;'>
        “Yatırım Panosu, finansın lavanta kokulu hali.” 💙🌿
    </p>
    <p style='font-size: 12px; color: #bbb; margin-top: 8px;'>
        Bu proje tamamen kişisel geliştirme amacıyla hazırlanmıştır.
    </p>
</div>

<style>
@keyframes pulse {{
  0% {{ opacity: 0.7; }}
  50% {{ opacity: 1; }}
  100% {{ opacity: 0.7; }}
}}
</style>
""", unsafe_allow_html=True)