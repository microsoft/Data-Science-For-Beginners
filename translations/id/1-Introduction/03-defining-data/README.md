# Mendefinisikan Data

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Mendefinisikan Data - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Data adalah fakta, informasi, pengamatan dan pengukuran yang digunakan untuk membuat penemuan dan mendukung keputusan yang berinformasi. Sebuah titik data adalah satu unit data dalam sebuah dataset, yang merupakan kumpulan titik data. Dataset dapat datang dalam format dan struktur yang berbeda-beda, dan biasanya akan berdasarkan sumbernya, atau dari mana data berasal. Misalnya, pendapatan bulanan sebuah perusahaan mungkin ada dalam spreadsheet tetapi data detak jantung per jam dari smartwatch mungkin dalam format [JSON](https://stackoverflow.com/a/383699). Umum bagi ilmuwan data untuk bekerja dengan berbagai jenis data dalam sebuah dataset.

Pelajaran ini berfokus pada mengidentifikasi dan mengklasifikasikan data berdasarkan karakteristik dan sumbernya.

## [Kuis Pra-Kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Bagaimana Data Dijelaskan

### Data Mentah
Data mentah adalah data yang berasal dari sumbernya dalam keadaan awal dan belum dianalisis atau diorganisasi. Untuk memahami apa yang sedang terjadi dengan sebuah dataset, data perlu diatur dalam format yang dapat dipahami oleh manusia maupun teknologi yang mungkin digunakan untuk menganalisis lebih lanjut. Struktur sebuah dataset menggambarkan bagaimana data diorganisasi dan dapat diklasifikasikan sebagai terstruktur, tidak terstruktur, dan semi-terstruktur. Jenis-jenis struktur ini akan bervariasi tergantung pada sumber tetapi pada akhirnya masuk dalam tiga kategori ini.

### Data Kuantitatif
Data kuantitatif adalah pengamatan numerik dalam sebuah dataset dan biasanya dapat dianalisis, diukur, dan digunakan secara matematis. Beberapa contoh data kuantitatif adalah: populasi sebuah negara, tinggi badan seseorang, atau pendapatan kuartalan sebuah perusahaan. Dengan analisis tambahan, data kuantitatif dapat digunakan untuk menemukan tren musiman Indeks Kualitas Udara (AQI) atau memperkirakan kemungkinan kemacetan pada jam sibuk di hari kerja biasa.

### Data Kualitatif
Data kualitatif, juga dikenal sebagai data kategorikal, adalah data yang tidak dapat diukur secara objektif seperti pengamatan data kuantitatif. Ini umumnya berupa berbagai format data subjektif yang menangkap kualitas sesuatu, seperti produk atau proses. Kadang-kadang, data kualitatif berupa angka dan biasanya tidak digunakan secara matematis, seperti nomor telepon atau cap waktu. Beberapa contoh data kualitatif adalah: komentar video, merek dan model mobil, atau warna favorit teman dekat Anda. Data kualitatif dapat digunakan untuk memahami produk apa yang paling disukai konsumen atau mengidentifikasi kata kunci populer dalam resume lamaran kerja.

### Data Terstruktur
Data terstruktur adalah data yang diorganisasi ke dalam baris dan kolom, di mana setiap baris memiliki set kolom yang sama. Kolom mewakili nilai dari tipe tertentu dan akan diidentifikasi dengan nama yang menggambarkan apa yang direpresentasikan nilai tersebut, sementara baris berisi nilai-nilai sebenarnya. Kolom sering memiliki seperangkat aturan atau batasan pada nilainya, untuk memastikan bahwa nilai tersebut akurat merepresentasikan kolom. Misalnya bayangkan sebuah spreadsheet pelanggan di mana setiap baris harus memiliki nomor telepon dan nomor telepon tidak pernah berisi karakter alfabet. Mungkin ada aturan yang diterapkan pada kolom nomor telepon untuk memastikan kolom tersebut tidak kosong dan hanya berisi angka.

Keuntungan dari data terstruktur adalah dapat diatur sedemikian rupa sehingga dapat dihubungkan dengan data terstruktur lainnya. Namun, karena data dirancang untuk diatur dengan cara tertentu, membuat perubahan pada keseluruhan strukturnya bisa memerlukan banyak usaha. Contohnya, menambahkan kolom email pada spreadsheet pelanggan yang tidak boleh kosong berarti Anda harus mencari cara untuk menambahkan nilai-nilai ini ke baris pelanggan yang sudah ada di dataset.

Contoh data terstruktur: spreadsheet, basis data relasional, nomor telepon, laporan bank

### Data Tidak Terstruktur
Data tidak terstruktur biasanya tidak dapat dikategorikan ke dalam baris atau kolom dan tidak memiliki format atau aturan yang harus diikuti. Karena data tidak terstruktur memiliki lebih sedikit batasan pada strukturnya, lebih mudah untuk menambah informasi baru dibandingkan dengan dataset terstruktur. Jika sensor yang menangkap data tekanan barometrik setiap 2 menit menerima pembaruan yang memungkinkan mengukur dan merekam suhu, maka tidak perlu mengubah data yang sudah ada jika data tidak terstruktur. Namun, hal ini dapat membuat analisis atau penyelidikan jenis data ini menjadi lebih lama. Misalnya, seorang ilmuwan yang ingin mencari suhu rata-rata bulan sebelumnya dari data sensor, tetapi menemukan bahwa sensor merekam "e" dalam beberapa data untuk menunjukkan bahwa sensor rusak, bukan angka biasa, berarti data tidak lengkap.

Contoh data tidak terstruktur: berkas teks, pesan teks, berkas video

### Semi-terstruktur
Data semi-terstruktur memiliki fitur yang menjadikannya kombinasi antara data terstruktur dan tidak terstruktur. Data ini biasanya tidak mengikuti format baris dan kolom tetapi diatur dengan cara yang dianggap terstruktur dan mungkin mengikuti format atau aturan tetap. Struktur akan bervariasi antara sumber, seperti hierarki yang terdefinisi dengan baik hingga sesuatu yang lebih fleksibel yang memungkinkan integrasi informasi baru dengan mudah. Metadata adalah indikator yang membantu menentukan bagaimana data diorganisasi dan disimpan dan akan memiliki berbagai nama, berdasarkan tipe data. Beberapa nama umum untuk metadata adalah tag, elemen, entitas, dan atribut. Contohnya, sebuah pesan email biasanya memiliki subjek, isi, dan daftar penerima dan dapat diorganisasi berdasarkan pengirim atau waktu pengiriman.

Contoh data semi-terstruktur: HTML, berkas CSV, JavaScript Object Notation (JSON)

## Sumber Data

Sumber data adalah lokasi awal di mana data dihasilkan, atau di mana data "tinggal" dan bervariasi berdasarkan bagaimana dan kapan data dikumpulkan. Data yang dihasilkan oleh penggunanya disebut data primer sementara data sekunder berasal dari sumber yang mengumpulkan data untuk penggunaan umum. Misalnya, sekelompok ilmuwan yang mengumpulkan pengamatan di hutan hujan dianggap sebagai data primer, dan jika mereka memutuskan membagikannya dengan ilmuwan lain, itu menjadi data sekunder bagi yang menggunakannya.

Basis data adalah sumber umum dan mengandalkan sistem manajemen basis data untuk meng-host dan memelihara data di mana pengguna menggunakan perintah yang disebut kueri untuk menjelajahi data. Berkas sebagai sumber data bisa berupa berkas audio, gambar, dan video serta spreadsheet seperti Excel. Sumber internet adalah lokasi umum untuk men-host data, di mana basis data maupun berkas dapat ditemukan. Antarmuka pemrograman aplikasi, yang dikenal sebagai API, memungkinkan programmer membuat cara untuk berbagi data dengan pengguna eksternal melalui internet, sementara proses web scraping mengekstrak data dari halaman web. [Pelajaran di Bekerja dengan Data](../../../../../../../../../2-Working-With-Data) berfokus pada bagaimana menggunakan berbagai sumber data.

## Kesimpulan

Dalam pelajaran ini kita telah mempelajari:

- Apa itu data
- Bagaimana data dijelaskan
- Bagaimana data diklasifikasikan dan dikategorikan
- Di mana data dapat ditemukan

## 🚀 Tantangan

Kaggle adalah sumber dataset terbuka yang sangat baik. Gunakan [alat pencarian dataset](https://www.kaggle.com/datasets) untuk menemukan beberapa dataset menarik dan klasifikasikan 3-5 dataset dengan kriteria ini:

- Apakah data kuantitatif atau kualitatif?
- Apakah data terstruktur, tidak terstruktur, atau semi-terstruktur?

## [Kuis Pasca-kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Tinjauan & Belajar Mandiri

- Unit Microsoft Learn ini, berjudul [Identify data formats](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) memiliki penjelasan rinci tentang data terstruktur, semi-terstruktur, dan tidak terstruktur.

## Tugas

[Mengklasifikasikan Dataset](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->