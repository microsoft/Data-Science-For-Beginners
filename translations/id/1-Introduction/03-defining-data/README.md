<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T23:59:07+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "id"
}
-->
# Mendefinisikan Data

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Mendefinisikan Data - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Data adalah fakta, informasi, observasi, dan pengukuran yang digunakan untuk membuat penemuan dan mendukung pengambilan keputusan yang terinformasi. Sebuah titik data adalah satu unit data dalam sebuah dataset, yang merupakan kumpulan dari titik-titik data. Dataset dapat hadir dalam berbagai format dan struktur, biasanya berdasarkan sumbernya atau dari mana data tersebut berasal. Sebagai contoh, pendapatan bulanan sebuah perusahaan mungkin disimpan dalam spreadsheet, sedangkan data detak jantung per jam dari smartwatch mungkin dalam format [JSON](https://stackoverflow.com/a/383699). Umumnya, ilmuwan data bekerja dengan berbagai jenis data dalam sebuah dataset.

Pelajaran ini berfokus pada mengidentifikasi dan mengklasifikasikan data berdasarkan karakteristik dan sumbernya.

## [Kuis Pra-Pelajaran](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Bagaimana Data Dijelaskan

### Data Mentah
Data mentah adalah data yang berasal dari sumbernya dalam keadaan awal dan belum dianalisis atau diorganisasi. Untuk memahami apa yang terjadi dalam sebuah dataset, data perlu diorganisasi ke dalam format yang dapat dipahami oleh manusia serta teknologi yang mungkin digunakan untuk menganalisisnya lebih lanjut. Struktur dataset menggambarkan bagaimana data diorganisasi dan dapat diklasifikasikan sebagai terstruktur, tidak terstruktur, dan semi-terstruktur. Jenis struktur ini akan bervariasi tergantung pada sumbernya, tetapi pada akhirnya akan masuk ke dalam tiga kategori ini.

### Data Kuantitatif
Data kuantitatif adalah observasi numerik dalam sebuah dataset yang biasanya dapat dianalisis, diukur, dan digunakan secara matematis. Beberapa contoh data kuantitatif adalah: populasi suatu negara, tinggi badan seseorang, atau pendapatan kuartalan sebuah perusahaan. Dengan analisis tambahan, data kuantitatif dapat digunakan untuk menemukan tren musiman pada Indeks Kualitas Udara (AQI) atau memperkirakan kemungkinan kemacetan lalu lintas pada hari kerja biasa.

### Data Kualitatif
Data kualitatif, juga dikenal sebagai data kategorikal, adalah data yang tidak dapat diukur secara objektif seperti observasi data kuantitatif. Umumnya, data ini berupa berbagai format data subjektif yang menangkap kualitas sesuatu, seperti produk atau proses. Kadang-kadang, data kualitatif bersifat numerik tetapi tidak digunakan secara matematis, seperti nomor telepon atau stempel waktu. Beberapa contoh data kualitatif adalah: komentar video, merek dan model mobil, atau warna favorit teman terdekat Anda. Data kualitatif dapat digunakan untuk memahami produk mana yang paling disukai konsumen atau mengidentifikasi kata kunci populer dalam resume lamaran kerja.

### Data Terstruktur
Data terstruktur adalah data yang diorganisasi ke dalam baris dan kolom, di mana setiap baris memiliki set kolom yang sama. Kolom mewakili nilai dari jenis tertentu dan akan diidentifikasi dengan nama yang menggambarkan apa yang diwakili oleh nilai tersebut, sementara baris berisi nilai-nilai aktual. Kolom sering kali memiliki serangkaian aturan atau batasan tertentu pada nilai-nilai, untuk memastikan bahwa nilai-nilai tersebut secara akurat mewakili kolom. Sebagai contoh, bayangkan sebuah spreadsheet pelanggan di mana setiap baris harus memiliki nomor telepon dan nomor telepon tersebut tidak pernah mengandung karakter alfabet. Mungkin ada aturan yang diterapkan pada kolom nomor telepon untuk memastikan kolom tersebut tidak pernah kosong dan hanya berisi angka.

Keuntungan dari data terstruktur adalah bahwa data dapat diorganisasi sedemikian rupa sehingga dapat dihubungkan dengan data terstruktur lainnya. Namun, karena data dirancang untuk diorganisasi dengan cara tertentu, membuat perubahan pada struktur keseluruhannya dapat memerlukan banyak usaha. Sebagai contoh, menambahkan kolom email ke spreadsheet pelanggan yang tidak boleh kosong berarti Anda perlu mencari cara untuk menambahkan nilai-nilai ini ke baris pelanggan yang sudah ada dalam dataset.

Contoh data terstruktur: spreadsheet, basis data relasional, nomor telepon, laporan bank.

### Data Tidak Terstruktur
Data tidak terstruktur biasanya tidak dapat dikategorikan ke dalam baris atau kolom dan tidak memiliki format atau aturan tertentu untuk diikuti. Karena data tidak terstruktur memiliki lebih sedikit batasan pada strukturnya, lebih mudah untuk menambahkan informasi baru dibandingkan dengan dataset terstruktur. Jika sebuah sensor yang menangkap data tekanan barometrik setiap 2 menit menerima pembaruan yang sekarang memungkinkan sensor tersebut mengukur dan merekam suhu, tidak diperlukan perubahan pada data yang sudah ada jika data tersebut tidak terstruktur. Namun, ini mungkin membuat analisis atau investigasi data jenis ini memakan waktu lebih lama. Sebagai contoh, seorang ilmuwan yang ingin menemukan suhu rata-rata bulan sebelumnya dari data sensor, tetapi menemukan bahwa sensor mencatat "e" dalam beberapa datanya untuk menunjukkan bahwa sensor tersebut rusak, bukan angka biasa, yang berarti data tersebut tidak lengkap.

Contoh data tidak terstruktur: file teks, pesan teks, file video.

### Data Semi-Terstruktur
Data semi-terstruktur memiliki fitur yang membuatnya menjadi kombinasi antara data terstruktur dan tidak terstruktur. Data ini biasanya tidak mengikuti format baris dan kolom tetapi diorganisasi dengan cara yang dianggap terstruktur dan mungkin mengikuti format tetap atau aturan tertentu. Struktur ini akan bervariasi antara sumber, seperti hierarki yang terdefinisi dengan baik hingga sesuatu yang lebih fleksibel yang memungkinkan integrasi informasi baru dengan mudah. Metadata adalah indikator yang membantu menentukan bagaimana data diorganisasi dan disimpan, serta memiliki berbagai nama berdasarkan jenis data. Beberapa nama umum untuk metadata adalah tag, elemen, entitas, dan atribut. Sebagai contoh, sebuah pesan email biasa akan memiliki subjek, isi, dan daftar penerima, serta dapat diorganisasi berdasarkan siapa atau kapan pesan tersebut dikirim.

Contoh data semi-terstruktur: HTML, file CSV, JavaScript Object Notation (JSON).

## Sumber Data 

Sumber data adalah lokasi awal di mana data dihasilkan, atau di mana data "berada" dan akan bervariasi berdasarkan bagaimana dan kapan data dikumpulkan. Data yang dihasilkan oleh penggunanya dikenal sebagai data primer, sedangkan data sekunder berasal dari sumber yang telah mengumpulkan data untuk penggunaan umum. Sebagai contoh, sekelompok ilmuwan yang mengumpulkan observasi di hutan hujan akan dianggap sebagai data primer, dan jika mereka memutuskan untuk membagikannya dengan ilmuwan lain, data tersebut akan dianggap sebagai data sekunder bagi mereka yang menggunakannya.

Basis data adalah sumber yang umum dan bergantung pada sistem manajemen basis data untuk meng-host dan memelihara data, di mana pengguna menggunakan perintah yang disebut kueri untuk mengeksplorasi data. File sebagai sumber data dapat berupa file audio, gambar, dan video serta spreadsheet seperti Excel. Sumber internet adalah lokasi umum untuk meng-host data, di mana basis data serta file dapat ditemukan. Antarmuka pemrograman aplikasi, juga dikenal sebagai API, memungkinkan programmer untuk membuat cara berbagi data dengan pengguna eksternal melalui internet, sementara proses web scraping mengekstrak data dari halaman web. [Pelajaran dalam Bekerja dengan Data](../../../../../../../../../2-Working-With-Data) berfokus pada cara menggunakan berbagai sumber data.

## Kesimpulan

Dalam pelajaran ini kita telah mempelajari:

- Apa itu data
- Bagaimana data dijelaskan
- Bagaimana data diklasifikasikan dan dikategorikan
- Di mana data dapat ditemukan

## 🚀 Tantangan

Kaggle adalah sumber yang sangat baik untuk dataset terbuka. Gunakan [alat pencarian dataset](https://www.kaggle.com/datasets) untuk menemukan beberapa dataset menarik dan klasifikasikan 3-5 dataset dengan kriteria ini:

- Apakah data tersebut kuantitatif atau kualitatif?
- Apakah data tersebut terstruktur, tidak terstruktur, atau semi-terstruktur?

## [Kuis Pasca-Pelajaran](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Tinjauan & Studi Mandiri

- Unit Microsoft Learn ini, berjudul [Classify your Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) memiliki penjelasan rinci tentang data terstruktur, semi-terstruktur, dan tidak terstruktur.

## Tugas

[Mengklasifikasikan Dataset](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.