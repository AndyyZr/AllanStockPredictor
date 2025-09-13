import streamlit as st
import yfinance as yf
import pandas as pd
import requests

st.title("📊 Stock Predictor")

# Get list of S&P 500 tickers
@st.cache_data
def load_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables = pd.read_html(url)
    df = tables[0]
    return df["Symbol"].tolist()

tickers = load_sp500_tickers()

# Dropdown for all S&P 500 stocks
ticker = st.selectbox("Choose a stock:", tickers)

if st.button("Predict"):
    data = yf.download(ticker, period="6mo")

    if data.empty:
        st.error("⚠️ No data found for this stock.")
    else:
        last_close = data["Close"].iloc[-1]
        prev_close = data["Close"].iloc[-2]

        if last_close > prev_close:
            st.success(f"📈 {ticker} looks like it’s going UP")
        else:
            st.error(f"📉 {ticker} looks like it’s going DOWN")

        st.line_chart(data["Close"])
