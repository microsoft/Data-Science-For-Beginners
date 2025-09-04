<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90a815d332aea41a222f4c6372e7186e",
  "translation_date": "2025-09-04T20:45:35+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "ms"
}
-->
# Bekerja dengan Data: Penyediaan Data

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Penyediaan Data - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

## [Kuiz Pra-Kuliah](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Bergantung kepada sumbernya, data mentah mungkin mengandungi beberapa ketidakkonsistenan yang boleh menyebabkan cabaran dalam analisis dan pemodelan. Dalam erti kata lain, data ini boleh dikategorikan sebagai "kotor" dan perlu dibersihkan. Pelajaran ini memberi tumpuan kepada teknik untuk membersihkan dan mengubah data bagi menangani cabaran data yang hilang, tidak tepat, atau tidak lengkap. Topik yang dibincangkan dalam pelajaran ini akan menggunakan Python dan pustaka Pandas dan akan [ditunjukkan dalam notebook](notebook.ipynb) dalam direktori ini.

## Kepentingan membersihkan data

- **Kemudahan penggunaan dan pengulangan**: Apabila data disusun dan dinormalisasi dengan betul, ia lebih mudah untuk dicari, digunakan, dan dikongsi dengan orang lain.

- **Konsistensi**: Sains data sering memerlukan kerja dengan lebih daripada satu set data, di mana set data dari pelbagai sumber perlu digabungkan. Memastikan setiap set data individu mempunyai standardisasi yang sama akan memastikan data masih berguna apabila digabungkan menjadi satu set data.

- **Ketepatan model**: Data yang telah dibersihkan meningkatkan ketepatan model yang bergantung padanya.

## Matlamat dan strategi pembersihan yang biasa

- **Meneroka set data**: Penerokaan data, yang dibincangkan dalam [pelajaran kemudian](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), boleh membantu anda mengenal pasti data yang perlu dibersihkan. Melihat nilai secara visual dalam set data boleh memberikan jangkaan tentang rupa keseluruhan data atau memberikan idea tentang masalah yang boleh diselesaikan. Penerokaan boleh melibatkan pertanyaan asas, visualisasi, dan pensampelan.

- **Pemformatan**: Bergantung kepada sumbernya, data boleh mempunyai ketidakkonsistenan dalam cara ia dipersembahkan. Ini boleh menyebabkan masalah dalam mencari dan mewakili nilai, di mana ia dilihat dalam set data tetapi tidak diwakili dengan betul dalam visualisasi atau hasil pertanyaan. Masalah pemformatan biasa melibatkan penyelesaian ruang kosong, tarikh, dan jenis data. Menyelesaikan isu pemformatan biasanya bergantung kepada orang yang menggunakan data. Sebagai contoh, standard tentang cara tarikh dan nombor dipersembahkan boleh berbeza mengikut negara.

- **Penduaan**: Data yang mempunyai lebih daripada satu kejadian boleh menghasilkan keputusan yang tidak tepat dan biasanya perlu dibuang. Ini boleh berlaku apabila menggabungkan dua atau lebih set data. Walau bagaimanapun, terdapat keadaan di mana penduaan dalam set data gabungan mengandungi maklumat tambahan yang mungkin perlu dikekalkan.

- **Data yang hilang**: Data yang hilang boleh menyebabkan ketidaktepatan serta keputusan yang lemah atau berat sebelah. Kadangkala ini boleh diselesaikan dengan "memuat semula" data, mengisi nilai yang hilang dengan pengiraan dan kod seperti Python, atau hanya membuang nilai dan data yang berkaitan. Terdapat banyak sebab mengapa data mungkin hilang, dan tindakan yang diambil untuk menyelesaikan nilai yang hilang ini boleh bergantung kepada bagaimana dan mengapa ia hilang.

## Meneroka maklumat DataFrame
> **Matlamat pembelajaran:** Pada akhir subseksyen ini, anda seharusnya selesa mencari maklumat umum tentang data yang disimpan dalam DataFrame pandas.

Setelah anda memuatkan data anda ke dalam pandas, ia kemungkinan besar akan berada dalam DataFrame (rujuk [pelajaran sebelumnya](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) untuk gambaran terperinci). Walau bagaimanapun, jika set data dalam DataFrame anda mempunyai 60,000 baris dan 400 lajur, bagaimana anda mula memahami apa yang anda sedang kerjakan? Nasib baik, [pandas](https://pandas.pydata.org/) menyediakan beberapa alat yang mudah untuk melihat maklumat keseluruhan tentang DataFrame selain daripada beberapa baris pertama dan terakhir.

Untuk meneroka fungsi ini, kita akan mengimport pustaka Python scikit-learn dan menggunakan set data ikonik: **set data Iris**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |panjang sepal (cm)|lebar sepal (cm)|panjang petal (cm)|lebar petal (cm)|
|----------------------------------------|------------------|----------------|------------------|----------------|
|0                                       |5.1               |3.5             |1.4               |0.2             |
|1                                       |4.9               |3.0             |1.4               |0.2             |
|2                                       |4.7               |3.2             |1.3               |0.2             |
|3                                       |4.6               |3.1             |1.5               |0.2             |
|4                                       |5.0               |3.6             |1.4               |0.2             |

- **DataFrame.info**: Untuk memulakan, kaedah `info()` digunakan untuk mencetak ringkasan kandungan yang terdapat dalam `DataFrame`. Mari kita lihat set data ini untuk melihat apa yang kita ada:
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
Daripada ini, kita tahu bahawa set data *Iris* mempunyai 150 entri dalam empat lajur tanpa entri null. Semua data disimpan sebagai nombor titik terapung 64-bit.

- **DataFrame.head()**: Seterusnya, untuk memeriksa kandungan sebenar `DataFrame`, kita menggunakan kaedah `head()`. Mari lihat beberapa baris pertama `iris_df` kita:
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
- **DataFrame.tail()**: Sebaliknya, untuk memeriksa beberapa baris terakhir `DataFrame`, kita menggunakan kaedah `tail()`:
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
> **Kesimpulan:** Walaupun hanya dengan melihat metadata tentang maklumat dalam DataFrame atau beberapa nilai pertama dan terakhir dalamnya, anda boleh mendapatkan idea segera tentang saiz, bentuk, dan kandungan data yang anda sedang kerjakan.

## Menangani Data yang Hilang
> **Matlamat pembelajaran:** Pada akhir subseksyen ini, anda seharusnya tahu cara menggantikan atau membuang nilai null daripada DataFrame.

Kebanyakan masa, set data yang anda ingin gunakan (atau perlu gunakan) mempunyai nilai yang hilang di dalamnya. Cara data yang hilang ditangani membawa kompromi halus yang boleh mempengaruhi analisis akhir anda dan hasil dunia sebenar.

Pandas menangani nilai yang hilang dengan dua cara. Yang pertama telah anda lihat sebelum ini dalam bahagian sebelumnya: `NaN`, atau Not a Number. Ini sebenarnya adalah nilai khas yang merupakan sebahagian daripada spesifikasi titik terapung IEEE dan hanya digunakan untuk menunjukkan nilai titik terapung yang hilang.

Untuk nilai yang hilang selain daripada titik terapung, pandas menggunakan objek Python `None`. Walaupun mungkin kelihatan mengelirukan bahawa anda akan menemui dua jenis nilai yang pada dasarnya mengatakan perkara yang sama, terdapat alasan programatik yang kukuh untuk pilihan reka bentuk ini dan, dalam amalan, pendekatan ini membolehkan pandas memberikan kompromi yang baik untuk kebanyakan kes. Walaupun begitu, kedua-dua `None` dan `NaN` membawa sekatan yang perlu anda perhatikan berkaitan dengan cara ia boleh digunakan.

Ketahui lebih lanjut tentang `NaN` dan `None` daripada [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Mengesan nilai null**: Dalam `pandas`, kaedah `isnull()` dan `notnull()` adalah kaedah utama anda untuk mengesan data null. Kedua-duanya mengembalikan topeng Boolean ke atas data anda. Kita akan menggunakan `numpy` untuk nilai `NaN`:
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
Perhatikan dengan teliti outputnya. Adakah ada yang mengejutkan anda? Walaupun `0` adalah null aritmetik, ia tetap merupakan integer yang sah dan pandas menganggapnya sebagai sedemikian. `''` sedikit lebih halus. Walaupun kita menggunakannya dalam Bahagian 1 untuk mewakili nilai rentetan kosong, ia tetap merupakan objek rentetan dan bukan representasi null seperti yang dianggap oleh pandas.

Sekarang, mari kita balikkan ini dan gunakan kaedah ini dengan cara yang lebih seperti yang akan anda gunakan dalam amalan. Anda boleh menggunakan topeng Boolean secara langsung sebagai indeks ``Series`` atau ``DataFrame``, yang boleh berguna apabila cuba bekerja dengan nilai yang hilang (atau hadir) secara terasing.

> **Kesimpulan**: Kedua-dua kaedah `isnull()` dan `notnull()` menghasilkan hasil yang serupa apabila anda menggunakannya dalam `DataFrame`: ia menunjukkan hasil dan indeks hasil tersebut, yang akan sangat membantu anda semasa anda bergelut dengan data anda.

- **Membuang nilai null**: Selain mengenal pasti nilai yang hilang, pandas menyediakan cara yang mudah untuk membuang nilai null daripada `Series` dan `DataFrame`. (Terutamanya pada set data yang besar, sering kali lebih disarankan untuk hanya membuang nilai [NA] yang hilang daripada analisis anda daripada menanganinya dengan cara lain.) Untuk melihat ini dalam tindakan, mari kembali ke `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Perhatikan bahawa ini sepatutnya kelihatan seperti output anda daripada `example3[example3.notnull()]`. Perbezaannya di sini ialah, daripada hanya mengindeks pada nilai yang bertopeng, `dropna` telah membuang nilai yang hilang tersebut daripada `Series` `example1`.

Oleh kerana `DataFrame` mempunyai dua dimensi, ia memberikan lebih banyak pilihan untuk membuang data.

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

(Adakah anda perasan bahawa pandas menaikkan dua lajur kepada titik terapung untuk menampung `NaN`?)

Anda tidak boleh membuang satu nilai daripada `DataFrame`, jadi anda perlu membuang baris atau lajur penuh. Bergantung pada apa yang anda lakukan, anda mungkin ingin melakukan salah satu atau yang lain, dan oleh itu pandas memberikan anda pilihan untuk kedua-duanya. Oleh kerana dalam sains data, lajur biasanya mewakili pembolehubah dan baris mewakili pemerhatian, anda lebih cenderung untuk membuang baris data; tetapan lalai untuk `dropna()` adalah untuk membuang semua baris yang mengandungi sebarang nilai null:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Jika perlu, anda boleh membuang nilai NA daripada lajur. Gunakan `axis=1` untuk melakukannya:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Perhatikan bahawa ini boleh membuang banyak data yang mungkin anda ingin simpan, terutamanya dalam set data yang lebih kecil. Bagaimana jika anda hanya ingin membuang baris atau lajur yang mengandungi beberapa atau bahkan semua nilai null? Anda menentukan tetapan tersebut dalam `dropna` dengan parameter `how` dan `thresh`.

Secara lalai, `how='any'` (jika anda ingin memeriksa sendiri atau melihat parameter lain yang dimiliki oleh kaedah tersebut, jalankan `example4.dropna?` dalam sel kod). Anda boleh menentukan `how='all'` sebagai alternatif untuk hanya membuang baris atau lajur yang mengandungi semua nilai null. Mari kita kembangkan `DataFrame` contoh kita untuk melihat ini dalam tindakan.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Parameter `thresh` memberikan kawalan yang lebih terperinci: anda menetapkan bilangan nilai *bukan null* yang diperlukan oleh baris atau lajur untuk disimpan:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Di sini, baris pertama dan terakhir telah dibuang, kerana ia hanya mengandungi dua nilai bukan null.

- **Mengisi nilai null**: Bergantung pada set data anda, kadangkala lebih masuk akal untuk mengisi nilai null dengan nilai yang sah daripada membuangnya. Anda boleh menggunakan `isnull` untuk melakukan ini secara langsung, tetapi itu boleh menjadi membosankan, terutamanya jika anda mempunyai banyak nilai untuk diisi. Oleh kerana ini adalah tugas yang biasa dalam sains data, pandas menyediakan `fillna`, yang mengembalikan salinan `Series` atau `DataFrame` dengan nilai yang hilang digantikan dengan nilai pilihan anda. Mari buat `Series` contoh lain untuk melihat cara ini berfungsi dalam amalan.
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
Anda boleh mengisi semua entri null dengan satu nilai, seperti `0`:
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
Anda boleh **mengisi ke depan** nilai null, iaitu menggunakan nilai sah terakhir untuk mengisi null:
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
Anda juga boleh **mengisi ke belakang** untuk menyebarkan nilai sah seterusnya ke belakang untuk mengisi null:
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
Seperti yang anda mungkin jangkakan, ini berfungsi sama dengan `DataFrame`, tetapi anda juga boleh menentukan `axis` sepanjang mana untuk mengisi nilai null. Menggunakan semula `example2` yang digunakan sebelum ini:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Perhatikan bahawa apabila nilai sebelumnya tidak tersedia untuk pengisian ke depan, nilai null tetap ada.
> **Intipati Penting:** Terdapat pelbagai cara untuk menangani nilai yang hilang dalam set data anda. Strategi khusus yang anda gunakan (menghapusnya, menggantikannya, atau bagaimana anda menggantikannya) harus ditentukan oleh keunikan data tersebut. Anda akan mengembangkan pemahaman yang lebih baik tentang cara menangani nilai yang hilang semakin banyak anda berinteraksi dengan set data.

## Menghapus Data Pendua

> **Matlamat Pembelajaran:** Pada akhir subseksyen ini, anda seharusnya selesa mengenal pasti dan menghapus nilai pendua daripada DataFrame.

Selain data yang hilang, anda juga sering akan menemui data pendua dalam set data dunia nyata. Nasib baik, `pandas` menyediakan cara mudah untuk mengesan dan menghapus entri pendua.

- **Mengenal pasti pendua: `duplicated`**: Anda boleh dengan mudah mengenal pasti nilai pendua menggunakan kaedah `duplicated` dalam pandas, yang mengembalikan topeng Boolean yang menunjukkan sama ada entri dalam `DataFrame` adalah pendua entri sebelumnya. Mari kita cipta satu lagi contoh `DataFrame` untuk melihat ini dalam tindakan.
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
- **Menghapus pendua: `drop_duplicates`:** hanya mengembalikan salinan data di mana semua nilai `duplicated` adalah `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Kedua-dua `duplicated` dan `drop_duplicates` secara lalai mempertimbangkan semua lajur tetapi anda boleh menentukan bahawa ia hanya memeriksa subset lajur dalam `DataFrame` anda:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Intipati Penting:** Menghapus data pendua adalah bahagian penting dalam hampir setiap projek sains data. Data pendua boleh mengubah hasil analisis anda dan memberikan keputusan yang tidak tepat!


## 🚀 Cabaran

Semua bahan yang dibincangkan disediakan sebagai [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Selain itu, terdapat latihan selepas setiap bahagian, cubalah!

## [Kuiz Selepas Kuliah](https://ff-quizzes.netlify.app/en/ds/)



## Ulasan & Kajian Kendiri

Terdapat banyak cara untuk meneroka dan mendekati penyediaan data anda untuk analisis dan pemodelan, dan membersihkan data adalah langkah penting yang memerlukan pengalaman "praktikal". Cuba cabaran ini dari Kaggle untuk meneroka teknik yang tidak dibincangkan dalam pelajaran ini.

- [Cabaran Pembersihan Data: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Cabaran Pembersihan Data: Skala dan Normalisasi Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Tugasan

[Menilai Data daripada Borang](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.