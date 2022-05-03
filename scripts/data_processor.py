import pandas_datareader as web
import pandas as pd
import streamlit as st

def get_stock_data(stock_name, start_date=pd.to_datetime('01/01/2020'), end_date=pd.to_datetime('22/06/2020')):
    try:
        df_stock = web.DataReader(stock_name, start=start_date, end=end_date, data_source='yahoo')
        return df_stock
    except:
        n = (end_date - start_date).days
        df = pd.DataFrame(
            dict(
                Open = [1]*n,
                Close = [1]*n,
                High = [1]*n,
                Low = [1]*n
            )
        )
        st.warning('Stock not available')
        return df

def ret_stock(df_stock, price_type='Close'):
    price = df_stock[price_type]
    return (price - price.shift(1)) / price.shift(1)