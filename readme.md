📊 Data Quality Dashboard

Data Quality Dashboard adalah aplikasi interaktif berbasis Streamlit yang dirancang untuk membantu pengguna dalam memantau dan mengevaluasi kualitas dataset berbentuk CSV. Dashboard ini menekankan Data Quality Score dengan tiga metrik inti: Accuracy, Completeness, dan Timeliness, sekaligus menyajikan visualisasi interaktif untuk pemahaman cepat.

🔹 Tujuan Proyek

Data yang berkualitas adalah fondasi dari analisis yang akurat dan pengambilan keputusan yang tepat. Proyek ini bertujuan untuk:
1. Memberikan penilaian objektif terhadap kualitas dataset.
2. Memvisualisasikan persentase kualitas data agar mudah dipahami.
3. Membantu pengguna mengidentifikasi area perbaikan, misalnya kolom dengan banyak missing value atau data yang sudah usang.
4. Menyediakan alat yang mudah digunakan tanpa memerlukan coding untuk pengguna non-teknis.

🔹 Fitur Utama

1. Upload CSV – Unggah file CSV dan lihat pratinjau data secara instan.
2. Perhitungan Data Quality Score:
3. Accuracy – Rasio data valid (non-missing) terhadap total sel dataset.
4. Completeness – Rasio data non-null terhadap total sel.
5. Timeliness – Persentase data yang terbaru dalam 30 hari terakhir (opsional, jika ada kolom timestamp).
6. Visualisasi Interaktif – Menampilkan Data Quality Score dalam grafik batang dengan persentase.
7. Responsif dan Interaktif – Bisa dijalankan di browser dengan kontrol slider untuk filter data.
8. Dashboard Insight – Cepat menilai kesehatan dataset sebelum proses analisis atau modelisasi.

🔹 Alur Kerja Dashboard

Upload CSV – Pengguna memilih file CSV dari perangkat lokal.

Pra-pemrosesan Data – Aplikasi secara otomatis mengisi missing values (opsional) dan mengubah kolom tanggal menjadi format datetime.

Perhitungan Metrik – Menghitung Accuracy, Completeness, dan Timeliness:

Accuracy = 1 – (jumlah sel missing / total sel)

Completeness = (jumlah sel non-null / total sel)

Timeliness = persentase data dalam 30 hari terakhir

Visualisasi Interaktif – Tampilkan bar chart dengan persentase dari setiap metrik.

Analisis Lanjutan – Bisa melihat metrik per kolom untuk menemukan area perbaikan data.

🔹 Instalasi

Clone repository:

git clone https://github.com/username/data-quality-dashboard.git
cd data-quality-dashboard

Buat virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/MacOS
venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

Dependencies utama: streamlit, pandas, plotly

🔹 Cara Menjalankan

Jalankan aplikasi Streamlit:

streamlit run dq_dashboard.py

Aplikasi akan terbuka di browser pada URL: http://localhost:8501.

Upload CSV, dan dashboard akan otomatis menampilkan Data Quality Score dan visualisasi.

🔹 Contoh Screenshot dan Visualisasi
Preview Data

Tampilan pratinjau dataset setelah upload CSV:


Data Quality Scores

Grafik batang interaktif menampilkan persentase Accuracy, Completeness, Timeliness:


Timeliness Trend

Jika tersedia kolom timestamp, visualisasi persentase data terbaru dalam 30 hari terakhir:


🔹 Format CSV yang Didukung

File harus CSV.

Kolom numerik atau teks untuk evaluasi accuracy dan completeness.

Kolom opsional: timestamp (untuk evaluasi timeliness).

🔹 Struktur Project
data-quality-dashboard/
│
├─ dq_dashboard.py          # File utama Streamlit
├─ requirements.txt         # Daftar package Python
├─ README.md                # Dokumentasi project
├─ assets/                  # Folder untuk GIF/screenshot demo
│   ├─ demo.gif
│   ├─ bar_chart_example.png
│   ├─ timeliness_example.png
│   └─ preview_data.png
└─ data/                    # Folder opsional untuk CSV contoh
🔹 Manfaat Proyek

Non-teknisi: Mudah digunakan untuk menilai dataset tanpa coding.

Analis Data: Mengetahui kualitas dataset sebelum memproses analisis atau model prediksi.

Manajemen Data: Membantu mengidentifikasi kolom dengan masalah missing atau data lama.

🔹 Lisensi

MIT License – Bebas digunakan, dimodifikasi, dan dibagikan.