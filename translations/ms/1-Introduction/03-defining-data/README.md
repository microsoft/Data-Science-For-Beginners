# Mendefinisikan Data

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Mendefinisikan Data - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Data adalah fakta, maklumat, pemerhatian dan ukuran yang digunakan untuk membuat penemuan dan menyokong keputusan yang maklum. Titik data adalah satu unit data dalam satu set data, yang merupakan koleksi titik data. Set data boleh datang dalam pelbagai format dan struktur, dan biasanya akan berdasarkan kepada sumbernya, atau dari mana data itu datang. Sebagai contoh, pendapatan bulanan sesebuah syarikat mungkin berada dalam hamparan tetapi data kadar denyutan jantung setiap jam dari jam pintar mungkin dalam format [JSON](https://stackoverflow.com/a/383699). Adalah biasa untuk saintis data bekerja dengan pelbagai jenis data dalam satu set data.

Pelajaran ini memfokuskan pada mengenal pasti dan mengklasifikasikan data mengikut ciri-ciri dan sumbernya.

## [Kuiz Pra-Kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Bagaimana Data Diterangkan

### Data Mentah
Data mentah adalah data yang datang dari sumbernya dalam keadaan asal dan belum dianalisis atau diatur. Untuk memahami apa yang sedang berlaku dengan satu set data, ia perlu disusun dalam format yang boleh difahami oleh manusia serta teknologi yang mungkin digunakan untuk menganalisisnya lebih lanjut. Struktur satu set data menerangkan bagaimana ia diatur dan boleh diklasifikasikan sebagai berstruktur, tidak berstruktur dan separa berstruktur. Jenis struktur ini akan berbeza-beza, bergantung pada sumber tetapi akhirnya akan sesuai dalam tiga kategori ini.

### Data Kuantitatif
Data kuantitatif adalah pemerhatian berangka dalam satu set data dan biasanya boleh dianalisis, diukur dan digunakan secara matematik. Beberapa contoh data kuantitatif adalah: populasi sesebuah negara, ketinggian seseorang atau pendapatan suku tahunan syarikat. Dengan beberapa analisis tambahan, data kuantitatif boleh digunakan untuk menemui tren bermusim Indeks Kualiti Udara (AQI) atau menganggarkan kebarangkalian trafik waktu puncak pada hari kerja biasa.

### Data Kualitatif
Data kualitatif, juga dikenali sebagai data kategori adalah data yang tidak boleh diukur secara objektif seperti pemerhatian data kuantitatif. Ia biasanya dalam pelbagai format data subjektif yang menangkap kualiti sesuatu, seperti produk atau proses. Kadang-kadang, data kualitatif adalah berangka dan biasanya tidak digunakan secara matematik, seperti nombor telefon atau cap masa. Beberapa contoh data kualitatif adalah: komen video, jenama dan model kereta atau warna kegemaran kawan rapat anda. Data kualitatif boleh digunakan untuk memahami produk mana yang paling disukai pengguna atau mengenal pasti kata kunci popular dalam resume permohonan kerja.

### Data Berstruktur
Data berstruktur adalah data yang diatur dalam baris dan lajur, di mana setiap baris akan mempunyai set lajur yang sama. Lajur mewakili nilai suatu jenis tertentu dan akan dikenal pasti dengan nama yang menerangkan apa yang nilai itu wakili, manakala baris mengandungi nilai sebenar. Lajur sering mempunyai set peraturan atau had tertentu untuk nilai, bagi memastikan bahawa nilai itu mewakili lajur dengan tepat. Sebagai contoh bayangkan hamparan pelanggan di mana setiap baris mesti mempunyai nombor telefon dan nombor telefon itu tidak mengandungi aksara alfabet. Mungkin ada peraturan yang dikenakan pada lajur nombor telefon untuk memastikan ia tidak pernah kosong dan hanya mengandungi nombor.

Kelebihan data berstruktur adalah ia boleh disusun dengan cara yang boleh dikaitkan dengan data berstruktur lain. Namun, kerana data direka untuk diatur dalam cara tertentu, membuat perubahan pada struktur keseluruhannya boleh mengambil banyak usaha. Sebagai contoh, menambah lajur e-mel ke hamparan pelanggan yang tidak boleh kosong bermakna anda perlu mencari cara bagaimana menambah nilai ini ke baris pelanggan yang sedia ada dalam set data.

Contoh data berstruktur: hamparan, pangkalan data berhubung, nombor telefon, penyata bank

### Data Tidak Berstruktur
Data tidak berstruktur biasanya tidak boleh dikategorikan dalam baris atau lajur dan tidak mengandungi format atau set peraturan untuk diikuti. Oleh kerana data tidak berstruktur mempunyai kurang sekatan pada strukturnya, ia lebih mudah untuk menambah maklumat baru berbanding dengan set data berstruktur. Jika sensor yang menangkap data tekanan barometrik setiap 2 minit menerima kemas kini yang kini membolehkan ia mengukur dan merekod suhu, ia tidak memerlukan pengubahan data sedia ada jika ia tidak berstruktur. Namun, ini mungkin menjadikan analisis atau penyiasatan jenis data ini mengambil masa lebih lama. Sebagai contoh, seorang saintis yang mahu mencari suhu purata bulan lalu dari data sensor, tetapi mendapati sensor merekod "e" dalam beberapa data yang direkod untuk menunjukkan bahawa ia rosak dan bukannya nombor biasa, yang bermaksud data itu tidak lengkap.

Contoh data tidak berstruktur: fail teks, mesej teks, fail video

### Separuh Berstruktur
Data separuh berstruktur mempunyai ciri yang menjadikannya gabungan antara data berstruktur dan tidak berstruktur. Ia biasanya tidak mematuhi format baris dan lajur tetapi disusun dengan cara yang dianggap berstruktur dan mungkin mengikuti format tetap atau set peraturan. Struktur akan berbeza antara sumber, seperti hierarki yang ditakrifkan dengan baik kepada sesuatu yang lebih fleksibel yang membenarkan integrasi maklumat baru dengan mudah. Metadata adalah penunjuk yang membantu menentukan bagaimana data disusun dan disimpan dan akan mempunyai pelbagai nama, berdasarkan jenis data. Beberapa nama biasa untuk metadata adalah tag, elemen, entiti dan atribut. Sebagai contoh, mesej e-mel biasa akan mempunyai subjek, badan dan satu set penerima dan boleh diatur mengikut siapa atau bila ia dihantar.

Contoh data separa berstruktur: HTML, fail CSV, JavaScript Object Notation (JSON)

## Sumber Data

Sumber data adalah lokasi awal di mana data dijana, atau di mana ia "berkedudukan" dan akan berbeza berdasarkan bagaimana dan bila ia dikumpulkan. Data yang dijana oleh pengguna adalah dikenali sebagai data primer manakala data sekunder datang dari sumber yang telah mengumpulkan data untuk kegunaan umum. Sebagai contoh, sekumpulan saintis yang mengumpulkan pemerhatian di hutan hujan dianggap sebagai primer dan jika mereka memutuskan untuk berkongsi dengan saintis lain, ia dianggap sebagai sekunder bagi mereka yang menggunakannya.

Pangkalan data adalah sumber biasa dan bergantung pada sistem pengurusan pangkalan data untuk mengehos dan menyelenggara data di mana pengguna menggunakan arahan dipanggil pertanyaan untuk meneroka data. Fail sebagai sumber data boleh berupa fail audio, imej dan video serta hamparan seperti Excel. Sumber internet adalah lokasi biasa untuk mengehos data, di mana pangkalan data serta fail boleh dijumpai. Antara muka pengaturcaraan aplikasi, juga dikenali sebagai API membolehkan pengaturcara mencipta cara untuk berkongsi data dengan pengguna luaran melalui internet, manakala proses pengikisan web mengekstrak data dari halaman web. [Pelajaran dalam Bekerja dengan Data](../../../../../../../../../2-Working-With-Data) memfokuskan pada cara menggunakan pelbagai sumber data.

## Kesimpulan

Dalam pelajaran ini kami telah mempelajari:

- Apa itu data
- Bagaimana data diterangkan
- Bagaimana data diklasifikasikan dan dikategorikan
- Di mana data boleh didapati

## 🚀 Cabaran

Kaggle adalah sumber set data terbuka yang hebat. Gunakan [alat carian set data](https://www.kaggle.com/datasets) untuk mencari beberapa set data menarik dan klasifikasikan 3-5 set data dengan kriteria ini:

- Adakah data kuantitatif atau kualitatif?
- Adakah data berstruktur, tidak berstruktur, atau separa berstruktur?

## [Kuiz pasca kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Ulang Kaji & Belajar Sendiri

- Unit Microsoft Learn ini, bertajuk [Kenal pasti format data](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) mempunyai pecahan terperinci tentang data berstruktur, separa berstruktur, dan tidak berstruktur.

## Tugasan

[Mengklasifikasikan Set Data](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->