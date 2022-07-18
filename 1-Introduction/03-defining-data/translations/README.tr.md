# Veriyi Tanımlamak

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/03-DefiningData.png)|
|:---:|
|Veriyi Tanımlamak - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Veri, keşifler yapmak ve bilinçli kararları desteklemek için kullanılan gerçekler, bilgi, gözlemler ve ölçümlerdir. Bir veri noktası, veri noktalarından oluşan bir yığın olan veri setlerindeki bir birim veridir. Veri setleri genellikle kaynağına veya verinin nereden geldiğine bağlı olarak farklı formatlarda ve yapılarda bulunabilir. Örneğin, bir şirketin aylık kazancı bir hesap çizelgesinde bulunabilecekken bir akıllı saatten gelen saatlik kalp atışı verisi [JSON] (https://stackoverflow.com/a/383699) formatında olabilir.

Bu ders veriyi karakteristiklerine ve kaynaklarına göre tanımlama ve sınıflandırma üzerine odaklanmaktadır.

## [Ders Öncesi Kısa Sınavı](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)

## Veri nasıl tanımlanır

**Ham veri** kaynağından oluşturulduğu şekilde aktarılan ve analiz edilmemiş veya düzenlenmemiş veridir. Bir veri setinde ne olduğunu anlayabilmek için veri setlerinin insanların ve verilerin daha ileri düzeyde analiz etmekte kullanabilecekleri teknolojilerin anlayabileceği bir formatta düzenlenmesi gerekmektedir. Bir veri setinin yapısı veri setinin nasıl düzenlendiğini açıklar ve yapısal, yapısal olmayan ve yarı yapısal olarak sınıflandırılabilir.Bu yapı tipleri değişkenlik gösterebilir ve kaynağa bağlıdır ancak veri setleri nihayetinde bu üç kategoriden birisine uyacaktır.

### Nicel veri

Nicel veri bir veri setinin içerisindeki sayısal gözlemlerdir ve genel olacak analiz edilebilir, ölçülebilir ve matematiksel olarak kullanılabilirdir. Nicel verinin bazı örnekleri şu şekilde verilebilir: ülkenin nüfusu, kişinin boyu veya şirketin kazancı. Bazı ek analizlerle nicel veri, Hava Kalitesi İndeksi'nin sezonsal eğilimlerini keşfetmek için veya sıradan bir iş günündeki trafiğin en yoğun olduğu zamanları tahmin etmek için kullanılabilir.

### Nitel veri
Nitel veri veya diğer adıysal kategorik veri, nicel verinin gözlemlerindeki gibi objektif olarak ölçülemeyen verilerdir. Genel olarak ürün veya süreç gibi bir şeyin niteliğini tutan çeşitli formatlardaki subjektif verilerdir. Bazen nitel veri telefon numaraları veya zaman damgaları gibi sayısal olabilir ve genellikle bunlar matematiksel olarak kullanılamaz. Nitel data ile ilgili bazı örnekler: video yorumları, bir arabanın marka ve modeli veya en yakın arkadaşının en sevdiği rengi. Nitel veri, müşterilerin hangi ürünleri en çok sevdiğini görmekte veya bir iş başvurusundaki öz geçmişlerde sıklıkla kullanılan kelimeleri belirlemekte kullanılabilir.

### Yapısal veri

Yapısal veri, her satırın aynı sütun takımına sahip olduğu satır ve sütunlarla düzenlenmiş veridir. Sütunlar belirli bir tipteki değeri temsil eder ve değerin neyi temsil ettiğini açıklayan bir isimle tanımlanır, satırlar ise gerçek değerleri bulundurur. Sütunlar genellikle değerin doğru bir şekilde sütunu temsil ettiğini güvence altına almak için spesifik bir dizi kurallara ya da değerler üzerinde sınırlandırmalara sahip olur. Örneğin her satırın bir telefon numarası içermesi gerektiği ve numaraların alfabetik karakterleri asla içermemesi gerektiği bir müşteri çizelgesini düşünün. Telefon numarası sütununa asla boş olmaması ve sadece numara içerdiğinden emin olmak için kurallar uygulanmış olabilir.

Yapısal verinin bir faydası diğer yapısal verilerle ilişkilendirilerek düzenlenebilir olmasıdır. Ancak veri spesifik bir şekilde düzenlendiği için genel yapısında değişiklikler yapmak oldukça fazla efor gerektirecektir. Örneğin bir müşteri çizelgesine bir email sütunu eklemek, sizin aynı zamanda veri setinde bulunan varolan müşteri satırlarına bu değerleri nasıl ekleyeceğinizi çözmenizi gerektirecektir.

Yapısal veriye örnekler: çizelgeler, ilişkisel veritabanları, telefon numaraları, hesap ekstreleri

### Yapısal olmayan veri

Yapısal olmayan veri genellikle satırlar ve sütunlar kullanılarak kategorize edilemez ve bir format veya takip edilecek kurallar bulundurmazlar. Çünkü yapısal olmayan veriler yapılarında daha az sınırlandırmalar bulundururlar. Yapısal veri setleriyle karşılaştırıldığında yeni bilgi eklemek daha kolaydır. Her 2 dakikada bir barometrik basınç verisini toplayan bir sensör eğer sıcaklığı da ölçüp kaydetmesine izin veren bir güncelleme aldıysa ve eğer veri yapısal değilse mevcut veride değişiklik yapmamıza gerek kalmaz. Ancak bu tip bir veriyi analiz edip incelemek daha uzun süre alabilir. Örneğin sensör verisinden geçen ayki ortalama sıcaklığı bulmak isteyen bir bilim adamını düşünelim. Fakat keşfediyor ki sensör topladığı verilerde bir sayı yerine hatalı olduğunu gösteren "e" harfini kaydetmiş, yani bu demek oluyor ki veri eksiktir.

Yapısal olmayan veriler üzerine örnekler: metin dosyaları, metin iletisi, video dosyaları

### Yarı yapısal

Yarı yapısal veri, onu hem yapısal hem de yapısal olmayan verinin bir kombinasyonu yapan özelliklere sahiptir. Genellikle satır ve sütunlar formatına uymaz ancak yapısal olarak kabul edilebilecek bir şekilde düzenlenmiştir ve sabit bir formatı veya bir dizi kuralı takip eder. İyi tanımlanmış bir hiyerarşi veya yeni bilginin kolay entegrasyonuna izin veren daha esnek bir şeyler gibi kaynaklar arasında yapı değişkenlik gösterecektir. Metaveri verilerin nasıl organize edileceğine ve saklanacağına karar vermeye yardımcı olan göstergelerdir ve verinin tipine dayalı olarak çeşitli isimleri olacaktır. Etiketler, elemanlar, varlıklar ve nitelikler bazı yaygın metaveri isimleridir. Örneğin tipik bir email iletisi konuya, mesaj gövdesine ve bir dizi alıcıya sahiptir ve kim tarafından veya ne zaman gönderildiğine göre düzenlenebilir.

Yarı yapısal veriye örnekler: HTML, CSV dosyaları, JavaScript Nesne Notasyonu (JSON)

## Verinin Kaynakları

Bir veri kaynağı verinin oluşturulduğu veya "yaşadığı" ilk konumdur ve nasıl ve ne zaman toplandığına göre değişkenlik gösterecektir. Kullanıcı(lar) tarafından oluşturulan veriler birincil veri olarak tanımlanırken ikincil veri dediğimiz veriler genel kullanım için toplanmış verilerin bulunduğu bir kaynaktan gelir. Örneğin bir yağmur ormanındaki gözlemleri toplayan bir gurup bilim adamı birincil kaynak olarak nitelendirilebilirken eğer bu kişiler toplandıkları verileri başka bilim adamlarıyla paylaşmak isterlerse bu verileri kullanacaklara bu veriler ikincil veri olacaktır.

Veritabanları yaygın bir kaynaktır ve verileri tutmak ve sürdürülebilirliği sağlamak için bir veritabanı yönetim sistemine bağlıdır. Kullanıcılar verileri araştırmak için sorgular dediğimiz komutları kullanır. Dosya şeklindeki veir kaynakları sesler, görüntüler ve video dosyaları olabileceği gibi Excel gibi hesap çizelgeleri de olabilir. Veritabanlarının ve dosyaların bulunabileceği internet kaynakları verileri barındırmak için yaygın bir kaynaktır. Uygulama programlama arayüzleri (API) programlamacıların harici kullanıcılara internet üzerinden veri paylaşımı için yollar oluşturmaya olanak sağlarken web kazıma işlemi web sitelerinden veri çıkarmaya yarar. ["Veriyle Çalışmak"taki dersler](../../../2-Working-With-Data) çeşitli veri kaynaklarının nasıl kullanılacağına odaklanmaktadır.

## Sonuç

Bu derste öğrendiklerimizi gözden geçirelim:

- Verinin ne olduğunu
- Verinin nasıl tanımlandığını
- Verinin nasıl sınıflandırılıp kategorize edildiğini
- Verinin nerelerde bulunabileceği öğrendik.

## 🚀 Challange

Kaggle mükemmel bir açık veri seti kaynağıdır. İlginç birkaç veri seti bulmak ve 3 ila 5 veri setini aşağıdaki kriterlere göre sıralamak için [Veri seti arama aracını](https://www.kaggle.com/datasets) kullanın.

Kriterler:

- Bu veri nicel midir yoksa nitel midir?
- Bu veri yapısal mıdır, yapısal değil midir yoksa yarı yapısal mıdır? 

## [Ders Sonu Kısa Sınavı](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## İnceleme & Öz Çalışma

- Bu [Verini Sınıflandır](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) başlıklı Microsoft Learn dersi detaylı bir şekilde yapısal, yarı yapısal ve yapısal olmayan verileri ele almaktadır.

## Ödev

[Veri Setlerini Sınıflandırma](../assignment.md)
