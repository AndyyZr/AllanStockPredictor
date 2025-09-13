import streamlit as st
import yfinance as yf
from sp500 import sp500_stocks  # import the list from sp500.py

st.title("📊 Stock Predictor")

ticker = st.selectbox("Choose a stock:", sp500_stocks)

if st.button("Predict"):
    try:
        data = yf.download(ticker, period="6mo")
        if data.empty:
            st.error("⚠️ No data found.")
        else:
            last_close = data["Close"].iloc[-1]
            prev_close = data["Close"].iloc[-2]

            if last_close > prev_close:
                st.success(f"📈 {ticker} looks like it’s going UP")
            else:
                st.error(f"📉 {ticker} looks like it’s going DOWN")

            st.line_chart(data["Close"])
    except Exception as e:
        st.error(f"❌ Error: {e}")
