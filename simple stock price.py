import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
#simple stock option

shown are the stock **Closing price** and **Volume** of google 

""")
# this is the ticker symbols !
tickersymbol = 'GOOGL'


#here we get data on this ticker 
tickerdata = yf.Ticker(tickersymbol)

# now we get the historical price for this ticker 
tickerdf = tickerdata.history(period = 'id', start= '2010-5-31', end = '2022-5-31')
#open  high  low  close  volume  dividends  stocksplits 

st.line_chart(tickerdf.Close)
st.line_chart(tickerdf.Volume)



