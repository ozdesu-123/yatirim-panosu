import streamlit as st
import feedparser
from datetime import datetime
from dateutil import parser as dateparser
from dateutil.relativedelta import relativedelta

# Stil dosyasını uygula
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📰 Ekonomik Haber Köşesi")
st.markdown("💡 Tarafsız ve güvenilir kaynaklardan ekonomik gelişmeleri oku. Bilgi = Güç!")

rss_feeds = {
    "ParaAnaliz": "https://www.paraanaliz.com/feed",
    "Gazete Duvar Ekonomi": "https://www.gazeteduvar.com.tr/rss/ekonomi.xml",
    "Dünya Gazetesi": "https://www.dunya.com/rss/ekonomi.xml",
    "T24 Ekonomi": "https://t24.com.tr/rss/ekonomi.xml",
    "Euronews Türkçe": "https://tr.euronews.com/rss?level=theme&name=news"
}

def time_ago(published_str):
    try:
        published = dateparser.parse(published_str)
        now = datetime.now(published.tzinfo)
        delta = relativedelta(now, published)
        if delta.years:
            return f"{delta.years} yıl önce"
        elif delta.months:
            return f"{delta.months} ay önce"
        elif delta.days:
            return f"{delta.days} gün önce"
        elif delta.hours:
            return f"{delta.hours} saat önce"
        elif delta.minutes:
            return f"{delta.minutes} dakika önce"
        else:
            return "Az önce"
    except:
        return "Zaman bilinmiyor"

for source, url in rss_feeds.items():
    try:
        feed = feedparser.parse(url)
        st.markdown(f"<h3 style='color:#003f5c;'>🗞️ {source}</h3>", unsafe_allow_html=True)

        if not feed.entries:
            st.warning(f"😴 {source} şu an haber göndermiyor gibi görünüyor.")
            continue

        for entry in feed.entries[:5]:
            published = entry.get("published", "Tarih yok")
            summary = entry.get("summary", "💬 Özet bulunamadı.")

            st.markdown(f"""
            <div style='background-color: #ffffff; border-radius: 10px; padding: 16px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
                <h4 style='margin-bottom: 10px;'><a href="{entry.link}" target="_blank" style='text-decoration: none; color: #2f855a;'>{entry.title}</a></h4>
                <p style='color:#333;'>{summary}</p>
                <div style='font-size: 13px; color: #888; margin-top: 10px;'>📅 {time_ago(published)}</div>
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ {source} verisi alınamadı: {e}")