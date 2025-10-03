<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:07:04+00:00",
  "source_file": "USAGE.md",
  "language_code": "ms"
}
-->
# Panduan Penggunaan

Panduan ini menyediakan contoh dan alur kerja biasa untuk menggunakan kurikulum Data Science untuk Pemula.

## Kandungan

- [Cara Menggunakan Kurikulum Ini](../..)
- [Bekerja dengan Pelajaran](../..)
- [Bekerja dengan Jupyter Notebooks](../..)
- [Menggunakan Aplikasi Kuiz](../..)
- [Alur Kerja Biasa](../..)
- [Tip untuk Pembelajar Sendiri](../..)
- [Tip untuk Guru](../..)

## Cara Menggunakan Kurikulum Ini

Kurikulum ini direka untuk fleksibiliti dan boleh digunakan dalam pelbagai cara:

- **Pembelajaran kendiri**: Belajar secara bebas mengikut kelajuan anda sendiri
- **Pengajaran di kelas**: Digunakan sebagai kursus berstruktur dengan bimbingan
- **Kumpulan belajar**: Belajar secara kolaboratif dengan rakan-rakan
- **Format bengkel**: Sesi pembelajaran intensif jangka pendek

## Bekerja dengan Pelajaran

Setiap pelajaran mengikuti struktur yang konsisten untuk memaksimumkan pembelajaran:

### Struktur Pelajaran

1. **Kuiz Pra-pelajaran**: Uji pengetahuan sedia ada anda
2. **Sketchnote** (Pilihan): Ringkasan visual konsep utama
3. **Video** (Pilihan): Kandungan video tambahan
4. **Pelajaran Bertulis**: Konsep utama dan penjelasan
5. **Jupyter Notebook**: Latihan pengekodan secara langsung
6. **Tugasan**: Praktikkan apa yang telah anda pelajari
7. **Kuiz Pasca-pelajaran**: Kukuhkan pemahaman anda

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

### Memulakan Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Menjalankan Sel Notebook

1. **Jalankan sel**: Tekan `Shift + Enter` atau klik butang "Run"
2. **Jalankan semua sel**: Pilih "Cell" → "Run All" dari menu
3. **Mulakan semula kernel**: Pilih "Kernel" → "Restart" jika anda menghadapi masalah

### Contoh: Bekerja dengan Data dalam Notebook

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

### Menyimpan Kerja Anda

- Jupyter menyimpan secara automatik secara berkala
- Simpan secara manual: Tekan `Ctrl + S` (atau `Cmd + S` pada macOS)
- Kemajuan anda disimpan dalam fail `.ipynb`

## Menggunakan Aplikasi Kuiz

### Menjalankan Aplikasi Kuiz Secara Tempatan

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Menjawab Kuiz

1. Kuiz pra-pelajaran disediakan di bahagian atas setiap pelajaran
2. Kuiz pasca-pelajaran disediakan di bahagian bawah setiap pelajaran
3. Setiap kuiz mempunyai 3 soalan
4. Kuiz direka untuk mengukuhkan pembelajaran, bukan untuk ujian menyeluruh

### Penomboran Kuiz

- Kuiz bernombor 0-39 (40 kuiz keseluruhan)
- Setiap pelajaran biasanya mempunyai kuiz pra dan pasca
- URL kuiz termasuk nombor kuiz: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Alur Kerja Biasa

### Alur Kerja 1: Laluan Pemula Lengkap

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

Jika anda berminat dengan topik tertentu:

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

### Alur Kerja 3: Pembelajaran Berdasarkan Projek

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Alur Kerja 4: Data Science Berasaskan Awan

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Tip untuk Pembelajar Sendiri

### Kekal Teratur

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Berlatih Secara Berkala

- Tetapkan masa khusus setiap hari atau minggu
- Lengkapkan sekurang-kurangnya satu pelajaran setiap minggu
- Tinjau pelajaran sebelumnya secara berkala

### Berinteraksi dengan Komuniti

- Sertai [komuniti Discord](https://aka.ms/ds4beginners/discord)
- Sertai saluran #Data-Science-for-Beginners di Discord [Perbincangan Discord](https://aka.ms/ds4beginners/discord)
- Kongsi kemajuan anda dan ajukan soalan

### Bangunkan Projek Anda Sendiri

Selepas melengkapkan pelajaran, gunakan konsep untuk projek peribadi:

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

## Tip untuk Guru

### Persediaan Kelas

1. Tinjau [for-teachers.md](for-teachers.md) untuk panduan terperinci
2. Sediakan persekitaran bersama (GitHub Classroom atau Codespaces)
3. Tetapkan saluran komunikasi (Discord, Slack, atau Teams)

### Perancangan Pelajaran

**Jadual 10 Minggu yang Disyorkan:**

- **Minggu 1-2**: Pengenalan (Pelajaran 1-4)
- **Minggu 3-4**: Bekerja dengan Data (Pelajaran 5-8)
- **Minggu 5-6**: Visualisasi Data (Pelajaran 9-13)
- **Minggu 7-8**: Kitaran Hayat Data Science (Pelajaran 14-16)
- **Minggu 9**: Data Science Berasaskan Awan (Pelajaran 17-19)
- **Minggu 10**: Aplikasi Dunia Nyata & Projek Akhir (Pelajaran 20)

### Menjalankan Docsify untuk Akses Luar Talian

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Penilaian Tugasan

- Tinjau notebook pelajar untuk latihan yang telah diselesaikan
- Periksa pemahaman melalui skor kuiz
- Nilai projek akhir menggunakan prinsip kitaran hayat data science

### Membuat Tugasan

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

## Bekerja Secara Luar Talian

### Muat Turun Sumber

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Jalankan Dokumentasi Secara Tempatan

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Jalankan Aplikasi Kuiz Secara Tempatan

```bash
cd quiz-app
npm run serve
```

## Mengakses Kandungan Terjemahan

Terjemahan tersedia dalam lebih daripada 40 bahasa:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Setiap terjemahan mengekalkan struktur yang sama seperti versi Bahasa Inggeris.

## Sumber Tambahan

### Teruskan Pembelajaran

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Laluan pembelajaran tambahan
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Sumber untuk pelajar
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Forum komuniti

### Kurikulum Berkaitan

- [AI untuk Pemula](https://aka.ms/ai-beginners)
- [ML untuk Pemula](https://aka.ms/ml-beginners)
- [Web Dev untuk Pemula](https://aka.ms/webdev-beginners)
- [Generative AI untuk Pemula](https://aka.ms/genai-beginners)

## Mendapatkan Bantuan

- Tinjau [TROUBLESHOOTING.md](TROUBLESHOOTING.md) untuk isu biasa
- Cari [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Sertai [Discord kami](https://aka.ms/ds4beginners/discord)
- Tinjau [CONTRIBUTING.md](CONTRIBUTING.md) untuk melaporkan isu atau menyumbang

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.