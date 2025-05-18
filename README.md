# 📊 Dashboard Analisis Rental Sepeda 🚴

Dashboard ini dibuat menggunakan Python dan Streamlit untuk melakukan analisis terhadap data penyewaan sepeda dari sistem **Capital Bikeshare** di Washington D.C.

## 🧠 Fitur Dashboard
- Visualisasi **tren penyewaan sepeda** berdasarkan bulan dan tahun.
- Analisis perbandingan jumlah penyewa antara **hari kerja (working day)** dan **hari libur**.
- Penyajian data dalam bentuk tabel dan grafik interaktif.
- Penjelasan naratif dan kesimpulan dari hasil visualisasi.

---

## ⚙️ Setup Environment

### Opsi 1 — Menggunakan Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Opsi 2 — Menggunakan Pipenv
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Dashboard
Setelah semua dependensi terinstal, jalankan aplikasi dashboard Streamlit dengan perintah berikut:

```bash
cd dashboard
streamlit run dashboard.py
```

---

## 🗃 Struktur Folder
```
submission/
├── dashboard/
│   ├── dashboard.py              # Script utama Streamlit
│   ├── main_data.csv             # Dataset utama untuk analisis
│   └── data/
│       ├── data_1.csv            # Dataset tambahan 
│       └── data_2.csv            # Dataset tambahan 
├── notebook.ipynb                # Proses analisis dan eksplorasi data
├── requirements.txt              # Daftar library yang digunakan
├── README.md                     # Dokumentasi proyek
└── url.txt                       # Tautan ke dashboard online
```

---

## 🔍 Insight dan Analisis
Pastikan file `notebook.ipynb` sudah dijalankan dan memuat:
- Proses **data gathering**, **cleaning**, dan **exploratory data analysis (EDA)**.
- Visualisasi dengan penjelasan di setiap tahap dalam format markdown.
- Insight yang didapat dari hasil analisis.

---

## 🌐 Tautan Dashboard 
Silakan lihat file `url.txt` untuk mengakses dashboard online (menggunakan Streamlit Cloud).

---

## 📝 Catatan Tambahan
- Dashboard ini dibuat untuk keperluan submission analisis data.
- Visualisasi mengikuti prinsip desain yang jelas, interaktif, dan informatif.
- File ini merupakan bagian dari proyek yang dikemas dalam format ZIP sebelum dikirim.