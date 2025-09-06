<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cfb068050337a36e348debaa502a24fa",
  "translation_date": "2025-09-06T09:01:45+00:00",
  "source_file": "3-Data-Visualization/13-meaningful-visualizations/README.md",
  "language_code": "tr"
}
-->
# Anlamlı Görselleştirmeler Yapmak

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Anlamlı Görselleştirmeler - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

> "Veriyi yeterince zorlarsanız, her şeyi itiraf eder." -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Bir veri bilimcisinin temel becerilerinden biri, sahip olduğunuz soruları yanıtlamaya yardımcı olan anlamlı bir veri görselleştirmesi oluşturma yeteneğidir. Verilerinizi görselleştirmeden önce, önceki derslerde yaptığınız gibi, temizlenmiş ve hazırlanmış olduğundan emin olmanız gerekir. Bundan sonra, verileri en iyi şekilde nasıl sunacağınızı belirlemeye başlayabilirsiniz.

Bu derste şunları gözden geçireceksiniz:

1. Doğru grafik türünü nasıl seçersiniz
2. Yanıltıcı grafiklerden nasıl kaçınırsınız
3. Renklerle nasıl çalışılır
4. Grafiklerinizi okunabilirlik için nasıl şekillendirirsiniz
5. Animasyonlu veya 3D grafik çözümleri nasıl oluşturulur
6. Yaratıcı bir görselleştirme nasıl oluşturulur

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ds/quiz/24)

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

Bir veri bilimcisi doğru veri için doğru grafiği seçmekte dikkatli olsa bile, veriler genellikle bir noktayı kanıtlamak için, çoğu zaman verinin kendisini baltalama pahasına, yanıltıcı bir şekilde sunulabilir. Yanıltıcı grafikler ve infografikler hakkında birçok örnek vardır!

[![Alberto Cairo'dan How Charts Lie](../../../../3-Data-Visualization/13-meaningful-visualizations/images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")

> 🎥 Yanıltıcı grafikler hakkında bir konferans konuşması için yukarıdaki görsele tıklayın

Bu grafik, X eksenini ters çevirerek tarihe dayalı olarak gerçeğin tersini gösteriyor:

![kötü grafik 1](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-1.png)

[Bu grafik](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) daha da yanıltıcıdır, çünkü göz, zamanla COVID vakalarının çeşitli ilçelerde azaldığı sonucuna varmak için sağa çekilir. Aslında, tarihlere yakından bakarsanız, bu yanıltıcı düşüş eğilimini vermek için yeniden düzenlendiklerini görürsünüz.

![kötü grafik 2](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-2.jpg)

Bu kötü şöhretli örnek, yanıltmak için renk ve ters çevrilmiş bir Y ekseni kullanır: Silah dostu yasaların geçmesinden sonra silahlı ölümlerin arttığı sonucuna varmak yerine, göz bunun tersinin doğru olduğuna inanır:

![kötü grafik 3](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-3.jpg)

Bu garip grafik, oranların nasıl manipüle edilebileceğini, komik bir şekilde gösteriyor:

![kötü grafik 4](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-4.jpg)

Karşılaştırılamaz olanı karşılaştırmak, başka bir yanıltıcı numaradır. [Harika bir web sitesi](https://tylervigen.com/spurious-correlations), Maine'deki boşanma oranı ile margarin tüketimi gibi şeyleri ilişkilendiren 'uydurma korelasyonlar' hakkında 'gerçekler' sergiliyor. Bir Reddit grubu da [verilerin çirkin kullanımlarını](https://www.reddit.com/r/dataisugly/top/?t=all) topluyor.

Gözün yanıltıcı grafiklerle ne kadar kolay aldatılabileceğini anlamak önemlidir. Veri bilimcisinin niyeti iyi olsa bile, çok fazla kategori gösteren bir pasta grafiği gibi kötü bir grafik türü seçimi yanıltıcı olabilir.

## Renk

Yukarıdaki 'Florida silah şiddeti' grafiğinde gördüğünüz gibi, renk, özellikle Matplotlib ve Seaborn gibi çeşitli onaylanmış renk kütüphaneleri ve paletleriyle tasarlanmamış grafiklerde, grafiklere ek bir anlam katmanı sağlayabilir. Bir grafiği elle yapıyorsanız, biraz [renk teorisi](https://colormatters.com/color-and-design/basic-color-theory) çalışması yapın.

> ✅ Grafik tasarlarken, erişilebilirliğin görselleştirmenin önemli bir yönü olduğunu unutmayın. Bazı kullanıcılar renk körü olabilir - grafiğiniz görme engelli kullanıcılar için iyi görüntüleniyor mu?

Grafiğiniz için renk seçerken dikkatli olun, çünkü renk, istemediğiniz bir anlam taşıyabilir. Yukarıdaki 'boy' grafiğindeki 'pembe kadınlar', grafiğin kendisinin tuhaflığına katkıda bulunan belirgin bir 'feminen' anlam taşır.

[Renk anlamı](https://colormatters.com/color-symbolism/the-meanings-of-colors) dünyanın farklı yerlerinde farklı olabilir ve genellikle tonlarına göre anlam değiştirir. Genel olarak, renk anlamları şunları içerir:

| Renk   | Anlam               |
| ------ | ------------------- |
| kırmızı | güç                |
| mavi    | güven, sadakat     |
| sarı    | mutluluk, dikkat   |
| yeşil   | ekoloji, şans, kıskançlık |
| mor     | mutluluk           |
| turuncu | canlılık           |

Özel renklerle bir grafik oluşturmanız gerekiyorsa, grafiklerinizin hem erişilebilir olduğundan hem de seçtiğiniz rengin iletmeye çalıştığınız anlamla uyumlu olduğundan emin olun.

## Grafiklerinizi okunabilirlik için şekillendirme

Grafikler okunabilir olmadıkça anlamlı değildir! Verilerinizle iyi ölçeklenecek şekilde grafiğinizin genişliğini ve yüksekliğini şekillendirmeyi düşünmek için bir an durun. Eğer bir değişken (örneğin tüm 50 eyalet) gösterilmesi gerekiyorsa, mümkünse bunları Y ekseninde dikey olarak gösterin, böylece yatay kaydırmalı bir grafik oluşmasın.

Eksenlerinizi etiketleyin, gerekirse bir açıklama ekleyin ve verilerin daha iyi anlaşılması için araç ipuçları sunun.

Verileriniz X ekseninde metinsel ve ayrıntılıysa, daha iyi okunabilirlik için metni açılı bir şekilde yerleştirebilirsiniz. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html), verileriniz destekliyorsa 3D grafikler sunar. `mpl_toolkits.mplot3d` kullanarak sofistike veri görselleştirmeleri oluşturabilirsiniz.

![3d grafikler](../../../../3-Data-Visualization/13-meaningful-visualizations/images/3d.png)

## Animasyon ve 3D grafik gösterimi

Bugün en iyi veri görselleştirmelerinden bazıları animasyonludur. Shirley Wu, '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)' gibi D3 ile yapılmış harika örnekler sunar; burada her çiçek bir filmin görselleştirmesidir. Guardian için başka bir örnek, 'bussed out', NYC'nin evsiz sorununu insanları şehirden otobüsle çıkararak nasıl ele aldığını göstermek için görselleştirmeleri Greensock ve D3 ile birleştiren etkileşimli bir deneyimdir.

![busing](../../../../3-Data-Visualization/13-meaningful-visualizations/images/busing.png)

> "Bussed Out: Amerika Evsizlerini Nasıl Hareket Ettiriyor" [Guardian'dan](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Görselleştirmeler Nadieh Bremer & Shirley Wu tarafından.

Bu ders, bu güçlü görselleştirme kütüphanelerini öğretmek için yeterli derinliğe sahip olmasa da, bir Vue.js uygulamasında D3'ü kullanarak "Tehlikeli İlişkiler" kitabının animasyonlu bir sosyal ağ görselleştirmesini oluşturmayı deneyin.

> "Les Liaisons Dangereuses", bir dizi mektup olarak sunulan bir roman, yani bir mektup romanıdır. 1782'de Choderlos de Laclos tarafından yazılmıştır ve 18. yüzyılın sonlarında Fransız aristokrasisinin iki düellocu kahramanı olan Vicomte de Valmont ve Marquise de Merteuil'ün ahlaki açıdan yozlaşmış sosyal manevralarını anlatır. İkisi de sonunda yok olur, ancak büyük bir sosyal zarar vermeden önce değil. Roman, intikam planları yapmak veya sadece sorun çıkarmak için çevrelerindeki çeşitli kişilere yazılan bir dizi mektup olarak gelişir. Bu mektupların bir görselleştirmesini oluşturarak anlatının anahtar figürlerini görsel olarak keşfedin.

Bir sosyal ağı gösteren bir grafik oluşturacak bir web uygulamasını tamamlayacaksınız. Bu uygulama, Vue.js ve D3 kullanarak bir [ağ görselleştirmesi](https://github.com/emiliorizzo/vue-d3-network) oluşturmak için oluşturulmuş bir kütüphane kullanır. Uygulama çalışırken, ekrandaki düğümleri sürükleyerek verileri karıştırabilirsiniz.

![liaisons](../../../../3-Data-Visualization/13-meaningful-visualizations/images/liaisons.png)

## Proje: D3.js kullanarak bir ağ grafiği oluşturun

> Bu ders klasörü, referansınız için tamamlanmış projeyi bulabileceğiniz bir `solution` klasörü içerir.

1. Başlangıç klasörünün kökündeki README.md dosyasındaki talimatları izleyin. Projenizin bağımlılıklarını yüklemeden önce makinenizde NPM ve Node.js'nin çalıştığından emin olun.

2. `starter/src` klasörünü açın. Orada, romanın tüm mektuplarını, numaralandırılmış, 'to' ve 'from' açıklamalarıyla birlikte içeren bir .json dosyasını bulabileceğiniz bir `assets` klasörü bulacaksınız.

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

İnternette yanıltıcı görselleştirmeleri keşfetmek için bir tur atın. Yazar kullanıcıyı nasıl yanıltıyor ve bu kasıtlı mı? Görselleştirmeleri düzeltmeye çalışarak nasıl görünmeleri gerektiğini gösterin.

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ds/quiz/25)

## İnceleme ve Kendi Kendine Çalışma

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
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.