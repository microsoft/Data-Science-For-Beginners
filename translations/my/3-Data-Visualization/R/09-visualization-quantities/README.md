<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-30T18:45:47+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "my"
}
-->
# အရေအတွက်များကိုမြင်နိုင်အောင်ဖော်ပြခြင်း
|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| အရေအတွက်များကိုမြင်နိုင်အောင်ဖော်ပြခြင်း - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

ဒီသင်ခန်းစာမှာ R package library အမျိုးမျိုးကိုအသုံးပြုပြီး အရေအတွက်ဆိုင်ရာအကြောင်းအရာများကို စိတ်ဝင်စားဖွယ်မြင်နိုင်အောင် ဖော်ပြပုံများဖန်တီးနည်းကိုလေ့လာပါမည်။ Minnesota ရှိငှက်များအကြောင်းကို စစ်ဆေးပြီးသား dataset ကိုအသုံးပြုကာ ဒေသတွင်းတောရိုင်းတိရစ္ဆာန်များအကြောင်း စိတ်ဝင်စားဖွယ်အချက်အလက်များကိုလေ့လာနိုင်ပါသည်။

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## ggplot2 ဖြင့်တောင်ပံအကျယ်ကိုကြည့်ရှုခြင်း
အမျိုးမျိုးသောရုပ်ပုံများနှင့်ဇယားများကို ရိုးရှင်းပြီးခက်ခဲသောပုံစံများဖြင့်ဖန်တီးရန်အကောင်းဆုံး library တစ်ခုမှာ [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html) ဖြစ်သည်။ အထွေထွေအားဖြင့်၊ ဒီ library များကိုအသုံးပြု၍ ဒေတာကို plot လုပ်ခြင်း၏လုပ်ငန်းစဉ်မှာ dataframe ၏တစ်စိတ်တစ်ပိုင်းကို ရွေးချယ်ခြင်း၊ လိုအပ်သောဒေတာကိုပြောင်းလဲခြင်း၊ x နှင့် y axis တန်ဖိုးများကိုသတ်မှတ်ခြင်း၊ ဖော်ပြလိုသော plot အမျိုးအစားကိုဆုံးဖြတ်ခြင်းနှင့် plot ကိုဖော်ပြခြင်းတို့ပါဝင်သည်။

`ggplot2` သည် The Grammar of Graphics အခြေခံ၍ ရုပ်ပုံများကို ဖန်တီးရန်အတွက် declarative system တစ်ခုဖြစ်သည်။ [Grammar of Graphics](https://en.wikipedia.org/wiki/Ggplot2) သည် ရုပ်ပုံများကို semantic components (scales နှင့် layers) အဖြစ်ခွဲခြားသော ဒေတာ visualization အတွက်အထွေထွေစနစ်တစ်ခုဖြစ်သည်။ အခြေခံကုဒ်နည်းနည်းဖြင့် univariate ဒေတာ သို့မဟုတ် multivariate ဒေတာများအတွက် ရုပ်ပုံများနှင့်ဇယားများဖန်တီးရန်ရိုးရှင်းမှုကြောင့် `ggplot2` သည် R တွင် visualization အတွက်အသုံးပြုမှုအများဆုံး package ဖြစ်သည်။ အသုံးပြုသူသည် `ggplot2` ကို variable များကို aesthetics နှင့် graphical primitives များကိုဘယ်လို map လုပ်မည်ကိုပြောပြပြီး `ggplot2` သည်ကျန်ရှိသောအရာများကိုစီမံဆောင်ရွက်သည်။

> ✅ Plot = Data + Aesthetics + Geometry  
> - Data သည် dataset ကိုဆိုလိုသည်  
> - Aesthetics သည်လေ့လာလိုသော variable များကိုပြသည် (x နှင့် y variable များ)  
> - Geometry သည် plot အမျိုးအစားကိုဆိုလိုသည် (line plot, bar plot စသည်)  

သင့်ဒေတာနှင့် plot မှတဆင့်ပြောပြလိုသောအကြောင်းအရာအပေါ်မူတည်၍ အကောင်းဆုံး geometry (plot အမျိုးအစား) ကိုရွေးချယ်ပါ။

> - အလားအလာများကိုခွဲခြားရန်: line, column  
> - တန်ဖိုးများကိုနှိုင်းယှဉ်ရန်: bar, column, pie, scatterplot  
> - အစိတ်အပိုင်းများသည်တစ်ခုလုံးနှင့်ဆက်စပ်ပုံကိုပြရန်: pie  
> - ဒေတာ၏ဖြန့်ဝေမှုကိုပြရန်: scatterplot, bar  
> - တန်ဖိုးများအကြားဆက်နွယ်မှုကိုပြရန်: line, scatterplot, bubble  

✅ [cheatsheet](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) ရှိ ggplot2 အတွက်ဖော်ပြချက်ကိုလည်းကြည့်ရှုနိုင်ပါသည်။

## ငှက်တောင်ပံအကျယ်တန်ဖိုးများအတွက် line plot တစ်ခုဖန်တီးပါ

R console ကိုဖွင့်ပြီး dataset ကို import လုပ်ပါ။  
> Note: Dataset သည် repo ၏ root တွင် `/data` folder တွင်သိမ်းဆည်းထားသည်။

Dataset ကို import လုပ်ပြီး ဒေတာ၏အပေါ်ဆုံး ၅ ရွေ့ကိုကြည့်ရှုပါ။

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
ဒေတာ၏အပေါ်ဆုံးတွင် text နှင့် number များရောနှောထားသည်-

|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

အထူးစိတ်ဝင်စားဖွယ်ရှိသောငှက်များအတွက် maximum wingspan ကိုကြည့်ရှုလိုပါက numeric data အချို့ကို basic line plot ဖြင့်စတင် plot လုပ်ပါ။

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
ဒီမှာ `ggplot2` package ကို install လုပ်ပြီး `library("ggplot2")` command ကိုအသုံးပြုကာ workspace ထဲသို့ import လုပ်ပါသည်။ ggplot တွင် plot တစ်ခုကိုဖော်ပြရန် `ggplot()` function ကိုအသုံးပြုပြီး dataset, x နှင့် y variable များကို attribute အဖြစ်သတ်မှတ်ပါသည်။ ဒီအခါမှာ line plot ကို plot လုပ်ရန် `geom_line()` function ကိုအသုံးပြုပါသည်။

![MaxWingspan-lineplot](../../../../../translated_images/my/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

သင်ဘာတွေသတိထားမိပါသလဲ? အနည်းဆုံး outlier တစ်ခုရှိသလိုပဲ - တောင်ပံအကျယ်တစ်ခုကတော်တော်လေးကြီးတယ်! 2000+ စင်တီမီတာတောင်ပံအကျယ်က 20 မီတာကျော်ရှိတယ် - Minnesota မှာ Pterodactyls တွေရှိနေသလား? စစ်ဆေးကြည့်ရအောင်။

Excel မှာ sort လုပ်ပြီး outlier များကိုရှာဖွေနိုင်သော်လည်း၊ plot ထဲကနေဆက်လက် visualization လုပ်ပါ။

x-axis မှာငှက်အမျိုးအစားများကိုပြရန် label များထည့်ပါ:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
`theme` မှာ angle ကိုသတ်မှတ်ပြီး `xlab()` နှင့် `ylab()` မှာ x နှင့် y axis label များကိုသတ်မှတ်ပါသည်။ `ggtitle()` သည် graph/plot ကိုနာမည်ပေးသည်။

![MaxWingspan-lineplot-improved](../../../../../translated_images/my/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

label များကို 45 ဒီဂရီလှည့်ထားသော်လည်း၊ ဖတ်ရန်အလွန်များနေသည်။ အခြား strategy တစ်ခုကိုစမ်းကြည့်ရအောင်- outlier များကိုသာ label လုပ်ပြီး label များကို chart ထဲမှာထားပါ။ scatter chart ကိုအသုံးပြုကာ label များအတွက်နေရာပိုမိုရရှိစေပါ:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
ဒီမှာဘာတွေဖြစ်နေပါသလဲ? `geom_point()` function ကိုအသုံးပြုကာ scatter point များကို plot လုပ်ပါသည်။ ဒီနဲ့အတူ `MaxWingspan > 500` ရှိသောငှက်များအတွက် label များထည့်ပြီး x axis မှ label များကိုဖယ်ရှားကာ plot ကိုရှင်းလင်းစေပါသည်။

သင်ဘာတွေရှာဖွေတွေ့ရှိပါသလဲ?

![MaxWingspan-scatterplot](../../../../../translated_images/my/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## သင့်ဒေတာကို filter လုပ်ပါ

Bald Eagle နှင့် Prairie Falcon သည် အလွန်ကြီးမားသောငှက်များဖြစ်နိုင်သော်လည်း၊ maximum wingspan တွင် 0 တစ်ခုထပ်ထည့်ထားသောအမှားဖြစ်နိုင်သည်။ Bald Eagle တစ်ကောင်မှာ 25 မီတာတောင်ပံအကျယ်ရှိမည်မဟုတ်သော်လည်း၊ ရှိပါက ကျွန်ုပ်တို့ကိုသတင်းပို့ပါ! ဒီ outlier ၂ ခုမပါသော dataframe အသစ်တစ်ခုကိုဖန်တီးပါ:

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
`birds_filtered` ဆိုသော dataframe အသစ်တစ်ခုကိုဖန်တီးပြီး scatter plot တစ်ခုကို plot လုပ်ပါသည်။ outlier များကို filter လုပ်ခြင်းဖြင့် သင့်ဒေတာသည် ပိုမိုညီညွတ်ပြီးနားလည်ရလွယ်ကူလာသည်။

![MaxWingspan-scatterplot-improved](../../../../../translated_images/my/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

အနည်းဆုံးတောင်ပံအကျယ်အရ dataset ကိုရှင်းလင်းပြီးနောက်၊ ငှက်များအကြောင်းပိုမိုရှာဖွေကြည့်ရအောင်။

line နှင့် scatter plot များသည် ဒေတာတန်ဖိုးများနှင့်၎င်းတို့၏ဖြန့်ဝေမှုကိုဖော်ပြနိုင်သော်လည်း၊ dataset ၏ inherent values အကြောင်းကိုစဉ်းစားလိုပါသည်။ အရေအတွက်ဆိုင်ရာအောက်ပါမေးခွန်းများကိုဖြေရှင်းရန် visualization များဖန်တီးနိုင်သည်-

> ငှက်အမျိုးအစားများဘယ်လောက်ရှိပြီး၊ အရေအတွက်ဘယ်လောက်ရှိသလဲ?  
> ငှက်များအနက်ဘယ်လောက် extinction, endangered, rare, သို့မဟုတ် common ဖြစ်သလဲ?  
> Linnaeus ရဲ့ terminology အရ genus နှင့် order များဘယ်လောက်ရှိသလဲ?  

## Bar chart များကိုလေ့လာပါ

Bar chart များသည် ဒေတာကိုအုပ်စုဖွဲ့ရန်လိုအပ်သောအခါတွင်အသုံးဝင်သည်။ dataset တွင်ရှိသောငှက်အမျိုးအစားများကိုလေ့လာပြီး အများဆုံးရှိသောအမျိုးအစားကိုကြည့်ရှုပါ။ Filter လုပ်ထားသောဒေတာပေါ်တွင် bar chart တစ်ခုဖန်တီးပါ။

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
ဒီ snippet တွင် [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) နှင့် [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) package များကို install လုပ်ကာ ဒေတာကို manipulate လုပ်ရန်နှင့် group လုပ်ရန်အသုံးပြုသည်။ ငှက်၏ `Category` အပေါ်မူတည်၍ ဒေတာကို group လုပ်ပြီး `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan` column များကို summarise လုပ်သည်။ ထို့နောက် `ggplot2` package ကိုအသုံးပြုကာ bar chart ကို plot လုပ်ပြီး category များအတွက်အရောင်များနှင့် label များကိုသတ်မှတ်သည်။

![Stacked bar chart](../../../../../translated_images/my/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

ဒီ bar chart သည် များလွန်းသော non-grouped data ကြောင့် မဖတ်နိုင်ပါ။ plot လုပ်လိုသောဒေတာကိုသာရွေးချယ်ရန်လိုအပ်သည်၊ ဒါကြောင့် ငှက်၏ category အပေါ်မူတည်၍ length ကိုကြည့်ရှုပါ။

သင့်ဒေတာကို ငှက်၏ category ကိုသာပါဝင်အောင် filter လုပ်ပါ။

Category များများသောကြောင့်၊ ဒီ chart ကိုvertically ဖော်ပြပြီး data အားလုံးအတွက် height ကိုပြင်ဆင်ပါ:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
`Category` column တွင်ရှိသော unique value များကို count လုပ်ပြီး `birds_count` ဆိုသော dataframe အသစ်တစ်ခုထဲသို့ sort လုပ်သည်။ ဒီ sorted data ကို level တူညီအတိုင်း factor လုပ်ကာ sorted ပုံစံဖြင့် plot လုပ်သည်။ `ggplot2` ကိုအသုံးပြုကာ bar chart ကို plot လုပ်သည်။ `coord_flip()` သည် horizontal bar များကို plot လုပ်သည်။

![category-length](../../../../../translated_images/my/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

ဒီ bar chart သည် category တစ်ခုစီတွင်ရှိသောငှက်အရေအတွက်ကိုကောင်းစွာမြင်နိုင်စေသည်။ Minnesota တွင် Ducks/Geese/Waterfowl category တွင်ငှက်အများဆုံးရှိသည်ကို တစ်ချက်ကြည့်လိုက်တာနဲ့မြင်နိုင်သည်။ Minnesota သည် '10,000 ရေကန်များ၏မြေ' ဖြစ်သောကြောင့်၊ ဒီအရာသည်အံ့ဩစရာမဟုတ်ပါ။

✅ ဒီ dataset ပေါ်မှာ count အမျိုးမျိုးကိုစမ်းကြည့်ပါ။ သင်အံ့ဩစရာတွေ့ရှိပါသလား?

## ဒေတာကိုနှိုင်းယှဉ်ခြင်း

Grouped data များကိုနှိုင်းယှဉ်ရန် axis အသစ်များဖန်တီးကာစမ်းကြည့်နိုင်သည်။ ငှက်၏ category အပေါ်မူတည်၍ MaxLength ကိုနှိုင်းယှဉ်ကြည့်ပါ:

```r
birds_grouped <- birds_filtered %>%
  group_by(Category) %>%
  summarise(
  MaxLength = max(MaxLength, na.rm = T),
  MinLength = max(MinLength, na.rm = T)
           ) %>%
  arrange(Category)
  
ggplot(birds_grouped,aes(Category,MaxLength))+geom_bar(stat="identity")+coord_flip()
```  
`birds_filtered` ဒေတာကို `Category` အပေါ်မူတည်၍ group လုပ်ပြီး bar graph ကို plot လုပ်သည်။

![comparing data](../../../../../translated_images/my/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

ဒီမှာအံ့ဩစရာမရှိပါ- hummingbirds တွင် Pelicans သို့မဟုတ် Geese နှင့်နှိုင်းယှဉ်ပါက MaxLength အနည်းဆုံးရှိသည်။ ဒေတာသည် logical make sense ဖြစ်သည်မှာကောင်းပါသည်!

Bar chart များကို data များကို superimpose လုပ်ကာပိုမိုစိတ်ဝင်စားဖွယ်ဖန်တီးနိုင်သည်။ Minimum နှင့် Maximum Length ကိုငှက် category တစ်ခုစီပေါ်မှာ superimpose လုပ်ကြည့်ရအောင်:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../translated_images/my/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 စိန်ခေါ်မှု

ဒီငှက် dataset သည် ecosystem တစ်ခုအတွင်းရှိငှက်အမျိုးအစားများအကြောင်းအချက်အလက်များစွာကိုပေးသည်။ အင်တာနက်ပေါ်တွင်ရှာဖွေပြီး ငှက်များနှင့်ဆက်စပ်သော dataset အခြားများကိုရှာဖွေကြည့်ပါ။ ငှက်များအကြောင်း သင်မသိခဲ့သောအချက်အလက်များကိုရှာဖွေဖော်ထုတ်ရန် chart များနှင့် graph များကိုဖန်တီးရန်လေ့ကျင့်ပါ။

## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## ပြန်လည်သုံးသပ်ခြင်းနှင့်ကိုယ်တိုင်လေ့လာခြင်း

ဒီပထမဆုံးသင်ခန်းစာသည် `ggplot2` ကိုအသုံးပြုကာ အရေအတွက်များကို visualization လုပ်နည်းအကြောင်းအချက်အလက်အချို့ကိုပေးသည်။ dataset များကို visualization လုပ်ရန်အခြားနည်းလမ်းများအကြောင်းလေ့လာပါ။ [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) နှင့် [Plotly](https://github.com/plotly/plotly.R#readme) ကဲ့သို့သော package များကိုအသုံးပြု

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် ရှုယူသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။