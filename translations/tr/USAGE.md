<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:02:24+00:00",
  "source_file": "USAGE.md",
  "language_code": "tr"
}
-->
# Kullanım Kılavuzu

Bu kılavuz, Veri Bilimi için Başlangıç müfredatını kullanmaya yönelik örnekler ve yaygın iş akışlarını sunar.

## İçindekiler

- [Bu Müfredat Nasıl Kullanılır](../..)
- [Derslerle Çalışmak](../..)
- [Jupyter Notebooks ile Çalışmak](../..)
- [Quiz Uygulamasını Kullanmak](../..)
- [Yaygın İş Akışları](../..)
- [Kendi Kendine Öğrenenler için İpuçları](../..)
- [Eğitmenler için İpuçları](../..)

## Bu Müfredat Nasıl Kullanılır

Bu müfredat esnek bir şekilde tasarlanmıştır ve farklı şekillerde kullanılabilir:

- **Kendi hızınızda öğrenme**: Dersleri bağımsız olarak kendi hızınızda tamamlayın
- **Sınıf eğitimi**: Yapılandırılmış bir kurs olarak rehberli eğitimle kullanın
- **Çalışma grupları**: Akranlarınızla iş birliği içinde öğrenin
- **Atölye formatı**: Yoğun kısa süreli öğrenme oturumları

## Derslerle Çalışmak

Her ders, öğrenmeyi en üst düzeye çıkarmak için tutarlı bir yapıya sahiptir:

### Ders Yapısı

1. **Ders Öncesi Quiz**: Mevcut bilginizi test edin
2. **Sketchnote** (Opsiyonel): Anahtar kavramların görsel özeti
3. **Video** (Opsiyonel): Ek video içeriği
4. **Yazılı Ders**: Temel kavramlar ve açıklamalar
5. **Jupyter Notebook**: Uygulamalı kodlama alıştırmaları
6. **Ödev**: Öğrendiklerinizi uygulayın
7. **Ders Sonrası Quiz**: Anlamanızı pekiştirin

### Bir Ders için Örnek İş Akışı

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

## Jupyter Notebooks ile Çalışmak

### Jupyter'i Başlatma

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Notebook Hücrelerini Çalıştırma

1. **Bir hücreyi çalıştırın**: `Shift + Enter` tuşlarına basın veya "Çalıştır" düğmesine tıklayın
2. **Tüm hücreleri çalıştırın**: Menüden "Cell" → "Run All" seçeneğini seçin
3. **Kernel'i yeniden başlatın**: Sorun yaşarsanız "Kernel" → "Restart" seçeneğini seçin

### Örnek: Bir Notebook'ta Veri ile Çalışmak

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

### Çalışmanızı Kaydetme

- Jupyter periyodik olarak otomatik kaydeder
- Manuel kaydetme: `Ctrl + S` (macOS'ta `Cmd + S`) tuşlarına basın
- İlerlemeniz `.ipynb` dosyasında kaydedilir

## Quiz Uygulamasını Kullanmak

### Quiz Uygulamasını Yerel Olarak Çalıştırma

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Quizleri Çözme

1. Ders öncesi quizler her dersin başında bağlantı olarak verilmiştir
2. Ders sonrası quizler her dersin sonunda bağlantı olarak verilmiştir
3. Her quizde 3 soru bulunur
4. Quizler öğrenmeyi pekiştirmek için tasarlanmıştır, kapsamlı bir test amacı taşımaz

### Quiz Numaralandırması

- Quizler 0-39 arasında numaralandırılmıştır (toplam 40 quiz)
- Her ders genellikle bir ön ve bir son quiz içerir
- Quiz URL'leri quiz numarasını içerir: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Yaygın İş Akışları

### İş Akışı 1: Tamamen Yeni Başlayanlar İçin Yol

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

### İş Akışı 2: Konuya Özel Öğrenme

Belirli bir konuya ilgi duyuyorsanız:

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

### İş Akışı 3: Proje Tabanlı Öğrenme

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### İş Akışı 4: Bulut Tabanlı Veri Bilimi

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Kendi Kendine Öğrenenler için İpuçları

### Düzenli Kalın

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Düzenli Olarak Pratik Yapın

- Her gün veya hafta için belirli bir zaman ayırın
- Haftada en az bir dersi tamamlayın
- Önceki dersleri periyodik olarak gözden geçirin

### Toplulukla Etkileşim Kurun

- [Discord topluluğuna](https://aka.ms/ds4beginners/discord) katılın
- Discord'daki #Data-Science-for-Beginners kanalına katılın [Discord Tartışmaları](https://aka.ms/ds4beginners/discord)
- İlerlemenizi paylaşın ve sorular sorun

### Kendi Projelerinizi Oluşturun

Dersleri tamamladıktan sonra, öğrendiğiniz kavramları kişisel projelerde uygulayın:

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

## Eğitmenler için İpuçları

### Sınıf Kurulumu

1. Ayrıntılı rehberlik için [for-teachers.md](for-teachers.md) dosyasını inceleyin
2. Paylaşılan bir ortam oluşturun (GitHub Classroom veya Codespaces)
3. İletişim kanalı oluşturun (Discord, Slack veya Teams)

### Ders Planlama

**Önerilen 10 Haftalık Program:**

- **Hafta 1-2**: Giriş (Dersler 1-4)
- **Hafta 3-4**: Veri ile Çalışma (Dersler 5-8)
- **Hafta 5-6**: Veri Görselleştirme (Dersler 9-13)
- **Hafta 7-8**: Veri Bilimi Yaşam Döngüsü (Dersler 14-16)
- **Hafta 9**: Bulut Veri Bilimi (Dersler 17-19)
- **Hafta 10**: Gerçek Dünya Uygulamaları ve Final Projeleri (Ders 20)

### Docsify'ı Çevrimdışı Erişim için Çalıştırma

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Ödev Değerlendirme

- Öğrenci notebooklarını tamamlanmış alıştırmalar için inceleyin
- Quiz skorları üzerinden anlayışı kontrol edin
- Final projelerini veri bilimi yaşam döngüsü ilkelerine göre değerlendirin

### Ödev Oluşturma

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

## Çevrimdışı Çalışma

### Kaynakları İndirme

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Belgeleri Yerel Olarak Çalıştırma

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Quiz Uygulamasını Yerel Olarak Çalıştırma

```bash
cd quiz-app
npm run serve
```

## Çevrilmiş İçeriğe Erişim

Çeviriler 40'tan fazla dilde mevcuttur:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Her çeviri, İngilizce versiyonla aynı yapıyı korur.

## Ek Kaynaklar

### Öğrenmeye Devam Edin

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Ek öğrenme yolları
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Öğrenciler için kaynaklar
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Topluluk forumu

### İlgili Müfredatlar

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Yardım Alma

- Yaygın sorunlar için [TROUBLESHOOTING.md](TROUBLESHOOTING.md) dosyasını kontrol edin
- [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) üzerinde arama yapın
- [Discord](https://aka.ms/ds4beginners/discord) topluluğumuza katılın
- Sorun bildirmek veya katkıda bulunmak için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyin

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.