<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:43:50+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "id"
}
-->
# Panduan Pemecahan Masalah

Panduan ini memberikan solusi untuk masalah umum yang mungkin Anda temui saat bekerja dengan kurikulum Data Science untuk Pemula.

## Daftar Isi

- [Masalah Python dan Jupyter](../..)
- [Masalah Paket dan Ketergantungan](../..)
- [Masalah Jupyter Notebook](../..)
- [Masalah Aplikasi Kuis](../..)
- [Masalah Git dan GitHub](../..)
- [Masalah Dokumentasi Docsify](../..)
- [Masalah Data dan File](../..)
- [Masalah Performa](../..)
- [Mendapatkan Bantuan Tambahan](../..)

## Masalah Python dan Jupyter

### Python Tidak Ditemukan atau Versi Salah

**Masalah:** `python: command not found` atau versi Python salah

**Solusi:**

```bash
# Check Python version
python --version
python3 --version

# If Python 3 is installed as 'python3', create an alias
# On macOS/Linux, add to ~/.bashrc or ~/.zshrc:
alias python=python3
alias pip=pip3

# Or use python3 explicitly
python3 -m pip install jupyter
```

**Solusi untuk Windows:**
1. Instal ulang Python dari [python.org](https://www.python.org/)
2. Saat instalasi, centang "Add Python to PATH"
3. Restart terminal/command prompt Anda

### Masalah Aktivasi Lingkungan Virtual

**Masalah:** Lingkungan virtual tidak dapat diaktifkan

**Solusi:**

**Windows:**
```bash
# If you get execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Ensure the activate script is executable
chmod +x venv/bin/activate

# Then activate
source venv/bin/activate
```

**Verifikasi aktivasi:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Masalah Kernel Jupyter

**Masalah:** "Kernel tidak ditemukan" atau "Kernel terus mati"

**Solusi:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Masalah:** Versi Python salah di Jupyter

**Solusi:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Masalah Paket dan Ketergantungan

### Kesalahan Import

**Masalah:** `ModuleNotFoundError: No module named 'pandas'` (atau paket lainnya)

**Solusi:**

```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install missing package
pip install pandas

# Install all common packages
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

# Verify installation
python -c "import pandas; print(pandas.__version__)"
```

### Kegagalan Instalasi Pip

**Masalah:** `pip install` gagal dengan kesalahan izin

**Solusi:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Masalah:** `pip install` gagal dengan kesalahan sertifikat SSL

**Solusi:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Konflik Versi Paket

**Masalah:** Versi paket tidak kompatibel

**Solusi:**

```bash
# Create fresh virtual environment
python -m venv venv-new
source venv-new/bin/activate  # or venv-new\Scripts\activate on Windows

# Install packages with specific versions if needed
pip install pandas==1.3.0
pip install numpy==1.21.0

# Or let pip resolve dependencies
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

## Masalah Jupyter Notebook

### Jupyter Tidak Mau Mulai

**Masalah:** Perintah `jupyter notebook` tidak ditemukan

**Solusi:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook Tidak Mau Dimuat atau Disimpan

**Masalah:** "Notebook gagal dimuat" atau kesalahan saat menyimpan

**Solusi:**

1. Periksa izin file
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Periksa apakah file rusak
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Hapus cache Jupyter
```bash
jupyter notebook --clear-cache
```

### Sel Tidak Mau Dieksekusi

**Masalah:** Sel macet di "In [*]" atau membutuhkan waktu lama

**Solusi:**

1. **Hentikan kernel**: Klik tombol "Interrupt" atau tekan `I, I`
2. **Restart kernel**: Menu Kernel → Restart
3. **Periksa apakah ada loop tak berujung** dalam kode Anda
4. **Hapus output**: Cell → All Output → Clear

### Grafik Tidak Tampil

**Masalah:** Grafik `matplotlib` tidak muncul di notebook

**Solusi:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternatif untuk grafik interaktif:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Masalah Aplikasi Kuis

### npm install Gagal

**Masalah:** Kesalahan saat menjalankan `npm install`

**Solusi:**

```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install

# If still failing, try with legacy peer deps
npm install --legacy-peer-deps
```

### Aplikasi Kuis Tidak Mau Mulai

**Masalah:** `npm run serve` gagal

**Solusi:**

```bash
# Check Node.js version
node --version  # Should be 12.x or higher

# Reinstall dependencies
cd quiz-app
rm -rf node_modules package-lock.json
npm install

# Try different port
npm run serve -- --port 8081
```

### Port Sudah Digunakan

**Masalah:** "Port 8080 sudah digunakan"

**Solusi:**

```bash
# Find and kill process on port 8080
# macOS/Linux:
lsof -ti:8080 | xargs kill -9

# Windows:
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# Or use a different port
npm run serve -- --port 8081
```

### Kuis Tidak Dimuat atau Halaman Kosong

**Masalah:** Aplikasi kuis dimuat tetapi menunjukkan halaman kosong

**Solusi:**

1. Periksa konsol browser untuk kesalahan (F12)
2. Hapus cache dan cookie browser
3. Coba browser lain
4. Pastikan JavaScript diaktifkan
5. Periksa apakah pemblokir iklan mengganggu

```bash
# Rebuild the app
npm run build
npm run serve
```

## Masalah Git dan GitHub

### Git Tidak Dikenali

**Masalah:** `git: command not found`

**Solusi:**

**Windows:**
- Instal Git dari [git-scm.com](https://git-scm.com/)
- Restart terminal setelah instalasi

**macOS:**

> **Catatan:** Jika Anda belum menginstal Homebrew, ikuti instruksi di [https://brew.sh/](https://brew.sh/) untuk menginstalnya terlebih dahulu.
```bash
# Install via Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

**Linux:**
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo dnf install git      # Fedora
```

### Clone Gagal

**Masalah:** `git clone` gagal dengan kesalahan autentikasi

**Solusi:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Izin Ditolak (publickey)

**Masalah:** Autentikasi kunci SSH gagal

**Solusi:**

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add key to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Add public key to GitHub
# Copy key: cat ~/.ssh/id_ed25519.pub
# Add at: https://github.com/settings/keys
```

## Masalah Dokumentasi Docsify

### Perintah Docsify Tidak Ditemukan

**Masalah:** `docsify: command not found`

**Solusi:**

```bash
# Install globally
npm install -g docsify-cli

# If permission error on macOS/Linux
sudo npm install -g docsify-cli

# Verify installation
docsify --version

# If still not found, add npm global path
# Find npm global path
npm config get prefix

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$PATH:/usr/local/bin"
```

### Dokumentasi Tidak Dimuat

**Masalah:** Docsify berjalan tetapi konten tidak dimuat

**Solusi:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Gambar Tidak Tampil

**Masalah:** Gambar menunjukkan ikon tautan rusak

**Solusi:**

1. Periksa apakah jalur gambar bersifat relatif
2. Pastikan file gambar ada di repositori
3. Hapus cache browser
4. Verifikasi ekstensi file sesuai (case-sensitive pada beberapa sistem)

## Masalah Data dan File

### Kesalahan File Tidak Ditemukan

**Masalah:** `FileNotFoundError` saat memuat data

**Solusi:**

```python
import os

# Check current working directory
print(os.getcwd())

# Use absolute path
data_path = os.path.join(os.getcwd(), 'data', 'filename.csv')
df = pd.read_csv(data_path)

# Or use relative path from notebook location
df = pd.read_csv('../data/filename.csv')

# Verify file exists
print(os.path.exists('data/filename.csv'))
```

### Kesalahan Membaca CSV

**Masalah:** Kesalahan saat membaca file CSV

**Solusi:**

```python
import pandas as pd

# Try different encodings
df = pd.read_csv('file.csv', encoding='utf-8')
# or
df = pd.read_csv('file.csv', encoding='latin-1')
# or
df = pd.read_csv('file.csv', encoding='ISO-8859-1')

# Handle missing values
df = pd.read_csv('file.csv', na_values=['NA', 'N/A', ''])

# Specify delimiter if not comma
df = pd.read_csv('file.csv', delimiter=';')
```

### Kesalahan Memori dengan Dataset Besar

**Masalah:** `MemoryError` saat memuat file besar

**Solusi:**

```python
# Read in chunks
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Process chunk
    chunks.append(chunk)
df = pd.concat(chunks)

# Or read specific columns only
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])

# Use more efficient data types
df = pd.read_csv('file.csv', dtype={'column_name': 'int32'})
```

## Masalah Performa

### Performa Notebook Lambat

**Masalah:** Notebook berjalan sangat lambat

**Solusi:**

1. **Restart kernel dan hapus output**
   - Kernel → Restart & Clear Output

2. **Tutup notebook yang tidak digunakan**

3. **Optimalkan kode:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Ambil sampel dataset besar:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Browser Crash

**Masalah:** Browser crash atau tidak responsif

**Solusi:**

1. Tutup tab yang tidak digunakan
2. Hapus cache browser
3. Tingkatkan memori browser (Chrome: `chrome://settings/system`)
4. Gunakan JupyterLab sebagai alternatif:
```bash
pip install jupyterlab
jupyter lab
```

## Mendapatkan Bantuan Tambahan

### Sebelum Meminta Bantuan

1. Periksa panduan pemecahan masalah ini
2. Cari di [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Tinjau [INSTALLATION.md](INSTALLATION.md) dan [USAGE.md](USAGE.md)
4. Coba cari pesan kesalahan secara online

### Cara Meminta Bantuan

Saat membuat issue atau meminta bantuan, sertakan:

1. **Sistem Operasi**: Windows, macOS, atau Linux (distribusi mana)
2. **Versi Python**: Jalankan `python --version`
3. **Pesan Kesalahan**: Salin pesan kesalahan lengkap
4. **Langkah untuk Mereproduksi**: Apa yang Anda lakukan sebelum kesalahan terjadi
5. **Apa yang Sudah Dicoba**: Solusi yang sudah Anda coba

**Contoh:**
```
**Operating System:** macOS 12.0
**Python Version:** 3.9.7
**Error Message:** ModuleNotFoundError: No module named 'pandas'
**Steps to Reproduce:**
1. Activated virtual environment
2. Started Jupyter notebook
3. Tried to import pandas

**What I've Tried:**
- Ran pip install pandas
- Restarted Jupyter
```

### Sumber Daya Komunitas

- **GitHub Issues**: [Buat issue](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Bergabung dengan komunitas kami](https://aka.ms/ds4beginners/discord)
- **Diskusi**: [Diskusi GitHub](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Forum Tanya Jawab](https://docs.microsoft.com/answers/)

### Dokumentasi Terkait

- [INSTALLATION.md](INSTALLATION.md) - Instruksi pengaturan
- [USAGE.md](USAGE.md) - Cara menggunakan kurikulum
- [CONTRIBUTING.md](CONTRIBUTING.md) - Cara berkontribusi
- [README.md](README.md) - Gambaran proyek

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.