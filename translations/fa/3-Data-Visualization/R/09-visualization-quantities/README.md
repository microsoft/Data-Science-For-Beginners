<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-24T01:17:31+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "fa"
}
-->
# تجسم مقادیر

|![طرح دستی توسط [(@sketchthedocs)](https://sketchthedocs.dev)](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| تجسم مقادیر - _طرح دستی توسط [@nitya](https://twitter.com/nitya)_ |

در این درس، شما یاد خواهید گرفت که چگونه از برخی از کتابخانه‌های موجود در بسته‌های R برای ایجاد تجسم‌های جذاب پیرامون مفهوم مقدار استفاده کنید. با استفاده از یک مجموعه داده پاک شده درباره پرندگان مینه‌سوتا، می‌توانید حقایق جالبی درباره حیات وحش محلی یاد بگیرید.

## [آزمون پیش از درس](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## مشاهده طول بال‌ها با ggplot2

یک کتابخانه عالی برای ایجاد نمودارها و چارت‌های ساده و پیچیده از انواع مختلف، [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html) است. به طور کلی، فرآیند رسم داده‌ها با استفاده از این کتابخانه‌ها شامل شناسایی بخش‌های مورد نظر از دیتافریم، انجام هرگونه تبدیل لازم بر روی داده‌ها، اختصاص مقادیر محور x و y، تصمیم‌گیری درباره نوع نمودار و سپس نمایش نمودار است.

`ggplot2` یک سیستم برای ایجاد گرافیک به صورت اعلامی است که بر اساس دستور زبان گرافیک طراحی شده است. [دستور زبان گرافیک](https://en.wikipedia.org/wiki/Ggplot2) یک طرح کلی برای تجسم داده‌ها است که نمودارها را به اجزای معنایی مانند مقیاس‌ها و لایه‌ها تقسیم می‌کند. به عبارت دیگر، سهولت ایجاد نمودارها و گراف‌ها برای داده‌های تک‌متغیره یا چندمتغیره با کد کم، `ggplot2` را به محبوب‌ترین بسته برای تجسم داده‌ها در R تبدیل کرده است. کاربر به `ggplot2` می‌گوید که چگونه متغیرها را به زیبایی‌شناسی‌ها نگاشت کند، از کدام عناصر گرافیکی استفاده کند، و `ggplot2` بقیه کارها را انجام می‌دهد.

> ✅ نمودار = داده + زیبایی‌شناسی + هندسه  
> - داده به مجموعه داده اشاره دارد  
> - زیبایی‌شناسی متغیرهایی را که باید بررسی شوند نشان می‌دهد (متغیرهای x و y)  
> - هندسه نوع نمودار را مشخص می‌کند (نمودار خطی، نمودار میله‌ای و غیره)  

هندسه مناسب (نوع نمودار) را بر اساس داده‌های خود و داستانی که می‌خواهید از طریق نمودار بیان کنید، انتخاب کنید.

> - برای تحلیل روندها: خطی، ستونی  
> - برای مقایسه مقادیر: میله‌ای، ستونی، دایره‌ای، پراکندگی  
> - برای نشان دادن ارتباط بخش‌ها با کل: دایره‌ای  
> - برای نشان دادن توزیع داده‌ها: پراکندگی، میله‌ای  
> - برای نشان دادن روابط بین مقادیر: خطی، پراکندگی، حبابی  

✅ همچنین می‌توانید این [برگه تقلب توصیفی](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) برای ggplot2 را بررسی کنید.

## ایجاد نمودار خطی درباره مقادیر طول بال پرندگان

کنسول R را باز کنید و مجموعه داده را وارد کنید.  
> توجه: مجموعه داده در ریشه این مخزن در پوشه `/data` ذخیره شده است.

بیایید مجموعه داده را وارد کنیم و سر (پنج ردیف اول) داده‌ها را مشاهده کنیم.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
سر داده‌ها ترکیبی از متن و اعداد دارد:

|      | نام                          | نام علمی                | دسته‌بندی              | راسته        | خانواده   | جنس        | وضعیت حفاظتی         | حداقل طول | حداکثر طول | حداقل وزن بدن | حداکثر وزن بدن | حداقل طول بال | حداکثر طول بال |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | اردک سوت‌زن شکم‌سیاه         | Dendrocygna autumnalis | اردک‌ها/غازها/آبزیان  | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | اردک سوت‌زن قهوه‌ای          | Dendrocygna bicolor    | اردک‌ها/غازها/آبزیان  | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | غاز برفی                     | Anser caerulescens     | اردک‌ها/غازها/آبزیان  | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | غاز راس                      | Anser rossii           | اردک‌ها/غازها/آبزیان  | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | غاز پیشانی‌سفید بزرگ         | Anser albifrons        | اردک‌ها/غازها/آبزیان  | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

بیایید با رسم برخی از داده‌های عددی با استفاده از یک نمودار خطی ساده شروع کنیم. فرض کنید می‌خواهید نمایی از حداکثر طول بال این پرندگان جالب داشته باشید.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
در اینجا، بسته `ggplot2` را نصب کرده و سپس با استفاده از دستور `library("ggplot2")` آن را وارد فضای کاری می‌کنید. برای رسم هر نمودار در ggplot، از تابع `ggplot()` استفاده می‌شود و شما مجموعه داده، متغیرهای x و y را به عنوان ویژگی‌ها مشخص می‌کنید. در این مورد، از تابع `geom_line()` استفاده می‌کنیم زیرا هدف ما رسم نمودار خطی است.

![MaxWingspan-lineplot](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-lineplot.png)

چه چیزی بلافاصله توجه شما را جلب می‌کند؟ به نظر می‌رسد حداقل یک مقدار پرت وجود دارد - این طول بال واقعاً چشمگیر است! طول بال بیش از 2000 سانتی‌متر برابر با بیش از 20 متر است - آیا دایناسورهای پرنده در مینه‌سوتا پرسه می‌زنند؟ بیایید بررسی کنیم.

در حالی که می‌توانید با یک مرتب‌سازی سریع در اکسل این مقادیر پرت را پیدا کنید، بهتر است فرآیند تجسم را از داخل نمودار ادامه دهید.

به محور x برچسب‌هایی اضافه کنید تا نشان دهید چه نوع پرندگانی مورد بررسی قرار گرفته‌اند:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
ما زاویه را در `theme` مشخص می‌کنیم و برچسب‌های محور x و y را در `xlab()` و `ylab()` به ترتیب مشخص می‌کنیم. `ggtitle()` نامی به نمودار/چارت می‌دهد.

![MaxWingspan-lineplot-improved](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-lineplot-improved.png)

حتی با چرخش برچسب‌ها به زاویه 45 درجه، تعداد زیادی برچسب وجود دارد که خواندن آن‌ها دشوار است. بیایید استراتژی دیگری را امتحان کنیم: فقط مقادیر پرت را برچسب‌گذاری کنیم و برچسب‌ها را در داخل نمودار قرار دهیم. می‌توانید از نمودار پراکندگی استفاده کنید تا فضای بیشتری برای برچسب‌گذاری ایجاد کنید:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
چه اتفاقی افتاده است؟ شما از تابع `geom_point()` برای رسم نقاط پراکندگی استفاده کردید. با این کار، برچسب‌هایی برای پرندگانی که `MaxWingspan > 500` داشتند اضافه کردید و همچنین برچسب‌های محور x را برای کاهش شلوغی نمودار پنهان کردید.

چه چیزی کشف می‌کنید؟

![MaxWingspan-scatterplot](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-scatterplot.png)

## فیلتر کردن داده‌ها

هم عقاب سرسفید و هم شاهین دشتی، در حالی که احتمالاً پرندگان بسیار بزرگی هستند، به نظر می‌رسد اشتباه برچسب‌گذاری شده‌اند و یک صفر اضافی به طول بال حداکثر آن‌ها اضافه شده است. بعید است که با عقاب سرسفیدی با طول بال 25 متر روبرو شوید، اما اگر چنین شد، لطفاً به ما اطلاع دهید! بیایید یک دیتافریم جدید بدون این دو مقدار پرت ایجاد کنیم:

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
ما یک دیتافریم جدید به نام `birds_filtered` ایجاد کردیم و سپس نمودار پراکندگی رسم کردیم. با حذف مقادیر پرت، داده‌های شما اکنون منسجم‌تر و قابل فهم‌تر شده‌اند.

![MaxWingspan-scatterplot-improved](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-scatterplot-improved.png)

حالا که مجموعه داده‌ای تمیزتر داریم، حداقل از نظر طول بال، بیایید اطلاعات بیشتری درباره این پرندگان کشف کنیم.

در حالی که نمودارهای خطی و پراکندگی می‌توانند اطلاعاتی درباره مقادیر داده‌ها و توزیع آن‌ها نمایش دهند، ما می‌خواهیم درباره مقادیر ذاتی این مجموعه داده فکر کنیم. شما می‌توانید تجسم‌هایی ایجاد کنید تا به سوالات زیر درباره مقدار پاسخ دهید:

> چند دسته از پرندگان وجود دارد و تعداد آن‌ها چقدر است؟  
> چند پرنده منقرض، در معرض خطر، نادر یا معمولی هستند؟  
> چند پرنده از جنس‌ها و راسته‌های مختلف در اصطلاحات لینائوس وجود دارند؟  

## بررسی نمودارهای میله‌ای

نمودارهای میله‌ای زمانی کاربردی هستند که نیاز به نمایش گروه‌بندی داده‌ها دارید. بیایید دسته‌بندی‌های پرندگان موجود در این مجموعه داده را بررسی کنیم تا ببینیم کدام دسته بیشترین تعداد را دارد.  
بیایید یک نمودار میله‌ای بر اساس داده‌های فیلتر شده ایجاد کنیم.

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
در قطعه کد زیر، بسته‌های [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) و [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) را نصب می‌کنیم تا به دستکاری و گروه‌بندی داده‌ها برای رسم نمودار میله‌ای انباشته کمک کنیم. ابتدا داده‌ها را بر اساس `Category` پرنده گروه‌بندی کرده و سپس ستون‌های `MinLength`، `MaxLength`، `MinBodyMass`، `MaxBodyMass`، `MinWingspan`، `MaxWingspan` را خلاصه می‌کنیم. سپس، نمودار میله‌ای را با استفاده از بسته `ggplot2` رسم کرده و رنگ‌ها و برچسب‌های مختلف را مشخص می‌کنیم.

![Stacked bar chart](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/stacked-bar-chart.png)

این نمودار میله‌ای، با این حال، خوانا نیست زیرا داده‌های غیرگروه‌بندی شده زیادی وجود دارد. شما باید فقط داده‌هایی را که می‌خواهید رسم کنید انتخاب کنید، بنابراین بیایید طول پرندگان را بر اساس دسته‌بندی آن‌ها بررسی کنیم.

داده‌های خود را فیلتر کنید تا فقط دسته‌بندی پرندگان را شامل شود.

از آنجا که دسته‌بندی‌های زیادی وجود دارد، می‌توانید این نمودار را به صورت عمودی نمایش دهید و ارتفاع آن را برای نمایش تمام داده‌ها تنظیم کنید:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
ابتدا مقادیر منحصر به فرد در ستون `Category` را شمارش کرده و سپس آن‌ها را به یک دیتافریم جدید به نام `birds_count` مرتب می‌کنیم. این داده‌های مرتب شده سپس در همان سطح فاکتور می‌شوند تا به صورت مرتب رسم شوند. با استفاده از `ggplot2` داده‌ها را در یک نمودار میله‌ای رسم می‌کنیم. `coord_flip()` میله‌های افقی را رسم می‌کند.

![category-length](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/category-length.png)

این نمودار میله‌ای نمای خوبی از تعداد پرندگان در هر دسته‌بندی نشان می‌دهد. در یک نگاه، می‌بینید که بیشترین تعداد پرندگان در این منطقه در دسته اردک‌ها/غازها/آبزیان قرار دارند. مینه‌سوتا "سرزمین 10,000 دریاچه" است، بنابراین این موضوع تعجب‌آور نیست!

✅ برخی شمارش‌های دیگر را روی این مجموعه داده امتحان کنید. آیا چیزی شما را شگفت‌زده می‌کند؟

## مقایسه داده‌ها

می‌توانید مقایسه‌های مختلفی از داده‌های گروه‌بندی شده با ایجاد محورهای جدید امتحان کنید. یک مقایسه از حداکثر طول پرنده، بر اساس دسته‌بندی آن را امتحان کنید:

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
ما داده‌های `birds_filtered` را بر اساس `Category` گروه‌بندی کرده و سپس نمودار میله‌ای رسم می‌کنیم.

![comparing data](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/comparingdata.png)

اینجا چیزی تعجب‌آور نیست: مرغ مگس‌خوار کمترین حداکثر طول را در مقایسه با پلیکان‌ها یا غازها دارد. خوب است وقتی داده‌ها منطقی به نظر می‌رسند!

می‌توانید تجسم‌های جالب‌تری از نمودارهای میله‌ای با قرار دادن داده‌ها روی هم ایجاد کنید. بیایید حداقل و حداکثر طول را روی یک دسته‌بندی پرنده قرار دهیم:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/superimposed-values.png)

## 🚀 چالش

این مجموعه داده پرندگان اطلاعات زیادی درباره انواع مختلف پرندگان در یک اکوسیستم خاص ارائه می‌دهد. در اینترنت جستجو کنید و ببینید آیا می‌توانید مجموعه داده‌های دیگری مرتبط با پرندگان پیدا کنید. تمرین کنید نمودارها و گراف‌هایی پیرامون این پرندگان بسازید تا حقایقی را کشف کنید که قبلاً نمی‌دانستید.

## [آزمون پس از درس](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## مرور و مطالعه شخصی

این درس اول اطلاعاتی درباره نحوه استفاده از `ggplot2` برای تجسم مقادیر به شما داده است. تحقیق کنید و روش‌های دیگری برای کار با مجموعه داده‌ها برای تجسم پیدا کنید. تحقیق کنید و به دنبال مجموعه داده‌هایی باشید که بتوانید با استفاده از بسته‌های دیگر مانند [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) و [Plotly](https://github.com/plotly/plotly.R#readme) تجسم کنید.

## تکلیف  
[خطوط، پراکندگی‌ها و میله‌ها](assignment.md)  

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادقتی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.