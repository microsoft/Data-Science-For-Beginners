<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a49d78e32e280c410f04e5f2a2068e77",
  "translation_date": "2025-09-05T23:54:11+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "id"
}
-->
# Memvisualisasikan Kuantitas

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Memvisualisasikan Kuantitas - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Dalam pelajaran ini, Anda akan mengeksplorasi cara menggunakan salah satu dari banyak pustaka Python yang tersedia untuk belajar membuat visualisasi menarik seputar konsep kuantitas. Dengan menggunakan dataset yang telah dibersihkan tentang burung-burung di Minnesota, Anda dapat mempelajari banyak fakta menarik tentang satwa liar lokal.  
## [Kuis sebelum pelajaran](https://ff-quizzes.netlify.app/en/ds/quiz/16)

## Mengamati rentang sayap dengan Matplotlib

Salah satu pustaka yang sangat baik untuk membuat plot dan grafik sederhana maupun kompleks dari berbagai jenis adalah [Matplotlib](https://matplotlib.org/stable/index.html). Secara umum, proses memplot data menggunakan pustaka ini mencakup mengidentifikasi bagian dari dataframe yang ingin Anda targetkan, melakukan transformasi data yang diperlukan, menetapkan nilai sumbu x dan y, memutuskan jenis plot yang akan ditampilkan, dan kemudian menampilkan plot tersebut. Matplotlib menawarkan berbagai macam visualisasi, tetapi untuk pelajaran ini, mari kita fokus pada jenis yang paling sesuai untuk memvisualisasikan kuantitas: grafik garis, scatterplot, dan diagram batang.

> ✅ Gunakan grafik terbaik yang sesuai dengan struktur data Anda dan cerita yang ingin Anda sampaikan.  
> - Untuk menganalisis tren dari waktu ke waktu: garis  
> - Untuk membandingkan nilai: batang, kolom, pie, scatterplot  
> - Untuk menunjukkan bagaimana bagian-bagian berhubungan dengan keseluruhan: pie  
> - Untuk menunjukkan distribusi data: scatterplot, batang  
> - Untuk menunjukkan tren: garis, kolom  
> - Untuk menunjukkan hubungan antar nilai: garis, scatterplot, bubble  

Jika Anda memiliki dataset dan perlu mengetahui seberapa banyak suatu item tertentu, salah satu tugas pertama yang harus Anda lakukan adalah memeriksa nilainya.  

✅ Ada banyak 'cheat sheet' yang sangat bagus untuk Matplotlib [di sini](https://matplotlib.org/cheatsheets/cheatsheets.pdf).

## Membuat grafik garis tentang nilai rentang sayap burung

Buka file `notebook.ipynb` di root folder pelajaran ini dan tambahkan sebuah sel.

> Catatan: data disimpan di root repositori ini dalam folder `/data`.

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```  
Data ini adalah campuran teks dan angka:

|      | Nama                         | NamaIlmiah             | Kategori              | Ordo         | Famili   | Genus       | StatusKonservasi    | PanjangMin | PanjangMax | BeratMin    | BeratMax    | RentangSayapMin | RentangSayapMax |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | --------------: | --------------: |
|    0 | Itik bersiul perut hitam     | Dendrocygna autumnalis | Bebek/Angsa/Burung Air| Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |              76 |              94 |
|    1 | Itik bersiul fulvous         | Dendrocygna bicolor    | Bebek/Angsa/Burung Air| Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |              85 |              93 |
|    2 | Angsa salju                  | Anser caerulescens     | Bebek/Angsa/Burung Air| Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |             135 |             165 |
|    3 | Angsa Ross                   | Anser rossii           | Bebek/Angsa/Burung Air| Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |             113 |             116 |
|    4 | Angsa putih besar            | Anser albifrons        | Bebek/Angsa/Burung Air| Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |             130 |             165 |

Mari kita mulai dengan memplot beberapa data numerik menggunakan grafik garis dasar. Misalkan Anda ingin melihat rentang sayap maksimum untuk burung-burung menarik ini.

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```  
![Max Wingspan](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-02.png)

Apa yang langsung Anda perhatikan? Tampaknya ada setidaknya satu outlier - itu adalah rentang sayap yang luar biasa! Rentang sayap 2300 sentimeter setara dengan 23 meter - apakah ada Pterodactyl berkeliaran di Minnesota? Mari kita selidiki.

Meskipun Anda bisa melakukan pengurutan cepat di Excel untuk menemukan outlier tersebut, yang mungkin adalah kesalahan pengetikan, lanjutkan proses visualisasi dengan bekerja dari dalam plot.

Tambahkan label ke sumbu x untuk menunjukkan jenis burung yang dimaksud:

```
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.xticks(rotation=45)
x = birds['Name'] 
y = birds['MaxWingspan']

plt.plot(x, y)

plt.show()
```  
![wingspan with labels](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-labels-02.png)

Bahkan dengan rotasi label diatur ke 45 derajat, masih terlalu banyak untuk dibaca. Mari coba strategi yang berbeda: beri label hanya pada outlier dan atur label di dalam grafik. Anda dapat menggunakan scatter chart untuk memberikan lebih banyak ruang untuk pelabelan:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)

for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
    
plt.show()
```  
Apa yang terjadi di sini? Anda menggunakan `tick_params` untuk menyembunyikan label bawah dan kemudian membuat loop pada dataset burung Anda. Dengan memplot grafik menggunakan titik biru kecil dengan `bo`, Anda memeriksa burung mana saja yang memiliki rentang sayap maksimum di atas 500 dan menampilkan label mereka di sebelah titik jika memenuhi syarat. Anda menggeser label sedikit pada sumbu y (`y * (1 - 0.05)`) dan menggunakan nama burung sebagai label.

Apa yang Anda temukan?

![outliers](../../../../3-Data-Visualization/09-visualization-quantities/images/labeled-wingspan-02.png)  
## Memfilter data

Baik Bald Eagle maupun Prairie Falcon, meskipun mungkin burung yang sangat besar, tampaknya salah diberi label, dengan tambahan `0` pada rentang sayap maksimum mereka. Tidak mungkin Anda akan bertemu dengan Bald Eagle dengan rentang sayap 25 meter, tetapi jika iya, beri tahu kami! Mari kita buat dataframe baru tanpa dua outlier tersebut:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()
```  

Dengan memfilter outlier, data Anda sekarang lebih kohesif dan mudah dipahami.

![scatterplot of wingspans](../../../../3-Data-Visualization/09-visualization-quantities/images/scatterplot-wingspan-02.png)  

Sekarang kita memiliki dataset yang lebih bersih setidaknya dalam hal rentang sayap, mari kita temukan lebih banyak tentang burung-burung ini.

Meskipun grafik garis dan scatterplot dapat menampilkan informasi tentang nilai data dan distribusinya, kita ingin memikirkan nilai-nilai yang melekat dalam dataset ini. Anda dapat membuat visualisasi untuk menjawab pertanyaan berikut tentang kuantitas:

> Berapa banyak kategori burung yang ada, dan berapa jumlahnya?  
> Berapa banyak burung yang punah, terancam, langka, atau umum?  
> Berapa banyak genus dan ordo yang ada dalam terminologi Linnaeus?  
## Mengeksplorasi diagram batang

Diagram batang sangat praktis ketika Anda perlu menunjukkan pengelompokan data. Mari kita eksplorasi kategori burung yang ada dalam dataset ini untuk melihat mana yang paling umum berdasarkan jumlah.

Dalam file notebook, buat diagram batang dasar.

✅ Perhatikan, Anda dapat memfilter dua burung outlier yang telah kita identifikasi di bagian sebelumnya, mengedit kesalahan pada rentang sayap mereka, atau membiarkan mereka tetap ada untuk latihan ini yang tidak bergantung pada nilai rentang sayap.

Jika Anda ingin membuat diagram batang, Anda dapat memilih data yang ingin Anda fokuskan. Diagram batang dapat dibuat dari data mentah:

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```  
![full data as a bar chart](../../../../3-Data-Visualization/09-visualization-quantities/images/full-data-bar-02.png)  

Namun, diagram batang ini sulit dibaca karena terlalu banyak data yang tidak dikelompokkan. Anda perlu memilih hanya data yang ingin Anda plot, jadi mari kita lihat panjang burung berdasarkan kategori mereka.

Filter data Anda untuk hanya menyertakan kategori burung.

✅ Perhatikan bahwa Anda menggunakan Pandas untuk mengelola data, dan kemudian membiarkan Matplotlib melakukan pemetaan grafik.

Karena ada banyak kategori, Anda dapat menampilkan grafik ini secara vertikal dan menyesuaikan tingginya untuk mencakup semua data:

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```  
![category and length](../../../../3-Data-Visualization/09-visualization-quantities/images/category-counts-02.png)  

Diagram batang ini menunjukkan pandangan yang baik tentang jumlah burung di setiap kategori. Sekilas, Anda dapat melihat bahwa jumlah burung terbesar di wilayah ini adalah dalam kategori Bebek/Angsa/Burung Air. Minnesota adalah 'tanah 10.000 danau', jadi ini tidak mengejutkan!

✅ Cobalah beberapa penghitungan lain pada dataset ini. Apakah ada yang mengejutkan Anda?

## Membandingkan data

Anda dapat mencoba berbagai perbandingan data yang dikelompokkan dengan membuat sumbu baru. Cobalah perbandingan PanjangMaksimum burung, berdasarkan kategorinya:

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```  
![comparing data](../../../../3-Data-Visualization/09-visualization-quantities/images/category-length-02.png)  

Tidak ada yang mengejutkan di sini: burung kolibri memiliki PanjangMaksimum paling kecil dibandingkan dengan Pelikan atau Angsa. Bagus ketika data masuk akal secara logis!

Anda dapat membuat visualisasi diagram batang yang lebih menarik dengan menumpangkan data. Mari kita tumpangkan Panjang Minimum dan Panjang Maksimum pada kategori burung tertentu:

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```  
Dalam grafik ini, Anda dapat melihat rentang per kategori burung dari Panjang Minimum dan Panjang Maksimum. Anda dapat dengan aman mengatakan bahwa, berdasarkan data ini, semakin besar burung, semakin besar rentang panjangnya. Menarik!

![superimposed values](../../../../3-Data-Visualization/09-visualization-quantities/images/superimposed-02.png)  

## 🚀 Tantangan

Dataset burung ini menawarkan banyak informasi tentang berbagai jenis burung dalam ekosistem tertentu. Cari di internet dan lihat apakah Anda dapat menemukan dataset lain yang berorientasi pada burung. Latih membuat grafik dan diagram seputar burung-burung ini untuk menemukan fakta yang tidak Anda sadari.

## [Kuis setelah pelajaran](https://ff-quizzes.netlify.app/en/ds/quiz/17)

## Tinjauan & Studi Mandiri

Pelajaran pertama ini telah memberikan Anda beberapa informasi tentang cara menggunakan Matplotlib untuk memvisualisasikan kuantitas. Lakukan penelitian tentang cara lain untuk bekerja dengan dataset untuk visualisasi. [Plotly](https://github.com/plotly/plotly.py) adalah salah satu yang tidak akan kita bahas dalam pelajaran ini, jadi lihat apa yang dapat ditawarkannya.  
## Tugas

[Lines, Scatters, and Bars](assignment.md)  

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.