<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T19:00:32+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "id"
}
-->
# Mendefinisikan Ilmu Data

| ![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Mendefinisikan Ilmu Data - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_          |

---

[![Video Mendefinisikan Ilmu Data](../../../../translated_images/id/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Kuis sebelum kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Apa itu Data?
Dalam kehidupan sehari-hari, kita selalu dikelilingi oleh data. Teks yang sedang Anda baca sekarang adalah data. Daftar nomor telepon teman-teman Anda di ponsel adalah data, begitu juga dengan waktu saat ini yang ditampilkan di jam tangan Anda. Sebagai manusia, kita secara alami beroperasi dengan data, misalnya dengan menghitung uang yang kita miliki atau menulis surat kepada teman.

Namun, data menjadi jauh lebih penting dengan adanya komputer. Fungsi utama komputer adalah melakukan perhitungan, tetapi mereka membutuhkan data untuk diolah. Oleh karena itu, kita perlu memahami bagaimana komputer menyimpan dan memproses data.

Dengan munculnya Internet, peran komputer sebagai perangkat pengolah data semakin meningkat. Jika Anda memikirkannya, kita sekarang lebih sering menggunakan komputer untuk memproses dan berkomunikasi data daripada untuk perhitungan sebenarnya. Ketika kita menulis email kepada teman atau mencari informasi di Internet, kita pada dasarnya sedang membuat, menyimpan, mengirimkan, dan memanipulasi data.
> Bisakah Anda mengingat kapan terakhir kali Anda menggunakan komputer untuk benar-benar melakukan perhitungan?

## Apa itu Ilmu Data?

Menurut [Wikipedia](https://en.wikipedia.org/wiki/Data_science), **Ilmu Data** didefinisikan sebagai *bidang ilmiah yang menggunakan metode ilmiah untuk mengekstrak pengetahuan dan wawasan dari data terstruktur dan tidak terstruktur, serta menerapkan pengetahuan dan wawasan yang dapat ditindaklanjuti dari data di berbagai domain aplikasi*.

Definisi ini menyoroti aspek-aspek penting berikut dari ilmu data:

* Tujuan utama ilmu data adalah **mengekstrak pengetahuan** dari data, dengan kata lain - **memahami** data, menemukan hubungan tersembunyi, dan membangun **model**.
* Ilmu data menggunakan **metode ilmiah**, seperti probabilitas dan statistik. Faktanya, ketika istilah *ilmu data* pertama kali diperkenalkan, beberapa orang berpendapat bahwa ilmu data hanyalah nama baru yang keren untuk statistik. Namun, sekarang sudah jelas bahwa bidang ini jauh lebih luas.
* Pengetahuan yang diperoleh harus diterapkan untuk menghasilkan **wawasan yang dapat ditindaklanjuti**, yaitu wawasan praktis yang dapat diterapkan pada situasi bisnis nyata.
* Kita harus mampu mengoperasikan data yang **terstruktur** maupun **tidak terstruktur**. Kita akan kembali membahas berbagai jenis data ini nanti dalam kursus.
* **Domain aplikasi** adalah konsep penting, dan para ilmuwan data sering kali membutuhkan tingkat keahlian tertentu dalam domain masalah, misalnya: keuangan, kedokteran, pemasaran, dll.

> Aspek penting lainnya dari Ilmu Data adalah mempelajari bagaimana data dapat dikumpulkan, disimpan, dan dioperasikan menggunakan komputer. Sementara statistik memberikan dasar matematika, ilmu data menerapkan konsep matematika untuk benar-benar menarik wawasan dari data.

Salah satu cara (yang dikaitkan dengan [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) untuk melihat ilmu data adalah menganggapnya sebagai paradigma ilmu yang terpisah:
* **Empiris**, di mana kita lebih banyak mengandalkan pengamatan dan hasil eksperimen
* **Teoretis**, di mana konsep baru muncul dari pengetahuan ilmiah yang ada
* **Komputasional**, di mana kita menemukan prinsip baru berdasarkan beberapa eksperimen komputasi
* **Berbasis Data**, berdasarkan penemuan hubungan dan pola dalam data  

## Bidang Terkait Lainnya

Karena data ada di mana-mana, ilmu data sendiri juga merupakan bidang yang luas, yang menyentuh banyak disiplin ilmu lainnya.

<dl>
<dt>Basis Data</dt>
<dd>
Pertimbangan penting adalah <b>bagaimana menyimpan</b> data, yaitu bagaimana menyusunnya sedemikian rupa sehingga memungkinkan pemrosesan yang lebih cepat. Ada berbagai jenis basis data yang menyimpan data terstruktur dan tidak terstruktur, yang <a href="../../2-Working-With-Data/README.md">akan kita bahas dalam kursus ini</a>.
</dd>
<dt>Big Data</dt>
<dd>
Sering kali kita perlu menyimpan dan memproses data dalam jumlah besar dengan struktur yang relatif sederhana. Ada pendekatan dan alat khusus untuk menyimpan data tersebut secara terdistribusi di kluster komputer, dan memprosesnya secara efisien.
</dd>
<dt>Pembelajaran Mesin</dt>
<dd>
Salah satu cara untuk memahami data adalah dengan <b>membangun model</b> yang dapat memprediksi hasil yang diinginkan. Mengembangkan model dari data disebut <b>pembelajaran mesin</b>. Anda mungkin ingin melihat <a href="https://aka.ms/ml-beginners">Kurikulum Pembelajaran Mesin untuk Pemula</a> kami untuk mempelajari lebih lanjut tentang ini.
</dd>
<dt>Kecerdasan Buatan</dt>
<dd>
Sebuah area dari pembelajaran mesin yang dikenal sebagai kecerdasan buatan (AI) juga bergantung pada data, dan melibatkan pembangunan model dengan kompleksitas tinggi yang meniru proses berpikir manusia. Metode AI sering memungkinkan kita mengubah data tidak terstruktur (misalnya, bahasa alami) menjadi wawasan yang terstruktur.
</dd>
<dt>Visualisasi</dt>
<dd>
Jumlah data yang sangat besar sulit dipahami oleh manusia, tetapi begitu kita membuat visualisasi yang berguna menggunakan data tersebut, kita dapat lebih memahami data dan menarik kesimpulan. Oleh karena itu, penting untuk mengetahui banyak cara untuk memvisualisasikan informasi - sesuatu yang akan kita bahas di <a href="../../3-Data-Visualization/README.md">Bagian 3</a> dari kursus kita. Bidang terkait juga mencakup <b>Infografis</b>, dan <b>Interaksi Manusia-Komputer</b> secara umum.
</dd>
</dl>

## Jenis Data

Seperti yang telah disebutkan, data ada di mana-mana. Kita hanya perlu menangkapnya dengan cara yang tepat! Penting untuk membedakan antara data **terstruktur** dan **tidak terstruktur**. Data terstruktur biasanya direpresentasikan dalam bentuk yang terorganisir dengan baik, sering kali sebagai tabel atau sejumlah tabel, sedangkan data tidak terstruktur hanyalah kumpulan file. Kadang-kadang kita juga dapat berbicara tentang data **semi-terstruktur**, yang memiliki semacam struktur yang dapat sangat bervariasi.

| Terstruktur                                                                  | Semi-terstruktur                                                                              | Tidak terstruktur                       |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------- |
| Daftar orang dengan nomor telepon mereka                                     | Halaman Wikipedia dengan tautan                                                              | Teks dari Ensiklopedia Britannica      |
| Suhu di semua ruangan gedung setiap menit selama 20 tahun terakhir           | Koleksi makalah ilmiah dalam format JSON dengan penulis, tanggal publikasi, dan abstrak      | Berkas video mentah dari kamera pengawas |
| Data usia dan jenis kelamin semua orang yang masuk ke gedung                 | Halaman Internet                                                                             | File berbagi dokumen perusahaan         |

## Dari Mana Mendapatkan Data

Ada banyak sumber data yang mungkin, dan akan sulit untuk mencantumkan semuanya! Namun, mari kita sebutkan beberapa tempat khas di mana Anda dapat memperoleh data:

* **Terstruktur**
  - **Internet of Things** (IoT), termasuk data dari berbagai sensor, seperti sensor suhu atau tekanan, menyediakan banyak data yang berguna. Misalnya, jika sebuah gedung perkantoran dilengkapi dengan sensor IoT, kita dapat secara otomatis mengontrol pemanasan dan pencahayaan untuk meminimalkan biaya.
  - **Survei** yang kita minta pengguna untuk diisi setelah pembelian, atau setelah mengunjungi situs web.
  - **Analisis perilaku** dapat, misalnya, membantu kita memahami seberapa dalam seorang pengguna menjelajahi situs, dan apa alasan umum mereka meninggalkan situs.
* **Tidak terstruktur**
  - **Teks** dapat menjadi sumber wawasan yang kaya, seperti skor **sentimen keseluruhan**, atau ekstraksi kata kunci dan makna semantik.
  - **Gambar** atau **Video**. Video dari kamera pengawas dapat digunakan untuk memperkirakan lalu lintas di jalan, dan memberi tahu orang-orang tentang potensi kemacetan.
  - **Log** server web dapat digunakan untuk memahami halaman mana dari situs kita yang paling sering dikunjungi, dan berapa lama.
* Semi-terstruktur
  - Grafik **Jejaring Sosial** dapat menjadi sumber data yang hebat tentang kepribadian pengguna dan potensi efektivitas dalam menyebarkan informasi.
  - Ketika kita memiliki banyak foto dari sebuah pesta, kita dapat mencoba mengekstrak data **Dinamika Kelompok** dengan membangun grafik orang-orang yang berfoto bersama.

Dengan mengetahui berbagai sumber data yang mungkin, Anda dapat mencoba memikirkan berbagai skenario di mana teknik ilmu data dapat diterapkan untuk memahami situasi dengan lebih baik, dan untuk meningkatkan proses bisnis.

## Apa yang Bisa Dilakukan dengan Data

Dalam Ilmu Data, kita fokus pada langkah-langkah berikut dalam perjalanan data:

<dl>
<dt>1) Akuisisi Data</dt>
<dd>
Langkah pertama adalah mengumpulkan data. Meskipun dalam banyak kasus ini bisa menjadi proses yang sederhana, seperti data yang masuk ke basis data dari aplikasi web, terkadang kita perlu menggunakan teknik khusus. Misalnya, data dari sensor IoT bisa sangat besar, dan praktik yang baik adalah menggunakan titik akhir buffering seperti IoT Hub untuk mengumpulkan semua data sebelum diproses lebih lanjut.
</dd>
<dt>2) Penyimpanan Data</dt>
<dd>
Menyimpan data bisa menjadi tantangan, terutama jika kita berbicara tentang big data. Saat memutuskan bagaimana menyimpan data, masuk akal untuk memperkirakan cara Anda ingin melakukan kueri data di masa depan. Ada beberapa cara data dapat disimpan:
<ul>
<li>Basis data relasional menyimpan kumpulan tabel, dan menggunakan bahasa khusus yang disebut SQL untuk melakukan kueri. Biasanya, tabel diorganisasikan ke dalam kelompok yang berbeda yang disebut skema. Dalam banyak kasus, kita perlu mengonversi data dari bentuk aslinya agar sesuai dengan skema.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">Basis data NoSQL</a>, seperti <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, tidak memaksakan skema pada data, dan memungkinkan penyimpanan data yang lebih kompleks, misalnya dokumen JSON hierarkis atau grafik. Namun, basis data NoSQL tidak memiliki kemampuan kueri yang kaya seperti SQL, dan tidak dapat menegakkan integritas referensial, yaitu aturan tentang bagaimana data disusun dalam tabel dan mengatur hubungan antar tabel.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Penyimpanan Data Lake</a> digunakan untuk koleksi besar data dalam bentuk mentah, tidak terstruktur. Data lake sering digunakan dengan big data, di mana semua data tidak dapat muat di satu mesin, dan harus disimpan serta diproses oleh kluster server. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> adalah format data yang sering digunakan bersama dengan big data.</li> 
</ul>
</dd>
<dt>3) Pemrosesan Data</dt>
<dd>
Ini adalah bagian paling menarik dari perjalanan data, yang melibatkan konversi data dari bentuk aslinya ke bentuk yang dapat digunakan untuk visualisasi/pelatihan model. Ketika berurusan dengan data tidak terstruktur seperti teks atau gambar, kita mungkin perlu menggunakan beberapa teknik AI untuk mengekstrak <b>fitur</b> dari data, sehingga mengonversinya ke bentuk terstruktur.
</dd>
<dt>4) Visualisasi / Wawasan Manusia</dt>
<dd>
Sering kali, untuk memahami data, kita perlu memvisualisasikannya. Dengan memiliki banyak teknik visualisasi yang berbeda dalam kotak alat kita, kita dapat menemukan tampilan yang tepat untuk mendapatkan wawasan. Sering kali, seorang ilmuwan data perlu "bermain dengan data", memvisualisasikannya berkali-kali dan mencari beberapa hubungan. Selain itu, kita dapat menggunakan teknik statistik untuk menguji hipotesis atau membuktikan korelasi antara berbagai bagian data.
</dd>
<dt>5) Melatih model prediktif</dt>
<dd>
Karena tujuan utama ilmu data adalah untuk dapat membuat keputusan berdasarkan data, kita mungkin ingin menggunakan teknik <a href="http://github.com/microsoft/ml-for-beginners">Pembelajaran Mesin</a> untuk membangun model prediktif. Kita kemudian dapat menggunakan ini untuk membuat prediksi menggunakan kumpulan data baru dengan struktur yang serupa.
</dd>
</dl>

Tentu saja, tergantung pada data yang sebenarnya, beberapa langkah mungkin tidak ada (misalnya, ketika kita sudah memiliki data di basis data, atau ketika kita tidak memerlukan pelatihan model), atau beberapa langkah mungkin diulang beberapa kali (seperti pemrosesan data).

## Digitalisasi dan Transformasi Digital

Dalam dekade terakhir, banyak bisnis mulai memahami pentingnya data dalam pengambilan keputusan bisnis. Untuk menerapkan prinsip-prinsip ilmu data dalam menjalankan bisnis, pertama-tama kita perlu mengumpulkan beberapa data, yaitu menerjemahkan proses bisnis ke dalam bentuk digital. Ini dikenal sebagai **digitalisasi**. Menerapkan teknik ilmu data pada data ini untuk memandu keputusan dapat menghasilkan peningkatan produktivitas yang signifikan (atau bahkan perubahan arah bisnis), yang disebut **transformasi digital**.

Mari kita pertimbangkan sebuah contoh. Misalkan kita memiliki kursus ilmu data (seperti ini) yang kita sampaikan secara online kepada siswa, dan kita ingin menggunakan ilmu data untuk meningkatkannya. Bagaimana kita bisa melakukannya?

Kita bisa mulai dengan bertanya "Apa yang bisa didigitalisasi?" Cara paling sederhana adalah mengukur waktu yang dibutuhkan setiap siswa untuk menyelesaikan setiap modul, dan mengukur pengetahuan yang diperoleh dengan memberikan tes pilihan ganda di akhir setiap modul. Dengan merata-rata waktu penyelesaian di seluruh siswa, kita dapat mengetahui modul mana yang paling sulit bagi siswa, dan bekerja untuk menyederhanakannya.
> Anda mungkin berpendapat bahwa pendekatan ini tidak ideal, karena modul dapat memiliki panjang yang berbeda. Mungkin lebih adil untuk membagi waktu dengan panjang modul (dalam jumlah karakter), dan membandingkan nilai-nilai tersebut.

Ketika kita mulai menganalisis hasil tes pilihan ganda, kita dapat mencoba menentukan konsep mana yang sulit dipahami oleh siswa, dan menggunakan informasi tersebut untuk meningkatkan konten. Untuk melakukan itu, kita perlu merancang tes sedemikian rupa sehingga setiap pertanyaan terhubung dengan konsep atau bagian pengetahuan tertentu.

Jika kita ingin lebih rumit lagi, kita dapat memplot waktu yang dihabiskan untuk setiap modul terhadap kategori usia siswa. Kita mungkin menemukan bahwa untuk beberapa kategori usia, diperlukan waktu yang tidak wajar untuk menyelesaikan modul, atau siswa berhenti sebelum menyelesaikannya. Hal ini dapat membantu kita memberikan rekomendasi usia untuk modul tersebut, dan meminimalkan ketidakpuasan orang dari ekspektasi yang salah.

## 🚀 Tantangan

Dalam tantangan ini, kita akan mencoba menemukan konsep-konsep yang relevan dengan bidang Data Science dengan melihat teks. Kita akan mengambil artikel Wikipedia tentang Data Science, mengunduh dan memproses teksnya, lalu membuat word cloud seperti ini:

![Word Cloud untuk Data Science](../../../../translated_images/id/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Kunjungi [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') untuk membaca kode. Anda juga dapat menjalankan kode tersebut, dan melihat bagaimana kode tersebut melakukan semua transformasi data secara real-time.

> Jika Anda tidak tahu cara menjalankan kode di Jupyter Notebook, lihat [artikel ini](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Kuis setelah kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Tugas

* **Tugas 1**: Modifikasi kode di atas untuk menemukan konsep terkait untuk bidang **Big Data** dan **Machine Learning**
* **Tugas 2**: [Pikirkan Tentang Skenario Data Science](assignment.md)

## Kredit

Pelajaran ini dibuat dengan ♥️ oleh [Dmitry Soshnikov](http://soshnikov.com)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang salah yang timbul dari penggunaan terjemahan ini.