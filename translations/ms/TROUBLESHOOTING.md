<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:44:12+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "ms"
}
-->
# Panduan Penyelesaian Masalah

Panduan ini menyediakan penyelesaian untuk isu-isu biasa yang mungkin anda hadapi semasa menggunakan kurikulum Data Science for Beginners.

## Kandungan

- [Isu Python dan Jupyter](../..)
- [Isu Pakej dan Kebergantungan](../..)
- [Isu Jupyter Notebook](../..)
- [Isu Aplikasi Kuiz](../..)
- [Isu Git dan GitHub](../..)
- [Isu Dokumentasi Docsify](../..)
- [Isu Data dan Fail](../..)
- [Isu Prestasi](../..)
- [Mendapatkan Bantuan Tambahan](../..)

## Isu Python dan Jupyter

### Python Tidak Ditemui atau Versi Salah

**Masalah:** `python: command not found` atau versi Python salah

**Penyelesaian:**

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

**Penyelesaian Windows:**
1. Pasang semula Python dari [python.org](https://www.python.org/)
2. Semasa pemasangan, tandakan "Add Python to PATH"
3. Mulakan semula terminal/command prompt anda

### Isu Pengaktifan Persekitaran Maya

**Masalah:** Persekitaran maya tidak dapat diaktifkan

**Penyelesaian:**

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

**Sahkan pengaktifan:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Isu Kernel Jupyter

**Masalah:** "Kernel tidak ditemui" atau "Kernel terus mati"

**Penyelesaian:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Masalah:** Versi Python salah dalam Jupyter

**Penyelesaian:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Isu Pakej dan Kebergantungan

### Ralat Import

**Masalah:** `ModuleNotFoundError: No module named 'pandas'` (atau pakej lain)

**Penyelesaian:**

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

### Kegagalan Pemasangan Pip

**Masalah:** `pip install` gagal dengan ralat kebenaran

**Penyelesaian:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Masalah:** `pip install` gagal dengan ralat sijil SSL

**Penyelesaian:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Konflik Versi Pakej

**Masalah:** Versi pakej tidak serasi

**Penyelesaian:**

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

## Isu Jupyter Notebook

### Jupyter Tidak Dapat Dimulakan

**Masalah:** Perintah `jupyter notebook` tidak ditemui

**Penyelesaian:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook Tidak Dapat Dimuat atau Disimpan

**Masalah:** "Notebook gagal dimuat" atau ralat simpan

**Penyelesaian:**

1. Periksa kebenaran fail
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Periksa kerosakan fail
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Kosongkan cache Jupyter
```bash
jupyter notebook --clear-cache
```

### Sel Tidak Dapat Dilaksanakan

**Masalah:** Sel tersekat pada "In [*]" atau mengambil masa terlalu lama

**Penyelesaian:**

1. **Ganggu kernel**: Klik butang "Interrupt" atau tekan `I, I`
2. **Mulakan semula kernel**: Menu Kernel → Restart
3. **Periksa gelung tak terhingga** dalam kod anda
4. **Kosongkan output**: Cell → All Output → Clear

### Plot Tidak Ditampilkan

**Masalah:** Plot `matplotlib` tidak muncul dalam notebook

**Penyelesaian:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternatif untuk plot interaktif:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Isu Aplikasi Kuiz

### npm install Gagal

**Masalah:** Ralat semasa `npm install`

**Penyelesaian:**

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

### Aplikasi Kuiz Tidak Dapat Dimulakan

**Masalah:** `npm run serve` gagal

**Penyelesaian:**

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

**Penyelesaian:**

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

### Kuiz Tidak Dimuat atau Halaman Kosong

**Masalah:** Aplikasi kuiz dimuat tetapi menunjukkan halaman kosong

**Penyelesaian:**

1. Periksa konsol pelayar untuk ralat (F12)
2. Kosongkan cache dan kuki pelayar
3. Cuba pelayar lain
4. Pastikan JavaScript diaktifkan
5. Periksa jika penapis iklan mengganggu

```bash
# Rebuild the app
npm run build
npm run serve
```

## Isu Git dan GitHub

### Git Tidak Dikenali

**Masalah:** `git: command not found`

**Penyelesaian:**

**Windows:**
- Pasang Git dari [git-scm.com](https://git-scm.com/)
- Mulakan semula terminal selepas pemasangan

**macOS:**

> **Nota:** Jika anda belum memasang Homebrew, ikuti arahan di [https://brew.sh/](https://brew.sh/) untuk memasangnya terlebih dahulu.
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

**Masalah:** `git clone` gagal dengan ralat pengesahan

**Penyelesaian:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Kebenaran Ditolak (publickey)

**Masalah:** Pengesahan kunci SSH gagal

**Penyelesaian:**

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

## Isu Dokumentasi Docsify

### Perintah Docsify Tidak Ditemui

**Masalah:** `docsify: command not found`

**Penyelesaian:**

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

**Masalah:** Docsify berfungsi tetapi kandungan tidak dimuat

**Penyelesaian:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Imej Tidak Ditampilkan

**Masalah:** Imej menunjukkan ikon pautan rosak

**Penyelesaian:**

1. Periksa laluan imej adalah relatif
2. Pastikan fail imej wujud dalam repositori
3. Kosongkan cache pelayar
4. Sahkan sambungan fail sepadan (case-sensitive pada sesetengah sistem)

## Isu Data dan Fail

### Ralat Fail Tidak Ditemui

**Masalah:** `FileNotFoundError` semasa memuatkan data

**Penyelesaian:**

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

### Ralat Membaca CSV

**Masalah:** Ralat membaca fail CSV

**Penyelesaian:**

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

### Ralat Memori dengan Dataset Besar

**Masalah:** `MemoryError` semasa memuatkan fail besar

**Penyelesaian:**

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

## Isu Prestasi

### Prestasi Notebook Perlahan

**Masalah:** Notebook berjalan sangat perlahan

**Penyelesaian:**

1. **Mulakan semula kernel dan kosongkan output**
   - Kernel → Restart & Clear Output

2. **Tutup notebook yang tidak digunakan**

3. **Optimumkan kod:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Sampel dataset besar:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Pelayar Terhenti

**Masalah:** Pelayar terhenti atau tidak responsif

**Penyelesaian:**

1. Tutup tab yang tidak digunakan
2. Kosongkan cache pelayar
3. Tingkatkan memori pelayar (Chrome: `chrome://settings/system`)
4. Gunakan JupyterLab sebagai alternatif:
```bash
pip install jupyterlab
jupyter lab
```

## Mendapatkan Bantuan Tambahan

### Sebelum Meminta Bantuan

1. Periksa panduan penyelesaian masalah ini
2. Cari [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Semak [INSTALLATION.md](INSTALLATION.md) dan [USAGE.md](USAGE.md)
4. Cuba cari mesej ralat secara dalam talian

### Cara Meminta Bantuan

Apabila membuat isu atau meminta bantuan, sertakan:

1. **Sistem Operasi**: Windows, macOS, atau Linux (distribusi mana)
2. **Versi Python**: Jalankan `python --version`
3. **Mesej Ralat**: Salin mesej ralat lengkap
4. **Langkah untuk Menghasilkan Semula**: Apa yang anda lakukan sebelum ralat berlaku
5. **Apa yang Anda Cuba**: Penyelesaian yang telah anda cuba

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

### Sumber Komuniti

- **GitHub Issues**: [Buat isu](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Sertai komuniti kami](https://aka.ms/ds4beginners/discord)
- **Perbincangan**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Forum Q&A](https://docs.microsoft.com/answers/)

### Dokumentasi Berkaitan

- [INSTALLATION.md](INSTALLATION.md) - Arahan pemasangan
- [USAGE.md](USAGE.md) - Cara menggunakan kurikulum
- [CONTRIBUTING.md](CONTRIBUTING.md) - Cara menyumbang
- [README.md](README.md) - Gambaran keseluruhan projek

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.