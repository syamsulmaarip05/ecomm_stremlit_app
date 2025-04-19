import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analisis E-Commerce", layout="wide")

st.title("📦 Analisis Data E-Commerce Brazil")
st.write("by Syamsul Maarip")

# Load data
avg_ratings_sorted = pd.read_csv("avg_ratings_sorted.csv")
review_scores_sorted = pd.read_csv("review_scores_sorted.csv")
top_produk_per_kota = pd.read_csv("top_produk_per_kota.csv")

# Sidebar untuk navigasi
menu = st.sidebar.radio("Pilih Analisis", ("📊 Rating Produk", "📍 Kota Populer"))

# ================================
# TAB 1: Rating Produk
# ================================
if menu == "📊 Rating Produk":
    st.header("📊 Top Produk dengan Rating Tertinggi")

    st.subheader("Top 10 Produk Berdasarkan Rating")
    top_10 = avg_ratings_sorted.head(10)
    st.dataframe(top_10)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top_10, x='review_score', y='category', palette='Blues_d', ax=ax)
    ax.set_xlabel("Rating")
    ax.set_ylabel("Kategori Produk")
    ax.set_title("Top 10 Produk dengan Rating Tertinggi")
    st.pyplot(fig)

    st.subheader("Distribusi Kategori Rating")
    rating_counts = review_scores_sorted['rating_category'].value_counts()
    st.bar_chart(rating_counts)

# ================================
# TAB 2: Kota Populer
# ================================
elif menu == "📍 Kota Populer":
    st.header("📍 Produk Paling Populer di Masing-masing Kota")

    st.dataframe(top_produk_per_kota.head(10))

    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.barplot(data=top_produk_per_kota.head(10),
                y='geolocation_city',
                x='total_orders',
                hue='product_category_name',
                dodge=False,
                ax=ax2)
    ax2.set_title('Produk Paling Populer di Masing-masing Kota')
    ax2.set_xlabel('Jumlah Pembelian')
    ax2.set_ylabel('Kota')
    st.pyplot(fig2)

st.caption("📌 Data berdasarkan dataset publik e-commerce Brazil")
