<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-06T09:06:08+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "tr"
}
-->
# Veriyi Tanımlama

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Veriyi Tanımlama - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Veri, keşifler yapmak ve bilinçli kararlar desteklemek için kullanılan gerçekler, bilgiler, gözlemler ve ölçümlerdir. Bir veri noktası, bir veri kümesindeki tek bir veri birimidir ve veri noktalarının bir koleksiyonudur. Veri kümeleri farklı formatlarda ve yapılarda olabilir ve genellikle kaynağına, yani verinin nereden geldiğine bağlıdır. Örneğin, bir şirketin aylık kazançları bir elektronik tablo formatında olabilirken, bir akıllı saatten gelen saatlik kalp atış hızı verileri [JSON](https://stackoverflow.com/a/383699) formatında olabilir. Veri bilimciler genellikle bir veri kümesindeki farklı veri türleriyle çalışırlar.

Bu ders, veriyi özelliklerine ve kaynaklarına göre tanımlamaya ve sınıflandırmaya odaklanmaktadır.

## [Ders Öncesi Testi](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Verinin Tanımlanması

### Ham Veri
Ham veri, kaynağından gelen ve henüz analiz edilmemiş veya organize edilmemiş veridir. Bir veri kümesinde neler olduğunu anlamak için, verinin insanlar ve analiz için kullanılan teknolojiler tarafından anlaşılabilir bir formata organize edilmesi gerekir. Bir veri kümesinin yapısı, nasıl organize edildiğini tanımlar ve yapılandırılmış, yapılandırılmamış ve yarı yapılandırılmış olarak sınıflandırılabilir. Bu yapılar, kaynağa bağlı olarak değişiklik gösterebilir ancak nihayetinde bu üç kategoriye uyacaktır.

### Nicel Veri
Nicel veri, bir veri kümesindeki sayısal gözlemlerdir ve genellikle analiz edilebilir, ölçülebilir ve matematiksel olarak kullanılabilir. Nicel veriye bazı örnekler: bir ülkenin nüfusu, bir kişinin boyu veya bir şirketin üç aylık kazançları. Ek analizlerle, nicel veri Hava Kalitesi İndeksi (AQI) için mevsimsel eğilimleri keşfetmek veya tipik bir iş gününde yoğun saat trafiği olasılığını tahmin etmek için kullanılabilir.

### Nitel Veri
Nitel veri, kategorik veri olarak da bilinir ve nicel veri gözlemleri gibi nesnel olarak ölçülemeyen veridir. Genellikle bir ürün veya sürecin kalitesini yakalayan çeşitli formatlarda öznel veridir. Bazen nitel veri sayısal olabilir ancak genellikle matematiksel olarak kullanılmaz, örneğin telefon numaraları veya zaman damgaları. Nitel veriye bazı örnekler: video yorumları, bir arabanın marka ve modeli veya en yakın arkadaşlarınızın en sevdiği renk. Nitel veri, tüketicilerin en çok hangi ürünleri sevdiğini anlamak veya iş başvurusu özgeçmişlerinde popüler anahtar kelimeleri belirlemek için kullanılabilir.

### Yapılandırılmış Veri
Yapılandırılmış veri, satır ve sütunlara organize edilmiş veridir; her satır aynı sütun setine sahip olacaktır. Sütunlar, belirli bir türdeki bir değeri temsil eder ve değerin neyi temsil ettiğini açıklayan bir isimle tanımlanır, satırlar ise gerçek değerleri içerir. Sütunlar genellikle değerlerin sütunu doğru bir şekilde temsil etmesini sağlamak için belirli bir dizi kural veya kısıtlama içerir. Örneğin, her satırda bir telefon numarasının olması gereken ve telefon numaralarının alfabetik karakterler içermediği bir müşteri elektronik tablosunu hayal edin. Telefon numarası sütununda boş olmaması ve yalnızca sayılar içermesi gerektiğini belirten kurallar uygulanabilir.

Yapılandırılmış verinin bir avantajı, diğer yapılandırılmış verilerle ilişkilendirilebilecek şekilde organize edilebilmesidir. Ancak, veri belirli bir şekilde organize edilmek üzere tasarlandığından, genel yapısında değişiklik yapmak oldukça fazla çaba gerektirebilir. Örneğin, müşteri elektronik tablosuna boş olamayacak bir e-posta sütunu eklemek, mevcut müşteri satırlarına bu değerleri nasıl ekleyeceğinizi belirlemenizi gerektirir.

Yapılandırılmış veri örnekleri: elektronik tablolar, ilişkisel veritabanları, telefon numaraları, banka ekstreleri

### Yapılandırılmamış Veri
Yapılandırılmamış veri genellikle satır veya sütunlara kategorize edilemez ve bir format veya takip edilmesi gereken bir dizi kural içermez. Yapılandırılmamış verinin yapısında daha az kısıtlama olduğu için, yapılandırılmış bir veri kümesine kıyasla yeni bilgi eklemek daha kolaydır. Örneğin, her 2 dakikada bir barometrik basınç verisi toplayan bir sensörün artık sıcaklık ölçüp kaydedebilmesini sağlayan bir güncelleme alması, veri yapılandırılmamışsa mevcut veriyi değiştirmeyi gerektirmez. Ancak, bu tür veriyi analiz etmek veya incelemek daha uzun sürebilir. Örneğin, bir bilim insanı sensör verilerinden geçen ayın ortalama sıcaklığını bulmak ister ancak sensörün bazı verilerinde "e" kaydettiğini ve bunun sensörün bozuk olduğunu belirttiğini keşfeder, bu da verinin eksik olduğu anlamına gelir.

Yapılandırılmamış veri örnekleri: metin dosyaları, metin mesajları, video dosyaları

### Yarı Yapılandırılmış Veri
Yarı yapılandırılmış veri, yapılandırılmış ve yapılandırılmamış verinin bir kombinasyonu olmasını sağlayan özelliklere sahiptir. Genellikle satır ve sütun formatına uymaz ancak yapılandırılmış olarak kabul edilen bir şekilde organize edilmiştir ve sabit bir format veya bir dizi kurala uyabilir. Yapı, kaynaklar arasında değişiklik gösterebilir; iyi tanımlanmış bir hiyerarşiden, yeni bilgilerin kolayca entegre edilmesine izin veren daha esnek bir yapıya kadar. Meta veriler, verinin nasıl organize edildiğini ve saklandığını belirlemeye yardımcı olan göstergelerdir ve veri türüne bağlı olarak çeşitli isimlere sahip olacaktır. Meta veriler için yaygın isimler arasında etiketler, öğeler, varlıklar ve öznitelikler bulunur. Örneğin, tipik bir e-posta mesajı bir konu, gövde ve bir alıcılar setine sahip olacaktır ve kim tarafından veya ne zaman gönderildiğine göre organize edilebilir.

Yarı yapılandırılmış veri örnekleri: HTML, CSV dosyaları, JavaScript Object Notation (JSON)

## Veri Kaynakları 

Bir veri kaynağı, verinin oluşturulduğu veya "yaşadığı" ilk konumdur ve nasıl ve ne zaman toplandığına bağlı olarak değişiklik gösterebilir. Kullanıcı(lar) tarafından oluşturulan veri birincil veri olarak bilinirken, genel kullanım için veri toplayan bir kaynaktan gelen veri ikincil veri olarak kabul edilir. Örneğin, bir grup bilim insanının bir yağmur ormanında gözlemler toplaması birincil veri olarak kabul edilir ve bu veriyi diğer bilim insanlarıyla paylaşmaya karar verirlerse, bunu kullananlar için ikincil veri olarak kabul edilir.

Veritabanları yaygın bir kaynaktır ve bir veritabanı yönetim sistemi, veriyi barındırmak ve korumak için kullanılır; kullanıcılar, veriyi keşfetmek için sorgu adı verilen komutlar kullanır. Dosyalar veri kaynakları olarak ses, görüntü ve video dosyaları ile Excel gibi elektronik tablolar olabilir. İnternet kaynakları, veritabanlarının yanı sıra dosyaların bulunabileceği yaygın bir veri barındırma yeridir. Uygulama programlama arayüzleri, API'ler olarak da bilinir, programcıların internet üzerinden harici kullanıcılarla veri paylaşma yolları oluşturmasına olanak tanır, web kazıma ise bir web sayfasından veri çıkarma işlemidir. [Veriyle Çalışma Dersleri](../../../../../../../../../2-Working-With-Data), çeşitli veri kaynaklarını nasıl kullanacağınızı öğrenmeye odaklanır.

## Sonuç

Bu derste öğrendik:

- Verinin ne olduğunu
- Verinin nasıl tanımlandığını
- Verinin nasıl sınıflandırıldığını ve kategorize edildiğini
- Verinin nerede bulunabileceğini

## 🚀 Meydan Okuma

Kaggle, açık veri kümeleri için mükemmel bir kaynaktır. [Veri kümesi arama aracı](https://www.kaggle.com/datasets) ile bazı ilginç veri kümeleri bulun ve 3-5 veri kümesini şu kriterlere göre sınıflandırın:

- Veri nicel mi yoksa nitel mi?
- Veri yapılandırılmış, yapılandırılmamış mı yoksa yarı yapılandırılmış mı?

## [Ders Sonrası Testi](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Gözden Geçirme ve Kendi Kendine Çalışma

- Bu Microsoft Learn birimi, [Verinizi Sınıflandırın](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) başlıklı, yapılandırılmış, yarı yapılandırılmış ve yapılandırılmamış verinin ayrıntılı bir dökümüne sahiptir.

## Ödev

[Veri Kümelerini Sınıflandırma](assignment.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.