import streamlit as st
import yfinance as yf

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
st.title("🔔 Fiyat Alarmı")
st.markdown("Belirlediğin fiyat aralıklarıyla yatırım fırsatlarını kaçırma! ⏰")

# İzlenecek varlıklar
assets = {
    "USDTRY=X": "Dolar / TL",
    "EURTRY=X": "Euro / TL",
    "XAUUSD=X": "ONS Altın",
    "BTC-USD": "Bitcoin",
}

# Kullanıcıdan seçim
selected_ticker = st.selectbox("🔍 İzlemek istediğin varlığı seç", list(assets.keys()), format_func=lambda x: assets[x])

# Fiyat eşiği girişi
col1, col2 = st.columns(2)
with col1:
    min_price = st.number_input("📉 Alt Limit", min_value=0.0, step=0.1)
with col2:
    max_price = st.number_input("📈 Üst Limit", min_value=0.0, step=0.1)

# Fiyat kontrolü
if st.button("🚨 Alarmı Kontrol Et"):
    try:
        data = yf.download(selected_ticker, period="1d", interval="1h")
        current_price = float(data["Close"].iloc[-1])
        st.success(f"🔎 {assets[selected_ticker]} anlık fiyatı: {current_price:.2f}")

        if min_price > 0 and current_price < min_price:
            st.error(f"📉 Fiyat {min_price} ₺ altına düştü! 🟥")
        elif max_price > 0 and current_price > max_price:
            st.warning(f"📈 Fiyat {max_price} ₺ üzerine çıktı! 🟨")
        else:
            st.info("✅ Fiyat belirlenen aralıkta.")

    except Exception as e:
        st.error(f"Veri alınamadı: {e}")