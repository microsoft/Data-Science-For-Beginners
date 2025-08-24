<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-24T01:09:46+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "fa"
}
-->
# تجسم توزیع‌ها

|![طرح دستی توسط [(@sketchthedocs)](https://sketchthedocs.dev)](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| تجسم توزیع‌ها - _طرح دستی توسط [@nitya](https://twitter.com/nitya)_ |

در درس قبلی، شما برخی حقایق جالب درباره یک مجموعه داده از پرندگان مینه‌سوتا یاد گرفتید. شما با تجسم نقاط پرت داده‌های اشتباه را پیدا کردید و تفاوت‌های بین دسته‌های پرندگان را بر اساس حداکثر طول آن‌ها بررسی کردید.

## [آزمون قبل از درس](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## بررسی مجموعه داده پرندگان

یکی دیگر از روش‌های بررسی داده‌ها، نگاه کردن به توزیع آن‌ها است، یا اینکه داده‌ها چگونه در طول یک محور سازماندهی شده‌اند. شاید، به عنوان مثال، بخواهید درباره توزیع کلی حداکثر طول بال یا حداکثر جرم بدن پرندگان مینه‌سوتا در این مجموعه داده اطلاعات کسب کنید.

بیایید برخی حقایق درباره توزیع داده‌ها در این مجموعه داده کشف کنیم. در کنسول R خود، `ggplot2` و پایگاه داده را وارد کنید. نقاط پرت را از پایگاه داده حذف کنید، همان‌طور که در موضوع قبلی انجام دادید.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | نام                          | نام علمی               | دسته                  | راسته        | خانواده  | جنس        | وضعیت حفاظتی         | حداقل طول | حداکثر طول | حداقل جرم بدن | حداکثر جرم بدن | حداقل طول بال | حداکثر طول بال |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | اردک سوت‌زن شکم‌سیاه         | Dendrocygna autumnalis | اردک‌ها/غازها/آبزیان | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | اردک سوت‌زن قهوه‌ای          | Dendrocygna bicolor    | اردک‌ها/غازها/آبزیان | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | غاز برفی                     | Anser caerulescens     | اردک‌ها/غازها/آبزیان | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | غاز راس                      | Anser rossii           | اردک‌ها/غازها/آبزیان | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | غاز پیشانی‌سفید بزرگ         | Anser albifrons        | اردک‌ها/غازها/آبزیان | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

به طور کلی، می‌توانید به سرعت نحوه توزیع داده‌ها را با استفاده از یک نمودار پراکندگی، همان‌طور که در درس قبلی انجام دادید، مشاهده کنید:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![حداکثر طول بر اساس راسته](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/max-length-per-order.png)

این نمودار نمای کلی از توزیع کلی طول بدن بر اساس راسته پرندگان ارائه می‌دهد، اما بهترین روش برای نمایش توزیع‌های واقعی نیست. این کار معمولاً با ایجاد یک هیستوگرام انجام می‌شود.

## کار با هیستوگرام‌ها

`ggplot2` روش‌های بسیار خوبی برای تجسم توزیع داده‌ها با استفاده از هیستوگرام‌ها ارائه می‌دهد. این نوع نمودار شبیه به نمودار میله‌ای است که در آن توزیع از طریق افزایش و کاهش میله‌ها قابل مشاهده است. برای ساخت یک هیستوگرام، به داده‌های عددی نیاز دارید. برای ساخت یک هیستوگرام، می‌توانید نموداری با نوع 'hist' برای هیستوگرام ترسیم کنید. این نمودار توزیع `MaxBodyMass` را برای کل محدوده داده‌های عددی مجموعه داده نشان می‌دهد. با تقسیم آرایه داده‌ها به بخش‌های کوچکتر، می‌تواند توزیع مقادیر داده‌ها را نمایش دهد:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![توزیع در کل مجموعه داده](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/distribution-over-the-entire-dataset.png)

همان‌طور که می‌بینید، بیشتر از ۴۰۰ پرنده در این مجموعه داده در محدوده زیر ۲۰۰۰ برای حداکثر جرم بدن قرار دارند. با تغییر پارامتر `bins` به عددی بالاتر، مثلاً ۳۰، بینش بیشتری به دست آورید:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![توزیع با ۳۰ بخش](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/distribution-30bins.png)

این نمودار توزیع را به شکلی کمی دقیق‌تر نشان می‌دهد. می‌توان با انتخاب داده‌ها در یک محدوده خاص، نموداری کمتر متمایل به سمت چپ ایجاد کرد:

داده‌های خود را فیلتر کنید تا فقط پرندگانی که جرم بدن آن‌ها زیر ۶۰ است را بگیرید و ۳۰ `bins` نمایش دهید:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![هیستوگرام فیلتر شده](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/filtered-histogram.png)

✅ برخی فیلترها و نقاط داده دیگر را امتحان کنید. برای مشاهده توزیع کامل داده‌ها، فیلتر `['MaxBodyMass']` را حذف کنید تا توزیع‌های برچسب‌دار نمایش داده شوند.

هیستوگرام همچنین گزینه‌های زیبایی برای رنگ و برچسب‌گذاری ارائه می‌دهد:

یک هیستوگرام دو بعدی ایجاد کنید تا رابطه بین دو توزیع را مقایسه کنید. بیایید `MaxBodyMass` و `MaxLength` را مقایسه کنیم. `ggplot2` یک روش داخلی برای نمایش همگرایی با استفاده از رنگ‌های روشن‌تر ارائه می‌دهد:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
به نظر می‌رسد که یک همبستگی مورد انتظار بین این دو عنصر در طول یک محور مورد انتظار وجود دارد، با یک نقطه همگرایی بسیار قوی:

![نمودار دو بعدی](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/2d-plot.png)

هیستوگرام‌ها به طور پیش‌فرض برای داده‌های عددی خوب عمل می‌کنند. اگر بخواهید توزیع‌ها را بر اساس داده‌های متنی ببینید چه می‌کنید؟

## بررسی مجموعه داده برای توزیع‌ها با استفاده از داده‌های متنی

این مجموعه داده همچنین اطلاعات خوبی درباره دسته پرندگان و جنس، گونه، و خانواده آن‌ها و همچنین وضعیت حفاظتی آن‌ها ارائه می‌دهد. بیایید به این اطلاعات حفاظتی بپردازیم. توزیع پرندگان بر اساس وضعیت حفاظتی آن‌ها چگونه است؟

> ✅ در این مجموعه داده، چندین مخفف برای توصیف وضعیت حفاظتی استفاده شده است. این مخفف‌ها از [دسته‌بندی‌های فهرست قرمز IUCN](https://www.iucnredlist.org/) گرفته شده‌اند، سازمانی که وضعیت گونه‌ها را فهرست می‌کند.
> 
> - CR: در معرض خطر بحرانی
> - EN: در معرض خطر
> - EX: منقرض شده
> - LC: کمترین نگرانی
> - NT: نزدیک به تهدید
> - VU: آسیب‌پذیر

این مقادیر متنی هستند، بنابراین باید یک تبدیل انجام دهید تا یک هیستوگرام ایجاد کنید. با استفاده از فریم داده `filteredBirds`، وضعیت حفاظتی آن را در کنار حداقل طول بال نمایش دهید. چه چیزی مشاهده می‌کنید؟

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

![طول بال و وضعیت حفاظتی](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/wingspan-conservation-collation.png)

به نظر نمی‌رسد که همبستگی خوبی بین حداقل طول بال و وضعیت حفاظتی وجود داشته باشد. سایر عناصر مجموعه داده را با استفاده از این روش آزمایش کنید. آیا همبستگی‌ای پیدا می‌کنید؟

## نمودارهای چگالی

ممکن است متوجه شده باشید که هیستوگرام‌هایی که تاکنون مشاهده کرده‌ایم، "پله‌ای" هستند و به صورت یک قوس روان جریان ندارند. برای نمایش یک نمودار چگالی روان‌تر، می‌توانید از نمودار چگالی استفاده کنید.

بیایید اکنون با نمودارهای چگالی کار کنیم!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![نمودار چگالی](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/density-plot.png)

می‌توانید ببینید که این نمودار شبیه نمودار قبلی برای داده‌های حداقل طول بال است؛ فقط کمی روان‌تر است. اگر بخواهید آن خط ناهموار `MaxBodyMass` را در نمودار دوم که ساختید، روان‌تر کنید، می‌توانید با استفاده از این روش آن را به خوبی بازسازی کنید:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![چگالی جرم بدن](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/bodymass-smooth.png)

اگر بخواهید یک خط روان، اما نه خیلی روان داشته باشید، پارامتر `adjust` را ویرایش کنید:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![چگالی جرم بدن کمتر روان](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/less-smooth-bodymass.png)

✅ درباره پارامترهای موجود برای این نوع نمودار مطالعه کنید و آزمایش کنید!

این نوع نمودار تجسم‌های توضیحی زیبایی ارائه می‌دهد. به عنوان مثال، با چند خط کد می‌توانید چگالی حداکثر جرم بدن را بر اساس راسته پرندگان نمایش دهید:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![جرم بدن بر اساس راسته](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/bodymass-per-order.png)

## 🚀 چالش

هیستوگرام‌ها نوعی نمودار پیشرفته‌تر از نمودارهای پراکندگی ساده، نمودارهای میله‌ای یا نمودارهای خطی هستند. در اینترنت جستجو کنید تا نمونه‌های خوبی از استفاده از هیستوگرام‌ها پیدا کنید. آن‌ها چگونه استفاده می‌شوند، چه چیزی را نشان می‌دهند، و در چه زمینه‌ها یا حوزه‌هایی معمولاً استفاده می‌شوند؟

## [آزمون پس از درس](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## مرور و مطالعه شخصی

در این درس، از `ggplot2` استفاده کردید و شروع به نمایش نمودارهای پیشرفته‌تر کردید. درباره `geom_density_2d()` که "منحنی چگالی احتمال پیوسته در یک یا چند بعد" است، تحقیق کنید. [مستندات](https://ggplot2.tidyverse.org/reference/geom_density_2d.html) را بخوانید تا بفهمید چگونه کار می‌کند.

## تکلیف

[مهارت‌های خود را اعمال کنید](assignment.md)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.