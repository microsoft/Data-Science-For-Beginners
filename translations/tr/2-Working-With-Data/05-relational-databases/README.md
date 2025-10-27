<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T18:51:42+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "tr"
}
-->
# Verilerle Çalışmak: İlişkisel Veritabanları

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Verilerle Çalışmak: İlişkisel Veritabanları - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Muhtemelen geçmişte bilgi depolamak için bir elektronik tablo kullanmışsınızdır. Satır ve sütunlardan oluşan bir yapı vardı; satırlar bilgiyi (veya veriyi) içerirken, sütunlar bu bilgiyi tanımlıyordu (bazen meta veri olarak adlandırılır). İlişkisel bir veritabanı, tablolar içindeki satır ve sütunların bu temel prensibi üzerine inşa edilmiştir. Bu, bilgiyi birden fazla tabloya yaymanıza olanak tanır, böylece daha karmaşık verilerle çalışabilir, tekrarları önleyebilir ve verileri keşfetme konusunda daha fazla esneklik sağlayabilirsiniz. Şimdi ilişkisel veritabanı kavramlarını inceleyelim.

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Her şey tablolarla başlar

Bir ilişkisel veritabanının temelinde tablolar bulunur. Elektronik tabloda olduğu gibi, bir tablo sütunlar ve satırlardan oluşan bir koleksiyondur. Satır, üzerinde çalışmak istediğimiz veriyi veya bilgiyi içerir, örneğin bir şehrin adı veya yağış miktarı. Sütunlar ise depolanan veriyi tanımlar.

Şehirler hakkında bilgi depolamak için bir tablo oluşturarak keşfimize başlayalım. Şehirlerin adını ve ülkesini içerebiliriz. Bunu aşağıdaki gibi bir tabloda saklayabilirsiniz:

| Şehir    | Ülke          |
| -------- | ------------- |
| Tokyo    | Japonya       |
| Atlanta  | Amerika Birleşik Devletleri |
| Auckland | Yeni Zelanda  |

Dikkat edin, **şehir**, **ülke** ve **nüfus** sütun adları depolanan veriyi tanımlıyor ve her satır bir şehir hakkında bilgi içeriyor.

## Tek tablo yaklaşımının eksiklikleri

Yukarıdaki tablo size oldukça tanıdık geliyor olabilir. Gelişmekte olan veritabanımıza biraz daha veri ekleyelim - yıllık yağış miktarı (milimetre cinsinden). 2018, 2019 ve 2020 yıllarına odaklanacağız. Tokyo için ekleyecek olsaydık, şöyle görünebilirdi:

| Şehir | Ülke   | Yıl  | Miktar |
| ----- | ------ | ---- | ------ |
| Tokyo | Japonya| 2020 | 1690   |
| Tokyo | Japonya| 2019 | 1874   |
| Tokyo | Japonya| 2018 | 1445   |

Tablomuzda ne fark ettiniz? Şehrin adını ve ülkesini tekrar tekrar kopyaladığımızı fark etmiş olabilirsiniz. Bu, oldukça fazla depolama alanı kaplayabilir ve birden fazla kopyaya sahip olmak büyük ölçüde gereksizdir. Sonuçta, Tokyo'nun ilgilendiğimiz tek bir adı var.

Tamam, başka bir şey deneyelim. Her yıl için yeni sütunlar ekleyelim:

| Şehir    | Ülke          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japonya       | 1445 | 1874 | 1690 |
| Atlanta  | Amerika Birleşik Devletleri | 1779 | 1111 | 1683 |
| Auckland | Yeni Zelanda  | 1386 | 942  | 1176 |

Bu, satır tekrarını önlerken başka zorluklar ekliyor. Her yeni yıl olduğunda tablomuzun yapısını değiştirmemiz gerekecek. Ayrıca, verilerimiz büyüdükçe yılları sütun olarak tutmak, değerleri geri almak ve hesaplamak için işleri zorlaştıracaktır.

Bu nedenle birden fazla tabloya ve ilişkilere ihtiyacımız var. Verilerimizi bölerek tekrarları önleyebilir ve verilerle çalışma konusunda daha fazla esneklik sağlayabiliriz.

## İlişkilerin kavramları

Verilerimize geri dönelim ve nasıl bölmek istediğimize karar verelim. Şehirlerimizin adını ve ülkesini saklamak istediğimizi biliyoruz, bu yüzden bu muhtemelen en iyi şekilde bir tabloda çalışır.

| Şehir    | Ülke          |
| -------- | ------------- |
| Tokyo    | Japonya       |
| Atlanta  | Amerika Birleşik Devletleri |
| Auckland | Yeni Zelanda  |

Ancak bir sonraki tabloyu oluşturmadan önce, her şehri nasıl referans alacağımızı belirlememiz gerekiyor. Bir tür tanımlayıcıya, kimliğe veya (teknik veritabanı terimleriyle) bir birincil anahtara ihtiyacımız var. Birincil anahtar, bir tabloda belirli bir satırı tanımlamak için kullanılan bir değerdir. Bu, bir değere dayalı olabilir (örneğin, şehrin adını kullanabiliriz), ancak neredeyse her zaman bir sayı veya başka bir tanımlayıcı olmalıdır. Kimliğin asla değişmemesi gerekir, çünkü bu ilişkiyi bozabilir. Çoğu durumda, birincil anahtar veya kimlik otomatik olarak oluşturulan bir sayı olacaktır.

> ✅ Birincil anahtar genellikle PK olarak kısaltılır.

### şehirler

| şehir_id | Şehir    | Ülke          |
| -------- | -------- | ------------- |
| 1        | Tokyo    | Japonya       |
| 2        | Atlanta  | Amerika Birleşik Devletleri |
| 3        | Auckland | Yeni Zelanda  |

> ✅ Bu derste "id" ve "birincil anahtar" terimlerini birbirinin yerine kullandığımızı fark edeceksiniz. Buradaki kavramlar, daha sonra keşfedeceğiniz DataFrame'ler için de geçerlidir. DataFrame'ler "birincil anahtar" terminolojisini kullanmaz, ancak benzer şekilde davrandıklarını fark edeceksiniz.

Şehirler tablomuzu oluşturduktan sonra, yağış miktarını saklayalım. Şehir hakkında tam bilgiyi kopyalamak yerine, kimliği kullanabiliriz. Ayrıca, yeni oluşturulan tablonun da bir *id* sütununa sahip olduğundan emin olmalıyız, çünkü tüm tabloların bir kimliği veya birincil anahtarı olmalıdır.

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

Yeni oluşturulan **yağış** tablosundaki **şehir_id** sütununa dikkat edin. Bu sütun, **şehirler** tablosundaki kimliklere referans veren değerler içerir. Teknik ilişkisel veri terimlerinde, bu bir **yabancı anahtar** olarak adlandırılır; başka bir tablodan bir birincil anahtardır. Bunu sadece bir referans veya işaretçi olarak düşünebilirsiniz. **şehir_id** 1, Tokyo'yu ifade eder.

> [!NOTE] 
> Yabancı anahtar genellikle FK olarak kısaltılır.

## Veriyi Geri Çağırma

Verilerimizi iki tabloya ayırdıktan sonra, bunları nasıl geri çağıracağımızı merak ediyor olabilirsiniz. MySQL, SQL Server veya Oracle gibi bir ilişkisel veritabanı kullanıyorsanız, Structured Query Language veya SQL adı verilen bir dil kullanabilirsiniz. SQL (bazen "sequel" olarak telaffuz edilir), ilişkisel bir veritabanında veri almak ve değiştirmek için kullanılan standart bir dildir.

Veriyi almak için `SELECT` komutunu kullanırsınız. Temelde, görmek istediğiniz sütunları **seçer** ve bunların bulunduğu tabloyu **from** ile belirtirsiniz. Sadece şehirlerin isimlerini göstermek isteseydiniz, aşağıdaki sorguyu kullanabilirdiniz:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` sütunları listelediğiniz yerdir ve `FROM` tabloları listelediğiniz yerdir.

> [!NOTE] 
> SQL sözdizimi büyük/küçük harf duyarlı değildir, yani `select` ve `SELECT` aynı anlama gelir. Ancak, kullandığınız veritabanı türüne bağlı olarak sütunlar ve tablolar büyük/küçük harf duyarlı olabilir. Bu nedenle, programlamada her şeyi büyük/küçük harf duyarlıymış gibi ele almak en iyi uygulamadır. SQL sorguları yazarken yaygın bir uygulama, anahtar kelimeleri tamamen büyük harflerle yazmaktır.

Yukarıdaki sorgu tüm şehirleri gösterecektir. Sadece Yeni Zelanda'daki şehirleri göstermek istediğimizi hayal edelim. Bir tür filtreye ihtiyacımız var. SQL'deki anahtar kelime `WHERE`, yani "bir şey doğru olduğunda"dır.

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Veriyi Birleştirme

Şimdiye kadar veriyi tek bir tablodan aldık. Şimdi hem **şehirler** hem de **yağış** tablolarındaki verileri bir araya getirmek istiyoruz. Bu, onları *birleştirerek* yapılır. Etkili bir şekilde iki tablo arasında bir bağlantı oluşturur ve her tablodan bir sütunun değerlerini eşleştirir.

Örneğimizde, **yağış** tablosundaki **şehir_id** sütununu **şehirler** tablosundaki **şehir_id** sütunuyla eşleştireceğiz. Bu, yağış değerini ilgili şehirle eşleştirecektir. Yapacağımız birleştirme türü, *iç birleştirme* olarak adlandırılır, yani diğer tablodan hiçbir şeyle eşleşmeyen satırlar görüntülenmeyecektir. Bizim durumumuzda her şehrin yağış verisi var, bu yüzden her şey görüntülenecek.

Şimdi tüm şehirler için 2019 yılı yağışlarını alalım.

Bunu adım adım yapacağız. İlk adım, verileri birleştirmek için dikiş sütunlarını belirtmek - daha önce vurguladığımız gibi **şehir_id**.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

İstediğimiz iki sütunu ve tabloları **şehir_id** ile birleştirmek istediğimizi vurguladık. Şimdi sadece 2019 yılını filtrelemek için `WHERE` ifadesini ekleyebiliriz.

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

İlişkisel veritabanları, bilgiyi birden fazla tabloya bölmek ve ardından görüntüleme ve analiz için bir araya getirmek üzerine kuruludur. Bu, hesaplamalar yapmak ve veriyi manipüle etmek için yüksek bir esneklik sağlar. İlişkisel bir veritabanının temel kavramlarını ve iki tablo arasında bir birleştirme yapmayı nasıl gerçekleştireceğinizi gördünüz.

## 🚀 Meydan Okuma

İnternette birçok ilişkisel veritabanı bulunmaktadır. Yukarıda öğrendiğiniz becerileri kullanarak verileri keşfedebilirsiniz.

## Ders Sonrası Test

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Gözden Geçirme ve Kendi Kendine Çalışma

SQL ve ilişkisel veritabanı kavramlarını keşfetmeye devam etmeniz için [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) üzerinde birkaç kaynak bulunmaktadır:

- [İlişkisel veri kavramlarını açıklayın](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Transact-SQL ile Sorgulamaya Başlayın](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL, SQL'in bir versiyonudur)
- [Microsoft Learn'de SQL içeriği](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Ödev

[Ödev Başlığı](assignment.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.