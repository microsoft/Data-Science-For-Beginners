<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:06:44+00:00",
  "source_file": "USAGE.md",
  "language_code": "id"
}
-->
# Panduan Penggunaan

Panduan ini menyediakan contoh dan alur kerja umum untuk menggunakan kurikulum Data Science untuk Pemula.

## Daftar Isi

- [Cara Menggunakan Kurikulum Ini](../..)
- [Bekerja dengan Pelajaran](../..)
- [Bekerja dengan Jupyter Notebooks](../..)
- [Menggunakan Aplikasi Kuis](../..)
- [Alur Kerja Umum](../..)
- [Tips untuk Pembelajar Mandiri](../..)
- [Tips untuk Pengajar](../..)

## Cara Menggunakan Kurikulum Ini

Kurikulum ini dirancang fleksibel dan dapat digunakan dalam berbagai cara:

- **Belajar mandiri**: Pelajari pelajaran secara independen sesuai kecepatan Anda
- **Instruksi di kelas**: Gunakan sebagai kursus terstruktur dengan bimbingan
- **Kelompok belajar**: Belajar secara kolaboratif dengan teman
- **Format workshop**: Sesi belajar intensif jangka pendek

## Bekerja dengan Pelajaran

Setiap pelajaran mengikuti struktur yang konsisten untuk memaksimalkan pembelajaran:

### Struktur Pelajaran

1. **Kuis Pra-pelajaran**: Uji pengetahuan awal Anda
2. **Sketchnote** (Opsional): Ringkasan visual konsep utama
3. **Video** (Opsional): Konten video tambahan
4. **Pelajaran Tertulis**: Konsep inti dan penjelasan
5. **Jupyter Notebook**: Latihan coding langsung
6. **Tugas**: Latih apa yang telah Anda pelajari
7. **Kuis Pasca-pelajaran**: Perkuat pemahaman Anda

### Contoh Alur Kerja untuk Pelajaran

```bash
# 1. Navigate to the lesson directory
cd 1-Introduction/01-defining-data-science

# 2. Read the README.md
# Open README.md in your browser or editor

# 3. Take the pre-lesson quiz
# Click the quiz link in the README

# 4. Open the Jupyter notebook (if available)
jupyter notebook

# 5. Complete the exercises in the notebook

# 6. Work on the assignment

# 7. Take the post-lesson quiz
```

## Bekerja dengan Jupyter Notebooks

### Memulai Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Menjalankan Sel Notebook

1. **Eksekusi sel**: Tekan `Shift + Enter` atau klik tombol "Run"
2. **Eksekusi semua sel**: Pilih "Cell" → "Run All" dari menu
3. **Restart kernel**: Pilih "Kernel" → "Restart" jika Anda mengalami masalah

### Contoh: Bekerja dengan Data di Notebook

```python
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load a dataset
df = pd.read_csv('data/sample.csv')

# Explore the data
df.head()
df.info()
df.describe()

# Create a visualization
plt.figure(figsize=(10, 6))
plt.plot(df['column_name'])
plt.title('Sample Visualization')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```

### Menyimpan Pekerjaan Anda

- Jupyter secara otomatis menyimpan secara berkala
- Simpan secara manual: Tekan `Ctrl + S` (atau `Cmd + S` di macOS)
- Kemajuan Anda disimpan dalam file `.ipynb`

## Menggunakan Aplikasi Kuis

### Menjalankan Aplikasi Kuis Secara Lokal

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Mengikuti Kuis

1. Kuis pra-pelajaran terhubung di bagian atas setiap pelajaran
2. Kuis pasca-pelajaran terhubung di bagian bawah setiap pelajaran
3. Setiap kuis memiliki 3 pertanyaan
4. Kuis dirancang untuk memperkuat pembelajaran, bukan untuk pengujian yang mendalam

### Penomoran Kuis

- Kuis diberi nomor 0-39 (total 40 kuis)
- Setiap pelajaran biasanya memiliki kuis pra dan pasca
- URL kuis mencakup nomor kuis: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Alur Kerja Umum

### Alur Kerja 1: Jalur Pemula Lengkap

```bash
# 1. Set up your environment (see INSTALLATION.md)

# 2. Start with Lesson 1
cd 1-Introduction/01-defining-data-science

# 3. For each lesson:
#    - Take pre-lesson quiz
#    - Read the lesson content
#    - Work through the notebook
#    - Complete the assignment
#    - Take post-lesson quiz

# 4. Progress through all 20 lessons sequentially
```

### Alur Kerja 2: Pembelajaran Berdasarkan Topik

Jika Anda tertarik pada topik tertentu:

```bash
# Example: Focus on Data Visualization
cd 3-Data-Visualization

# Explore lessons 9-13:
# - Lesson 9: Visualizing Quantities
# - Lesson 10: Visualizing Distributions
# - Lesson 11: Visualizing Proportions
# - Lesson 12: Visualizing Relationships
# - Lesson 13: Meaningful Visualizations
```

### Alur Kerja 3: Pembelajaran Berbasis Proyek

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Alur Kerja 4: Data Science Berbasis Cloud

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Tips untuk Pembelajar Mandiri

### Tetap Terorganisir

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Berlatih Secara Teratur

- Sisihkan waktu khusus setiap hari atau minggu
- Selesaikan setidaknya satu pelajaran per minggu
- Tinjau pelajaran sebelumnya secara berkala

### Berinteraksi dengan Komunitas

- Bergabunglah dengan [komunitas Discord](https://aka.ms/ds4beginners/discord)
- Berpartisipasi di Channel #Data-Science-for-Beginners di Discord [Diskusi Discord](https://aka.ms/ds4beginners/discord)
- Bagikan kemajuan Anda dan ajukan pertanyaan

### Bangun Proyek Anda Sendiri

Setelah menyelesaikan pelajaran, terapkan konsep pada proyek pribadi:

```python
# Example: Analyze your own dataset
import pandas as pd

# Load your own data
my_data = pd.read_csv('my-project/data.csv')

# Apply techniques learned
# - Data cleaning (Lesson 8)
# - Exploratory data analysis (Lesson 7)
# - Visualization (Lessons 9-13)
# - Analysis (Lesson 15)
```

## Tips untuk Pengajar

### Pengaturan Kelas

1. Tinjau [for-teachers.md](for-teachers.md) untuk panduan rinci
2. Siapkan lingkungan bersama (GitHub Classroom atau Codespaces)
3. Tetapkan saluran komunikasi (Discord, Slack, atau Teams)

### Perencanaan Pelajaran

**Jadwal 10 Minggu yang Disarankan:**

- **Minggu 1-2**: Pengantar (Pelajaran 1-4)
- **Minggu 3-4**: Bekerja dengan Data (Pelajaran 5-8)
- **Minggu 5-6**: Visualisasi Data (Pelajaran 9-13)
- **Minggu 7-8**: Siklus Hidup Data Science (Pelajaran 14-16)
- **Minggu 9**: Data Science Berbasis Cloud (Pelajaran 17-19)
- **Minggu 10**: Aplikasi Dunia Nyata & Proyek Akhir (Pelajaran 20)

### Menjalankan Docsify untuk Akses Offline

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Penilaian Tugas

- Tinjau notebook siswa untuk latihan yang telah diselesaikan
- Periksa pemahaman melalui skor kuis
- Evaluasi proyek akhir menggunakan prinsip siklus hidup data science

### Membuat Tugas

```python
# Example custom assignment template
"""
Assignment: [Topic]

Objective: [Learning goal]

Dataset: [Provide or have students find one]

Tasks:
1. Load and explore the dataset
2. Clean and prepare the data
3. Create at least 3 visualizations
4. Perform analysis
5. Communicate findings

Deliverables:
- Jupyter notebook with code and explanations
- Written summary of findings
"""
```

## Bekerja Secara Offline

### Unduh Sumber Daya

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Jalankan Dokumentasi Secara Lokal

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Jalankan Aplikasi Kuis Secara Lokal

```bash
cd quiz-app
npm run serve
```

## Mengakses Konten yang Diterjemahkan

Terjemahan tersedia dalam lebih dari 40 bahasa:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Setiap terjemahan mempertahankan struktur yang sama seperti versi bahasa Inggris.

## Sumber Daya Tambahan

### Lanjutkan Belajar

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Jalur pembelajaran tambahan
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Sumber daya untuk siswa
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Forum komunitas

### Kurikulum Terkait

- [AI untuk Pemula](https://aka.ms/ai-beginners)
- [ML untuk Pemula](https://aka.ms/ml-beginners)
- [Web Dev untuk Pemula](https://aka.ms/webdev-beginners)
- [Generative AI untuk Pemula](https://aka.ms/genai-beginners)

## Mendapatkan Bantuan

- Periksa [TROUBLESHOOTING.md](TROUBLESHOOTING.md) untuk masalah umum
- Cari [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Bergabunglah dengan [Discord kami](https://aka.ms/ds4beginners/discord)
- Tinjau [CONTRIBUTING.md](CONTRIBUTING.md) untuk melaporkan masalah atau berkontribusi

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.