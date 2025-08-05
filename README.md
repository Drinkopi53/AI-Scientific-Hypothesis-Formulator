# AI Scientific Hypothesis Formulator

## Deskripsi
AI Scientific Hypothesis Formulator adalah program baris perintah inovatif yang dirancang untuk membantu para peneliti mempercepat penemuan ilmiah. Dengan menganalisis sekumpulan besar makalah penelitian dalam format PDF, aplikasi ini menggunakan teknik pemrosesan bahasa alami (NLP) dasar untuk mengidentifikasi konsep-konsep kunci dan menyarankan hipotesis baru yang belum pernah diuji.

Proyek ini berfungsi sebagai Produk Minimum yang Layak (MVP) untuk memvalidasi konsep inti dari pembuatan hipotesis otomatis dari literatur ilmiah yang ada.

## Fitur Utama
- **Pemrosesan PDF**: Secara otomatis memindai direktori, membaca, dan mengekstrak teks dari beberapa file PDF.
- **Ekstraksi Konsep**: Menggunakan model TF-IDF untuk mengidentifikasi istilah dan konsep kunci dari teks yang diekstraksi.
- **Generasi Hipotesis**: Merumuskan hipotesis baru dengan menemukan hubungan potensial antara konsep-konsep kunci menggunakan templat yang dapat disesuaikan.
- **Antarmuka Baris Perintah (CLI)**: Antarmuka yang mudah digunakan untuk menjalankan program, menentukan direktori input, dan mengatur jumlah hipotesis yang akan dihasilkan.
- **Modular dan Dapat Diperluas**: Kode disusun menjadi modul-modul terpisah untuk pemrosesan data, generasi hipotesis, dan pembuatan data uji.

## Teknologi yang Digunakan
- **Python 3**: Bahasa pemrograman inti.
- **PyPDF2**: Untuk membaca dan mengekstrak teks dari file PDF.
- **scikit-learn**: Untuk menerapkan model TF-IDF untuk ekstraksi kata kunci.
- **reportlab**: Untuk secara terprogram menghasilkan file PDF uji.

## Instalasi
Untuk menyiapkan proyek ini secara lokal, ikuti langkah-langkah berikut:

1. **Kloning Repositori**
   ```bash
   git clone https://github.com/username/AI-Scientific-Hypothesis-Formulator.git
   cd AI-Scientific-Hypothesis-Formulator
   ```

2. **Buat Lingkungan Virtual (Disarankan)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   *Catatan: Di Windows, gunakan `venv\Scripts\activate`.*

3. **Instal Dependensi**
   Semua dependensi yang diperlukan tercantum dalam file `requirements.txt`. Instal dengan pip:
   ```bash
   pip install -r requirements.txt
   ```

## Penggunaan
Setelah instalasi, Anda dapat menjalankan program dari baris perintah.

1. **Siapkan Makalah Anda**
   Tempatkan semua makalah penelitian PDF yang ingin Anda analisis ke dalam satu direktori (misalnya, `papers/`). Jika direktori tersebut tidak ada, buatlah:
   ```bash
   mkdir papers
   ```

2. **Jalankan Program**
   Gunakan skrip `main.py` untuk memulai proses. Anda harus memberikan path ke direktori makalah Anda.
   ```bash
   python3 src/main.py papers/
   ```

3. **Sesuaikan Jumlah Hipotesis**
   Anda dapat menentukan jumlah hipotesis yang akan dihasilkan menggunakan flag `--num_hypotheses`.
   ```bash
   python3 src/main.py papers/ --num_hypotheses 10
   ```

## Kontribusi
Kontribusi untuk proyek ini sangat diharapkan! Jika Anda ingin berkontribusi, silakan fork repositori dan ajukan pull request.

Untuk perubahan besar, harap buka isu terlebih dahulu untuk mendiskusikan apa yang ingin Anda ubah.

## Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.
