import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from gtts import gTTS
import os

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

from gnews import GNews

news_api = GNews(language="en", country="US", max_results=10)

def extract_news(company):
    """Fetch news articles using GNews API"""
    articles = news_api.get_news(company)

    if not articles:
        return []

    extracted_articles = []
    for article in articles:
        extracted_articles.append({
            "title": article["title"],
            "summary": article["description"],
            "link": article["url"]
        })

    return extracted_articles


def analyze_sentiment(text):
    """Perform sentiment analysis."""
    sentiment_score = sia.polarity_scores(text)["compound"]
    if sentiment_score > 0.05:
        return "Positive"
    elif sentiment_score < -0.05:
        return "Negative"
    else:
        return "Neutral"

from googletrans import Translator
from gtts import gTTS

translator = Translator()

def generate_tts(text, filename="output.mp3"):
    """Translate English text to Hindi and convert to speech."""
    translated_text = translator.translate(text, src="en", dest="hi").text
    tts = gTTS(text=translated_text, lang="hi", slow=False)
    tts.save(filename)
    return filename
