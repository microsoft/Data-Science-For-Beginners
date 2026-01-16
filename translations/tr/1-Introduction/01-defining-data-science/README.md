<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T18:52:02+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "tr"
}
-->
# Veri Biliminin Tanımı

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Veri Biliminin Tanımı - _Sketchnote by [@nitya](https://twitter.com/nitya)_               |

---

[![Veri Biliminin Tanımı Videosu](../../../../translated_images/tr/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Ders Öncesi Testi](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Veri Nedir?
Günlük hayatımızda sürekli olarak verilerle çevriliyiz. Şu anda okuduğunuz metin bir veridir. Akıllı telefonunuzdaki arkadaşlarınızın telefon numaraları bir veridir, aynı şekilde saatinizde görünen mevcut zaman da bir veridir. İnsanlar olarak, doğal olarak verilerle çalışırız; sahip olduğumuz parayı sayarız veya arkadaşlarımıza mektuplar yazarız.

Ancak, bilgisayarların icadıyla birlikte veri çok daha kritik bir hale geldi. Bilgisayarların temel rolü hesaplamalar yapmaktır, ancak çalışabilmeleri için verilere ihtiyaç duyarlar. Bu nedenle, bilgisayarların verileri nasıl depoladığını ve işlediğini anlamamız gerekiyor.

İnternetin ortaya çıkışıyla birlikte, bilgisayarların veri işleme cihazları olarak rolü arttı. Düşünürseniz, artık bilgisayarları hesaplama yapmaktan çok veri işleme ve iletişim için kullanıyoruz. Bir arkadaşımıza e-posta yazdığımızda veya internette bilgi aradığımızda - aslında veri oluşturuyor, depoluyor, aktarıyor ve manipüle ediyoruz.
> Bilgisayarları en son ne zaman gerçekten bir şey hesaplamak için kullandığınızı hatırlıyor musunuz?

## Veri Bilimi Nedir?

[Wikipedia](https://en.wikipedia.org/wiki/Data_science)'ya göre, **Veri Bilimi**, *yapılandırılmış ve yapılandırılmamış verilerden bilgi ve içgörü elde etmek için bilimsel yöntemler kullanan ve bu bilgiyi ve uygulanabilir içgörüleri geniş bir uygulama alanında kullanan bilimsel bir alan* olarak tanımlanır.

Bu tanım, veri biliminin şu önemli yönlerini vurgular:

* Veri biliminin ana hedefi, verilerden **bilgi çıkarmak**, başka bir deyişle - verileri **anlamak**, bazı gizli ilişkiler bulmak ve bir **model** oluşturmaktır.
* Veri bilimi, olasılık ve istatistik gibi **bilimsel yöntemler** kullanır. Aslında, *veri bilimi* terimi ilk kez ortaya çıktığında, bazı insanlar veri biliminin istatistik için sadece yeni bir havalı isim olduğunu savundu. Günümüzde bu alanın çok daha geniş olduğu açıkça görülmektedir.
* Elde edilen bilgiler, gerçek iş durumlarına uygulanabilecek **uygulanabilir içgörüler** üretmek için kullanılmalıdır.
* Hem **yapılandırılmış** hem de **yapılandırılmamış** verilerle çalışabilmeliyiz. Kursun ilerleyen bölümlerinde farklı veri türlerini tartışacağız.
* **Uygulama alanı** önemli bir kavramdır ve veri bilimciler genellikle finans, tıp, pazarlama gibi problem alanında en azından bir dereceye kadar uzmanlığa ihtiyaç duyarlar.

> Veri Biliminin bir diğer önemli yönü, verilerin bilgisayarlar kullanılarak nasıl toplanabileceğini, depolanabileceğini ve işlenebileceğini incelemesidir. İstatistik bize matematiksel temelleri sağlarken, veri bilimi matematiksel kavramları verilerden içgörü elde etmek için uygular.

[Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))'e atfedilen bir yaklaşıma göre, veri bilimine ayrı bir bilim paradigması olarak bakılabilir:
* **Ampirik**, çoğunlukla gözlemlere ve deney sonuçlarına dayanır
* **Teorik**, yeni kavramlar mevcut bilimsel bilgiden ortaya çıkar
* **Hesaplamalı**, bazı hesaplama deneylerine dayanarak yeni prensipler keşfedilir
* **Veri Odaklı**, verilerdeki ilişkileri ve desenleri keşfetmeye dayanır  

## İlgili Diğer Alanlar

Veri her yerde olduğu için, veri bilimi de birçok diğer disipline dokunan geniş bir alandır.

<dl>
<dt>Veritabanları</dt>
<dd>
Verilerin <b>nasıl depolanacağı</b> önemli bir husustur, yani verileri daha hızlı işleme imkanı sağlayacak şekilde nasıl yapılandıracağımız. Yapılandırılmış ve yapılandırılmamış verileri depolayan farklı türde veritabanları vardır, bunları <a href="../../2-Working-With-Data/README.md">kursumuzda ele alacağız</a>.
</dd>
<dt>Büyük Veri</dt>
<dd>
Çoğu zaman, nispeten basit bir yapıya sahip çok büyük miktarda veriyi depolamamız ve işlememiz gerekir. Bu verileri bir bilgisayar kümesinde dağıtılmış bir şekilde depolamak ve verimli bir şekilde işlemek için özel yaklaşımlar ve araçlar vardır.
</dd>
<dt>Makine Öğrenimi</dt>
<dd>
Veriyi anlamanın bir yolu, istenen sonucu tahmin edebilecek bir <b>model</b> oluşturmaktır. Verilerden model geliştirmeye <b>makine öğrenimi</b> denir. Daha fazla bilgi edinmek için <a href="https://aka.ms/ml-beginners">Makine Öğrenimi Başlangıç Kılavuzu</a> müfredatımıza göz atabilirsiniz.
</dd>
<dt>Yapay Zeka</dt>
<dd>
Makine öğreniminin bir alanı olan yapay zeka (AI) da verilere dayanır ve insan düşünce süreçlerini taklit eden yüksek karmaşıklıkta modeller oluşturmayı içerir. AI yöntemleri genellikle yapılandırılmamış verileri (örneğin doğal dil) yapılandırılmış içgörülere dönüştürmemize olanak tanır.
</dd>
<dt>Görselleştirme</dt>
<dd>
Büyük miktarda veri bir insan için anlaşılmaz olabilir, ancak bu verileri kullanarak faydalı görselleştirmeler oluşturduğumuzda, veriyi daha iyi anlayabilir ve bazı sonuçlar çıkarabiliriz. Bu nedenle, bilgiyi görselleştirmenin birçok yolunu bilmek önemlidir - bu konuyu kursumuzun <a href="../../3-Data-Visualization/README.md">3. Bölümünde</a> ele alacağız. İlgili alanlar arasında <b>Bilgilendirme Grafikleri</b> ve genel olarak <b>İnsan-Bilgisayar Etkileşimi</b> yer alır.
</dd>
</dl>

## Veri Türleri

Daha önce de belirttiğimiz gibi, veri her yerde. Sadece doğru şekilde yakalamamız gerekiyor! **Yapılandırılmış** ve **yapılandırılmamış** veri arasında ayrım yapmak faydalıdır. Yapılandırılmış veri genellikle iyi yapılandırılmış bir formda, genellikle bir tablo veya bir dizi tablo olarak temsil edilirken, yapılandırılmamış veri sadece bir dosya koleksiyonudur. Bazen ayrıca büyük ölçüde değişebilen bir tür yapıya sahip olan **yarı yapılandırılmış** verilerden de bahsedebiliriz.

| Yapılandırılmış                                                             | Yarı yapılandırılmış                                                                          | Yapılandırılmamış                       |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| Telefon numaralarıyla birlikte kişilerin listesi                            | Bağlantılar içeren Wikipedia sayfaları                                                        | Encyclopedia Britannica'nın metni       |
| Son 20 yılda bir binanın tüm odalarındaki her dakika sıcaklık ölçümleri      | Yazarlar, yayın tarihi ve özet içeren JSON formatında bilimsel makaleler koleksiyonu          | Gözetim kamerasından gelen ham video     |
| Binaya giren tüm kişilerin yaş ve cinsiyet verileri                          | İnternet sayfaları                                                                            | Gözetim kamerasından gelen ham video     |

## Veriyi Nereden Alabilirsiniz?

Veri elde edilebilecek birçok kaynak vardır ve hepsini listelemek imkansızdır! Ancak, veriyi alabileceğiniz tipik yerlerden bazılarını belirtelim:

* **Yapılandırılmış**
  - **Nesnelerin İnterneti** (IoT), sıcaklık veya basınç sensörleri gibi farklı sensörlerden gelen veriler dahil olmak üzere birçok faydalı veri sağlar. Örneğin, bir ofis binası IoT sensörleriyle donatılmışsa, maliyetleri en aza indirmek için ısıtma ve aydınlatmayı otomatik olarak kontrol edebiliriz.
  - **Anketler**, kullanıcıların bir satın alma işleminden sonra veya bir web sitesini ziyaret ettikten sonra doldurmasını istediğimiz anketler.
  - **Davranış Analizi**, örneğin bir kullanıcının bir siteye ne kadar derinlemesine girdiğini ve siteyi terk etme nedenini anlamamıza yardımcı olabilir.
* **Yapılandırılmamış**
  - **Metinler**, genel bir **duygu skoru** veya anahtar kelimeler ve anlamsal anlam çıkarma gibi zengin içgörüler sağlayabilir.
  - **Görüntüler** veya **Videolar**. Bir gözetim kamerasından gelen video, yoldaki trafiği tahmin etmek ve insanları olası trafik sıkışıklıkları hakkında bilgilendirmek için kullanılabilir.
  - Web sunucusu **Günlükleri**, sitemizin en sık ziyaret edilen sayfalarını ve ne kadar süreyle ziyaret edildiğini anlamak için kullanılabilir.
* Yarı yapılandırılmış
  - **Sosyal Ağ** grafikleri, kullanıcı kişilikleri ve bilgiyi yayma potansiyeli hakkında veri için harika kaynaklar olabilir.
  - Bir partiden bir grup fotoğrafımız olduğunda, birbirleriyle fotoğraf çeken kişilerin bir grafiğini oluşturarak **Grup Dinamikleri** verilerini çıkarmayı deneyebiliriz.

Farklı veri kaynaklarını bilerek, veri bilimi tekniklerinin durumu daha iyi anlamak ve iş süreçlerini iyileştirmek için uygulanabileceği farklı senaryolar hakkında düşünebilirsiniz.

## Verilerle Neler Yapabilirsiniz?

Veri Biliminde, veri yolculuğunun şu adımlarına odaklanıyoruz:

<dl>
<dt>1) Veri Toplama</dt>
<dd>
İlk adım veriyi toplamaktır. Çoğu durumda bu, web uygulamasından bir veritabanına gelen veri gibi basit bir süreç olabilir, ancak bazen özel teknikler kullanmamız gerekebilir. Örneğin, IoT sensörlerinden gelen veri çok fazla olabilir ve tüm verileri daha fazla işlemden önce toplamak için IoT Hub gibi tampon uç noktaları kullanmak iyi bir uygulamadır.
</dd>
<dt>2) Veri Depolama</dt>
<dd>
Veri depolamak zorlu olabilir, özellikle büyük veri söz konusu olduğunda. Verilerin nasıl depolanacağına karar verirken, gelecekte verileri nasıl sorgulamak istediğinizi öngörmek mantıklıdır. Veriler birkaç şekilde depolanabilir:
<ul>
<li>İlişkisel bir veritabanı, bir dizi tabloyu depolar ve bu tabloları sorgulamak için SQL adı verilen özel bir dil kullanır. Genellikle tablolar, şemalar adı verilen farklı gruplara organize edilir. Çoğu durumda, verileri orijinal formdan şemaya uyacak şekilde dönüştürmemiz gerekir.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">NoSQL</a> veritabanı, örneğin <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, veriler üzerinde şemaları zorlamaz ve hiyerarşik JSON belgeleri veya grafikler gibi daha karmaşık verileri depolamaya olanak tanır. Ancak, NoSQL veritabanları SQL'in zengin sorgulama yeteneklerine sahip değildir ve tabloların nasıl yapılandırıldığı ve tablolar arasındaki ilişkileri yöneten referans bütünlüğünü sağlayamaz.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Veri Gölü</a> depolama, ham, yapılandırılmamış formda büyük veri koleksiyonları için kullanılır. Veri gölleri genellikle büyük veri ile kullanılır, burada tüm veriler bir makineye sığmaz ve bir sunucu kümesi tarafından depolanmalı ve işlenmelidir. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a>, genellikle büyük veri ile birlikte kullanılan veri formatıdır.</li> 
</ul>
</dd>
<dt>3) Veri İşleme</dt>
<dd>
Bu, veri yolculuğunun en heyecan verici kısmıdır ve verilerin orijinal formundan görselleştirme/model eğitimi için kullanılabilecek bir forma dönüştürülmesini içerir. Yapılandırılmamış verilerle (örneğin metin veya görüntüler) çalışırken, verilerden <b>özellikler</b> çıkarmak için bazı AI tekniklerini kullanmamız gerekebilir, böylece veriyi yapılandırılmış bir forma dönüştürebiliriz.
</dd>
<dt>4) Görselleştirme / İnsan İçgörüleri</dt>
<dd>
Çoğu zaman, veriyi anlamak için görselleştirmemiz gerekir. Araç kutumuzda birçok farklı görselleştirme tekniği olduğunda, içgörü elde etmek için doğru görünümü bulabiliriz. Çoğu zaman, bir veri bilimci "verilerle oynamalı", verileri birçok kez görselleştirmeli ve bazı ilişkiler aramalıdır. Ayrıca, bir hipotezi test etmek veya farklı veri parçaları arasında bir korelasyonu kanıtlamak için istatistiksel teknikler kullanabiliriz.   
</dd>
<dt>5) Tahmin Modeli Eğitimi</dt>
<dd>
Veri biliminin nihai hedefi, verilere dayanarak kararlar alabilmek olduğundan, <a href="http://github.com/microsoft/ml-for-beginners">Makine Öğrenimi</a> tekniklerini kullanarak bir tahmin modeli oluşturmak isteyebiliriz. Daha sonra bunu, benzer yapıya sahip yeni veri setlerini kullanarak tahminler yapmak için kullanabiliriz.
</dd>
</dl>

Tabii ki, gerçek verilere bağlı olarak, bazı adımlar eksik olabilir (örneğin, veriler zaten veritabanında olduğunda veya model eğitimi gerekmediğinde), veya bazı adımlar birkaç kez tekrarlanabilir (örneğin veri işleme).

## Dijitalleşme ve Dijital Dönüşüm

Son on yılda, birçok işletme, iş kararları alırken verilerin önemini anlamaya başladı. İşletmeyi yürütmek için veri bilimi ilkelerini uygulamak isteyen biri önce bazı verileri toplamalı, yani iş süreçlerini dijital forma dönüştürmelidir. Bu, **dijitalleşme** olarak bilinir. Bu verilere veri bilimi tekniklerini uygulayarak kararları yönlendirmek, üretkenlikte önemli artışlara (ve hatta işin yön değiştirmesine) yol açabilir, bu da **dijital dönüşüm** olarak adlandırılır.

Bir örnek düşünelim. Diyelim ki öğrencilere çevrimiçi olarak sunduğumuz bir veri bilimi kursumuz var ve bunu geliştirmek için veri bilimi kullanmak istiyoruz. Bunu nasıl yapabiliriz?

"Ne dijitalleştirilebilir?" diye sorarak başlayabiliriz. En basit yol, her öğrencinin her modülü tamamlaması için geçen süreyi ölçmek ve her modülün sonunda çoktan seçmeli bir test vererek elde edilen bilgiyi ölçmek olabilir. Tüm öğrenciler arasında tamamlanma süresini ortalama alarak, öğrenciler için en çok zorluk çıkaran modülleri bulabilir ve onları basitleştirmek için çalışabiliriz.
> Bu yaklaşımın ideal olmadığını savunabilirsiniz, çünkü modüller farklı uzunluklarda olabilir. Zamanı modülün uzunluğuna (karakter sayısına göre) bölmek ve bu değerleri karşılaştırmak muhtemelen daha adil olacaktır.

Çoktan seçmeli testlerin sonuçlarını analiz etmeye başladığımızda, öğrencilerin anlamakta zorlandığı kavramları belirlemeye çalışabilir ve bu bilgiyi içeriği geliştirmek için kullanabiliriz. Bunu yapmak için, testleri her sorunun belirli bir kavram veya bilgi parçasıyla eşleştiği şekilde tasarlamamız gerekir.

Daha karmaşık bir analiz yapmak istersek, her modül için harcanan zamanı öğrencilerin yaş kategorilerine göre karşılaştırabiliriz. Bazı yaş kategorileri için modülü tamamlamak çok uzun zaman aldığını veya öğrencilerin modülü tamamlamadan bıraktığını görebiliriz. Bu, modül için yaş önerileri sunmamıza ve yanlış beklentilerden kaynaklanan memnuniyetsizliği en aza indirmemize yardımcı olabilir.

## 🚀 Zorluk

Bu zorlukta, metinlere bakarak Veri Bilimi alanıyla ilgili kavramları bulmaya çalışacağız. Veri Bilimi ile ilgili bir Wikipedia makalesi alacak, metni indirecek ve işleyeceğiz, ardından aşağıdaki gibi bir kelime bulutu oluşturacağız:

![Veri Bilimi için Kelime Bulutu](../../../../translated_images/tr/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Kodları incelemek için [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') dosyasını ziyaret edin. Ayrıca kodu çalıştırabilir ve tüm veri dönüşümlerinin gerçek zamanlı olarak nasıl gerçekleştirildiğini görebilirsiniz.

> Jupyter Notebook'ta kod çalıştırmayı bilmiyorsanız, [bu makaleye](https://soshnikov.com/education/how-to-execute-notebooks-from-github/) göz atabilirsiniz.

## [Ders sonrası quiz](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Ödevler

* **Görev 1**: Yukarıdaki kodu değiştirerek **Büyük Veri** ve **Makine Öğrenimi** alanlarıyla ilgili kavramları bulun.
* **Görev 2**: [Veri Bilimi Senaryoları Üzerine Düşünün](assignment.md)

## Katkıda Bulunanlar

Bu ders, [Dmitry Soshnikov](http://soshnikov.com) tarafından ♥️ ile hazırlanmıştır.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.