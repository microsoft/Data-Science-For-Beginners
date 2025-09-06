<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "661dad02c3ac239644d34c1eb51e76f8",
  "translation_date": "2025-09-06T21:20:06+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "id"
}
-->
# Siklus Data Science: Menganalisis

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Siklus Data Science: Menganalisis - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

## [Kuis Pra-Kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Menganalisis dalam siklus data memastikan bahwa data dapat menjawab pertanyaan yang diajukan atau menyelesaikan masalah tertentu. Langkah ini juga dapat berfokus pada memastikan bahwa model secara tepat menangani pertanyaan dan masalah tersebut. Pelajaran ini berfokus pada Analisis Data Eksploratif atau EDA, yaitu teknik untuk mendefinisikan fitur dan hubungan dalam data serta dapat digunakan untuk mempersiapkan data untuk pemodelan.

Kami akan menggunakan dataset contoh dari [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) untuk menunjukkan bagaimana ini dapat diterapkan dengan Python dan pustaka Pandas. Dataset ini berisi jumlah beberapa kata umum yang ditemukan dalam email, sumber email ini bersifat anonim. Gunakan [notebook](notebook.ipynb) di direktori ini untuk mengikuti.

## Analisis Data Eksploratif

Tahap pengumpulan dalam siklus adalah tempat data diperoleh serta masalah dan pertanyaan yang ada, tetapi bagaimana kita tahu bahwa data dapat membantu mendukung hasil akhir? 
Ingat bahwa seorang data scientist mungkin akan mengajukan pertanyaan berikut saat mereka memperoleh data:
- Apakah saya memiliki cukup data untuk menyelesaikan masalah ini?
- Apakah kualitas data cukup baik untuk masalah ini?
- Jika saya menemukan informasi tambahan melalui data ini, haruskah kita mempertimbangkan untuk mengubah atau mendefinisikan ulang tujuan?
Analisis Data Eksploratif adalah proses untuk mengenal data tersebut dan dapat digunakan untuk menjawab pertanyaan-pertanyaan ini, serta mengidentifikasi tantangan dalam bekerja dengan dataset. Mari kita fokus pada beberapa teknik yang digunakan untuk mencapai hal ini.

## Profil Data, Statistik Deskriptif, dan Pandas
Bagaimana kita mengevaluasi apakah kita memiliki cukup data untuk menyelesaikan masalah ini? Profil data dapat meringkas dan mengumpulkan beberapa informasi umum tentang dataset kita melalui teknik statistik deskriptif. Profil data membantu kita memahami apa yang tersedia bagi kita, dan statistik deskriptif membantu kita memahami berapa banyak hal yang tersedia bagi kita.

Dalam beberapa pelajaran sebelumnya, kita telah menggunakan Pandas untuk menyediakan beberapa statistik deskriptif dengan fungsi [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Fungsi ini menyediakan jumlah, nilai maksimum dan minimum, rata-rata, deviasi standar, dan kuantil pada data numerik. Menggunakan statistik deskriptif seperti fungsi `describe()` dapat membantu Anda menilai seberapa banyak data yang Anda miliki dan apakah Anda membutuhkan lebih banyak.

## Sampling dan Querying
Menjelajahi seluruh dataset yang besar bisa sangat memakan waktu dan biasanya merupakan tugas yang dilakukan oleh komputer. Namun, sampling adalah alat yang berguna untuk memahami data dan memungkinkan kita memiliki pemahaman yang lebih baik tentang apa yang ada dalam dataset dan apa yang diwakilinya. Dengan sampel, Anda dapat menerapkan probabilitas dan statistik untuk membuat beberapa kesimpulan umum tentang data Anda. Meskipun tidak ada aturan yang pasti tentang seberapa banyak data yang harus Anda sampel, penting untuk dicatat bahwa semakin banyak data yang Anda sampel, semakin tepat generalisasi yang dapat Anda buat tentang data tersebut. 
Pandas memiliki fungsi [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) di pustakanya di mana Anda dapat memberikan argumen tentang berapa banyak sampel acak yang ingin Anda terima dan gunakan.

Querying umum terhadap data dapat membantu Anda menjawab beberapa pertanyaan dan teori umum yang mungkin Anda miliki. Berbeda dengan sampling, query memungkinkan Anda memiliki kontrol dan fokus pada bagian spesifik dari data yang Anda miliki pertanyaan tentangnya. 
Fungsi [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) di pustaka Pandas memungkinkan Anda memilih kolom dan menerima jawaban sederhana tentang data melalui baris yang diambil.

## Menjelajahi dengan Visualisasi
Anda tidak perlu menunggu hingga data benar-benar bersih dan dianalisis untuk mulai membuat visualisasi. Faktanya, memiliki representasi visual saat menjelajahi dapat membantu mengidentifikasi pola, hubungan, dan masalah dalam data. Selain itu, visualisasi menyediakan cara komunikasi dengan mereka yang tidak terlibat dalam pengelolaan data dan dapat menjadi kesempatan untuk berbagi dan memperjelas pertanyaan tambahan yang belum dijawab pada tahap pengumpulan. Lihat [bagian tentang Visualisasi](../../../../../../../../../3-Data-Visualization) untuk mempelajari lebih lanjut tentang beberapa cara populer untuk menjelajahi secara visual.

## Menjelajahi untuk Mengidentifikasi Ketidakkonsistenan
Semua topik dalam pelajaran ini dapat membantu mengidentifikasi nilai yang hilang atau tidak konsisten, tetapi Pandas menyediakan fungsi untuk memeriksa beberapa di antaranya. [isna() atau isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) dapat memeriksa nilai yang hilang. Salah satu bagian penting dari menjelajahi nilai-nilai ini dalam data Anda adalah menjelajahi mengapa mereka berakhir seperti itu sejak awal. Hal ini dapat membantu Anda memutuskan tindakan apa yang harus diambil untuk menyelesaikannya](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Kuis Pasca-Kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Tugas

[Menjelajahi untuk jawaban](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.