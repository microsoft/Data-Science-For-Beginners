<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a167aa0bfb1c46ece1b3d21ae939cc0d",
  "translation_date": "2025-09-04T20:34:47+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "id"
}
-->
# Siklus Data Science: Analisis

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Siklus Data Science: Analisis - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

## Kuis Sebelum Kuliah

## [Kuis Sebelum Kuliah](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Analisis dalam siklus data memastikan bahwa data dapat menjawab pertanyaan yang diajukan atau menyelesaikan masalah tertentu. Langkah ini juga dapat berfokus pada memastikan bahwa model secara tepat menangani pertanyaan dan masalah tersebut. Pelajaran ini berfokus pada Analisis Data Eksploratif atau EDA, yaitu teknik untuk mendefinisikan fitur dan hubungan dalam data serta dapat digunakan untuk mempersiapkan data untuk pemodelan.

Kami akan menggunakan dataset contoh dari [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) untuk menunjukkan bagaimana ini dapat diterapkan dengan Python dan pustaka Pandas. Dataset ini berisi jumlah beberapa kata umum yang ditemukan dalam email, sumber email ini bersifat anonim. Gunakan [notebook](notebook.ipynb) di direktori ini untuk mengikuti langkah-langkahnya.

## Analisis Data Eksploratif

Tahap pengumpulan dalam siklus adalah saat data diperoleh serta masalah dan pertanyaan yang ada, tetapi bagaimana kita tahu bahwa data dapat mendukung hasil akhir? 
Ingatlah bahwa seorang data scientist mungkin akan mengajukan pertanyaan berikut saat mereka memperoleh data:
- Apakah saya memiliki cukup data untuk menyelesaikan masalah ini?
- Apakah kualitas data cukup baik untuk masalah ini?
- Jika saya menemukan informasi tambahan melalui data ini, haruskah kita mempertimbangkan untuk mengubah atau mendefinisikan ulang tujuan?
Analisis Data Eksploratif adalah proses untuk mengenal data tersebut dan dapat digunakan untuk menjawab pertanyaan-pertanyaan ini, serta mengidentifikasi tantangan dalam bekerja dengan dataset. Mari kita fokus pada beberapa teknik yang digunakan untuk mencapai hal ini.

## Profiling Data, Statistik Deskriptif, dan Pandas
Bagaimana kita mengevaluasi apakah kita memiliki cukup data untuk menyelesaikan masalah ini? Profiling data dapat merangkum dan mengumpulkan beberapa informasi umum tentang dataset kita melalui teknik statistik deskriptif. Profiling data membantu kita memahami apa yang tersedia bagi kita, dan statistik deskriptif membantu kita memahami seberapa banyak yang tersedia bagi kita.

Dalam beberapa pelajaran sebelumnya, kita telah menggunakan Pandas untuk menyediakan beberapa statistik deskriptif dengan [`describe()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Fungsi ini memberikan jumlah, nilai maksimum dan minimum, rata-rata, deviasi standar, dan kuantil pada data numerik. Menggunakan statistik deskriptif seperti fungsi `describe()` dapat membantu Anda menilai seberapa banyak data yang Anda miliki dan apakah Anda membutuhkan lebih banyak.

## Sampling dan Querying
Mengeksplorasi seluruh dataset yang besar bisa sangat memakan waktu dan biasanya merupakan tugas yang dilakukan oleh komputer. Namun, sampling adalah alat yang berguna untuk memahami data dan memungkinkan kita memiliki pemahaman yang lebih baik tentang apa yang ada dalam dataset dan apa yang diwakilinya. Dengan sampel, Anda dapat menerapkan probabilitas dan statistik untuk membuat beberapa kesimpulan umum tentang data Anda. Meskipun tidak ada aturan yang pasti tentang seberapa banyak data yang harus Anda sampel, penting untuk dicatat bahwa semakin banyak data yang Anda sampel, semakin tepat generalisasi yang dapat Anda buat tentang data tersebut. 
Pandas memiliki [`sample()` function dalam pustakanya](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) di mana Anda dapat memberikan argumen tentang berapa banyak sampel acak yang ingin Anda terima dan gunakan.

Querying umum pada data dapat membantu Anda menjawab beberapa pertanyaan dan teori umum yang mungkin Anda miliki. Berbeda dengan sampling, query memungkinkan Anda memiliki kontrol dan fokus pada bagian spesifik dari data yang Anda pertanyakan. 
Fungsi [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) dalam pustaka Pandas memungkinkan Anda memilih kolom dan menerima jawaban sederhana tentang data melalui baris yang diambil.

## Mengeksplorasi dengan Visualisasi
Anda tidak perlu menunggu hingga data benar-benar bersih dan dianalisis untuk mulai membuat visualisasi. Faktanya, memiliki representasi visual saat mengeksplorasi dapat membantu mengidentifikasi pola, hubungan, dan masalah dalam data. Selain itu, visualisasi menyediakan cara komunikasi dengan mereka yang tidak terlibat dalam pengelolaan data dan dapat menjadi kesempatan untuk berbagi dan mengklarifikasi pertanyaan tambahan yang belum dijawab pada tahap pengumpulan. Lihat [bagian tentang Visualisasi](../../../../../../../../../3-Data-Visualization) untuk mempelajari lebih lanjut tentang beberapa cara populer untuk mengeksplorasi secara visual.

## Mengeksplorasi untuk Mengidentifikasi Ketidakkonsistenan
Semua topik dalam pelajaran ini dapat membantu mengidentifikasi nilai yang hilang atau tidak konsisten, tetapi Pandas menyediakan fungsi untuk memeriksa beberapa di antaranya. [isna() atau isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) dapat memeriksa nilai yang hilang. Salah satu bagian penting dari eksplorasi nilai-nilai ini dalam data Anda adalah mengeksplorasi mengapa mereka berakhir seperti itu sejak awal. Hal ini dapat membantu Anda memutuskan tindakan apa yang [harus diambil untuk menyelesaikannya](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Kuis Setelah Kuliah](https://ff-quizzes.netlify.app/en/ds/)

## Tugas

[Mengeksplorasi untuk jawaban](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.