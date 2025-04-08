# pages/2_BorsaTakibi.py

import streamlit as st
import yfinance as yf
import pandas as pd
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
st.title("📈 Borsa (BIST) Takip Ekranı")
st.markdown("📊 Borsa İstanbul'dan seçili hisselerin anlık fiyatlarını ve grafiklerini inceleyebilirsin.")

# İzlenecek örnek hisseler
bist_stocks = {
    "AKBNK.IS": "Akbank",
    "THYAO.IS": "THY",
    "ASELS.IS": "Aselsan",
    "SISE.IS": "Şişecam",
    "KCHOL.IS": "Koç Holding"
}

for symbol, name in bist_stocks.items():
    try:
        data = yf.download(symbol, period="7d", interval="1h")
        data.dropna(inplace=True)

        if data.empty:
            raise ValueError("Veri alınamadı.")

        # 🔐 Burayı sağlamlaştırdık
        current_price = float(data["Close"].iloc[-1])

        st.subheader(f"📌 {name} ({symbol})")
        st.metric(label="Anlık Fiyat", value=f"{current_price:.2f} ₺")
        st.line_chart(data["Close"])
        st.markdown("---")

    except Exception as e:
        st.error(f"❌ {name} verisi alınamadı: {e}")