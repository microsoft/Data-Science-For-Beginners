<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a0556b17de4c8d1a9470b02247b01d4",
  "translation_date": "2025-09-04T20:42:42+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "ms"
}
-->
# Pengenalan kepada Sains Data di Awan

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Sains Data di Awan: Pengenalan - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Dalam pelajaran ini, anda akan mempelajari prinsip asas Awan, kemudian anda akan melihat mengapa ia menarik untuk menggunakan perkhidmatan Awan bagi menjalankan projek sains data anda, dan kita akan melihat beberapa contoh projek sains data yang dijalankan di Awan.

## [Kuiz Pra-Kuliah](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Apakah itu Awan?

Awan, atau Pengkomputeran Awan, adalah penyampaian pelbagai perkhidmatan pengkomputeran berdasarkan bayaran mengikut penggunaan yang dihoskan pada infrastruktur melalui internet. Perkhidmatan ini termasuk penyelesaian seperti storan, pangkalan data, rangkaian, perisian, analitik, dan perkhidmatan pintar.

Kita biasanya membezakan Awan Awam, Awan Peribadi, dan Awan Hibrid seperti berikut:

* **Awan Awam**: Awan awam dimiliki dan dikendalikan oleh penyedia perkhidmatan awan pihak ketiga yang menyampaikan sumber pengkomputerannya melalui Internet kepada orang awam.
* **Awan Peribadi**: Merujuk kepada sumber pengkomputeran awan yang digunakan secara eksklusif oleh satu perniagaan atau organisasi, dengan perkhidmatan dan infrastruktur yang diselenggara pada rangkaian peribadi.
* **Awan Hibrid**: Awan hibrid adalah sistem yang menggabungkan awan awam dan peribadi. Pengguna memilih pusat data di lokasi, sambil membenarkan data dan aplikasi dijalankan pada satu atau lebih awan awam.

Kebanyakan perkhidmatan pengkomputeran awan tergolong dalam tiga kategori: Infrastruktur sebagai Perkhidmatan (IaaS), Platform sebagai Perkhidmatan (PaaS), dan Perisian sebagai Perkhidmatan (SaaS).

* **Infrastruktur sebagai Perkhidmatan (IaaS)**: Pengguna menyewa infrastruktur IT seperti pelayan dan mesin maya (VM), storan, rangkaian, sistem operasi.
* **Platform sebagai Perkhidmatan (PaaS)**: Pengguna menyewa persekitaran untuk membangun, menguji, menyampaikan, dan mengurus aplikasi perisian. Pengguna tidak perlu risau tentang penyediaan atau pengurusan infrastruktur asas seperti pelayan, storan, rangkaian, dan pangkalan data yang diperlukan untuk pembangunan.
* **Perisian sebagai Perkhidmatan (SaaS)**: Pengguna mendapat akses kepada aplikasi perisian melalui Internet, atas permintaan dan biasanya berdasarkan langganan. Pengguna tidak perlu risau tentang hosting dan pengurusan aplikasi perisian, infrastruktur asas, atau penyelenggaraan seperti peningkatan perisian dan pembaikan keselamatan.

Beberapa penyedia Awan terbesar adalah Amazon Web Services, Google Cloud Platform, dan Microsoft Azure.

## Mengapa Memilih Awan untuk Sains Data?

Pembangun dan profesional IT memilih untuk bekerja dengan Awan atas pelbagai sebab, termasuk yang berikut:

* **Inovasi**: Anda boleh memperkasakan aplikasi anda dengan mengintegrasikan perkhidmatan inovatif yang dicipta oleh penyedia Awan terus ke dalam aplikasi anda.
* **Fleksibiliti**: Anda hanya membayar untuk perkhidmatan yang anda perlukan dan boleh memilih daripada pelbagai perkhidmatan. Anda biasanya membayar mengikut penggunaan dan menyesuaikan perkhidmatan anda mengikut keperluan yang berubah.
* **Bajet**: Anda tidak perlu membuat pelaburan awal untuk membeli perkakasan dan perisian, menyediakan dan menjalankan pusat data di lokasi, dan anda hanya membayar untuk apa yang anda gunakan.
* **Kebolehskalaan**: Sumber anda boleh diskalakan mengikut keperluan projek anda, yang bermaksud aplikasi anda boleh menggunakan lebih banyak atau kurang kuasa pengkomputeran, storan, dan jalur lebar, dengan menyesuaikan kepada faktor luaran pada bila-bila masa.
* **Produktiviti**: Anda boleh memberi tumpuan kepada perniagaan anda daripada menghabiskan masa pada tugas yang boleh diuruskan oleh pihak lain, seperti mengurus pusat data.
* **Kebolehpercayaan**: Pengkomputeran Awan menawarkan beberapa cara untuk membuat sandaran data anda secara berterusan dan anda boleh menyediakan rancangan pemulihan bencana untuk memastikan perniagaan dan perkhidmatan anda terus berjalan, walaupun dalam masa krisis.
* **Keselamatan**: Anda boleh mendapat manfaat daripada dasar, teknologi, dan kawalan yang memperkukuhkan keselamatan projek anda.

Ini adalah beberapa sebab paling biasa mengapa orang memilih untuk menggunakan perkhidmatan Awan. Sekarang kita mempunyai pemahaman yang lebih baik tentang apa itu Awan dan manfaat utamanya, mari kita lihat lebih khusus kepada pekerjaan saintis data dan pembangun yang bekerja dengan data, serta bagaimana Awan dapat membantu mereka menghadapi beberapa cabaran yang mungkin mereka hadapi:

* **Menyimpan sejumlah besar data**: Daripada membeli, mengurus, dan melindungi pelayan besar, anda boleh menyimpan data anda terus di awan, dengan penyelesaian seperti Azure Cosmos DB, Azure SQL Database, dan Azure Data Lake Storage.
* **Melakukan Integrasi Data**: Integrasi data adalah bahagian penting dalam Sains Data, yang membolehkan anda membuat peralihan daripada pengumpulan data kepada tindakan. Dengan perkhidmatan integrasi data yang ditawarkan di awan, anda boleh mengumpul, mengubah, dan mengintegrasikan data daripada pelbagai sumber ke dalam satu gudang data, dengan Data Factory.
* **Memproses data**: Memproses sejumlah besar data memerlukan banyak kuasa pengkomputeran, dan tidak semua orang mempunyai akses kepada mesin yang cukup berkuasa untuk itu, sebab itulah ramai orang memilih untuk terus memanfaatkan kuasa pengkomputeran besar awan untuk menjalankan dan menyebarkan penyelesaian mereka.
* **Menggunakan perkhidmatan analitik data**: Perkhidmatan awan seperti Azure Synapse Analytics, Azure Stream Analytics, dan Azure Databricks membantu anda mengubah data anda menjadi wawasan yang boleh diambil tindakan.
* **Menggunakan perkhidmatan Pembelajaran Mesin dan kecerdasan data**: Daripada memulakan dari awal, anda boleh menggunakan algoritma pembelajaran mesin yang ditawarkan oleh penyedia awan, dengan perkhidmatan seperti AzureML. Anda juga boleh menggunakan perkhidmatan kognitif seperti pertuturan-ke-teks, teks-ke-pertuturan, penglihatan komputer, dan banyak lagi.

## Contoh Sains Data di Awan

Mari kita buat ini lebih nyata dengan melihat beberapa senario.

### Analisis Sentimen Media Sosial Masa Nyata
Kita akan mulakan dengan senario yang biasa dikaji oleh mereka yang baru bermula dengan pembelajaran mesin: analisis sentimen media sosial secara masa nyata.

Katakan anda menjalankan laman web berita dan anda ingin memanfaatkan data langsung untuk memahami kandungan apa yang mungkin menarik minat pembaca anda. Untuk mengetahui lebih lanjut tentang itu, anda boleh membina program yang melakukan analisis sentimen masa nyata terhadap data daripada penerbitan Twitter, pada topik yang relevan dengan pembaca anda.

Penunjuk utama yang akan anda lihat adalah jumlah tweet pada topik tertentu (hashtag) dan sentimen, yang ditentukan menggunakan alat analitik yang melakukan analisis sentimen sekitar topik yang ditentukan.

Langkah-langkah yang diperlukan untuk mencipta projek ini adalah seperti berikut:

* Cipta hab acara untuk input penstriman, yang akan mengumpul data daripada Twitter.
* Konfigurasikan dan mulakan aplikasi klien Twitter, yang akan memanggil API Penstriman Twitter.
* Cipta tugas Analitik Penstriman.
* Tentukan input dan pertanyaan tugas.
* Cipta sink output dan tentukan output tugas.
* Mulakan tugas.

Untuk melihat proses penuh, lihat [dokumentasi](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analisis Kertas Saintifik
Mari kita ambil satu lagi contoh projek yang dicipta oleh [Dmitry Soshnikov](http://soshnikov.com), salah seorang penulis kurikulum ini.

Dmitry mencipta alat yang menganalisis kertas COVID. Dengan mengkaji projek ini, anda akan melihat bagaimana anda boleh mencipta alat yang mengekstrak pengetahuan daripada kertas saintifik, mendapatkan wawasan, dan membantu penyelidik menavigasi melalui koleksi kertas yang besar dengan cara yang cekap.

Mari kita lihat langkah-langkah yang digunakan untuk ini:
* Mengekstrak dan memproses maklumat dengan [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Menggunakan [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) untuk memproses secara selari.
* Menyimpan dan membuat pertanyaan maklumat dengan [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Mencipta papan pemuka interaktif untuk penerokaan dan visualisasi data menggunakan Power BI.

Untuk melihat proses penuh, lawati [blog Dmitry](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Seperti yang anda lihat, kita boleh memanfaatkan perkhidmatan Awan dalam pelbagai cara untuk melakukan Sains Data.

## Nota Kaki

Sumber:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Kuiz Pasca-Kuliah

## [Kuiz Pasca-Kuliah](https://ff-quizzes.netlify.app/en/ds/)

## Tugasan

[Penyelidikan Pasaran](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.