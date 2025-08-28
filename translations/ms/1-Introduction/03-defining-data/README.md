<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-28T19:00:03+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "ms"
}
-->
# Mendefinisikan Data

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Mendefinisikan Data - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Data adalah fakta, maklumat, pemerhatian dan pengukuran yang digunakan untuk membuat penemuan dan menyokong keputusan yang berinformasi. Titik data adalah unit tunggal data dalam satu set data, yang merupakan koleksi titik data. Set data boleh datang dalam pelbagai format dan struktur, dan biasanya berdasarkan sumbernya, atau dari mana data itu berasal. Sebagai contoh, pendapatan bulanan sebuah syarikat mungkin dalam bentuk spreadsheet tetapi data kadar denyutan jantung setiap jam dari jam tangan pintar mungkin dalam format [JSON](https://stackoverflow.com/a/383699). Adalah biasa bagi saintis data untuk bekerja dengan pelbagai jenis data dalam satu set data.

Pelajaran ini memberi tumpuan kepada mengenal pasti dan mengklasifikasikan data berdasarkan ciri-cirinya dan sumbernya.

## [Kuiz Pra-Kuliah](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)

## Bagaimana Data Diterangkan

### Data Mentah
Data mentah adalah data yang datang dari sumbernya dalam keadaan asal dan belum dianalisis atau diatur. Untuk memahami apa yang berlaku dengan satu set data, ia perlu diatur dalam format yang boleh difahami oleh manusia serta teknologi yang mungkin mereka gunakan untuk menganalisisnya lebih lanjut. Struktur satu set data menerangkan bagaimana ia diatur dan boleh diklasifikasikan sebagai berstruktur, tidak berstruktur, dan separa berstruktur. Jenis struktur ini akan berbeza, bergantung pada sumbernya tetapi akhirnya akan sesuai dengan tiga kategori ini.

### Data Kuantitatif
Data kuantitatif adalah pemerhatian berangka dalam satu set data dan biasanya boleh dianalisis, diukur, dan digunakan secara matematik. Beberapa contoh data kuantitatif adalah: populasi sesebuah negara, ketinggian seseorang, atau pendapatan suku tahunan sebuah syarikat. Dengan analisis tambahan, data kuantitatif boleh digunakan untuk menemui tren musiman Indeks Kualiti Udara (AQI) atau menganggarkan kebarangkalian kesesakan lalu lintas pada hari kerja biasa.

### Data Kualitatif
Data kualitatif, juga dikenali sebagai data kategori, adalah data yang tidak boleh diukur secara objektif seperti pemerhatian data kuantitatif. Ia biasanya dalam pelbagai format data subjektif yang menangkap kualiti sesuatu, seperti produk atau proses. Kadang-kadang, data kualitatif adalah berangka tetapi tidak biasanya digunakan secara matematik, seperti nombor telefon atau cap waktu. Beberapa contoh data kualitatif adalah: komen video, jenama dan model kereta, atau warna kegemaran rakan terdekat anda. Data kualitatif boleh digunakan untuk memahami produk mana yang paling disukai pengguna atau mengenal pasti kata kunci popular dalam resume permohonan kerja.

### Data Berstruktur
Data berstruktur adalah data yang diatur dalam baris dan lajur, di mana setiap baris akan mempunyai set lajur yang sama. Lajur mewakili nilai jenis tertentu dan akan dikenalpasti dengan nama yang menerangkan apa yang diwakili oleh nilai tersebut, sementara baris mengandungi nilai sebenar. Lajur sering mempunyai set peraturan atau sekatan tertentu pada nilai, untuk memastikan nilai tersebut mewakili lajur dengan tepat. Sebagai contoh, bayangkan spreadsheet pelanggan di mana setiap baris mesti mempunyai nombor telefon dan nombor telefon tersebut tidak pernah mengandungi aksara abjad. Mungkin ada peraturan yang diterapkan pada lajur nombor telefon untuk memastikan ia tidak pernah kosong dan hanya mengandungi nombor.

Kelebihan data berstruktur adalah ia boleh diatur sedemikian rupa sehingga boleh berkaitan dengan data berstruktur lain. Walau bagaimanapun, kerana data direka untuk diatur dengan cara tertentu, membuat perubahan pada struktur keseluruhannya boleh memerlukan banyak usaha. Sebagai contoh, menambah lajur e-mel pada spreadsheet pelanggan yang tidak boleh kosong bermaksud anda perlu memikirkan bagaimana anda akan menambah nilai ini pada baris pelanggan yang sedia ada dalam set data.

Contoh data berstruktur: spreadsheet, pangkalan data relasi, nombor telefon, penyata bank.

### Data Tidak Berstruktur
Data tidak berstruktur biasanya tidak boleh dikategorikan ke dalam baris atau lajur dan tidak mengandungi format atau set peraturan untuk diikuti. Oleh kerana data tidak berstruktur mempunyai sekatan yang lebih sedikit pada strukturnya, lebih mudah untuk menambah maklumat baru berbanding dengan set data berstruktur. Jika sensor yang menangkap data tekanan barometrik setiap 2 minit telah menerima kemas kini yang kini membolehkannya mengukur dan merekodkan suhu, ia tidak memerlukan perubahan pada data sedia ada jika ia tidak berstruktur. Walau bagaimanapun, ini mungkin membuat analisis atau penyiasatan jenis data ini mengambil masa lebih lama. Sebagai contoh, seorang saintis yang ingin mencari suhu purata bulan sebelumnya dari data sensor, tetapi mendapati bahawa sensor merekodkan "e" dalam beberapa datanya untuk menunjukkan ia rosak dan bukannya nombor biasa, yang bermaksud data tersebut tidak lengkap.

Contoh data tidak berstruktur: fail teks, mesej teks, fail video.

### Data Separa Berstruktur
Data separa berstruktur mempunyai ciri-ciri yang menjadikannya gabungan data berstruktur dan tidak berstruktur. Ia biasanya tidak mematuhi format baris dan lajur tetapi diatur dengan cara yang dianggap berstruktur dan mungkin mengikuti format tetap atau set peraturan. Struktur akan berbeza antara sumber, seperti hierarki yang ditentukan dengan baik kepada sesuatu yang lebih fleksibel yang membolehkan integrasi maklumat baru dengan mudah. Metadata adalah indikator yang membantu menentukan bagaimana data diatur dan disimpan dan akan mempunyai pelbagai nama, berdasarkan jenis data. Beberapa nama umum untuk metadata adalah tag, elemen, entiti, dan atribut. Sebagai contoh, mesej e-mel biasa akan mempunyai subjek, badan, dan set penerima dan boleh diatur berdasarkan siapa atau bila ia dihantar.

Contoh data separa berstruktur: HTML, fail CSV, JavaScript Object Notation (JSON).

## Sumber Data

Sumber data adalah lokasi awal di mana data dihasilkan, atau di mana ia "berada" dan akan berbeza berdasarkan bagaimana dan bila ia dikumpulkan. Data yang dihasilkan oleh penggunanya dikenali sebagai data primer sementara data sekunder berasal dari sumber yang telah mengumpulkan data untuk kegunaan umum. Sebagai contoh, sekumpulan saintis yang mengumpulkan pemerhatian di hutan hujan akan dianggap sebagai data primer dan jika mereka memutuskan untuk berkongsi dengan saintis lain, ia akan dianggap sebagai data sekunder bagi mereka yang menggunakannya.

Pangkalan data adalah sumber yang biasa dan bergantung pada sistem pengurusan pangkalan data untuk menjadi tuan rumah dan mengekalkan data di mana pengguna menggunakan arahan yang dipanggil kueri untuk meneroka data. Fail sebagai sumber data boleh berupa fail audio, imej, dan video serta spreadsheet seperti Excel. Sumber internet adalah lokasi biasa untuk menjadi tuan rumah data, di mana pangkalan data serta fail boleh ditemui. Antara muka pengaturcaraan aplikasi, juga dikenali sebagai API, membolehkan pengaturcara mencipta cara untuk berkongsi data dengan pengguna luaran melalui internet, sementara proses web scraping mengekstrak data dari halaman web. [Pelajaran dalam Bekerja dengan Data](../../../../../../../../../2-Working-With-Data) memberi tumpuan kepada cara menggunakan pelbagai sumber data.

## Kesimpulan

Dalam pelajaran ini kita telah mempelajari:

- Apa itu data
- Bagaimana data diterangkan
- Bagaimana data diklasifikasikan dan dikategorikan
- Di mana data boleh ditemui

## 🚀 Cabaran

Kaggle adalah sumber yang sangat baik untuk set data terbuka. Gunakan [alat carian set data](https://www.kaggle.com/datasets) untuk mencari beberapa set data yang menarik dan klasifikasikan 3-5 set data dengan kriteria ini:

- Adakah data kuantitatif atau kualitatif?
- Adakah data berstruktur, tidak berstruktur, atau separa berstruktur?

## [Kuiz Pasca-Kuliah](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Kajian & Pembelajaran Kendiri

- Unit Microsoft Learn ini, bertajuk [Classify your Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) mempunyai pecahan terperinci tentang data berstruktur, separa berstruktur, dan tidak berstruktur.

## Tugasan

[Classifying Datasets](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.