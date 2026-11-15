# Bike Sharing Analytics Dashboard

Proyek akhir analisis data menggunakan Bike Sharing Dataset (2011–2012) untuk menganalisis pola penyewaan sepeda berdasarkan musim, tipe pengguna (*casual* vs *registered*), pola jam operasional (hari kerja vs akhir pekan/libur), serta segmentasi waktu operasional (*clustering*).

## Struktur Direktori

* `Dashboard/dashboard.py` : File utama aplikasi dashboard Streamlit
* `Dashboard/main_data.csv` : Dataset bersih yang digunakan oleh dashboard
* `data/day.csv` : Dataset penyewaan sepeda harian
* `data/hour.csv` : Dataset penyewaan sepeda per jam
* `notebook.ipynb` : Notebook proses analisis data lengkap
* `README.md` : Dokumentasi dan panduan menjalankan proyek
* `requirements.txt` : Daftar *library* Python yang dibutuhkan
* `url.txt` : Tautan aplikasi dashboard yang telah di-*deploy* secara publik

## Setup Environment - Virtual Environment

1. Buka terminal atau Command Prompt, lalu arahkan ke direktori utama proyek (`SubmissionFundamental/`).
2. Buat *virtual environment* dengan perintah berikut:
   `python -m venv .venv`
3. Aktifkan *virtual environment*:
   * **Windows (Command Prompt):** `.venv\Scripts\activate`
   * **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
   * **Linux / macOS:** `source .venv/bin/activate`

## Instalasi Dependensi

Pastikan *virtual environment* sudah aktif dan terminal berada di direktori yang memuat berkas `requirements.txt`, kemudian instal seluruh *library* yang dibutuhkan:
`pip install -r requirements.txt`

## Menjalankan Dashboard

Jalankan aplikasi Streamlit sesuai dengan lokasi berkas pada struktur proyek menggunakan perintah berikut:
`streamlit run Dashboard/dashboard.py`

Setelah perintah dijalankan, aplikasi dashboard akan otomatis terbuka di browser pada alamat `http://localhost:8501`.

## Dashboard Online

Aplikasi dashboard yang telah di-*deploy* secara publik dapat diakses melalui tautan yang tercantum pada berkas `url.txt`.
