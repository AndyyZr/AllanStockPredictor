import streamlit as st
import yfinance as yf

st.title("📊 Stock Predictor")

# Full S&P 500 tickers list
sp500_stocks = [
    "AAPL","MSFT","AMZN","GOOG","TSLA","META","NVDA","BRK.B","JPM","UNH","V",
    "XOM","JNJ","WMT","LLY","PG","MA","HD","CVX","MRK","ABBV","PEP","KO","BAC",
    "AVGO","PFE","COST","ADBE","TMO","CSCO","DIS","MCD","ACN","DHR","VZ","NFLX",
    "WFC","ABT","LIN","NKE","TXN","PM","INTC","NEE","RTX","HON","UPS","MS","UNP",
    "IBM","AMGN","CAT","LOW","BA","GS","AMD","MDT","CVS","BLK","AXP","SCHW","NOW",
    "AMT","QCOM","SPGI","T","PLD","COP","DE","LMT","BKNG","ADI","SYK","ELV","INTU",
    "ISRG","GE","MDLZ","VRTX","C","ETN","ADP","ZTS","REGN","MU","MMC","SO","PGR",
    "TJX","GILD","PNC","CL","USB","BDX","CI","CB","MO","APD","DUK","TGT","CSX",
    "NSC","ICE","CME","EOG","FCX","HUM","EQIX","ITW","SHW","WM","NOC","ORLY","PSX",
    "FISV","MRNA","EMR","MCO","AON","GD","AEP","FDX","SLB","PXD","CCI","HCA","EW",
    "MAR","ROP","MPC","MSI","ETR","ALL","TRV","PSA","KDP","KMB","AIG","OXY","CLX",
    "D","AZO","ADM","PEG","SRE","LHX","WMB","STZ","EXC","VLO","DOW","CMI","KMI",
    "PRU","KR","APH","VICI","IDXX","MTD","CTAS","ORCL","HLT","PAYX","MSCI","DHI",
    "WELL","LRCX","AFL","PCAR","COF","ROST","YUM","DD","HPQ","HES","XEL","CTVA",
    "ODFL","F","TEL","OTIS","GIS","AMP","WEC","PPG","MNST","RCL","HIG","NEM",
    "BIIB","A","GWW","DLR","CARR","CHTR","FAST","WBD","WBA","SYY","EFX","KHC",
    "STT","AME","LEN","MTB","OKE","NUE","MSCI","KEYS","ZBH","HAL","VRSK","TSCO",
    "LH","PAYC","IRM","FITB","LYB","ECL","MKC","BLL","DTE","CMS","AWK","CE",
    "HBAN","NDAQ","TER","SYF","SWK","GRMN","RMD","CFG","EXPE","HPE","NTRS",
    "VTRS","GNRC","XYL","ANET","UAL","BBY","LUV","RJF","MCK","CF","WAT","CPRT",
    "CINF","HOLX","TSN","ALB","FMC","AAP","BEN","HSY","UAL","PPL","CNP","AES",
    "PFG","KEY","K","LKQ","WRB","NRG","VFC","TSLA","META"  # and more (list continues)
]

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
