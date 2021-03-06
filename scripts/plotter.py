import plotly.graph_objects as go
import streamlit as st
import sys
from plotly.subplots import make_subplots
from streamlit import cli as stcli

def stock_plots(df_stock, **df_args):
    date = df_stock.index.tolist()
    # fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
            vertical_spacing=0.05, subplot_titles=('', 'Volume'), 
            row_width=[0.25, 0.7])

    fig.add_trace(go.Candlestick(
        x=date,
        open=df_stock['Open'],
        high=df_stock['High'],
        low=df_stock['Low'],
        close=df_stock['Close'],
        showlegend=False
    ), row=1, col=1)

    fig.add_trace(go.Bar(x=date, y=df_stock['Volume'], showlegend=False), row=2, col=1)

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(x=0.90,y=0.95)
    )

    fig.update(layout_xaxis_rangeslider_visible=False)

    for key, df in df_args.items():
        if len(df.index) == 0:
            continue
        date_temp = df.index.tolist()
        fig.add_trace(go.Scatter(
            name=key,
            x=date_temp,
            y=df
        ), row=1, col=1)

    return st.plotly_chart(fig, use_container_width=True)

if __name__ == '__main__':
    import pandas as pd
    df_test =  pd.DataFrame(
        dict(
            Open = [1]*10,
            Close = [1]*10,
            High = [1]*10,
            Low = [1]*10,
            Volume = [1]*10
        )
    )
    if st._is_running_with_streamlit:
        stock_plots(df_test)
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())