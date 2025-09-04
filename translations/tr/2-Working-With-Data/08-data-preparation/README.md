<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90a815d332aea41a222f4c6372e7186e",
  "translation_date": "2025-09-04T18:09:31+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "tr"
}
-->
# Veriyle Çalışma: Veri Hazırlığı

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Veri Hazırlığı - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Ders Öncesi Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Ham veriler, kaynağına bağlı olarak analiz ve modelleme sırasında zorluklara neden olabilecek bazı tutarsızlıklar içerebilir. Başka bir deyişle, bu veriler "kirli" olarak kategorize edilebilir ve temizlenmesi gerekir. Bu ders, eksik, hatalı veya eksik verilerle ilgili zorlukları ele almak için verileri temizleme ve dönüştürme tekniklerine odaklanmaktadır. Bu derste ele alınan konular, Python ve Pandas kütüphanesini kullanacak ve bu dizindeki [not defterinde gösterilecektir](notebook.ipynb).

## Veriyi Temizlemenin Önemi

- **Kullanım ve yeniden kullanım kolaylığı**: Veriler düzgün bir şekilde organize edildiğinde ve normalleştirildiğinde, arama yapmak, kullanmak ve başkalarıyla paylaşmak daha kolay hale gelir.

- **Tutarlılık**: Veri bilimi genellikle birden fazla veri setiyle çalışmayı gerektirir; farklı kaynaklardan gelen veri setlerinin birleştirilmesi gerekir. Her bir veri setinin ortak bir standartlaştırmaya sahip olması, tüm veri setleri birleştirildiğinde verilerin hala kullanışlı olmasını sağlar.

- **Model doğruluğu**: Temizlenmiş veriler, bu verilere dayanan modellerin doğruluğunu artırır.

## Yaygın Temizleme Amaçları ve Stratejileri

- **Bir veri setini keşfetmek**: Veri keşfi, [ilerideki bir derste](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing) ele alınacak olup, temizlenmesi gereken verileri keşfetmenize yardımcı olabilir. Bir veri setindeki değerleri görsel olarak gözlemlemek, geri kalanının nasıl görüneceği konusunda beklentiler oluşturabilir veya çözülebilecek sorunlar hakkında fikir verebilir. Keşif, temel sorgulama, görselleştirme ve örnekleme içerebilir.

- **Formatlama**: Kaynağa bağlı olarak, veriler sunum biçiminde tutarsızlıklar gösterebilir. Bu, veri setinde görülen ancak görselleştirmelerde veya sorgu sonuçlarında doğru şekilde temsil edilmeyen değerlerin aranması ve temsil edilmesinde sorunlara neden olabilir. Yaygın formatlama sorunları, boşlukları, tarihleri ve veri türlerini çözmeyi içerir. Formatlama sorunlarını çözmek genellikle veriyi kullanan kişilere bağlıdır. Örneğin, tarihlerin ve sayıların nasıl sunulacağına ilişkin standartlar ülkeden ülkeye farklılık gösterebilir.

- **Çoğaltmalar**: Birden fazla kez görünen veriler yanlış sonuçlar üretebilir ve genellikle kaldırılmalıdır. Bu, iki veya daha fazla veri setini birleştirirken yaygın bir durum olabilir. Ancak, birleştirilen veri setlerindeki çoğaltmalar, ek bilgi sağlayabilecek parçalar içerebilir ve korunması gerekebilir.

- **Eksik Veriler**: Eksik veriler yanlışlıklara, zayıf veya önyargılı sonuçlara neden olabilir. Bazen bunlar verilerin "yeniden yüklenmesi", eksik değerlerin Python gibi kodlarla hesaplanarak doldurulması veya basitçe değerin ve ilgili verilerin kaldırılmasıyla çözülebilir. Verilerin neden eksik olduğu ve eksik değerleri çözmek için alınan eylemler, eksikliğin nasıl ve neden meydana geldiğine bağlı olabilir.

## DataFrame Bilgilerini Keşfetmek
> **Öğrenme hedefi:** Bu alt bölümün sonunda, pandas DataFrame'lerde depolanan veriler hakkında genel bilgi bulma konusunda rahat olmalısınız.

Verilerinizi pandas'a yükledikten sonra, büyük olasılıkla bir DataFrame içinde olacaktır (detaylı bir genel bakış için önceki [derse](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) bakın). Ancak, DataFrame'inizdeki veri seti 60.000 satır ve 400 sütun içeriyorsa, neyle çalıştığınızı nasıl anlayabilirsiniz? Neyse ki, [pandas](https://pandas.pydata.org/) bir DataFrame'deki genel bilgilerle birlikte ilk birkaç ve son birkaç satırı hızlıca görmenizi sağlayan kullanışlı araçlar sunar.

Bu işlevselliği keşfetmek için Python scikit-learn kütüphanesini içe aktaracağız ve ikonik bir veri seti olan **Iris veri setini** kullanacağız.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|
|----------------------------------------|-----------------|----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: Başlangıç olarak, `info()` yöntemi bir `DataFrame` içeriği hakkında özet bilgi yazdırmak için kullanılır. Bu veri setine bir göz atalım:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
Buradan, *Iris* veri setinin dört sütunda 150 girişe sahip olduğunu ve hiç boş giriş olmadığını biliyoruz. Tüm veriler 64-bit kayan nokta sayıları olarak depolanmıştır.

- **DataFrame.head()**: Ardından, `DataFrame`'in gerçek içeriğini kontrol etmek için `head()` yöntemini kullanırız. `iris_df`'imizin ilk birkaç satırına bakalım:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: Tersine, `DataFrame`'in son birkaç satırını kontrol etmek için `tail()` yöntemini kullanırız:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Sonuç:** Bir DataFrame'deki bilgiler hakkında meta verileri veya ilk ve son birkaç değeri inceleyerek, üzerinde çalıştığınız verilerin boyutu, şekli ve içeriği hakkında hemen bir fikir edinebilirsiniz.

## Eksik Verilerle Başa Çıkmak
> **Öğrenme hedefi:** Bu alt bölümün sonunda, DataFrame'lerden null değerleri değiştirme veya kaldırma konusunda bilgi sahibi olmalısınız.

Çoğu zaman, kullanmak istediğiniz (veya kullanmak zorunda olduğunuz) veri setlerinde eksik değerler bulunur. Eksik verilerin nasıl ele alındığı, nihai analiziniz ve gerçek dünya sonuçlarınız üzerinde ince dengelemeler taşıyabilir.

Pandas eksik değerleri iki şekilde ele alır. İlkini önceki bölümlerde görmüştünüz: `NaN`, yani Not a Number. Bu, aslında IEEE kayan nokta spesifikasyonunun bir parçası olan özel bir değerdir ve yalnızca eksik kayan nokta değerlerini belirtmek için kullanılır.

Kayan nokta dışındaki eksik değerler için pandas, Python `None` nesnesini kullanır. İki farklı türde eksik değerle karşılaşmanın kafa karıştırıcı görünebileceği düşünülse de, bu tasarım seçiminin sağlam programlama nedenleri vardır ve pratikte bu yaklaşım, pandas'ın çoğu durumda iyi bir denge sunmasını sağlar. Bununla birlikte, hem `None` hem de `NaN`, nasıl kullanılabilecekleri konusunda dikkat edilmesi gereken sınırlamalar taşır.

`NaN` ve `None` hakkında daha fazla bilgi için [not defterine](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) göz atın!

- **Null değerleri tespit etme**: `pandas`'ta, `isnull()` ve `notnull()` yöntemleri null verileri tespit etmek için birincil yöntemlerinizdir. Her ikisi de verileriniz üzerinde Boolean maskeleri döndürür. `NaN` değerleri için `numpy` kullanacağız:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Çıktıya dikkatlice bakın. Sizi şaşırtan bir şey var mı? `0` aritmetik olarak null olsa da, yine de tamamen geçerli bir tam sayı olarak kabul edilir ve pandas bunu bu şekilde ele alır. `''` biraz daha ince bir durumdur. Bölüm 1'de boş bir dize değeri olarak kullandığımız halde, yine de bir dize nesnesidir ve pandas açısından null bir temsil değildir.

Şimdi bunu tersine çevirip, bu yöntemleri pratikte daha çok kullanacağınız şekilde kullanalım. Boolean maskeleri doğrudan bir ``Series`` veya ``DataFrame`` indeksi olarak kullanabilirsiniz, bu da eksik (veya mevcut) değerlerle çalışırken faydalı olabilir.

> **Sonuç:** Hem `isnull()` hem de `notnull()` yöntemleri, `DataFrame`'lerde benzer sonuçlar üretir: sonuçları ve bu sonuçların indeksini gösterir, bu da verilerinizle uğraşırken size büyük ölçüde yardımcı olacaktır.

- **Null değerleri kaldırma**: Eksik değerleri tespit etmenin ötesinde, pandas `Series` ve `DataFrame`'lerden null değerleri kaldırmak için uygun bir yöntem sunar. (Özellikle büyük veri setlerinde, eksik [NA] değerleri analizinizden basitçe kaldırmak, diğer yollarla uğraşmaktan daha tavsiye edilebilir olabilir.) Bunu görmek için `example1`'e geri dönelim:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Bu, `example3[example3.notnull()]` çıktınıza benzemelidir. Buradaki fark, maskelenmiş değerler üzerinde sadece indeksleme yapmak yerine, `dropna`'nın eksik değerleri `Series` `example1`'den kaldırmış olmasıdır.

`DataFrame`'ler iki boyuta sahip olduğundan, veri kaldırma için daha fazla seçenek sunar.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Pandas'ın `NaN`'leri barındırmak için iki sütunu float olarak yükselttiğini fark ettiniz mi?)

Bir `DataFrame`'den tek bir değeri kaldıramazsınız, bu yüzden tam satırları veya sütunları kaldırmanız gerekir. Yaptığınız şeye bağlı olarak, birini veya diğerini yapmak isteyebilirsiniz ve bu nedenle pandas her ikisi için de seçenekler sunar. Veri biliminde sütunlar genellikle değişkenleri, satırlar ise gözlemleri temsil ettiğinden, veri satırlarını kaldırmanız daha olasıdır; `dropna()` için varsayılan ayar, herhangi bir null değer içeren tüm satırları kaldırmaktır:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Gerekirse, sütunlardan NA değerlerini kaldırabilirsiniz. Bunu yapmak için `axis=1` kullanın:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Bu, özellikle daha küçük veri setlerinde, tutmak isteyebileceğiniz çok fazla veriyi kaldırabilir. Peki ya yalnızca birkaç veya tamamen null değer içeren satırları veya sütunları kaldırmak isterseniz? Bu ayarları `dropna` içinde `how` ve `thresh` parametreleriyle belirtebilirsiniz.

Varsayılan olarak, `how='any'` (kendiniz kontrol etmek veya yöntemin başka hangi parametrelere sahip olduğunu görmek isterseniz, bir kod hücresinde `example4.dropna?` çalıştırın). Alternatif olarak, yalnızca tüm null değerleri içeren satırları veya sütunları kaldırmak için `how='all'` belirtebilirsiniz. Bu işlemi görmek için örnek `DataFrame`'imizi genişletelim.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

`thresh` parametresi size daha ince bir kontrol sağlar: bir satır veya sütunun tutulması için sahip olması gereken *null olmayan* değer sayısını ayarlarsınız:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Burada, yalnızca iki null olmayan değer içeren ilk ve son satır kaldırılmıştır.

- **Null değerleri doldurma**: Veri setinize bağlı olarak, bazen null değerleri geçerli olanlarla doldurmak, onları kaldırmaktan daha mantıklı olabilir. Bunu yerinde yapmak için `isnull` kullanabilirsiniz, ancak bu, özellikle doldurulacak çok fazla değeriniz varsa zahmetli olabilir. Bu, veri biliminde çok yaygın bir görev olduğundan, pandas `fillna` sağlar; bu, eksik değerlerin seçtiğiniz bir değerle değiştirildiği bir `Series` veya `DataFrame` kopyası döndürür. Bunun pratikte nasıl çalıştığını görmek için başka bir örnek `Series` oluşturalım.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Tüm null girişleri tek bir değerle, örneğin `0` ile doldurabilirsiniz:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Null değerleri **ileri doldurabilirsiniz**, yani son geçerli değeri null bir değeri doldurmak için kullanabilirsiniz:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
Ayrıca **geri doldurma** yaparak, null bir değeri doldurmak için bir sonraki geçerli değeri geriye doğru yayabilirsiniz:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Tahmin edebileceğiniz gibi, bu `DataFrame`'lerde de aynı şekilde çalışır, ancak null değerleri doldurmak için bir `axis` belirtebilirsiniz. Daha önce kullanılan `example2`'yi tekrar ele alalım:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Dikkat edin, önceki bir değer ileri doldurma için mevcut olmadığında, null değer kalır.
> **Önemli Nokta:** Veri setlerinizdeki eksik değerlerle başa çıkmanın birden fazla yolu vardır. Kullanacağınız spesifik strateji (eksik değerleri kaldırmak, değiştirmek veya nasıl değiştireceğiniz) verinin özelliklerine bağlı olmalıdır. Veri setleriyle daha fazla çalıştıkça ve etkileşimde bulundukça eksik değerlerle nasıl başa çıkacağınız konusunda daha iyi bir anlayış geliştireceksiniz.

## Yinelenen Verilerin Kaldırılması

> **Öğrenme Hedefi:** Bu alt bölümün sonunda, DataFrame'lerdeki yinelenen değerleri tanımlama ve kaldırma konusunda rahat olmalısınız.

Eksik verilere ek olarak, gerçek dünya veri setlerinde sıklıkla yinelenen verilere rastlarsınız. Neyse ki, `pandas` yinelenen girişleri tespit etmek ve kaldırmak için kolay bir yöntem sunar.

- **Yinelenenleri Tanımlama: `duplicated`**: Pandas'taki `duplicated` yöntemiyle yinelenen değerleri kolayca tespit edebilirsiniz. Bu yöntem, bir `DataFrame`'deki bir girişin daha önceki bir girişin yinelenmiş olup olmadığını gösteren bir Boolean maskesi döndürür. Bunu uygulamalı olarak görmek için başka bir örnek `DataFrame` oluşturalım.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Yinelenenleri Kaldırma: `drop_duplicates`:** `duplicated` değerlerinin `False` olduğu verilerin bir kopyasını döndürür:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Hem `duplicated` hem de `drop_duplicates` varsayılan olarak tüm sütunları dikkate alır, ancak `DataFrame`'inizde yalnızca belirli bir sütun alt kümesini incelemelerini belirtebilirsiniz:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Önemli Nokta:** Yinelenen verilerin kaldırılması neredeyse her veri bilimi projesinin önemli bir parçasıdır. Yinelenen veriler analiz sonuçlarınızı değiştirebilir ve size yanlış sonuçlar verebilir!


## 🚀 Zorluk

Tartışılan tüm materyaller [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb) olarak sağlanmıştır. Ayrıca, her bölümün sonunda egzersizler bulunmaktadır, bunları denemeyi unutmayın!

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ds/)



## Gözden Geçirme ve Kendi Kendine Çalışma

Verilerinizi analiz ve modelleme için hazırlamanın ve temizlemenin birçok yolu vardır ve bu adım "uygulamalı" bir deneyimdir. Bu dersin kapsamadığı teknikleri keşfetmek için Kaggle'daki şu zorlukları deneyin:

- [Veri Temizleme Zorluğu: Tarihleri Ayrıştırma](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Veri Temizleme Zorluğu: Veriyi Ölçeklendirme ve Normalleştirme](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Ödev

[Bir Formdan Veri Değerlendirme](assignment.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.