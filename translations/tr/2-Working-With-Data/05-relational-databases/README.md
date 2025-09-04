<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-04T18:08:58+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "tr"
}
-->
# Verilerle Çalışmak: İlişkisel Veritabanları

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Verilerle Çalışmak: İlişkisel Veritabanları - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Muhtemelen geçmişte bilgileri saklamak için bir elektronik tablo kullandınız. Satır ve sütunlardan oluşan bir düzeniniz vardı; satırlar bilgileri (veya verileri) içerirken, sütunlar bu bilgileri tanımlıyordu (bazen buna meta veri denir). İlişkisel bir veritabanı, tablolardaki sütunlar ve satırlar temel prensibi üzerine kuruludur ve bilgilerin birden fazla tabloya yayılmasına olanak tanır. Bu, daha karmaşık verilerle çalışmanıza, tekrardan kaçınmanıza ve verileri keşfetme konusunda esneklik sağlamanıza olanak tanır. Haydi, ilişkisel veritabanı kavramlarını keşfedelim.

## [Ders Öncesi Test](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Her şey tablolarla başlar

Bir ilişkisel veritabanının temelinde tablolar bulunur. Elektronik tabloda olduğu gibi, bir tablo sütunlar ve satırlardan oluşan bir koleksiyondur. Satır, üzerinde çalışmak istediğimiz verileri veya bilgileri içerir, örneğin bir şehrin adı veya yağış miktarı. Sütunlar ise depoladıkları verileri tanımlar.

Şehirler hakkında bilgi saklamak için bir tablo oluşturarak keşfimize başlayalım. Şehirlerin adını ve ülkesini saklayarak başlayabiliriz. Bunu aşağıdaki gibi bir tabloda saklayabilirsiniz:

| Şehir    | Ülke          |
| -------- | ------------- |
| Tokyo    | Japonya       |
| Atlanta  | Amerika Birleşik Devletleri |
| Auckland | Yeni Zelanda  |

Dikkat edin, **şehir**, **ülke** ve **nüfus** sütun adları depolanan verileri tanımlıyor ve her satır bir şehir hakkında bilgi içeriyor.

## Tek tablo yaklaşımının eksiklikleri

Yukarıdaki tablo size oldukça tanıdık geliyor olabilir. Gelişmekte olan veritabanımıza yıllık yağış miktarını (milimetre cinsinden) ekleyerek başlayalım. 2018, 2019 ve 2020 yıllarına odaklanacağız. Tokyo için ekleyecek olursak, tablo şu şekilde görünebilir:

| Şehir  | Ülke    | Yıl  | Miktar |
| ------ | ------- | ---- | ------ |
| Tokyo  | Japonya | 2020 | 1690   |
| Tokyo  | Japonya | 2019 | 1874   |
| Tokyo  | Japonya | 2018 | 1445   |

Tablomuzda ne fark ettiniz? Şehrin adını ve ülkesini tekrar tekrar çoğalttığımızı fark edebilirsiniz. Bu, oldukça fazla depolama alanı kaplayabilir ve gereksiz bir şekilde birden fazla kopyaya sahip olmamıza neden olur. Sonuçta, Tokyo'nun ilgilendiğimiz tek bir adı var.

Tamam, başka bir şey deneyelim. Her yıl için yeni sütunlar ekleyelim:

| Şehir    | Ülke          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japonya       | 1445 | 1874 | 1690 |
| Atlanta  | Amerika Birleşik Devletleri | 1779 | 1111 | 1683 |
| Auckland | Yeni Zelanda  | 1386 | 942  | 1176 |

Bu, satır çoğaltmayı önlerken başka zorluklar ekler. Her yeni yıl olduğunda tablomuzun yapısını değiştirmemiz gerekecek. Ayrıca, verilerimiz büyüdükçe yılları sütun olarak tutmak değerleri almak ve hesaplamak açısından daha zor hale gelecektir.

Bu nedenle birden fazla tabloya ve ilişkilere ihtiyacımız var. Verilerimizi bölerek tekrardan kaçınabilir ve verilerle çalışma konusunda daha fazla esneklik sağlayabiliriz.

## İlişkiler kavramı

Verilerimize geri dönelim ve nasıl bölmek istediğimizi belirleyelim. Şehirlerimizin adı ve ülkesini saklamak istediğimizi biliyoruz, bu muhtemelen bir tabloda en iyi şekilde çalışacaktır.

| Şehir    | Ülke          |
| -------- | ------------- |
| Tokyo    | Japonya       |
| Atlanta  | Amerika Birleşik Devletleri |
| Auckland | Yeni Zelanda  |

Ancak bir sonraki tabloyu oluşturmadan önce her şehri nasıl referans alacağımızı belirlememiz gerekiyor. Bir tür tanımlayıcıya, kimliğe veya (teknik veritabanı terimleriyle) birincil anahtara ihtiyacımız var. Birincil anahtar, bir tabloda belirli bir satırı tanımlamak için kullanılan bir değerdir. Bu, bir değere dayalı olabilir (örneğin, şehrin adını kullanabiliriz), ancak neredeyse her zaman bir sayı veya başka bir tanımlayıcı olmalıdır. Kimliğin asla değişmemesini isteriz, çünkü bu ilişkiyi bozabilir. Çoğu durumda birincil anahtar veya kimlik otomatik olarak oluşturulan bir sayı olacaktır.

> ✅ Birincil anahtar genellikle PK olarak kısaltılır

### şehirler

| şehir_id | Şehir    | Ülke          |
| -------- | -------- | ------------- |
| 1        | Tokyo    | Japonya       |
| 2        | Atlanta  | Amerika Birleşik Devletleri |
| 3        | Auckland | Yeni Zelanda  |

> ✅ Bu derste "id" ve "birincil anahtar" terimlerini birbirinin yerine kullandığımızı fark edeceksiniz. Buradaki kavramlar, daha sonra keşfedeceğiniz DataFrame'lere de uygulanır. DataFrame'ler "birincil anahtar" terminolojisini kullanmaz, ancak aynı şekilde davrandıklarını fark edeceksiniz.

Şehirler tablomuzu oluşturduktan sonra yağış miktarını saklayalım. Şehir hakkında tam bilgiyi çoğaltmak yerine kimliği kullanabiliriz. Ayrıca, yeni oluşturulan tablonun da bir *id* sütununa sahip olduğundan emin olmalıyız, çünkü tüm tabloların bir kimliği veya birincil anahtarı olmalıdır.

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

Yeni oluşturulan **yağış** tablosundaki **şehir_id** sütununa dikkat edin. Bu sütun, **şehirler** tablosundaki kimliklere referans olan değerleri içerir. Teknik ilişkisel veri terimlerinde buna **yabancı anahtar** denir; başka bir tablodan bir birincil anahtardır. Bunu bir referans veya işaretçi olarak düşünebilirsiniz. **şehir_id** 1 Tokyo'yu ifade eder.

> [!NOTE] Yabancı anahtar genellikle FK olarak kısaltılır

## Verileri alma

Verilerimizi iki tabloya ayırdıktan sonra, nasıl alacağımızı merak ediyor olabilirsiniz. MySQL, SQL Server veya Oracle gibi bir ilişkisel veritabanı kullanıyorsak, Structured Query Language veya SQL adlı bir dil kullanabiliriz. SQL (bazen sequel olarak telaffuz edilir), ilişkisel bir veritabanında veri almak ve değiştirmek için kullanılan standart bir dildir.

Veri almak için `SELECT` komutunu kullanırsınız. Temelde, görmek istediğiniz sütunları **seçer** ve bunların bulunduğu tabloyu **belirtirsiniz**. Sadece şehirlerin adlarını göstermek istiyorsanız, aşağıdaki sorguyu kullanabilirsiniz:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` sütunları listelediğiniz yerdir ve `FROM` tabloları listelediğiniz yerdir.

> [NOTE] SQL sözdizimi büyük/küçük harf duyarsızdır, yani `select` ve `SELECT` aynı anlama gelir. Ancak, kullandığınız veritabanı türüne bağlı olarak sütunlar ve tablolar büyük/küçük harf duyarlı olabilir. Bu nedenle, programlamada her şeyi büyük/küçük harf duyarlıymış gibi ele almak en iyi uygulamadır. SQL sorguları yazarken yaygın bir uygulama, anahtar kelimeleri tamamen büyük harflerle yazmaktır.

Yukarıdaki sorgu tüm şehirleri gösterecektir. Sadece Yeni Zelanda'daki şehirleri göstermek istediğimizi hayal edelim. Bir tür filtreye ihtiyacımız var. SQL'deki anahtar kelime `WHERE`, yani "bir şey doğru olduğunda"dır.

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Verileri birleştirme

Şimdiye kadar verileri tek bir tablodan aldık. Şimdi **şehirler** ve **yağış** tablolarındaki verileri bir araya getirmek istiyoruz. Bu, onları *birleştirerek* yapılır. İki tablo arasında bir dikiş oluşturacak ve her tablodan bir sütunun değerlerini eşleştireceksiniz.

Örneğimizde, **yağış** tablosundaki **şehir_id** sütununu **şehirler** tablosundaki **şehir_id** sütunuyla eşleştireceğiz. Bu, yağış değerini ilgili şehriyle eşleştirecektir. Yapacağımız birleştirme türü, *iç birleştirme* olarak adlandırılır, yani diğer tablodan hiçbir şeyle eşleşmeyen satırlar görüntülenmeyecektir. Bizim durumumuzda her şehirde yağış var, bu yüzden her şey görüntülenecek.

Haydi, tüm şehirler için 2019 yılı yağışlarını alalım.

Bunu adım adım yapacağız. İlk adım, **şehir_id** sütununu vurgulayarak verileri birleştirmek.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Birleştirmek istediğimiz iki sütunu ve tabloları **şehir_id** ile birleştirmek istediğimizi vurguladık. Şimdi sadece 2019 yılını filtrelemek için `WHERE` ifadesini ekleyebiliriz.

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

İlişkisel veritabanları, bilgileri birden fazla tabloya bölmek ve ardından görüntüleme ve analiz için bir araya getirmek üzerine kuruludur. Bu, hesaplamalar yapmak ve verileri manipüle etmek için yüksek derecede esneklik sağlar. İlişkisel bir veritabanının temel kavramlarını ve iki tablo arasında bir birleştirme yapmayı gördünüz.

## 🚀 Meydan Okuma

İnternette birçok ilişkisel veritabanı bulunmaktadır. Yukarıda öğrendiğiniz becerileri kullanarak verileri keşfedebilirsiniz.

## Ders Sonrası Test

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ds/)

## Gözden Geçirme ve Kendi Kendine Çalışma

SQL ve ilişkisel veritabanı kavramlarını keşfetmeye devam etmeniz için [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) üzerinde çeşitli kaynaklar bulunmaktadır.

- [İlişkisel veri kavramlarını açıklayın](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Transact-SQL ile sorgulamaya başlayın](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL, SQL'in bir versiyonudur)
- [Microsoft Learn'deki SQL içeriği](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Ödev

[Ödev Başlığı](assignment.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.