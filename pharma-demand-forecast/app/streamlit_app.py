
import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

st.title("📊 Pharma Demand Forecasting App")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['date'])
    product = st.selectbox("Select product", sorted(df['product_name'].unique()))
    region = st.selectbox("Select region", sorted(df['region'].unique()))
    sub_df = df[(df['product_name'] == product) & (df['region'] == region)]
    sub_df = sub_df[['date', 'sales_units']].rename(columns={'date': 'ds', 'sales_units': 'y'})

    model = Prophet()
    model.fit(sub_df)

    future = model.make_future_dataframe(periods=12, freq='W')
    forecast = model.predict(future)

    fig = model.plot(forecast)
    st.pyplot(fig)
