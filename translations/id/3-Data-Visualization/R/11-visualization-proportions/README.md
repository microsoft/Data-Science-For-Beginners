<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-28T18:29:40+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "id"
}
-->
# Visualisasi Proporsi

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Visualisasi Proporsi - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Dalam pelajaran ini, Anda akan menggunakan dataset yang berfokus pada alam untuk memvisualisasikan proporsi, seperti berapa banyak jenis jamur yang ada dalam dataset tentang jamur. Mari kita eksplorasi jamur yang menarik ini menggunakan dataset dari Audubon yang mencantumkan detail tentang 23 spesies jamur berinsang dalam keluarga Agaricus dan Lepiota. Anda akan bereksperimen dengan visualisasi menarik seperti:

- Diagram lingkaran 🥧
- Diagram donat 🍩
- Diagram waffle 🧇

> 💡 Proyek yang sangat menarik bernama [Charticulator](https://charticulator.com) oleh Microsoft Research menawarkan antarmuka drag and drop gratis untuk visualisasi data. Dalam salah satu tutorial mereka, mereka juga menggunakan dataset jamur ini! Jadi Anda dapat mengeksplorasi data dan mempelajari pustaka ini secara bersamaan: [Tutorial Charticulator](https://charticulator.com/tutorials/tutorial4.html).

## [Kuis Pra-Pelajaran](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Mengenal Jamur Anda 🍄

Jamur sangat menarik. Mari kita impor dataset untuk mempelajarinya:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
Sebuah tabel dicetak dengan beberapa data yang bagus untuk analisis:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban 
| Edible | Convex       |Smooth       | Green     | No Bruises| None   |Free            | Crowded       | Broad     | Black      | Tapering   | Equal      |  Smooth | Smooth                    | White                 | White                  | Partial    | White     | One         | Evanescent | Brown             | Abundant | Grasses
|Edible  |  Convex      | Scaly   | Yellow         | Bruises  | Almond  | Free | Close  |   Broad   |   Brown  | Enlarging   |   Club                      | Smooth                  | Smooth    | White                 |  White                | Partial      | White    |  One  |  Pendant | Black   | Numerous | Grasses
      
Langsung saja, Anda akan melihat bahwa semua data berbentuk teks. Anda harus mengonversi data ini agar dapat digunakan dalam diagram. Sebagian besar data, sebenarnya, direpresentasikan sebagai objek:

```r
names(mushrooms)
```

Outputnya adalah:

```output
[1] "class"                    "cap.shape"               
 [3] "cap.surface"              "cap.color"               
 [5] "bruises"                  "odor"                    
 [7] "gill.attachment"          "gill.spacing"            
 [9] "gill.size"                "gill.color"              
[11] "stalk.shape"              "stalk.root"              
[13] "stalk.surface.above.ring" "stalk.surface.below.ring"
[15] "stalk.color.above.ring"   "stalk.color.below.ring"  
[17] "veil.type"                "veil.color"              
[19] "ring.number"              "ring.type"               
[21] "spore.print.color"        "population"              
[23] "habitat"            
```
Ambil data ini dan ubah kolom 'class' menjadi kategori:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```


Sekarang, jika Anda mencetak data jamur, Anda dapat melihat bahwa data telah dikelompokkan ke dalam kategori berdasarkan kelas beracun/dapat dimakan:
```r
View(grouped)
```


| class | count |
| --------- | --------- |
| Edible | 4208 |
| Poisonous| 3916 |



Jika Anda mengikuti urutan yang disajikan dalam tabel ini untuk membuat label kategori kelas Anda, Anda dapat membuat diagram lingkaran.

## Lingkaran!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
Voila, diagram lingkaran yang menunjukkan proporsi data ini berdasarkan dua kelas jamur. Sangat penting untuk mendapatkan urutan label yang benar, terutama di sini, jadi pastikan untuk memverifikasi urutan pembuatan array label!

![pie chart](../../../../../translated_images/id/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Donat!

Diagram lingkaran yang sedikit lebih menarik secara visual adalah diagram donat, yaitu diagram lingkaran dengan lubang di tengah. Mari kita lihat data kita menggunakan metode ini.

Lihatlah berbagai habitat tempat jamur tumbuh:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Outputnya adalah:
| habitat| count |
| --------- | --------- |
| Grasses    | 2148 |
| Leaves| 832 |
| Meadows    | 292 |
| Paths| 1144 |
| Urban    | 368 |
| Waste| 192 |
| Wood| 3148 |


Di sini, Anda mengelompokkan data berdasarkan habitat. Ada 7 habitat yang tercantum, jadi gunakan itu sebagai label untuk diagram donat Anda:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![donut chart](../../../../../translated_images/id/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Kode ini menggunakan dua pustaka - ggplot2 dan webr. Dengan menggunakan fungsi PieDonut dari pustaka webr, kita dapat membuat diagram donat dengan mudah!

Diagram donat di R juga dapat dibuat hanya dengan pustaka ggplot2. Anda dapat mempelajari lebih lanjut tentangnya [di sini](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) dan mencobanya sendiri.

Sekarang setelah Anda tahu cara mengelompokkan data Anda dan kemudian menampilkannya sebagai lingkaran atau donat, Anda dapat mengeksplorasi jenis diagram lainnya. Cobalah diagram waffle, yang merupakan cara berbeda untuk mengeksplorasi kuantitas.
## Waffle!

Diagram tipe 'waffle' adalah cara berbeda untuk memvisualisasikan kuantitas sebagai array 2D dari kotak-kotak. Cobalah memvisualisasikan berbagai kuantitas warna tutup jamur dalam dataset ini. Untuk melakukan ini, Anda perlu menginstal pustaka pembantu bernama [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) dan menggunakannya untuk menghasilkan visualisasi Anda:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Pilih segmen data Anda untuk dikelompokkan:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Buat diagram waffle dengan membuat label dan kemudian mengelompokkan data Anda:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Dengan menggunakan diagram waffle, Anda dapat dengan jelas melihat proporsi warna tutup dalam dataset jamur ini. Menariknya, ada banyak jamur dengan tutup hijau!

![waffle chart](../../../../../translated_images/id/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

Dalam pelajaran ini, Anda mempelajari tiga cara untuk memvisualisasikan proporsi. Pertama, Anda perlu mengelompokkan data Anda ke dalam kategori dan kemudian memutuskan cara terbaik untuk menampilkan data - lingkaran, donat, atau waffle. Semuanya menarik dan memberikan pengguna gambaran instan tentang dataset.

## 🚀 Tantangan

Cobalah membuat ulang diagram yang menarik ini di [Charticulator](https://charticulator.com).
## [Kuis Pasca-Pelajaran](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Tinjauan & Studi Mandiri

Kadang-kadang tidak jelas kapan harus menggunakan diagram lingkaran, donat, atau waffle. Berikut beberapa artikel untuk dibaca tentang topik ini:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Lakukan penelitian untuk menemukan lebih banyak informasi tentang keputusan yang sulit ini.
## Tugas

[Cobalah di Excel](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.