<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cfb068050337a36e348debaa502a24fa",
  "translation_date": "2025-09-05T23:54:40+00:00",
  "source_file": "3-Data-Visualization/13-meaningful-visualizations/README.md",
  "language_code": "id"
}
-->
# Membuat Visualisasi yang Bermakna

|![Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev)](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Visualisasi yang Bermakna - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

> "Jika Anda menyiksa data cukup lama, data akan mengaku apa saja" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Salah satu keterampilan dasar seorang ilmuwan data adalah kemampuan untuk membuat visualisasi data yang bermakna yang membantu menjawab pertanyaan yang Anda miliki. Sebelum memvisualisasikan data Anda, pastikan data tersebut telah dibersihkan dan dipersiapkan, seperti yang telah Anda lakukan di pelajaran sebelumnya. Setelah itu, Anda dapat mulai memutuskan cara terbaik untuk menyajikan data tersebut.

Dalam pelajaran ini, Anda akan mempelajari:

1. Cara memilih jenis grafik yang tepat
2. Cara menghindari grafik yang menyesatkan
3. Cara bekerja dengan warna
4. Cara menata grafik agar mudah dibaca
5. Cara membuat solusi grafik animasi atau 3D
6. Cara membuat visualisasi yang kreatif

## [Kuis Pra-Pelajaran](https://ff-quizzes.netlify.app/en/ds/quiz/24)

## Memilih jenis grafik yang tepat

Dalam pelajaran sebelumnya, Anda telah bereksperimen dengan membangun berbagai visualisasi data menarik menggunakan Matplotlib dan Seaborn. Secara umum, Anda dapat memilih [jenis grafik yang tepat](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) untuk pertanyaan yang Anda ajukan menggunakan tabel berikut:

| Anda perlu:                | Anda sebaiknya menggunakan:     |
| -------------------------- | ------------------------------- |
| Menunjukkan tren data dari waktu ke waktu | Garis                          |
| Membandingkan kategori     | Batang, Pie                     |
| Membandingkan total        | Pie, Batang Bertumpuk           |
| Menunjukkan hubungan       | Scatter, Garis, Facet, Dual Line|
| Menunjukkan distribusi     | Scatter, Histogram, Box         |
| Menunjukkan proporsi       | Pie, Donut, Waffle              |

> ✅ Bergantung pada komposisi data Anda, Anda mungkin perlu mengonversinya dari teks ke numerik agar grafik tertentu dapat mendukungnya.

## Menghindari penyesatan

Meskipun seorang ilmuwan data berhati-hati memilih grafik yang tepat untuk data yang tepat, ada banyak cara data dapat ditampilkan untuk membuktikan suatu poin, sering kali dengan mengorbankan integritas data itu sendiri. Ada banyak contoh grafik dan infografis yang menyesatkan!

[![Bagaimana Grafik Berbohong oleh Alberto Cairo](../../../../3-Data-Visualization/13-meaningful-visualizations/images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "Bagaimana Grafik Berbohong")

> 🎥 Klik gambar di atas untuk menonton pembicaraan konferensi tentang grafik yang menyesatkan

Grafik ini membalik sumbu X untuk menunjukkan kebalikan dari kebenaran, berdasarkan tanggal:

![grafik buruk 1](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-1.png)

[Grafik ini](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) bahkan lebih menyesatkan, karena mata tertarik ke kanan untuk menyimpulkan bahwa, seiring waktu, kasus COVID menurun di berbagai wilayah. Faktanya, jika Anda melihat lebih dekat pada tanggalnya, Anda akan menemukan bahwa tanggal-tanggal tersebut telah diatur ulang untuk memberikan tren menurun yang menyesatkan.

![grafik buruk 2](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-2.jpg)

Contoh terkenal ini menggunakan warna DAN sumbu Y yang dibalik untuk menipu: alih-alih menyimpulkan bahwa kematian akibat senjata meningkat setelah undang-undang yang mendukung senjata disahkan, mata justru tertipu untuk berpikir sebaliknya:

![grafik buruk 3](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-3.jpg)

Grafik aneh ini menunjukkan bagaimana proporsi dapat dimanipulasi, dengan efek yang menggelikan:

![grafik buruk 4](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-4.jpg)

Membandingkan hal yang tidak sebanding adalah trik licik lainnya. Ada [situs web yang luar biasa](https://tylervigen.com/spurious-correlations) tentang 'korelasi palsu' yang menampilkan 'fakta' yang menghubungkan hal-hal seperti tingkat perceraian di Maine dan konsumsi margarin. Sebuah grup Reddit juga mengumpulkan [penggunaan data yang buruk](https://www.reddit.com/r/dataisugly/top/?t=all).

Penting untuk memahami betapa mudahnya mata dapat tertipu oleh grafik yang menyesatkan. Bahkan jika niat ilmuwan data baik, memilih jenis grafik yang buruk, seperti grafik pie dengan terlalu banyak kategori, dapat menyesatkan.

## Warna

Anda telah melihat dalam grafik 'kekerasan senjata di Florida' di atas bagaimana warna dapat memberikan lapisan makna tambahan pada grafik, terutama grafik yang tidak dirancang menggunakan pustaka seperti Matplotlib dan Seaborn yang dilengkapi dengan berbagai pustaka warna dan palet yang telah diverifikasi. Jika Anda membuat grafik secara manual, pelajari sedikit tentang [teori warna](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Perhatikan, saat merancang grafik, bahwa aksesibilitas adalah aspek penting dari visualisasi. Beberapa pengguna Anda mungkin buta warna - apakah grafik Anda dapat dilihat dengan baik oleh pengguna dengan gangguan penglihatan?

Berhati-hatilah saat memilih warna untuk grafik Anda, karena warna dapat menyampaikan makna yang mungkin tidak Anda maksudkan. 'Wanita merah muda' dalam grafik 'tinggi badan' di atas menyampaikan makna 'feminin' yang menambah keanehan grafik itu sendiri.

Meskipun [makna warna](https://colormatters.com/color-symbolism/the-meanings-of-colors) mungkin berbeda di berbagai belahan dunia, dan cenderung berubah makna sesuai dengan nuansanya, secara umum makna warna meliputi:

| Warna  | Makna               |
| ------ | ------------------- |
| merah  | kekuatan            |
| biru   | kepercayaan, loyalitas |
| kuning | kebahagiaan, kehati-hatian |
| hijau  | ekologi, keberuntungan, iri hati |
| ungu   | kebahagiaan         |
| oranye | semangat            |

Jika Anda ditugaskan untuk membuat grafik dengan warna khusus, pastikan grafik Anda dapat diakses dan warna yang Anda pilih sesuai dengan makna yang ingin Anda sampaikan.

## Menata grafik agar mudah dibaca

Grafik tidak akan bermakna jika tidak dapat dibaca! Luangkan waktu untuk mempertimbangkan penataan lebar dan tinggi grafik Anda agar sesuai dengan data Anda. Jika satu variabel (seperti semua 50 negara bagian) perlu ditampilkan, tampilkan secara vertikal pada sumbu Y jika memungkinkan untuk menghindari grafik yang harus digulir secara horizontal.

Beri label pada sumbu Anda, sediakan legenda jika diperlukan, dan tawarkan tooltip untuk pemahaman data yang lebih baik.

Jika data Anda berupa teks dan panjang pada sumbu X, Anda dapat memiringkan teks untuk meningkatkan keterbacaan. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) menawarkan pemetaan 3D, jika data Anda mendukungnya. Visualisasi data yang canggih dapat dibuat menggunakan `mpl_toolkits.mplot3d`.

![grafik 3D](../../../../3-Data-Visualization/13-meaningful-visualizations/images/3d.png)

## Tampilan grafik animasi dan 3D

Beberapa visualisasi data terbaik saat ini bersifat animasi. Shirley Wu memiliki karya luar biasa yang dibuat dengan D3, seperti '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', di mana setiap bunga adalah visualisasi dari sebuah film. Contoh lain untuk Guardian adalah 'bussed out', pengalaman interaktif yang menggabungkan visualisasi dengan Greensock dan D3 serta format artikel scrollytelling untuk menunjukkan bagaimana NYC menangani masalah tunawisma dengan mengirim orang keluar dari kota.

![busing](../../../../3-Data-Visualization/13-meaningful-visualizations/images/busing.png)

> "Bussed Out: How America Moves its Homeless" dari [the Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Visualisasi oleh Nadieh Bremer & Shirley Wu

Meskipun pelajaran ini tidak cukup mendalam untuk mengajarkan pustaka visualisasi yang kuat ini, cobalah menggunakan D3 dalam aplikasi Vue.js menggunakan pustaka untuk menampilkan visualisasi buku "Dangerous Liaisons" sebagai jaringan sosial animasi.

> "Les Liaisons Dangereuses" adalah novel epistolari, atau novel yang disajikan sebagai serangkaian surat. Ditulis pada tahun 1782 oleh Choderlos de Laclos, novel ini menceritakan tentang manuver sosial yang kejam dan tidak bermoral dari dua protagonis yang bersaing dari aristokrasi Prancis pada akhir abad ke-18, Vicomte de Valmont dan Marquise de Merteuil. Keduanya akhirnya mengalami kehancuran, tetapi tidak tanpa menyebabkan kerusakan sosial yang besar. Novel ini berkembang sebagai serangkaian surat yang ditulis kepada berbagai orang di lingkaran mereka, merencanakan balas dendam atau sekadar membuat masalah. Buat visualisasi surat-surat ini untuk menemukan tokoh utama dalam narasi, secara visual.

Anda akan menyelesaikan aplikasi web yang akan menampilkan tampilan animasi dari jaringan sosial ini. Aplikasi ini menggunakan pustaka yang dibuat untuk membuat [visualisasi jaringan](https://github.com/emiliorizzo/vue-d3-network) menggunakan Vue.js dan D3. Saat aplikasi berjalan, Anda dapat menarik node di layar untuk mengacak data.

![liaisons](../../../../3-Data-Visualization/13-meaningful-visualizations/images/liaisons.png)

## Proyek: Membuat grafik untuk menunjukkan jaringan menggunakan D3.js

> Folder pelajaran ini mencakup folder `solution` di mana Anda dapat menemukan proyek yang telah selesai, untuk referensi Anda.

1. Ikuti instruksi di file README.md di root folder starter. Pastikan Anda memiliki NPM dan Node.js yang berjalan di komputer Anda sebelum menginstal dependensi proyek Anda.

2. Buka folder `starter/src`. Anda akan menemukan folder `assets` di mana Anda dapat menemukan file .json dengan semua surat dari novel, diberi nomor, dengan anotasi 'to' dan 'from'.

3. Lengkapi kode di `components/Nodes.vue` untuk mengaktifkan visualisasi. Cari metode bernama `createLinks()` dan tambahkan loop bersarang berikut.

Loop melalui objek .json untuk menangkap data 'to' dan 'from' untuk surat-surat dan membangun objek `links` sehingga pustaka visualisasi dapat mengonsumsinya:

```javascript
//loop through letters
      let f = 0;
      let t = 0;
      for (var i = 0; i < letters.length; i++) {
          for (var j = 0; j < characters.length; j++) {
              
            if (characters[j] == letters[i].from) {
              f = j;
            }
            if (characters[j] == letters[i].to) {
              t = j;
            }
        }
        this.links.push({ sid: f, tid: t });
      }
  ```

Jalankan aplikasi Anda dari terminal (npm run serve) dan nikmati visualisasinya!

## 🚀 Tantangan

Jelajahi internet untuk menemukan visualisasi yang menyesatkan. Bagaimana penulis menipu pengguna, dan apakah itu disengaja? Cobalah memperbaiki visualisasi tersebut untuk menunjukkan bagaimana seharusnya tampilannya.

## [Kuis Pasca-Pelajaran](https://ff-quizzes.netlify.app/en/ds/quiz/25)

## Tinjauan & Studi Mandiri

Berikut adalah beberapa artikel untuk dibaca tentang visualisasi data yang menyesatkan:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Lihatlah visualisasi menarik ini untuk aset dan artefak sejarah:

https://handbook.pubpub.org/

Baca artikel ini tentang bagaimana animasi dapat meningkatkan visualisasi Anda:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Tugas

[Buat visualisasi kustom Anda sendiri](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.