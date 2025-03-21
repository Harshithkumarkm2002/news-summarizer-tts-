from flask import Flask, request, jsonify
from utils import extract_news, analyze_sentiment, generate_tts

app = Flask(__name__)

@app.route("/news", methods=["GET"])
def get_news():
    """API to fetch news and analyze sentiment."""
    company = request.args.get("company")
    if not company:
        return jsonify({"error": "Company name is required"}), 400

    articles = extract_news(company)
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["title"])

    return jsonify({"company": company, "articles": articles})

@app.route("/tts", methods=["POST"])
def text_to_speech():
    """API to convert text to Hindi speech."""
    data = request.json
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "Text required"}), 400

    filename = generate_tts(text)
    return jsonify({"audio_file": filename})

if __name__ == "__main__":
    app.run(debug=True)
