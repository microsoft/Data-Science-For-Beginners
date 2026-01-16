<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-28T18:33:40+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "id"
}
-->
# Visualisasi Hubungan: Semua Tentang Madu 🍯

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Visualisasi Hubungan - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Melanjutkan fokus penelitian kami tentang alam, mari kita temukan visualisasi menarik untuk menunjukkan hubungan antara berbagai jenis madu, berdasarkan dataset yang berasal dari [Departemen Pertanian Amerika Serikat](https://www.nass.usda.gov/About_NASS/index.php).

Dataset ini, yang terdiri dari sekitar 600 item, menampilkan produksi madu di banyak negara bagian AS. Misalnya, Anda dapat melihat jumlah koloni, hasil per koloni, total produksi, stok, harga per pon, dan nilai madu yang diproduksi di negara bagian tertentu dari tahun 1998-2012, dengan satu baris per tahun untuk setiap negara bagian.

Akan menarik untuk memvisualisasikan hubungan antara produksi tahunan suatu negara bagian dan, misalnya, harga madu di negara bagian tersebut. Alternatifnya, Anda dapat memvisualisasikan hubungan antara hasil madu per koloni di berbagai negara bagian. Rentang tahun ini mencakup 'CCD' atau 'Colony Collapse Disorder' yang pertama kali terlihat pada tahun 2006 (http://npic.orst.edu/envir/ccd.html), sehingga dataset ini menjadi bahan studi yang menyentuh. 🐝

## [Kuis Pra-Pelajaran](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

Dalam pelajaran ini, Anda dapat menggunakan ggplot2, yang telah Anda gunakan sebelumnya, sebagai pustaka yang baik untuk memvisualisasikan hubungan antara variabel. Yang sangat menarik adalah penggunaan fungsi `geom_point` dan `qplot` dari ggplot2 yang memungkinkan pembuatan scatter plot dan line plot untuk dengan cepat memvisualisasikan '[hubungan statistik](https://ggplot2.tidyverse.org/)', yang memungkinkan data scientist memahami lebih baik bagaimana variabel saling berhubungan.

## Scatterplot

Gunakan scatterplot untuk menunjukkan bagaimana harga madu berkembang dari tahun ke tahun di setiap negara bagian. ggplot2, dengan menggunakan `ggplot` dan `geom_point`, secara praktis mengelompokkan data negara bagian dan menampilkan titik data untuk data kategoris dan numerik.

Mari kita mulai dengan mengimpor data dan Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Anda akan melihat bahwa data madu memiliki beberapa kolom menarik, termasuk tahun dan harga per pon. Mari kita eksplorasi data ini, dikelompokkan berdasarkan negara bagian AS:

| state | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |
| FL    | 230000 | 98          |22540000   | 4508000  | 0.64       | 14426000  | 1998 |

Buat scatterplot dasar untuk menunjukkan hubungan antara harga per pon madu dan asal negara bagian AS. Buat sumbu `y` cukup tinggi untuk menampilkan semua negara bagian:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![scatterplot 1](../../../../../translated_images/id/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

Sekarang, tunjukkan data yang sama dengan skema warna madu untuk menunjukkan bagaimana harga berkembang dari tahun ke tahun. Anda dapat melakukannya dengan menambahkan parameter 'scale_color_gradientn' untuk menunjukkan perubahan dari tahun ke tahun:

> ✅ Pelajari lebih lanjut tentang [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - coba skema warna pelangi yang indah!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![scatterplot 2](../../../../../translated_images/id/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

Dengan perubahan skema warna ini, Anda dapat melihat bahwa ada perkembangan yang jelas selama bertahun-tahun dalam hal harga madu per pon. Memang, jika Anda melihat sampel data untuk memverifikasi (pilih negara bagian tertentu, misalnya Arizona), Anda dapat melihat pola kenaikan harga dari tahun ke tahun, dengan beberapa pengecualian:

| state | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ    | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ    | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ    | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ    | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ    | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ    | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ    | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ    | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ    | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ    | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ    | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ    | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ    | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ    | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ    | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

Cara lain untuk memvisualisasikan perkembangan ini adalah dengan menggunakan ukuran, bukan warna. Untuk pengguna yang buta warna, ini mungkin menjadi pilihan yang lebih baik. Edit visualisasi Anda untuk menunjukkan kenaikan harga dengan peningkatan lingkaran titik:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Anda dapat melihat ukuran titik yang secara bertahap meningkat.

![scatterplot 3](../../../../../translated_images/id/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

Apakah ini kasus sederhana dari hukum penawaran dan permintaan? Karena faktor seperti perubahan iklim dan keruntuhan koloni, apakah madu yang tersedia untuk dibeli semakin sedikit dari tahun ke tahun, sehingga harga meningkat?

Untuk menemukan korelasi antara beberapa variabel dalam dataset ini, mari kita eksplorasi beberapa grafik garis.

## Grafik Garis

Pertanyaan: Apakah ada kenaikan harga madu per pon yang jelas dari tahun ke tahun? Anda dapat dengan mudah menemukannya dengan membuat grafik garis tunggal:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Jawaban: Ya, dengan beberapa pengecualian sekitar tahun 2003:

![line chart 1](../../../../../translated_images/id/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

Pertanyaan: Nah, pada tahun 2003 apakah kita juga melihat lonjakan pasokan madu? Bagaimana jika Anda melihat total produksi dari tahun ke tahun?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![line chart 2](../../../../../translated_images/id/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

Jawaban: Tidak benar-benar. Jika Anda melihat total produksi, sebenarnya tampaknya meningkat pada tahun tersebut, meskipun secara umum jumlah madu yang diproduksi menurun selama tahun-tahun ini.

Pertanyaan: Dalam hal ini, apa yang bisa menyebabkan lonjakan harga madu sekitar tahun 2003?

Untuk menemukan ini, Anda dapat mengeksplorasi facet grid.

## Facet Grids

Facet grid mengambil satu aspek dari dataset Anda (dalam kasus kami, Anda dapat memilih 'tahun' untuk menghindari terlalu banyak aspek yang dihasilkan). Seaborn kemudian dapat membuat plot untuk masing-masing aspek tersebut berdasarkan koordinat x dan y yang Anda pilih untuk perbandingan visual yang lebih mudah. Apakah tahun 2003 menonjol dalam jenis perbandingan ini?

Buat facet grid dengan menggunakan `facet_wrap` seperti yang direkomendasikan oleh [dokumentasi ggplot2](https://ggplot2.tidyverse.org/reference/facet_wrap.html).

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
Dalam visualisasi ini, Anda dapat membandingkan hasil per koloni dan jumlah koloni dari tahun ke tahun, berdampingan dengan pengaturan wrap pada 3 untuk kolom:

![facet grid](../../../../../translated_images/id/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

Untuk dataset ini, tidak ada yang secara khusus menonjol terkait jumlah koloni dan hasilnya, dari tahun ke tahun dan negara bagian ke negara bagian. Apakah ada cara lain untuk menemukan korelasi antara kedua variabel ini?

## Grafik Garis Ganda

Cobalah plot multiline dengan menumpangkan dua grafik garis di atas satu sama lain, menggunakan fungsi `par` dan `plot` dari R. Kita akan memplot tahun pada sumbu x dan menampilkan dua sumbu y. Jadi, tampilkan hasil per koloni dan jumlah koloni, yang ditumpangkan:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![superimposed plots](../../../../../translated_images/id/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

Meskipun tidak ada yang mencolok di sekitar tahun 2003, ini memungkinkan kita mengakhiri pelajaran ini dengan catatan yang sedikit lebih bahagia: meskipun jumlah koloni secara keseluruhan menurun, jumlah koloni mulai stabil meskipun hasil per koloni menurun.

Semangat, lebah, semangat!

🐝❤️
## 🚀 Tantangan

Dalam pelajaran ini, Anda belajar lebih banyak tentang penggunaan scatterplot dan line grid lainnya, termasuk facet grid. Tantang diri Anda untuk membuat facet grid menggunakan dataset yang berbeda, mungkin yang telah Anda gunakan sebelumnya dalam pelajaran ini. Perhatikan berapa lama waktu yang dibutuhkan untuk membuatnya dan bagaimana Anda perlu berhati-hati tentang berapa banyak grid yang perlu Anda gambar menggunakan teknik ini.
## [Kuis Pasca-Pelajaran](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Tinjauan & Studi Mandiri

Grafik garis bisa sederhana atau cukup kompleks. Lakukan sedikit pembacaan di [dokumentasi ggplot2](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) tentang berbagai cara Anda dapat membangunnya. Cobalah untuk meningkatkan grafik garis yang Anda buat dalam pelajaran ini dengan metode lain yang tercantum dalam dokumen.
## Tugas

[Masuk ke sarang lebah](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.