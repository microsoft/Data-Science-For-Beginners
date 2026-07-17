# Veri Tanımlama

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Veri Tanımlama - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Veri, keşif yapmak ve bilinçli kararlar almak için kullanılan gerçekler, bilgiler, gözlemler ve ölçümlerdir. Veri noktası, veri noktalarının bir koleksiyonu olan bir veri seti içindeki tek bir veri birimidir. Veri setleri farklı formatlarda ve yapılarda olabilir ve genellikle kaynağına veya verinin nereden geldiğine bağlıdır. Örneğin, bir şirketin aylık kazancı bir elektronik tabloda olabilir ancak bir akıllı saatten gelen saatlik kalp atış hızı verisi [JSON](https://stackoverflow.com/a/383699) formatında olabilir. Veri bilimcilerin bir veri seti içindeki farklı türde verilerle çalışması yaygındır. 

Bu ders, veriyi özellikleri ve kaynaklarına göre tanımlama ve sınıflandırmaya odaklanmaktadır.

## [Ders Öncesi Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Veri Nasıl Tanımlanır

### Ham Veri
Ham veri, kaynağından alınmış, ilk halindeki ve henüz analiz edilmemiş veya düzenlenmemiş veridir. Bir veri setinde olan biteni anlamak için, verilerin insanlar ve onları analiz etmek için kullanabilecekleri teknolojiler tarafından anlaşılabilir bir formata organize edilmesi gerekir. Bir veri setinin yapısı, onun nasıl düzenlendiğini açıklar ve yapılandırılmış, yapılandırılmamış ve yarı yapılandırılmış olarak sınıflandırılabilir. Bu yapı türleri kaynağa bağlı olarak değişir ancak nihayetinde bu üç kategoriye uyar. 

### Nicel Veri
Nicel veri, bir veri setindeki sayısal gözlemlerdir ve tipik olarak analiz edilebilir, ölçülebilir ve matematiksel olarak kullanılabilir. Nicel veri örnekleri: bir ülkenin nüfusu, bir kişinin boyu veya bir şirketin üç aylık kazancı. Bazı ek analizlerle, nicel veriler Hava Kalitesi İndeksi'nin (AQI) mevsimsel trendlerini keşfetmek veya tipik bir iş günündeki yoğun saat trafiği olasılığını tahmin etmek için kullanılabilir.

### Nitel Veri
Nitel veri, kategorik veri olarak da bilinir, nicel verinin gözlemleri gibi nesnel olarak ölçülemeyen verilerdir. Genellikle bir ürün veya sürecin kalitesini yakalayan çeşitli biçimlerde öznel veridir. Bazen nitel veri sayısaldır ve tipik olarak matematiksel olarak kullanılmaz, örneğin telefon numaraları veya zaman damgaları gibi. Nitel veri örnekleri: video yorumları, bir arabanın marka ve modeli veya en yakın arkadaşlarınızın favori rengi. Nitel veri, tüketicilerin en çok hangi ürünleri sevdiğini anlamak veya iş başvurusu özgeçmişlerinde popüler anahtar kelimeleri belirlemek için kullanılabilir.

### Yapılandırılmış Veri
Yapılandırılmış veri, satırlar ve sütunlar halinde düzenlenmiş verilerdir ve her satır aynı sütun setine sahip olur. Sütunlar belirli bir türden bir değeri temsil eder ve değerin neyi temsil ettiğini açıklayan bir isimle tanımlanır, satırlar ise gerçek değerleri içerir. Sütunlarda genellikle değerlerin doğru temsilini sağlamak için belirli kurallar veya kısıtlamalar bulunur. Örneğin, her satırda bir telefon numarası bulunması gereken ve telefon numaralarında asla harf bulunmayan bir müşteri elektronik tablosunu düşünün. Telefon numarası sütununda boş olmaması ve sadece sayı içermesi için kurallar uygulanabilir. 

Yapılandırılmış verinin bir avantajı, diğer yapılandırılmış verilerle ilişkili olacak şekilde düzenlenebilmesidir. Ancak, veriler belirli bir şekilde düzenlenmek üzere tasarlandığı için, genel yapısında değişiklik yapmak büyük çaba gerektirebilir. Örneğin, müşteri elektronik tablosuna boş bırakılmaması gereken bir e-posta sütunu eklemek, bu değerlerin var olan müşteri satırlarına nasıl eklenebileceğini çözmek anlamına gelir. 

Yapılandırılmış veri örnekleri: elektronik tablolar, ilişkisel veritabanları, telefon numaraları, banka hesap dökümleri

### Yapılandırılmamış Veri
Yapılandırılmamış veri genellikle satırlara veya sütunlara kategorize edilemez ve takip etmesi gereken bir format ya da kural seti yoktur. Yapılandırılmamış veride yapısal kısıtlamalar daha az olduğu için, yeni bilgi eklemek yapılandırılmış veri setine kıyasla daha kolaydır. Örneğin, her 2 dakikada bir barometrik basıncı ölçen bir sensör artık sıcaklığı da ölçüp kaydedebiliyorsa, yapılandırılmamış veri ise mevcut verileri değiştirmeye gerek yoktur. Ancak bu tür verinin analiz edilmesi veya incelenmesi daha uzun sürebilir. Örneğin, bir bilim insanı sensör verilerinden geçen ayın ortalama sıcaklığını bulmak ister ancak sensörün bazı verilerde kırık olduğunu belirtmek için "e" yazdığını keşfeder, bu da verilerin eksik olduğu anlamına gelir.

Yapılandırılmamış veri örnekleri: metin dosyaları, kısa mesajlar, video dosyaları

### Yarı Yapılandırılmış Veri
Yarı yapılandırılmış veri, yapılandırılmış ile yapılandırılmamış verinin birleşimi özellikler taşır. Genellikle satır ve sütun formatına uymasa da yapılandırılmış şekilde düzenlenmiş olup sabit format veya kurallar seti izleyebilir. Yapı, iyi tanımlanmış bir hiyerarşiden yeni bilgilerin kolayca entegre edilmesine izin veren daha esnek yapılara kadar kaynaklar arasında değişebilir. Meta veriler, verinin nasıl düzenlendiği ve saklandığını belirlemeye yardımcı olan göstergelerdir ve veri tipine göre farklı isimler taşıyabilir. Meta verilerin bazı yaygın isimleri etiketler, elementler, varlıklar ve niteliklerdir. Örneğin, tipik bir e-posta mesajının bir konusu, gövdesi ve alıcıları vardır ve kim tarafından ya da ne zaman gönderildiğine göre düzenlenebilir. 

Yarı yapılandırılmış veri örnekleri: HTML, CSV dosyaları, JavaScript Nesne Gösterimi (JSON)

## Veri Kaynakları 

Veri kaynağı, verinin üretildiği ilk yerdir veya verinin "yaşadığı" yerdir ve ne zaman ve nasıl toplandığına göre değişir. Kullanıcıları tarafından üretilen veriler birincil veri olarak bilinirken, genel kullanım için veri toplayan kaynaktan gelen veriler ikincil veri olarak adlandırılır. Örneğin, bir grup bilim insanının bir yağmur ormanında yaptığı gözlemler birincil kabul edilir ve onları diğer bilim insanlarıyla paylaşırlarsa kullananlar için ikincil olur. 

Veritabanları yaygın bir kaynaktır ve veriyi barındırmak ve yönetmek için veritabanı yönetim sistemi gerektirir; kullanıcılar veriyi keşfetmek için sorgu adı verilen komutları kullanır. Dosyalar da ses, görüntü ve video dosyaları ile Excel gibi elektronik tablolar olabilir. İnternet kaynakları veri barındırma için yaygın yerlerdir; burada hem veritabanları hem de dosyalar bulunabilir. Uygulama programlama arayüzleri (API'ler), programcıların veriyi dış kullanıcılarla internet üzerinden paylaşmanın yollarını oluşturmasını sağlar, web kazıma ise bir web sayfasından veri çıkarır. [Veri ile Çalışma](../../../../../../../../../2-Working-With-Data) dersleri çeşitli veri kaynaklarının nasıl kullanılacağını anlatır. 

## Sonuç

Bu derste şunları öğrendik:

- Veri nedir
- Verinin nasıl tanımlandığı
- Veri nasıl sınıflandırılır ve kategorize edilir
- Veri nerede bulunur

## 🚀 Meydan Okuma

Kaggle, açık veri setleri için mükemmel bir kaynaktır. [Veri seti arama aracını](https://www.kaggle.com/datasets) kullanarak ilginç veri setleri bulun ve 3-5 veri setini bu kriterlere göre sınıflandırın:

- Veri nicel mi yoksa nitel mi?
- Veri yapılandırılmış, yapılandırılmamış mı yoksa yarı yapılandırılmış mı?

## [Ders Sonrası Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## İnceleme & Kendi Kendine Çalışma

- Bu Microsoft Learn ünitesi, [Veri formatlarını tanımlama](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) yapılandırılmış, yarı yapılandırılmış ve yapılandırılmamış verinin detaylı bir dökümünü sunar.

## Ödev

[Veri Setlerini Sınıflandırma](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->