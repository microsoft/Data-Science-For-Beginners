<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:30:52+00:00",
  "source_file": "AGENTS.md",
  "language_code": "id"
}
-->
# AGENTS.md

## Gambaran Proyek

Data Science for Beginners adalah kurikulum komprehensif selama 10 minggu dengan 20 pelajaran yang dibuat oleh Microsoft Azure Cloud Advocates. Repositori ini merupakan sumber pembelajaran yang mengajarkan konsep dasar ilmu data melalui pelajaran berbasis proyek, termasuk notebook Jupyter, kuis interaktif, dan tugas praktis.

**Teknologi Utama:**
- **Jupyter Notebooks**: Media pembelajaran utama menggunakan Python 3
- **Library Python**: pandas, numpy, matplotlib untuk analisis dan visualisasi data
- **Vue.js 2**: Aplikasi kuis (folder quiz-app)
- **Docsify**: Generator situs dokumentasi untuk akses offline
- **Node.js/npm**: Manajemen paket untuk komponen JavaScript
- **Markdown**: Semua konten pelajaran dan dokumentasi

**Arsitektur:**
- Repositori edukasi multi-bahasa dengan terjemahan yang luas
- Terstruktur dalam modul pelajaran (1-Introduction hingga 6-Data-Science-In-Wild)
- Setiap pelajaran mencakup README, notebook, tugas, dan kuis
- Aplikasi kuis Vue.js yang berdiri sendiri untuk penilaian sebelum/sesudah pelajaran
- Dukungan GitHub Codespaces dan kontainer pengembangan VS Code

## Perintah Pengaturan

### Pengaturan Repositori
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Pengaturan Lingkungan Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Pengaturan Aplikasi Kuis
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### Server Dokumentasi Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Pengaturan Proyek Visualisasi
Untuk proyek visualisasi seperti meaningful-visualizations (pelajaran 13):
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## Alur Kerja Pengembangan

### Bekerja dengan Jupyter Notebooks
1. Mulai Jupyter di root repositori: `jupyter notebook`
2. Navigasikan ke folder pelajaran yang diinginkan
3. Buka file `.ipynb` untuk mengerjakan latihan
4. Notebook bersifat mandiri dengan penjelasan dan sel kode
5. Sebagian besar notebook menggunakan pandas, numpy, dan matplotlib - pastikan ini terinstal

### Struktur Pelajaran
Setiap pelajaran biasanya mencakup:
- `README.md` - Konten utama pelajaran dengan teori dan contoh
- `notebook.ipynb` - Latihan praktis menggunakan Jupyter notebook
- `assignment.ipynb` atau `assignment.md` - Tugas latihan
- Folder `solution/` - Notebook solusi dan kode
- Folder `images/` - Materi visual pendukung

### Pengembangan Aplikasi Kuis
- Aplikasi Vue.js 2 dengan hot-reload selama pengembangan
- Kuis disimpan di `quiz-app/src/assets/translations/`
- Setiap bahasa memiliki folder terjemahan sendiri (en, fr, es, dll.)
- Penomoran kuis dimulai dari 0 hingga 39 (total 40 kuis)

### Menambahkan Terjemahan
- Terjemahan ditempatkan di folder `translations/` di root repositori
- Setiap bahasa memiliki struktur pelajaran lengkap yang mencerminkan bahasa Inggris
- Terjemahan otomatis melalui GitHub Actions (co-op-translator.yml)

## Instruksi Pengujian

### Pengujian Aplikasi Kuis
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Pengujian Notebook
- Tidak ada kerangka pengujian otomatis untuk notebook
- Validasi manual: Jalankan semua sel secara berurutan untuk memastikan tidak ada kesalahan
- Verifikasi file data dapat diakses dan output dihasilkan dengan benar
- Periksa apakah visualisasi ditampilkan dengan baik

### Pengujian Dokumentasi
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Pemeriksaan Kualitas Kode
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Panduan Gaya Kode

### Python (Jupyter Notebooks)
- Ikuti panduan gaya PEP 8 untuk kode Python
- Gunakan nama variabel yang jelas yang menjelaskan data yang dianalisis
- Sertakan sel markdown dengan penjelasan sebelum sel kode
- Fokuskan sel kode pada konsep atau operasi tunggal
- Gunakan pandas untuk manipulasi data, matplotlib untuk visualisasi
- Pola impor umum:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Ikuti panduan gaya Vue.js 2 dan praktik terbaik
- Konfigurasi ESLint di `quiz-app/package.json`
- Gunakan komponen Vue single-file (.vue files)
- Pertahankan arsitektur berbasis komponen
- Jalankan `npm run lint` sebelum melakukan commit

### Dokumentasi Markdown
- Gunakan hierarki heading yang jelas (# ## ### dll.)
- Sertakan blok kode dengan spesifikasi bahasa
- Tambahkan teks alt untuk gambar
- Tautkan ke pelajaran dan sumber daya terkait
- Pertahankan panjang baris yang wajar untuk keterbacaan

### Organisasi File
- Konten pelajaran dalam folder bernomor (01-defining-data-science, dll.)
- Solusi dalam subfolder `solution/` khusus
- Terjemahan mencerminkan struktur bahasa Inggris di folder `translations/`
- Simpan file data di folder `data/` atau folder khusus pelajaran

## Build dan Deployment

### Deployment Aplikasi Kuis
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Deployment Azure Static Web Apps
Aplikasi kuis dapat dideploy ke Azure Static Web Apps:
1. Buat sumber daya Azure Static Web App
2. Hubungkan ke repositori GitHub
3. Konfigurasikan pengaturan build:
   - Lokasi aplikasi: `quiz-app`
   - Lokasi output: `dist`
4. Workflow GitHub Actions akan otomatis mendeply saat ada push

### Situs Dokumentasi
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repositori mencakup konfigurasi kontainer pengembangan
- Codespaces secara otomatis mengatur lingkungan Python dan Node.js
- Buka repositori di Codespace melalui UI GitHub
- Semua dependensi terinstal secara otomatis

## Panduan Pull Request

### Sebelum Mengirimkan
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Format Judul PR
- Gunakan judul yang jelas dan deskriptif
- Format: `[Komponen] Deskripsi singkat`
- Contoh:
  - `[Pelajaran 7] Perbaiki kesalahan impor notebook Python`
  - `[Aplikasi Kuis] Tambahkan terjemahan bahasa Jerman`
  - `[Dokumentasi] Perbarui README dengan prasyarat baru`

### Pemeriksaan yang Diperlukan
- Pastikan semua kode berjalan tanpa kesalahan
- Verifikasi notebook dieksekusi sepenuhnya
- Konfirmasi aplikasi Vue.js berhasil dibangun
- Periksa tautan dokumentasi berfungsi
- Uji aplikasi kuis jika dimodifikasi
- Verifikasi terjemahan mempertahankan struktur yang konsisten

### Panduan Kontribusi
- Ikuti gaya dan pola kode yang ada
- Tambahkan komentar penjelasan untuk logika yang kompleks
- Perbarui dokumentasi yang relevan
- Uji perubahan di berbagai modul pelajaran jika berlaku
- Tinjau file CONTRIBUTING.md

## Catatan Tambahan

### Library Umum yang Digunakan
- **pandas**: Manipulasi dan analisis data
- **numpy**: Komputasi numerik
- **matplotlib**: Visualisasi dan plotting data
- **seaborn**: Visualisasi data statistik (beberapa pelajaran)
- **scikit-learn**: Pembelajaran mesin (pelajaran lanjutan)

### Bekerja dengan File Data
- File data terletak di folder `data/` atau direktori khusus pelajaran
- Sebagian besar notebook mengharapkan file data di jalur relatif
- File CSV adalah format data utama
- Beberapa pelajaran menggunakan JSON untuk contoh data non-relasional

### Dukungan Multibahasa
- Terjemahan lebih dari 40 bahasa melalui GitHub Actions otomatis
- Workflow terjemahan di `.github/workflows/co-op-translator.yml`
- Terjemahan di folder `translations/` dengan kode bahasa
- Terjemahan kuis di `quiz-app/src/assets/translations/`

### Opsi Lingkungan Pengembangan
1. **Pengembangan Lokal**: Instal Python, Jupyter, Node.js secara lokal
2. **GitHub Codespaces**: Lingkungan pengembangan instan berbasis cloud
3. **VS Code Dev Containers**: Pengembangan berbasis kontainer lokal
4. **Binder**: Luncurkan notebook di cloud (jika dikonfigurasi)

### Panduan Konten Pelajaran
- Setiap pelajaran bersifat mandiri tetapi membangun konsep sebelumnya
- Kuis sebelum pelajaran menguji pengetahuan awal
- Kuis setelah pelajaran memperkuat pembelajaran
- Tugas memberikan latihan praktis
- Sketchnotes memberikan ringkasan visual

### Pemecahan Masalah Umum

**Masalah Kernel Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Kegagalan Instalasi npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Kesalahan Impor di Notebook:**
- Verifikasi semua library yang diperlukan telah terinstal
- Periksa kompatibilitas versi Python (disarankan Python 3.7+)
- Pastikan lingkungan virtual diaktifkan

**Docsify Tidak Memuat:**
- Verifikasi Anda melayani dari root repositori
- Periksa bahwa `index.html` ada
- Pastikan akses jaringan yang tepat (port 3000)

### Pertimbangan Performa
- Dataset besar mungkin membutuhkan waktu untuk dimuat di notebook
- Rendering visualisasi bisa lambat untuk plot yang kompleks
- Server dev Vue.js memungkinkan hot-reload untuk iterasi cepat
- Build produksi dioptimalkan dan diminimalkan

### Catatan Keamanan
- Jangan komit data sensitif atau kredensial
- Gunakan variabel lingkungan untuk kunci API dalam pelajaran cloud
- Pelajaran terkait Azure mungkin memerlukan kredensial akun Azure
- Pertahankan dependensi tetap diperbarui untuk patch keamanan

## Kontribusi untuk Terjemahan
- Terjemahan otomatis dikelola melalui GitHub Actions
- Koreksi manual diterima untuk akurasi terjemahan
- Ikuti struktur folder terjemahan yang ada
- Perbarui tautan kuis untuk menyertakan parameter bahasa: `?loc=fr`
- Uji pelajaran yang diterjemahkan untuk memastikan tampilan yang benar

## Sumber Daya Terkait
- Kurikulum utama: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Forum Diskusi: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Kurikulum Microsoft lainnya: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Pemeliharaan Proyek
- Pembaruan rutin untuk menjaga konten tetap relevan
- Kontribusi komunitas diterima
- Masalah dilacak di GitHub
- PR ditinjau oleh pemelihara kurikulum
- Tinjauan dan pembaruan konten bulanan

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.