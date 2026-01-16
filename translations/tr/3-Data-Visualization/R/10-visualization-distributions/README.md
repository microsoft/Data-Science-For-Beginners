<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-28T11:08:25+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "tr"
}
-->
# Dağılımları Görselleştirme

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Dağılımları Görselleştirme - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Önceki derste, Minnesota kuşlarıyla ilgili bir veri kümesi hakkında bazı ilginç bilgiler öğrendiniz. Aykırı değerleri görselleştirerek hatalı verileri buldunuz ve kuş kategorileri arasındaki maksimum uzunluk farklarına baktınız.

## [Ders Öncesi Testi](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Kuş veri kümesini keşfedin

Verilere derinlemesine bakmanın bir başka yolu, verilerin bir eksen boyunca nasıl organize edildiğini incelemek, yani dağılımını incelemektir. Örneğin, bu veri kümesinde Minnesota kuşlarının maksimum kanat açıklığı veya maksimum vücut kütlesinin genel dağılımını öğrenmek isteyebilirsiniz.

Bu veri kümesindeki verilerin dağılımları hakkında bazı bilgiler keşfedelim. R konsolunuzda `ggplot2` ve veri tabanını içe aktarın. Önceki konuda olduğu gibi veri tabanından aykırı değerleri kaldırın.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | İsim                         | BilimselAd             | Kategori              | Takım         | Aile     | Cins        | KorumaDurumu        | MinUzunluk | MaxUzunluk | MinVücutKütlesi | MaxVücutKütlesi | MinKanatAçıklığı | MaxKanatAçıklığı |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :------------ | :------- | :---------- | :----------------- | ----------: | ----------: | --------------: | --------------: | --------------: | --------------: |
|    0 | Kara karınlı ıslıkçı ördek   | Dendrocygna autumnalis | Ördekler/Kazlar/Su Kuşları | Anseriformes | Anatidae | Dendrocygna | LC                 |        47   |        56   |           652   |          1020   |            76   |            94   |
|    1 | Sarımsı ıslıkçı ördek        | Dendrocygna bicolor    | Ördekler/Kazlar/Su Kuşları | Anseriformes | Anatidae | Dendrocygna | LC                 |        45   |        53   |           712   |          1050   |            85   |            93   |
|    2 | Kar kazı                     | Anser caerulescens     | Ördekler/Kazlar/Su Kuşları | Anseriformes | Anatidae | Anser       | LC                 |        64   |        79   |          2050   |          4050   |           135   |           165   |
|    3 | Ross'un kazı                 | Anser rossii           | Ördekler/Kazlar/Su Kuşları | Anseriformes | Anatidae | Anser       | LC                 |      57.3   |        64   |          1066   |          1567   |           113   |           116   |
|    4 | Büyük beyaz alınlı kaz       | Anser albifrons        | Ördekler/Kazlar/Su Kuşları | Anseriformes | Anatidae | Anser       | LC                 |        64   |        81   |          1930   |          3310   |           130   |           165   |

Genel olarak, verilerin nasıl dağıldığını hızlıca görmek için önceki derste yaptığımız gibi bir dağılım grafiği kullanabilirsiniz:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![her takıma göre maksimum uzunluk](../../../../../translated_images/tr/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.png)

Bu, her kuş takımına göre vücut uzunluğunun genel dağılımını gösterir, ancak gerçek dağılımları göstermek için en uygun yol değildir. Bu görev genellikle bir Histogram oluşturarak gerçekleştirilir.

## Histogramlarla Çalışmak

`ggplot2`, Histogramlar kullanarak veri dağılımını görselleştirmek için çok iyi yöntemler sunar. Bu tür grafik, çubukların yükselip alçalmasıyla dağılımın görülebildiği bir çubuk grafik gibidir. Bir histogram oluşturmak için sayısal verilere ihtiyacınız vardır. Histogram oluşturmak için, grafiğin türünü 'hist' olarak tanımlayarak bir grafik çizebilirsiniz. Bu grafik, tüm veri kümesinin MaxBodyMass dağılımını gösterir. Verileri daha küçük bölmelere ayırarak, verilerin değerlerinin dağılımını gösterebilir:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![tüm veri kümesi üzerindeki dağılım](../../../../../translated_images/tr/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.png)

Gördüğünüz gibi, bu veri kümesindeki 400'den fazla kuşun çoğu, Max Body Mass değerinin 2000'in altında olduğu aralığa düşmektedir. `bins` parametresini daha yüksek bir sayıya, örneğin 30'a değiştirerek veriler hakkında daha fazla bilgi edinin:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![30 bölmeli dağılım](../../../../../translated_images/tr/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.png)

Bu grafik, dağılımı biraz daha ayrıntılı bir şekilde gösterir. Daha az sola eğimli bir grafik, yalnızca belirli bir aralıktaki verileri seçerek oluşturulabilir:

Verilerinizi filtreleyerek vücut kütlesi 60'ın altında olan kuşları alın ve 30 `bins` gösterin:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![filtrelenmiş histogram](../../../../../translated_images/tr/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.png)

✅ Diğer filtreleri ve veri noktalarını deneyin. Verilerin tam dağılımını görmek için, etiketli dağılımları göstermek için `['MaxBodyMass']` filtresini kaldırın.

Histogram, bazı güzel renk ve etiketleme geliştirmeleri de sunar:

İki dağılım arasındaki ilişkiyi karşılaştırmak için 2D bir histogram oluşturun. `MaxBodyMass` ve `MaxLength`'i karşılaştıralım. `ggplot2`, parlak renkler kullanarak yakınsama göstermenin yerleşik bir yolunu sunar:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Bu iki öğe arasında beklenen bir eksen boyunca bir korelasyon olduğu ve bir noktada özellikle güçlü bir yakınsama olduğu görülüyor:

![2d grafik](../../../../../translated_images/tr/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.png)

Histogramlar, varsayılan olarak sayısal verilerle iyi çalışır. Peki ya metin verilerine göre dağılımları görmek isterseniz? 
## Metin verilerini kullanarak veri kümesindeki dağılımları keşfedin 

Bu veri kümesi ayrıca kuş kategorisi, cinsi, türü ve ailesi ile koruma durumu hakkında iyi bilgiler içerir. Bu koruma bilgilerini inceleyelim. Kuşların koruma durumlarına göre dağılımı nedir?

> ✅ Veri kümesinde, koruma durumunu tanımlamak için birkaç kısaltma kullanılmıştır. Bu kısaltmalar, türlerin durumunu kataloglayan bir organizasyon olan [IUCN Kırmızı Liste Kategorileri](https://www.iucnredlist.org/) tarafından sağlanmıştır.
> 
> - CR: Kritik Tehlike Altında
> - EN: Tehlike Altında
> - EX: Soyu Tükenmiş
> - LC: En Az Endişe
> - NT: Tehdit Altında
> - VU: Hassas

Bunlar metin tabanlı değerlerdir, bu nedenle bir histogram oluşturmak için bir dönüşüm yapmanız gerekecektir. Filtrelenmiş kuşlar veri çerçevesini kullanarak, koruma durumunu Minimum Kanat Açıklığı ile birlikte gösterin. Ne görüyorsunuz? 

```r
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EX'] <- 'x1' 
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'CR'] <- 'x2'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EN'] <- 'x3'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'NT'] <- 'x4'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'VU'] <- 'x5'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'LC'] <- 'x6'

ggplot(data=birds_filtered_1, aes(x = MinWingspan, fill = ConservationStatus)) +
  geom_histogram(position = "identity", alpha = 0.4, bins = 20) +
  scale_fill_manual(name="Conservation Status",values=c("red","green","blue","pink"),labels=c("Endangered","Near Threathened","Vulnerable","Least Concern"))
```

![kanat açıklığı ve koruma durumu](../../../../../translated_images/tr/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.png)

Minimum kanat açıklığı ile koruma durumu arasında iyi bir korelasyon görünmüyor. Bu yöntemi kullanarak veri kümesinin diğer öğelerini test edin. Farklı filtreler de deneyebilirsiniz. Herhangi bir korelasyon buluyor musunuz?

## Yoğunluk Grafikleri

Şimdiye kadar incelediğimiz histogramların 'basamaklı' olduğunu ve düzgün bir yay şeklinde akmadığını fark etmiş olabilirsiniz. Daha düzgün bir yoğunluk grafiği göstermek için bir yoğunluk grafiği deneyebilirsiniz.

Hadi yoğunluk grafikleriyle çalışalım!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![yoğunluk grafiği](../../../../../translated_images/tr/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.png)

Grafiğin, Minimum Kanat Açıklığı verileri için önceki grafiği nasıl yansıttığını görebilirsiniz; sadece biraz daha düzgün. İkinci grafikte oluşturduğunuz o keskin MaxBodyMass çizgisini yeniden oluşturup bu yöntemle çok iyi bir şekilde düzeltebilirsiniz:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![vücut kütlesi yoğunluğu](../../../../../translated_images/tr/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.png)

Çok düzgün ama aşırı düzgün olmayan bir çizgi istiyorsanız, `adjust` parametresini düzenleyin: 

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![daha az düzgün vücut kütlesi](../../../../../translated_images/tr/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.png)

✅ Bu tür grafik için mevcut parametreler hakkında okuyun ve deneyin!

Bu tür grafikler, açıklayıcı görselleştirmeler sunar. Örneğin, birkaç satır kodla her kuş takımına göre maksimum vücut kütlesi yoğunluğunu gösterebilirsiniz:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![her takıma göre vücut kütlesi](../../../../../translated_images/tr/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.png)

## 🚀 Meydan Okuma

Histogramlar, temel dağılım grafikleri, çubuk grafikler veya çizgi grafiklerden daha sofistike bir grafik türüdür. İnternette histogramların iyi kullanımlarını bulmak için bir arama yapın. Nasıl kullanıldıklarını, neyi gösterdiklerini ve hangi alanlarda veya araştırma konularında kullanıldıklarını inceleyin.

## [Ders Sonrası Testi](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Gözden Geçirme ve Kendi Kendine Çalışma

Bu derste, `ggplot2` kullandınız ve daha sofistike grafikler göstermeye başladınız. `geom_density_2d()` hakkında araştırma yapın, bu "bir veya daha fazla boyutta sürekli olasılık yoğunluğu eğrisi"dir. Nasıl çalıştığını anlamak için [belgelere](https://ggplot2.tidyverse.org/reference/geom_density_2d.html) göz atın.

## Ödev

[Becerilerinizi uygulayın](assignment.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.