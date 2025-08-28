<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-28T10:56:26+00:00",
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

Yaşam döngüsünün veri toplama aşaması, verilerin elde edildiği ve mevcut problemler ile soruların belirlendiği aşamadır. Ancak, verilerin nihai sonucu destekleyip destekleyemeyeceğini nasıl anlayabiliriz? 
Bir veri bilimci, verileri elde ettiğinde şu soruları sorabilir:
-   Bu problemi çözmek için yeterli veriye sahip miyim?
-   Bu problem için verinin kalitesi kabul edilebilir mi?
-   Bu veri aracılığıyla ek bilgiler keşfedersem, hedefleri değiştirmeyi veya yeniden tanımlamayı düşünmeli miyiz?
Keşifsel Veri Analizi, veriyi tanıma sürecidir ve bu soruları yanıtlamak için kullanılabilir. Ayrıca veri setiyle çalışmanın zorluklarını belirlemeye yardımcı olabilir. Şimdi bu hedeflere ulaşmak için kullanılan bazı tekniklere odaklanalım.

## Veri Profili Çıkartma, Tanımlayıcı İstatistikler ve Pandas
Bu problemi çözmek için yeterli veriye sahip olup olmadığımızı nasıl değerlendiririz? Veri profili çıkartma, tanımlayıcı istatistikler teknikleri aracılığıyla veri setimiz hakkında genel bilgiler özetleyebilir ve toplayabilir. Veri profili çıkartma, elimizde ne olduğunu anlamamıza yardımcı olurken, tanımlayıcı istatistikler elimizde ne kadar şey olduğunu anlamamıza yardımcı olur.

Önceki derslerin birkaçında, Pandas kullanarak [`describe()` fonksiyonu](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) ile bazı tanımlayıcı istatistikler sağlamıştık. Bu fonksiyon, sayısal verilerdeki toplam, maksimum ve minimum değerler, ortalama, standart sapma ve çeyrek değerleri sağlar. `describe()` gibi tanımlayıcı istatistikler kullanarak ne kadar veriye sahip olduğunuzu ve daha fazlasına ihtiyacınız olup olmadığını değerlendirebilirsiniz.

## Örnekleme ve Sorgulama
Büyük bir veri setindeki her şeyi keşfetmek çok zaman alıcı olabilir ve genellikle bir bilgisayara bırakılan bir görevdir. Ancak, örnekleme, veriyi anlamada yardımcı bir araçtır ve veri setinde ne olduğunu ve neyi temsil ettiğini daha iyi anlamamızı sağlar. Bir örnekleme ile, olasılık ve istatistik uygulayarak veriniz hakkında genel sonuçlara ulaşabilirsiniz. Ne kadar veri örneklemeniz gerektiği konusunda belirli bir kural olmasa da, daha fazla veri örneklediğinizde, veri hakkında daha kesin genellemeler yapabilirsiniz. 
Pandas kütüphanesi, [`sample()` fonksiyonunu](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) içerir ve bu fonksiyon, kaç rastgele örnek almak istediğinizi belirterek kullanabilirsiniz.

Veri üzerinde genel sorgulamalar yapmak, sahip olduğunuz bazı genel soruları ve teorileri yanıtlamanıza yardımcı olabilir. Örneklemenin aksine, sorgulamalar belirli veri bölümlerine odaklanmanıza ve kontrol sağlamanıza olanak tanır. 
Pandas kütüphanesindeki [`query()` fonksiyonu](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html), sütunları seçmenize ve alınan satırlar aracılığıyla veri hakkında basit cevaplar almanıza olanak tanır.

## Görselleştirmelerle Keşfetme
Veriler tamamen temizlenip analiz edilene kadar görselleştirmeler oluşturmaya başlamanız gerekmez. Aslında, keşif sırasında görsel bir temsil oluşturmak, verilerdeki desenleri, ilişkileri ve problemleri belirlemeye yardımcı olabilir. Ayrıca, görselleştirmeler, verileri yönetmeyen kişilerle iletişim kurmanın bir yolu olabilir ve yakalama aşamasında ele alınmayan ek soruları paylaşma ve netleştirme fırsatı sunabilir. Görselleştirme ile ilgili daha fazla bilgi için [Görselleştirme Bölümüne](../../../../../../../../../3-Data-Visualization) göz atabilirsiniz.

## Tutarsızlıkları Belirlemek İçin Keşfetme
Bu dersteki tüm konular, eksik veya tutarsız değerleri belirlemeye yardımcı olabilir, ancak Pandas bu değerleri kontrol etmek için bazı fonksiyonlar sağlar. [isna() veya isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) eksik değerleri kontrol edebilir. Verinizdeki bu değerleri keşfetmenin önemli bir parçası, bu değerlerin neden bu şekilde oluştuğunu anlamaktır. Bu, [bu değerleri çözmek için hangi adımları atmanız gerektiğine]( /2-Working-With-Data/08-data-preparation/notebook.ipynb) karar vermenize yardımcı olabilir.

## [Ders Öncesi Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Ödev

[Cevaplar için Keşfetme](assignment.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.