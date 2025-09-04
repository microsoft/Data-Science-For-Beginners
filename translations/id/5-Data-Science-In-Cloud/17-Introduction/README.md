<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a0556b17de4c8d1a9470b02247b01d4",
  "translation_date": "2025-09-04T20:31:05+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "id"
}
-->
# Pengantar Data Science di Cloud

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science di Cloud: Pengantar - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Dalam pelajaran ini, Anda akan mempelajari prinsip-prinsip dasar Cloud, kemudian Anda akan melihat mengapa menggunakan layanan Cloud untuk menjalankan proyek data science Anda bisa menjadi menarik, dan kita akan melihat beberapa contoh proyek data science yang dijalankan di Cloud.

## [Kuis Pra-Kuliah](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Apa itu Cloud?

Cloud, atau Cloud Computing, adalah penyediaan berbagai layanan komputasi berbasis bayar sesuai penggunaan yang di-host pada infrastruktur melalui internet. Layanan ini mencakup solusi seperti penyimpanan, basis data, jaringan, perangkat lunak, analitik, dan layanan cerdas.

Biasanya kita membedakan Cloud Publik, Cloud Privat, dan Cloud Hybrid sebagai berikut:

* Cloud Publik: Cloud publik dimiliki dan dioperasikan oleh penyedia layanan cloud pihak ketiga yang menyediakan sumber daya komputasi melalui Internet kepada publik.
* Cloud Privat: Mengacu pada sumber daya komputasi cloud yang digunakan secara eksklusif oleh satu bisnis atau organisasi, dengan layanan dan infrastruktur yang dikelola di jaringan privat.
* Cloud Hybrid: Cloud hybrid adalah sistem yang menggabungkan cloud publik dan privat. Pengguna memilih pusat data di lokasi, sambil memungkinkan data dan aplikasi dijalankan di satu atau lebih cloud publik.

Sebagian besar layanan komputasi cloud terbagi dalam tiga kategori: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), dan Software as a Service (SaaS).

* Infrastructure as a Service (IaaS): pengguna menyewa infrastruktur TI seperti server dan mesin virtual (VM), penyimpanan, jaringan, sistem operasi.
* Platform as a Service (PaaS): pengguna menyewa lingkungan untuk mengembangkan, menguji, menyampaikan, dan mengelola aplikasi perangkat lunak. Pengguna tidak perlu khawatir tentang pengaturan atau pengelolaan infrastruktur dasar seperti server, penyimpanan, jaringan, dan basis data yang diperlukan untuk pengembangan.
* Software as a Service (SaaS): pengguna mendapatkan akses ke aplikasi perangkat lunak melalui Internet, sesuai permintaan dan biasanya berdasarkan langganan. Pengguna tidak perlu khawatir tentang hosting dan pengelolaan aplikasi perangkat lunak, infrastruktur dasar, atau pemeliharaan seperti pembaruan perangkat lunak dan patch keamanan.

Beberapa penyedia Cloud terbesar adalah Amazon Web Services, Google Cloud Platform, dan Microsoft Azure.

## Mengapa Memilih Cloud untuk Data Science?

Pengembang dan profesional TI memilih bekerja dengan Cloud karena berbagai alasan, termasuk:

* Inovasi: Anda dapat mendukung aplikasi Anda dengan mengintegrasikan layanan inovatif yang dibuat oleh penyedia Cloud langsung ke dalam aplikasi Anda.
* Fleksibilitas: Anda hanya membayar untuk layanan yang Anda butuhkan dan dapat memilih dari berbagai layanan. Anda biasanya membayar sesuai penggunaan dan menyesuaikan layanan Anda sesuai kebutuhan yang berkembang.
* Anggaran: Anda tidak perlu melakukan investasi awal untuk membeli perangkat keras dan perangkat lunak, mengatur dan menjalankan pusat data di lokasi, dan Anda hanya membayar untuk apa yang Anda gunakan.
* Skalabilitas: Sumber daya Anda dapat disesuaikan sesuai kebutuhan proyek Anda, yang berarti aplikasi Anda dapat menggunakan lebih banyak atau lebih sedikit daya komputasi, penyimpanan, dan bandwidth, dengan menyesuaikan faktor eksternal kapan saja.
* Produktivitas: Anda dapat fokus pada bisnis Anda daripada menghabiskan waktu untuk tugas-tugas yang dapat dikelola oleh pihak lain, seperti mengelola pusat data.
* Keandalan: Cloud Computing menawarkan beberapa cara untuk terus mencadangkan data Anda dan Anda dapat mengatur rencana pemulihan bencana untuk menjaga bisnis dan layanan Anda tetap berjalan, bahkan di saat krisis.
* Keamanan: Anda dapat memanfaatkan kebijakan, teknologi, dan kontrol yang memperkuat keamanan proyek Anda.

Ini adalah beberapa alasan umum mengapa orang memilih menggunakan layanan Cloud. Sekarang kita memiliki pemahaman yang lebih baik tentang apa itu Cloud dan manfaat utamanya, mari kita lihat lebih spesifik pekerjaan para ilmuwan data dan pengembang yang bekerja dengan data, serta bagaimana Cloud dapat membantu mereka menghadapi berbagai tantangan yang mungkin mereka hadapi:

* Menyimpan sejumlah besar data: Alih-alih membeli, mengelola, dan melindungi server besar, Anda dapat menyimpan data Anda langsung di cloud, dengan solusi seperti Azure Cosmos DB, Azure SQL Database, dan Azure Data Lake Storage.
* Melakukan Integrasi Data: Integrasi data adalah bagian penting dari Data Science, yang memungkinkan Anda beralih dari pengumpulan data ke pengambilan tindakan. Dengan layanan integrasi data yang ditawarkan di cloud, Anda dapat mengumpulkan, mengubah, dan mengintegrasikan data dari berbagai sumber ke dalam satu gudang data, dengan Data Factory.
* Memproses data: Memproses sejumlah besar data membutuhkan banyak daya komputasi, dan tidak semua orang memiliki akses ke mesin yang cukup kuat untuk itu, itulah mengapa banyak orang memilih langsung memanfaatkan daya komputasi besar dari cloud untuk menjalankan dan menyebarkan solusi mereka.
* Menggunakan layanan analitik data: layanan cloud seperti Azure Synapse Analytics, Azure Stream Analytics, dan Azure Databricks membantu Anda mengubah data menjadi wawasan yang dapat ditindaklanjuti.
* Menggunakan layanan Machine Learning dan kecerdasan data: Alih-alih memulai dari awal, Anda dapat menggunakan algoritma machine learning yang ditawarkan oleh penyedia cloud, dengan layanan seperti AzureML. Anda juga dapat menggunakan layanan kognitif seperti speech-to-text, text-to-speech, computer vision, dan lainnya.

## Contoh Data Science di Cloud

Mari kita buat ini lebih nyata dengan melihat beberapa skenario.

### Analisis Sentimen Media Sosial Secara Real-Time
Kita mulai dengan skenario yang sering dipelajari oleh orang-orang yang memulai dengan machine learning: analisis sentimen media sosial secara real-time.

Misalnya, Anda menjalankan situs web media berita dan ingin memanfaatkan data langsung untuk memahami konten apa yang mungkin menarik bagi pembaca Anda. Untuk mengetahui lebih lanjut tentang itu, Anda dapat membuat program yang melakukan analisis sentimen real-time dari data publikasi Twitter, pada topik yang relevan dengan pembaca Anda.

Indikator utama yang akan Anda lihat adalah volume tweet pada topik tertentu (hashtag) dan sentimen, yang ditentukan menggunakan alat analitik yang melakukan analisis sentimen seputar topik yang ditentukan.

Langkah-langkah yang diperlukan untuk membuat proyek ini adalah sebagai berikut:

* Buat event hub untuk streaming input, yang akan mengumpulkan data dari Twitter.
* Konfigurasikan dan mulai aplikasi klien Twitter, yang akan memanggil API Streaming Twitter.
* Buat pekerjaan Stream Analytics.
* Tentukan input dan query pekerjaan.
* Buat output sink dan tentukan output pekerjaan.
* Mulai pekerjaan.

Untuk melihat proses lengkapnya, kunjungi [dokumentasi](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analisis Makalah Ilmiah
Mari kita ambil contoh lain dari proyek yang dibuat oleh [Dmitry Soshnikov](http://soshnikov.com), salah satu penulis kurikulum ini.

Dmitry membuat alat yang menganalisis makalah COVID. Dengan meninjau proyek ini, Anda akan melihat bagaimana Anda dapat membuat alat yang mengekstrak pengetahuan dari makalah ilmiah, mendapatkan wawasan, dan membantu peneliti menavigasi melalui koleksi makalah yang besar dengan cara yang efisien.

Mari kita lihat langkah-langkah yang digunakan untuk ini:
* Mengekstrak dan memproses informasi dengan [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Menggunakan [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) untuk memproses secara paralel.
* Menyimpan dan melakukan query informasi dengan [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Membuat dashboard interaktif untuk eksplorasi dan visualisasi data menggunakan Power BI.

Untuk melihat proses lengkapnya, kunjungi [blog Dmitry](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Seperti yang Anda lihat, kita dapat memanfaatkan layanan Cloud dengan berbagai cara untuk melakukan Data Science.

## Catatan Kaki

Sumber:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Kuis Pasca-Kuliah

## [Kuis Pasca-Kuliah](https://ff-quizzes.netlify.app/en/ds/)

## Tugas

[Penelitian Pasar](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.