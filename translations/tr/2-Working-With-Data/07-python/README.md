<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7bfec050f4717dcc2dfd028aca9d21f3",
  "translation_date": "2025-09-06T15:42:34+00:00",
  "source_file": "2-Working-With-Data/07-python/README.md",
  "language_code": "tr"
}
-->
# Veriyle Çalışmak: Python ve Pandas Kütüphanesi

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/07-WorkWithPython.png) |
| :-------------------------------------------------------------------------------------------------------: |
|                 Python ile Çalışmak - _Sketchnote by [@nitya](https://twitter.com/nitya)_                 |

[![Tanıtım Videosu](../../../../translated_images/tr/video-ds-python.245247dc811db8e4d5ac420246de8a118c63fd28f6a56578d08b630ae549f260.png)](https://youtu.be/dZjWOGbsN4Y)

Veritabanları, verileri depolamak ve sorgulamak için oldukça verimli yollar sunarken, veri işleme konusunda en esnek yöntem, kendi programınızı yazarak veriyi manipüle etmektir. Çoğu durumda, bir veritabanı sorgusu yapmak daha etkili bir yol olabilir. Ancak, daha karmaşık veri işleme gerektiğinde, SQL kullanarak bunu kolayca yapmak mümkün olmayabilir. 
Veri işleme herhangi bir programlama diliyle yapılabilir, ancak bazı diller veriyle çalışmak açısından daha üst seviyedir. Veri bilimciler genellikle aşağıdaki dillerden birini tercih eder:

* **[Python](https://www.python.org/)**, genel amaçlı bir programlama dili olup, basitliği nedeniyle genellikle yeni başlayanlar için en iyi seçeneklerden biri olarak kabul edilir. Python, ZIP arşivinden veri çıkarmak veya bir resmi gri tonlamaya dönüştürmek gibi birçok pratik problemi çözmenize yardımcı olabilecek ek kütüphanelere sahiptir. Python, veri biliminin yanı sıra web geliştirme için de sıkça kullanılır.
* **[R](https://www.r-project.org/)**, istatistiksel veri işleme amacıyla geliştirilmiş geleneksel bir araçtır. Büyük bir kütüphane deposu (CRAN) içerir ve veri işleme için iyi bir seçimdir. Ancak, R genel amaçlı bir programlama dili değildir ve veri bilimi alanı dışında nadiren kullanılır.
* **[Julia](https://julialang.org/)**, veri bilimi için özel olarak geliştirilmiş bir başka dildir. Python'dan daha iyi performans sunmayı amaçlar ve bilimsel deneyler için harika bir araçtır.

Bu derste, basit veri işleme için Python kullanmaya odaklanacağız. Dil hakkında temel bir bilgiye sahip olduğunuzu varsayacağız. Python hakkında daha derinlemesine bilgi almak isterseniz, aşağıdaki kaynaklara göz atabilirsiniz:

* [Learn Python in a Fun Way with Turtle Graphics and Fractals](https://github.com/shwars/pycourse) - Python Programlama hakkında GitHub tabanlı hızlı giriş kursu
* [Take your First Steps with Python](https://docs.microsoft.com/en-us/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum) üzerinde öğrenme yolu

Veriler birçok farklı biçimde olabilir. Bu derste, üç veri biçimini ele alacağız - **tablo verisi**, **metin** ve **görseller**.

Tüm ilgili kütüphanelerin tam bir genel görünümünü vermek yerine, birkaç veri işleme örneğine odaklanacağız. Bu, size mümkün olanın ana fikrini verecek ve ihtiyaç duyduğunuzda problemlerinize çözüm bulabileceğiniz yerleri anlamanızı sağlayacaktır.

> **En faydalı tavsiye**. Bilmediğiniz bir veri işlemi gerçekleştirmek istediğinizde, internetten arama yapmayı deneyin. [Stackoverflow](https://stackoverflow.com/) genellikle birçok tipik görev için Python'da faydalı kod örnekleri içerir.

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ds/quiz/12)

## Tablo Verisi ve DataFrame'ler

İlişkisel veritabanları hakkında konuştuğumuzda tablo verisiyle zaten tanışmıştınız. Çok fazla veri olduğunda ve bu veriler birçok farklı bağlantılı tabloda yer aldığında, SQL kullanmak kesinlikle mantıklıdır. Ancak, elimizde bir veri tablosu olduğunda ve bu veri hakkında **anlayış** veya **içgörü** elde etmek istediğimizde, örneğin dağılım, değerler arasındaki korelasyon gibi, SQL kullanmak her zaman yeterli olmayabilir. Veri bilimi alanında, orijinal verinin bazı dönüşümlerini gerçekleştirmek ve ardından görselleştirme yapmak gerektiğinde birçok durum vardır. Bu adımların her ikisi de Python kullanılarak kolayca yapılabilir.

Python'da tablo verisiyle çalışmanıza yardımcı olabilecek en faydalı iki kütüphane şunlardır:
* **[Pandas](https://pandas.pydata.org/)**, **DataFrame** adı verilen yapıları manipüle etmenize olanak tanır. DataFrame'ler, ilişkisel tablolara benzer. Adlandırılmış sütunlara sahip olabilir ve satır, sütun ve genel olarak DataFrame'ler üzerinde çeşitli işlemler gerçekleştirebilirsiniz.
* **[Numpy](https://numpy.org/)**, **tensor** yani çok boyutlu **array**'lerle çalışmak için bir kütüphanedir. Array'ler aynı temel türde değerlere sahiptir ve DataFrame'den daha basittir, ancak daha fazla matematiksel işlem sunar ve daha az yük oluşturur.

Ayrıca bilmeniz gereken birkaç başka kütüphane daha vardır:
* **[Matplotlib](https://matplotlib.org/)**, veri görselleştirme ve grafik çizimi için kullanılan bir kütüphanedir
* **[SciPy](https://www.scipy.org/)**, bazı ek bilimsel fonksiyonlar içeren bir kütüphanedir. Bu kütüphaneyle olasılık ve istatistik hakkında konuşurken zaten karşılaşmıştık.

Python programınızın başında genellikle bu kütüphaneleri içe aktarmak için aşağıdaki kod parçasını kullanırsınız:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import ... # you need to specify exact sub-packages that you need
``` 

Pandas birkaç temel kavram etrafında şekillenmiştir.

### Series 

**Series**, bir liste veya numpy array'e benzer bir değerler dizisidir. Ana fark, serilerin ayrıca bir **index**'e sahip olmasıdır ve seriler üzerinde işlem yaparken (örneğin, toplama), indeks dikkate alınır. İndeks, bir liste veya array'den bir seri oluştururken varsayılan olarak kullanılan basit bir tamsayı satır numarası kadar basit olabilir veya tarih aralığı gibi karmaşık bir yapıya sahip olabilir.

> **Not**: Eşlik eden notebook'ta [`notebook.ipynb`](notebook.ipynb) bazı giriş niteliğinde Pandas kodu bulunmaktadır. Burada yalnızca bazı örnekleri özetliyoruz ve tam notebook'u incelemenizi kesinlikle öneririz.

Bir örneği ele alalım: dondurma satışlarımızı analiz etmek istiyoruz. Belirli bir zaman dilimi için satış rakamlarının (her gün satılan ürün sayısı) bir serisini oluşturalım:

```python
start_date = "Jan 1, 2020"
end_date = "Mar 31, 2020"
idx = pd.date_range(start_date,end_date)
print(f"Length of index is {len(idx)}")
items_sold = pd.Series(np.random.randint(25,50,size=len(idx)),index=idx)
items_sold.plot()
```
![Zaman Serisi Grafiği](../../../../translated_images/tr/timeseries-1.80de678ab1cf727e50e00bcf24009fa2b0a8b90ebc43e34b99a345227d28e467.png)

Şimdi, her hafta arkadaşlarımız için bir parti düzenlediğimizi ve parti için ek olarak 10 paket dondurma aldığımızı varsayalım. Bunu göstermek için haftalık olarak indekslenmiş başka bir seri oluşturabiliriz:
```python
additional_items = pd.Series(10,index=pd.date_range(start_date,end_date,freq="W"))
```
İki seriyi topladığımızda toplam sayıyı elde ederiz:
```python
total_items = items_sold.add(additional_items,fill_value=0)
total_items.plot()
```
![Zaman Serisi Grafiği](../../../../translated_images/tr/timeseries-2.aae51d575c55181ceda81ade8c546a2fc2024f9136934386d57b8a189d7570ff.png)

> **Not**: Basit `total_items+additional_items` sözdizimini kullanmıyoruz. Eğer kullansaydık, sonuç serisinde birçok `NaN` (*Not a Number*) değeri alırdık. Bunun nedeni, `additional_items` serisindeki bazı indeks noktaları için eksik değerler olmasıdır ve `NaN` ile herhangi bir şeyi toplamak `NaN` sonucunu verir. Bu nedenle toplama sırasında `fill_value` parametresini belirtmemiz gerekir.

Zaman serileriyle, farklı zaman aralıklarıyla seriyi yeniden örnekleyebiliriz. Örneğin, aylık ortalama satış hacmini hesaplamak istersek, aşağıdaki kodu kullanabiliriz:
```python
monthly = total_items.resample("1M").mean()
ax = monthly.plot(kind='bar')
```
![Aylık Zaman Serisi Ortalamaları](../../../../translated_images/tr/timeseries-3.f3147cbc8c624881008564bc0b5d9fcc15e7374d339da91766bd0e1c6bd9e3af.png)

### DataFrame

Bir DataFrame, aynı indekse sahip bir dizi serinin koleksiyonudur. Birkaç seriyi bir araya getirerek bir DataFrame oluşturabiliriz:
```python
a = pd.Series(range(1,10))
b = pd.Series(["I","like","to","play","games","and","will","not","change"],index=range(0,9))
df = pd.DataFrame([a,b])
```
Bu, aşağıdaki gibi yatay bir tablo oluşturacaktır:
|     | 0   | 1    | 2   | 3   | 4      | 5   | 6      | 7    | 8    |
| --- | --- | ---- | --- | --- | ------ | --- | ------ | ---- | ---- |
| 0   | 1   | 2    | 3   | 4   | 5      | 6   | 7      | 8    | 9    |
| 1   | I   | like | to  | use | Python | and | Pandas | very | much |

Serileri sütun olarak kullanabilir ve sütun adlarını sözlük kullanarak belirtebiliriz:
```python
df = pd.DataFrame({ 'A' : a, 'B' : b })
```
Bu, aşağıdaki gibi bir tablo oluşturacaktır:

|     | A   | B      |
| --- | --- | ------ |
| 0   | 1   | I      |
| 1   | 2   | like   |
| 2   | 3   | to     |
| 3   | 4   | use    |
| 4   | 5   | Python |
| 5   | 6   | and    |
| 6   | 7   | Pandas |
| 7   | 8   | very   |
| 8   | 9   | much   |

**Not**: Önceki tabloyu transpoze ederek de bu tablo düzenini elde edebiliriz, örneğin 
```python
df = pd.DataFrame([a,b]).T..rename(columns={ 0 : 'A', 1 : 'B' })
```
Burada `.T`, DataFrame'i transpoze etme işlemini, yani satırları ve sütunları değiştirme işlemini ifade eder ve `rename` işlemi, sütun adlarını önceki örneğe uyacak şekilde yeniden adlandırmamıza olanak tanır.

DataFrame'ler üzerinde gerçekleştirebileceğimiz en önemli işlemlerden bazıları şunlardır:

**Sütun seçimi**. Bireysel sütunları `df['A']` yazarak seçebiliriz - bu işlem bir Seri döndürür. Ayrıca, başka bir DataFrame'e alt küme sütunları seçerek `df[['B','A']]` yazabiliriz - bu başka bir DataFrame döndürür.

**Belirli satırları filtreleme**. Örneğin, yalnızca `A` sütunu 5'ten büyük olan satırları bırakmak için `df[df['A']>5]` yazabiliriz.

> **Not**: Filtreleme şu şekilde çalışır. `df['A']<5` ifadesi, orijinal serinin `df['A']` her bir öğesi için ifadenin `True` veya `False` olduğunu belirten bir boolean serisi döndürür. Boolean serisi indeks olarak kullanıldığında, DataFrame'deki satırların alt kümesini döndürür. Bu nedenle, rastgele Python boolean ifadeleri kullanmak mümkün değildir, örneğin `df[df['A']>5 and df['A']<7]` yazmak yanlış olur. Bunun yerine, boolean seriler üzerinde özel `&` işlemini kullanarak `df[(df['A']>5) & (df['A']<7)]` yazmalısınız (*parantezler burada önemlidir*).

**Hesaplanabilir yeni sütunlar oluşturma**. DataFrame için kolayca hesaplanabilir yeni sütunlar oluşturabiliriz, örneğin:
```python
df['DivA'] = df['A']-df['A'].mean() 
``` 
Bu örnek, A'nın ortalama değerinden sapmasını hesaplar. Burada aslında bir seri hesaplıyoruz ve ardından bu seriyi sol taraftaki sütuna atayarak yeni bir sütun oluşturuyoruz. Bu nedenle, serilerle uyumlu olmayan işlemleri kullanamayız, örneğin aşağıdaki kod yanlıştır:
```python
# Wrong code -> df['ADescr'] = "Low" if df['A'] < 5 else "Hi"
df['LenB'] = len(df['B']) # <- Wrong result
``` 
Son örnek, sözdizimsel olarak doğru olsa da, yanlış bir sonuç verir çünkü serinin `B` uzunluğunu tüm sütun değerlerine atar, bireysel öğelerin uzunluğunu değil.

Bu tür karmaşık ifadeleri hesaplamamız gerektiğinde, `apply` fonksiyonunu kullanabiliriz. Son örnek şu şekilde yazılabilir:
```python
df['LenB'] = df['B'].apply(lambda x : len(x))
# or 
df['LenB'] = df['B'].apply(len)
```

Yukarıdaki işlemlerden sonra aşağıdaki DataFrame'e ulaşırız:

|     | A   | B      | DivA | LenB |
| --- | --- | ------ | ---- | ---- |
| 0   | 1   | I      | -4.0 | 1    |
| 1   | 2   | like   | -3.0 | 4    |
| 2   | 3   | to     | -2.0 | 2    |
| 3   | 4   | use    | -1.0 | 3    |
| 4   | 5   | Python | 0.0  | 6    |
| 5   | 6   | and    | 1.0  | 3    |
| 6   | 7   | Pandas | 2.0  | 6    |
| 7   | 8   | very   | 3.0  | 4    |
| 8   | 9   | much   | 4.0  | 4    |

**Satırları numaralara göre seçmek** `iloc` yapısını kullanarak yapılabilir. Örneğin, DataFrame'den ilk 5 satırı seçmek için:
```python
df.iloc[:5]
```

**Gruplama**, genellikle Excel'deki *pivot tablolar* benzeri bir sonuç elde etmek için kullanılır. Örneğin, `LenB`'nin her bir değeri için `A` sütununun ortalama değerini hesaplamak istersek, DataFrame'i `LenB`'ye göre gruplandırabilir ve `mean` çağırabiliriz:
```python
df.groupby(by='LenB')[['A','DivA']].mean()
```
Eğer grup içindeki ortalama ve eleman sayısını hesaplamak istersek, daha karmaşık bir `aggregate` fonksiyonunu kullanabiliriz:
```python
df.groupby(by='LenB') \
 .aggregate({ 'DivA' : len, 'A' : lambda x: x.mean() }) \
 .rename(columns={ 'DivA' : 'Count', 'A' : 'Mean'})
```
Bu bize aşağıdaki tabloyu verir:

| LenB | Count | Mean     |
| ---- | ----- | -------- |
| 1    | 1     | 1.000000 |
| 2    | 1     | 3.000000 |
| 3    | 2     | 5.000000 |
| 4    | 3     | 6.333333 |
| 6    | 2     | 6.000000 |

### Veri Alma
Python nesnelerinden Series ve DataFrame oluşturmanın ne kadar kolay olduğunu gördük. Ancak, veri genellikle bir metin dosyası veya bir Excel tablosu şeklinde gelir. Neyse ki, Pandas bize diskteki verileri yüklemek için basit bir yol sunar. Örneğin, bir CSV dosyasını okumak şu kadar basittir:
```python
df = pd.read_csv('file.csv')
```
"Challenge" bölümünde, verileri yükleme örneklerini, dış web sitelerinden veri alma dahil olmak üzere, daha fazla göreceğiz.

### Yazdırma ve Görselleştirme

Bir Veri Bilimci genellikle veriyi keşfetmek zorundadır, bu yüzden onu görselleştirebilmek önemlidir. DataFrame büyük olduğunda, çoğu zaman sadece her şeyin doğru yapıldığından emin olmak için ilk birkaç satırı yazdırmak isteriz. Bu, `df.head()` çağrılarak yapılabilir. Eğer bunu Jupyter Notebook'tan çalıştırıyorsanız, DataFrame'i güzel bir tablo formunda yazdıracaktır.

Ayrıca bazı sütunları görselleştirmek için `plot` fonksiyonunun kullanımını gördük. `plot` birçok görev için çok kullanışlıdır ve `kind=` parametresi ile birçok farklı grafik türünü destekler. Ancak, daha karmaşık bir şey çizmek için her zaman ham `matplotlib` kütüphanesini kullanabilirsiniz. Veri görselleştirmeyi ayrı derslerde detaylı olarak ele alacağız.

Bu genel bakış, Pandas'ın en önemli kavramlarını kapsar, ancak kütüphane çok zengindir ve onunla yapabileceklerinizin sınırı yoktur! Şimdi bu bilgiyi belirli bir problemi çözmek için uygulayalım.

## 🚀 Challenge 1: COVID Yayılımını Analiz Etmek

Odaklanacağımız ilk problem, COVID-19'un salgın yayılımını modellemektir. Bunu yapmak için, [Johns Hopkins Üniversitesi](https://jhu.edu/) [Sistem Bilimi ve Mühendisliği Merkezi](https://systems.jhu.edu/) (CSSE) tarafından sağlanan, farklı ülkelerdeki enfekte bireylerin sayısına ilişkin verileri kullanacağız. Veri seti [bu GitHub deposunda](https://github.com/CSSEGISandData/COVID-19) mevcuttur.

Verilerle nasıl başa çıkılacağını göstermek istediğimiz için, [`notebook-covidspread.ipynb`](notebook-covidspread.ipynb) dosyasını açmanızı ve baştan sona okumanızı öneriyoruz. Hücreleri çalıştırabilir ve sonunda sizin için bıraktığımız bazı zorlukları deneyebilirsiniz.

![COVID Yayılımı](../../../../translated_images/tr/covidspread.f3d131c4f1d260ab0344d79bac0abe7924598dd754859b165955772e1bd5e8a2.png)

> Jupyter Notebook'ta kod nasıl çalıştırılır bilmiyorsanız, [bu makaleye](https://soshnikov.com/education/how-to-execute-notebooks-from-github/) göz atabilirsiniz.

## Yapılandırılmamış Verilerle Çalışmak

Veriler çok sık tablosal formda gelirken, bazı durumlarda daha az yapılandırılmış verilerle, örneğin metin veya görüntülerle çalışmamız gerekebilir. Bu durumda, yukarıda gördüğümüz veri işleme tekniklerini uygulamak için, yapılandırılmış veriyi bir şekilde **çıkarmamız** gerekir. İşte birkaç örnek:

* Metinden anahtar kelimeleri çıkarmak ve bu anahtar kelimelerin ne sıklıkta göründüğünü görmek
* Resimdeki nesneler hakkında bilgi çıkarmak için sinir ağlarını kullanmak
* Video kamera akışındaki insanların duyguları hakkında bilgi almak

## 🚀 Challenge 2: COVID Makalelerini Analiz Etmek

Bu zorlukta, COVID pandemisi konusuna devam edeceğiz ve konu hakkındaki bilimsel makaleleri işlemeye odaklanacağız. [CORD-19 Veri Seti](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge), meta veriler ve özetlerle birlikte (ve yaklaşık yarısı için tam metin de sağlanmış) COVID hakkında 7000'den fazla (yazım sırasında) makale içerir.

Bu veri setini [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health/?WT.mc_id=academic-77958-bethanycheum) bilişsel hizmetini kullanarak analiz etmenin tam bir örneği [bu blog yazısında](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) açıklanmıştır. Bu analizin basitleştirilmiş bir versiyonunu tartışacağız.

> **NOTE**: Bu depo kapsamında veri setinin bir kopyasını sağlamıyoruz. Öncelikle [Kaggle'daki bu veri setinden](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) [`metadata.csv`](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) dosyasını indirmeniz gerekebilir. Kaggle'a kayıt olmanız gerekebilir. Ayrıca, veri setini kayıt olmadan [buradan](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html) indirebilirsiniz, ancak bu meta veri dosyasına ek olarak tüm tam metinleri de içerecektir.

[`notebook-papers.ipynb`](notebook-papers.ipynb) dosyasını açın ve baştan sona okuyun. Hücreleri çalıştırabilir ve sonunda sizin için bıraktığımız bazı zorlukları deneyebilirsiniz.

![Covid Tıbbi Tedavi](../../../../translated_images/tr/covidtreat.b2ba59f57ca45fbcda36e0ddca3f8cfdddeeed6ca879ea7f866d93fa6ec65791.png)

## Görüntü Verilerini İşleme

Son zamanlarda, görüntüleri anlamamıza olanak tanıyan çok güçlü AI modelleri geliştirildi. Önceden eğitilmiş sinir ağları veya bulut hizmetleri kullanılarak çözülebilecek birçok görev vardır. Bazı örnekler şunlardır:

* **Görüntü Sınıflandırma**, görüntüyü önceden tanımlanmış sınıflardan birine kategorize etmenize yardımcı olabilir. [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum) gibi hizmetleri kullanarak kendi görüntü sınıflandırıcılarınızı kolayca eğitebilirsiniz.
* **Nesne Tespiti**, görüntüdeki farklı nesneleri tespit etmek için. [Computer Vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) gibi hizmetler birçok yaygın nesneyi tespit edebilir ve [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum) modeli ile ilgi alanınızdaki belirli nesneleri tespit etmek için eğitim yapabilirsiniz.
* **Yüz Tespiti**, Yaş, Cinsiyet ve Duygu tespiti dahil. Bu, [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum) aracılığıyla yapılabilir.

Tüm bu bulut hizmetleri [Python SDK'ları](https://docs.microsoft.com/samples/azure-samples/cognitive-services-python-sdk-samples/cognitive-services-python-sdk-samples/?WT.mc_id=academic-77958-bethanycheum) kullanılarak çağrılabilir ve böylece veri keşfi iş akışınıza kolayca entegre edilebilir.

İşte Görüntü veri kaynaklarından veri keşfetme örnekleri:
* [Kodlama Olmadan Veri Bilimi Nasıl Öğrenilir](https://soshnikov.com/azure/how-to-learn-data-science-without-coding/) blog yazısında, Instagram fotoğraflarını keşfederek, bir fotoğrafın daha fazla beğeni almasını sağlayan şeyleri anlamaya çalışıyoruz. Önce [Computer Vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) kullanarak fotoğraflardan mümkün olduğunca fazla bilgi çıkarıyoruz ve ardından [Azure Machine Learning AutoML](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml/?WT.mc_id=academic-77958-bethanycheum) kullanarak yorumlanabilir bir model oluşturuyoruz.
* [Yüz Çalışmaları Atölyesi](https://github.com/CloudAdvocacy/FaceStudies) içinde, [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum) kullanarak etkinliklerden fotoğraflardaki insanların duygularını çıkarıyoruz ve insanları mutlu eden şeyleri anlamaya çalışıyoruz.

## Sonuç

Yapılandırılmış veya yapılandırılmamış verileriniz olsun, Python kullanarak veri işleme ve anlama ile ilgili tüm adımları gerçekleştirebilirsiniz. Muhtemelen veri işleme için en esnek yoldur ve bu nedenle çoğu veri bilimci Python'u birincil araçları olarak kullanır. Veri bilimi yolculuğunuzda ciddiyseniz, Python'u derinlemesine öğrenmek muhtemelen iyi bir fikirdir!

## [Ders sonrası test](https://ff-quizzes.netlify.app/en/ds/quiz/13)

## Gözden Geçirme ve Kendi Kendine Çalışma

**Kitaplar**
* [Wes McKinney. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](https://www.amazon.com/gp/product/1491957662)

**Çevrimiçi Kaynaklar**
* Resmi [10 minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) eğitimi
* [Pandas Görselleştirme Belgeleri](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)

**Python Öğrenmek**
* [Turtle Graphics ve Fraktallar ile Eğlenceli Bir Şekilde Python Öğrenin](https://github.com/shwars/pycourse)
* [Python ile İlk Adımlarınızı Atın](https://docs.microsoft.com/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) Microsoft Learn'deki Öğrenme Yolu [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

## Ödev

[Yukarıdaki zorluklar için daha ayrıntılı veri çalışması yapın](assignment.md)

## Krediler

Bu ders [Dmitry Soshnikov](http://soshnikov.com) tarafından ♥️ ile yazılmıştır.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.