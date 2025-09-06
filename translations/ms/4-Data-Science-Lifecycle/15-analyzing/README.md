<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "661dad02c3ac239644d34c1eb51e76f8",
  "translation_date": "2025-09-06T21:22:03+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "ms"
}
-->
# Kitaran Hayat Sains Data: Menganalisis

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Kitaran Hayat Sains Data: Menganalisis - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

## [Kuiz Pra-Kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Menganalisis dalam kitaran hayat data mengesahkan bahawa data boleh menjawab soalan yang dicadangkan atau menyelesaikan masalah tertentu. Langkah ini juga boleh memberi tumpuan kepada mengesahkan sama ada model menangani soalan dan masalah ini dengan betul. Pelajaran ini memberi tumpuan kepada Analisis Data Eksploratori atau EDA, iaitu teknik untuk mentakrifkan ciri-ciri dan hubungan dalam data serta boleh digunakan untuk menyediakan data bagi pemodelan.

Kita akan menggunakan set data contoh daripada [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) untuk menunjukkan bagaimana ini boleh diaplikasikan menggunakan Python dan pustaka Pandas. Set data ini mengandungi kiraan beberapa perkataan biasa yang terdapat dalam e-mel, di mana sumber e-mel ini adalah tanpa nama. Gunakan [notebook](notebook.ipynb) dalam direktori ini untuk mengikuti langkah-langkahnya.

## Analisis Data Eksploratori

Fasa pengumpulan dalam kitaran hayat adalah di mana data diperoleh serta masalah dan soalan dikenal pasti, tetapi bagaimana kita tahu data tersebut boleh menyokong hasil akhir? 
Ingat bahawa seorang saintis data mungkin bertanya soalan berikut apabila mereka memperoleh data:
- Adakah saya mempunyai cukup data untuk menyelesaikan masalah ini?
- Adakah kualiti data ini boleh diterima untuk masalah ini?
- Jika saya menemui maklumat tambahan melalui data ini, patutkah kita mempertimbangkan untuk mengubah atau mentakrifkan semula matlamat?

Analisis Data Eksploratori adalah proses untuk mengenali data tersebut dan boleh digunakan untuk menjawab soalan-soalan ini, serta mengenal pasti cabaran dalam bekerja dengan set data tersebut. Mari kita fokus kepada beberapa teknik yang digunakan untuk mencapai ini.

## Pemprofilan Data, Statistik Deskriptif, dan Pandas
Bagaimana kita menilai sama ada kita mempunyai cukup data untuk menyelesaikan masalah ini? Pemprofilan data boleh meringkaskan dan mengumpulkan beberapa maklumat umum tentang set data kita melalui teknik statistik deskriptif. Pemprofilan data membantu kita memahami apa yang tersedia kepada kita, dan statistik deskriptif membantu kita memahami berapa banyak perkara yang tersedia kepada kita.

Dalam beberapa pelajaran sebelum ini, kita telah menggunakan Pandas untuk menyediakan beberapa statistik deskriptif dengan fungsi [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Fungsi ini menyediakan kiraan, nilai maksimum dan minimum, purata, sisihan piawai, dan kuantil pada data berangka. Menggunakan statistik deskriptif seperti fungsi `describe()` boleh membantu anda menilai berapa banyak data yang anda ada dan sama ada anda memerlukan lebih banyak.

## Pensampelan dan Pertanyaan
Meneroka segala-galanya dalam set data yang besar boleh memakan masa yang lama dan biasanya merupakan tugas yang diserahkan kepada komputer. Walau bagaimanapun, pensampelan adalah alat yang berguna untuk memahami data dan membolehkan kita memahami dengan lebih baik apa yang terdapat dalam set data dan apa yang diwakilinya. Dengan sampel, anda boleh menggunakan kebarangkalian dan statistik untuk membuat beberapa kesimpulan umum tentang data anda. Walaupun tiada peraturan yang ditetapkan tentang berapa banyak data yang perlu anda sampel, adalah penting untuk diingat bahawa lebih banyak data yang anda sampel, lebih tepat generalisasi yang boleh anda buat tentang data tersebut.

Pandas mempunyai fungsi [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) dalam pustakanya di mana anda boleh memberikan argumen tentang berapa banyak sampel rawak yang anda ingin terima dan gunakan.

Pertanyaan umum terhadap data boleh membantu anda menjawab beberapa soalan dan teori umum yang mungkin anda ada. Berbeza dengan pensampelan, pertanyaan membolehkan anda mempunyai kawalan dan memberi tumpuan kepada bahagian tertentu data yang anda ingin tahu. Fungsi [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) dalam pustaka Pandas membolehkan anda memilih lajur dan menerima jawapan mudah tentang data melalui baris yang diperoleh.

## Meneroka dengan Visualisasi
Anda tidak perlu menunggu sehingga data dibersihkan dan dianalisis sepenuhnya untuk mula mencipta visualisasi. Malah, mempunyai representasi visual semasa meneroka boleh membantu mengenal pasti corak, hubungan, dan masalah dalam data. Selain itu, visualisasi menyediakan cara komunikasi dengan mereka yang tidak terlibat dalam pengurusan data dan boleh menjadi peluang untuk berkongsi dan menjelaskan soalan tambahan yang tidak ditangani dalam peringkat pengumpulan. Rujuk [bahagian tentang Visualisasi](../../../../../../../../../3-Data-Visualization) untuk mengetahui lebih lanjut tentang beberapa cara popular untuk meneroka secara visual.

## Meneroka untuk Mengenal Pasti Ketidakkonsistenan
Semua topik dalam pelajaran ini boleh membantu mengenal pasti nilai yang hilang atau tidak konsisten, tetapi Pandas menyediakan fungsi untuk memeriksa beberapa daripadanya. [isna() atau isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) boleh memeriksa nilai yang hilang. Satu perkara penting dalam meneroka nilai-nilai ini dalam data anda adalah untuk meneroka mengapa ia berakhir seperti itu pada awalnya. Ini boleh membantu anda memutuskan apa [tindakan yang perlu diambil untuk menyelesaikannya](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Kuiz Pasca-Kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Tugasan

[Meneroka untuk jawapan](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.