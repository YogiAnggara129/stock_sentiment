import streamlit as st
import pandas as pd
import numpy as np
import pandas_datareader as web
import plotly.graph_objects as go


st.set_page_config(layout="wide")

'''
# Stock Sentiment
'''

c1, c2 = st.columns((4, 1))

stock_name = st.text_input('Stock Name', '^JKSE')
jci = web.DataReader(stock_name, start='01/01/2020', end='22/06/2020', data_source='yahoo')
# jci_weekly = jci.resample('W').mean()

candlestick_plotly = go.Figure({ 'x':jci.index.tolist(), 'open':jci['Open'], 'high':jci['High'], 'low':jci['Low'], 'close':jci['Close'],  'type': 'candlestick' }).update_layout(margin=dict(l=20, r=20, t=20, b=20))
with c1:
    st.plotly_chart(candlestick_plotly, use_container_width=True )

ret2 = (jci.iloc[-1,:] - jci.iloc[-2,:]) / jci.iloc[-2,:]
ret1 = (jci.iloc[-2,:] - jci.iloc[-3,:]) / jci.iloc[-3,:]

ret = (jci['Close'] - jci['Close'].shift(1)) / jci['Close'].shift(1)

with c2:
    st.metric('Return', round(ret[-1], 5), round(ret[-1], 5) - round(ret[-2], 5))
    st.metric('Expected Return', round(ret.mean(), 5))
    st.metric('Risk', round(ret.std(), 5))


