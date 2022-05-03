import streamlit as st
import pandas as pd
import scripts.data_processor as dp
from scripts import plotter

st.set_page_config(page_title='Stock Sentiment', layout="wide")

# dashboard styling
with open('static/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

'''
# Stock Sentiment
'''
# initialize stock
c1, c2, c3 = st.columns((2,1,1))
stock_name = c1.text_input('Stock Name', '^JKSE')
start_date = c2.date_input('Start Date', pd.to_datetime('2022/01/01'))
end_date = c3.date_input('End Date', pd.Timestamp.now())
df_stock = dp.get_stock_data(stock_name, start_date, end_date)
ret = dp.ret_stock(df_stock)

# stock metric
c1, c2, c3, c4, c5 = st.columns((1,1,1,1,1))
c1.metric('Return', round(ret[-1], 5))
c2.metric('Expected Return', round(ret.mean(), 5))
c3.metric('Risk', round(ret.std(), 5))
c4.metric('Alpha', round(ret.std(), 5))
c5.metric('Beta', round(ret.std(), 5))

# stock plot
tes=df_stock['Close']
plotter.stock_plots(df_stock, SMA_7=df_stock['Close'].rolling(window=7).mean())

