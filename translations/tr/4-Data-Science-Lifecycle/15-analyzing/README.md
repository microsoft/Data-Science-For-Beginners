<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a167aa0bfb1c46ece1b3d21ae939cc0d",
  "translation_date": "2025-09-04T18:10:16+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "tr"
}
-->
# Veri Bilimi Yaşam Döngüsü: Analiz Etme

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Veri Bilimi Yaşam Döngüsü: Analiz Etme - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## Ders Öncesi Quiz

## [Ders Öncesi Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Veri yaşam döngüsünde analiz etme aşaması, verilerin önerilen soruları yanıtlayabileceğini veya belirli bir problemi çözebileceğini doğrular. Bu adım ayrıca bir modelin bu soruları ve problemleri doğru bir şekilde ele aldığını doğrulamaya odaklanabilir. Bu ders, verilerdeki özellikleri ve ilişkileri tanımlamak için kullanılan teknikler olan Keşifsel Veri Analizi (Exploratory Data Analysis veya EDA) üzerine odaklanmaktadır ve verileri modelleme için hazırlamak amacıyla kullanılabilir.

Bu ders kapsamında, Python ve Pandas kütüphanesi ile nasıl uygulanabileceğini göstermek için [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) sitesinden bir örnek veri seti kullanacağız. Bu veri seti, e-postalarda bulunan bazı yaygın kelimelerin sayısını içerir ve bu e-postaların kaynakları anonimdir. Bu dizindeki [notebook](notebook.ipynb) dosyasını takip ederek ilerleyebilirsiniz.

## Keşifsel Veri Analizi

Yaşam döngüsünün veri toplama aşaması, verilerin elde edildiği ve ele alınan problemler ile soruların belirlendiği yerdir, ancak verilerin nihai sonucu destekleyip destekleyemeyeceğini nasıl bilebiliriz? 
Bir veri bilimcinin veri toplarken şu soruları sorması gerektiğini hatırlayın:
-   Bu problemi çözmek için yeterli veriye sahip miyim?
-   Bu problem için verinin kalitesi kabul edilebilir mi?
-   Bu veri aracılığıyla ek bilgiler keşfedersem, hedefleri değiştirmeyi veya yeniden tanımlamayı düşünmeli miyiz?
Keşifsel Veri Analizi, veriyi tanıma sürecidir ve bu soruları yanıtlamak için kullanılabilir, ayrıca veri setiyle çalışmanın zorluklarını belirlemeye yardımcı olabilir. Bu hedeflere ulaşmak için kullanılan bazı tekniklere odaklanalım.

## Veri Profilleme, Tanımlayıcı İstatistikler ve Pandas
Bu problemi çözmek için yeterli veriye sahip olup olmadığımızı nasıl değerlendiririz? Veri profilleme, tanımlayıcı istatistikler teknikleri aracılığıyla veri setimiz hakkında genel bilgiler özetleyebilir ve toplayabilir. Veri profilleme, elimizde ne olduğunu anlamamıza yardımcı olurken, tanımlayıcı istatistikler elimizde ne kadar şey olduğunu anlamamıza yardımcı olur.

Önceki derslerin birkaçında, Pandas kullanarak [`describe()` fonksiyonu](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) ile bazı tanımlayıcı istatistikler sağlamıştık. Bu fonksiyon, sayısal verilerdeki toplam, maksimum ve minimum değerler, ortalama, standart sapma ve çeyrek değerleri sağlar. `describe()` gibi tanımlayıcı istatistikler kullanarak ne kadar veriye sahip olduğunuzu ve daha fazlasına ihtiyacınız olup olmadığını değerlendirebilirsiniz.

## Örnekleme ve Sorgulama
Büyük bir veri setindeki her şeyi keşfetmek çok zaman alıcı olabilir ve genellikle bir bilgisayara bırakılan bir görevdir. Ancak, örnekleme, veriyi anlamada yardımcı bir araçtır ve veri setinde ne olduğunu ve neyi temsil ettiğini daha iyi anlamamızı sağlar. Bir örnekle, olasılık ve istatistik uygulayarak veriniz hakkında genel sonuçlara ulaşabilirsiniz. Ne kadar veri örneklemeniz gerektiği konusunda belirli bir kural olmasa da, daha fazla veri örnekledikçe veri hakkında daha kesin genellemeler yapabilirsiniz. 
Pandas kütüphanesi, [`sample()` fonksiyonunu](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) içerir ve bu fonksiyona kaç rastgele örnek almak istediğinizi belirtebilirsiniz.

Veri üzerinde genel sorgulamalar yapmak, sahip olduğunuz bazı genel soruları ve teorileri yanıtlamanıza yardımcı olabilir. Örneklemenin aksine, sorgular belirli veri bölümlerine odaklanmanıza ve kontrol sağlamanıza olanak tanır. 
Pandas kütüphanesindeki [`query()` fonksiyonu](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html), sütunları seçmenize ve alınan satırlar aracılığıyla veri hakkında basit yanıtlar almanıza olanak tanır.

## Görselleştirmelerle Keşfetme
Veriler tamamen temizlenip analiz edilene kadar görselleştirmeler oluşturmaya başlamanız gerekmez. Aslında, keşif sırasında görsel bir temsil oluşturmak, verideki desenleri, ilişkileri ve problemleri belirlemeye yardımcı olabilir. Ayrıca, görselleştirmeler, veriyi yönetmeyen kişilerle iletişim kurmanın bir yolu olabilir ve yakalama aşamasında ele alınmayan ek soruları paylaşma ve netleştirme fırsatı sunabilir. Görselleştirme hakkında daha fazla bilgi edinmek için [Görselleştirme Bölümüne](../../../../../../../../../3-Data-Visualization) göz atabilirsiniz.

## Tutarsızlıkları Belirlemek İçin Keşfetme
Bu dersteki tüm konular, eksik veya tutarsız değerleri belirlemeye yardımcı olabilir, ancak Pandas bazılarını kontrol etmek için fonksiyonlar sağlar. [isna() veya isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) eksik değerleri kontrol edebilir. Verinizdeki bu değerleri keşfetmenin önemli bir parçası, neden bu şekilde olduklarını anlamaktır. Bu, onları çözmek için hangi [adımları atmanız gerektiğine](/2-Working-With-Data/08-data-preparation/notebook.ipynb) karar vermenize yardımcı olabilir.

## [Ders Sonrası Quiz](https://ff-quizzes.netlify.app/en/ds/)

## Ödev

[Cevaplar için Keşfetme](assignment.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.