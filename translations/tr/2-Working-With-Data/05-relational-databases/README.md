<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T11:22:19+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "tr"
}
-->
# Veri ile Çalışmak: İlişkisel Veritabanları

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Veri ile Çalışmak: İlişkisel Veritabanları - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Geçmişte bilgileri depolamak için bir elektronik tablo kullandığınız olasılığı yüksek. Satırlar ve sütunlardan oluşan bir setiniz vardı; satırlar bilgiyi (veya veriyi) içerirken, sütunlar bilgiyi tanımlıyordu (bazen meta veri olarak adlandırılır). İlişkisel veritabanı, tablolar içindeki sütunlar ve satırlar temel prensibine dayanır ve bilgiyi birden çok tabloya yaymanıza olanak tanır. Bu, daha karmaşık verilerle çalışmanıza, çoğaltmayı önlemenize ve veriyi keşfetme şeklinizde esneklik sağlamanıza olanak tanır. İlişkisel veritabanı kavramlarını keşfedelim.

## [Ön ders sınavı](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Her şey tablolarla başlar

İlişkisel veritabanının temelinde tablolar vardır. Elektronik tabloda olduğu gibi, bir tablo sütunlar ve satırlardan oluşan bir koleksiyondur. Satır, üzerinde çalışmak istediğimiz veri veya bilgiyi içerir; örneğin bir şehrin adı veya yağış miktarı gibi. Sütunlar ise depoladıkları veriyi tanımlar.

Keşfimize şehirler hakkında bilgi depolamak için bir tablo oluşturarak başlayalım. Şehirlerin adı ve ülkesi ile başlayabiliriz. Bunu aşağıdaki gibi bir tabloda depolayabilirsiniz:

| Şehir    | Ülke          |
| -------- | ------------- |
| Tokyo    | Japonya       |
| Atlanta  | Amerika Birleşik Devletleri |
| Auckland | Yeni Zelanda  |

**şehir**, **ülke** ve **nüfus** sütun adlarının depolanan veriyi tanımladığını ve her satırın bir şehir hakkında bilgi içerdiğini fark edin.

## Tek tablo yaklaşımının eksiklikleri

Yukarıdaki tablo size oldukça tanıdık gelebilir. Gelişmekte olan veritabanımıza yıllık yağış miktarını (milimetre cinsinden) ekleyelim. 2018, 2019 ve 2020 yıllarına odaklanacağız. Tokyo için eklersek şöyle görünebilir:

| Şehir  | Ülke    | Yıl  | Miktar |
| ------ | ------- | ---- | ------ |
| Tokyo  | Japonya | 2020 | 1690   |
| Tokyo  | Japonya | 2019 | 1874   |
| Tokyo  | Japonya | 2018 | 1445   |

Tablomuzda ne fark ettiniz? Şehir adı ve ülke bilgisini tekrar tekrar çoğalttığımızı fark etmiş olabilirsiniz. Bu oldukça fazla depolama alanı kaplayabilir ve birden çok kopyaya sahip olmak büyük ölçüde gereksizdir. Sonuçta, Tokyo'nun ilgilendiğimiz tek bir adı vardır.

Tamam, başka bir şey deneyelim. Her yıl için yeni sütunlar ekleyelim:

| Şehir    | Ülke          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japonya       | 1445 | 1874 | 1690 |
| Atlanta  | Amerika Birleşik Devletleri | 1779 | 1111 | 1683 |
| Auckland | Yeni Zelanda  | 1386 | 942  | 1176 |

Bu, satır çoğaltmayı önlerken birkaç başka zorluk da getirir. Her yeni yıl için tablonun yapısını değiştirmemiz gerekir. Ayrıca, verilerimiz büyüdükçe yılların sütun olarak olması değerleri almak ve hesaplamak için işleri zorlaştırır.

İşte bu yüzden birden çok tabloya ve ilişkilere ihtiyacımız var. Verilerimizi parçalara ayırarak çoğaltmayı önleyebilir ve verilerle çalışma şeklimizde daha fazla esneklik sağlayabiliriz.

## İlişki kavramları

Verilerimize dönelim ve nasıl bölmek istediğimizi belirleyelim. Şehirlerin adı ve ülkesini depolamak istediğimizi biliyoruz, bu yüzden bu muhtemelen en iyi tek bir tabloda olur.

| Şehir    | Ülke          |
| -------- | ------------- |
| Tokyo    | Japonya       |
| Atlanta  | Amerika Birleşik Devletleri |
| Auckland | Yeni Zelanda  |

Ancak bir sonraki tabloyu oluşturmadan önce, her şehri nasıl referans göstereceğimizi bulmamız gerekiyor. Bir tür tanımlayıcıya, kimliğe veya (teknik veritabanı terimleriyle) birincil anahtara ihtiyacımız var. Birincil anahtar, bir tabloda belirli bir satırı tanımlamak için kullanılan bir değerdir. Bu, kendisi bir değere dayanabilir (örneğin şehir adını kullanabiliriz), ancak neredeyse her zaman bir sayı veya başka bir tanımlayıcı olmalıdır. Kimliğin asla değişmemesini isteriz çünkü bu ilişkiyi bozar. Çoğu durumda birincil anahtar veya kimlik otomatik oluşturulan bir sayı olacaktır.

> ✅ Birincil anahtar genellikle PK olarak kısaltılır

### şehirler

| city_id | Şehir    | Ülke          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japonya       |
| 2       | Atlanta  | Amerika Birleşik Devletleri |
| 3       | Auckland | Yeni Zelanda  |

> ✅ Bu derste "id" ve "birincil anahtar" terimlerini birbirinin yerine kullandığımızı fark edeceksiniz. Buradaki kavramlar, daha sonra keşfedeceğiniz DataFrame'ler için geçerlidir. DataFrame'ler "birincil anahtar" terimini kullanmaz, ancak benzer şekilde davranırlar.

Şehirler tablomuzu oluşturduğumuza göre, yağışı depolayalım. Şehir hakkında tam bilgiyi çoğaltmak yerine, id'yi kullanabiliriz. Ayrıca yeni oluşturulan tablonun da bir *id* sütununa sahip olduğundan emin olmalıyız; çünkü tüm tabloların bir id veya birincil anahtarı olmalıdır.

### yağış

| rainfall_id | city_id | Yıl  | Miktar |
| ----------- | ------- | ---- | ------ |
| 1           | 1       | 2018 | 1445   |
| 2           | 1       | 2019 | 1874   |
| 3           | 1       | 2020 | 1690   |
| 4           | 2       | 2018 | 1779   |
| 5           | 2       | 2019 | 1111   |
| 6           | 2       | 2020 | 1683   |
| 7           | 3       | 2018 | 1386   |
| 8           | 3       | 2019 | 942    |
| 9           | 3       | 2020 | 1176   |

Yeni oluşturulan **yağış** tablosundaki **city_id** sütununa dikkat edin. Bu sütun, **şehirler** tablosundaki ID'leri referans eden değerler içerir. Teknik ilişkisel veri terimleriyle, buna **yabancı anahtar** denir; başka bir tablonun birincil anahtarıdır. Bunu sadece bir referans veya işaretçi olarak düşünebilirsiniz. **city_id** 1 Tokyo'yu referans eder.

> [!NOTE] 
> Yabancı anahtar genellikle FK olarak kısaltılır

## Veriyi alma

Verilerimizi iki tabloya ayırdık, şimdi nasıl alacağımızı merak ediyor olabilirsiniz. MySQL, SQL Server veya Oracle gibi ilişkisel bir veritabanı kullanıyorsak, Yapılandırılmış Sorgu Dili veya SQL adlı bir dili kullanabiliriz. SQL (bazen sequel olarak telaffuz edilir) ilişkisel veritabanında veri almak ve değiştirmek için kullanılan standart bir dildir.

Veri almak için `SELECT` komutunu kullanırsınız. Temelde, görmek istediğiniz sütunları **SELECT** ile seçer ve bunların bulunduğu tabloyu **FROM** ile belirtirsiniz. Sadece şehir isimlerini göstermek isteseydiniz, aşağıdakini kullanabilirdiniz:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` sütunları listelediğiniz yerdir, `FROM` ise tabloları listelediğiniz yerdir.

> [!NOTE] 
> SQL sözdizimi büyük/küçük harfe duyarsızdır, yani `select` ve `SELECT` aynı anlama gelir. Ancak, kullandığınız veritabanı türüne bağlı olarak sütunlar ve tablolar büyük/küçük harfe duyarlı olabilir. Bu nedenle, programlamada her şeyi büyük/küçük harfe duyarlı olarak ele almak en iyi uygulamadır. SQL sorguları yazarken yaygın uygulama, anahtar kelimeleri tamamen büyük harflerle yazmaktır.

Yukarıdaki sorgu tüm şehirleri gösterecektir. Diyelim ki sadece Yeni Zelanda'daki şehirleri göstermek istiyoruz. Bir tür filtreye ihtiyacımız var. Bunun için SQL anahtar kelimesi `WHERE`'dır, yani "bir şey doğru olduğunda".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Veriyi birleştirme

Şimdiye kadar veriyi tek bir tablodan aldık. Şimdi hem **şehirler** hem de **yağış** tablolarından veriyi bir araya getirmek istiyoruz. Bu, onları *birleştirerek* yapılır. Etkili bir şekilde iki tablo arasında bir dikiş oluşturur ve her tablodan bir sütundaki değerleri eşleştirirsiniz.

Örneğimizde, **yağış** tablosundaki **city_id** sütununu **şehirler** tablosundaki **city_id** sütunu ile eşleştireceğiz. Bu, yağış değerini ilgili şehirle eşleştirecektir. Yapacağımız birleştirme türü *inner* join olarak adlandırılır; yani diğer tablodan hiçbir şeyle eşleşmeyen satırlar gösterilmez. Bizim durumumuzda her şehrin yağışı var, bu yüzden her şey gösterilecektir.

Tüm şehirler için 2019 yılı yağışını alalım.

Bunu adım adım yapacağız. İlk adım, dikiş için sütunları belirtmekle verileri birleştirmektir - daha önce vurgulandığı gibi **city_id**.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

İstediğimiz iki sütunu ve tabloları **city_id** üzerinden birleştirmek istediğimizi vurguladık. Şimdi sadece 2019 yılını filtrelemek için `WHERE` ifadesini ekleyebiliriz.

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

İlişkisel veritabanları, bilgiyi birden çok tabloya bölmeye ve ardından görüntüleme ve analiz için tekrar bir araya getirmeye odaklanır. Bu, hesaplamalar yapma ve veriyi başka şekillerde manipüle etme konusunda yüksek derecede esneklik sağlar. İlişkisel veritabanının temel kavramlarını ve iki tablo arasında nasıl birleştirme yapılacağını gördünüz.

## 🚀 Meydan Okuma

İnternette birçok ilişkisel veritabanı mevcuttur. Yukarıda öğrendiğiniz becerileri kullanarak verileri keşfedebilirsiniz.

## Ders Sonrası Quiz

## [Ders sonrası quiz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## İnceleme & Kendi Kendine Çalışma

SQL ve ilişkisel veritabanı kavramlarını keşfetmeye devam etmek için [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) üzerinde çeşitli kaynaklar mevcuttur

- [İlişkisel veri kavramlarını tanımla](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Transact-SQL ile Sorgulamaya Başlayın](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL, SQL'nin bir versiyonudur)
- [Microsoft Learn'de SQL içeriği](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Ödev

[Havalimanı verilerini görüntüleme](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->