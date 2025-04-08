import streamlit as st
import feedparser
from bs4 import BeautifulSoup

# Stil dosyası
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🗞️ Gündem Haberleri")
st.markdown("📌 Türkiye ve dünya gündemini güvenilir kaynaklardan takip et!")

rss_feeds = {
    "Sözcü - Son Dakika": "https://www.sozcu.com.tr/feeds-son-dakika",
    "Sözcü - Haberler": "https://www.sozcu.com.tr/feeds-rss-category-haberler",
    "Halk TV": "https://www.halktv.com.tr/service/rss.php",
     "Reuters" : "https://www.reutersagency.com/feed/?taxonomy=best-sectors&post_type=best",
    "Euronews Türkce" :"tr.euronews.com/rss?level=theme&name=news",
    "BBC NEWS": "http://feeds.bbci.co.uk/news/rss.xml"

}

for source, url in rss_feeds.items():
    try:
        feed = feedparser.parse(url)
        st.subheader(f"🌍 {source}")

        if not feed.entries:
            st.warning(f"😴 {source} şu anda haber göndermiyor olabilir.")
            continue

        for entry in feed.entries[:5]:
            title = entry.get("title", "📰 Başlık yok")
            link = entry.get("link", "#")
            summary_raw = entry.get("summary", "")
            published = entry.get("published", "Tarih yok")

            # Özetten görseli ayırmak için HTML'yi parse et
            soup = BeautifulSoup(summary_raw, "html.parser")
            image = soup.find("img")
            text = soup.get_text()

            if image:
                st.image(image["src"], width=150)

            st.markdown(f"🔹 **[{title}]({link})**")
            st.markdown(f"{text}")
            st.markdown(f"📅 {published}")
            st.markdown("---")

    except Exception as e:
        st.error(f"❌ {source} verisi alınamadı: {e}")