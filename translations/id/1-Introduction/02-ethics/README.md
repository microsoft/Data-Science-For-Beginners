<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a34157cc63516eba97c89a0b2f8c3e6",
  "translation_date": "2025-09-03T21:37:18+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "id"
}
-->
# Pengantar Etika Data

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Etika Data Sains - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

---

Kita semua adalah warga data yang hidup di dunia yang dipenuhi data.

Tren pasar menunjukkan bahwa pada tahun 2022, 1 dari 3 organisasi besar akan membeli dan menjual data mereka melalui [Marketplace dan Exchange](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) online. Sebagai **Pengembang Aplikasi**, kita akan menemukan bahwa semakin mudah dan murah untuk mengintegrasikan wawasan berbasis data dan otomatisasi berbasis algoritma ke dalam pengalaman pengguna sehari-hari. Namun, seiring dengan semakin meluasnya AI, kita juga perlu memahami potensi bahaya yang disebabkan oleh [weaponisasi](https://www.youtube.com/watch?v=TQHs8SA1qpk) algoritma semacam itu dalam skala besar.

Tren juga menunjukkan bahwa kita akan menciptakan dan mengonsumsi lebih dari [180 zettabyte](https://www.statista.com/statistics/871513/worldwide-data-created/) data pada tahun 2025. Sebagai **Ilmuwan Data**, ini memberi kita akses yang belum pernah terjadi sebelumnya ke data pribadi. Ini berarti kita dapat membangun profil perilaku pengguna dan memengaruhi pengambilan keputusan dengan cara yang menciptakan [ilusi pilihan bebas](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) sambil secara potensial mendorong pengguna menuju hasil yang kita inginkan. Hal ini juga menimbulkan pertanyaan yang lebih luas tentang privasi data dan perlindungan pengguna.

Etika data kini menjadi _pagar pengaman yang diperlukan_ untuk ilmu data dan rekayasa, membantu kita meminimalkan potensi bahaya dan konsekuensi yang tidak diinginkan dari tindakan berbasis data kita. [Gartner Hype Cycle untuk AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) mengidentifikasi tren relevan dalam etika digital, AI yang bertanggung jawab, dan tata kelola AI sebagai pendorong utama untuk megatren yang lebih besar seputar _demokratisasi_ dan _industrialisasi_ AI.

![Gartner's Hype Cycle untuk AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Dalam pelajaran ini, kita akan menjelajahi area menarik dari etika data - mulai dari konsep inti dan tantangan, hingga studi kasus dan konsep AI terapan seperti tata kelola - yang membantu membangun budaya etika dalam tim dan organisasi yang bekerja dengan data dan AI.

## [Kuis Pra-Kuliah](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Definisi Dasar

Mari kita mulai dengan memahami terminologi dasar.

Kata "etika" berasal dari [kata Yunani "ethikos"](https://en.wikipedia.org/wiki/Ethics) (dan akar katanya "ethos") yang berarti _karakter atau sifat moral_. 

**Etika** adalah tentang nilai-nilai bersama dan prinsip moral yang mengatur perilaku kita dalam masyarakat. Etika tidak didasarkan pada hukum tetapi pada norma yang diterima secara luas tentang apa yang "benar vs. salah". Namun, pertimbangan etika dapat memengaruhi inisiatif tata kelola perusahaan dan regulasi pemerintah yang menciptakan lebih banyak insentif untuk kepatuhan.

**Etika Data** adalah [cabang baru dari etika](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) yang "mempelajari dan mengevaluasi masalah moral terkait _data, algoritma, dan praktik terkait_". Di sini, **"data"** berfokus pada tindakan terkait pembuatan, pencatatan, kurasi, pemrosesan, penyebaran, berbagi, dan penggunaan, **"algoritma"** berfokus pada AI, agen, pembelajaran mesin, dan robot, dan **"praktik"** berfokus pada topik seperti inovasi yang bertanggung jawab, pemrograman, peretasan, dan kode etika.

**Etika Terapan** adalah [penerapan praktis dari pertimbangan moral](https://en.wikipedia.org/wiki/Applied_ethics). Ini adalah proses aktif menyelidiki masalah etika dalam konteks _tindakan, produk, dan proses dunia nyata_, serta mengambil langkah-langkah korektif untuk memastikan bahwa tindakan tersebut tetap selaras dengan nilai-nilai etika yang telah ditentukan.

**Budaya Etika** adalah tentang [_mengoperasionalkan_ etika terapan](https://hbr.org/2019/05/how-to-design-an-ethical-organization) untuk memastikan bahwa prinsip dan praktik etika kita diadopsi secara konsisten dan dapat diskalakan di seluruh organisasi. Budaya etika yang sukses mendefinisikan prinsip etika di seluruh organisasi, memberikan insentif yang berarti untuk kepatuhan, dan memperkuat norma etika dengan mendorong dan memperkuat perilaku yang diinginkan di setiap tingkat organisasi.

## Konsep Etika

Dalam bagian ini, kita akan membahas konsep seperti **nilai bersama** (prinsip) dan **tantangan etika** (masalah) untuk etika data - serta mengeksplorasi **studi kasus** yang membantu Anda memahami konsep-konsep ini dalam konteks dunia nyata.

### 1. Prinsip Etika

Setiap strategi etika data dimulai dengan mendefinisikan _prinsip etika_ - "nilai bersama" yang menggambarkan perilaku yang dapat diterima, dan membimbing tindakan yang sesuai, dalam proyek data & AI kita. Anda dapat mendefinisikan ini di tingkat individu atau tim. Namun, sebagian besar organisasi besar merumuskan ini dalam pernyataan misi atau kerangka kerja _AI etis_ yang ditentukan di tingkat korporat dan ditegakkan secara konsisten di semua tim.

**Contoh:** Pernyataan misi [AI yang Bertanggung Jawab](https://www.microsoft.com/en-us/ai/responsible-ai) Microsoft berbunyi: _"Kami berkomitmen untuk kemajuan AI yang didorong oleh prinsip etika yang mengutamakan manusia"_ - mengidentifikasi 6 prinsip etika dalam kerangka kerja berikut:

![AI yang Bertanggung Jawab di Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Mari kita jelajahi prinsip-prinsip ini secara singkat. _Transparansi_ dan _akuntabilitas_ adalah nilai-nilai dasar yang menjadi landasan prinsip lainnya - jadi mari kita mulai dari sana:

* [**Akuntabilitas**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) membuat praktisi _bertanggung jawab_ atas operasi data & AI mereka, serta kepatuhan terhadap prinsip etika ini.
* [**Transparansi**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) memastikan bahwa tindakan data dan AI _dapat dipahami_ (dapat diinterpretasikan) oleh pengguna, menjelaskan apa dan mengapa di balik keputusan.
* [**Keadilan**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - berfokus pada memastikan AI memperlakukan _semua orang_ secara adil, mengatasi bias sosial-teknis sistemik atau implisit dalam data dan sistem.
* [**Keandalan & Keamanan**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - memastikan bahwa AI berperilaku _konsisten_ dengan nilai-nilai yang ditentukan, meminimalkan potensi bahaya atau konsekuensi yang tidak diinginkan.
* [**Privasi & Keamanan**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - tentang memahami asal-usul data, dan memberikan _privasi data serta perlindungan terkait_ kepada pengguna.
* [**Inklusivitas**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - tentang merancang solusi AI dengan niat, menyesuaikannya untuk memenuhi _beragam kebutuhan_ & kemampuan manusia.

> 🚨 Pikirkan tentang apa pernyataan misi etika data Anda. Jelajahi kerangka kerja AI etis dari organisasi lain - berikut adalah contoh dari [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), dan [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Nilai bersama apa yang mereka miliki? Bagaimana prinsip-prinsip ini terkait dengan produk AI atau industri tempat mereka beroperasi?

### 2. Tantangan Etika

Setelah kita mendefinisikan prinsip etika, langkah berikutnya adalah mengevaluasi tindakan data dan AI kita untuk melihat apakah tindakan tersebut selaras dengan nilai-nilai bersama tersebut. Pikirkan tindakan Anda dalam dua kategori: _pengumpulan data_ dan _desain algoritma_. 

Dalam pengumpulan data, tindakan kemungkinan melibatkan **data pribadi** atau informasi yang dapat diidentifikasi secara pribadi (PII) untuk individu yang dapat diidentifikasi. Ini mencakup [beragam item data non-pribadi](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) yang _secara kolektif_ mengidentifikasi individu. Tantangan etika dapat berkaitan dengan _privasi data_, _kepemilikan data_, dan topik terkait seperti _persetujuan yang diinformasikan_ dan _hak kekayaan intelektual_ untuk pengguna.

Dalam desain algoritma, tindakan akan melibatkan pengumpulan & kurasi **dataset**, lalu menggunakannya untuk melatih & menerapkan **model data** yang memprediksi hasil atau mengotomatisasi keputusan dalam konteks dunia nyata. Tantangan etika dapat muncul dari _bias dataset_, masalah _kualitas data_, _ketidakadilan_, dan _kesalahan representasi_ dalam algoritma - termasuk beberapa masalah yang bersifat sistemik.

Dalam kedua kasus, tantangan etika menyoroti area di mana tindakan kita mungkin bertentangan dengan nilai-nilai bersama kita. Untuk mendeteksi, mengurangi, meminimalkan, atau menghilangkan kekhawatiran ini - kita perlu mengajukan pertanyaan moral "ya/tidak" terkait tindakan kita, lalu mengambil tindakan korektif sesuai kebutuhan. Mari kita lihat beberapa tantangan etika dan pertanyaan moral yang mereka timbulkan:

#### 2.1 Kepemilikan Data

Pengumpulan data sering kali melibatkan data pribadi yang dapat mengidentifikasi subjek data. [Kepemilikan data](https://permission.io/blog/data-ownership) adalah tentang _kontrol_ dan [_hak pengguna_](https://permission.io/blog/data-ownership) terkait pembuatan, pemrosesan, dan penyebaran data. 

Pertanyaan moral yang perlu kita ajukan adalah: 
 * Siapa yang memiliki data? (pengguna atau organisasi)
 * Hak apa yang dimiliki subjek data? (misalnya: akses, penghapusan, portabilitas)
 * Hak apa yang dimiliki organisasi? (misalnya: memperbaiki ulasan pengguna yang berbahaya)

#### 2.2 Persetujuan yang Diinformasikan

[Persetujuan yang diinformasikan](https://legaldictionary.net/informed-consent/) mendefinisikan tindakan pengguna yang menyetujui suatu tindakan (seperti pengumpulan data) dengan _pemahaman penuh_ tentang fakta relevan termasuk tujuan, potensi risiko, dan alternatif. 

Pertanyaan yang perlu dieksplorasi di sini adalah:
 * Apakah pengguna (subjek data) memberikan izin untuk pengambilan dan penggunaan data?
 * Apakah pengguna memahami tujuan pengambilan data tersebut?
 * Apakah pengguna memahami potensi risiko dari partisipasi mereka?

#### 2.3 Kekayaan Intelektual

[Kekayaan intelektual](https://en.wikipedia.org/wiki/Intellectual_property) mengacu pada kreasi tak berwujud yang dihasilkan dari inisiatif manusia, yang mungkin _memiliki nilai ekonomi_ bagi individu atau bisnis. 

Pertanyaan yang perlu dieksplorasi di sini adalah:
 * Apakah data yang dikumpulkan memiliki nilai ekonomi bagi pengguna atau bisnis?
 * Apakah **pengguna** memiliki kekayaan intelektual di sini?
 * Apakah **organisasi** memiliki kekayaan intelektual di sini?
 * Jika hak-hak ini ada, bagaimana kita melindunginya?

#### 2.4 Privasi Data

[Privasi data](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) atau privasi informasi mengacu pada pelestarian privasi pengguna dan perlindungan identitas pengguna terkait informasi yang dapat diidentifikasi secara pribadi. 

Pertanyaan yang perlu dieksplorasi di sini adalah:
 * Apakah data (pribadi) pengguna aman dari peretasan dan kebocoran?
 * Apakah data pengguna hanya dapat diakses oleh pengguna dan konteks yang berwenang?
 * Apakah anonimitas pengguna terjaga saat data dibagikan atau disebarluaskan?
 * Bisakah pengguna diidentifikasi dari dataset yang dianonimkan?

#### 2.5 Hak untuk Dilupakan

[Hak untuk Dilupakan](https://en.wikipedia.org/wiki/Right_to_be_forgotten) atau [Hak untuk Penghapusan](https://www.gdpreu.org/right-to-be-forgotten/) memberikan perlindungan data pribadi tambahan kepada pengguna. Secara khusus, ini memberikan hak kepada pengguna untuk meminta penghapusan atau penghapusan data pribadi dari pencarian Internet dan lokasi lainnya, _dalam keadaan tertentu_ - memungkinkan mereka memulai kembali secara online tanpa tindakan masa lalu yang membebani mereka.

Pertanyaan yang perlu dieksplorasi di sini adalah:
 * Apakah sistem memungkinkan subjek data untuk meminta penghapusan?
 * Haruskah penarikan persetujuan pengguna memicu penghapusan otomatis?
 * Apakah data dikumpulkan tanpa persetujuan atau dengan cara yang melanggar hukum?
 * Apakah kita mematuhi peraturan pemerintah untuk privasi data?

#### 2.6 Bias Dataset

Bias Dataset atau [Bias Pengumpulan](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) adalah tentang memilih subset data yang _tidak representatif_ untuk pengembangan algoritma, menciptakan potensi ketidakadilan dalam hasil untuk kelompok yang beragam. Jenis bias termasuk bias seleksi atau sampling, bias sukarelawan, dan bias instrumen. 

Pertanyaan yang perlu dieksplorasi di sini adalah:
 * Apakah kita merekrut set subjek data yang representatif?
 * Apakah kita menguji dataset yang dikumpulkan atau dikurasi untuk berbagai bias?
 * Bisakah kita mengurangi atau menghilangkan bias yang ditemukan?

#### 2.7 Kualitas Data

[Kualitas Data](https://lakefs.io/data-quality-testing/) melihat validitas dataset yang dikurasi yang digunakan untuk mengembangkan algoritma kita, memeriksa apakah fitur dan catatan memenuhi persyaratan untuk tingkat akurasi dan konsistensi yang diperlukan untuk tujuan AI kita.

Pertanyaan yang perlu dieksplorasi di sini adalah:
 * Apakah kita menangkap _fitur_ yang valid untuk kasus penggunaan kita?
 * Apakah data ditangkap _secara konsisten_ di berbagai sumber data?
 * Apakah dataset _lengkap_ untuk kondisi atau skenario yang beragam?
 * Apakah informasi yang ditangkap _akurat_ dalam mencerminkan kenyataan?
[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) memeriksa apakah desain algoritma secara sistematis mendiskriminasi kelompok tertentu dari subjek data, yang dapat menyebabkan [potensi kerugian](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) dalam _alokasi_ (di mana sumber daya ditolak atau ditahan dari kelompok tersebut) dan _kualitas layanan_ (di mana AI tidak seakurat untuk beberapa kelompok dibandingkan dengan yang lain).

Pertanyaan yang dapat dieksplorasi di sini adalah:
 * Apakah kita mengevaluasi akurasi model untuk berbagai kelompok dan kondisi?
 * Apakah kita memeriksa sistem untuk potensi kerugian (misalnya, stereotip)?
 * Bisakah kita merevisi data atau melatih ulang model untuk mengurangi kerugian yang teridentifikasi?

Jelajahi sumber daya seperti [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) untuk mempelajari lebih lanjut.

#### 2.9 Misrepresentasi

[Misrepresentasi Data](https://www.sciencedirect.com/topics/computer-science/misrepresentation) berkaitan dengan apakah kita menyampaikan wawasan dari data yang dilaporkan secara jujur dengan cara yang menyesatkan untuk mendukung narasi yang diinginkan.

Pertanyaan yang dapat dieksplorasi di sini adalah:
 * Apakah kita melaporkan data yang tidak lengkap atau tidak akurat?
 * Apakah kita memvisualisasikan data dengan cara yang menghasilkan kesimpulan yang menyesatkan?
 * Apakah kita menggunakan teknik statistik selektif untuk memanipulasi hasil?
 * Apakah ada penjelasan alternatif yang mungkin menawarkan kesimpulan berbeda?

#### 2.10 Pilihan Bebas
[Ilusi Pilihan Bebas](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) terjadi ketika "arsitektur pilihan" sistem menggunakan algoritma pengambilan keputusan untuk mendorong orang mengambil hasil yang diinginkan sambil tampak memberikan mereka opsi dan kendali. [Pola gelap](https://www.darkpatterns.org/) ini dapat menyebabkan kerugian sosial dan ekonomi bagi pengguna. Karena keputusan pengguna memengaruhi profil perilaku, tindakan ini berpotensi mendorong pilihan di masa depan yang dapat memperkuat atau memperluas dampak kerugian ini.

Pertanyaan yang dapat dieksplorasi di sini adalah:
 * Apakah pengguna memahami implikasi dari membuat pilihan tersebut?
 * Apakah pengguna menyadari pilihan (alternatif) dan pro & kontra dari masing-masing?
 * Bisakah pengguna membatalkan pilihan yang otomatis atau dipengaruhi di kemudian hari?

### 3. Studi Kasus

Untuk menempatkan tantangan etika ini dalam konteks dunia nyata, penting untuk melihat studi kasus yang menyoroti potensi kerugian dan konsekuensi bagi individu dan masyarakat ketika pelanggaran etika seperti ini diabaikan.

Berikut beberapa contohnya:

| Tantangan Etika | Studi Kasus  | 
|--- |--- |
| **Persetujuan Informasi** | 1972 - [Tuskegee Syphilis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Pria Afrika-Amerika yang berpartisipasi dalam studi dijanjikan perawatan medis gratis _tetapi ditipu_ oleh peneliti yang gagal memberi tahu subjek tentang diagnosis mereka atau tentang ketersediaan pengobatan. Banyak subjek meninggal & pasangan atau anak-anak mereka terpengaruh; studi berlangsung selama 40 tahun. | 
| **Privasi Data** |  2007 - [Netflix data prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) memberikan peneliti _10 juta peringkat film anonim dari 50 ribu pelanggan_ untuk membantu meningkatkan algoritma rekomendasi. Namun, peneliti dapat menghubungkan data anonim dengan data yang dapat diidentifikasi secara pribadi dalam _dataset eksternal_ (misalnya, komentar IMDb) - secara efektif "mendeanonimkan" beberapa pelanggan Netflix.|
| **Bias Pengumpulan**  | 2013 - Kota Boston [mengembangkan Street Bump](https://www.boston.gov/transportation/street-bump), sebuah aplikasi yang memungkinkan warga melaporkan lubang jalan, memberikan data jalan yang lebih baik kepada kota untuk menemukan dan memperbaiki masalah. Namun, [orang-orang dalam kelompok berpenghasilan rendah memiliki akses lebih sedikit ke mobil dan ponsel](https://hbr.org/2013/04/the-hidden-biases-in-big-data), membuat masalah jalan mereka tidak terlihat dalam aplikasi ini. Pengembang bekerja dengan akademisi untuk mengatasi masalah _akses yang adil dan kesenjangan digital_ demi keadilan. |
| **Keadilan Algoritmik**  | 2018 - Studi MIT [Gender Shades Study](http://gendershades.org/overview.html) mengevaluasi akurasi produk AI klasifikasi gender, mengungkapkan kesenjangan akurasi untuk wanita dan orang kulit berwarna. Sebuah [Apple Card 2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) tampaknya menawarkan kredit lebih sedikit kepada wanita dibandingkan pria. Keduanya menggambarkan masalah bias algoritmik yang menyebabkan kerugian sosial-ekonomi.|
| **Misrepresentasi Data** | 2020 - [Departemen Kesehatan Georgia merilis grafik COVID-19](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) yang tampaknya menyesatkan warga tentang tren kasus yang dikonfirmasi dengan pengurutan non-kronologis pada sumbu x. Ini menggambarkan misrepresentasi melalui trik visualisasi. |
| **Ilusi pilihan bebas** | 2020 - Aplikasi pembelajaran [ABCmouse membayar $10 juta untuk menyelesaikan keluhan FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) di mana orang tua terjebak membayar langganan yang tidak dapat mereka batalkan. Ini menggambarkan pola gelap dalam arsitektur pilihan, di mana pengguna didorong menuju pilihan yang berpotensi merugikan. |
| **Privasi Data & Hak Pengguna** | 2021 - [Kebocoran Data Facebook](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) mengekspos data dari 530 juta pengguna, menghasilkan penyelesaian $5 miliar kepada FTC. Namun, Facebook menolak memberi tahu pengguna tentang pelanggaran tersebut, melanggar hak pengguna terkait transparansi data dan akses. |

Ingin menjelajahi lebih banyak studi kasus? Lihat sumber daya berikut:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - dilema etika di berbagai industri. 
* [Kursus Etika Data Science](https://www.coursera.org/learn/data-science-ethics#syllabus) - studi kasus penting yang dieksplorasi.
* [Di mana hal-hal telah salah](https://deon.drivendata.org/examples/) - daftar periksa deon dengan contoh-contoh.

> 🚨 Pikirkan tentang studi kasus yang telah Anda lihat - apakah Anda pernah mengalami, atau terpengaruh oleh, tantangan etika serupa dalam hidup Anda? Bisakah Anda memikirkan setidaknya satu studi kasus lain yang menggambarkan salah satu tantangan etika yang telah kita bahas di bagian ini?

## Etika Terapan

Kita telah membahas konsep etika, tantangan, dan studi kasus dalam konteks dunia nyata. Tetapi bagaimana kita memulai _menerapkan_ prinsip dan praktik etika dalam proyek kita? Dan bagaimana kita _mengoperasionalkan_ praktik ini untuk tata kelola yang lebih baik? Mari kita eksplorasi beberapa solusi dunia nyata:

### 1. Kode Profesional

Kode Profesional menawarkan satu opsi bagi organisasi untuk "mendorong" anggota mendukung prinsip etika mereka dan pernyataan misi. Kode adalah _panduan moral_ untuk perilaku profesional, membantu karyawan atau anggota membuat keputusan yang selaras dengan prinsip organisasi mereka. Kode ini hanya sebaik kepatuhan sukarela dari anggota; namun, banyak organisasi menawarkan penghargaan dan hukuman tambahan untuk memotivasi kepatuhan dari anggota.

Contoh meliputi:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Kode Etika
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Kode Perilaku (dibuat 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (sejak 1993)

> 🚨 Apakah Anda tergabung dalam organisasi profesional teknik atau data science? Jelajahi situs mereka untuk melihat apakah mereka mendefinisikan kode etika profesional. Apa yang dikatakan tentang prinsip etika mereka? Bagaimana mereka "mendorong" anggota untuk mengikuti kode tersebut?

### 2. Daftar Periksa Etika

Sementara kode profesional mendefinisikan _perilaku etis_ yang diperlukan dari praktisi, mereka [memiliki keterbatasan yang diketahui](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) dalam penegakan, terutama dalam proyek skala besar. Sebagai gantinya, banyak ahli data science [menganjurkan daftar periksa](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), yang dapat **menghubungkan prinsip dengan praktik** dengan cara yang lebih deterministik dan dapat ditindaklanjuti.

Daftar periksa mengubah pertanyaan menjadi tugas "ya/tidak" yang dapat dioperasionalkan, memungkinkan mereka untuk dilacak sebagai bagian dari alur kerja rilis produk standar.

Contoh meliputi:
 * [Deon](https://deon.drivendata.org/) - daftar periksa etika data umum yang dibuat dari [rekomendasi industri](https://deon.drivendata.org/#checklist-citations) dengan alat baris perintah untuk integrasi yang mudah.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - memberikan panduan umum untuk praktik penanganan informasi dari perspektif eksposur hukum dan sosial.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - dibuat oleh praktisi AI untuk mendukung adopsi dan integrasi pemeriksaan keadilan dalam siklus pengembangan AI.
 * [22 pertanyaan untuk etika dalam data dan AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - kerangka kerja yang lebih terbuka, terstruktur untuk eksplorasi awal masalah etika dalam desain, implementasi, dan konteks organisasi.

### 3. Regulasi Etika

Etika adalah tentang mendefinisikan nilai-nilai bersama dan melakukan hal yang benar _secara sukarela_. **Kepatuhan** adalah tentang _mematuhi hukum_ jika dan di mana ditentukan. **Tata kelola** secara luas mencakup semua cara di mana organisasi beroperasi untuk menegakkan prinsip etika dan mematuhi hukum yang telah ditetapkan.

Saat ini, tata kelola mengambil dua bentuk dalam organisasi. Pertama, ini tentang mendefinisikan prinsip **AI etis** dan menetapkan praktik untuk mengoperasionalkan adopsi di semua proyek terkait AI dalam organisasi. Kedua, ini tentang mematuhi semua **regulasi perlindungan data** yang diwajibkan pemerintah untuk wilayah tempat organisasi beroperasi.

Contoh regulasi perlindungan data dan privasi:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - mengatur pengumpulan, penggunaan, dan pengungkapan informasi pribadi oleh _pemerintah federal_.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - melindungi data kesehatan pribadi.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - melindungi privasi data anak-anak di bawah 13 tahun.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - memberikan hak pengguna, perlindungan data, dan privasi.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) memberikan konsumen lebih banyak _hak_ atas data (pribadi) mereka.
 * `2021`, [Undang-Undang Perlindungan Informasi Pribadi China](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) baru saja disahkan, menciptakan salah satu regulasi privasi data online terkuat di dunia.

> 🚨 Uni Eropa mendefinisikan GDPR (General Data Protection Regulation) yang tetap menjadi salah satu regulasi privasi data paling berpengaruh saat ini. Tahukah Anda bahwa GDPR juga mendefinisikan [8 hak pengguna](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) untuk melindungi privasi digital dan data pribadi warga? Pelajari tentang apa saja hak tersebut, dan mengapa itu penting.

### 4. Budaya Etika

Perlu dicatat bahwa masih ada kesenjangan tak berwujud antara _kepatuhan_ (melakukan cukup untuk memenuhi "huruf hukum") dan mengatasi [masalah sistemik](https://www.coursera.org/learn/data-science-ethics/home/week/4) (seperti osifikasi, asimetri informasi, dan ketidakadilan distribusi) yang dapat mempercepat penggunaan AI sebagai senjata.

Yang terakhir membutuhkan [pendekatan kolaboratif untuk mendefinisikan budaya etika](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) yang membangun koneksi emosional dan nilai-nilai bersama yang konsisten _di seluruh organisasi_ dalam industri. Ini menyerukan lebih banyak [budaya etika data yang diformalkan](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) dalam organisasi - memungkinkan _siapa pun_ untuk [menarik tali Andon](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (untuk mengangkat kekhawatiran etika lebih awal dalam proses) dan menjadikan _penilaian etika_ (misalnya, dalam perekrutan) sebagai kriteria inti pembentukan tim dalam proyek AI.

---
## [Kuis pasca-kuliah](https://ff-quizzes.netlify.app/en/ds/) 🎯
## Tinjauan & Studi Mandiri 

Kursus dan buku membantu memahami konsep etika inti dan tantangan, sementara studi kasus dan alat membantu dengan praktik etika terapan dalam konteks dunia nyata. Berikut beberapa sumber daya untuk memulai.

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - pelajaran tentang Keadilan, dari Microsoft.
* [Prinsip AI yang Bertanggung Jawab](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - jalur pembelajaran gratis dari Microsoft Learn.
* [Etika dan Ilmu Data](https://resources.oreilly.com/examples/0636920203964) - EBook O'Reilly (M. Loukides, H. Mason, dan lainnya)
* [Etika Ilmu Data](https://www.coursera.org/learn/data-science-ethics#syllabus) - kursus online dari Universitas Michigan.
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - studi kasus dari Universitas Texas.

# Tugas 

[Tulis Studi Kasus Etika Data](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.