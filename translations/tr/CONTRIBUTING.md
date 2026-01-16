<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T13:59:29+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tr"
}
-->
# Veri Bilimine Giriş için Katkıda Bulunma

Veri Bilimine Giriş müfredatına katkıda bulunma ilginiz için teşekkür ederiz! Topluluktan gelen katkıları memnuniyetle karşılıyoruz.

## İçindekiler

- [Davranış Kuralları](../..)
- [Nasıl Katkıda Bulunabilirim?](../..)
- [Başlarken](../..)
- [Katkı Kuralları](../..)
- [Pull Request Süreci](../..)
- [Stil Kuralları](../..)
- [Katkıda Bulunma Lisans Anlaşması](../..)

## Davranış Kuralları

Bu proje [Microsoft Açık Kaynak Davranış Kuralları](https://opensource.microsoft.com/codeofconduct/) benimsemiştir. Daha fazla bilgi için [Davranış Kuralları SSS](https://opensource.microsoft.com/codeofconduct/faq/) bölümüne bakabilir veya ek sorularınız ya da yorumlarınız için [opencode@microsoft.com](mailto:opencode@microsoft.com) adresine e-posta gönderebilirsiniz.

## Nasıl Katkıda Bulunabilirim?

### Hata Bildirme

Hata raporları oluşturmadan önce, mevcut sorunları kontrol ederek yinelenen raporları önleyin. Hata raporu oluştururken mümkün olduğunca fazla ayrıntı ekleyin:

- **Açık ve açıklayıcı bir başlık kullanın**
- **Sorunu yeniden oluşturmak için gereken adımları ayrıntılı olarak açıklayın**
- **Spesifik örnekler sağlayın** (kod parçacıkları, ekran görüntüleri)
- **Gözlemlediğiniz davranışı ve beklediğiniz sonucu açıklayın**
- **Ortam detaylarınızı ekleyin** (işletim sistemi, Python sürümü, tarayıcı)

### İyileştirme Önerileri

İyileştirme önerileri memnuniyetle karşılanır! Öneri yaparken:

- **Açık ve açıklayıcı bir başlık kullanın**
- **Önerilen iyileştirmeyi ayrıntılı olarak açıklayın**
- **Bu iyileştirmenin neden faydalı olacağını açıklayın**
- **Diğer projelerdeki benzer özellikleri listeleyin (varsa)**

### Dokümantasyona Katkıda Bulunma

Dokümantasyon iyileştirmeleri her zaman takdir edilir:

- **Yazım hatalarını ve dilbilgisi hatalarını düzeltin**
- **Açıklamaların netliğini artırın**
- **Eksik dokümantasyonu ekleyin**
- **Güncel olmayan bilgileri güncelleyin**
- **Örnekler veya kullanım durumları ekleyin**

### Kod Katkıları

Kod katkıları memnuniyetle karşılanır, örneğin:

- **Yeni dersler veya alıştırmalar**
- **Hata düzeltmeleri**
- **Mevcut not defterlerinde iyileştirmeler**
- **Yeni veri setleri veya örnekler**
- **Quiz uygulaması iyileştirmeleri**

## Başlarken

### Ön Koşullar

Katkıda bulunmadan önce aşağıdakilere sahip olduğunuzdan emin olun:

1. Bir GitHub hesabı
2. Sisteminizde yüklü Git
3. Python 3.7+ ve Jupyter yüklü
4. Node.js ve npm (quiz uygulaması katkıları için)
5. Müfredat yapısına aşinalık

Ayrıntılı kurulum talimatları için [INSTALLATION.md](INSTALLATION.md) dosyasına bakın.

### Fork ve Klonlama

1. GitHub'da **deponun fork'unu oluşturun**
2. Fork'unuzu yerel olarak **klonlayın**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Upstream remote ekleyin**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Bir Dal Oluşturun

Çalışmanız için yeni bir dal oluşturun:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Dal adlandırma kuralları:
- `feature/` - Yeni özellikler veya dersler
- `fix/` - Hata düzeltmeleri
- `docs/` - Dokümantasyon değişiklikleri
- `refactor/` - Kod yeniden düzenleme

## Katkı Kuralları

### Ders İçeriği İçin

Yeni dersler eklerken veya mevcut olanları değiştirirken:

1. **Mevcut yapıyı takip edin**:
   - README.md ile ders içeriği
   - Alıştırmalar içeren Jupyter not defteri
   - Ödev (varsa)
   - Ön ve son quiz bağlantıları

2. **Şu öğeleri ekleyin**:
   - Açık öğrenme hedefleri
   - Adım adım açıklamalar
   - Yorumlarla birlikte kod örnekleri
   - Pratik için alıştırmalar
   - Ek kaynaklara bağlantılar

3. **Erişilebilirliği sağlayın**:
   - Açık, basit bir dil kullanın
   - Görseller için alt metin sağlayın
   - Kod yorumları ekleyin
   - Farklı öğrenme stillerini göz önünde bulundurun

### Jupyter Not Defterleri İçin

1. **Tüm çıktıları temizleyin**:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Açıklamalar içeren markdown hücreleri ekleyin**

3. **Tutarlı biçimlendirme kullanın**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Not defterinizi tamamen test edin** ve ardından gönderin

### Python Kodu İçin

[PEP 8](https://www.python.org/dev/peps/pep-0008/) stil kurallarını takip edin:

```python
# Good practices
import pandas as pd

def calculate_mean(data):
    """Calculate the mean of a dataset.
    
    Args:
        data (list): List of numerical values
        
    Returns:
        float: Mean of the dataset
    """
    return sum(data) / len(data)
```

### Quiz Uygulaması Katkıları İçin

Quiz uygulamasını değiştirirken:

1. **Yerel olarak test edin**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Linter çalıştırın**:
   ```bash
   npm run lint
   ```

3. **Başarıyla derleyin**:
   ```bash
   npm run build
   ```

4. **Vue.js stil rehberini** ve mevcut desenleri takip edin

### Çeviriler İçin

Çeviriler eklerken veya güncellerken:

1. `translations/` klasöründeki yapıyı takip edin
2. Dil kodunu klasör adı olarak kullanın (ör. Fransızca için `fr`)
3. İngilizce sürümle aynı dosya yapısını koruyun
4. Quiz bağlantılarını dil parametresiyle güncelleyin: `?loc=fr`
5. Tüm bağlantıları ve biçimlendirmeyi test edin

## Pull Request Süreci

### Göndermeden Önce

1. **Dalınızı en son değişikliklerle güncelleyin**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Değişikliklerinizi test edin**:
   - Değiştirilen tüm not defterlerini çalıştırın
   - Quiz uygulamasını test edin (değiştirildiyse)
   - Tüm bağlantıların çalıştığını doğrulayın
   - Yazım ve dilbilgisi hatalarını kontrol edin

3. **Değişikliklerinizi commit edin**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Açık commit mesajları yazın:
   - Şimdiki zaman kullanın ("Özellik ekle" değil "Özellik eklendi")
   - Emir kipinde yazın ("İmleci taşı..." değil "İmleç taşınıyor...")
   - İlk satırı 72 karakterle sınırlayın
   - İlgili sorunları ve pull request'leri referans gösterin

4. **Fork'unuza push yapın**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Pull Request Oluşturma

1. [Depoya](https://github.com/microsoft/Data-Science-For-Beginners) gidin
2. "Pull requests" → "New pull request" seçeneğine tıklayın
3. "compare across forks" seçeneğine tıklayın
4. Fork ve dalınızı seçin
5. "Create pull request" seçeneğine tıklayın

### PR Başlık Formatı

Açık, açıklayıcı başlıklar kullanın ve şu formatı takip edin:

```
[Component] Brief description
```

Örnekler:
- `[Ders 7] Python not defteri import hatasını düzelt`
- `[Quiz Uygulaması] Almanca çeviri ekle`
- `[Dokümanlar] README'yi yeni ön koşullarla güncelle`
- `[Düzeltme] Görselleştirme dersindeki veri yolunu düzelt`

### PR Açıklaması

PR açıklamanıza şunları ekleyin:

- **Ne**: Hangi değişiklikleri yaptınız?
- **Neden**: Bu değişiklikler neden gerekli?
- **Nasıl**: Değişiklikleri nasıl uyguladınız?
- **Test**: Değişiklikleri nasıl test ettiniz?
- **Ekran Görüntüleri**: Görsel değişiklikler için ekran görüntüleri ekleyin
- **İlgili Sorunlar**: İlgili sorunlara bağlantı verin (ör. "Fixes #123")

### İnceleme Süreci

1. **Otomatik kontroller** PR'nizde çalıştırılacak
2. **Bakıcılar katkınızı inceleyecek**
3. **Geri bildirimi ele alın** ve ek commit'ler yapın
4. Onaylandıktan sonra, bir **bakıcı PR'nizi birleştirecek**

### PR'niz Birleştirildikten Sonra

1. Dalınızı silin:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. Fork'unuzu güncelleyin:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Stil Kuralları

### Markdown

- Tutarlı başlık seviyeleri kullanın
- Bölümler arasında boş satırlar ekleyin
- Dil belirticileriyle kod blokları kullanın:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Görseller için alt metin ekleyin: `![Alt metin](../../translated_images/tr/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`
- Satır uzunluklarını makul tutun (yaklaşık 80-100 karakter)

### Python

- PEP 8 stil rehberini takip edin
- Anlamlı değişken adları kullanın
- Fonksiyonlara docstring ekleyin
- Uygun yerlerde tür ipuçları ekleyin:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Vue.js 2 stil rehberini takip edin
- Sağlanan ESLint yapılandırmasını kullanın
- Modüler, yeniden kullanılabilir bileşenler yazın
- Karmaşık mantık için yorumlar ekleyin

### Dosya Organizasyonu

- İlgili dosyaları bir arada tutun
- Açıklayıcı dosya adları kullanın
- Mevcut dizin yapısını takip edin
- Gereksiz dosyaları commit etmeyin (.DS_Store, .pyc, node_modules, vb.)

## Katkıda Bulunma Lisans Anlaşması

Bu proje katkıları ve önerileri memnuniyetle karşılar. Çoğu katkı, bize katkınızı kullanma hakkını verdiğinizi ve bu hakkı gerçekten verdiğinizi beyan eden bir Katkıda Bulunma Lisans Anlaşması (CLA) kabul etmenizi gerektirir. Ayrıntılar için https://cla.microsoft.com adresini ziyaret edin.

Bir pull request gönderdiğinizde, bir CLA-bot otomatik olarak bir CLA sağlayıp sağlamanız gerekip gerekmediğini belirleyecek ve PR'yi uygun şekilde işaretleyecektir (ör. etiket, yorum). Bot tarafından sağlanan talimatları takip etmeniz yeterlidir. Bu işlemi, CLA kullanan tüm depolar için yalnızca bir kez yapmanız gerekecek.

## Sorular?

- [Discord Kanalımız #data-science-for-beginners](https://aka.ms/ds4beginners/discord) adresine göz atın
- [Discord topluluğumuza](https://aka.ms/ds4beginners/discord) katılın
- Mevcut [sorunları](https://github.com/microsoft/Data-Science-For-Beginners/issues) ve [pull request'leri](https://github.com/microsoft/Data-Science-For-Beginners/pulls) inceleyin

## Teşekkürler!

Katkılarınız bu müfredatı herkes için daha iyi hale getiriyor. Katkıda bulunmak için zaman ayırdığınız için teşekkür ederiz!

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.