<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "870a0086adbc313a8eea5489bdcb2522",
  "translation_date": "2025-08-28T10:51:44+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "tr"
}
-->
# Verilerle Çalışmak: İlişkisel Veritabanları

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Verilerle Çalışmak: İlişkisel Veritabanları - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Muhtemelen geçmişte bilgi depolamak için bir elektronik tablo kullanmışsınızdır. Satır ve sütunlardan oluşan bir yapınız vardı; satırlar bilgiyi (veya veriyi) içerirken, sütunlar bu bilgiyi tanımlıyordu (bazen buna meta veri denir). İlişkisel bir veritabanı, tablolardaki sütunlar ve satırlar prensibine dayanır ve bilgiyi birden fazla tabloya yaymanıza olanak tanır. Bu, daha karmaşık verilerle çalışmanıza, tekrarı önlemenize ve verileri keşfetme şeklinizde esneklik sağlamanıza olanak tanır. Haydi, ilişkisel veritabanı kavramlarını keşfedelim.

## [Ders Öncesi Testi](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Her Şey Tablolarla Başlar

Bir ilişkisel veritabanının temelinde tablolar bulunur. Tıpkı bir elektronik tabloda olduğu gibi, bir tablo sütunlar ve satırlardan oluşan bir koleksiyondur. Satır, çalışmak istediğimiz veriyi veya bilgiyi içerir, örneğin bir şehrin adı ya da yağış miktarı. Sütunlar ise depoladıkları veriyi tanımlar.

Şehirler hakkında bilgi depolamak için bir tablo oluşturarak keşfimize başlayalım. Şehirlerin adını ve ülkesini içeren bir tablo oluşturabiliriz. Bu tablo şu şekilde görünebilir:

| Şehir    | Ülke          |
| -------- | ------------- |
| Tokyo    | Japonya       |
| Atlanta  | Amerika Birleşik Devletleri |
| Auckland | Yeni Zelanda  |

Dikkat edin, **şehir**, **ülke** ve **nüfus** sütun adları depolanan veriyi tanımlar ve her satır bir şehir hakkında bilgi içerir.

## Tek Tablo Yaklaşımının Eksiklikleri

Yukarıdaki tablo size oldukça tanıdık gelebilir. Gelişmekte olan veritabanımıza yıllık yağış miktarını (milimetre cinsinden) ekleyerek biraz daha veri ekleyelim. 2018, 2019 ve 2020 yıllarına odaklanalım. Tokyo için ekleyecek olursak, tablo şu şekilde görünebilir:

| Şehir  | Ülke    | Yıl  | Miktar |
| ------ | ------- | ---- | ------ |
| Tokyo  | Japonya | 2020 | 1690   |
| Tokyo  | Japonya | 2019 | 1874   |
| Tokyo  | Japonya | 2018 | 1445   |

Tablomuzda ne fark ettiniz? Şehrin adı ve ülkesini tekrar tekrar kopyaladığımızı fark etmiş olabilirsiniz. Bu, oldukça fazla depolama alanı kaplayabilir ve büyük ölçüde gereksizdir. Sonuçta, Tokyo'nun ilgilendiğimiz tek bir adı var.

Tamam, başka bir şey deneyelim. Her yıl için yeni sütunlar ekleyelim:

| Şehir    | Ülke          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japonya       | 1445 | 1874 | 1690 |
| Atlanta  | Amerika Birleşik Devletleri | 1779 | 1111 | 1683 |
| Auckland | Yeni Zelanda  | 1386 | 942  | 1176 |

Bu, satır tekrarını önlerken başka zorluklar ekliyor. Her yeni yıl için tablomuzun yapısını değiştirmemiz gerekecek. Ayrıca, verilerimiz büyüdükçe yılları sütun olarak tutmak, değerleri geri almak ve hesaplamak için işleri zorlaştıracaktır.

Bu nedenle birden fazla tabloya ve ilişkilere ihtiyacımız var. Verilerimizi bölerek tekrarı önleyebilir ve verilerle çalışma şeklimizde daha fazla esneklik sağlayabiliriz.

## İlişkilerin Kavramları

Verilerimize geri dönelim ve nasıl böleceğimizi belirleyelim. Şehirlerimizin adını ve ülkesini depolamak istediğimizi biliyoruz, bu nedenle bu bilgiler muhtemelen bir tabloda en iyi şekilde saklanır.

| Şehir    | Ülke          |
| -------- | ------------- |
| Tokyo    | Japonya       |
| Atlanta  | Amerika Birleşik Devletleri |
| Auckland | Yeni Zelanda  |

Ancak bir sonraki tabloyu oluşturmadan önce, her şehri nasıl referans alacağımızı belirlememiz gerekiyor. Bir tür tanımlayıcıya, kimliğe veya (teknik veritabanı terimleriyle) bir birincil anahtara ihtiyacımız var. Birincil anahtar, bir tablodaki belirli bir satırı tanımlamak için kullanılan bir değerdir. Bu, bir değerin kendisine dayalı olabilir (örneğin, şehrin adını kullanabiliriz), ancak neredeyse her zaman bir sayı veya başka bir tanımlayıcı olmalıdır. Kimliğin asla değişmemesini isteriz, çünkü bu ilişkiyi bozabilir. Çoğu durumda, birincil anahtar veya kimlik otomatik olarak oluşturulan bir sayı olacaktır.

> ✅ Birincil anahtar genellikle PK olarak kısaltılır.

### şehirler

| şehir_id | Şehir    | Ülke          |
| -------- | -------- | ------------- |
| 1        | Tokyo    | Japonya       |
| 2        | Atlanta  | Amerika Birleşik Devletleri |
| 3        | Auckland | Yeni Zelanda  |

> ✅ Bu derste "id" ve "birincil anahtar" terimlerini birbirinin yerine kullandığımızı fark edeceksiniz. Buradaki kavramlar, daha sonra keşfedeceğiniz DataFrame'ler için de geçerlidir. DataFrame'ler "birincil anahtar" terminolojisini kullanmaz, ancak benzer şekilde davrandıklarını fark edeceksiniz.

Şehirler tablomuzu oluşturduğumuza göre, yağış miktarını saklayalım. Şehirle ilgili tam bilgiyi kopyalamak yerine, kimliği kullanabiliriz. Ayrıca, yeni oluşturulan tablonun da bir *id* sütununa sahip olduğundan emin olmalıyız, çünkü tüm tabloların bir kimlik veya birincil anahtarı olmalıdır.

### yağış

| yağış_id | şehir_id | Yıl  | Miktar |
| -------- | -------- | ---- | ------ |
| 1        | 1        | 2018 | 1445   |
| 2        | 1        | 2019 | 1874   |
| 3        | 1        | 2020 | 1690   |
| 4        | 2        | 2018 | 1779   |
| 5        | 2        | 2019 | 1111   |
| 6        | 2        | 2020 | 1683   |
| 7        | 3        | 2018 | 1386   |
| 8        | 3        | 2019 | 942    |
| 9        | 3        | 2020 | 1176   |

Yeni oluşturulan **yağış** tablosundaki **şehir_id** sütununa dikkat edin. Bu sütun, **şehirler** tablosundaki kimliklere referans veren değerler içerir. Teknik ilişkisel veri terimleriyle, buna **yabancı anahtar** denir; başka bir tablodan bir birincil anahtardır. Bunu bir referans veya işaretçi olarak düşünebilirsiniz. **şehir_id** 1, Tokyo'yu referans alır.

> [!NOTE] Yabancı anahtar genellikle FK olarak kısaltılır.

## Veriyi Geri Getirme

Verilerimizi iki tabloya ayırdıktan sonra, bunları nasıl geri getireceğimizi merak ediyor olabilirsiniz. MySQL, SQL Server veya Oracle gibi bir ilişkisel veritabanı kullanıyorsak, Yapılandırılmış Sorgu Dili veya SQL adlı bir dil kullanabiliriz. SQL (bazen "sequel" olarak telaffuz edilir), ilişkisel bir veritabanında veri almak ve değiştirmek için kullanılan standart bir dildir.

Veriyi almak için `SELECT` komutunu kullanırsınız. Temel olarak, görmek istediğiniz sütunları **seçer** ve bunların bulunduğu tabloyu **belirtirsiniz**. Sadece şehirlerin adlarını görüntülemek istiyorsanız, şu sorguyu kullanabilirsiniz:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT`, listelemek istediğiniz sütunları, `FROM` ise bu sütunların bulunduğu tabloları belirtir.

> [NOTE] SQL sözdizimi büyük/küçük harf duyarlı değildir, yani `select` ve `SELECT` aynı anlama gelir. Ancak, kullandığınız veritabanı türüne bağlı olarak sütunlar ve tablolar büyük/küçük harf duyarlı olabilir. Bu nedenle, programlamada her şeyi büyük/küçük harf duyarlıymış gibi ele almak en iyi uygulamadır. SQL sorguları yazarken, anahtar kelimeleri tamamen büyük harflerle yazmak yaygın bir konvansiyondur.

Yukarıdaki sorgu tüm şehirleri görüntüler. Sadece Yeni Zelanda'daki şehirleri görüntülemek istediğimizi hayal edelim. Bir tür filtreye ihtiyacımız var. SQL'deki anahtar kelime `WHERE`, yani "bir şey doğru olduğunda"dır.

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Veriyi Birleştirme

Şimdiye kadar veriyi tek bir tablodan aldık. Şimdi **şehirler** ve **yağış** tablolarındaki verileri bir araya getirmek istiyoruz. Bu, onları *birleştirerek* yapılır. İki tablo arasında bir dikiş oluşturur ve her tablodan bir sütundaki değerleri eşleştirirsiniz.

Örneğimizde, **yağış** tablosundaki **şehir_id** sütununu, **şehirler** tablosundaki **şehir_id** sütunuyla eşleştireceğiz. Bu, yağış değerini ilgili şehriyle eşleştirecektir. Yapacağımız birleştirme türü, *iç birleştirme* olarak adlandırılır, yani diğer tablodan hiçbir şeyle eşleşmeyen satırlar görüntülenmez. Bizim durumumuzda her şehirde yağış verisi var, bu yüzden her şey görüntülenecek.

Tüm şehirler için 2019 yılı yağış miktarını alalım.

Bunu adım adım yapacağız. İlk adım, **şehir_id** sütunlarını belirterek verileri birleştirmektir.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Birleştirmek istediğimiz iki sütunu ve tabloları **şehir_id** üzerinden birleştirmek istediğimizi vurguladık. Şimdi sadece 2019 yılını filtrelemek için `WHERE` ifadesini ekleyebiliriz.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Özet

İlişkisel veritabanları, bilgiyi birden fazla tabloya bölmek ve ardından görüntüleme ve analiz için bir araya getirmek üzerine kuruludur. Bu, hesaplamalar yapmak ve verileri manipüle etmek için yüksek bir esneklik sağlar. İlişkisel bir veritabanının temel kavramlarını ve iki tablo arasında bir birleştirme yapmayı gördünüz.

## 🚀 Meydan Okuma

İnternette birçok ilişkisel veritabanı mevcuttur. Yukarıda öğrendiğiniz becerileri kullanarak verileri keşfedebilirsiniz.

## Ders Sonrası Testi

## [Ders Sonrası Testi](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/9)

## Gözden Geçirme ve Kendi Kendine Çalışma

SQL ve ilişkisel veritabanı kavramlarını keşfetmeye devam etmeniz için [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) üzerinde çeşitli kaynaklar mevcuttur:

- [İlişkisel veri kavramlarını açıklayın](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Transact-SQL ile Sorgulamaya Başlayın](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL, SQL'in bir versiyonudur)
- [Microsoft Learn'deki SQL içeriği](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Ödev

[Ödev Başlığı](assignment.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.