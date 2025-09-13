import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📊 Stock Predictor (Simple Version)")

# Dropdown for stock selection
stocks = ["AAPL", "TSLA", "AMZN", "MSFT", "GOOG"]
ticker = st.selectbox("Choose a stock:", stocks)

# Fetch stock data
data = yf.download(ticker, period="6mo")

# Simple trend predictor
if len(data) > 2:
    last_close = data["Close"].iloc[-1]
    prev_close = data["Close"].iloc[-2]

    if last_close > prev_close:
        st.success(f"📈 {ticker} looks like it’s going UP")
    else:
        st.error(f"📉 {ticker} looks like it’s going DOWN")

# Show chart
st.line_chart(data["Close"])

