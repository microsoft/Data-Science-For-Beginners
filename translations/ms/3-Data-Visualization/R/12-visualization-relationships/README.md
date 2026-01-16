<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-28T18:34:15+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "ms"
}
-->
# Memvisualkan Hubungan: Semua Tentang Madu 🍯

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Memvisualkan Hubungan - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Meneruskan fokus kajian kita terhadap alam semula jadi, mari kita terokai visualisasi menarik untuk menunjukkan hubungan antara pelbagai jenis madu, berdasarkan dataset yang diperoleh daripada [Jabatan Pertanian Amerika Syarikat](https://www.nass.usda.gov/About_NASS/index.php).

Dataset ini mengandungi kira-kira 600 item yang memaparkan pengeluaran madu di banyak negeri di Amerika Syarikat. Sebagai contoh, anda boleh melihat bilangan koloni, hasil per koloni, jumlah pengeluaran, stok, harga per paun, dan nilai madu yang dihasilkan di negeri tertentu dari tahun 1998-2012, dengan satu baris setiap tahun bagi setiap negeri.

Adalah menarik untuk memvisualkan hubungan antara pengeluaran tahunan negeri tertentu dan, sebagai contoh, harga madu di negeri tersebut. Sebagai alternatif, anda boleh memvisualkan hubungan antara hasil madu per koloni di negeri-negeri. Tempoh tahun ini meliputi 'CCD' atau 'Colony Collapse Disorder' yang pertama kali dilihat pada tahun 2006 (http://npic.orst.edu/envir/ccd.html), menjadikannya dataset yang menyentuh hati untuk dikaji. 🐝

## [Kuiz Pra-Pelajaran](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

Dalam pelajaran ini, anda boleh menggunakan ggplot2, yang telah anda gunakan sebelum ini, sebagai perpustakaan yang baik untuk memvisualkan hubungan antara pemboleh ubah. Yang paling menarik ialah penggunaan fungsi `geom_point` dan `qplot` dalam ggplot2 yang membolehkan plot taburan dan plot garis untuk memvisualkan '[hubungan statistik](https://ggplot2.tidyverse.org/)' dengan cepat, yang membantu saintis data memahami bagaimana pemboleh ubah saling berkaitan.

## Scatterplots

Gunakan scatterplot untuk menunjukkan bagaimana harga madu berkembang dari tahun ke tahun, mengikut negeri. ggplot2, menggunakan `ggplot` dan `geom_point`, dengan mudah mengelompokkan data negeri dan memaparkan titik data untuk kedua-dua data kategori dan numerik.

Mari kita mulakan dengan mengimport data dan Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Anda akan perasan bahawa data madu mempunyai beberapa kolum menarik, termasuk tahun dan harga per paun. Mari kita terokai data ini, yang dikelompokkan mengikut negeri di Amerika Syarikat:

| negeri | numcol | hasilpercol | jumlahprod | stok     | hargaperlb | nilaiprod | tahun |
| ------ | ------ | ----------- | ---------- | -------- | ---------- | --------- | ----- |
| AL     | 16000  | 71          | 1136000    | 159000   | 0.72       | 818000    | 1998  |
| AZ     | 55000  | 60          | 3300000    | 1485000  | 0.64       | 2112000   | 1998  |
| AR     | 53000  | 65          | 3445000    | 1688000  | 0.59       | 2033000   | 1998  |
| CA     | 450000 | 83          | 37350000   | 12326000 | 0.62       | 23157000  | 1998  |
| CO     | 27000  | 72          | 1944000    | 1594000  | 0.7        | 1361000   | 1998  |
| FL     | 230000 | 98          | 22540000   | 4508000  | 0.64       | 14426000  | 1998  |

Buat scatterplot asas untuk menunjukkan hubungan antara harga per paun madu dan negeri asalnya di Amerika Syarikat. Jadikan paksi `y` cukup tinggi untuk memaparkan semua negeri:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![scatterplot 1](../../../../../translated_images/ms/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

Sekarang, tunjukkan data yang sama dengan skema warna madu untuk menunjukkan bagaimana harga berkembang dari tahun ke tahun. Anda boleh melakukannya dengan menambah parameter 'scale_color_gradientn' untuk menunjukkan perubahan dari tahun ke tahun:

> ✅ Ketahui lebih lanjut tentang [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - cuba skema warna pelangi yang indah!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![scatterplot 2](../../../../../translated_images/ms/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

Dengan perubahan skema warna ini, anda dapat melihat dengan jelas perkembangan yang kuat dari tahun ke tahun dalam hal harga madu per paun. Malah, jika anda melihat set sampel dalam data untuk mengesahkan (pilih negeri tertentu, contohnya Arizona), anda dapat melihat pola kenaikan harga dari tahun ke tahun, dengan beberapa pengecualian:

| negeri | numcol | hasilpercol | jumlahprod | stok    | hargaperlb | nilaiprod | tahun |
| ------ | ------ | ----------- | ---------- | ------- | ---------- | --------- | ----- |
| AZ     | 55000  | 60          | 3300000    | 1485000 | 0.64       | 2112000   | 1998  |
| AZ     | 52000  | 62          | 3224000    | 1548000 | 0.62       | 1999000   | 1999  |
| AZ     | 40000  | 59          | 2360000    | 1322000 | 0.73       | 1723000   | 2000  |
| AZ     | 43000  | 59          | 2537000    | 1142000 | 0.72       | 1827000   | 2001  |
| AZ     | 38000  | 63          | 2394000    | 1197000 | 1.08       | 2586000   | 2002  |
| AZ     | 35000  | 72          | 2520000    | 983000  | 1.34       | 3377000   | 2003  |
| AZ     | 32000  | 55          | 1760000    | 774000  | 1.11       | 1954000   | 2004  |
| AZ     | 36000  | 50          | 1800000    | 720000  | 1.04       | 1872000   | 2005  |
| AZ     | 30000  | 65          | 1950000    | 839000  | 0.91       | 1775000   | 2006  |
| AZ     | 30000  | 64          | 1920000    | 902000  | 1.26       | 2419000   | 2007  |
| AZ     | 25000  | 64          | 1600000    | 336000  | 1.26       | 2016000   | 2008  |
| AZ     | 20000  | 52          | 1040000    | 562000  | 1.45       | 1508000   | 2009  |
| AZ     | 24000  | 77          | 1848000    | 665000  | 1.52       | 2809000   | 2010  |
| AZ     | 23000  | 53          | 1219000    | 427000  | 1.55       | 1889000   | 2011  |
| AZ     | 22000  | 46          | 1012000    | 253000  | 1.79       | 1811000   | 2012  |

Cara lain untuk memvisualkan perkembangan ini adalah dengan menggunakan saiz, bukannya warna. Untuk pengguna yang buta warna, ini mungkin pilihan yang lebih baik. Edit visualisasi anda untuk menunjukkan kenaikan harga dengan peningkatan saiz titik:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Anda dapat melihat saiz titik semakin besar secara beransur-ansur.

![scatterplot 3](../../../../../translated_images/ms/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

Adakah ini kes mudah permintaan dan penawaran? Disebabkan faktor seperti perubahan iklim dan keruntuhan koloni, adakah madu semakin kurang tersedia untuk dibeli dari tahun ke tahun, dan oleh itu harga meningkat?

Untuk mencari korelasi antara beberapa pemboleh ubah dalam dataset ini, mari kita terokai beberapa carta garis.

## Carta Garis

Soalan: Adakah terdapat kenaikan yang jelas dalam harga madu per paun dari tahun ke tahun? Anda boleh menemui ini dengan mudah dengan mencipta satu carta garis:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Jawapan: Ya, dengan beberapa pengecualian sekitar tahun 2003:

![line chart 1](../../../../../translated_images/ms/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

Soalan: Baiklah, pada tahun 2003 adakah kita juga melihat lonjakan dalam bekalan madu? Bagaimana jika anda melihat jumlah pengeluaran dari tahun ke tahun?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![line chart 2](../../../../../translated_images/ms/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

Jawapan: Tidak begitu. Jika anda melihat jumlah pengeluaran, ia sebenarnya kelihatan meningkat pada tahun tersebut, walaupun secara amnya jumlah madu yang dihasilkan menurun sepanjang tahun-tahun ini.

Soalan: Dalam kes itu, apa yang boleh menyebabkan lonjakan harga madu sekitar tahun 2003?

Untuk menemui ini, anda boleh menerokai grid facet.

## Grid Facet

Grid facet mengambil satu aspek dataset anda (dalam kes kita, anda boleh memilih 'tahun' untuk mengelakkan terlalu banyak aspek dihasilkan). Seaborn kemudian boleh membuat plot untuk setiap aspek koordinat x dan y yang anda pilih untuk perbandingan visual yang lebih mudah. Adakah tahun 2003 menonjol dalam jenis perbandingan ini?

Buat grid facet dengan menggunakan `facet_wrap` seperti yang disyorkan oleh [dokumentasi ggplot2](https://ggplot2.tidyverse.org/reference/facet_wrap.html).

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
Dalam visualisasi ini, anda boleh membandingkan hasil per koloni dan bilangan koloni dari tahun ke tahun, bersebelahan dengan wrap yang ditetapkan pada 3 untuk kolum:

![facet grid](../../../../../translated_images/ms/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

Untuk dataset ini, tiada apa-apa yang benar-benar menonjol berkaitan dengan bilangan koloni dan hasilnya, dari tahun ke tahun dan negeri ke negeri. Adakah terdapat cara lain untuk mencari korelasi antara dua pemboleh ubah ini?

## Plot Garis Berganda

Cuba plot multiline dengan meletakkan dua plot garis di atas satu sama lain, menggunakan fungsi `par` dan `plot` dalam R. Kita akan memplotkan tahun pada paksi x dan memaparkan dua paksi y. Jadi, paparkan hasil per koloni dan bilangan koloni, yang disuperimposkan:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![superimposed plots](../../../../../translated_images/ms/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

Walaupun tiada apa-apa yang menonjol sekitar tahun 2003, ia membolehkan kita mengakhiri pelajaran ini dengan nota yang sedikit lebih gembira: walaupun terdapat penurunan bilangan koloni secara keseluruhan, bilangan koloni semakin stabil walaupun hasil per koloni semakin berkurangan.

Teruskan, lebah, teruskan!

🐝❤️
## 🚀 Cabaran

Dalam pelajaran ini, anda telah mempelajari sedikit lagi tentang kegunaan scatterplots dan grid garis, termasuk grid facet. Cabar diri anda untuk mencipta grid facet menggunakan dataset yang berbeza, mungkin yang anda gunakan sebelum pelajaran ini. Perhatikan berapa lama masa yang diambil untuk mencipta dan bagaimana anda perlu berhati-hati tentang berapa banyak grid yang perlu anda lukis menggunakan teknik ini.
## [Kuiz Pasca-Pelajaran](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Kajian & Pembelajaran Kendiri

Plot garis boleh menjadi mudah atau agak kompleks. Lakukan sedikit pembacaan dalam [dokumentasi ggplot2](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) tentang pelbagai cara anda boleh membinanya. Cuba tingkatkan carta garis yang anda bina dalam pelajaran ini dengan kaedah lain yang disenaraikan dalam dokumen tersebut.
## Tugasan

[Selami Sarang Lebah](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.