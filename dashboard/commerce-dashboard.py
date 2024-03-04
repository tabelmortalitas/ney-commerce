#Import all libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import streamlit as st
sns.set(style='dark')

#Load all data
grouped_orders_2017_df = pd.read_csv('grouped_orders_2017.csv', sep=',')
grouped_orders_2018_df = pd.read_csv('grouped_orders_2018.csv',sep=',')
grouped_revenue_2017_df = pd.read_csv('grouped_revenue_2017.csv')
grouped_revenue_2018_df = pd.read_csv('grouped_revenue_2018.csv')
top_sell_df = pd.read_csv('top_sell.csv')
bad_sell_df = pd.read_csv('bad_sell.csv')
top_revenue_df = pd.read_csv('top_revenue.csv')
bad_revenue_df = pd.read_csv('bad_revenue.csv')
rfm = pd.read_csv('rfm.csv')

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://www.pixenli.com/image/fm0aEpMI")
    st.write("For Anything You Want!")

st.title('ney-Commerce :sparkles: \n')

st.header('Performa Pemesanan')
col1, col2 = st.columns(2)

with col1:
    total_orders_2017 = grouped_orders_2017_df.order_id.sum()
    st.metric("Jumlah pesanan tahun 2017", value=total_orders_2017)

with col2:
    total_orders_2018 = grouped_orders_2018_df.order_id.sum()
    st.metric("Jumlah pesanan tahun 2018", value=total_orders_2018)

tab1, tab2 = st.tabs(["2017","2018"])

with tab1:
    st.subheader("Tingkat jumlah pemesanan tahun 2017")
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        grouped_orders_2017_df["order_purchase_timestamp"],
        grouped_orders_2017_df["order_id"],
        marker='o', 
        linewidth=4,
        color="#90CAF9"
    )
    ax.set_ylabel("Jumlah pemesanan")
    ax.set_xlabel("Periode")
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
    with st.expander("See explanation"):
        st.write("Pada tahun 2017 jumlah pemesanan perbulan relatif naik dengan jumlah pemesanan tertinggi pada bulan November.")

with tab2:
    st.subheader("Tingkat jumlah pemesanan tahun 2018")
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        grouped_orders_2018_df["order_purchase_timestamp"],
        grouped_orders_2018_df["order_id"],
        marker='o', 
        linewidth=4,
        color="#90CAF9"
    )
    ax.set_ylabel("Jumlah pemesanan")
    ax.set_xlabel("Periode")
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
    with st.expander("See explanation"):
        st.write("Sementara itu, jumlah pemesanan per bulan pada tahun 2018 relatif menurun dengan jumlah pemesanan paling sedikit pada bulan September dan Oktober.")

st.header('\n Performa Pendapatan')
col1, col2 = st.columns(2)

with col1:
    total_revenue_2017 = grouped_revenue_2017_df.payment_value.sum()
    st.metric("Jumlah pendapatan tahun 2017", value=total_revenue_2017)

with col2:
    total_revenue_2018 = grouped_revenue_2018_df.payment_value.sum().round()
    st.metric("Jumlah pendapatan tahun 2018", value=total_revenue_2018)

tab1, tab2 = st.tabs(["2017","2018"])

with tab1:
    st.subheader("Tingkat pendapatan tahun 2017 (dalam juta)")
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        grouped_revenue_2017_df["order_purchase_timestamp"],
        grouped_revenue_2017_df["payment_value"],
        marker='o', 
        linewidth=4,
        color="#90CAF9"
    )
    ax.set_ylabel("Pendapatan")
    ax.set_xlabel("Periode")
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
    with st.expander("See explanation"):
        st.write("Tingkat pendapatan per bulan pada tahun 2017 relatif naik dengan jumlah pendapatan tertinggi pada bulan November.")

with tab2:
    st.subheader("Tingkat pendapatan tahun 2018 (dalam juta)")
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        grouped_revenue_2018_df["order_purchase_timestamp"],
        grouped_revenue_2018_df["payment_value"],
        marker='o', 
        linewidth=4,
        color="#90CAF9"
    )
    ax.set_ylabel("Pendapatan")
    ax.set_xlabel("Periode")
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
    with st.expander("See explanation"):
        st.write("Sementara itu, pendapatan per bulan pada tahun 2018 relatif turun dengan jumlah pendapatan paling sedikit pada bulan September dan Oktober.")

st.header('\n Performa Kategori Produk')
st.subheader('Kategori Produk Paling Laris dan Tidak')
col1, col2 = st.columns(2)

with col1:
    st.subheader("Kategori Paling Laris")
    fig = plt.figure(figsize=(10,5))
    sns.barplot(
    x="order_id",
    y="product_category_name_english",
    data=top_sell_df.sort_values(by='order_id', ascending=False),
    color="#72BCD4"
    )
    plt.title("10 Kategori produk kurang laris", loc="center", fontsize=20)
    plt.ylabel("Kategori produk")
    plt.xlabel("Jumlah pesanan")
    plt.tick_params(axis='y', labelsize=12)
    st.pyplot(fig)

with col2:
    st.subheader("Kategori Paling Tidak Laris")
    fig = plt.figure(figsize=(10,5))
    sns.barplot(
    x="order_id",
    y="product_category_name_english",
    data=bad_sell_df.sort_values(by='order_id', ascending=True),
    color="#DB5856"
    )
    plt.title("10 Kategori produk kurang laris", loc="center", fontsize=20)
    plt.ylabel("Kategori produk")
    plt.xlabel("Jumlah pesanan")
    plt.tick_params(axis='y', labelsize=12)
    st.pyplot(fig)

with st.expander("See explanation"):
        st.write("Kategori produk paling banyak terjual adalah bed_bath_table sementara paling sedikit terjual adalah security_and_services.")

st.subheader('\n Kategori Produk dengan Pendapatan Terbanyak dan Terendah')
col1, col2 = st.columns(2)

with col1:
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(
        x="payment_value",
        y="product_category_name_english",
        data=top_revenue_df,
        color="#72BCD4"
    )
    plt.title("10 Kategori produk pendapatan terbanyak", loc="center", fontsize=20)
    plt.ylabel("Kategori produk")
    plt.xlabel("Jumlah pendapatan (dalam juta)")
    plt.tick_params(axis='y', labelsize=12)
    st.pyplot(fig)

with col2:
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(
        x="payment_value",
        y="product_category_name_english",
        data=bad_revenue_df.sort_values(by='payment_value', ascending=True),
        color="#DB5856"
        )
    plt.title("10 Kategori produk pendapatan tersedikit", loc="center", fontsize=20)
    plt.ylabel("Kategori produk")
    plt.xlabel("Jumlah pendapatan (dalam juta)")
    plt.tick_params(axis='y', labelsize=12)
    st.pyplot(fig)

with st.expander("See explanation"):
        st.write("Kategori produk dengan pendapatan paling banyak adalah bed_bath_table sementara paling sedikit adalah security_and_services.")

st.header('\n RFM Analysis')
tab1, tab2, tab3 = st.tabs(["Recency","Frequency","Monetary"])

with tab1:
    st.subheader("Recency Analysis")
    colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]
    fig = plt.figure(figsize=(10, 5))

    sns.barplot(y="customer_unique_id", x="recency", data=rfm.sort_values(by="recency", ascending=True).head(5), palette=colors)
    plt.ylabel("customer_unique_id")
    plt.xlabel("recency (days)")
    plt.title("5 Most Recent (days)", loc="center", fontsize=18)
    plt.tick_params(axis ='x', labelsize=15)
    st.pyplot(fig)
    with st.expander("See explanation"):
        st.write("Pembelian kembali pelanggan paling cepat adalah 0 hari, yaitu pada hari yang sama pelanggan melakukan lebih dari satu transaksi.")

with tab2:
    colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]
    fig = plt.figure(figsize=(10, 5))

    sns.barplot(y="customer_unique_id", x="frequency", data=rfm.sort_values(by="frequency", ascending=False).head(5), palette=colors)
    plt.ylabel("customer_unique_id")
    plt.xlabel("frequency")
    plt.title("5 Most Frequent", loc="center", fontsize=18)
    plt.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)
    with st.expander("See explanation"):
        st.write("Pelanggan yang paling sering melakukan pembelian melakukan 17 kali transaksi.")

with tab3:
    colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]
    fig = plt.figure(figsize=(10, 5))

    sns.barplot(y="customer_unique_id", x="monetary", data=rfm.sort_values(by="monetary", ascending=False).head(5), palette=colors)
    plt.ylabel("customer_unique_id")
    plt.xlabel("monetary")
    plt.title("5 Most Monetary", loc="center", fontsize=18)
    plt.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)
    with st.expander("See explanation"):
        st.write("Pelanggan paling banyak menghabiskan uang sebesar 13664.08")

st.caption('Copyright (c) ney-Commerce 2024')