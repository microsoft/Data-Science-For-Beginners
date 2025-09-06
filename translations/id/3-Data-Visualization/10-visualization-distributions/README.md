<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-05T23:55:46+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "id"
}
-->
# Memvisualisasikan Distribusi

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Memvisualisasikan Distribusi - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Pada pelajaran sebelumnya, Anda mempelajari beberapa fakta menarik tentang dataset burung-burung di Minnesota. Anda menemukan data yang salah dengan memvisualisasikan outlier dan melihat perbedaan antara kategori burung berdasarkan panjang maksimum mereka.

## [Kuis sebelum pelajaran](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## Jelajahi dataset burung

Cara lain untuk menggali data adalah dengan melihat distribusinya, atau bagaimana data diatur sepanjang sumbu. Misalnya, Anda mungkin ingin mengetahui distribusi umum dari dataset ini, seperti rentang maksimum lebar sayap atau massa tubuh maksimum burung-burung di Minnesota.

Mari kita temukan beberapa fakta tentang distribusi data dalam dataset ini. Dalam file _notebook.ipynb_ di folder pelajaran ini, impor Pandas, Matplotlib, dan data Anda:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Nama                        | NamaIlmiah             | Kategori              | Ordo         | Famili   | Genus       | StatusKonservasi   | MinPanjang | MaxPanjang | MinMassaTubuh | MaxMassaTubuh | MinLebarSayap | MaxLebarSayap |
| ---: | :-------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | ---------: | ---------: | ------------: | ------------: | ------------: | ------------: |
|    0 | Itik bersiul perut hitam    | Dendrocygna autumnalis | Bebek/Angsa/Burung Air| Anseriformes | Anatidae | Dendrocygna | LC                 |        47  |        56  |         652   |        1020   |          76   |          94   |
|    1 | Itik bersiul fulvous        | Dendrocygna bicolor    | Bebek/Angsa/Burung Air| Anseriformes | Anatidae | Dendrocygna | LC                 |        45  |        53  |         712   |        1050   |          85   |          93   |
|    2 | Angsa salju                 | Anser caerulescens     | Bebek/Angsa/Burung Air| Anseriformes | Anatidae | Anser       | LC                 |        64  |        79  |        2050   |        4050   |         135   |         165   |
|    3 | Angsa Ross                  | Anser rossii           | Bebek/Angsa/Burung Air| Anseriformes | Anatidae | Anser       | LC                 |      57.3  |        64  |        1066   |        1567   |         113   |         116   |
|    4 | Angsa depan putih besar     | Anser albifrons        | Bebek/Angsa/Burung Air| Anseriformes | Anatidae | Anser       | LC                 |        64  |        81  |        1930   |        3310   |         130   |         165   |

Secara umum, Anda dapat dengan cepat melihat bagaimana data didistribusikan dengan menggunakan scatter plot seperti yang kita lakukan pada pelajaran sebelumnya:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![panjang maksimum per ordo](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Ini memberikan gambaran umum tentang distribusi panjang tubuh per Ordo burung, tetapi ini bukan cara terbaik untuk menampilkan distribusi yang sebenarnya. Tugas ini biasanya dilakukan dengan membuat Histogram.
## Bekerja dengan histogram

Matplotlib menawarkan cara yang sangat baik untuk memvisualisasikan distribusi data menggunakan Histogram. Jenis grafik ini mirip dengan grafik batang di mana distribusi dapat dilihat melalui naik turunnya batang. Untuk membuat histogram, Anda memerlukan data numerik. Untuk membuat Histogram, Anda dapat membuat grafik dengan mendefinisikan jenisnya sebagai 'hist' untuk Histogram. Grafik ini menunjukkan distribusi MaxBodyMass untuk seluruh rentang data numerik dalam dataset. Dengan membagi array data menjadi beberapa bin yang lebih kecil, histogram dapat menampilkan distribusi nilai data:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![distribusi seluruh dataset](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Seperti yang Anda lihat, sebagian besar dari 400+ burung dalam dataset ini memiliki Max Body Mass di bawah 2000. Dapatkan wawasan lebih lanjut tentang data dengan mengubah parameter `bins` ke angka yang lebih tinggi, misalnya 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![distribusi seluruh dataset dengan parameter bin lebih besar](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Grafik ini menunjukkan distribusi dengan cara yang lebih rinci. Grafik yang kurang miring ke kiri dapat dibuat dengan memastikan bahwa Anda hanya memilih data dalam rentang tertentu:

Saring data Anda untuk mendapatkan hanya burung-burung yang memiliki massa tubuh di bawah 60, dan tampilkan 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![histogram yang disaring](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Cobalah beberapa filter dan titik data lainnya. Untuk melihat distribusi penuh data, hapus filter `['MaxBodyMass']` untuk menampilkan distribusi yang diberi label.

Histogram juga menawarkan beberapa peningkatan warna dan pelabelan yang menarik untuk dicoba:

Buat histogram 2D untuk membandingkan hubungan antara dua distribusi. Mari kita bandingkan `MaxBodyMass` vs. `MaxLength`. Matplotlib menawarkan cara bawaan untuk menunjukkan konvergensi menggunakan warna yang lebih cerah:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Tampaknya ada korelasi yang diharapkan antara kedua elemen ini di sepanjang sumbu yang diharapkan, dengan satu titik konvergensi yang sangat kuat:

![plot 2D](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Histogram bekerja dengan baik secara default untuk data numerik. Bagaimana jika Anda perlu melihat distribusi berdasarkan data teks? 
## Jelajahi dataset untuk distribusi menggunakan data teks 

Dataset ini juga mencakup informasi yang baik tentang kategori burung serta genus, spesies, dan famili mereka, serta status konservasi mereka. Mari kita gali informasi konservasi ini. Bagaimana distribusi burung berdasarkan status konservasi mereka?

> ✅ Dalam dataset, beberapa akronim digunakan untuk menggambarkan status konservasi. Akronim ini berasal dari [Kategori Daftar Merah IUCN](https://www.iucnredlist.org/), sebuah organisasi yang mengkatalogkan status spesies.
> 
> - CR: Kritis Terancam Punah
> - EN: Terancam Punah
> - EX: Punah
> - LC: Perhatian Paling Sedikit
> - NT: Hampir Terancam
> - VU: Rentan

Nilai-nilai ini berbasis teks sehingga Anda perlu melakukan transformasi untuk membuat histogram. Menggunakan dataframe filteredBirds, tampilkan status konservasi bersama dengan MinWingspan-nya. Apa yang Anda lihat? 

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![kolasi lebar sayap dan konservasi](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Tampaknya tidak ada korelasi yang baik antara lebar sayap minimum dan status konservasi. Uji elemen lain dari dataset menggunakan metode ini. Anda juga dapat mencoba filter yang berbeda. Apakah Anda menemukan korelasi?

## Plot kepadatan

Anda mungkin memperhatikan bahwa histogram yang telah kita lihat sejauh ini 'bertingkat' dan tidak mengalir dengan mulus dalam bentuk lengkung. Untuk menunjukkan grafik kepadatan yang lebih halus, Anda dapat mencoba plot kepadatan.

Untuk bekerja dengan plot kepadatan, kenali pustaka plotting baru, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

Muat Seaborn, coba plot kepadatan dasar:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Plot kepadatan](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Anda dapat melihat bagaimana plot ini mencerminkan yang sebelumnya untuk data MinWingspan; hanya saja lebih halus. Menurut dokumentasi Seaborn, "Dibandingkan dengan histogram, KDE dapat menghasilkan plot yang lebih rapi dan lebih mudah diinterpretasikan, terutama saat menggambar beberapa distribusi. Namun, ini memiliki potensi untuk memperkenalkan distorsi jika distribusi dasarnya terbatas atau tidak halus. Seperti histogram, kualitas representasi juga bergantung pada pemilihan parameter pemulusan yang baik." [sumber](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Dengan kata lain, outlier seperti biasa akan membuat grafik Anda berperilaku buruk.

Jika Anda ingin mengunjungi kembali garis MaxBodyMass yang bergerigi pada grafik kedua yang Anda buat, Anda dapat menghaluskannya dengan sangat baik dengan membuat ulang menggunakan metode ini:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![garis massa tubuh yang halus](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Jika Anda menginginkan garis yang halus, tetapi tidak terlalu halus, edit parameter `bw_adjust`: 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![garis massa tubuh kurang halus](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ Bacalah tentang parameter yang tersedia untuk jenis plot ini dan bereksperimenlah!

Jenis grafik ini menawarkan visualisasi yang sangat informatif. Dengan beberapa baris kode, misalnya, Anda dapat menunjukkan kepadatan massa tubuh maksimum per Ordo burung:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![massa tubuh per ordo](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Anda juga dapat memetakan kepadatan beberapa variabel dalam satu grafik. Uji MaxLength dan MinLength burung dibandingkan dengan status konservasi mereka:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![beberapa kepadatan, ditumpangkan](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Mungkin ada baiknya meneliti apakah kelompok burung 'Rentan' berdasarkan panjang mereka memiliki arti tertentu atau tidak.

## 🚀 Tantangan

Histogram adalah jenis grafik yang lebih canggih dibandingkan scatterplot, grafik batang, atau grafik garis dasar. Cari di internet untuk menemukan contoh penggunaan histogram yang baik. Bagaimana histogram digunakan, apa yang mereka tunjukkan, dan di bidang atau area penyelidikan apa mereka cenderung digunakan?

## [Kuis setelah pelajaran](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## Tinjauan & Studi Mandiri

Dalam pelajaran ini, Anda menggunakan Matplotlib dan mulai bekerja dengan Seaborn untuk menunjukkan grafik yang lebih canggih. Lakukan penelitian tentang `kdeplot` di Seaborn, sebuah "kurva kepadatan probabilitas kontinu dalam satu atau lebih dimensi". Bacalah [dokumentasi](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) untuk memahami cara kerjanya.

## Tugas

[Terapkan keterampilan Anda](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.