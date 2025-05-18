import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.set_page_config(
    page_title="Analisa Rental Sepeda",
    page_icon=":bicycle:",
)

def create_trend_bike(df):
    trend_bike = df.groupby(by='yr').agg({
    'cnt': 'mean'
    }).sort_values(by="yr", ascending=False) # diurutkan berdasarkan tahun
    return trend_bike

def create_comparisson_workingday(df):
    comparisson_workingday=df.groupby(by='workingday').agg({
    'cnt': ['max', 'min', 'mean']
    })
    return comparisson_workingday

# Meload dataset kedalam variabel day_df
day_df = pd.read_csv('dashboard/day_cleaned.csv')

# Menyiapkan dataframe
trend_bike = create_trend_bike(day_df)
comparisson_workingday = create_comparisson_workingday(day_df)

st.title('Dashboard Rental Sepeda ')
tab1, tab2, tab3 = st.tabs(["Pendahuluan", "Data Set", "Chart"])
 
with tab1:
    st.header("Rental Sepeda")
    st.image("dashboard/sepeda.jpg")
    st.write("Sistem berbagi sepeda adalah generasi baru dari penyewaan sepeda tradisional di mana seluruh proses mulai dari keanggotaan, penyewaan, dan pengembalian sepeda menjadi otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari posisi tertentu dan mengembalikannya di posisi lain. Saat ini, terdapat lebih dari 500 program berbagi sepeda di seluruh dunia yang terdiri dari lebih dari 500 ribu sepeda. Saat ini, terdapat minat yang besar terhadap sistem ini karena peran penting mereka dalam masalah lalu lintas, lingkungan dan kesehatan Terlepas dari aplikasi dunia nyata yang menarik dari sistem berbagi sepeda, karakteristik data yang dihasilkan oleh sistem ini membuatnya menarik untuk penelitian. Berbeda dengan layanan transportasi lain seperti bus atau kereta bawah tanah, durasi perjalanan, posisi keberangkatan dan kedatangan secara eksplisit dicatat dalam sistem ini. Fitur ini mengubah sistem berbagi sepeda menjadi jaringan sensor virtual yang dapat digunakan untuk merasakan mobilitas di kota. Dengan demikian, diharapkan sebagian besar kejadian penting di kota dapat dideteksi melalui pemantauan data ini.")
    
 
with tab2:
    st.header("Data Set")
    st.dataframe(data=day_df, width=800, height=500)
    st.write("Proses penyewaan sepeda bersama sangat berkorelasi dengan kondisi lingkungan dan musim. Misalnya, kondisi cuaca, curah hujan, hari dalam seminggu, musim, jam dalam sehari, dan lain-lain dapat mempengaruhi perilaku penyewaan. Kumpulan data inti terkait dengan catatan historis dua tahun yang berhubungan dengan tahun 2011 dan 2012 dari sistem Capital Bikeshare, Washington D.C., Amerika Serikat yang tersedia untuk umum di http://capitalbikeshare.com/system-data. Kami mengumpulkan data tersebut dalam dua basis data per jam dan per hari, kemudian mengekstrak dan menambahkan informasi cuaca dan musim yang sesuai. Informasi cuaca diambil dari http://www.freemeteo.com.")
 
with tab3:
    st.header("Chart Hasil Analisis")
    st.subheader("Tren Jumlah Pengguna Sepeda Dalam Tahun 2011 dan 2012")
    
    trend_bike = trend_bike.reset_index() # Mereset index setiap row nya
    day_df['mnth'] = pd.Categorical(day_df['mnth'], categories=
    ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    ordered=True)

    # Menjumlahkan total cnt dalam setiap bulan nya
    monthly_counts = day_df.groupby(by=["mnth","yr"]).agg({
        "cnt": "sum"
    }).sort_values(by=["yr","mnth"], ascending=False).reset_index()

    # Menentukan garis didalam chart menggunakan library seaborn
   
    sns.lineplot(
        data=monthly_counts,
        x="mnth",
        y="cnt",
        hue="yr",
        palette="deep",
        style="yr",
        marker="o",
        dashes=False)

    # Menambahkan atribut untuk memperjelas chart
    plt.title("Trend Sewa Sepeda")
    plt.xlabel(None)
    plt.ylabel("count of total rental")
    plt.legend(title="Tahun", loc="upper right")
    st.pyplot(plt)
    
    with st.expander("Kesimpulan"):
        st.write("Tren rental sepeda meningkat pada tahun 2012 dari 2011, dan untuk setiap bulannya peningkatan terjadi dalam awal tahun sampai pertengahan tahun, walaupun selalu terjadi penurunan tren setiap akhir tahun dimulai dari bulan october.")
    st.subheader("Perbandingan Penyewa Sepeda Workingday Dan Holiday")
    plt.figure(figsize=(10,6))
    sns.barplot(
        x='workingday',
        y='cnt',
        palette='rocket',
        data=day_df)

    plt.title('Perbandingan Penyewa Sepeda Workingday Dan Holiday')
    plt.xlabel(None)
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(plt)
    with st.expander("Kesimpulan"):
        st.write("Lebih Banyak orang melakukan rental sepeda pada workday dibanding holiday. ini menunjukan bahwa orang suka menggunakan sepeda untuk menjalan kegiatan sehari-hari nya")

