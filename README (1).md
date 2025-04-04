📰 News Summarization & Hindi TTS Application
🚀 A web-based application that extracts news articles, analyzes sentiment, and converts summaries into Hindi speech.

GitHub Repository: "https://github.com/Harshithkumarkm2002/news-summarizer-tts-"
Hugging Face Deployment: "https://huggingface.co/spaces/harshithk288/news-summarizer-tts/tree/main"
Video Demo: "https://drive.google.com/file/d/1dQfFt2UiEW2NYy8cpvQdmRgtTo6AsrL0/view?usp=drive_link"

📌 Features
✅ Extracts top 10 news articles related to a company
✅ Performs sentiment analysis (Positive, Negative, Neutral)
✅ Comparative Analysis of multiple articles
✅ Generates Hindi audio output using TTS
✅ User-friendly interface with Streamlit
✅ API-based architecture for smooth communication
✅ Deployed on Hugging Face Spaces


📌 Installation Guide
🔹 1. Clone the Repository
    
    git clone https://github.com/yourusername/news-summarizer-tts.git
    cd news-summarizer-tts

🔹 2. Create a Virtual Environment
    
    python -m venv venv
    source venv/bin/activate  # On Mac/Linux
    venv\Scripts\activate     # On Windows
    
🔹 3. Install Dependencies

    pip install -r requirements.txt

🔹 4. Run the Application

    streamlit run app.py

📌 API Endpoints
Method	Endpoint	Description
GET	/fetch_news?company=Tesla	Fetches top 10 news articles
POST	/analyze_sentiment	Returns sentiment analysis of articles
POST	/generate_tts	Converts summary to Hindi speech


📌 Project Structure

📂 news-summarizer-tts

 ├── 📜 app.py               # Streamlit Frontend
 
 ├── 📜 api.py               # Backend API
 
 ├── 📜 utils.py             # Helper functions (Scraping, NLP, TTS)
 
 ├── 📜 requirements.txt     # Dependencies
 
 ├── 📜 README.md            # Documentation
 
 └── 📂 data/                # (Optional) Store fetched articles
 
📌 Assumptions & Limitations
🔹 Scraping only works for non-JS websites
🔹 Hindi TTS output is limited to summaries
🔹 API rate limits may affect performance

📌 Deployment on Hugging Face Spaces
1️⃣ Go to Hugging Face Spaces
2️⃣ Create a new Space → Select Streamlit
3️⃣ Upload your files (app.py, api.py, utils.py, requirements.txt)
4️⃣ Click Deploy → Wait for build to finish
5️⃣ App is live! 🎉



📌 License
This project is open-source and available under the MIT License.
