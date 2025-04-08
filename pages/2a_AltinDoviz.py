import streamlit as st
import yfinance as yf
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
st.title("💰 Altın & Döviz Takibi")

assets = {
    "XAUUSD=X": "ONS Altın",
    "EURUSD=X": "Euro / Dolar",
    "USDTRY=X": "Dolar / TL",
    "EURTRY=X": "Euro / TL"
}

for ticker, name in assets.items():
    try:
        data = yf.download(ticker, period="7d", interval="1h")
        data.dropna(inplace=True)
        current_price = data["Close"].iloc[-1].item()

        st.subheader(name)
        st.metric(label="Anlık Fiyat", value=f"{current_price:.2f}")
        st.line_chart(data["Close"])
        st.markdown("---")
    except Exception as e:
        st.error(f"{name} verisi alınamadı: {e}")