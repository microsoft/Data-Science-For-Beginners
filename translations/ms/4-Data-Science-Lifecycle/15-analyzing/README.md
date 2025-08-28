<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-28T18:20:05+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "ms"
}
-->
# Kitaran Hayat Sains Data: Menganalisis

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Kitaran Hayat Sains Data: Menganalisis - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

## Kuiz Pra-Kuliah

## [Kuiz Pra-Kuliah](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Menganalisis dalam kitaran hayat data mengesahkan bahawa data boleh menjawab soalan yang dicadangkan atau menyelesaikan masalah tertentu. Langkah ini juga boleh memberi tumpuan kepada mengesahkan model yang betul-betul menangani soalan dan masalah tersebut. Pelajaran ini memberi tumpuan kepada Analisis Data Eksploratori atau EDA, iaitu teknik untuk mendefinisikan ciri dan hubungan dalam data dan boleh digunakan untuk menyediakan data untuk pemodelan.

Kami akan menggunakan dataset contoh daripada [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) untuk menunjukkan bagaimana ini boleh diterapkan dengan Python dan perpustakaan Pandas. Dataset ini mengandungi kiraan beberapa perkataan biasa yang terdapat dalam e-mel, sumber e-mel ini adalah tanpa nama. Gunakan [notebook](notebook.ipynb) dalam direktori ini untuk mengikuti.

## Analisis Data Eksploratori

Fasa pengumpulan dalam kitaran hayat adalah di mana data diperoleh serta masalah dan soalan yang dihadapi, tetapi bagaimana kita tahu data boleh membantu menyokong hasil akhir? 
Ingat bahawa seorang saintis data mungkin bertanya soalan berikut apabila mereka memperoleh data:
-   Adakah saya mempunyai cukup data untuk menyelesaikan masalah ini?
-   Adakah kualiti data boleh diterima untuk masalah ini?
-   Jika saya menemui maklumat tambahan melalui data ini, patutkah kita mempertimbangkan untuk mengubah atau mentakrifkan semula matlamat?
Analisis Data Eksploratori adalah proses untuk mengenali data tersebut dan boleh digunakan untuk menjawab soalan-soalan ini, serta mengenal pasti cabaran bekerja dengan dataset. Mari kita fokus pada beberapa teknik yang digunakan untuk mencapai ini.

## Profil Data, Statistik Deskriptif, dan Pandas
Bagaimana kita menilai sama ada kita mempunyai cukup data untuk menyelesaikan masalah ini? Profil data boleh meringkaskan dan mengumpulkan beberapa maklumat umum tentang dataset kita melalui teknik statistik deskriptif. Profil data membantu kita memahami apa yang tersedia untuk kita, dan statistik deskriptif membantu kita memahami berapa banyak perkara yang tersedia untuk kita.

Dalam beberapa pelajaran sebelumnya, kita telah menggunakan Pandas untuk menyediakan beberapa statistik deskriptif dengan fungsi [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Ia menyediakan kiraan, nilai maksimum dan minimum, purata, sisihan piawai dan kuantil pada data berangka. Menggunakan statistik deskriptif seperti fungsi `describe()` boleh membantu anda menilai berapa banyak yang anda ada dan sama ada anda memerlukan lebih banyak.

## Pensampelan dan Pertanyaan
Meneroka segala-galanya dalam dataset yang besar boleh memakan masa yang sangat lama dan biasanya tugas yang diserahkan kepada komputer. Walau bagaimanapun, pensampelan adalah alat yang berguna untuk memahami data dan membolehkan kita mempunyai pemahaman yang lebih baik tentang apa yang ada dalam dataset dan apa yang diwakilinya. Dengan sampel, anda boleh menggunakan kebarangkalian dan statistik untuk membuat beberapa kesimpulan umum tentang data anda. Walaupun tiada peraturan yang ditetapkan tentang berapa banyak data yang patut anda sampel, adalah penting untuk diingat bahawa lebih banyak data yang anda sampel, lebih tepat generalisasi yang boleh anda buat tentang data tersebut. 
Pandas mempunyai fungsi [`sample()` dalam perpustakaannya](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) di mana anda boleh memberikan argumen tentang berapa banyak sampel rawak yang anda ingin terima dan gunakan.

Pertanyaan umum tentang data boleh membantu anda menjawab beberapa soalan dan teori umum yang mungkin anda ada. Berbeza dengan pensampelan, pertanyaan membolehkan anda mempunyai kawalan dan fokus pada bahagian tertentu data yang anda ada soalan tentang. 
Fungsi [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) dalam perpustakaan Pandas membolehkan anda memilih lajur dan menerima jawapan mudah tentang data melalui baris yang diperoleh.

## Meneroka dengan Visualisasi
Anda tidak perlu menunggu sehingga data dibersihkan dan dianalisis sepenuhnya untuk mula mencipta visualisasi. Malah, mempunyai representasi visual semasa meneroka boleh membantu mengenal pasti corak, hubungan, dan masalah dalam data. Selain itu, visualisasi menyediakan cara komunikasi dengan mereka yang tidak terlibat dalam pengurusan data dan boleh menjadi peluang untuk berkongsi dan menjelaskan soalan tambahan yang tidak ditangani dalam peringkat pengumpulan. Rujuk [bahagian tentang Visualisasi](../../../../../../../../../3-Data-Visualization) untuk mengetahui lebih lanjut tentang beberapa cara popular untuk meneroka secara visual.

## Meneroka untuk mengenal pasti ketidakkonsistenan
Semua topik dalam pelajaran ini boleh membantu mengenal pasti nilai yang hilang atau tidak konsisten, tetapi Pandas menyediakan fungsi untuk memeriksa beberapa perkara ini. [isna() atau isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) boleh memeriksa nilai yang hilang. Satu perkara penting dalam meneroka nilai-nilai ini dalam data anda adalah untuk meneroka mengapa ia berakhir seperti itu pada mulanya. Ini boleh membantu anda memutuskan tindakan apa yang perlu diambil untuk menyelesaikannya](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Kuiz Pra-Kuliah](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Tugasan

[Meneroka untuk jawapan](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.