<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:20:18+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tr"
}
-->
# AGENTS.md

## Proje Genel Bakış

Başlangıç seviyesindeki Veri Bilimi, Microsoft Azure Cloud Advocates tarafından oluşturulan kapsamlı bir 10 haftalık, 20 derslik müfredattır. Bu depo, Jupyter defterleri, interaktif testler ve uygulamalı ödevler içeren proje tabanlı derslerle temel veri bilimi kavramlarını öğretmek için bir öğrenme kaynağıdır.

**Anahtar Teknolojiler:**
- **Jupyter Notebooks**: Python 3 kullanılarak birincil öğrenme aracı
- **Python Kütüphaneleri**: pandas, numpy, matplotlib veri analizi ve görselleştirme için
- **Vue.js 2**: Test uygulaması (quiz-app klasörü)
- **Docsify**: Çevrimdışı erişim için dokümantasyon sitesi oluşturucu
- **Node.js/npm**: JavaScript bileşenleri için paket yönetimi
- **Markdown**: Tüm ders içeriği ve dokümantasyon

**Mimari:**
- Çok dilli eğitim deposu, kapsamlı çevirilerle
- Ders modüllerine yapılandırılmış (1-Giriş'ten 6-Vahşi Veri Bilimi'ne kadar)
- Her ders README, defterler, ödevler ve testler içerir
- Bağımsız Vue.js test uygulaması, ders öncesi/sonrası değerlendirmeler için
- GitHub Codespaces ve VS Code geliştirme konteynerleri desteği

## Kurulum Komutları

### Depo Kurulumu
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python Ortamı Kurulumu
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Test Uygulaması Kurulumu
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

### Docsify Dokümantasyon Sunucusu
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Görselleştirme Projeleri Kurulumu
Örneğin anlamlı görselleştirmeler (ders 13) için:
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


## Geliştirme İş Akışı

### Jupyter Notebooks ile Çalışma
1. Depo kökünde Jupyter'i başlatın: `jupyter notebook`
2. İstediğiniz ders klasörüne gidin
3. Egzersizleri çalışmak için `.ipynb` dosyalarını açın
4. Defterler, açıklamalar ve kod hücreleri ile kendi içinde açıklayıcıdır
5. Çoğu defter pandas, numpy ve matplotlib kullanır - bunların yüklü olduğundan emin olun

### Ders Yapısı
Her ders genellikle şunları içerir:
- `README.md` - Teori ve örneklerle ana ders içeriği
- `notebook.ipynb` - Uygulamalı Jupyter defteri egzersizleri
- `assignment.ipynb` veya `assignment.md` - Uygulama ödevleri
- `solution/` klasörü - Çözüm defterleri ve kodları
- `images/` klasörü - Destekleyici görsel materyaller

### Test Uygulaması Geliştirme
- Vue.js 2 uygulaması, geliştirme sırasında sıcak yükleme ile
- Testler `quiz-app/src/assets/translations/` içinde saklanır
- Her dilin kendi çeviri klasörü vardır (en, fr, es, vb.)
- Test numaralandırması 0'dan başlar ve 39'a kadar gider (toplam 40 test)

### Çeviriler Eklemek
- Çeviriler depo kökündeki `translations/` klasörüne gider
- Her dil, İngilizce yapıdan aynen kopyalanır
- GitHub Actions ile otomatik çeviri (co-op-translator.yml)

## Test Talimatları

### Test Uygulaması Testi
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Defter Testi
- Defterler için otomatik test çerçevesi yoktur
- Manuel doğrulama: Tüm hücreleri sırayla çalıştırarak hata olmadığından emin olun
- Veri dosyalarının erişilebilir olduğunu ve çıktılarının doğru şekilde üretildiğini doğrulayın
- Görselleştirmelerin düzgün şekilde oluşturulduğunu kontrol edin

### Dokümantasyon Testi
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Kod Kalitesi Kontrolleri
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Kod Stili Yönergeleri

### Python (Jupyter Notebooks)
- Python kodu için PEP 8 stil yönergelerini takip edin
- Analiz edilen veriyi açıklayan açık değişken adları kullanın
- Kod hücrelerinden önce açıklamalar içeren markdown hücreleri ekleyin
- Kod hücrelerini tek bir kavram veya işlem üzerinde odaklanmış tutun
- Veri manipülasyonu için pandas, görselleştirme için matplotlib kullanın
- Yaygın import deseni:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Vue.js 2 stil rehberi ve en iyi uygulamaları takip edin
- `quiz-app/package.json` içinde ESLint yapılandırması
- Vue tek dosya bileşenleri (.vue dosyaları) kullanın
- Bileşen tabanlı mimariyi koruyun
- Değişiklikleri göndermeden önce `npm run lint` çalıştırın

### Markdown Dokümantasyonu
- Açık başlık hiyerarşisi kullanın (# ## ### vb.)
- Dil belirleyicilerle kod blokları ekleyin
- Görseller için alt metin ekleyin
- İlgili derslere ve kaynaklara bağlantı verin
- Okunabilirlik için satır uzunluklarını makul tutun

### Dosya Organizasyonu
- Ders içeriği numaralandırılmış klasörlerde (01-defining-data-science, vb.)
- Çözümler özel `solution/` alt klasörlerinde
- Çeviriler İngilizce yapıyı `translations/` klasöründe yansıtır
- Veri dosyalarını `data/` veya ders özel klasörlerinde tutun

## Derleme ve Dağıtım

### Test Uygulaması Dağıtımı
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps Dağıtımı
Test uygulaması Azure Static Web Apps'e dağıtılabilir:
1. Azure Static Web App kaynağı oluşturun
2. GitHub deposuna bağlanın
3. Derleme ayarlarını yapılandırın:
   - Uygulama konumu: `quiz-app`
   - Çıktı konumu: `dist`
4. GitHub Actions iş akışı, gönderim üzerine otomatik olarak dağıtım yapar

### Dokümantasyon Sitesi
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Depo, geliştirme konteyner yapılandırması içerir
- Codespaces, Python ve Node.js ortamını otomatik olarak kurar
- GitHub arayüzü üzerinden depoyu Codespace'de açın
- Tüm bağımlılıklar otomatik olarak yüklenir

## Çekme İsteği Yönergeleri

### Göndermeden Önce
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR Başlık Formatı
- Açık, açıklayıcı başlıklar kullanın
- Format: `[Bileşen] Kısa açıklama`
- Örnekler:
  - `[Ders 7] Python defteri import hatasını düzelt`
  - `[Test Uygulaması] Almanca çeviri ekle`
  - `[Dokümanlar] Yeni ön koşullarla README'yi güncelle`

### Gerekli Kontroller
- Tüm kodun hatasız çalıştığından emin olun
- Defterlerin tamamen çalıştığını doğrulayın
- Vue.js uygulamalarının başarıyla derlendiğini doğrulayın
- Dokümantasyon bağlantılarının çalıştığını kontrol edin
- Test uygulamasını değiştirilmişse test edin
- Çevirilerin tutarlı yapı koruduğunu doğrulayın

### Katkı Yönergeleri
- Mevcut kod stilini ve desenlerini takip edin
- Karmaşık mantık için açıklayıcı yorumlar ekleyin
- İlgili dokümantasyonu güncelleyin
- Değişiklikleri farklı ders modüllerinde test edin (uygulanabilir ise)
- CONTRIBUTING.md dosyasını inceleyin

## Ek Notlar

### Kullanılan Yaygın Kütüphaneler
- **pandas**: Veri manipülasyonu ve analizi
- **numpy**: Sayısal hesaplama
- **matplotlib**: Veri görselleştirme ve grafik çizimi
- **seaborn**: İstatistiksel veri görselleştirme (bazı derslerde)
- **scikit-learn**: Makine öğrenimi (ileri düzey derslerde)

### Veri Dosyaları ile Çalışma
- Veri dosyaları `data/` klasöründe veya ders özel dizinlerinde bulunur
- Çoğu defter, veri dosyalarını göreceli yollarda bekler
- CSV dosyaları birincil veri formatıdır
- Bazı dersler, ilişkisel olmayan veri örnekleri için JSON kullanır

### Çok Dilli Destek
- 40+ dil çevirisi, otomatik GitHub Actions ile
- Çeviri iş akışı `.github/workflows/co-op-translator.yml` içinde
- Çeviriler `translations/` klasöründe dil kodları ile
- Test çevirileri `quiz-app/src/assets/translations/` içinde

### Geliştirme Ortamı Seçenekleri
1. **Yerel Geliştirme**: Python, Jupyter, Node.js yerel olarak kurun
2. **GitHub Codespaces**: Bulut tabanlı anında geliştirme ortamı
3. **VS Code Geliştirme Konteynerleri**: Yerel konteyner tabanlı geliştirme
4. **Binder**: Defterleri bulutta başlatın (eğer yapılandırılmışsa)

### Ders İçeriği Yönergeleri
- Her ders bağımsızdır ancak önceki kavramlar üzerine inşa edilir
- Ders öncesi testler, ön bilgiyi test eder
- Ders sonrası testler öğrenmeyi pekiştirir
- Ödevler uygulamalı pratik sağlar
- Sketchnotes görsel özetler sunar

### Yaygın Sorunları Giderme

**Jupyter Çekirdek Sorunları:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm Kurulum Hataları:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Defterlerde İthalat Hataları:**
- Gerekli tüm kütüphanelerin yüklü olduğundan emin olun
- Python sürüm uyumluluğunu kontrol edin (Python 3.7+ önerilir)
- Sanal ortamın etkinleştirildiğinden emin olun

**Docsify Yüklenmiyor:**
- Depo kökünden hizmet verdiğinizden emin olun
- `index.html` dosyasının mevcut olduğunu kontrol edin
- Doğru ağ erişimini sağlayın (port 3000)

### Performans Dikkatleri
- Büyük veri setleri defterlerde yüklenirken zaman alabilir
- Karmaşık grafikler için görselleştirme oluşturma yavaş olabilir
- Vue.js geliştirme sunucusu hızlı yineleme için sıcak yükleme sağlar
- Üretim derlemeleri optimize edilmiş ve küçültülmüştür

### Güvenlik Notları
- Hassas veri veya kimlik bilgileri gönderilmemelidir
- Bulut derslerinde API anahtarları için ortam değişkenlerini kullanın
- Azure ile ilgili dersler Azure hesap kimlik bilgileri gerektirebilir
- Güvenlik yamaları için bağımlılıkları güncel tutun

## Çevirilere Katkı
- Otomatik çeviriler GitHub Actions ile yönetilir
- Çeviri doğruluğu için manuel düzeltmeler memnuniyetle karşılanır
- Mevcut çeviri klasör yapısını takip edin
- Test bağlantılarını dil parametresiyle güncelleyin: `?loc=fr`
- Çevrilmiş derslerin düzgün şekilde görüntülendiğini test edin

## İlgili Kaynaklar
- Ana müfredat: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Öğrenci Merkezi: https://docs.microsoft.com/learn/student-hub
- Tartışma Forumu: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Diğer Microsoft müfredatları: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Proje Bakımı
- İçeriği güncel tutmak için düzenli güncellemeler
- Topluluk katkıları memnuniyetle karşılanır
- GitHub'da sorunlar takip edilir
- Çekme istekleri müfredat bakımcıları tarafından gözden geçirilir
- Aylık içerik incelemeleri ve güncellemeler

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.