<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-06T08:54:58+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "tr"
}
-->
# Bulutta Veri Bilimine Giriş

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Bulutta Veri Bilimine Giriş - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Bu derste, Bulutun temel prensiplerini öğreneceksiniz, ardından veri bilimi projelerinizi yürütmek için Bulut hizmetlerini kullanmanın neden ilginç olabileceğini göreceksiniz ve Bulutta yürütülen bazı veri bilimi projelerine örnekler inceleyeceğiz.

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Bulut Nedir?

Bulut veya Bulut Bilişim, internet üzerinden barındırılan bir altyapı üzerinde geniş bir yelpazede "kullandıkça öde" esasına dayalı bilişim hizmetlerinin sunulmasıdır. Hizmetler arasında depolama, veritabanları, ağ oluşturma, yazılım, analiz ve akıllı hizmetler gibi çözümler bulunur.

Genellikle Kamu, Özel ve Hibrit bulutları şu şekilde ayırırız:

* Kamu bulutu: Kamu bulutu, üçüncü taraf bir bulut hizmeti sağlayıcısı tarafından sahip olunan ve işletilen, bilişim kaynaklarını internet üzerinden halka sunan bir buluttur.
* Özel bulut: Özel bulut, yalnızca bir işletme veya organizasyon tarafından kullanılan bulut bilişim kaynaklarını ifade eder. Hizmetler ve altyapı özel bir ağ üzerinde yönetilir.
* Hibrit bulut: Hibrit bulut, kamu ve özel bulutları birleştiren bir sistemdir. Kullanıcılar, bir yerinde veri merkezi seçerken, veri ve uygulamaların bir veya daha fazla kamu bulutunda çalışmasına izin verir.

Çoğu bulut bilişim hizmeti üç kategoriye ayrılır: Hizmet Olarak Altyapı (IaaS), Hizmet Olarak Platform (PaaS) ve Hizmet Olarak Yazılım (SaaS).

* Hizmet Olarak Altyapı (IaaS): Kullanıcılar sunucular, sanal makineler (VM'ler), depolama, ağlar, işletim sistemleri gibi bir BT altyapısını kiralar.
* Hizmet Olarak Platform (PaaS): Kullanıcılar yazılım uygulamaları geliştirmek, test etmek, sunmak ve yönetmek için bir ortam kiralar. Kullanıcılar, geliştirme için gereken sunucular, depolama, ağ ve veritabanlarının altyapısını kurmak veya yönetmek zorunda kalmaz.
* Hizmet Olarak Yazılım (SaaS): Kullanıcılar, internet üzerinden talep üzerine ve genellikle abonelik esasına dayalı olarak yazılım uygulamalarına erişir. Kullanıcılar, yazılım uygulamasını barındırma ve yönetme, altyapıyı veya bakımını (örneğin yazılım güncellemeleri ve güvenlik yamaları) düşünmek zorunda kalmaz.

En büyük Bulut sağlayıcılarından bazıları Amazon Web Services, Google Cloud Platform ve Microsoft Azure'dur.

## Veri Bilimi için Neden Bulutu Seçmelisiniz?

Geliştiriciler ve BT profesyonelleri, Bulut ile çalışmayı aşağıdaki nedenler dahil olmak üzere birçok sebepten dolayı tercih eder:

* Yenilik: Uygulamalarınızı, Bulut sağlayıcıları tarafından oluşturulan yenilikçi hizmetleri doğrudan uygulamalarınıza entegre ederek güçlendirebilirsiniz.
* Esneklik: İhtiyacınız olan hizmetler için ödeme yaparsınız ve geniş bir hizmet yelpazesinden seçim yapabilirsiniz. Genellikle kullandıkça ödersiniz ve hizmetlerinizi değişen ihtiyaçlarınıza göre uyarlarsınız.
* Bütçe: Donanım ve yazılım satın almak, yerinde veri merkezleri kurmak ve işletmek için başlangıç yatırımları yapmanız gerekmez; sadece kullandığınız kadarını ödersiniz.
* Ölçeklenebilirlik: Kaynaklarınız, projenizin ihtiyaçlarına göre ölçeklenebilir, bu da uygulamalarınızın herhangi bir zamanda dış faktörlere uyum sağlayarak daha fazla veya daha az işlem gücü, depolama ve bant genişliği kullanabileceği anlamına gelir.
* Verimlilik: Veri merkezlerini yönetmek gibi başkası tarafından yönetilebilecek görevlerde zaman harcamak yerine işinize odaklanabilirsiniz.
* Güvenilirlik: Bulut Bilişim, verilerinizi sürekli yedeklemek için çeşitli yollar sunar ve kriz zamanlarında bile işinizi ve hizmetlerinizi devam ettirmek için felaket kurtarma planları oluşturabilirsiniz.
* Güvenlik: Projenizin güvenliğini artıran politikalar, teknolojiler ve kontrollerden faydalanabilirsiniz.

Bunlar, insanların Bulut hizmetlerini kullanmayı tercih etmesinin en yaygın nedenlerinden bazılarıdır. Artık Bulutun ne olduğunu ve temel faydalarını daha iyi anladığımıza göre, veri bilimcilerin ve veri ile çalışan geliştiricilerin işlerine daha spesifik olarak bakalım ve Bulutun karşılaşabilecekleri çeşitli zorluklarla nasıl yardımcı olabileceğini görelim:

* Büyük miktarda veri depolama: Büyük sunucular satın almak, yönetmek ve korumak yerine, verilerinizi doğrudan Bulutta depolayabilirsiniz. Örneğin Azure Cosmos DB, Azure SQL Database ve Azure Data Lake Storage gibi çözümlerle.
* Veri Entegrasyonu Yapma: Veri entegrasyonu, veri toplama aşamasından eyleme geçme aşamasına geçiş yapmanızı sağlayan veri biliminin önemli bir parçasıdır. Bulutta sunulan veri entegrasyon hizmetleri ile çeşitli kaynaklardan gelen verileri tek bir veri ambarında toplayabilir, dönüştürebilir ve entegre edebilirsiniz. Örneğin Data Factory ile.
* Veri işleme: Büyük miktarda veri işlemek çok fazla işlem gücü gerektirir ve herkesin bu kadar güçlü makineler erişimi olmayabilir. Bu nedenle birçok kişi, çözümlerini çalıştırmak ve dağıtmak için doğrudan Bulutun büyük işlem gücünden yararlanmayı tercih eder.
* Veri analitiği hizmetlerini kullanma: Azure Synapse Analytics, Azure Stream Analytics ve Azure Databricks gibi bulut hizmetleri, verilerinizi eyleme dönüştürülebilir içgörülere dönüştürmenize yardımcı olur.
* Makine Öğrenimi ve veri zekası hizmetlerini kullanma: Sıfırdan başlamak yerine, bulut sağlayıcısı tarafından sunulan makine öğrenimi algoritmalarını kullanabilirsiniz. Örneğin AzureML gibi hizmetlerle. Ayrıca konuşmadan metne, metinden konuşmaya, bilgisayar görüşü ve daha fazlası gibi bilişsel hizmetleri kullanabilirsiniz.

## Bulutta Veri Bilimi Örnekleri

Bu konuyu daha somut hale getirmek için birkaç senaryoya bakalım.

### Gerçek Zamanlı Sosyal Medya Duygu Analizi
Makine öğrenimine yeni başlayanların sıklıkla çalıştığı bir senaryodan başlayalım: gerçek zamanlı sosyal medya duygu analizi.

Diyelim ki bir haber medya web sitesi işletiyorsunuz ve okuyucularınızın ilgilenebileceği içerikleri anlamak için canlı verilerden yararlanmak istiyorsunuz. Bunun hakkında daha fazla bilgi edinmek için, okuyucularınızla ilgili konular hakkında Twitter yayınlarından gerçek zamanlı duygu analizi yapan bir program oluşturabilirsiniz.

Bakacağınız temel göstergeler, belirli konular (hashtagler) hakkındaki tweetlerin hacmi ve belirtilen konular etrafında duygu analizi yapan analitik araçlarla belirlenen duygudur.

Bu projeyi oluşturmak için gerekli adımlar şunlardır:

* Twitter'dan veri toplayacak bir giriş akışı için bir olay merkezi oluşturun.
* Twitter Streaming API'lerini çağıracak bir Twitter istemci uygulaması yapılandırın ve başlatın.
* Bir Stream Analytics işi oluşturun.
* İş girişini ve sorgusunu belirtin.
* Bir çıktı havuzu oluşturun ve iş çıktısını belirtin.
* İşi başlatın.

Tam süreci görmek için [belgelere](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099) göz atın.

### Bilimsel Makalelerin Analizi
Bu müfredatın yazarlarından biri olan [Dmitry Soshnikov](http://soshnikov.com) tarafından oluşturulan bir projeye bakalım.

Dmitry, COVID makalelerini analiz eden bir araç oluşturdu. Bu projeyi inceleyerek, bilimsel makalelerden bilgi çıkaran, içgörüler elde eden ve araştırmacıların büyük makale koleksiyonlarında verimli bir şekilde gezinmesine yardımcı olan bir araç nasıl oluşturabileceğinizi göreceksiniz.

Kullanılan farklı adımlara bakalım:
* [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ile bilgiyi çıkarma ve ön işleme.
* İşlemeyi paralelleştirmek için [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) kullanma.
* Bilgiyi depolama ve sorgulama için [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) kullanma.
* Power BI kullanarak veri keşfi ve görselleştirme için etkileşimli bir kontrol paneli oluşturma.

Tam süreci görmek için [Dmitry’nin blogunu](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) ziyaret edin.

Gördüğünüz gibi, Bulut hizmetlerini birçok farklı şekilde kullanarak Veri Bilimi gerçekleştirebiliriz.

## Dipnot

Kaynaklar:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Ders Sonrası Test

## [Ders sonrası test](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Ödev

[Pazar Araştırması](assignment.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.