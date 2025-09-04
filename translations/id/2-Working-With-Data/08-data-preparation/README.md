<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90a815d332aea41a222f4c6372e7186e",
  "translation_date": "2025-09-04T20:33:59+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "id"
}
-->
# Bekerja dengan Data: Persiapan Data

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Persiapan Data - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

## [Kuis Pra-Kuliah](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Bergantung pada sumbernya, data mentah mungkin mengandung beberapa inkonsistensi yang dapat menyebabkan tantangan dalam analisis dan pemodelan. Dengan kata lain, data ini dapat dikategorikan sebagai "kotor" dan perlu dibersihkan. Pelajaran ini berfokus pada teknik untuk membersihkan dan mentransformasi data guna menangani tantangan seperti data yang hilang, tidak akurat, atau tidak lengkap. Topik yang dibahas dalam pelajaran ini akan menggunakan Python dan pustaka Pandas dan akan [didemonstrasikan dalam notebook](notebook.ipynb) di direktori ini.

## Pentingnya Membersihkan Data

- **Kemudahan penggunaan dan penggunaan ulang**: Ketika data diorganisasi dan dinormalisasi dengan baik, data menjadi lebih mudah untuk dicari, digunakan, dan dibagikan kepada orang lain.

- **Konsistensi**: Ilmu data sering kali membutuhkan pengolahan lebih dari satu dataset, di mana dataset dari berbagai sumber perlu digabungkan. Memastikan bahwa setiap dataset individu memiliki standarisasi yang sama akan memastikan bahwa data tetap berguna ketika digabungkan menjadi satu dataset.

- **Akurasi model**: Data yang telah dibersihkan meningkatkan akurasi model yang bergantung padanya.

## Tujuan dan Strategi Pembersihan yang Umum

- **Mengeksplorasi dataset**: Eksplorasi data, yang dibahas dalam [pelajaran berikutnya](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), dapat membantu Anda menemukan data yang perlu dibersihkan. Mengamati nilai-nilai dalam dataset secara visual dapat memberikan gambaran tentang seperti apa data lainnya, atau memberikan ide tentang masalah yang dapat diselesaikan. Eksplorasi dapat melibatkan kueri dasar, visualisasi, dan pengambilan sampel.

- **Pemformatan**: Bergantung pada sumbernya, data dapat memiliki inkonsistensi dalam cara penyajiannya. Ini dapat menyebabkan masalah dalam pencarian dan representasi nilai, di mana nilai tersebut terlihat dalam dataset tetapi tidak direpresentasikan dengan benar dalam visualisasi atau hasil kueri. Masalah pemformatan umum melibatkan penyelesaian spasi kosong, tanggal, dan tipe data. Penyelesaian masalah pemformatan biasanya menjadi tanggung jawab orang yang menggunakan data. Misalnya, standar tentang bagaimana tanggal dan angka disajikan dapat berbeda di setiap negara.

- **Duplikasi**: Data yang memiliki lebih dari satu kemunculan dapat menghasilkan hasil yang tidak akurat dan biasanya harus dihapus. Ini dapat sering terjadi ketika menggabungkan dua atau lebih dataset. Namun, ada kasus di mana duplikasi dalam dataset gabungan mengandung informasi tambahan yang mungkin perlu dipertahankan.

- **Data yang Hilang**: Data yang hilang dapat menyebabkan ketidakakuratan serta hasil yang lemah atau bias. Terkadang ini dapat diselesaikan dengan "memuat ulang" data, mengisi nilai yang hilang dengan perhitungan dan kode seperti Python, atau cukup menghapus nilai dan data yang terkait. Ada banyak alasan mengapa data mungkin hilang, dan tindakan yang diambil untuk menyelesaikan nilai yang hilang ini dapat bergantung pada bagaimana dan mengapa data tersebut hilang.

## Mengeksplorasi Informasi DataFrame
> **Tujuan pembelajaran:** Pada akhir subbagian ini, Anda harus merasa nyaman menemukan informasi umum tentang data yang disimpan dalam DataFrame pandas.

Setelah Anda memuat data ke dalam pandas, kemungkinan besar data tersebut akan berada dalam bentuk DataFrame (lihat [pelajaran sebelumnya](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) untuk gambaran rinci). Namun, jika dataset dalam DataFrame Anda memiliki 60.000 baris dan 400 kolom, bagaimana Anda mulai memahami apa yang sedang Anda kerjakan? Untungnya, [pandas](https://pandas.pydata.org/) menyediakan beberapa alat yang nyaman untuk dengan cepat melihat informasi keseluruhan tentang DataFrame selain beberapa baris pertama dan terakhir.

Untuk mengeksplorasi fungsionalitas ini, kita akan mengimpor pustaka Python scikit-learn dan menggunakan dataset ikonik: **Iris dataset**.

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

- **DataFrame.info**: Untuk memulai, metode `info()` digunakan untuk mencetak ringkasan konten yang ada dalam `DataFrame`. Mari kita lihat dataset ini untuk melihat apa yang kita miliki:
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
Dari sini, kita tahu bahwa dataset *Iris* memiliki 150 entri dalam empat kolom tanpa entri null. Semua data disimpan sebagai angka floating-point 64-bit.

- **DataFrame.head()**: Selanjutnya, untuk memeriksa konten sebenarnya dari `DataFrame`, kita menggunakan metode `head()`. Mari kita lihat beberapa baris pertama dari `iris_df` kita:
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
- **DataFrame.tail()**: Sebaliknya, untuk memeriksa beberapa baris terakhir dari `DataFrame`, kita menggunakan metode `tail()`:
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
> **Kesimpulan:** Bahkan hanya dengan melihat metadata tentang informasi dalam DataFrame atau beberapa nilai pertama dan terakhir di dalamnya, Anda dapat langsung mendapatkan gambaran tentang ukuran, bentuk, dan konten data yang sedang Anda kerjakan.

## Menangani Data yang Hilang
> **Tujuan pembelajaran:** Pada akhir subbagian ini, Anda harus tahu cara mengganti atau menghapus nilai null dari DataFrame.

Sebagian besar waktu, dataset yang ingin Anda gunakan (atau harus digunakan) memiliki nilai yang hilang di dalamnya. Cara menangani data yang hilang membawa kompromi halus yang dapat memengaruhi analisis akhir Anda dan hasil dunia nyata.

Pandas menangani nilai yang hilang dengan dua cara. Yang pertama telah Anda lihat sebelumnya di bagian sebelumnya: `NaN`, atau Not a Number. Ini sebenarnya adalah nilai khusus yang merupakan bagian dari spesifikasi floating-point IEEE dan hanya digunakan untuk menunjukkan nilai floating-point yang hilang.

Untuk nilai yang hilang selain float, pandas menggunakan objek Python `None`. Meskipun mungkin tampak membingungkan bahwa Anda akan menemui dua jenis nilai berbeda yang pada dasarnya mengatakan hal yang sama, ada alasan programatik yang masuk akal untuk pilihan desain ini dan, dalam praktiknya, pendekatan ini memungkinkan pandas memberikan kompromi yang baik untuk sebagian besar kasus. Meskipun demikian, baik `None` maupun `NaN` memiliki batasan yang perlu Anda perhatikan terkait cara penggunaannya.

Pelajari lebih lanjut tentang `NaN` dan `None` dari [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Mendeteksi nilai null**: Dalam `pandas`, metode `isnull()` dan `notnull()` adalah metode utama Anda untuk mendeteksi data null. Keduanya mengembalikan Boolean mask atas data Anda. Kita akan menggunakan `numpy` untuk nilai `NaN`:
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
Perhatikan baik-baik outputnya. Apakah ada yang mengejutkan Anda? Meskipun `0` adalah null aritmatika, itu tetap merupakan bilangan bulat yang valid dan pandas memperlakukannya seperti itu. `''` sedikit lebih halus. Meskipun kita menggunakannya di Bagian 1 untuk mewakili nilai string kosong, itu tetap merupakan objek string dan bukan representasi null menurut pandas.

Sekarang, mari kita balikkan ini dan gunakan metode ini dengan cara yang lebih seperti yang akan Anda gunakan dalam praktik. Anda dapat menggunakan Boolean mask secara langsung sebagai indeks ``Series`` atau ``DataFrame``, yang dapat berguna saat mencoba bekerja dengan nilai yang hilang (atau ada) secara terisolasi.

> **Kesimpulan**: Baik metode `isnull()` maupun `notnull()` menghasilkan hasil serupa saat Anda menggunakannya dalam `DataFrame`: mereka menunjukkan hasil dan indeks hasil tersebut, yang akan sangat membantu Anda saat Anda bergulat dengan data Anda.

- **Menghapus nilai null**: Selain mengidentifikasi nilai yang hilang, pandas menyediakan cara yang nyaman untuk menghapus nilai null dari `Series` dan `DataFrame`. (Terutama pada dataset besar, sering kali lebih disarankan untuk menghapus nilai [NA] yang hilang dari analisis Anda daripada menanganinya dengan cara lain.) Untuk melihat ini dalam tindakan, mari kita kembali ke `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Perhatikan bahwa ini seharusnya terlihat seperti output Anda dari `example3[example3.notnull()]`. Perbedaannya di sini adalah, alih-alih hanya mengindeks pada nilai yang dimask, `dropna` telah menghapus nilai yang hilang dari `Series` `example1`.

Karena `DataFrame` memiliki dua dimensi, mereka memberikan lebih banyak opsi untuk menghapus data.

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

(Apakah Anda memperhatikan bahwa pandas mengubah dua kolom menjadi float untuk mengakomodasi `NaN`?)

Anda tidak dapat menghapus satu nilai dari `DataFrame`, jadi Anda harus menghapus seluruh baris atau kolom. Bergantung pada apa yang Anda lakukan, Anda mungkin ingin melakukan salah satu dari keduanya, dan pandas memberi Anda opsi untuk keduanya. Karena dalam ilmu data, kolom umumnya mewakili variabel dan baris mewakili observasi, Anda lebih mungkin menghapus baris data; pengaturan default untuk `dropna()` adalah menghapus semua baris yang mengandung nilai null apa pun:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Jika perlu, Anda dapat menghapus nilai NA dari kolom. Gunakan `axis=1` untuk melakukannya:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Perhatikan bahwa ini dapat menghapus banyak data yang mungkin ingin Anda pertahankan, terutama dalam dataset yang lebih kecil. Bagaimana jika Anda hanya ingin menghapus baris atau kolom yang mengandung beberapa atau bahkan semua nilai null? Anda menentukan pengaturan tersebut dalam `dropna` dengan parameter `how` dan `thresh`.

Secara default, `how='any'` (jika Anda ingin memeriksa sendiri atau melihat parameter lain yang dimiliki metode ini, jalankan `example4.dropna?` dalam sel kode). Anda dapat menentukan `how='all'` untuk hanya menghapus baris atau kolom yang mengandung semua nilai null. Mari kita perluas contoh `DataFrame` kita untuk melihat ini dalam tindakan.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Parameter `thresh` memberi Anda kontrol yang lebih halus: Anda menetapkan jumlah nilai *non-null* yang harus dimiliki baris atau kolom agar tetap dipertahankan:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Di sini, baris pertama dan terakhir telah dihapus, karena hanya mengandung dua nilai non-null.

- **Mengisi nilai null**: Bergantung pada dataset Anda, terkadang lebih masuk akal untuk mengisi nilai null dengan nilai valid daripada menghapusnya. Anda dapat menggunakan `isnull` untuk melakukan ini secara langsung, tetapi itu bisa melelahkan, terutama jika Anda memiliki banyak nilai untuk diisi. Karena ini adalah tugas yang umum dalam ilmu data, pandas menyediakan `fillna`, yang mengembalikan salinan `Series` atau `DataFrame` dengan nilai yang hilang diganti dengan nilai pilihan Anda. Mari kita buat contoh `Series` lain untuk melihat cara kerja ini dalam praktik.
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
Anda dapat mengisi semua entri null dengan satu nilai, seperti `0`:
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
Anda dapat **mengisi ke depan** nilai null, yaitu menggunakan nilai valid terakhir untuk mengisi null:
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
Anda juga dapat **mengisi ke belakang** untuk menyebarkan nilai valid berikutnya ke belakang untuk mengisi null:
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
Seperti yang mungkin Anda duga, ini bekerja sama dengan `DataFrame`, tetapi Anda juga dapat menentukan `axis` di sepanjang mana nilai null diisi. Menggunakan kembali `example2` yang sebelumnya:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Perhatikan bahwa ketika nilai sebelumnya tidak tersedia untuk pengisian ke depan, nilai null tetap ada.
> **Intisari:** Ada berbagai cara untuk menangani nilai yang hilang dalam dataset Anda. Strategi spesifik yang Anda gunakan (menghapusnya, menggantinya, atau bahkan bagaimana Anda menggantinya) harus ditentukan oleh karakteristik data tersebut. Anda akan semakin memahami cara menangani nilai yang hilang seiring dengan semakin seringnya Anda berinteraksi dengan dataset.

## Menghapus data duplikat

> **Tujuan pembelajaran:** Pada akhir bagian ini, Anda seharusnya merasa nyaman dalam mengidentifikasi dan menghapus nilai duplikat dari DataFrame.

Selain data yang hilang, Anda sering kali akan menemukan data duplikat dalam dataset dunia nyata. Untungnya, `pandas` menyediakan cara mudah untuk mendeteksi dan menghapus entri duplikat.

- **Mengidentifikasi duplikat: `duplicated`**: Anda dapat dengan mudah menemukan nilai duplikat menggunakan metode `duplicated` di pandas, yang mengembalikan masker Boolean yang menunjukkan apakah suatu entri dalam `DataFrame` adalah duplikat dari entri sebelumnya. Mari kita buat contoh `DataFrame` lain untuk melihat cara kerjanya.
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
- **Menghapus duplikat: `drop_duplicates`:** cukup mengembalikan salinan data di mana semua nilai `duplicated` adalah `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Baik `duplicated` maupun `drop_duplicates` secara default mempertimbangkan semua kolom, tetapi Anda dapat menentukan agar mereka hanya memeriksa subset kolom dalam `DataFrame` Anda:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Intisari:** Menghapus data duplikat adalah bagian penting dari hampir setiap proyek data sains. Data duplikat dapat mengubah hasil analisis Anda dan memberikan hasil yang tidak akurat!


## 🚀 Tantangan

Semua materi yang dibahas tersedia dalam [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Selain itu, terdapat latihan setelah setiap bagian, cobalah untuk mengerjakannya!

## [Kuis setelah kuliah](https://ff-quizzes.netlify.app/en/ds/)



## Tinjauan & Studi Mandiri

Ada banyak cara untuk menemukan dan mendekati persiapan data Anda untuk analisis dan pemodelan, serta membersihkan data adalah langkah penting yang membutuhkan pengalaman "praktis". Cobalah tantangan-tantangan ini dari Kaggle untuk mengeksplorasi teknik yang tidak dibahas dalam pelajaran ini.

- [Tantangan Pembersihan Data: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Tantangan Pembersihan Data: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Tugas

[Evaluasi Data dari Formulir](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.