<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-06T00:14:02+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "ms"
}
-->
## Jenis Data

Seperti yang telah disebutkan, data ada di mana-mana. Kita hanya perlu menangkapnya dengan cara yang betul! Adalah berguna untuk membezakan antara **data berstruktur** dan **data tidak berstruktur**. Data berstruktur biasanya diwakili dalam bentuk yang teratur, sering kali sebagai jadual atau beberapa jadual, manakala data tidak berstruktur hanyalah koleksi fail. Kadang-kadang kita juga boleh bercakap tentang **data separa berstruktur**, yang mempunyai beberapa jenis struktur yang mungkin berbeza-beza.

| Berstruktur                                                                  | Separa berstruktur                                                                             | Tidak berstruktur                       |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------- |
| Senarai orang dengan nombor telefon mereka                                  | Halaman Wikipedia dengan pautan                                                              | Teks Ensiklopedia Britannica           |
| Suhu di semua bilik bangunan setiap minit selama 20 tahun terakhir          | Koleksi kertas saintifik dalam format JSON dengan penulis, tarikh penerbitan, dan abstrak    | Perkongsian fail dengan dokumen korporat |
| Data umur dan jantina semua orang yang memasuki bangunan                    | Halaman Internet                                                                             | Rakaman video mentah dari kamera pengawasan |

## Di Mana Mendapatkan Data

Terdapat banyak sumber data yang mungkin, dan mustahil untuk menyenaraikan semuanya! Walau bagaimanapun, mari kita sebutkan beberapa tempat biasa di mana anda boleh mendapatkan data:

* **Berstruktur**
  - **Internet of Things** (IoT), termasuk data daripada pelbagai sensor seperti sensor suhu atau tekanan, menyediakan banyak data berguna. Sebagai contoh, jika bangunan pejabat dilengkapi dengan sensor IoT, kita boleh mengawal pemanasan dan pencahayaan secara automatik untuk meminimumkan kos.
  - **Tinjauan** yang kita minta pengguna lengkapkan selepas pembelian, atau selepas melawat laman web.
  - **Analisis tingkah laku** boleh, sebagai contoh, membantu kita memahami sejauh mana pengguna meneroka laman web, dan apa sebab utama mereka meninggalkan laman tersebut.
* **Tidak berstruktur**
  - **Teks** boleh menjadi sumber maklumat yang kaya, seperti skor **sentimen keseluruhan**, atau mengekstrak kata kunci dan makna semantik.
  - **Imej** atau **Video**. Rakaman video dari kamera pengawasan boleh digunakan untuk menganggarkan trafik di jalan raya, dan memberi maklumat kepada orang ramai tentang kemungkinan kesesakan lalu lintas.
  - **Log** pelayan web boleh digunakan untuk memahami halaman mana di laman web kita yang paling kerap dilawati, dan untuk berapa lama.
* **Separa berstruktur**
  - Graf **Rangkaian Sosial** boleh menjadi sumber data yang hebat tentang personaliti pengguna dan keberkesanan mereka dalam menyebarkan maklumat.
  - Apabila kita mempunyai koleksi gambar dari satu majlis, kita boleh cuba mengekstrak data **Dinamik Kumpulan** dengan membina graf orang yang bergambar bersama.

Dengan mengetahui pelbagai sumber data yang mungkin, anda boleh cuba memikirkan senario yang berbeza di mana teknik sains data boleh digunakan untuk memahami situasi dengan lebih baik, dan untuk meningkatkan proses perniagaan.

## Apa yang Boleh Dilakukan dengan Data

Dalam Sains Data, kita memberi tumpuan kepada langkah-langkah berikut dalam perjalanan data:

Sudah tentu, bergantung kepada data sebenar, beberapa langkah mungkin tidak diperlukan (contohnya, apabila kita sudah mempunyai data dalam pangkalan data, atau apabila kita tidak memerlukan latihan model), atau beberapa langkah mungkin diulang beberapa kali (seperti pemprosesan data).

## Digitalisasi dan Transformasi Digital

Dalam dekad yang lalu, banyak perniagaan mula memahami kepentingan data dalam membuat keputusan perniagaan. Untuk menerapkan prinsip sains data dalam menjalankan perniagaan, seseorang perlu terlebih dahulu mengumpulkan data, iaitu menterjemahkan proses perniagaan ke dalam bentuk digital. Ini dikenali sebagai **digitalisasi**. Menerapkan teknik sains data pada data ini untuk membimbing keputusan boleh membawa kepada peningkatan produktiviti yang ketara (atau bahkan perubahan arah perniagaan), yang disebut **transformasi digital**.

Mari kita pertimbangkan satu contoh. Katakan kita mempunyai kursus sains data (seperti kursus ini) yang kita sampaikan secara dalam talian kepada pelajar, dan kita ingin menggunakan sains data untuk memperbaikinya. Bagaimana kita boleh melakukannya?

Kita boleh mula dengan bertanya "Apa yang boleh didigitalkan?" Cara paling mudah adalah dengan mengukur masa yang diambil oleh setiap pelajar untuk menyelesaikan setiap modul, dan mengukur pengetahuan yang diperoleh dengan memberikan ujian pilihan berganda pada akhir setiap modul. Dengan purata masa penyelesaian di kalangan semua pelajar, kita boleh mengetahui modul mana yang paling sukar bagi pelajar, dan bekerja untuk mempermudahkannya.
Anda mungkin berpendapat bahawa pendekatan ini tidak sesuai, kerana modul boleh mempunyai panjang yang berbeza. Mungkin lebih adil untuk membahagikan masa mengikut panjang modul (dalam bilangan aksara), dan membandingkan nilai-nilai tersebut sebagai gantinya.
Apabila kita mula menganalisis keputusan ujian pilihan berganda, kita boleh cuba menentukan konsep mana yang pelajar sukar fahami, dan menggunakan maklumat tersebut untuk memperbaiki kandungan. Untuk melakukan itu, kita perlu merancang ujian sedemikian rupa sehingga setiap soalan berkait dengan konsep tertentu atau bahagian pengetahuan.

Jika kita ingin menjadi lebih rumit, kita boleh memplot masa yang diambil untuk setiap modul terhadap kategori umur pelajar. Kita mungkin mendapati bahawa untuk beberapa kategori umur, masa yang diambil untuk menyelesaikan modul adalah terlalu lama, atau pelajar berhenti sebelum menyelesaikannya. Ini boleh membantu kita memberikan cadangan umur untuk modul tersebut, dan mengurangkan ketidakpuasan orang ramai akibat jangkaan yang salah.

## 🚀 Cabaran

Dalam cabaran ini, kita akan cuba mencari konsep yang berkaitan dengan bidang Sains Data dengan melihat teks. Kita akan mengambil artikel Wikipedia tentang Sains Data, memuat turun dan memproses teks, dan kemudian membina awan perkataan seperti ini:

![Awan Perkataan untuk Sains Data](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Lawati [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') untuk membaca kod tersebut. Anda juga boleh menjalankan kod tersebut, dan melihat bagaimana ia melakukan semua transformasi data secara langsung.

> Jika anda tidak tahu cara menjalankan kod dalam Jupyter Notebook, lihat [artikel ini](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Kuiz selepas kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Tugasan

* **Tugas 1**: Ubah kod di atas untuk mencari konsep berkaitan bagi bidang **Big Data** dan **Machine Learning**
* **Tugas 2**: [Fikirkan Tentang Senario Sains Data](assignment.md)

## Kredit

Pelajaran ini telah ditulis dengan ♥️ oleh [Dmitry Soshnikov](http://soshnikov.com)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.