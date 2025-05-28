import streamlit as st
import requests
from datetime import datetime, timedelta

# Set Streamlit page config
st.set_page_config(page_title="Real-time News Summarizer", layout="wide")

# Tabs
tab1, tab2 = st.tabs(["🗞️ Quick Summary", "🌍 Detailed News"])

# ------------------- TAB 1 -------------------
with tab1:
    st.header("Quick International News Summary")

    # User inputs
    col1, col2 = st.columns(2)
    with col1:
        selected_date = st.date_input("Select Date", datetime.today())
    with col2:
        time_range = st.slider("Select Hour Range", 0, 23, (9, 10))

    # Prepare datetime range
    start_time = datetime.combine(selected_date, datetime.min.time()) + timedelta(hours=time_range[0])
    end_time = datetime.combine(selected_date, datetime.min.time()) + timedelta(hours=time_range[1])

    # Summarize button
    if st.button("Summarize News"):
        with st.spinner("Fetching and summarizing news..."):
            response = requests.post("http://localhost:8000/summarize", json={
                "start_time": start_time.isoformat(),
                "end_time": end_time.isoformat()
            })
            if response.status_code == 200:
                data = response.json()
                summaries = data.get("summaries", [])
                for i, summary in enumerate(summaries, 1):
                    st.markdown(f"**{i}.** {summary}")
            else:
                st.error("Error fetching summaries from backend.")

# ------------------- TAB 2 -------------------
with tab2:
    st.header("Detailed News by Country")

    countries = st.multiselect(
        "Select countries of interest:",
        ["US", "UK", "France", "India", "Germany", "Japan", "China"]
    )

    st.markdown("This feature will allow you to view country-specific news in future updates.")

    if st.button("Fetch Country News"):
        st.info("Backend integration for country-level summaries is under development.")
