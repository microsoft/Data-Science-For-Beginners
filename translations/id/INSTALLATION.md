<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:23:10+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "id"
}
-->
# Panduan Instalasi

Panduan ini akan membantu Anda menyiapkan lingkungan untuk bekerja dengan kurikulum Data Science untuk Pemula.

## Daftar Isi

- [Prasyarat](../..)
- [Opsi Mulai Cepat](../..)
- [Instalasi Lokal](../..)
- [Verifikasi Instalasi Anda](../..)

## Prasyarat

Sebelum memulai, pastikan Anda memiliki:

- Pemahaman dasar tentang command line/terminal
- Akun GitHub (gratis)
- Koneksi internet yang stabil untuk pengaturan awal

## Opsi Mulai Cepat

### Opsi 1: GitHub Codespaces (Direkomendasikan untuk Pemula)

Cara termudah untuk memulai adalah dengan GitHub Codespaces, yang menyediakan lingkungan pengembangan lengkap di browser Anda.

1. Buka [repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klik menu dropdown **Code**
3. Pilih tab **Codespaces**
4. Klik **Create codespace on main**
5. Tunggu hingga lingkungan selesai diinisialisasi (2-3 menit)

Lingkungan Anda sekarang siap dengan semua dependensi yang sudah diinstal!

### Opsi 2: Pengembangan Lokal

Untuk bekerja di komputer Anda sendiri, ikuti instruksi rinci di bawah ini.

## Instalasi Lokal

### Langkah 1: Instal Git

Git diperlukan untuk mengkloning repository dan melacak perubahan Anda.

**Windows:**
- Unduh dari [git-scm.com](https://git-scm.com/download/win)
- Jalankan installer dengan pengaturan default

**macOS:**
- Instal melalui Homebrew: `brew install git`
- Atau unduh dari [git-scm.com](https://git-scm.com/download/mac)

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### Langkah 2: Kloning Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Langkah 3: Instal Python dan Jupyter

Python 3.7 atau versi lebih tinggi diperlukan untuk pelajaran data science.

**Windows:**
1. Unduh Python dari [python.org](https://www.python.org/downloads/)
2. Saat instalasi, centang "Add Python to PATH"
3. Verifikasi instalasi:
```bash
python --version
```

**macOS:**
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

**Linux:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### Langkah 4: Siapkan Lingkungan Python

Disarankan untuk menggunakan virtual environment agar dependensi tetap terisolasi.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Langkah 5: Instal Paket Python

Instal pustaka data science yang diperlukan:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Langkah 6: Instal Node.js dan npm (Untuk Aplikasi Kuis)

Aplikasi kuis memerlukan Node.js dan npm.

**Windows/macOS:**
- Unduh dari [nodejs.org](https://nodejs.org/) (versi LTS direkomendasikan)
- Jalankan installer

**Linux:**
```bash
# Debian/Ubuntu
# WARNING: Piping scripts from the internet directly into bash can be a security risk.
# It is recommended to review the script before running it:
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# Then run:
#   sudo -E bash setup_lts.x
#
# Alternatively, you can use the one-liner below at your own risk:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Fedora
sudo dnf install nodejs

# Verify installation
node --version
npm --version
```

### Langkah 7: Instal Dependensi Aplikasi Kuis

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Langkah 8: Instal Docsify (Opsional)

Untuk akses offline ke dokumentasi:

```bash
npm install -g docsify-cli
```

## Verifikasi Instalasi Anda

### Uji Python dan Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Browser Anda seharusnya terbuka dengan antarmuka Jupyter. Anda sekarang dapat menavigasi ke file `.ipynb` dari pelajaran mana pun.

### Uji Aplikasi Kuis

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Aplikasi kuis seharusnya tersedia di `http://localhost:8080` (atau port lain jika 8080 sudah digunakan).

### Uji Server Dokumentasi

```bash
# From the root directory of the repository
docsify serve
```

Dokumentasi seharusnya tersedia di `http://localhost:3000`.

## Menggunakan VS Code Dev Containers

Jika Anda memiliki Docker yang terinstal, Anda dapat menggunakan VS Code Dev Containers:

1. Instal [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Instal [Visual Studio Code](https://code.visualstudio.com/)
3. Instal ekstensi [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Buka repository di VS Code
5. Tekan `F1` dan pilih "Remote-Containers: Reopen in Container"
6. Tunggu hingga container selesai dibangun (hanya pertama kali)

## Langkah Selanjutnya

- Jelajahi [README.md](README.md) untuk gambaran umum kurikulum
- Baca [USAGE.md](USAGE.md) untuk alur kerja dan contoh umum
- Periksa [TROUBLESHOOTING.md](TROUBLESHOOTING.md) jika Anda mengalami masalah
- Tinjau [CONTRIBUTING.md](CONTRIBUTING.md) jika Anda ingin berkontribusi

## Mendapatkan Bantuan

Jika Anda mengalami masalah:

1. Periksa panduan [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Cari [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) yang sudah ada
3. Bergabunglah dengan [komunitas Discord kami](https://aka.ms/ds4beginners/discord)
4. Buat issue baru dengan informasi rinci tentang masalah Anda

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.