# 🌍 Real-time News Summarizer with LLMs

A two-tabbed Streamlit + FastAPI application that fetches international news headlines in real time and summarizes them using Hugging Face Transformers.

---

## 🔧 Features

- 🗞️ **Quick Summary Tab**  
  Select a date and hour range to get summarized international news headlines.

- 🌐 **Detailed News Tab**  
  (WIP) Select specific countries to view country-wise news summaries.

- 🧠 **LLM-Powered Summarization**  
  Uses Hugging Face `flan-t5-base` (runs on CPU) for summarizing titles.

- 🔌 **FastAPI Backend**  
  Handles news fetching and model inference.

- 💡 **NewsData API**  
  Real-time international news fetched via [https://newsdata.io](https://newsdata.io)

---

## 📁 Project Structure

real_time_news_summarizer/
├── backend/
│ ├── main.py # FastAPI app
│ ├── summarizer.py # Summarization logic using HuggingFace
│ ├── news_fetcher.py # NewsData API integration
│ ├── models/ # (Unused if using HuggingFace)
│ └── config/.env # API key
│
├── frontend/
│ └── app.py # Streamlit UI with two tabs
│
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/news-summarizer.git
cd news-summarizer
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set up API key
Create a .env file in the root folder:

ini
Copy
Edit
NEWSDATA_API_KEY=your_newsdata_api_key_here
🔑 Get a free API key at https://newsdata.io

4. Run the FastAPI backend
bash
Copy
Edit
uvicorn backend.main:app --reload
5. Run the Streamlit frontend
bash
Copy
Edit
streamlit run frontend/app.py