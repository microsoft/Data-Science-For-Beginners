<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:23:26+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "ms"
}
-->
# Panduan Pemasangan

Panduan ini akan membantu anda menyediakan persekitaran untuk bekerja dengan kurikulum Data Science for Beginners.

## Kandungan

- [Keperluan Awal](../..)
- [Pilihan Permulaan Pantas](../..)
- [Pemasangan Tempatan](../..)
- [Sahkan Pemasangan Anda](../..)

## Keperluan Awal

Sebelum anda bermula, anda perlu mempunyai:

- Pemahaman asas tentang baris perintah/terminal
- Akaun GitHub (percuma)
- Sambungan internet yang stabil untuk persediaan awal

## Pilihan Permulaan Pantas

### Pilihan 1: GitHub Codespaces (Disyorkan untuk Pemula)

Cara paling mudah untuk bermula adalah dengan GitHub Codespaces, yang menyediakan persekitaran pembangunan lengkap dalam pelayar anda.

1. Pergi ke [repositori](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klik menu dropdown **Code**
3. Pilih tab **Codespaces**
4. Klik **Create codespace on main**
5. Tunggu persekitaran untuk diinisialisasi (2-3 minit)

Persekitaran anda kini sedia dengan semua kebergantungan yang telah dipasang!

### Pilihan 2: Pembangunan Tempatan

Untuk bekerja di komputer anda sendiri, ikuti arahan terperinci di bawah.

## Pemasangan Tempatan

### Langkah 1: Pasang Git

Git diperlukan untuk mengklon repositori dan menjejaki perubahan anda.

**Windows:**
- Muat turun dari [git-scm.com](https://git-scm.com/download/win)
- Jalankan pemasang dengan tetapan lalai

**macOS:**
- Pasang melalui Homebrew: `brew install git`
- Atau muat turun dari [git-scm.com](https://git-scm.com/download/mac)

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

### Langkah 2: Klon Repositori

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Langkah 3: Pasang Python dan Jupyter

Python 3.7 atau lebih tinggi diperlukan untuk pelajaran sains data.

**Windows:**
1. Muat turun Python dari [python.org](https://www.python.org/downloads/)
2. Semasa pemasangan, tandakan "Add Python to PATH"
3. Sahkan pemasangan:
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

### Langkah 4: Sediakan Persekitaran Python

Disyorkan untuk menggunakan persekitaran maya untuk memastikan kebergantungan terasing.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Langkah 5: Pasang Pakej Python

Pasang perpustakaan sains data yang diperlukan:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Langkah 6: Pasang Node.js dan npm (Untuk Aplikasi Kuiz)

Aplikasi kuiz memerlukan Node.js dan npm.

**Windows/macOS:**
- Muat turun dari [nodejs.org](https://nodejs.org/) (versi LTS disyorkan)
- Jalankan pemasang

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

### Langkah 7: Pasang Kebergantungan Aplikasi Kuiz

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Langkah 8: Pasang Docsify (Pilihan)

Untuk akses dokumentasi secara luar talian:

```bash
npm install -g docsify-cli
```

## Sahkan Pemasangan Anda

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

Pelayar anda sepatutnya terbuka dengan antara muka Jupyter. Anda kini boleh menavigasi ke fail `.ipynb` mana-mana pelajaran.

### Uji Aplikasi Kuiz

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Aplikasi kuiz sepatutnya tersedia di `http://localhost:8080` (atau port lain jika 8080 sibuk).

### Uji Pelayan Dokumentasi

```bash
# From the root directory of the repository
docsify serve
```

Dokumentasi sepatutnya tersedia di `http://localhost:3000`.

## Menggunakan VS Code Dev Containers

Jika anda mempunyai Docker yang dipasang, anda boleh menggunakan VS Code Dev Containers:

1. Pasang [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Pasang [Visual Studio Code](https://code.visualstudio.com/)
3. Pasang [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Buka repositori dalam VS Code
5. Tekan `F1` dan pilih "Remote-Containers: Reopen in Container"
6. Tunggu kontena untuk dibina (hanya kali pertama)

## Langkah Seterusnya

- Terokai [README.md](README.md) untuk gambaran keseluruhan kurikulum
- Baca [USAGE.md](USAGE.md) untuk aliran kerja dan contoh biasa
- Semak [TROUBLESHOOTING.md](TROUBLESHOOTING.md) jika anda menghadapi masalah
- Tinjau [CONTRIBUTING.md](CONTRIBUTING.md) jika anda ingin menyumbang

## Mendapatkan Bantuan

Jika anda menghadapi masalah:

1. Semak panduan [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Cari [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) yang sedia ada
3. Sertai komuniti [Discord kami](https://aka.ms/ds4beginners/discord)
4. Cipta isu baru dengan maklumat terperinci tentang masalah anda

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.