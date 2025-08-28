<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-28T11:25:32+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "tr"
}
-->
# Verileri Tanımlama

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Verileri Tanımlama - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Veri, keşifler yapmak ve bilinçli kararları desteklemek için kullanılan gerçekler, bilgiler, gözlemler ve ölçümlerdir. Bir veri noktası, bir veri kümesindeki tek bir veri birimidir ve veri noktalarının bir koleksiyonudur. Veri kümeleri farklı formatlarda ve yapılarda olabilir ve genellikle kaynağına, yani verinin nereden geldiğine bağlıdır. Örneğin, bir şirketin aylık kazançları bir elektronik tablo formatında olabilirken, bir akıllı saatten alınan saatlik kalp atış hızı verileri [JSON](https://stackoverflow.com/a/383699) formatında olabilir. Veri bilimciler genellikle bir veri kümesindeki farklı veri türleriyle çalışırlar.

Bu ders, verileri özelliklerine ve kaynaklarına göre tanımlamaya ve sınıflandırmaya odaklanmaktadır.

## [Ders Öncesi Test](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)
## Veriler Nasıl Tanımlanır?

### Ham Veri
Ham veri, kaynağından gelen ve başlangıç durumunda olan, analiz edilmemiş veya organize edilmemiş veridir. Bir veri kümesinde neler olduğunu anlamak için, hem insanlar hem de veriyi daha fazla analiz etmek için kullanabilecekleri teknoloji tarafından anlaşılabilir bir formata organize edilmesi gerekir. Bir veri kümesinin yapısı, nasıl organize edildiğini tanımlar ve yapılandırılmış, yapılandırılmamış ve yarı yapılandırılmış olarak sınıflandırılabilir. Bu yapı türleri kaynağa bağlı olarak değişir, ancak nihayetinde bu üç kategoriye uyar.

### Nicel Veri
Nicel veri, bir veri kümesindeki sayısal gözlemlerdir ve genellikle analiz edilebilir, ölçülebilir ve matematiksel olarak kullanılabilir. Nicel veriye bazı örnekler: bir ülkenin nüfusu, bir kişinin boyu veya bir şirketin üç aylık kazançları. Ek analizlerle, nicel veri Hava Kalitesi İndeksi (AQI) için mevsimsel eğilimleri keşfetmek veya tipik bir iş gününde yoğun saat trafiği olasılığını tahmin etmek için kullanılabilir.

### Nitel Veri
Nitel veri, kategorik veri olarak da bilinir ve nicel veri gözlemleri gibi objektif olarak ölçülemeyen veridir. Genellikle bir ürün veya sürecin kalitesini yakalayan çeşitli formatlarda subjektif verilerdir. Bazen nitel veri sayısal olabilir ve genellikle matematiksel olarak kullanılmaz, örneğin telefon numaraları veya zaman damgaları. Nitel veriye bazı örnekler: video yorumları, bir arabanın marka ve modeli veya en yakın arkadaşlarınızın en sevdiği renk. Nitel veri, tüketicilerin en çok hangi ürünleri sevdiğini anlamak veya iş başvurusu özgeçmişlerinde popüler anahtar kelimeleri belirlemek için kullanılabilir.

### Yapılandırılmış Veri
Yapılandırılmış veri, satır ve sütunlara organize edilmiş veridir; her satır aynı sütun setine sahip olacaktır. Sütunlar belirli bir türdeki bir değeri temsil eder ve değerin neyi temsil ettiğini açıklayan bir adla tanımlanır, satırlar ise gerçek değerleri içerir. Sütunlar genellikle değerlerin sütunu doğru bir şekilde temsil etmesini sağlamak için belirli bir dizi kural veya kısıtlama içerir. Örneğin, her satırın bir telefon numarasına sahip olması gereken ve telefon numaralarının alfabetik karakterler içermediği bir müşteri elektronik tablosunu hayal edin. Telefon numarası sütununda boş olmaması ve yalnızca sayılar içermesi gerektiğini belirten kurallar uygulanabilir.

Yapılandırılmış verinin bir avantajı, diğer yapılandırılmış verilerle ilişkilendirilebilecek şekilde organize edilebilmesidir. Ancak, veri belirli bir şekilde organize edilmek üzere tasarlandığından, genel yapısını değiştirmek çok fazla çaba gerektirebilir. Örneğin, müşteri elektronik tablosuna boş olamayacak bir e-posta sütunu eklemek, mevcut müşteri satırlarına bu değerleri nasıl ekleyeceğinizi bulmanızı gerektirir.

Yapılandırılmış veri örnekleri: elektronik tablolar, ilişkisel veritabanları, telefon numaraları, banka ekstreleri

### Yapılandırılmamış Veri
Yapılandırılmamış veri genellikle satır veya sütunlara kategorize edilemez ve bir format veya takip edilecek bir dizi kural içermez. Yapılandırılmamış verinin yapısında daha az kısıtlama olduğu için, yapılandırılmış bir veri kümesine kıyasla yeni bilgi eklemek daha kolaydır. Örneğin, her 2 dakikada bir barometrik basınç verisi toplayan bir sensörün artık sıcaklık ölçüp kaydedebilmesini sağlayan bir güncelleme alması, yapılandırılmamışsa mevcut veriyi değiştirmeyi gerektirmez. Ancak, bu tür verileri analiz etmek veya incelemek daha uzun sürebilir. Örneğin, bir bilim insanı sensör verilerinden geçen ayın ortalama sıcaklığını bulmak ister, ancak sensörün bazı verilerinde "e" kaydettiğini ve bunun sensörün bozuk olduğunu belirtmek için kullanıldığını keşfeder, bu da verinin eksik olduğu anlamına gelir.

Yapılandırılmamış veri örnekleri: metin dosyaları, metin mesajları, video dosyaları

### Yarı Yapılandırılmış Veri
Yarı yapılandırılmış veri, yapılandırılmış ve yapılandırılmamış verinin bir kombinasyonu olan özelliklere sahiptir. Genellikle satır ve sütun formatına uymasa da, yapılandırılmış olarak kabul edilen bir şekilde organize edilir ve sabit bir format veya bir dizi kurala uyabilir. Yapı, kaynaklar arasında değişir; iyi tanımlanmış bir hiyerarşiden, yeni bilgilerin kolayca entegre edilmesine izin veren daha esnek bir yapıya kadar. Meta veriler, verilerin nasıl organize edildiğini ve saklandığını belirlemeye yardımcı olan göstergelerdir ve veri türüne bağlı olarak çeşitli adlara sahip olacaktır. Meta veriler için yaygın adlar arasında etiketler, öğeler, varlıklar ve öznitelikler bulunur. Örneğin, tipik bir e-posta mesajı bir konu, gövde ve bir alıcılar setine sahip olacaktır ve kim tarafından veya ne zaman gönderildiğine göre organize edilebilir.

Yarı yapılandırılmış veri örnekleri: HTML, CSV dosyaları, JavaScript Object Notation (JSON)

## Veri Kaynakları 

Bir veri kaynağı, verinin oluşturulduğu veya "yaşadığı" ilk konumdur ve nasıl ve ne zaman toplandığına bağlı olarak değişir. Kullanıcı(lar) tarafından oluşturulan veriler birincil veri olarak bilinirken, genel kullanım için veri toplayan bir kaynaktan gelen veriler ikincil veri olarak adlandırılır. Örneğin, bir grup bilim insanının bir yağmur ormanında gözlemler toplaması birincil olarak kabul edilir ve bu verileri diğer bilim insanlarıyla paylaşmaya karar verirlerse, bunu kullananlar için ikincil olarak kabul edilir.

Veritabanları yaygın bir kaynaktır ve bir veritabanı yönetim sistemi, kullanıcıların veriyi keşfetmek için sorgular adı verilen komutlar kullandığı veriyi barındırmak ve sürdürmek için gereklidir. Veri kaynakları olarak dosyalar, ses, görüntü ve video dosyaları ile Excel gibi elektronik tablolar olabilir. İnternet kaynakları, veritabanlarının yanı sıra dosyaların bulunabileceği yaygın bir veri barındırma yeridir. Uygulama programlama arayüzleri, API'ler olarak da bilinir, programcıların internet üzerinden harici kullanıcılarla veri paylaşma yolları oluşturmasına olanak tanır, web kazıma ise bir web sayfasından veri çıkarma işlemidir. [Verilerle Çalışma dersleri](../../../../../../../../../2-Working-With-Data), çeşitli veri kaynaklarını nasıl kullanacağınızı öğrenmeye odaklanır.

## Sonuç

Bu derste öğrendik:

- Verinin ne olduğunu
- Verinin nasıl tanımlandığını
- Verinin nasıl sınıflandırıldığını ve kategorize edildiğini
- Verinin nerede bulunabileceğini

## 🚀 Zorluk

Kaggle, açık veri kümeleri için mükemmel bir kaynaktır. [Veri kümesi arama aracı](https://www.kaggle.com/datasets) ile ilginç veri kümeleri bulun ve 3-5 veri kümesini şu kriterlere göre sınıflandırın:

- Veri nicel mi yoksa nitel mi?
- Veri yapılandırılmış, yapılandırılmamış mı yoksa yarı yapılandırılmış mı?

## [Ders Sonrası Test](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Gözden Geçirme ve Kendi Kendine Çalışma

- Bu Microsoft Learn birimi, [Verinizi Sınıflandırın](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) başlıklı, yapılandırılmış, yarı yapılandırılmış ve yapılandırılmamış verilerin ayrıntılı bir dökümüne sahiptir.

## Ödev

[Veri Kümelerini Sınıflandırma](assignment.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.