<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:31:51+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ms"
}
-->
# AGENTS.md

## Gambaran Projek

Data Science for Beginners adalah kurikulum komprehensif selama 10 minggu dengan 20 pelajaran yang dicipta oleh Microsoft Azure Cloud Advocates. Repositori ini adalah sumber pembelajaran yang mengajar konsep asas sains data melalui pelajaran berasaskan projek, termasuk Jupyter notebooks, kuiz interaktif, dan tugasan praktikal.

**Teknologi Utama:**
- **Jupyter Notebooks**: Medium pembelajaran utama menggunakan Python 3
- **Perpustakaan Python**: pandas, numpy, matplotlib untuk analisis dan visualisasi data
- **Vue.js 2**: Aplikasi kuiz (folder quiz-app)
- **Docsify**: Penjana laman dokumentasi untuk akses luar talian
- **Node.js/npm**: Pengurusan pakej untuk komponen JavaScript
- **Markdown**: Semua kandungan pelajaran dan dokumentasi

**Arkitektur:**
- Repositori pendidikan pelbagai bahasa dengan terjemahan yang meluas
- Disusun dalam modul pelajaran (1-Pengenalan hingga 6-Data-Science-In-Wild)
- Setiap pelajaran termasuk README, notebooks, tugasan, dan kuiz
- Aplikasi kuiz Vue.js yang berdiri sendiri untuk penilaian sebelum/selepas pelajaran
- Sokongan GitHub Codespaces dan kontena dev VS Code

## Perintah Persediaan

### Persediaan Repositori
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Persediaan Persekitaran Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Persediaan Aplikasi Kuiz
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

### Pelayan Dokumentasi Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Persediaan Projek Visualisasi
Untuk projek visualisasi seperti meaningful-visualizations (pelajaran 13):
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


## Aliran Kerja Pembangunan

### Bekerja dengan Jupyter Notebooks
1. Mulakan Jupyter di akar repositori: `jupyter notebook`
2. Navigasi ke folder pelajaran yang diingini
3. Buka fail `.ipynb` untuk menjalankan latihan
4. Notebooks adalah berdiri sendiri dengan penjelasan dan sel kod
5. Kebanyakan notebooks menggunakan pandas, numpy, dan matplotlib - pastikan ini dipasang

### Struktur Pelajaran
Setiap pelajaran biasanya mengandungi:
- `README.md` - Kandungan utama pelajaran dengan teori dan contoh
- `notebook.ipynb` - Latihan praktikal Jupyter notebook
- `assignment.ipynb` atau `assignment.md` - Tugasan praktikal
- Folder `solution/` - Notebook dan kod penyelesaian
- Folder `images/` - Bahan visual sokongan

### Pembangunan Aplikasi Kuiz
- Aplikasi Vue.js 2 dengan hot-reload semasa pembangunan
- Kuiz disimpan dalam `quiz-app/src/assets/translations/`
- Setiap bahasa mempunyai folder terjemahan sendiri (en, fr, es, dll.)
- Penomboran kuiz bermula dari 0 hingga 39 (40 kuiz keseluruhan)

### Menambah Terjemahan
- Terjemahan diletakkan dalam folder `translations/` di akar repositori
- Setiap bahasa mempunyai struktur pelajaran lengkap yang mencerminkan bahasa Inggeris
- Terjemahan automatik melalui GitHub Actions (co-op-translator.yml)

## Arahan Pengujian

### Pengujian Aplikasi Kuiz
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
- Tiada rangka kerja ujian automatik untuk notebooks
- Pengesahan manual: Jalankan semua sel secara berurutan untuk memastikan tiada ralat
- Pastikan fail data boleh diakses dan output dihasilkan dengan betul
- Periksa bahawa visualisasi dipaparkan dengan baik

### Pengujian Dokumentasi
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Pemeriksaan Kualiti Kod
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Garis Panduan Gaya Kod

### Python (Jupyter Notebooks)
- Ikuti garis panduan gaya PEP 8 untuk kod Python
- Gunakan nama pemboleh ubah yang jelas yang menerangkan data yang dianalisis
- Sertakan sel markdown dengan penjelasan sebelum sel kod
- Kekalkan sel kod fokus pada konsep atau operasi tunggal
- Gunakan pandas untuk manipulasi data, matplotlib untuk visualisasi
- Corak import biasa:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Ikuti panduan gaya Vue.js 2 dan amalan terbaik
- Konfigurasi ESLint dalam `quiz-app/package.json`
- Gunakan komponen tunggal Vue (.vue files)
- Kekalkan seni bina berasaskan komponen
- Jalankan `npm run lint` sebelum membuat perubahan

### Dokumentasi Markdown
- Gunakan hierarki tajuk yang jelas (# ## ### dll.)
- Sertakan blok kod dengan penentu bahasa
- Tambahkan teks alt untuk imej
- Pautkan ke pelajaran dan sumber berkaitan
- Kekalkan panjang baris yang munasabah untuk kebolehbacaan

### Organisasi Fail
- Kandungan pelajaran dalam folder bernombor (01-defining-data-science, dll.)
- Penyelesaian dalam subfolder `solution/` khusus
- Terjemahan mencerminkan struktur bahasa Inggeris dalam folder `translations/`
- Simpan fail data dalam folder `data/` atau folder khusus pelajaran

## Pembinaan dan Penerapan

### Penerapan Aplikasi Kuiz
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Penerapan Azure Static Web Apps
Aplikasi kuiz boleh diterapkan ke Azure Static Web Apps:
1. Buat sumber Azure Static Web App
2. Sambungkan ke repositori GitHub
3. Konfigurasi tetapan pembinaan:
   - Lokasi aplikasi: `quiz-app`
   - Lokasi output: `dist`
4. Aliran kerja GitHub Actions akan menerapkan secara automatik pada push

### Laman Dokumentasi
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repositori termasuk konfigurasi kontena dev
- Codespaces secara automatik menyediakan persekitaran Python dan Node.js
- Buka repositori dalam Codespace melalui UI GitHub
- Semua kebergantungan dipasang secara automatik

## Garis Panduan Permintaan Tarik

### Sebelum Menghantar
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Format Tajuk PR
- Gunakan tajuk yang jelas dan deskriptif
- Format: `[Komponen] Penerangan ringkas`
- Contoh:
  - `[Pelajaran 7] Betulkan ralat import notebook Python`
  - `[Aplikasi Kuiz] Tambah terjemahan bahasa Jerman`
  - `[Dokumen] Kemas kini README dengan prasyarat baru`

### Pemeriksaan Diperlukan
- Pastikan semua kod berjalan tanpa ralat
- Sahkan notebook dijalankan sepenuhnya
- Pastikan aplikasi Vue.js dibina dengan berjaya
- Periksa bahawa pautan dokumentasi berfungsi
- Uji aplikasi kuiz jika diubah
- Sahkan terjemahan mengekalkan struktur yang konsisten

### Garis Panduan Sumbangan
- Ikuti gaya dan corak kod yang sedia ada
- Tambahkan komen penjelasan untuk logik yang kompleks
- Kemas kini dokumentasi yang relevan
- Uji perubahan merentasi modul pelajaran yang berbeza jika berkenaan
- Semak fail CONTRIBUTING.md

## Nota Tambahan

### Perpustakaan Biasa Digunakan
- **pandas**: Manipulasi dan analisis data
- **numpy**: Pengkomputeran numerik
- **matplotlib**: Visualisasi dan plot data
- **seaborn**: Visualisasi data statistik (beberapa pelajaran)
- **scikit-learn**: Pembelajaran mesin (pelajaran lanjutan)

### Bekerja dengan Fail Data
- Fail data terletak dalam folder `data/` atau direktori khusus pelajaran
- Kebanyakan notebooks mengharapkan fail data dalam laluan relatif
- Fail CSV adalah format data utama
- Beberapa pelajaran menggunakan JSON untuk contoh data bukan relasional

### Sokongan Pelbagai Bahasa
- 40+ terjemahan bahasa melalui GitHub Actions automatik
- Aliran kerja terjemahan dalam `.github/workflows/co-op-translator.yml`
- Terjemahan dalam folder `translations/` dengan kod bahasa
- Terjemahan kuiz dalam `quiz-app/src/assets/translations/`

### Pilihan Persekitaran Pembangunan
1. **Pembangunan Tempatan**: Pasang Python, Jupyter, Node.js secara tempatan
2. **GitHub Codespaces**: Persekitaran pembangunan segera berasaskan awan
3. **Kontena Dev VS Code**: Pembangunan berasaskan kontena tempatan
4. **Binder**: Lancarkan notebooks dalam awan (jika dikonfigurasi)

### Garis Panduan Kandungan Pelajaran
- Setiap pelajaran berdiri sendiri tetapi membina konsep sebelumnya
- Kuiz sebelum pelajaran menguji pengetahuan terdahulu
- Kuiz selepas pelajaran mengukuhkan pembelajaran
- Tugasan menyediakan latihan praktikal
- Sketchnotes menyediakan ringkasan visual

### Menyelesaikan Masalah Biasa

**Isu Kernel Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Kegagalan Pemasangan npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Ralat Import dalam Notebooks:**
- Pastikan semua perpustakaan yang diperlukan dipasang
- Periksa keserasian versi Python (Python 3.7+ disyorkan)
- Pastikan persekitaran maya diaktifkan

**Docsify Tidak Memuatkan:**
- Pastikan anda melayani dari akar repositori
- Periksa bahawa `index.html` wujud
- Pastikan akses rangkaian yang betul (port 3000)

### Pertimbangan Prestasi
- Dataset besar mungkin mengambil masa untuk dimuatkan dalam notebooks
- Rendering visualisasi boleh menjadi perlahan untuk plot yang kompleks
- Pelayan dev Vue.js membolehkan hot-reload untuk iterasi cepat
- Pembinaan pengeluaran dioptimumkan dan diminimumkan

### Nota Keselamatan
- Tiada data sensitif atau kelayakan harus dikomit
- Gunakan pembolehubah persekitaran untuk sebarang kunci API dalam pelajaran awan
- Pelajaran berkaitan Azure mungkin memerlukan kelayakan akaun Azure
- Kekalkan kebergantungan terkini untuk tampalan keselamatan

## Menyumbang kepada Terjemahan
- Terjemahan automatik diuruskan melalui GitHub Actions
- Pembetulan manual dialu-alukan untuk ketepatan terjemahan
- Ikuti struktur folder terjemahan yang sedia ada
- Kemas kini pautan kuiz untuk memasukkan parameter bahasa: `?loc=fr`
- Uji pelajaran yang diterjemahkan untuk paparan yang betul

## Sumber Berkaitan
- Kurikulum utama: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Forum Perbincangan: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Kurikulum Microsoft lain: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Penyelenggaraan Projek
- Kemas kini berkala untuk memastikan kandungan terkini
- Sumbangan komuniti dialu-alukan
- Isu dijejaki di GitHub
- PR disemak oleh penyelenggara kurikulum
- Semakan dan kemas kini kandungan bulanan

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.