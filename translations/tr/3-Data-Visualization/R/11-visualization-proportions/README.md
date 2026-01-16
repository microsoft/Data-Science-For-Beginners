<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-28T11:04:08+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "tr"
}
-->
# Oranları Görselleştirme

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Oranları Görselleştirme - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Bu derste, mantarlarla ilgili bir veri seti kullanarak oranları görselleştireceksiniz. Örneğin, bir veri setinde kaç farklı mantar türü bulunduğunu inceleyebilirsiniz. Agaricus ve Lepiota ailelerine ait 23 tür lamelli mantar hakkında bilgiler içeren Audubon'dan alınmış bir veri setini keşfedeceğiz. Aşağıdaki gibi lezzetli görselleştirmelerle denemeler yapacaksınız:

- Pasta grafikleri 🥧
- Donut grafikleri 🍩
- Waffle grafikleri 🧇

> 💡 Microsoft Research tarafından geliştirilen [Charticulator](https://charticulator.com) adlı çok ilginç bir proje, veri görselleştirmeleri için ücretsiz bir sürükle-bırak arayüzü sunuyor. Bu projede, mantar veri setini kullandıkları bir eğitim de var! Böylece hem veriyi keşfedebilir hem de kütüphaneyi öğrenebilirsiniz: [Charticulator eğitimi](https://charticulator.com/tutorials/tutorial4.html).

## [Ders Öncesi Test](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Mantarlarınızı Tanıyın 🍄

Mantarlar oldukça ilginçtir. Hadi bir veri seti içe aktararak onları inceleyelim:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
Bir tablo çıktı olarak basılır ve analiz için harika veriler içerir:


| sınıf     | şapka şekli | şapka yüzeyi | şapka rengi | morarma | koku    | lamel bağlantısı | lamel aralığı | lamel boyutu | lamel rengi | sap şekli | sap kökü | halka üstü sap yüzeyi | halka altı sap yüzeyi | halka üstü sap rengi | halka altı sap rengi | örtü türü | örtü rengi | halka sayısı | halka türü | spor baskı rengi | popülasyon | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Zehirli | Konveks    | Düz      | Kahverengi     | Morarma | Keskin | Serbest            | Yakın        | Dar    | Siyah      | Genişleyen   | Eşit      | Düz                   | Düz                   | Beyaz                  | Beyaz                  | Kısmi   | Beyaz      | Bir         | Sarkık   | Siyah             | Dağınık  | Şehir   |
| Yenilebilir    | Konveks    | Düz      | Sarı    | Morarma | Badem  | Serbest            | Yakın        | Geniş     | Siyah      | Genişleyen   | Kulüp       | Düz                   | Düz                   | Beyaz                  | Beyaz                  | Kısmi   | Beyaz      | Bir         | Sarkık   | Kahverengi             | Çok   | Çimenlik |
| Yenilebilir    | Çan      | Düz      | Beyaz     | Morarma | Anason   | Serbest            | Yakın        | Geniş     | Kahverengi      | Genişleyen   | Kulüp       | Düz                   | Düz                   | Beyaz                  | Beyaz                  | Kısmi   | Beyaz      | Bir         | Sarkık   | Kahverengi             | Çok   | Çayır |
| Zehirli | Konveks    | Pullu       | Beyaz     | Morarma | Keskin | Serbest            | Yakın        | Dar    | Kahverengi      | Genişleyen   | Eşit      | Düz                   | Düz                   | Beyaz                  | Beyaz                  | Kısmi   | Beyaz      | Bir         | Sarkık   | Siyah             | Dağınık  | Şehir 
| Yenilebilir | Konveks       |Düz       | Yeşil     | Morarma Yok| Yok   |Serbest            | Kalabalık       | Geniş     | Siyah      | Daralan   | Eşit      |  Düz | Düz                    | Beyaz                 | Beyaz                  | Kısmi    | Beyaz     | Bir         | Geçici | Kahverengi             | Bol | Çimenlik
|Yenilebilir  |  Konveks      | Pullu   | Sarı         | Morarma  | Badem  | Serbest | Yakın  |   Geniş   |   Kahverengi  | Genişleyen   |   Kulüp                      | Düz                  | Düz    | Beyaz                 |  Beyaz                | Kısmi      | Beyaz    |  Bir  |  Sarkık | Siyah   | Çok | Çimenlik
      
Hemen fark ediyorsunuz ki tüm veriler metinsel. Bu verileri bir grafik oluşturmak için dönüştürmeniz gerekecek. Aslında, verilerin çoğu bir nesne olarak temsil ediliyor:

```r
names(mushrooms)
```

Çıktı şu şekilde:

```output
[1] "class"                    "cap.shape"               
 [3] "cap.surface"              "cap.color"               
 [5] "bruises"                  "odor"                    
 [7] "gill.attachment"          "gill.spacing"            
 [9] "gill.size"                "gill.color"              
[11] "stalk.shape"              "stalk.root"              
[13] "stalk.surface.above.ring" "stalk.surface.below.ring"
[15] "stalk.color.above.ring"   "stalk.color.below.ring"  
[17] "veil.type"                "veil.color"              
[19] "ring.number"              "ring.type"               
[21] "spore.print.color"        "population"              
[23] "habitat"            
```
Bu verileri alın ve 'sınıf' sütununu bir kategoriye dönüştürün:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```


Şimdi, mantar verilerini yazdırırsanız, zehirli/yenilebilir sınıfına göre kategorilere ayrıldığını görebilirsiniz:
```r
View(grouped)
```


| sınıf | sayı |
| --------- | --------- |
| Yenilebilir | 4208 |
| Zehirli| 3916 |



Bu tablodaki sırayı takip ederek sınıf kategori etiketlerinizi oluşturursanız, bir pasta grafiği oluşturabilirsiniz.

## Pasta!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
İşte, bu iki mantar sınıfına göre verilerin oranlarını gösteren bir pasta grafiği. Etiketlerin sırasını doğru almak oldukça önemlidir, özellikle burada, bu yüzden etiket dizisinin oluşturulma sırasını doğruladığınızdan emin olun!

![pasta grafiği](../../../../../translated_images/tr/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Donutlar!

Biraz daha görsel olarak ilginç bir pasta grafiği, ortasında bir delik olan bir donut grafiğidir. Verilerimize bu yöntemle bakalım.

Mantarların büyüdüğü çeşitli habitatlara bir göz atın:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Çıktı şu şekilde:
| habitat| sayı |
| --------- | --------- |
| Çimenlik    | 2148 |
| Yapraklar| 832 |
| Çayırlar    | 292 |
| Yollar| 1144 |
| Şehir    | 368 |
| Atık| 192 |
| Odun| 3148 |


Burada, verilerinizi habitatlara göre grupluyorsunuz. 7 habitat listelenmiş, bu yüzden donut grafiğiniz için bunları etiket olarak kullanın:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![donut grafiği](../../../../../translated_images/tr/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Bu kod iki kütüphaneyi kullanır - ggplot2 ve webr. webr kütüphanesinin PieDonut fonksiyonunu kullanarak kolayca bir donut grafiği oluşturabilirsiniz!

R'de donut grafikleri yalnızca ggplot2 kütüphanesi kullanılarak da yapılabilir. Daha fazla bilgi edinmek için [buraya](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) göz atabilir ve kendiniz deneyebilirsiniz.

Artık verilerinizi nasıl gruplandıracağınızı ve ardından pasta veya donut olarak nasıl göstereceğinizi bildiğinize göre, diğer grafik türlerini keşfedebilirsiniz. Waffle grafiğini deneyin, bu da miktarları keşfetmenin farklı bir yoludur.
## Waffle!

'Waffle' türü bir grafik, miktarları karelerden oluşan 2D bir dizi olarak görselleştirmenin farklı bir yoludur. Bu veri setindeki mantar şapka renklerinin farklı miktarlarını görselleştirmeyi deneyin. Bunu yapmak için [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) adlı bir yardımcı kütüphane yüklemeniz ve görselleştirmenizi oluşturmak için kullanmanız gerekir:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Verilerinizden bir segment seçin ve gruplandırın:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Etiketler oluşturup verilerinizi gruplandırarak bir waffle grafiği oluşturun:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Bir waffle grafiği kullanarak, bu mantar veri setindeki şapka renklerinin oranlarını açıkça görebilirsiniz. İlginç bir şekilde, birçok yeşil şapkalı mantar var!

![waffle grafiği](../../../../../translated_images/tr/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

Bu derste, oranları görselleştirmenin üç yolunu öğrendiniz. Öncelikle, verilerinizi kategorilere ayırmanız ve ardından verileri göstermek için en iyi yolu seçmeniz gerekiyor - pasta, donut veya waffle. Hepsi lezzetli ve kullanıcıya bir veri setinin anlık görüntüsünü sunar.

## 🚀 Meydan Okuma

Bu lezzetli grafikleri [Charticulator](https://charticulator.com) ile yeniden oluşturmaya çalışın.
## [Ders Sonrası Test](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Gözden Geçirme ve Kendi Kendine Çalışma

Bazen pasta, donut veya waffle grafiği kullanmanın ne zaman uygun olduğu açık olmayabilir. Bu konuda okumak için bazı makaleler:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Bu zor kararla ilgili daha fazla bilgi bulmak için araştırma yapın.
## Ödev

[Excel'de Deneyin](assignment.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.