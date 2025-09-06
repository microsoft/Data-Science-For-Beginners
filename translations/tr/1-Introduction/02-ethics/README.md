<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1341f6da63d434f5ba31b08ea951b02c",
  "translation_date": "2025-09-06T09:06:31+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "tr"
}
-->
# Veri Etiğine Giriş

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Veri Bilimi Etiği - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

---

Hepimiz veriyle dolu bir dünyada yaşayan veri vatandaşlarıyız.

Pazar trendleri, 2022 yılı itibarıyla büyük organizasyonların üçte birinin verilerini çevrimiçi [Pazar Yerleri ve Borsalar](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) aracılığıyla alıp satacağını gösteriyor. **Uygulama Geliştiricileri** olarak, veri odaklı içgörüleri ve algoritma tabanlı otomasyonu günlük kullanıcı deneyimlerine entegre etmenin daha kolay ve ucuz hale geldiğini göreceğiz. Ancak yapay zeka yaygınlaştıkça, bu tür algoritmaların [silah haline getirilmesi](https://www.youtube.com/watch?v=TQHs8SA1qpk) durumunda ortaya çıkabilecek potansiyel zararları da anlamamız gerekecek.

Trendler ayrıca 2025 yılına kadar [180 zettabayt](https://www.statista.com/statistics/871513/worldwide-data-created/) veri oluşturup tüketeceğimizi gösteriyor. **Veri Bilimcileri** olarak, bu durum bize kişisel verilere benzeri görülmemiş bir erişim seviyesi sağlıyor. Bu, kullanıcıların davranış profillerini oluşturabileceğimiz ve karar alma süreçlerini, kullanıcıları tercih ettiğimiz sonuçlara yönlendirebilecek şekilde etkileyebileceğimiz anlamına geliyor. Aynı zamanda veri gizliliği ve kullanıcı korumaları gibi daha geniş soruları da gündeme getiriyor.

Veri etiği, veri bilimi ve mühendisliği için artık _gerekli koruma önlemleri_ haline geldi ve veri odaklı eylemlerimizden kaynaklanabilecek potansiyel zararları ve istenmeyen sonuçları en aza indirmemize yardımcı oluyor. [Gartner'ın Yapay Zeka Hype Döngüsü](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) dijital etik, sorumlu yapay zeka ve yapay zeka yönetimi gibi ilgili trendleri, yapay zekanın _demokratikleşmesi_ ve _endüstrileşmesi_ etrafındaki daha büyük megatrendlerin anahtar itici güçleri olarak tanımlıyor.

![Gartner'ın Yapay Zeka Hype Döngüsü - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Bu derste, veri etiği alanını keşfedeceğiz - temel kavramlardan ve zorluklardan, vaka çalışmalarına ve yönetişim gibi uygulamalı yapay zeka kavramlarına kadar - veri ve yapay zeka ile çalışan ekiplerde ve organizasyonlarda bir etik kültürü oluşturulmasına yardımcı olan konuları ele alacağız.

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Temel Tanımlar

Öncelikle temel terminolojiyi anlamakla başlayalım.

"Etik" kelimesi, [Yunanca "ethikos"](https://en.wikipedia.org/wiki/Ethics) (ve kökü "ethos") kelimesinden gelir ve _karakter veya ahlaki doğa_ anlamına gelir.

**Etik**, toplumdaki davranışlarımızı yöneten ortak değerler ve ahlaki ilkelerdir. Etik, yasalara değil, "doğru ile yanlış" arasındaki yaygın olarak kabul edilen normlara dayanır. Ancak etik düşünceler, kurumsal yönetim girişimlerini ve uyum için daha fazla teşvik yaratan hükümet düzenlemelerini etkileyebilir.

**Veri Etiği**, "_veri, algoritmalar ve ilgili uygulamalarla_ ilgili ahlaki sorunları inceleyen ve değerlendiren" [yeni bir etik dalıdır](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1). Burada, **"veri"** oluşturma, kaydetme, kürasyon, işleme, yayma, paylaşma ve kullanım ile ilgili eylemlere odaklanır, **"algoritmalar"** yapay zeka, ajanlar, makine öğrenimi ve robotlara odaklanır ve **"uygulamalar"** sorumlu yenilik, programlama, hackleme ve etik kodlar gibi konulara odaklanır.

**Uygulamalı Etik**, [ahlaki düşüncelerin pratik uygulamasıdır](https://en.wikipedia.org/wiki/Applied_ethics). Bu, _gerçek dünya eylemleri, ürünleri ve süreçleri_ bağlamında etik sorunları aktif olarak araştırma ve bunların tanımlı etik değerlerimizle uyumlu kalmasını sağlamak için düzeltici önlemler alma sürecidir.

**Etik Kültürü**, [_uygulamalı etiği_ operasyonelleştirmek](https://hbr.org/2019/05/how-to-design-an-ethical-organization) ile ilgilidir; etik ilkelerimizin ve uygulamalarımızın tüm organizasyon genelinde tutarlı ve ölçeklenebilir bir şekilde benimsenmesini sağlamak. Başarılı etik kültürleri, organizasyon genelinde etik ilkeler tanımlar, uyum için anlamlı teşvikler sağlar ve istenen davranışları her seviyede teşvik ederek ve güçlendirerek etik normları pekiştirir.

## Etik Kavramları

Bu bölümde, veri etiği için **ortak değerler** (ilkeler) ve **etik zorluklar** (sorunlar) gibi kavramları tartışacağız - ve bu kavramları gerçek dünya bağlamlarında anlamanıza yardımcı olacak **vaka çalışmaları** inceleyeceğiz.

### 1. Etik İlkeleri

Her veri etiği stratejisi, _etik ilkeler_ tanımlayarak başlar - veri ve yapay zeka projelerimizde kabul edilebilir davranışları tanımlayan ve uyumlu eylemleri yönlendiren "ortak değerler". Bunları bireysel veya ekip düzeyinde tanımlayabilirsiniz. Ancak, çoğu büyük organizasyon bunları kurumsal düzeyde tanımlanan ve tüm ekiplerde tutarlı bir şekilde uygulanan bir _etik yapay zeka_ misyon bildirimi veya çerçevesinde belirtir.

**Örnek:** Microsoft'un [Sorumlu Yapay Zeka](https://www.microsoft.com/en-us/ai/responsible-ai) misyon bildirimi şu şekilde ifade edilir: _"İnsanları ön planda tutan etik ilkelerle yönlendirilen yapay zekanın ilerlemesine bağlıyız"_ - aşağıdaki çerçevede 6 etik ilkeyi tanımlıyor:

![Microsoft'ta Sorumlu Yapay Zeka](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Bu ilkeleri kısaca inceleyelim. _Şeffaflık_ ve _hesap verebilirlik_ diğer ilkelerin üzerine inşa edildiği temel değerlerdir - bu yüzden buradan başlayalım:

* [**Hesap Verebilirlik**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6), uygulayıcıları veri ve yapay zeka operasyonlarından ve bu etik ilkelere uyumdan _sorumlu_ kılar.
* [**Şeffaflık**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6), veri ve yapay zeka eylemlerinin kullanıcılar için _anlaşılır_ (yorumlanabilir) olmasını sağlar, kararların arkasındaki ne ve nedenleri açıklar.
* [**Adalet**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6), yapay zekanın _tüm insanlara_ adil davranmasını sağlamaya odaklanır, veri ve sistemlerdeki sistemik veya örtük sosyo-teknik önyargıları ele alır.
* [**Güvenilirlik ve Güvenlik**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6), yapay zekanın tanımlı değerlere _tutarlı_ bir şekilde davranmasını sağlar, potansiyel zararları veya istenmeyen sonuçları en aza indirir.
* [**Gizlilik ve Güvenlik**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6), veri kökenini anlamak ve kullanıcılara _veri gizliliği ve ilgili korumalar_ sağlamakla ilgilidir.
* [**Kapsayıcılık**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6), yapay zeka çözümlerini niyetle tasarlamak, onları _geniş bir insan ihtiyaçları ve yetenekleri yelpazesine_ uyarlamakla ilgilidir.

> 🚨 Veri etiği misyon bildiriminizin ne olabileceğini düşünün. Diğer organizasyonların etik yapay zeka çerçevelerini keşfedin - işte [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) ve [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/) örnekleri. Ortak değerleri nelerdir? Bu ilkeler, çalıştıkları yapay zeka ürünü veya endüstrisiyle nasıl ilişkilidir?

### 2. Etik Zorluklar

Etik ilkeleri tanımladıktan sonra, bir sonraki adım veri ve yapay zeka eylemlerimizi bu ortak değerlerle uyumlu olup olmadığını değerlendirmektir. Eylemlerinizi iki kategoriye ayırmayı düşünün: _veri toplama_ ve _algoritma tasarımı_.

Veri toplama ile ilgili eylemler, büyük olasılıkla **kişisel veri** veya tanımlanabilir yaşayan bireyler için kişisel olarak tanımlanabilir bilgiler (PII) içerecektir. Bu, bir bireyi _toplu olarak_ tanımlayan [çeşitli kişisel olmayan veri öğelerini](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) içerir. Etik zorluklar, _veri gizliliği_, _veri sahipliği_ ve kullanıcılar için _bilgilendirilmiş onay_ ve _fikri mülkiyet hakları_ gibi ilgili konularla ilgili olabilir.

Algoritma tasarımı ile ilgili eylemler, **veri setleri** toplama ve kürasyon yapmayı, ardından bunları gerçek dünya bağlamlarında sonuçları tahmin eden veya kararları otomatikleştiren **veri modelleri** eğitmek ve dağıtmak için kullanmayı içerecektir. Etik zorluklar, _veri seti önyargısı_, _veri kalitesi_ sorunları, _adaletsizlik_ ve algoritmalardaki _yanlış temsil_ gibi konulardan kaynaklanabilir - bunlar arasında bazıları sistemik olabilir.

Her iki durumda da, etik zorluklar eylemlerimizin ortak değerlerimizle çatışabileceği alanları vurgular. Bu endişeleri tespit etmek, hafifletmek, en aza indirmek veya ortadan kaldırmak için, eylemlerimizle ilgili ahlaki "evet/hayır" soruları sormamız ve gerektiğinde düzeltici önlemler almamız gerekir. Şimdi bazı etik zorluklara ve bunların ortaya çıkardığı ahlaki sorulara bakalım:

#### 2.1 Veri Sahipliği

Veri toplama genellikle veri konularını tanımlayabilecek kişisel verileri içerir. [Veri sahipliği](https://permission.io/blog/data-ownership), verilerin oluşturulması, işlenmesi ve yayılması ile ilgili _kontrol_ ve [_kullanıcı hakları_](https://permission.io/blog/data-ownership) ile ilgilidir.

Sormamız gereken ahlaki sorular şunlardır:
 * Verinin sahibi kimdir? (kullanıcı mı yoksa organizasyon mu?)
 * Veri konularının hangi hakları vardır? (örneğin: erişim, silme, taşınabilirlik)
 * Organizasyonların hangi hakları vardır? (örneğin: kötü niyetli kullanıcı yorumlarını düzeltme)

#### 2.2 Bilgilendirilmiş Onay

[Bilgilendirilmiş onay](https://legaldictionary.net/informed-consent/), kullanıcıların (veri toplama gibi) bir eylemi, amacını, potansiyel risklerini ve alternatiflerini _tam olarak anlayarak_ kabul etmesi eylemini tanımlar.

Burada keşfedilecek sorular şunlardır:
 * Kullanıcı (veri konusu) veri yakalama ve kullanımı için izin verdi mi?
 * Kullanıcı, verinin yakalandığı amacı anladı mı?
 * Kullanıcı, katılımından kaynaklanabilecek potansiyel riskleri anladı mı?

#### 2.3 Fikri Mülkiyet

[Fikri mülkiyet](https://en.wikipedia.org/wiki/Intellectual_property), insan girişiminden kaynaklanan, bireyler veya işletmeler için _ekonomik değeri_ olabilecek soyut yaratımları ifade eder.

Burada keşfedilecek sorular şunlardır:
 * Toplanan veriler bir kullanıcı veya işletme için ekonomik değere sahip miydi?
 * Burada **kullanıcının** fikri mülkiyeti var mı?
 * Burada **organizasyonun** fikri mülkiyeti var mı?
 * Bu haklar varsa, onları nasıl koruyoruz?

#### 2.4 Veri Gizliliği

[Veri gizliliği](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) veya bilgi gizliliği, kullanıcı gizliliğinin korunması ve kullanıcı kimliğinin kişisel olarak tanımlanabilir bilgilerle ilgili olarak korunması anlamına gelir.

Burada keşfedilecek sorular şunlardır:
 * Kullanıcıların (kişisel) verileri hacklere ve sızıntılara karşı güvenli mi?
 * Kullanıcıların verileri yalnızca yetkili kullanıcılar ve bağlamlar için erişilebilir mi?
 * Kullanıcıların anonimliği veri paylaşıldığında veya yayıldığında korunuyor mu?
 * Kullanıcı anonimleştirilmiş veri setlerinden kimliksizleştirilebilir mi?

#### 2.5 Unutulma Hakkı

[Unutulma Hakkı](https://en.wikipedia.org/wiki/Right_to_be_forgotten) veya [Silme Hakkı](https://www.gdpreu.org/right-to-be-forgotten/), kullanıcılara ek kişisel veri koruması sağlar. Özellikle, kullanıcılara İnternet aramalarından ve diğer konumlardan kişisel verilerin silinmesini veya kaldırılmasını talep etme hakkı verir, _belirli koşullar altında_ - geçmiş eylemlerin kendilerine karşı kullanılmaması için çevrimiçi olarak yeni bir başlangıç yapmalarına olanak tanır.

Burada keşfedilecek sorular şunlardır:
 * Sistem, veri konularının silme talebinde bulunmasına izin veriyor mu?
 * Kullanıcı onayının geri çekilmesi otomatik silmeyi tetiklemeli mi?
 * Veri, kullanıcı onayı olmadan veya yasa dışı yollarla mı toplandı?
 * Veri gizliliği için hükümet düzenlemelerine uyuyor muyuz?

#### 2.6 Veri Seti Önyargısı

Veri seti veya [Toplama Önyargısı](http://researcharticles.com/index.php/bias-in-data-collection-in-research/), algoritma geliştirme için _temsil edici olmayan_ bir veri alt kümesi seçmekle ilgilidir ve bu durum çeşitli gruplar için sonuçların adaletsiz olmasına neden olabilir. Önyargı türleri arasında seçim veya örnekleme önyargısı, gönüllü önyargısı ve araç önyargısı bulunur.

Burada keşfedilecek sorular şunlardır:
 * Temsil edici bir veri konusu seti mi topladık?
 * Toplanan veya küratörlüğü yapılan veri setimizi çeşitli önyargılar açısından test ettik mi?
 * Keşfedilen önyargıları hafifletebilir veya ortadan kaldırabilir miyiz?

#### 2.7 Veri Kalitesi

[Veri Kalitesi](https://lakefs.io/data-quality-testing/), algoritmalarımızı geliştirmek için kullanılan küratörlüğü yapılmış veri setinin geçerliliğini inceler ve özelliklerin ve kayıtların yapay zeka amacımız için gereken doğruluk ve tutarlılık düzeyini karşılayıp karşılamadığını kontrol eder.

Burada keşfedilecek sorular şunlardır:
 * Kullanım durumumuz için geçerli _özellikleri_ yakaladık mı?
 * Çeşitli veri kaynakları arasında veri _tutarlı_ bir şekilde mi yakalandı?
 * Veri seti çeşitli koşullar veya senaryolar için _tam_ mı?
 * Bilgiler gerçekliği yansıtacak şekilde _doğru_ bir şekilde mi yakalandı?

#### 2.8 Algoritma Adaleti
[Algorithm Adaleti](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f), algoritma tasarımının belirli veri gruplarına sistematik olarak ayrımcılık yapıp yapmadığını ve bunun sonucunda _kaynak tahsisi_ (kaynakların o gruptan esirgenmesi veya reddedilmesi) ve _hizmet kalitesi_ (AI'nin bazı gruplar için diğerlerine göre daha az doğru olması) gibi [potansiyel zararlar](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) oluşturup oluşturmadığını kontrol eder.

Burada araştırılması gereken sorular:
 * Model doğruluğunu farklı gruplar ve koşullar için değerlendirdik mi?
 * Sistemi potansiyel zararlar (örneğin, stereotipleme) açısından inceledik mi?
 * Belirlenen zararları azaltmak için verileri revize edebilir veya modelleri yeniden eğitebilir miyiz?

Daha fazla bilgi edinmek için [AI Adalet kontrol listeleri](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) gibi kaynakları keşfedin.

#### 2.9 Yanıltıcı Temsil

[Veri Yanıltıcı Temsili](https://www.sciencedirect.com/topics/computer-science/misrepresentation), dürüstçe raporlanan verilerden elde edilen içgörülerin, istenen bir anlatıyı desteklemek için aldatıcı bir şekilde iletilip iletilmediğini sorgular.

Burada araştırılması gereken sorular:
 * Eksik veya yanlış veri mi raporluyoruz?
 * Verileri yanıltıcı sonuçlar çıkaracak şekilde mi görselleştiriyoruz?
 * Sonuçları manipüle etmek için seçici istatistiksel teknikler mi kullanıyoruz?
 * Farklı bir sonuca yol açabilecek alternatif açıklamalar var mı?

#### 2.10 Özgür Seçim

[Özgür Seçim Yanılsaması](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), sistemin "seçim mimarilerinin" karar verme algoritmalarını kullanarak insanları tercih edilen bir sonuca yönlendirdiği, ancak onlara seçenekler ve kontrol sunduğu izlenimini verdiği durumlarda ortaya çıkar. Bu [karanlık desenler](https://www.darkpatterns.org/) kullanıcılar için sosyal ve ekonomik zararlar yaratabilir. Kullanıcı kararları davranış profillerini etkilediğinden, bu eylemler potansiyel olarak bu zararların etkisini artırabilir veya uzatabilir.

Burada araştırılması gereken sorular:
 * Kullanıcı, o seçimi yapmanın sonuçlarını anladı mı?
 * Kullanıcı, (alternatif) seçeneklerin ve her birinin artıları ve eksilerinin farkında mıydı?
 * Kullanıcı, otomatik veya etkilenmiş bir seçimi daha sonra geri alabilir mi?

### 3. Vaka Çalışmaları

Bu etik zorlukları gerçek dünya bağlamlarında ele almak için, bu tür etik ihlallerin göz ardı edildiğinde bireyler ve toplum üzerindeki potansiyel zararları ve sonuçlarını vurgulayan vaka çalışmalarına bakmak faydalı olur.

İşte birkaç örnek:

| Etik Zorluk | Vaka Çalışması  | 
|--- |--- |
| **Bilgilendirilmiş Onay** | 1972 - [Tuskegee Frengi Çalışması](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Çalışmaya katılan Afrikalı Amerikalı erkeklere ücretsiz tıbbi bakım vaat edildi, ancak araştırmacılar tarafından teşhisleri veya tedavi seçenekleri hakkında bilgilendirilmediler. Birçok katılımcı öldü ve eşleri veya çocukları etkilendi; çalışma 40 yıl sürdü. | 
| **Veri Gizliliği** |  2007 - [Netflix veri ödülü](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) araştırmacılara _50K müşteriden 10M anonimleştirilmiş film derecelendirmesi_ sağladı. Ancak, araştırmacılar anonimleştirilmiş verileri _harici veri setlerindeki_ (örneğin, IMDb yorumları) kişisel olarak tanımlanabilir verilerle ilişkilendirebildi - bazı Netflix abonelerini "de-anonimleştirdi".|
| **Veri Toplama Yanlılığı**  | 2013 - Boston Şehri [Street Bump uygulamasını geliştirdi](https://www.boston.gov/transportation/street-bump), vatandaşların çukurları bildirmesine olanak tanıyarak şehre yol sorunlarını bulmak ve düzeltmek için daha iyi veriler sağladı. Ancak, [düşük gelir gruplarındaki insanların araba ve telefonlara erişimi daha azdı](https://hbr.org/2013/04/the-hidden-biases-in-big-data), bu da onların yol sorunlarını bu uygulamada görünmez hale getirdi. Geliştiriciler, adalet için _eşit erişim ve dijital bölünmeler_ sorunları üzerinde akademisyenlerle çalıştı. |
| **Algoritmik Adalet**  | 2018 - MIT [Gender Shades Çalışması](http://gendershades.org/overview.html), cinsiyet sınıflandırma AI ürünlerinin doğruluğunu değerlendirerek kadınlar ve renkli kişiler için doğrulukta boşluklar olduğunu ortaya çıkardı. Bir [2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) kadınlara erkeklere göre daha az kredi sunmuş gibi göründü. Her ikisi de algoritmik yanlılığın sosyo-ekonomik zararlara yol açtığını gösterdi.|
| **Veri Yanıltıcı Temsili** | 2020 - [Georgia Halk Sağlığı Departmanı COVID-19 grafiklerini yayınladı](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) ve x ekseninde kronolojik olmayan sıralama ile vatandaşları doğrulanmış vakalardaki eğilimler hakkında yanıltmış gibi göründü. Bu, görselleştirme hileleriyle yanıltıcı temsili örnekler. |
| **Özgür Seçim Yanılsaması** | 2020 - Öğrenme uygulaması [ABCmouse, FTC şikayetini çözmek için $10M ödedi](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) ve ebeveynler iptal edemedikleri abonelikler için ödeme yapmaya zorlandı. Bu, kullanıcıların potansiyel olarak zararlı seçimlere yönlendirildiği seçim mimarilerindeki karanlık desenleri gösterir. |
| **Veri Gizliliği ve Kullanıcı Hakları** | 2021 - Facebook [Veri İhlali](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) 530M kullanıcının verilerini ifşa etti ve FTC'ye $5B ödeme yaptı. Ancak, kullanıcıları ihlal hakkında bilgilendirmeyi reddetti ve veri şeffaflığı ve erişimi konusundaki kullanıcı haklarını ihlal etti. |

Daha fazla vaka çalışması keşfetmek ister misiniz? Bu kaynaklara göz atın:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - çeşitli endüstrilerde etik ikilemler. 
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - önemli vaka çalışmaları inceleniyor.
* [Where things have gone wrong](https://deon.drivendata.org/examples/) - deon kontrol listesi ve örnekler.

> 🚨 Gördüğünüz vaka çalışmalarını düşünün - hayatınızda benzer bir etik zorlukla karşılaştınız mı veya etkilendiniz mi? Bu bölümde tartıştığımız etik zorluklardan birini gösteren en az bir başka vaka çalışması düşünebilir misiniz?

## Uygulamalı Etik

Etik kavramları, zorlukları ve gerçek dünya bağlamlarında vaka çalışmalarını konuştuk. Peki, projelerimizde etik ilkeleri ve uygulamaları nasıl _uygularız_? Ve bu uygulamaları daha iyi yönetim için nasıl _operasyonelleştiririz_? Gerçek dünya çözümlerini keşfedelim:

### 1. Profesyonel Kodlar

Profesyonel Kodlar, organizasyonların üyelerini etik ilkelerini ve misyon beyanlarını desteklemeye "teşvik etmek" için bir seçenek sunar. Kodlar, profesyonel davranış için _ahlaki yönergeler_ olup, çalışanların veya üyelerin organizasyonlarının ilkelerine uygun kararlar almasına yardımcı olur. Ancak, üyelerin gönüllü uyumu kadar iyidirler; birçok organizasyon, üyelerin uyumunu motive etmek için ek ödüller ve cezalar sunar.

Örnekler:
 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Etik Kodu
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Davranış Kuralları (2013'te oluşturuldu)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (1993'ten beri)

> 🚨 Profesyonel bir mühendislik veya veri bilimi organizasyonuna üye misiniz? Sitelerini inceleyerek profesyonel bir etik kodu tanımlayıp tanımlamadıklarını görün. Bu, etik ilkeleri hakkında ne söylüyor? Üyeleri kodu takip etmeye nasıl "teşvik ediyorlar"?

### 2. Etik Kontrol Listeleri

Profesyonel kodlar, uygulayıcılardan beklenen _etik davranışı_ tanımlarken, [bilinen sınırlamaları](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) vardır, özellikle büyük ölçekli projelerde. Bunun yerine, birçok veri bilimi uzmanı [kontrol listelerini](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) savunur, bu da **ilkeleri uygulamalara** daha belirleyici ve uygulanabilir yollarla bağlayabilir.

Kontrol listeleri, soruları "evet/hayır" görevlerine dönüştürerek operasyonelleştirilebilir ve standart ürün sürüm iş akışlarının bir parçası olarak izlenebilir hale getirir.

Örnekler:
 * [Deon](https://deon.drivendata.org/) - [endüstri önerilerinden](https://deon.drivendata.org/#checklist-citations) oluşturulmuş genel amaçlı bir veri etik kontrol listesi ve kolay entegrasyon için bir komut satırı aracı.
 * [Gizlilik Denetim Kontrol Listesi](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - yasal ve sosyal maruz kalma perspektiflerinden bilgi işleme uygulamaları için genel rehberlik sağlar.
 * [AI Adalet Kontrol Listesi](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - AI geliştirme döngülerine adalet kontrollerinin benimsenmesini ve entegrasyonunu desteklemek için AI uygulayıcıları tarafından oluşturuldu.
 * [Veri ve AI'da etik için 22 soru](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - tasarım, uygulama ve organizasyonel bağlamlarda etik sorunların ilk keşfi için daha açık uçlu bir çerçeve.

### 3. Etik Düzenlemeler

Etik, paylaşılan değerleri tanımlamak ve doğru olanı _gönüllü olarak_ yapmakla ilgilidir. **Uyum**, tanımlanmışsa ve nerede tanımlanmışsa _yasalara uymak_ ile ilgilidir. **Yönetim**, organizasyonların etik ilkeleri uygulamak ve belirlenmiş yasalara uymak için çalıştığı tüm yolları kapsar.

Bugün, yönetim organizasyonlar içinde iki şekilde gerçekleşir. İlk olarak, **etik AI** ilkelerini tanımlamak ve organizasyondaki tüm AI ile ilgili projelerde benimsenmeyi operasyonelleştirmekle ilgilidir. İkincisi, faaliyet gösterdiği bölgeler için tüm hükümet tarafından belirlenmiş **veri koruma düzenlemelerine** uymakla ilgilidir.

Veri koruma ve gizlilik düzenlemeleri örnekleri:

 * `1974`, [ABD Gizlilik Yasası](https://www.justice.gov/opcl/privacy-act-1974) - _federal hükümetin_ kişisel bilgilerin toplanmasını, kullanılmasını ve açıklanmasını düzenler.
 * `1996`, [ABD Sağlık Sigortası Taşınabilirlik ve Hesap Verebilirlik Yasası (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - kişisel sağlık verilerini korur.
 * `1998`, [ABD Çocukların Çevrimiçi Gizliliğini Koruma Yasası (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - 13 yaş altındaki çocukların veri gizliliğini korur.
 * `2018`, [Genel Veri Koruma Yönetmeliği (GDPR)](https://gdpr-info.eu/) - kullanıcı hakları, veri koruma ve gizlilik sağlar.
 * `2018`, [California Tüketici Gizliliği Yasası (CCPA)](https://www.oag.ca.gov/privacy/ccpa) tüketicilere (kişisel) verileri üzerinde daha fazla _hak_ verir.
 * `2021`, Çin'in [Kişisel Bilgi Koruma Yasası](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) yeni geçti ve dünya çapında en güçlü çevrimiçi veri gizliliği düzenlemelerinden birini oluşturdu.

> 🚨 Avrupa Birliği tarafından tanımlanan GDPR (Genel Veri Koruma Yönetmeliği), bugün en etkili veri gizliliği düzenlemelerinden biri olmaya devam ediyor. Ayrıca vatandaşların dijital gizliliğini ve kişisel verilerini korumak için [8 kullanıcı hakkı](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) tanımladığını biliyor muydunuz? Bunların ne olduğunu ve neden önemli olduklarını öğrenin.

### 4. Etik Kültürü

Uyum (yasanın "harfini" yerine getirmek için yeterince yapmak) ile [sistemik sorunları](https://www.coursera.org/learn/data-science-ethics/home/week/4) ele almak (örneğin, katılaşma, bilgi asimetrisi ve dağıtım adaletsizliği) arasında hala elle tutulamayan bir boşluk olduğunu unutmayın. 

İkincisi, [etik kültürleri tanımlamak için işbirlikçi yaklaşımlar](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) gerektirir ve bu, organizasyonlar arasında duygusal bağlar ve tutarlı paylaşılan değerler oluşturur. Bu, organizasyonlarda daha [resmileştirilmiş veri etik kültürleri](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) oluşturmayı gerektirir - _herkesin_ (etik endişeleri sürecin erken aşamalarında dile getirmek için) [Andon ipini çekmesine](https://en.wikipedia.org/wiki/Andon_(manufacturing)) olanak tanır ve _etik değerlendirmeleri_ (örneğin, işe alımda) AI projelerinde ekip oluşturmanın temel kriteri haline getirir.

---
## [Ders sonrası test](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Gözden Geçirme ve Kendi Kendine Çalışma 

Kurslar ve kitaplar, temel etik kavramlarını ve zorluklarını anlamaya yardımcı olurken, vaka çalışmaları ve araçlar gerçek dünya bağlamlarında uygulamalı etik uygulamalarına yardımcı olur. İşte başlamak için birkaç kaynak.

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - Microsoft'tan Adalet üzerine bir ders.
* [Sorumlu Yapay Zeka İlkeleri](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - Microsoft Learn'den ücretsiz öğrenim yolu.
* [Etik ve Veri Bilimi](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EKitap (M. Loukides, H. Mason ve diğerleri)
* [Veri Bilimi Etiği](https://www.coursera.org/learn/data-science-ethics#syllabus) - Michigan Üniversitesi'nden çevrimiçi kurs.
* [Etik Açıklanıyor](https://ethicsunwrapped.utexas.edu/case-studies) - Texas Üniversitesi'nden vaka çalışmaları.

# Ödev 

[Bir Veri Etiği Vaka Çalışması Yazın](assignment.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.