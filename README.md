# 🛍️ E-Commerce Analysis Dashboard

Dashboard ini dibuat menggunakan **Streamlit** untuk memvisualisasikan hasil analisis data e-commerce publik dari Brasil. Terdapat dua fitur utama:
- Visualisasi produk dengan rating tertinggi
- Produk paling populer berdasarkan kota

## 📦 Dataset
Dataset yang digunakan:
- `avg_ratings_sorted.csv`: berisi produk dengan rating tertinggi
- `review_scores_sorted.csv`: berisi kategori rating produk
- `top_produk_per_kota.csv`: produk terpopuler di tiap kota

---

## 🛠️ Setup Environment

### Menggunakan Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Menggunakan Shell / Terminal Biasa
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

## 🚀 Menjalankan Streamlit App
```bash
streamlit run app.py
```

---

## 🌐 Deploy ke Streamlit Cloud
1. Upload semua file ke GitHub:
   - `app.py`
   - `requirements.txt`
   - `avg_ratings_sorted.csv`
   - `review_scores_sorted.csv`
   - `top_produk_per_kota.csv`

2. Buka [https://streamlit.io/cloud](https://streamlit.io/cloud)

3. Login dengan akun GitHub, pilih repo kamu, lalu klik **Deploy**

---

## 👨‍💻 Author
Syamsul Maarip

---

## 📌 Catatan
Visualisasi dibuat menggunakan **Seaborn** dan **Matplotlib**, pastikan dependensi sudah terinstall sebelum menjalankan aplikasi.

```
