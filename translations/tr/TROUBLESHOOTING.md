<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:39:08+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "tr"
}
-->
# Sorun Giderme Kılavuzu

Bu kılavuz, Data Science for Beginners müfredatıyla çalışırken karşılaşabileceğiniz yaygın sorunlara çözümler sunar.

## İçindekiler

- [Python ve Jupyter Sorunları](../..)
- [Paket ve Bağımlılık Sorunları](../..)
- [Jupyter Notebook Sorunları](../..)
- [Quiz Uygulaması Sorunları](../..)
- [Git ve GitHub Sorunları](../..)
- [Docsify Dokümantasyon Sorunları](../..)
- [Veri ve Dosya Sorunları](../..)
- [Performans Sorunları](../..)
- [Ek Yardım Alma](../..)

## Python ve Jupyter Sorunları

### Python Bulunamadı veya Yanlış Sürüm

**Sorun:** `python: command not found` veya yanlış Python sürümü

**Çözüm:**

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

**Windows Çözümü:**
1. [python.org](https://www.python.org/) adresinden Python'u yeniden yükleyin.
2. Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin.
3. Terminali/komut istemini yeniden başlatın.

### Sanal Ortam Aktifleştirme Sorunları

**Sorun:** Sanal ortam aktifleştirilemiyor

**Çözüm:**

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

**Aktivasyonu doğrulayın:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter Çekirdek Sorunları

**Sorun:** "Kernel not found" veya "Kernel keeps dying"

**Çözüm:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Sorun:** Jupyter'de yanlış Python sürümü

**Çözüm:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Paket ve Bağımlılık Sorunları

### İçe Aktarma Hataları

**Sorun:** `ModuleNotFoundError: No module named 'pandas'` (veya diğer paketler)

**Çözüm:**

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

### Pip Kurulum Hataları

**Sorun:** `pip install` izin hatalarıyla başarısız oluyor

**Çözüm:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Sorun:** `pip install` SSL sertifika hatalarıyla başarısız oluyor

**Çözüm:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Paket Sürüm Çakışmaları

**Sorun:** Uyumsuz paket sürümleri

**Çözüm:**

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

## Jupyter Notebook Sorunları

### Jupyter Başlamıyor

**Sorun:** `jupyter notebook` komutu bulunamadı

**Çözüm:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook Yüklenmiyor veya Kaydedilmiyor

**Sorun:** "Notebook failed to load" veya kaydetme hataları

**Çözüm:**

1. Dosya izinlerini kontrol edin.
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Dosya bozulmalarını kontrol edin.
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Jupyter önbelleğini temizleyin.
```bash
jupyter notebook --clear-cache
```

### Hücre Çalışmıyor

**Sorun:** Hücre "In [*]" durumunda takılı kalıyor veya çok uzun sürüyor

**Çözüm:**

1. **Çekirdeği durdurun**: "Interrupt" düğmesine tıklayın veya `I, I` tuşlarına basın.
2. **Çekirdeği yeniden başlatın**: Kernel menüsü → Restart
3. Kodunuzda **sonsuz döngüleri kontrol edin**.
4. **Çıktıyı temizleyin**: Cell → All Output → Clear

### Grafikler Görünmüyor

**Sorun:** `matplotlib` grafikler notebook'ta görünmüyor

**Çözüm:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Etkileşimli grafikler için alternatif:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Quiz Uygulaması Sorunları

### npm install Başarısız

**Sorun:** `npm install` sırasında hatalar

**Çözüm:**

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

### Quiz Uygulaması Başlamıyor

**Sorun:** `npm run serve` başarısız oluyor

**Çözüm:**

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

### Port Zaten Kullanımda

**Sorun:** "Port 8080 is already in use"

**Çözüm:**

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

### Quiz Yüklenmiyor veya Boş Sayfa

**Sorun:** Quiz uygulaması yükleniyor ama boş sayfa gösteriyor

**Çözüm:**

1. Tarayıcı konsolunda hataları kontrol edin (F12).
2. Tarayıcı önbelleğini ve çerezleri temizleyin.
3. Farklı bir tarayıcı deneyin.
4. JavaScript'in etkin olduğundan emin olun.
5. Reklam engelleyicilerin müdahale edip etmediğini kontrol edin.

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git ve GitHub Sorunları

### Git Tanınmıyor

**Sorun:** `git: command not found`

**Çözüm:**

**Windows:**
- [git-scm.com](https://git-scm.com/) adresinden Git'i yükleyin.
- Kurulumdan sonra terminali yeniden başlatın.

**macOS:**

> **Not:** Homebrew yüklü değilse, önce [https://brew.sh/](https://brew.sh/) adresindeki talimatları takip ederek yükleyin.
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

### Klonlama Başarısız

**Sorun:** `git clone` kimlik doğrulama hatalarıyla başarısız oluyor

**Çözüm:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### İzin Reddedildi (publickey)

**Sorun:** SSH anahtar kimlik doğrulaması başarısız oluyor

**Çözüm:**

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

## Docsify Dokümantasyon Sorunları

### Docsify Komutu Bulunamadı

**Sorun:** `docsify: command not found`

**Çözüm:**

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

### Dokümantasyon Yüklenmiyor

**Sorun:** Docsify çalışıyor ama içerik yüklenmiyor

**Çözüm:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Görseller Görünmüyor

**Sorun:** Görseller kırık bağlantı simgesi gösteriyor

**Çözüm:**

1. Görsel yollarının göreceli olduğundan emin olun.
2. Görsel dosyalarının depoda mevcut olduğundan emin olun.
3. Tarayıcı önbelleğini temizleyin.
4. Dosya uzantılarının eşleştiğini doğrulayın (bazı sistemlerde büyük/küçük harf duyarlıdır).

## Veri ve Dosya Sorunları

### Dosya Bulunamadı Hataları

**Sorun:** `FileNotFoundError` veri yüklenirken

**Çözüm:**

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

### CSV Okuma Hataları

**Sorun:** CSV dosyalarını okurken hatalar

**Çözüm:**

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

### Büyük Veri Setlerinde Bellek Hataları

**Sorun:** Büyük dosyalar yüklenirken `MemoryError`

**Çözüm:**

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

## Performans Sorunları

### Yavaş Notebook Performansı

**Sorun:** Notebook'lar çok yavaş çalışıyor

**Çözüm:**

1. **Çekirdeği yeniden başlatın ve çıktıyı temizleyin**
   - Kernel → Restart & Clear Output

2. **Kullanılmayan notebook'ları kapatın**

3. **Kodunuzu optimize edin:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Büyük veri setlerini örnekleyin:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Tarayıcı Çökmesi

**Sorun:** Tarayıcı çöküyor veya yanıt vermiyor

**Çözüm:**

1. Kullanılmayan sekmeleri kapatın.
2. Tarayıcı önbelleğini temizleyin.
3. Tarayıcı belleğini artırın (Chrome: `chrome://settings/system`).
4. JupyterLab kullanın:
```bash
pip install jupyterlab
jupyter lab
```

## Ek Yardım Alma

### Yardım İstemeden Önce

1. Bu sorun giderme kılavuzunu kontrol edin.
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) üzerinde arama yapın.
3. [INSTALLATION.md](INSTALLATION.md) ve [USAGE.md](USAGE.md) dosyalarını inceleyin.
4. Hata mesajını çevrimiçi aramayı deneyin.

### Yardım İsterken

Bir sorun oluştururken veya yardım isterken şunları ekleyin:

1. **İşletim Sistemi**: Windows, macOS veya Linux (hangi dağıtım)
2. **Python Sürümü**: `python --version` komutunu çalıştırın.
3. **Hata Mesajı**: Tam hata mesajını kopyalayın.
4. **Yeniden Üretme Adımları**: Hata oluşmadan önce yaptıklarınız.
5. **Denediğiniz Çözümler**: Daha önce denediğiniz çözümler.

**Örnek:**
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

### Topluluk Kaynakları

- **GitHub Issues**: [Sorun oluşturun](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Topluluğumuza katılın](https://aka.ms/ds4beginners/discord)
- **Tartışmalar**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Soru-Cevap Forumları](https://docs.microsoft.com/answers/)

### İlgili Dokümantasyon

- [INSTALLATION.md](INSTALLATION.md) - Kurulum talimatları
- [USAGE.md](USAGE.md) - Müfredatın nasıl kullanılacağı
- [CONTRIBUTING.md](CONTRIBUTING.md) - Katkıda bulunma rehberi
- [README.md](README.md) - Proje genel bakışı

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.