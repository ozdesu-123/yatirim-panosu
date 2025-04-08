import streamlit as st
import yfinance as yf
import pandas as pd
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sayfa ayarları
st.title("📊 Portföy Takip Ekranı")
st.markdown("💼 Yatırımlarının güncel durumunu kolayca takip et. Alım fiyatını ve miktarı gir, anlık K/Z durumunu gör!")

# 🎯 Takip edilecek varlıklar
assets = {
    "GAUTRY=X": "Gram Altın",
    "USDTRY=X": "Dolar / TL",
    "EURTRY=X": "Euro / TL"
}

# 🧾 Kullanıcıdan portföy verisi alma
st.sidebar.header("📩 Portföy Girişi")
portfolio = {}

for ticker, name in assets.items():
    with st.sidebar.expander(f"🪙 {name}"):
        buy_price = st.number_input(f"Alış Fiyatı ({name})", min_value=0.0, step=0.01, key=f"buy_{ticker}")
        quantity = st.number_input(f"Miktar ({name})", min_value=0.0, step=0.01, key=f"qty_{ticker}")
        portfolio[ticker] = {"buy_price": buy_price, "quantity": quantity}

st.markdown("___")

# 📈 Her varlık için veri çek ve göster
for ticker, name in assets.items():
    try:
        # Veriyi yfinance üzerinden çek
        data = yf.download(ticker, period="7d", interval="1h")
        data.dropna(inplace=True)

        if data.empty:
            raise ValueError("Veri seti boş, veri alınamadı.")

        # ✅ Son fiyatı al
        current_price = float(data["Close"].iloc[-1])
        # Kullanıcı girdileri
        buy_price = portfolio[ticker]["buy_price"]
        quantity = portfolio[ticker]["quantity"]

        # 📊 Anlık veriler
        st.subheader(f"📈 {name}")
        st.metric(label="Anlık Fiyat", value=f"{current_price:.2f} ₺")

        if buy_price > 0 and quantity > 0:
            cost = buy_price * quantity
            current_value = current_price * quantity
            profit = current_value - cost
            profit_color = "green" if profit >= 0 else "red"
            emoji = "🟢" if profit >= 0 else "🔴"

            st.markdown(
                f"""
                💰 **Toplam Değer:** {current_value:.2f} ₺  
                📦 **Maliyet:** {cost:.2f} ₺  
                📊 **K/Z:** <span style='color:{profit_color}; font-weight:bold;'>{emoji} {profit:.2f} ₺</span>
                """,
                unsafe_allow_html=True
            )

        # 🧮 Fiyat grafiği
        st.line_chart(data["Close"])
        st.markdown("----")

    except Exception as e:
        st.error(f"❌ {name} verisi alınamadı: {e}")