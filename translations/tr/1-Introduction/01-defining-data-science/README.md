<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-06T09:05:46+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "tr"
}
-->
## Veri Türleri

Daha önce de belirttiğimiz gibi, veri her yerde. Sadece doğru şekilde yakalamamız gerekiyor! **Yapılandırılmış** ve **yapılandırılmamış** veri arasında ayrım yapmak faydalı olabilir. Yapılandırılmış veri genellikle bir tablo veya bir dizi tablo gibi iyi yapılandırılmış bir biçimde temsil edilirken, yapılandırılmamış veri sadece bir dosya koleksiyonudur. Bazen **yarı yapılandırılmış** veriden de bahsedebiliriz; bu tür veriler bir tür yapıya sahip olabilir ancak bu yapı büyük ölçüde değişkenlik gösterebilir.

| Yapılandırılmış                                                              | Yarı yapılandırılmış                                                                          | Yapılandırılmamış                       |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------- |
| İnsanların telefon numaralarıyla birlikte listesi                           | Bağlantılar içeren Wikipedia sayfaları                                                      | Encyclopedia Britannica'nın metni       |
| Son 20 yılda bir binanın tüm odalarındaki her dakika sıcaklık ölçümleri      | Yazarlar, yayın tarihi ve özet bilgileriyle JSON formatında bilimsel makaleler koleksiyonu  | Kurumsal belgelerle dolu dosya paylaşımı |
| Binaya giren tüm insanların yaş ve cinsiyet bilgileri                        | İnternet sayfaları                                                                          | Gözetim kamerasından gelen ham video akışı |

## Veri Nereden Alınır?

Veri elde edilebilecek birçok kaynak vardır ve hepsini listelemek imkansızdır! Ancak, bazı tipik veri kaynaklarını belirtelim:

* **Yapılandırılmış**
  - **Nesnelerin İnterneti** (IoT), sıcaklık veya basınç sensörleri gibi farklı sensörlerden gelen veriler dahil olmak üzere birçok faydalı veri sağlar. Örneğin, bir ofis binası IoT sensörleriyle donatılmışsa, maliyetleri en aza indirmek için ısıtma ve aydınlatmayı otomatik olarak kontrol edebiliriz.
  - **Anketler**, kullanıcıların bir satın alma işleminden sonra veya bir web sitesini ziyaret ettikten sonra doldurmasını istediğimiz anketler.
  - **Davranış analizi**, örneğin bir kullanıcının bir siteye ne kadar derinlemesine girdiğini ve siteyi terk etme nedenlerini anlamamıza yardımcı olabilir.
* **Yapılandırılmamış**
  - **Metinler**, genel bir **duygu skoru** veya anahtar kelimeler ve anlamsal anlam çıkarma gibi zengin bir içgörü kaynağı olabilir.
  - **Görüntüler** veya **Videolar**. Bir gözetim kamerasından gelen video, yoldaki trafik yoğunluğunu tahmin etmek ve insanları olası trafik sıkışıklıkları hakkında bilgilendirmek için kullanılabilir.
  - Web sunucusu **Günlükleri**, sitemizin en sık ziyaret edilen sayfalarını ve bu sayfalarda ne kadar süre kalındığını anlamak için kullanılabilir.
* **Yarı yapılandırılmış**
  - **Sosyal Ağ** grafikleri, kullanıcı kişilikleri ve bilgiyi yayma potansiyel etkinliği hakkında veri sağlamak için harika kaynaklar olabilir.
  - Bir partiden bir dizi fotoğrafımız olduğunda, birbirleriyle fotoğraf çeken insanların grafiğini oluşturarak **Grup Dinamikleri** verilerini çıkarmaya çalışabiliriz.

Farklı veri kaynaklarını bilerek, veri bilimi tekniklerinin durumu daha iyi anlamak ve iş süreçlerini iyileştirmek için uygulanabileceği farklı senaryoları düşünebilirsiniz.

## Veri ile Neler Yapabilirsiniz?

Veri Bilimi'nde, veri yolculuğunun şu adımlarına odaklanıyoruz:

## Dijitalleşme ve Dijital Dönüşüm

Son on yılda, birçok işletme iş kararları alırken verinin önemini anlamaya başladı. Veri bilimi ilkelerini bir işletmeyi yönetmek için uygulamak, önce bazı verileri toplamak, yani iş süreçlerini dijital forma dönüştürmek gerektirir. Bu, **dijitalleşme** olarak bilinir. Bu veriye veri bilimi tekniklerini uygulayarak kararları yönlendirmek, üretkenlikte önemli artışlara (hatta işin yön değiştirmesine) yol açabilir ve bu da **dijital dönüşüm** olarak adlandırılır.

Bir örnek düşünelim. Diyelim ki öğrencilere çevrimiçi olarak sunduğumuz bir veri bilimi kursumuz var (tıpkı bu kurs gibi) ve bunu geliştirmek için veri bilimi kullanmak istiyoruz. Bunu nasıl yapabiliriz?

"Ne dijitalleştirilebilir?" sorusuyla başlayabiliriz. En basit yol, her öğrencinin her modülü tamamlaması için geçen süreyi ölçmek ve her modülün sonunda çoktan seçmeli bir test vererek elde edilen bilgiyi ölçmek olabilir. Tüm öğrenciler arasında tamamlanma süresini ortalama alarak, öğrenciler için en zorlayıcı olan modülleri bulabilir ve onları basitleştirmek için çalışabiliriz.
Bu yaklaşımın ideal olmadığını savunabilirsiniz, çünkü modüller farklı uzunluklarda olabilir. Zamanı modülün uzunluğuna (karakter sayısına göre) bölmek ve bu değerleri karşılaştırmak muhtemelen daha adil olacaktır.
Çoktan seçmeli testlerin sonuçlarını analiz etmeye başladığımızda, öğrencilerin anlamakta zorlandığı kavramları belirlemeye çalışabilir ve bu bilgiyi içeriği geliştirmek için kullanabiliriz. Bunu yapmak için, testleri her sorunun belirli bir kavram veya bilgi parçasıyla eşleştiği şekilde tasarlamamız gerekir.

Daha karmaşık bir analiz yapmak istersek, her modül için harcanan zamanı öğrencilerin yaş kategorilerine göre karşılaştırabiliriz. Bazı yaş kategorileri için modülü tamamlamak çok uzun zaman alıyor olabilir veya öğrenciler modülü tamamlamadan bırakıyor olabilir. Bu, modül için yaş önerileri sunmamıza ve yanlış beklentilerden kaynaklanan memnuniyetsizliği en aza indirmemize yardımcı olabilir.

## 🚀 Zorluk

Bu zorlukta, metinlere bakarak Veri Bilimi alanıyla ilgili kavramları bulmaya çalışacağız. Veri Bilimi ile ilgili bir Wikipedia makalesi alacağız, metni indirecek ve işleyeceğiz, ardından aşağıdaki gibi bir kelime bulutu oluşturacağız:

![Veri Bilimi için Kelime Bulutu](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Kodları incelemek için [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') dosyasını ziyaret edin. Kodları çalıştırabilir ve tüm veri dönüşümlerinin gerçek zamanlı olarak nasıl gerçekleştirildiğini görebilirsiniz.

> Jupyter Notebook'ta kod çalıştırmayı bilmiyorsanız, [bu makaleye](https://soshnikov.com/education/how-to-execute-notebooks-from-github/) göz atabilirsiniz.

## [Ders sonrası sınav](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Ödevler

* **Görev 1**: Yukarıdaki kodu değiştirerek **Büyük Veri** ve **Makine Öğrenimi** alanlarıyla ilgili kavramları bulun.
* **Görev 2**: [Veri Bilimi Senaryolarını Düşünün](assignment.md)

## Katkılar

Bu ders, [Dmitry Soshnikov](http://soshnikov.com) tarafından ♥️ ile hazırlanmıştır.

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.