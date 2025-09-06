<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c182e87f9f80be7e7cdffc7b40bbfccf",
  "translation_date": "2025-09-06T08:56:01+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "tr"
}
-->
# Verilerle Çalışmak: İlişkisel Olmayan Veriler

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|NoSQL Verilerle Çalışmak - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ds/quiz/10)

Veriler yalnızca ilişkisel veritabanlarıyla sınırlı değildir. Bu ders, ilişkisel olmayan verilere odaklanacak ve elektronik tablolar ile NoSQL'in temellerini kapsayacaktır.

## Elektronik Tablolar

Elektronik tablolar, kurulumu ve kullanıma başlanması daha az çaba gerektirdiği için verileri saklamak ve keşfetmek için popüler bir yöntemdir. Bu derste bir elektronik tablonun temel bileşenlerini, formülleri ve işlevleri öğreneceksiniz. Örnekler Microsoft Excel ile gösterilecektir, ancak diğer elektronik tablo yazılımlarıyla karşılaştırıldığında çoğu bölüm ve konu benzer adlara ve adımlara sahip olacaktır.

![İki çalışma sayfası içeren boş bir Microsoft Excel çalışma kitabı](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

Bir elektronik tablo bir dosyadır ve bir bilgisayarın, cihazın veya bulut tabanlı bir dosya sisteminin dosya sisteminde erişilebilir olacaktır. Yazılımın kendisi tarayıcı tabanlı olabilir veya bir bilgisayara yüklenmesi gereken bir uygulama ya da bir uygulama olarak indirilebilir. Excel'de bu dosyalar **çalışma kitapları** olarak tanımlanır ve bu terim dersin geri kalanında kullanılacaktır.

Bir çalışma kitabı, bir veya daha fazla **çalışma sayfası** içerir ve her çalışma sayfası sekmelerle etiketlenir. Bir çalışma sayfasında, gerçek verilerin bulunduğu **hücreler** adı verilen dikdörtgenler bulunur. Bir hücre, bir satır ve sütunun kesişimidir; sütunlar alfabetik karakterlerle, satırlar ise sayısal olarak etiketlenir. Bazı elektronik tablolarda, hücredeki verileri açıklamak için ilk birkaç satırda başlıklar bulunabilir.

Excel çalışma kitabının bu temel unsurlarıyla, bir envantere odaklanan [Microsoft Şablonları](https://templates.office.com/) örneğinden yararlanarak bir elektronik tablonun bazı ek bölümlerini inceleyeceğiz.

### Envanter Yönetimi

"InventoryExample" adlı elektronik tablo dosyası, bir envanterdeki öğelerin biçimlendirilmiş bir elektronik tablosudur ve "Inventory List", "Inventory Pick List" ve "Bin Lookup" olarak etiketlenmiş üç çalışma sayfası içerir. Inventory List çalışma sayfasının 4. satırı, başlık sütunundaki her hücrenin değerini açıklayan başlıktır.

![Microsoft Excel'deki bir envanter listesinden bir formülün vurgulanmış hali](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

Bazı durumlarda, bir hücre, değerini oluşturmak için diğer hücrelerin değerlerine bağlıdır. Inventory List elektronik tablosu, envanterindeki her öğenin maliyetini takip eder, ancak envanterdeki her şeyin toplam değerini bilmemiz gerekirse ne yaparız? [**Formüller**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263), hücre verileri üzerinde işlem yapar ve bu örnekte envanterin maliyetini hesaplamak için kullanılır. Bu elektronik tablo, Inventory Value sütununda, QTY başlığı altındaki miktarı ve COST başlığı altındaki maliyetleri çarparak her öğenin değerini hesaplayan bir formül kullanmıştır. Bir hücreye çift tıklamak veya hücreyi vurgulamak formülü gösterir. Formüllerin bir eşittir işaretiyle başladığını ve ardından hesaplama veya işlemin geldiğini fark edeceksiniz.

![Microsoft Excel'deki bir envanter listesinden bir işlevin vurgulanmış hali](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

Envanter Değeri'nin tüm değerlerini toplamak için başka bir formül kullanabiliriz. Bu, her hücreyi toplayarak hesaplanabilir, ancak bu zahmetli bir iş olabilir. Excel, hücre değerleri üzerinde hesaplamalar yapmak için önceden tanımlanmış formüller olan [**işlevler**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89) içerir. İşlevler, bu hesaplamaları yapmak için gerekli olan argümanlara ihtiyaç duyar. Bir işlev birden fazla argüman gerektiriyorsa, bunların belirli bir sırayla listelenmesi gerekir, aksi takdirde işlev doğru değeri hesaplamayabilir. Bu örnek, SUM işlevini kullanır ve toplamı oluşturmak için Inventory Value değerlerini argüman olarak kullanır; bu toplam, 3. satır, B sütununda (B3 olarak da adlandırılır) listelenmiştir.

## NoSQL

NoSQL, ilişkisel olmayan verileri saklamanın farklı yollarını kapsayan bir şemsiye terimdir ve "non-SQL", "ilişkisel olmayan" veya "sadece SQL değil" olarak yorumlanabilir. Bu tür veritabanı sistemleri 4 türe ayrılabilir.

![4 benzersiz sayısal anahtarın çeşitli değerlerle eşleştirildiği bir anahtar-değer veri deposunun grafiksel temsili](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> Kaynak: [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[Anahtar-değer](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) veritabanları, benzersiz bir anahtar ile bir değerin eşleştirildiği benzersiz anahtarlar oluşturur. Bu eşleştirmeler, uygun bir karma işlevi kullanan bir [karma tablosu](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) kullanılarak saklanır.

![Kişiler, ilgi alanları ve konumlar arasındaki ilişkileri gösteren bir grafik veri deposunun grafiksel temsili](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> Kaynak: [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[Grafik](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) veritabanları, verilerdeki ilişkileri tanımlar ve düğümler ve kenarlardan oluşan bir koleksiyon olarak temsil edilir. Bir düğüm, gerçek dünyada var olan bir varlığı, örneğin bir öğrenciyi veya banka ekstresini temsil eder. Kenarlar, iki varlık arasındaki ilişkiyi temsil eder. Her düğüm ve kenar, her bir düğüm ve kenar hakkında ek bilgi sağlayan özelliklere sahiptir.

![Kimlik ve İletişim Bilgileri adlı iki sütun ailesine sahip bir müşteri veritabanını gösteren bir sütunlu veri deposunun grafiksel temsili](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

[Sütunlu](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) veri depoları, verileri sütunlar ve satırlar halinde düzenler, ancak her sütun, bir sütun ailesi adı verilen gruplara ayrılır. Bir sütun altındaki tüm veriler ilişkilidir ve bir birim olarak alınabilir ve değiştirilebilir.

### Azure Cosmos DB ile Belge Veri Depoları

[Belge](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) veri depoları, bir anahtar-değer veri deposu kavramını temel alır ve bir dizi alan ve nesneden oluşur. Bu bölümde, Cosmos DB emülatörü ile belge veritabanlarını keşfedeceğiz.

Bir Cosmos DB veritabanı, "Sadece SQL Değil" tanımına uyar; Cosmos DB'nin belge veritabanı, verileri sorgulamak için SQL'e dayanır. SQL'in temellerini kapsayan [önceki ders](../05-relational-databases/README.md), burada bir belge veritabanına bazı aynı sorguları uygulamamıza olanak tanır. Cosmos DB Emülatörü'nü kullanacağız; bu, bir bilgisayarda yerel olarak bir belge veritabanı oluşturup keşfetmemizi sağlar. Emülatör hakkında daha fazla bilgi için [burayı okuyun](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

Bir belge, alanlar ve nesne değerlerinden oluşan bir koleksiyondur; alanlar, nesne değerinin neyi temsil ettiğini açıklar. Aşağıda bir belge örneği verilmiştir.

```json
{
    "firstname": "Eva",
    "age": 44,
    "id": "8c74a315-aebf-4a16-bb38-2430a9896ce5",
    "_rid": "bHwDAPQz8s0BAAAAAAAAAA==",
    "_self": "dbs/bHwDAA==/colls/bHwDAPQz8s0=/docs/bHwDAPQz8s0BAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f95-010a691e01d7\"",
    "_attachments": "attachments/",
    "_ts": 1630544034
}
```

Bu belgedeki ilgi çekici alanlar: `firstname`, `id` ve `age`. Cosmos DB tarafından oluşturulan alt çizgili diğer alanlar dikkate alınmamıştır.

#### Cosmos DB Emülatörü ile Verileri Keşfetme

Emülatörü [Windows için buradan](https://aka.ms/cosmosdb-emulator) indirip yükleyebilirsiniz. macOS ve Linux için emülatörü çalıştırma seçenekleri için bu [belgeye](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos) başvurun.

Emülatör, belgeleri keşfetmenizi sağlayan Explorer görünümünü başlatan bir tarayıcı penceresi açar.

![Cosmos DB Emülatörü'nün Explorer görünümü](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

Eğer takip ediyorsanız, "Start with Sample" seçeneğine tıklayarak SampleDB adlı bir örnek veritabanı oluşturabilirsiniz. SampleDB'yi genişletmek için oka tıkladığınızda, `Persons` adlı bir konteyner bulacaksınız; bir konteyner, içindeki belgeler olan bir öğe koleksiyonunu tutar. `Items` altındaki dört bireysel belgeyi keşfedebilirsiniz.

![Cosmos DB Emülatörü'nde örnek verileri keşfetme](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Cosmos DB Emülatörü ile Belge Verilerini Sorgulama

Yeni SQL Sorgusu düğmesine (soldan ikinci düğme) tıklayarak örnek verileri sorgulayabilirsiniz.

`SELECT * FROM c` konteynerdeki tüm belgeleri döndürür. Bir where cümlesi ekleyelim ve yaşı 40'tan küçük olan herkesi bulalım.

`SELECT * FROM c where c.age < 40`

![Cosmos DB Emülatörü'nde örnek veriler üzerinde bir SELECT sorgusu çalıştırma](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

Sorgu iki belge döndürür; her belgenin yaş değerinin 40'tan küçük olduğunu fark edin.

#### JSON ve Belgeler

Eğer JavaScript Object Notation (JSON) ile aşinaysanız, belgelerin JSON'a benzediğini fark edeceksiniz. Bu dizinde, Emülatör'deki Persons konteynerine `Upload Item` düğmesiyle yükleyebileceğiniz daha fazla veri içeren bir `PersonsData.json` dosyası bulunmaktadır.

Çoğu durumda, JSON verisi döndüren API'ler doğrudan belge veritabanlarına aktarılabilir ve saklanabilir. Aşağıda başka bir belge örneği verilmiştir; bu belge, Twitter API kullanılarak alınan ve ardından Cosmos DB'ye eklenen Microsoft Twitter hesabından tweetleri temsil eder.

```json
{
    "created_at": "2021-08-31T19:03:01.000Z",
    "id": "1432780985872142341",
    "text": "Blank slate. Like this tweet if you’ve ever painted in Microsoft Paint before. https://t.co/cFeEs8eOPK",
    "_rid": "dhAmAIUsA4oHAAAAAAAAAA==",
    "_self": "dbs/dhAmAA==/colls/dhAmAIUsA4o=/docs/dhAmAIUsA4oHAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f84-a0958ad901d7\"",
    "_attachments": "attachments/",
    "_ts": 1630537000
```

Bu belgedeki ilgi çekici alanlar: `created_at`, `id` ve `text`.

## 🚀 Zorluk

Bir `TwitterData.json` dosyası, SampleDB veritabanına yüklenebilir. Bunun ayrı bir konteynere eklenmesi önerilir. Bu şu şekilde yapılabilir:

1. Sağ üstteki yeni konteyner düğmesine tıklayın
1. Mevcut veritabanını (SampleDB) seçin, konteyner için bir kimlik oluşturun
1. Bölüm anahtarını `/id` olarak ayarlayın
1. Tamam'a tıklayın (bu görünümdeki diğer bilgileri yok sayabilirsiniz, çünkü bu küçük bir veri kümesi yerel olarak makinenizde çalışıyor)
1. Yeni konteynerinizi açın ve `Upload Item` düğmesiyle Twitter Data dosyasını yükleyin

Metin alanında Microsoft bulunan belgeleri bulmak için birkaç SELECT sorgusu çalıştırmayı deneyin. İpucu: [LIKE anahtar kelimesini](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character) kullanmayı deneyin.

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ds/quiz/11)

## Gözden Geçirme ve Kendi Kendine Çalışma

- Bu derste ele alınmayan elektronik tabloya eklenen bazı ek biçimlendirme ve özellikler vardır. Microsoft'un Excel hakkında daha fazla bilgi edinmek isterseniz [geniş bir dokümantasyon ve video kütüphanesi](https://support.microsoft.com/excel) bulunmaktadır.

- Bu mimari dokümantasyon, farklı türdeki ilişkisel olmayan verilerin özelliklerini detaylandırır: [İlişkisel Olmayan Veriler ve NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)

- Cosmos DB, bu derste bahsedilen farklı NoSQL türlerini de saklayabilen bulut tabanlı bir ilişkisel olmayan veritabanıdır. Bu türler hakkında daha fazla bilgi edinmek için bu [Cosmos DB Microsoft Learn Modülüne](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/) göz atın.

## Ödev

[Soda Profits](assignment.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.