<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:19:44+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "id"
}
-->
# Berkontribusi pada Data Science untuk Pemula

Terima kasih atas minat Anda untuk berkontribusi pada kurikulum Data Science untuk Pemula! Kami menyambut kontribusi dari komunitas.

## Daftar Isi

- [Kode Etik](../..)
- [Bagaimana Saya Bisa Berkontribusi?](../..)
- [Memulai](../..)
- [Panduan Kontribusi](../..)
- [Proses Pull Request](../..)
- [Panduan Gaya](../..)
- [Perjanjian Lisensi Kontributor](../..)

## Kode Etik

Proyek ini telah mengadopsi [Kode Etik Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Untuk informasi lebih lanjut, lihat [FAQ Kode Etik](https://opensource.microsoft.com/codeofconduct/faq/)  
atau hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk pertanyaan atau komentar tambahan.

## Bagaimana Saya Bisa Berkontribusi?

### Melaporkan Bug

Sebelum membuat laporan bug, harap periksa masalah yang sudah ada untuk menghindari duplikasi. Saat membuat laporan bug, sertakan detail sebanyak mungkin:

- **Gunakan judul yang jelas dan deskriptif**
- **Jelaskan langkah-langkah tepat untuk mereproduksi masalah**
- **Berikan contoh spesifik** (potongan kode, tangkapan layar)
- **Jelaskan perilaku yang Anda amati dan apa yang Anda harapkan**
- **Sertakan detail lingkungan Anda** (OS, versi Python, browser)

### Mengusulkan Peningkatan

Usulan peningkatan sangat kami hargai! Saat mengusulkan peningkatan:

- **Gunakan judul yang jelas dan deskriptif**
- **Berikan deskripsi rinci tentang peningkatan yang diusulkan**
- **Jelaskan mengapa peningkatan ini akan berguna**
- **Cantumkan fitur serupa di proyek lain, jika ada**

### Berkontribusi pada Dokumentasi

Perbaikan dokumentasi selalu dihargai:

- **Perbaiki kesalahan ketik dan tata bahasa**
- **Tingkatkan kejelasan penjelasan**
- **Tambahkan dokumentasi yang hilang**
- **Perbarui informasi yang sudah usang**
- **Tambahkan contoh atau kasus penggunaan**

### Berkontribusi pada Kode

Kami menyambut kontribusi kode termasuk:

- **Pelajaran atau latihan baru**
- **Perbaikan bug**
- **Peningkatan pada notebook yang ada**
- **Dataset atau contoh baru**
- **Peningkatan aplikasi kuis**

## Memulai

### Prasyarat

Sebelum berkontribusi, pastikan Anda memiliki:

1. Akun GitHub
2. Git terinstal di sistem Anda
3. Python 3.7+ dan Jupyter terinstal
4. Node.js dan npm (untuk kontribusi aplikasi kuis)
5. Pemahaman tentang struktur kurikulum

Lihat [INSTALLATION.md](INSTALLATION.md) untuk instruksi pengaturan yang lebih rinci.

### Fork dan Clone

1. **Fork repositori** di GitHub  
2. **Clone fork Anda** secara lokal:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Tambahkan upstream remote**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Buat Cabang

Buat cabang baru untuk pekerjaan Anda:  
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Konvensi penamaan cabang:  
- `feature/` - Fitur atau pelajaran baru  
- `fix/` - Perbaikan bug  
- `docs/` - Perubahan dokumentasi  
- `refactor/` - Refaktor kode  

## Panduan Kontribusi

### Untuk Konten Pelajaran

Saat berkontribusi pada pelajaran atau memodifikasi yang sudah ada:

1. **Ikuti struktur yang ada**:
   - README.md dengan konten pelajaran
   - Notebook Jupyter dengan latihan
   - Tugas (jika ada)
   - Tautan ke kuis sebelum dan sesudah

2. **Sertakan elemen-elemen ini**:
   - Tujuan pembelajaran yang jelas
   - Penjelasan langkah demi langkah
   - Contoh kode dengan komentar
   - Latihan untuk praktik
   - Tautan ke sumber daya tambahan

3. **Pastikan aksesibilitas**:
   - Gunakan bahasa yang jelas dan sederhana
   - Berikan teks alternatif untuk gambar
   - Sertakan komentar kode
   - Pertimbangkan gaya belajar yang berbeda

### Untuk Notebook Jupyter

1. **Hapus semua output** sebelum melakukan commit:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Sertakan sel markdown** dengan penjelasan  

3. **Gunakan format yang konsisten**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Uji notebook Anda** sepenuhnya sebelum mengirimkan  

### Untuk Kode Python

Ikuti panduan gaya [PEP 8](https://www.python.org/dev/peps/pep-0008/):  
```python
# Good practices
import pandas as pd

def calculate_mean(data):
    """Calculate the mean of a dataset.
    
    Args:
        data (list): List of numerical values
        
    Returns:
        float: Mean of the dataset
    """
    return sum(data) / len(data)
```
  

### Untuk Kontribusi Aplikasi Kuis

Saat memodifikasi aplikasi kuis:

1. **Uji secara lokal**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Jalankan linter**:  
   ```bash
   npm run lint
   ```
  
3. **Bangun dengan sukses**:  
   ```bash
   npm run build
   ```
  
4. **Ikuti panduan gaya Vue.js** dan pola yang ada  

### Untuk Terjemahan

Saat menambahkan atau memperbarui terjemahan:

1. Ikuti struktur di folder `translations/`  
2. Gunakan kode bahasa sebagai nama folder (misalnya, `fr` untuk bahasa Prancis)  
3. Pertahankan struktur file yang sama seperti versi bahasa Inggris  
4. Perbarui tautan kuis untuk menyertakan parameter bahasa: `?loc=fr`  
5. Uji semua tautan dan format  

## Proses Pull Request

### Sebelum Mengirimkan

1. **Perbarui cabang Anda** dengan perubahan terbaru:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Uji perubahan Anda**:
   - Jalankan semua notebook yang dimodifikasi
   - Uji aplikasi kuis jika dimodifikasi
   - Verifikasi semua tautan berfungsi
   - Periksa kesalahan ejaan dan tata bahasa

3. **Commit perubahan Anda**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Tulis pesan commit yang jelas:
   - Gunakan bentuk present tense ("Tambahkan fitur" bukan "Menambahkan fitur")
   - Gunakan bentuk imperatif ("Pindahkan kursor ke..." bukan "Memindahkan kursor ke...")
   - Batasi baris pertama hingga 72 karakter
   - Referensi masalah dan pull request jika relevan

4. **Push ke fork Anda**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Membuat Pull Request

1. Pergi ke [repositori](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Klik "Pull requests" → "New pull request"  
3. Klik "compare across forks"  
4. Pilih fork dan cabang Anda  
5. Klik "Create pull request"  

### Format Judul PR

Gunakan judul yang jelas dan deskriptif dengan format berikut:  
```
[Component] Brief description
```
  
Contoh:  
- `[Lesson 7] Perbaiki error impor notebook Python`  
- `[Quiz App] Tambahkan terjemahan bahasa Jerman`  
- `[Docs] Perbarui README dengan prasyarat baru`  
- `[Fix] Koreksi jalur data di pelajaran visualisasi`  

### Deskripsi PR

Sertakan dalam deskripsi PR Anda:

- **Apa**: Perubahan apa yang Anda buat?  
- **Mengapa**: Mengapa perubahan ini diperlukan?  
- **Bagaimana**: Bagaimana Anda mengimplementasikan perubahan?  
- **Pengujian**: Bagaimana Anda menguji perubahan?  
- **Tangkapan Layar**: Sertakan tangkapan layar untuk perubahan visual  
- **Masalah Terkait**: Tautkan ke masalah terkait (misalnya, "Fixes #123")  

### Proses Review

1. **Pemeriksaan otomatis** akan dijalankan pada PR Anda  
2. **Pemelihara akan meninjau** kontribusi Anda  
3. **Tanggapi umpan balik** dengan membuat commit tambahan  
4. Setelah disetujui, **pemelihara akan menggabungkan** PR Anda  

### Setelah PR Anda Digabungkan

1. Hapus cabang Anda:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Perbarui fork Anda:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Panduan Gaya

### Markdown

- Gunakan tingkat heading yang konsisten  
- Sertakan baris kosong di antara bagian  
- Gunakan blok kode dengan spesifikasi bahasa:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Tambahkan teks alternatif ke gambar: `![Alt text](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.id.png)`  
- Pertahankan panjang baris yang wajar (sekitar 80-100 karakter)  

### Python

- Ikuti panduan gaya PEP 8  
- Gunakan nama variabel yang bermakna  
- Tambahkan docstring ke fungsi  
- Sertakan petunjuk tipe jika sesuai:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Ikuti panduan gaya Vue.js 2  
- Gunakan konfigurasi ESLint yang disediakan  
- Tulis komponen yang modular dan dapat digunakan kembali  
- Tambahkan komentar untuk logika yang kompleks  

### Organisasi File

- Simpan file yang terkait bersama-sama  
- Gunakan nama file yang deskriptif  
- Ikuti struktur direktori yang ada  
- Jangan commit file yang tidak diperlukan (.DS_Store, .pyc, node_modules, dll.)  

## Perjanjian Lisensi Kontributor

Proyek ini menyambut kontribusi dan saran. Sebagian besar kontribusi mengharuskan Anda  
menyetujui Perjanjian Lisensi Kontributor (CLA) yang menyatakan bahwa Anda memiliki hak untuk,  
dan benar-benar memberikan kami hak untuk menggunakan kontribusi Anda. Untuk detailnya, kunjungi  
https://cla.microsoft.com.

Saat Anda mengirimkan pull request, bot CLA akan secara otomatis menentukan apakah Anda perlu  
memberikan CLA dan menghias PR dengan tepat (misalnya, label, komentar). Cukup ikuti  
instruksi yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali di semua repositori yang menggunakan CLA kami.

## Pertanyaan?

- Periksa [Saluran Discord #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Bergabunglah dengan [komunitas Discord kami](https://aka.ms/ds4beginners/discord)  
- Tinjau [masalah](https://github.com/microsoft/Data-Science-For-Beginners/issues) dan [pull request](https://github.com/microsoft/Data-Science-For-Beginners/pulls) yang ada  

## Terima Kasih!

Kontribusi Anda membuat kurikulum ini lebih baik untuk semua orang. Terima kasih telah meluangkan waktu untuk berkontribusi!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.