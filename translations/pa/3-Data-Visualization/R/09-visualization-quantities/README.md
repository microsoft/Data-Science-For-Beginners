<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-27T18:32:06+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "pa"
}
-->
# ਮਾਤਰਾ ਨੂੰ ਦਿਖਾਉਣਾ
|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| ਮਾਤਰਾ ਨੂੰ ਦਿਖਾਉਣਾ - _ਸਕੇਚਨੋਟ [@nitya](https://twitter.com/nitya) ਦੁਆਰਾ_ |

ਇਸ ਪਾਠ ਵਿੱਚ ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ ਕਿਵੇਂ ਕੁਝ ਉਪਲਬਧ R ਪੈਕੇਜ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਾਤਰਾ ਦੇ ਸੰਕਲਪ ਦੇ ਆਧਾਰ 'ਤੇ ਦਿਲਚਸਪ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ ਬਣਾਈਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ। ਮਿਨੇਸੋਟਾ ਦੇ ਪੰਛੀਆਂ ਬਾਰੇ ਇੱਕ ਸਾਫ ਕੀਤੇ ਡਾਟਾਸੈੱਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ, ਤੁਸੀਂ ਸਥਾਨਕ ਜੰਗਲੀ ਜੀਵਾਂ ਬਾਰੇ ਕਈ ਦਿਲਚਸਪ ਤੱਥ ਸਿੱਖ ਸਕਦੇ ਹੋ।  
## [ਪਾਠ ਤੋਂ ਪਹਿਲਾਂ ਕਵਿਜ਼](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## ggplot2 ਨਾਲ ਪੰਖਾਂ ਦੀ ਲੰਬਾਈ ਦਾ ਅਧਿਐਨ ਕਰੋ
ਸਧਾਰਣ ਅਤੇ ਜਟਿਲ ਪਲਾਟਾਂ ਅਤੇ ਚਾਰਟਾਂ ਬਣਾਉਣ ਲਈ ਇੱਕ ਸ਼ਾਨਦਾਰ ਲਾਇਬ੍ਰੇਰੀ ਹੈ [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html)। ਆਮ ਤੌਰ 'ਤੇ, ਇਹ ਲਾਇਬ੍ਰੇਰੀਆਂ ਵਰਤ ਕੇ ਡਾਟਾ ਪਲਾਟ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਸ਼ਾਮਲ ਹੈ: ਆਪਣੇ ਡਾਟਾਫਰੇਮ ਦੇ ਹਿੱਸਿਆਂ ਦੀ ਪਛਾਣ ਕਰਨਾ, ਜਿਨ੍ਹਾਂ ਨੂੰ ਤੁਸੀਂ ਟਾਰਗਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਡਾਟੇ 'ਤੇ ਜ਼ਰੂਰੀ ਤਬਦੀਲੀਆਂ ਕਰਨਾ, ਇਸ ਦੇ x ਅਤੇ y ਐਕਸਿਸ ਮੁੱਲਾਂ ਨੂੰ ਨਿਰਧਾਰਤ ਕਰਨਾ, ਪਲਾਟ ਦੀ ਕਿਸਮ ਚੁਣਨਾ, ਅਤੇ ਫਿਰ ਪਲਾਟ ਦਿਖਾਉਣਾ।

`ggplot2` ਇੱਕ ਸਿਸਟਮ ਹੈ ਜੋ ਗ੍ਰਾਫਿਕਸ ਨੂੰ ਡਿਕਲੇਰੇਟਿਵ ਢੰਗ ਨਾਲ ਬਣਾਉਂਦਾ ਹੈ, ਜੋ ਕਿ "ਗ੍ਰਾਮਰ ਆਫ ਗ੍ਰਾਫਿਕਸ" 'ਤੇ ਆਧਾਰਿਤ ਹੈ। [ਗ੍ਰਾਮਰ ਆਫ ਗ੍ਰਾਫਿਕਸ](https://en.wikipedia.org/wiki/Ggplot2) ਡਾਟਾ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ ਲਈ ਇੱਕ ਆਮ ਯੋਜਨਾ ਹੈ ਜੋ ਗ੍ਰਾਫਾਂ ਨੂੰ ਅਰਥਪੂਰਨ ਹਿੱਸਿਆਂ ਵਿੱਚ ਵੰਡਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਸਕੇਲ ਅਤੇ ਲੇਅਰ। ਸਧਾਰਣ ਸ਼ਬਦਾਂ ਵਿੱਚ, ਘੱਟ ਕੋਡ ਨਾਲ ਇੱਕਵਾਰੀ ਜਾਂ ਬਹੁਵਾਰੀ ਡਾਟੇ ਲਈ ਪਲਾਟਾਂ ਅਤੇ ਗ੍ਰਾਫਾਂ ਬਣਾਉਣ ਦੀ ਸਹੂਲਤ `ggplot2` ਨੂੰ R ਵਿੱਚ ਸਭ ਤੋਂ ਪ੍ਰਸਿੱਧ ਪੈਕੇਜ ਬਣਾਉਂਦੀ ਹੈ। ਯੂਜ਼ਰ `ggplot2` ਨੂੰ ਦੱਸਦਾ ਹੈ ਕਿ ਵੈਰੀਏਬਲਾਂ ਨੂੰ ਗ੍ਰਾਫਿਕਲ ਐਸਥੇਟਿਕਸ ਨਾਲ ਕਿਵੇਂ ਨਕਸ਼ਾ ਬਣਾਉਣਾ ਹੈ, ਕਿਹੜੇ ਗ੍ਰਾਫਿਕਲ ਪ੍ਰਿਮਿਟਿਵਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਨੀ ਹੈ, ਅਤੇ ਬਾਕੀ ਕੰਮ `ggplot2` ਕਰਦਾ ਹੈ।

> ✅ ਪਲਾਟ = ਡਾਟਾ + ਐਸਥੇਟਿਕਸ + ਜਿਓਮੈਟਰੀ  
> - ਡਾਟਾ ਡਾਟਾਸੈੱਟ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ  
> - ਐਸਥੇਟਿਕਸ ਉਹ ਵੈਰੀਏਬਲ ਹਨ ਜਿਨ੍ਹਾਂ ਦਾ ਅਧਿਐਨ ਕੀਤਾ ਜਾਣਾ ਹੈ (x ਅਤੇ y ਵੈਰੀਏਬਲ)  
> - ਜਿਓਮੈਟਰੀ ਪਲਾਟ ਦੀ ਕਿਸਮ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ (ਲਾਈਨ ਪਲਾਟ, ਬਾਰ ਪਲਾਟ, ਆਦਿ)  

ਆਪਣੇ ਡਾਟੇ ਅਤੇ ਕਹਾਣੀ ਦੇ ਅਨੁਸਾਰ ਸਭ ਤੋਂ ਵਧੀਆ ਜਿਓਮੈਟਰੀ (ਪਲਾਟ ਦੀ ਕਿਸਮ) ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਪਲਾਟ ਰਾਹੀਂ ਦੱਸਣਾ ਚਾਹੁੰਦੇ ਹੋ।  

> - ਰੁਝਾਨਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਲਈ: ਲਾਈਨ, ਕਾਲਮ  
> - ਮੁੱਲਾਂ ਦੀ ਤੁਲਨਾ ਕਰਨ ਲਈ: ਬਾਰ, ਕਾਲਮ, ਪਾਈ, ਸਕੈਟਰਪਲਾਟ  
> - ਪੂਰੇ ਨਾਲ ਹਿੱਸਿਆਂ ਦੇ ਸੰਬੰਧ ਦਿਖਾਉਣ ਲਈ: ਪਾਈ  
> - ਡਾਟੇ ਦੇ ਵੰਡਨ ਨੂੰ ਦਿਖਾਉਣ ਲਈ: ਸਕੈਟਰਪਲਾਟ, ਬਾਰ  
> - ਮੁੱਲਾਂ ਦੇ ਸੰਬੰਧ ਦਿਖਾਉਣ ਲਈ: ਲਾਈਨ, ਸਕੈਟਰਪਲਾਟ, ਬਬਲ  

✅ ਤੁਸੀਂ ਇਸ ਵੇਰਵੇਦਾਰ [ਚੀਟਸ਼ੀਟ](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) ਨੂੰ ਵੀ ਦੇਖ ਸਕਦੇ ਹੋ ਜੋ ggplot2 ਲਈ ਹੈ।

## ਪੰਖਾਂ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਲੰਬਾਈ ਬਾਰੇ ਲਾਈਨ ਪਲਾਟ ਬਣਾਓ

R ਕਨਸੋਲ ਖੋਲ੍ਹੋ ਅਤੇ ਡਾਟਾਸੈੱਟ ਇੰਪੋਰਟ ਕਰੋ।  
> ਨੋਟ: ਡਾਟਾਸੈੱਟ ਇਸ ਰਿਪੋ ਦੇ ਰੂਟ ਵਿੱਚ `/data` ਫੋਲਡਰ ਵਿੱਚ ਸਟੋਰ ਕੀਤਾ ਗਿਆ ਹੈ।

ਆਓ ਡਾਟਾਸੈੱਟ ਇੰਪੋਰਟ ਕਰੀਏ ਅਤੇ ਡਾਟੇ ਦੇ ਸਿਰਲੇਖ (ਪਹਿਲੀਆਂ 5 ਕਤਾਰਾਂ) ਨੂੰ ਦੇਖੀਏ।  

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
ਡਾਟੇ ਦੇ ਸਿਰਲੇਖ ਵਿੱਚ ਟੈਕਸਟ ਅਤੇ ਨੰਬਰਾਂ ਦਾ ਮਿਸ਼ਰਣ ਹੈ:  

|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

ਆਓ ਕੁਝ ਨੰਬਰਾਤਮਕ ਡਾਟੇ ਨੂੰ ਇੱਕ ਬੇਸਿਕ ਲਾਈਨ ਪਲਾਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪਲਾਟ ਕਰੀਏ। ਮੰਨੋ ਤੁਸੀਂ ਇਨ੍ਹਾਂ ਦਿਲਚਸਪ ਪੰਛੀਆਂ ਲਈ ਵੱਧ ਤੋਂ ਵੱਧ ਪੰਖਾਂ ਦੀ ਲੰਬਾਈ ਦੇਖਣਾ ਚਾਹੁੰਦੇ ਹੋ।  

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
ਇੱਥੇ, ਤੁਸੀਂ `ggplot2` ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰਦੇ ਹੋ ਅਤੇ ਫਿਰ ਇਸਨੂੰ `library("ggplot2")` ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵਰਕਸਪੇਸ ਵਿੱਚ ਇੰਪੋਰਟ ਕਰਦੇ ਹੋ। ggplot ਵਿੱਚ ਕੋਈ ਵੀ ਪਲਾਟ ਬਣਾਉਣ ਲਈ, `ggplot()` ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਅਤੇ ਤੁਸੀਂ ਡਾਟਾਸੈੱਟ, x ਅਤੇ y ਵੈਰੀਏਬਲਾਂ ਨੂੰ ਗੁਣਾਂ ਵਜੋਂ ਨਿਰਧਾਰਤ ਕਰਦੇ ਹੋ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ ਲਾਈਨ ਪਲਾਟ ਪਲਾਟ ਕਰਨ ਲਈ `geom_line()` ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਾਂ।  

![MaxWingspan-lineplot](../../../../../translated_images/pa/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)  

ਤੁਰੰਤ ਕੀ ਨਜ਼ਰ ਆਉਂਦਾ ਹੈ? ਘੱਟੋ-ਘੱਟ ਇੱਕ ਆਊਟਲਾਇਰ ਹੈ - ਇਹ ਕਾਫ਼ੀ ਵੱਡੀ ਪੰਖਾਂ ਦੀ ਲੰਬਾਈ ਹੈ! 2000+ ਸੈਂਟੀਮੀਟਰ ਪੰਖਾਂ ਦੀ ਲੰਬਾਈ 20 ਮੀਟਰ ਤੋਂ ਵੱਧ ਹੈ - ਕੀ ਮਿਨੇਸੋਟਾ ਵਿੱਚ ਪਟੇਰੋਡੈਕਟਿਲ ਉੱਡ ਰਹੇ ਹਨ? ਆਓ ਜਾਂਚ ਕਰੀਏ।  

ਜਦੋਂ ਤੁਸੀਂ Excel ਵਿੱਚ ਇੱਕ ਤੇਜ਼ ਸੌਰਟ ਕਰਕੇ ਉਹ ਆਊਟਲਾਇਰ ਲੱਭ ਸਕਦੇ ਹੋ, ਜੋ ਸ਼ਾਇਦ ਟਾਈਪੋਜ਼ ਹਨ, ਤਾਂ ਵੀ ਪਲਾਟ ਦੇ ਅੰਦਰੋਂ ਕੰਮ ਕਰਦੇ ਹੋਏ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ ਪ੍ਰਕਿਰਿਆ ਜਾਰੀ ਰੱਖੋ।  

x-ਐਕਸਿਸ 'ਤੇ ਲੇਬਲ ਸ਼ਾਮਲ ਕਰੋ ਤਾਂ ਜੋ ਇਹ ਦਿਖਾਇਆ ਜਾ ਸਕੇ ਕਿ ਕਿਹੜੇ ਪੰਛੀ ਗੱਲ ਵਿੱਚ ਹਨ:  

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
ਅਸੀਂ `theme` ਵਿੱਚ ਕੋਣ ਨਿਰਧਾਰਤ ਕਰਦੇ ਹਾਂ ਅਤੇ `xlab()` ਅਤੇ `ylab()` ਵਿੱਚ x ਅਤੇ y ਐਕਸਿਸ ਲੇਬਲ ਨਿਰਧਾਰਤ ਕਰਦੇ ਹਾਂ। `ggtitle()` ਗ੍ਰਾਫ/ਪਲਾਟ ਨੂੰ ਇੱਕ ਨਾਮ ਦਿੰਦਾ ਹੈ।  

![MaxWingspan-lineplot-improved](../../../../../translated_images/pa/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)  

45 ਡਿਗਰੀ 'ਤੇ ਲੇਬਲਾਂ ਦੇ ਰੋਟੇਸ਼ਨ ਦੇ ਨਾਲ ਵੀ, ਇਹ ਪੜ੍ਹਨ ਲਈ ਬਹੁਤ ਜ਼ਿਆਦਾ ਹਨ। ਆਓ ਇੱਕ ਵੱਖਰੀ ਰਣਨੀਤੀ ਅਪਣਾਈਏ: ਸਿਰਫ ਉਹ ਆਊਟਲਾਇਰ ਲੇਬਲ ਕਰੋ ਅਤੇ ਪਲਾਟ ਦੇ ਅੰਦਰ ਲੇਬਲ ਸੈੱਟ ਕਰੋ। ਤੁਸੀਂ ਲੇਬਲਿੰਗ ਲਈ ਹੋਰ ਜਗ੍ਹਾ ਬਣਾਉਣ ਲਈ ਇੱਕ ਸਕੈਟਰ ਚਾਰਟ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ:  

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
ਇੱਥੇ ਕੀ ਹੋ ਰਿਹਾ ਹੈ? ਤੁਸੀਂ `geom_point()` ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਕੈਟਰ ਪੌਇੰਟ ਪਲਾਟ ਕੀਤੇ। ਇਸ ਨਾਲ, ਤੁਸੀਂ ਉਹ ਪੰਛੀ ਲੇਬਲ ਕੀਤੇ ਜਿਨ੍ਹਾਂ ਦੀ `MaxWingspan > 500` ਸੀ ਅਤੇ ਪਲਾਟ ਨੂੰ ਕਲਟਰ-ਫ੍ਰੀ ਬਣਾਉਣ ਲਈ x ਐਕਸਿਸ ਦੇ ਲੇਬਲਾਂ ਨੂੰ ਛੁਪਾ ਦਿੱਤਾ।  

ਤੁਸੀਂ ਕੀ ਪਤਾ ਲਗਾਇਆ?  

![MaxWingspan-scatterplot](../../../../../translated_images/pa/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)  

## ਆਪਣੇ ਡਾਟੇ ਨੂੰ ਫਿਲਟਰ ਕਰੋ  

ਬਾਲਡ ਈਗਲ ਅਤੇ ਪ੍ਰੇਰੀ ਫਾਲਕਨ, ਜਦੋਂ ਕਿ ਸ਼ਾਇਦ ਬਹੁਤ ਵੱਡੇ ਪੰਛੀ ਹਨ, ਸ਼ਾਇਦ ਗਲਤ ਲੇਬਲ ਕੀਤੇ ਗਏ ਹਨ, ਉਨ੍ਹਾਂ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਪੰਖਾਂ ਦੀ ਲੰਬਾਈ ਵਿੱਚ ਇੱਕ ਵਾਧੂ 0 ਸ਼ਾਮਲ ਹੈ। ਇਹ ਸੰਭਵ ਨਹੀਂ ਹੈ ਕਿ ਤੁਸੀਂ 25 ਮੀਟਰ ਪੰਖਾਂ ਵਾਲੇ ਬਾਲਡ ਈਗਲ ਨੂੰ ਮਿਲੋਗੇ, ਪਰ ਜੇਕਰ ਮਿਲੇ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ ਸਾਨੂੰ ਦੱਸੋ! ਆਓ ਉਹ ਦੋ ਆਊਟਲਾਇਰਾਂ ਤੋਂ ਬਿਨਾਂ ਇੱਕ ਨਵਾਂ ਡਾਟਾਫਰੇਮ ਬਣਾਈਏ:  

```r
birds_filtered <- subset(birds, MaxWingspan < 500)

ggplot(data=birds_filtered, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  ylab("Wingspan (CM)") +
  xlab("Birds") +
  ggtitle("Max Wingspan in Centimeters") + 
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) +
  theme(axis.text.x=element_blank(), axis.ticks.x=element_blank())
```  
ਅਸੀਂ ਇੱਕ ਨਵਾਂ ਡਾਟਾਫਰੇਮ `birds_filtered` ਬਣਾਇਆ ਅਤੇ ਫਿਰ ਇੱਕ ਸਕੈਟਰ ਪਲਾਟ ਪਲਾਟ ਕੀਤਾ। ਆਊਟਲਾਇਰਾਂ ਨੂੰ ਫਿਲਟਰ ਕਰਕੇ, ਹੁਣ ਤੁਹਾਡਾ ਡਾਟਾ ਹੋਰ ਸੰਗਠਿਤ ਅਤੇ ਸਮਝਣਯੋਗ ਹੈ।  

![MaxWingspan-scatterplot-improved](../../../../../translated_images/pa/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)  

ਹੁਣ ਜਦੋਂ ਸਾਡੇ ਕੋਲ ਪੰਖਾਂ ਦੀ ਲੰਬਾਈ ਦੇ ਹਿਸਾਬ ਨਾਲ ਘੱਟੋ-ਘੱਟ ਇੱਕ ਸਾਫ ਡਾਟਾਸੈੱਟ ਹੈ, ਆਓ ਇਨ੍ਹਾਂ ਪੰਛੀਆਂ ਬਾਰੇ ਹੋਰ ਪਤਾ ਲਗਾਈਏ।  

ਲਾਈਨ ਅਤੇ ਸਕੈਟਰ ਪਲਾਟ ਡਾਟੇ ਦੇ ਮੁੱਲਾਂ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਵੰਡਨ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦਿਖਾ ਸਕਦੇ ਹਨ, ਪਰ ਅਸੀਂ ਇਸ ਡਾਟਾਸੈੱਟ ਵਿੱਚ ਮੌਜੂਦ ਮੁੱਲਾਂ ਬਾਰੇ ਸੋਚਣਾ ਚਾਹੁੰਦੇ ਹਾਂ। ਤੁਸੀਂ ਮਾਤਰਾ ਬਾਰੇ ਹੇਠਾਂ ਦਿੱਤੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦੇਣ ਲਈ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ ਬਣਾ ਸਕਦੇ ਹੋ:  

> ਕਿੰਨੀਆਂ ਸ਼੍ਰੇਣੀਆਂ ਦੇ ਪੰਛੀ ਹਨ, ਅਤੇ ਉਨ੍ਹਾਂ ਦੀ ਗਿਣਤੀ ਕੀ ਹੈ?  
> ਕਿੰਨੇ ਪੰਛੀ ਲੁਪਤ, ਖਤਰੇ ਵਿੱਚ, ਦੁਲਭ ਜਾਂ ਆਮ ਹਨ?  
> ਲਿਨੇਅਸ ਦੀ ਟਰਮੀਨੋਲੋਜੀ ਦੇ ਅਨੁਸਾਰ ਵੱਖ-ਵੱਖ ਜਨਸ ਅਤੇ ਆਰਡਰਾਂ ਦੇ ਕਿੰਨੇ ਹਨ?  

## ਬਾਰ ਚਾਰਟਾਂ ਦੀ ਖੋਜ ਕਰੋ  

ਜਦੋਂ ਤੁਹਾਨੂੰ ਡਾਟੇ ਦੇ ਸਮੂਹ ਦਿਖਾਉਣ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ, ਤਾਂ ਬਾਰ ਚਾਰਟ ਬਹੁਤ ਹੀ ਲਾਭਦਾਇਕ ਹੁੰਦੇ ਹਨ। ਆਓ ਇਸ ਡਾਟਾਸੈੱਟ ਵਿੱਚ ਮੌਜੂਦ ਪੰਛੀਆਂ ਦੀਆਂ ਸ਼੍ਰੇਣੀਆਂ ਦੀ ਖੋਜ ਕਰੀਏ ਤਾਂ ਜੋ ਇਹ ਦੇਖਿਆ ਜਾ ਸਕੇ ਕਿ ਕਿਹੜੀ ਸ਼੍ਰੇਣੀ ਸਭ ਤੋਂ ਆਮ ਹੈ।  
ਆਓ ਫਿਲਟਰ ਕੀਤੇ ਡਾਟੇ 'ਤੇ ਇੱਕ ਬਾਰ ਚਾਰਟ ਬਣਾਈਏ।  

```r
install.packages("dplyr")
install.packages("tidyverse")

library(lubridate)
library(scales)
library(dplyr)
library(ggplot2)
library(tidyverse)

birds_filtered %>% group_by(Category) %>%
  summarise(n=n(),
  MinLength = mean(MinLength),
  MaxLength = mean(MaxLength),
  MinBodyMass = mean(MinBodyMass),
  MaxBodyMass = mean(MaxBodyMass),
  MinWingspan=mean(MinWingspan),
  MaxWingspan=mean(MaxWingspan)) %>% 
  gather("key", "value", - c(Category, n)) %>%
  ggplot(aes(x = Category, y = value, group = key, fill = key)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#D62728", "#FF7F0E", "#8C564B","#2CA02C", "#1F77B4", "#9467BD")) +                   
  xlab("Category")+ggtitle("Birds of Minnesota")

```  
ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ, ਅਸੀਂ [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) ਅਤੇ [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) ਪੈਕੇਜਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰਦੇ ਹਾਂ ਜੋ ਡਾਟੇ ਨੂੰ ਮੈਨਿਪੂਲੇਟ ਅਤੇ ਗਰੁੱਪ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ ਤਾਂ ਜੋ ਇੱਕ ਸਟੈਕਡ ਬਾਰ ਚਾਰਟ ਪਲਾਟ ਕੀਤਾ ਜਾ ਸਕੇ। ਪਹਿਲਾਂ, ਤੁਸੀਂ ਡਾਟੇ ਨੂੰ ਪੰਛੀ ਦੀ `Category` ਦੇ ਅਨੁਸਾਰ ਗਰੁੱਪ ਕਰਦੇ ਹੋ ਅਤੇ ਫਿਰ `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan` ਕਾਲਮਾਂ ਨੂੰ ਸੰਖੇਪ ਕਰਦੇ ਹੋ। ਫਿਰ, `ggplot2` ਪੈਕੇਜ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬਾਰ ਚਾਰਟ ਪਲਾਟ ਕਰੋ ਅਤੇ ਵੱਖ-ਵੱਖ ਸ਼੍ਰੇਣੀਆਂ ਲਈ ਰੰਗ ਅਤੇ ਲੇਬਲ ਨਿਰਧਾਰਤ ਕਰੋ।  

![Stacked bar chart](../../../../../translated_images/pa/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)  

ਹਾਲਾਂਕਿ, ਇਹ ਬਾਰ ਚਾਰਟ ਪੜ੍ਹਨ ਯੋਗ ਨਹੀਂ ਹੈ ਕਿਉਂਕਿ ਬਹੁਤ ਸਾਰਾ ਗੈਰ-ਗਰੁੱਪ ਕੀਤਾ ਡਾਟਾ ਹੈ। ਤੁਹਾਨੂੰ ਸਿਰਫ ਉਹ ਡਾਟਾ ਚੁਣਨ ਦੀ ਲੋੜ ਹੈ ਜੋ ਤੁਸੀਂ ਪਲਾਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਇਸ ਲਈ ਆਓ ਪੰਛੀ ਦੀ ਸ਼੍ਰੇਣੀ ਦੇ ਆਧਾਰ 'ਤੇ ਪੰਛੀਆਂ ਦੀ ਲੰਬਾਈ ਦੇਖੀਏ।  

ਆਪਣੇ ਡਾਟੇ ਨੂੰ ਸਿਰਫ ਪੰਛੀ ਦੀ ਸ਼੍ਰੇਣੀ ਸ਼ਾਮਲ ਕਰਨ ਲਈ ਫਿਲਟਰ ਕਰੋ।  

ਕਿਉਂਕਿ ਬਹੁਤ ਸਾਰੀਆਂ ਸ਼੍ਰੇਣੀਆਂ ਹਨ, ਤੁਸੀਂ ਇਸ ਚਾਰਟ ਨੂੰ ਖੜ੍ਹੇ ਰੂਪ ਵਿੱਚ ਦਿਖਾ ਸਕਦੇ ਹੋ ਅਤੇ ਸਾਰੇ ਡਾਟੇ ਨੂੰ ਸਮਾਉਣ ਲਈ ਇਸ ਦੀ ਉਚਾਈ ਨੂੰ ਠੀਕ ਕਰ ਸਕਦੇ ਹੋ:  

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
ਤੁਸੀਂ `Category` ਕਾਲਮ ਵਿੱਚ ਵਿਲੱਖਣ ਮੁੱਲਾਂ ਦੀ ਗਿਣਤੀ ਕਰਦੇ ਹੋ ਅਤੇ ਫਿਰ ਉਨ੍ਹਾਂ ਨੂੰ ਇੱਕ ਨਵੇਂ ਡਾਟਾਫਰੇਮ `birds_count` ਵਿੱਚ ਸੌਰਟ ਕਰਦੇ ਹੋ। ਇਹ ਸੌਰਟ ਕੀਤਾ ਡਾਟਾ ਫਿਰ ਇੱਕੋ ਪੱਧਰ 'ਤੇ ਫੈਕਟਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਤਾਂ ਜੋ ਇਹ ਸੌਰਟ ਕੀਤੇ ਤਰੀਕੇ ਨਾਲ ਪਲਾਟ ਕੀਤਾ ਜਾ ਸਕੇ। `ggplot2` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤੁਸੀਂ ਫਿਰ ਡਾਟੇ ਨੂੰ ਇੱਕ ਬਾਰ ਚਾਰਟ ਵਿੱਚ ਪਲਾਟ ਕਰਦੇ ਹੋ। `coord_flip()` ਖੜ੍ਹੇ ਬਾਰ ਪਲਾਟ ਕਰਦਾ ਹੈ।  

![category-length](../../../../../translated_images/pa/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)  

ਇਹ ਬਾਰ ਚਾਰਟ

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।