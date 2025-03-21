import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:5000"

st.title("📢 News Summarization & Sentiment Analysis")

company = st.text_input("Enter Company Name")

if st.button("Get News"):
    response = requests.get(f"{BASE_URL}/news", params={"company": company})

    if response.status_code == 200:
        data = response.json()
        st.write(f"### News for {data['company']}")

        full_summary = ""

        for article in data["articles"]:
            st.subheader(article["title"])
            st.write(f"**Summary:** {article['summary']}")
            st.write(f"**Sentiment:** {article['sentiment']}")
            st.write(f"[Read more]({article['link']})")
            full_summary += article["summary"] + ". "

        # Send full summary to the API for Hindi TTS
        tts_response = requests.post(f"{BASE_URL}/tts", json={"text": full_summary})
        if tts_response.status_code == 200:
            st.audio("output.mp3", format="audio/mp3")
    else:
        st.error("Error fetching news!")
