<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-28T11:22:11+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "tr"
}
-->
# Küçük Diyabet Çalışması

Bu ödevde, [buradan](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html) alınan diyabet hastalarına ait küçük bir veri seti ile çalışacağız.

|   | YAŞ | CİNSİYET | BMI | BP | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-----|----------|-----|----|----|----|----|----|----|----|----|
| 0 | 59 | 2 | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48 | 1 | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72 | 2 | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ... | ... | ...| ...| ...| ...| ...| ...| ...| ... |

## Talimatlar

* [assignment notebook](assignment.ipynb) dosyasını bir jupyter notebook ortamında açın
* Notebook'ta listelenen tüm görevleri tamamlayın, yani:
   * [ ] Tüm değerler için ortalama ve varyans hesaplayın
   * [ ] Cinsiyete bağlı olarak BMI, BP ve Y için kutu grafikleri çizin
   * [ ] Yaş, Cinsiyet, BMI ve Y değişkenlerinin dağılımı nedir?
   * [ ] Farklı değişkenler ile hastalık ilerlemesi (Y) arasındaki korelasyonu test edin
   * [ ] Diyabet ilerleme derecesinin erkekler ve kadınlar arasında farklı olduğuna dair hipotezi test edin
   
## Değerlendirme Ölçütleri

Örnek Niteliğinde | Yeterli | Geliştirme Gerekiyor
--- | --- | -- |
Gerekli tüm görevler tamamlanmış, grafiklerle gösterilmiş ve açıklanmış | Görevlerin çoğu tamamlanmış, grafiklerden veya elde edilen değerlerden açıklamalar veya çıkarımlar eksik | Sadece ortalama/varyans hesaplama ve temel grafikler gibi basit görevler tamamlanmış, veriden herhangi bir sonuç çıkarılmamış

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.