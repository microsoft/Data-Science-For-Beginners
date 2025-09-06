<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4039f1c76548d144a0aee0bf28304ec",
  "translation_date": "2025-08-28T11:09:44+00:00",
  "source_file": "3-Data-Visualization/R/13-meaningful-vizualizations/README.md",
  "language_code": "tr"
}
-->
# Anlamlı Görselleştirmeler Yapmak

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Anlamlı Görselleştirmeler - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

> "Veriyi yeterince zorlayın, her şeyi itiraf eder." -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Bir veri bilimcisinin temel becerilerinden biri, sahip olduğunuz soruları yanıtlamaya yardımcı olacak anlamlı bir veri görselleştirmesi oluşturma yeteneğidir. Verilerinizi görselleştirmeden önce, önceki derslerde yaptığınız gibi temizlenmiş ve hazırlanmış olduğundan emin olmanız gerekir. Bundan sonra, verileri en iyi şekilde nasıl sunacağınızı belirlemeye başlayabilirsiniz.

Bu derste şunları gözden geçireceksiniz:

1. Doğru grafik türünü nasıl seçersiniz
2. Yanıltıcı grafiklerden nasıl kaçınırsınız
3. Renklerle nasıl çalışılır
4. Grafiklerinizi okunabilirlik için nasıl şekillendirirsiniz
5. Animasyonlu veya 3D grafik çözümleri nasıl oluşturulur
6. Yaratıcı bir görselleştirme nasıl yapılır

## [Ders Öncesi Test](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Doğru grafik türünü seçin

Önceki derslerde, Matplotlib ve Seaborn kullanarak her türlü ilginç veri görselleştirmesi oluşturmayı denediniz. Genel olarak, sorduğunuz soruya uygun [doğru grafik türünü](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) bu tabloyu kullanarak seçebilirsiniz:

| Yapmanız gereken:          | Kullanmanız gereken:            |
| -------------------------- | ------------------------------- |
| Zaman içindeki veri eğilimlerini gösterin | Çizgi                          |
| Kategorileri karşılaştırın | Çubuk, Pasta                    |
| Toplamları karşılaştırın   | Pasta, Yığılmış Çubuk           |
| İlişkileri gösterin        | Dağılım, Çizgi, Facet, Çift Çizgi |
| Dağılımları gösterin       | Dağılım, Histogram, Kutu        |
| Oranları gösterin          | Pasta, Donut, Waffle            |

> ✅ Verilerinizin yapısına bağlı olarak, belirli bir grafiğin desteklemesi için metinden sayısala dönüştürmeniz gerekebilir.

## Yanıltmadan kaçının

Bir veri bilimcisi doğru veri için doğru grafiği seçmekte dikkatli olsa bile, veriler genellikle bir noktayı kanıtlamak için, çoğu zaman verilerin kendisini baltalama pahasına, yanıltıcı bir şekilde sunulabilir. Yanıltıcı grafikler ve infografikler için birçok örnek vardır!

[![Alberto Cairo'dan How Charts Lie](../../../../../translated_images/tornado.2880ffc7f135f82b5e5328624799010abefd1080ae4b7ecacbdc7d792f1d8849.tr.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")

> 🎥 Yanıltıcı grafikler hakkında bir konferans konuşması için yukarıdaki görsele tıklayın

Bu grafik, X eksenini ters çevirerek tarihe dayalı olarak gerçeğin tam tersini gösteriyor:

![kötü grafik 1](../../../../../translated_images/bad-chart-1.596bc93425a8ac301a28b8361f59a970276e7b961658ce849886aa1fed427341.tr.png)

[Bu grafik](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) daha da yanıltıcıdır, çünkü göz sağa çekilerek COVID vakalarının zamanla azaldığı sonucuna varır. Ancak, tarihlere dikkatlice bakarsanız, bu yanıltıcı düşüş eğilimini vermek için yeniden düzenlendiklerini görürsünüz.

![kötü grafik 2](../../../../../translated_images/bad-chart-2.62edf4d2f30f4e519f5ef50c07ce686e27b0196a364febf9a4d98eecd21f9f60.tr.jpg)

Bu kötü şöhretli örnek, yanıltmak için renk ve ters çevrilmiş bir Y ekseni kullanır: Silah dostu yasaların geçmesinden sonra silahlı ölümlerin arttığı sonucuna varmak yerine, göz tam tersinin doğru olduğunu düşünmek için kandırılır:

![kötü grafik 3](../../../../../translated_images/bad-chart-3.e201e2e915a230bc2cde289110604ec9abeb89be510bd82665bebc1228258972.tr.jpg)

Bu garip grafik, oranın nasıl manipüle edilebileceğini komik bir şekilde gösteriyor:

![kötü grafik 4](../../../../../translated_images/bad-chart-4.8872b2b881ffa96c3e0db10eb6aed7793efae2cac382c53932794260f7bfff07.tr.jpg)

Karşılaştırılamaz olanı karşılaştırmak, başka bir gölgeli numaradır. [Harika bir web sitesi](https://tylervigen.com/spurious-correlations), Maine'deki boşanma oranı ile margarin tüketimi gibi şeyleri ilişkilendiren 'uydurma korelasyonlar' sergiliyor. Bir Reddit grubu da verilerin [çirkin kullanımlarını](https://www.reddit.com/r/dataisugly/top/?t=all) topluyor.

Gözün yanıltıcı grafiklerle ne kadar kolay kandırılabileceğini anlamak önemlidir. Veri bilimcisinin niyeti iyi olsa bile, çok fazla kategori gösteren bir pasta grafiği gibi kötü bir grafik türü seçimi yanıltıcı olabilir.

## Renk

Yukarıdaki 'Florida silah şiddeti' grafiğinde gördüğünüz gibi, renk, özellikle ggplot2 ve RColorBrewer gibi çeşitli onaylanmış renk kütüphaneleri ve paletleriyle gelen kütüphaneler kullanılmadan tasarlanan grafiklerde, grafiklere ek bir anlam katmanı sağlayabilir. Bir grafiği elle yapıyorsanız, biraz [renk teorisi](https://colormatters.com/color-and-design/basic-color-theory) çalışması yapın.

> ✅ Grafik tasarlarken, erişilebilirliğin görselleştirmenin önemli bir yönü olduğunu unutmayın. Bazı kullanıcılar renk körü olabilir - grafiğiniz görme engelli kullanıcılar için iyi görüntüleniyor mu?

Grafiğiniz için renk seçerken dikkatli olun, çünkü renk, istemediğiniz bir anlam taşıyabilir. Yukarıdaki 'boy uzunluğu' grafiğindeki 'pembe kadınlar', grafiğin kendisinin tuhaflığını artıran belirgin bir 'feminen' anlam taşır.

[Renk anlamı](https://colormatters.com/color-symbolism/the-meanings-of-colors) dünyanın farklı yerlerinde farklı olabilir ve genellikle tonlarına göre anlam değiştirir. Genel olarak, renk anlamları şunları içerir:

| Renk   | Anlam               |
| ------ | ------------------- |
| kırmızı | güç                 |
| mavi    | güven, sadakat      |
| sarı    | mutluluk, dikkat    |
| yeşil   | ekoloji, şans, kıskançlık |
| mor     | mutluluk            |
| turuncu | canlılık            |

Özel renklerle bir grafik oluşturmanız gerekiyorsa, grafiklerinizin hem erişilebilir olduğundan hem de seçtiğiniz rengin iletmeye çalıştığınız anlamla uyumlu olduğundan emin olun.

## Grafiklerinizi okunabilirlik için şekillendirme

Grafikler okunabilir değilse anlamlı değildir! Verilerinizle iyi ölçeklenecek şekilde grafiğinizin genişliğini ve yüksekliğini şekillendirmeyi düşünmek için bir an durun. Eğer bir değişken (örneğin tüm 50 eyalet) gösterilmesi gerekiyorsa, mümkünse bunları Y ekseninde dikey olarak gösterin, böylece yatay kaydırmalı bir grafik oluşmasın.

Eksenlerinizi etiketleyin, gerekirse bir açıklama ekleyin ve verilerin daha iyi anlaşılması için araç ipuçları sunun.

Verileriniz X ekseninde metinsel ve ayrıntılıysa, daha iyi okunabilirlik için metni açılı hale getirebilirsiniz. [plot3D](https://cran.r-project.org/web/packages/plot3D/index.html), verileriniz destekliyorsa 3D grafikler sunar. Bununla sofistike veri görselleştirmeleri üretilebilir.

![3d grafikler](../../../../../translated_images/3d.db1734c151eee87d924989306a00e23f8cddac6a0aab122852ece220e9448def.tr.png)

## Animasyon ve 3D grafik gösterimi

Bugün en iyi veri görselleştirmelerinden bazıları animasyonludur. Shirley Wu, '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)' gibi D3 ile yapılmış harika örnekler sunar; burada her çiçek bir filmin görselleştirmesidir. Guardian için başka bir örnek ise 'bussed out', NYC'nin evsiz sorununu insanları şehirden otobüsle çıkararak nasıl ele aldığını göstermek için görselleştirmeleri Greensock ve D3 ile birleştiren bir interaktif deneyimdir.

![otobüsle taşınma](../../../../../translated_images/busing.8157cf1bc89a3f65052d362a78c72f964982ceb9dcacbe44480e35909c3dce62.tr.png)

> "Bussed Out: How America Moves its Homeless" [the Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Görselleştirmeler Nadieh Bremer & Shirley Wu tarafından.

Bu ders, bu güçlü görselleştirme kütüphanelerini öğretmek için yeterli derinliğe sahip olmasa da, bir Vue.js uygulamasında D3 kullanarak "Tehlikeli İlişkiler" kitabının animasyonlu bir sosyal ağ görselleştirmesini görüntülemek için bir kütüphane denemeyi deneyin.

> "Les Liaisons Dangereuses", bir dizi mektup olarak sunulan bir roman, yani bir epistolar romanıdır. 1782'de Choderlos de Laclos tarafından yazılmıştır ve 18. yüzyılın sonlarında Fransız aristokrasisinin iki rakip kahramanı olan Vicomte de Valmont ve Marquise de Merteuil'ün ahlaki açıdan iflas etmiş sosyal manevralarını anlatır. İkisi de sonunda yok olur, ancak büyük bir sosyal zarar vermeden önce değil. Roman, intikam planlamak veya sadece sorun çıkarmak için çevrelerindeki çeşitli insanlara yazılan bir dizi mektup olarak gelişir. Bu mektupların bir görselleştirmesini oluşturarak anlatının anahtar figürlerini görsel olarak keşfedin.

Bir sosyal ağın animasyonlu bir görünümünü gösterecek bir web uygulamasını tamamlayacaksınız. Bu, Vue.js ve D3 kullanarak bir [ağ görselleştirmesi](https://github.com/emiliorizzo/vue-d3-network) oluşturmak için yapılmış bir kütüphane kullanır. Uygulama çalışırken, düğümleri ekranda sürükleyerek verileri karıştırabilirsiniz.

![ilişkiler](../../../../../translated_images/liaisons.90ce7360bcf8476558f700bbbaf198ad697d5b5cb2829ba141a89c0add7c6ecd.tr.png)

## Proje: D3.js kullanarak bir ağ göstermek için bir grafik oluşturun

> Bu ders klasörü, referansınız için tamamlanmış projeyi bulabileceğiniz bir `solution` klasörü içerir.

1. Başlangıç klasörünün kökündeki README.md dosyasındaki talimatları izleyin. Proje bağımlılıklarını yüklemeden önce makinenizde NPM ve Node.js'nin çalıştığından emin olun.

2. `starter/src` klasörünü açın. Orada, numaralandırılmış, 'to' ve 'from' açıklamalarıyla birlikte romandaki tüm mektupları içeren bir .json dosyasını bulabileceğiniz bir `assets` klasörü bulacaksınız.

3. Görselleştirmeyi etkinleştirmek için `components/Nodes.vue` dosyasındaki kodu tamamlayın. `createLinks()` adlı yöntemi bulun ve aşağıdaki iç içe döngüyü ekleyin.

.json nesnesini döngüye alarak mektupların 'to' ve 'from' verilerini yakalayın ve görselleştirme kütüphanesinin tüketebilmesi için `links` nesnesini oluşturun:

```javascript
//loop through letters
      let f = 0;
      let t = 0;
      for (var i = 0; i < letters.length; i++) {
          for (var j = 0; j < characters.length; j++) {
              
            if (characters[j] == letters[i].from) {
              f = j;
            }
            if (characters[j] == letters[i].to) {
              t = j;
            }
        }
        this.links.push({ sid: f, tid: t });
      }
  ```

Uygulamanızı terminalden çalıştırın (npm run serve) ve görselleştirmenin keyfini çıkarın!

## 🚀 Zorluk

İnternette yanıltıcı görselleştirmeler keşfetmek için bir tur atın. Yazar kullanıcıyı nasıl yanıltıyor ve bu kasıtlı mı? Görselleştirmeleri düzeltmeyi deneyin ve nasıl görünmeleri gerektiğini gösterin.

## [Ders Sonrası Test](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/25)

## Gözden Geçirme ve Kendi Kendine Çalışma

Yanıltıcı veri görselleştirme hakkında bazı makaleler okuyun:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Tarihi varlıklar ve eserler için bu ilginç görselleştirmelere bir göz atın:

https://handbook.pubpub.org/

Animasyonun görselleştirmelerinizi nasıl geliştirebileceğiyle ilgili bu makaleye göz atın:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Ödev

[Kendi özel görselleştirmenizi oluşturun](assignment.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.