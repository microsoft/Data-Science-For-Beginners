<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:20:25+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "tr"
}
-->
# Kurulum Kılavuzu

Bu kılavuz, Başlangıç Seviyesi Veri Bilimi müfredatıyla çalışmak için ortamınızı nasıl kuracağınızı gösterecek.

## İçindekiler

- [Ön Koşullar](../..)
- [Hızlı Başlangıç Seçenekleri](../..)
- [Yerel Kurulum](../..)
- [Kurulumunuzu Doğrulayın](../..)

## Ön Koşullar

Başlamadan önce şunlara sahip olmalısınız:

- Komut satırı/terminal konusunda temel bilgi
- Bir GitHub hesabı (ücretsiz)
- İlk kurulum için stabil bir internet bağlantısı

## Hızlı Başlangıç Seçenekleri

### Seçenek 1: GitHub Codespaces (Yeni Başlayanlar için Önerilir)

Başlamak için en kolay yol, tarayıcınızda tam bir geliştirme ortamı sağlayan GitHub Codespaces kullanmaktır.

1. [Depoya](https://github.com/microsoft/Data-Science-For-Beginners) gidin
2. **Code** açılır menüsüne tıklayın
3. **Codespaces** sekmesini seçin
4. **Create codespace on main** seçeneğine tıklayın
5. Ortamın başlatılmasını bekleyin (2-3 dakika)

Ortamınız artık tüm bağımlılıklarla birlikte hazır!

### Seçenek 2: Yerel Geliştirme

Kendi bilgisayarınızda çalışmak için aşağıdaki ayrıntılı talimatları izleyin.

## Yerel Kurulum

### Adım 1: Git'i Kurun

Git, depoyu klonlamak ve değişikliklerinizi takip etmek için gereklidir.

**Windows:**
- [git-scm.com](https://git-scm.com/download/win) adresinden indirin
- Varsayılan ayarlarla yükleyiciyi çalıştırın

**macOS:**
- Homebrew ile yükleyin: `brew install git`
- Ya da [git-scm.com](https://git-scm.com/download/mac) adresinden indirin

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

### Adım 2: Depoyu Klonlayın

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Adım 3: Python ve Jupyter'i Kurun

Veri bilimi dersleri için Python 3.7 veya üstü gereklidir.

**Windows:**
1. [python.org](https://www.python.org/downloads/) adresinden Python'u indirin
2. Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin
3. Kurulumu doğrulayın:
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

### Adım 4: Python Ortamını Ayarlayın

Bağımlılıkları izole etmek için sanal bir ortam kullanmanız önerilir.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Adım 5: Python Paketlerini Kurun

Gerekli veri bilimi kütüphanelerini yükleyin:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Adım 6: Node.js ve npm'i Kurun (Quiz Uygulaması için)

Quiz uygulaması Node.js ve npm gerektirir.

**Windows/macOS:**
- [nodejs.org](https://nodejs.org/) adresinden indirin (LTS sürümü önerilir)
- Yükleyiciyi çalıştırın

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

### Adım 7: Quiz Uygulaması Bağımlılıklarını Kurun

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Adım 8: Docsify'i Kurun (Opsiyonel)

Dokümantasyona çevrimdışı erişim için:

```bash
npm install -g docsify-cli
```

## Kurulumunuzu Doğrulayın

### Python ve Jupyter'i Test Edin

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Tarayıcınız Jupyter arayüzüyle açılmalıdır. Artık herhangi bir dersin `.ipynb` dosyasına gidebilirsiniz.

### Quiz Uygulamasını Test Edin

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Quiz uygulaması `http://localhost:8080` adresinde (veya 8080 meşgulse başka bir portta) kullanılabilir olmalıdır.

### Dokümantasyon Sunucusunu Test Edin

```bash
# From the root directory of the repository
docsify serve
```

Dokümantasyon `http://localhost:3000` adresinde kullanılabilir olmalıdır.

## VS Code Dev Containers Kullanımı

Docker yüklüyse, VS Code Dev Containers kullanabilirsiniz:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) yükleyin
2. [Visual Studio Code](https://code.visualstudio.com/) yükleyin
3. [Remote - Containers eklentisini](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) yükleyin
4. Depoyu VS Code'da açın
5. `F1` tuşuna basın ve "Remote-Containers: Reopen in Container" seçeneğini seçin
6. Konteynerin oluşturulmasını bekleyin (sadece ilk seferde)

## Sonraki Adımlar

- Müfredatın genel bir görünümü için [README.md](README.md) dosyasını inceleyin
- Yaygın iş akışları ve örnekler için [USAGE.md](USAGE.md) dosyasını okuyun
- Sorunlarla karşılaşırsanız [TROUBLESHOOTING.md](TROUBLESHOOTING.md) dosyasını kontrol edin
- Katkıda bulunmak istiyorsanız [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını gözden geçirin

## Yardım Alma

Sorunlarla karşılaşırsanız:

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) kılavuzunu kontrol edin
2. Mevcut [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) aramalarını yapın
3. [Discord topluluğumuza](https://aka.ms/ds4beginners/discord) katılın
4. Sorununuz hakkında ayrıntılı bilgi içeren yeni bir issue oluşturun

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.