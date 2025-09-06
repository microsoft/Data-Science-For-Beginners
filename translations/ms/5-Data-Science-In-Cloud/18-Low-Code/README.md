<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4da10766c64fce4294a98f6479dfb0",
  "translation_date": "2025-09-06T00:01:53+00:00",
  "source_file": "5-Data-Science-In-Cloud/18-Low-Code/README.md",
  "language_code": "ms"
}
-->
# Sains Data di Awan: Cara "Kod Rendah/Tiada Kod"

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/18-DataScience-Cloud.png)|
|:---:|
| Sains Data di Awan: Kod Rendah - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Kandungan:

- [Sains Data di Awan: Cara "Kod Rendah/Tiada Kod"](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Kuiz Pra-Kuliah](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [1. Pengenalan](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.1 Apa itu Azure Machine Learning?](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.2 Projek Ramalan Kegagalan Jantung:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.3 Dataset Kegagalan Jantung:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [2. Latihan model Kod Rendah/Tiada Kod dalam Azure ML Studio](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.1 Cipta ruang kerja Azure ML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.2 Sumber Pengiraan](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.1 Memilih pilihan yang sesuai untuk sumber pengiraan anda](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.2 Mencipta kluster pengiraan](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.3 Memuatkan Dataset](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.4 Latihan Kod Rendah/Tiada Kod dengan AutoML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [3. Penyebaran model Kod Rendah/Tiada Kod dan penggunaan titik akhir](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.1 Penyebaran model](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.2 Penggunaan titik akhir](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [🚀 Cabaran](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Kuiz Pasca-Kuliah](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Ulasan & Kajian Kendiri](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Tugasan](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  
## [Kuiz Pra-Kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/34)

## 1. Pengenalan
### 1.1 Apa itu Azure Machine Learning?

Platform awan Azure menawarkan lebih daripada 200 produk dan perkhidmatan awan yang direka untuk membantu anda merealisasikan penyelesaian baharu. Saintis data menghabiskan banyak masa untuk meneroka dan memproses data, serta mencuba pelbagai jenis algoritma latihan model untuk menghasilkan model yang tepat. Tugas-tugas ini memakan masa dan sering menggunakan perkakasan pengiraan yang mahal secara tidak efisien.

[Azure ML](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ialah platform berasaskan awan untuk membina dan mengendalikan penyelesaian pembelajaran mesin di Azure. Ia merangkumi pelbagai ciri dan keupayaan yang membantu saintis data menyediakan data, melatih model, menerbitkan perkhidmatan ramalan, dan memantau penggunaannya. Yang paling penting, ia membantu meningkatkan kecekapan dengan mengautomasi banyak tugas yang memakan masa yang berkaitan dengan latihan model; dan membolehkan mereka menggunakan sumber pengiraan berasaskan awan yang boleh diskalakan secara efektif untuk mengendalikan jumlah data yang besar sambil menanggung kos hanya apabila digunakan.

Azure ML menyediakan semua alat yang diperlukan oleh pembangun dan saintis data untuk aliran kerja pembelajaran mesin mereka. Ini termasuk:

- **Azure Machine Learning Studio**: portal web dalam Azure Machine Learning untuk pilihan kod rendah dan tiada kod untuk latihan model, penyebaran, automasi, penjejakan, dan pengurusan aset. Studio ini berintegrasi dengan Azure Machine Learning SDK untuk pengalaman yang lancar.
- **Jupyter Notebooks**: prototaip dan ujian model ML dengan cepat.
- **Azure Machine Learning Designer**: membolehkan seret-dan-lepas modul untuk membina eksperimen dan kemudian menyebarkan saluran paip dalam persekitaran kod rendah.
- **Antara muka automasi pembelajaran mesin (AutoML)**: mengautomasi tugas berulang dalam pembangunan model pembelajaran mesin, membolehkan pembinaan model ML dengan skala tinggi, kecekapan, dan produktiviti, sambil mengekalkan kualiti model.
- **Pelabelan Data**: alat ML yang dibantu untuk melabel data secara automatik.
- **Sambungan pembelajaran mesin untuk Visual Studio Code**: menyediakan persekitaran pembangunan penuh untuk membina dan mengurus projek ML.
- **CLI pembelajaran mesin**: menyediakan arahan untuk mengurus sumber Azure ML dari baris arahan.
- **Integrasi dengan rangka kerja sumber terbuka** seperti PyTorch, TensorFlow, Scikit-learn, dan banyak lagi untuk melatih, menyebarkan, dan mengurus proses pembelajaran mesin dari awal hingga akhir.
- **MLflow**: perpustakaan sumber terbuka untuk mengurus kitaran hayat eksperimen pembelajaran mesin anda. **MLFlow Tracking** ialah komponen MLflow yang mencatat dan menjejaki metrik latihan dan artifak model anda, tanpa mengira persekitaran eksperimen anda.

### 1.2 Projek Ramalan Kegagalan Jantung:

Tidak diragukan lagi bahawa membuat dan membina projek adalah cara terbaik untuk menguji kemahiran dan pengetahuan anda. Dalam pelajaran ini, kita akan meneroka dua cara berbeza untuk membina projek sains data bagi ramalan serangan kegagalan jantung dalam Azure ML Studio, melalui Kod Rendah/Tiada Kod dan melalui Azure ML SDK seperti yang ditunjukkan dalam skema berikut:

![project-schema](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/project-schema.PNG)

Setiap cara mempunyai kelebihan dan kekurangannya sendiri. Cara Kod Rendah/Tiada Kod lebih mudah untuk dimulakan kerana ia melibatkan interaksi dengan GUI (Antara Muka Pengguna Grafik), tanpa memerlukan pengetahuan kod sebelumnya. Kaedah ini membolehkan ujian cepat terhadap kebolehlaksanaan projek dan mencipta POC (Bukti Konsep). Walau bagaimanapun, apabila projek berkembang dan perlu bersedia untuk pengeluaran, tidak praktikal untuk mencipta sumber melalui GUI. Kita perlu mengautomasi semuanya secara programatik, dari penciptaan sumber hingga penyebaran model. Di sinilah pengetahuan tentang cara menggunakan Azure ML SDK menjadi penting.

|                   | Kod Rendah/Tiada Kod | Azure ML SDK              |
|-------------------|-----------------------|---------------------------|
| Kepakaran kod     | Tidak diperlukan     | Diperlukan                |
| Masa pembangunan  | Cepat dan mudah      | Bergantung pada kepakaran kod |
| Sedia untuk pengeluaran | Tidak               | Ya                        |

### 1.3 Dataset Kegagalan Jantung: 

Penyakit kardiovaskular (CVD) adalah penyebab utama kematian di seluruh dunia, menyumbang 31% daripada semua kematian global. Faktor risiko persekitaran dan tingkah laku seperti penggunaan tembakau, diet tidak sihat dan obesiti, kurang aktiviti fizikal, dan penggunaan alkohol yang berbahaya boleh digunakan sebagai ciri untuk model anggaran. Keupayaan untuk menganggarkan kebarangkalian perkembangan CVD boleh sangat berguna untuk mencegah serangan pada individu berisiko tinggi.

Kaggle telah menyediakan [Dataset Kegagalan Jantung](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) secara umum, yang akan kita gunakan untuk projek ini. Anda boleh memuat turun dataset sekarang. Ini adalah dataset tabular dengan 13 lajur (12 ciri dan 1 pemboleh ubah sasaran) dan 299 baris. 

|    | Nama pemboleh ubah         | Jenis            | Penerangan                                                | Contoh            |
|----|----------------------------|------------------|----------------------------------------------------------|-------------------|
| 1  | age                        | numerik          | umur pesakit                                             | 25                |
| 2  | anaemia                    | boolean          | Penurunan sel darah merah atau hemoglobin                | 0 atau 1          |
| 3  | creatinine_phosphokinase   | numerik          | Tahap enzim CPK dalam darah                              | 542               |
| 4  | diabetes                   | boolean          | Jika pesakit mempunyai diabetes                          | 0 atau 1          |
| 5  | ejection_fraction          | numerik          | Peratusan darah yang keluar dari jantung pada setiap kontraksi | 45                |
| 6  | high_blood_pressure        | boolean          | Jika pesakit mempunyai hipertensi                        | 0 atau 1          |
| 7  | platelets                  | numerik          | Platelet dalam darah                                     | 149000            |
| 8  | serum_creatinine           | numerik          | Tahap serum kreatinin dalam darah                        | 0.5               |
| 9  | serum_sodium               | numerik          | Tahap serum natrium dalam darah                          | jun               |
| 10 | sex                        | boolean          | wanita atau lelaki                                       | 0 atau 1          |
| 11 | smoking                    | boolean          | Jika pesakit merokok                                     | 0 atau 1          |
| 12 | time                       | numerik          | tempoh susulan (hari)                                    | 4                 |
|----|----------------------------|------------------|----------------------------------------------------------|-------------------|
| 21 | DEATH_EVENT [Sasaran]      | boolean          | jika pesakit meninggal semasa tempoh susulan             | 0 atau 1          |

Setelah anda mempunyai dataset, kita boleh memulakan projek dalam Azure.

## 2. Latihan model Kod Rendah/Tiada Kod dalam Azure ML Studio
### 2.1 Cipta ruang kerja Azure ML
Untuk melatih model dalam Azure ML, anda perlu mencipta ruang kerja Azure ML terlebih dahulu. Ruang kerja adalah sumber peringkat tertinggi untuk Azure Machine Learning, menyediakan tempat berpusat untuk bekerja dengan semua artifak yang anda cipta semasa menggunakan Azure Machine Learning. Ruang kerja menyimpan sejarah semua latihan, termasuk log, metrik, output, dan snapshot skrip anda. Anda menggunakan maklumat ini untuk menentukan latihan mana yang menghasilkan model terbaik. [Ketahui lebih lanjut](https://docs.microsoft.com/azure/machine-learning/concept-workspace?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

Adalah disyorkan untuk menggunakan pelayar yang paling terkini yang serasi dengan sistem operasi anda. Pelayar berikut disokong:

- Microsoft Edge (Microsoft Edge baharu, versi terkini. Bukan Microsoft Edge legasi)
- Safari (versi terkini, hanya untuk Mac)
- Chrome (versi terkini)
- Firefox (versi terkini)

Untuk menggunakan Azure Machine Learning, cipta ruang kerja dalam langganan Azure anda. Anda kemudian boleh menggunakan ruang kerja ini untuk mengurus data, sumber pengiraan, kod, model, dan artifak lain yang berkaitan dengan beban kerja pembelajaran mesin anda.

> **_NOTA:_** Langganan Azure anda akan dikenakan sedikit bayaran untuk penyimpanan data selagi ruang kerja Azure Machine Learning wujud dalam langganan anda, jadi kami mengesyorkan anda memadam ruang kerja Azure Machine Learning apabila anda tidak lagi menggunakannya.

1. Log masuk ke [portal Azure](https://ms.portal.azure.com/) menggunakan kelayakan Microsoft yang dikaitkan dengan langganan Azure anda.
2. Pilih **＋Cipta sumber**
   
   ![workspace-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-1.PNG)

   Cari Machine Learning dan pilih jubin Machine Learning

   ![workspace-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-2.PNG)

   Klik butang cipta

   ![workspace-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-3.PNG)

   Isikan tetapan seperti berikut:
   - Langganan: Langganan Azure anda
   - Kumpulan sumber: Cipta atau pilih kumpulan sumber
   - Nama ruang kerja: Masukkan nama unik untuk ruang kerja anda
   - Wilayah: Pilih wilayah geografi yang paling dekat dengan anda
   - Akaun penyimpanan: Perhatikan akaun penyimpanan baharu lalai yang akan dicipta untuk ruang kerja anda
   - Key vault: Perhatikan key vault baharu lalai yang akan dicipta untuk ruang kerja anda
   - Application insights: Perhatikan sumber application insights baharu lalai yang akan dicipta untuk ruang kerja anda
   - Container registry: Tiada (satu akan dicipta secara automatik kali pertama anda menyebarkan model ke dalam kontena)

    ![workspace-4](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-4.PNG)

   - Klik butang cipta + semak dan kemudian pada butang cipta
3. Tunggu ruang kerja anda dicipta (ini mungkin mengambil masa beberapa minit). Kemudian pergi ke ruang kerja tersebut dalam portal. Anda boleh mencarinya melalui perkhidmatan Azure Machine Learning.
4. Pada halaman Gambaran Keseluruhan untuk ruang kerja anda, lancarkan Azure Machine Learning studio (atau buka tab pelayar baharu dan navigasi ke https://ml.azure.com), dan log masuk ke Azure Machine Learning studio menggunakan akaun Microsoft anda. Jika diminta, pilih direktori dan langganan Azure anda, serta ruang kerja Azure Machine Learning anda.
   
![workspace-5](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-5.PNG)

5. Dalam Azure Machine Learning studio, togol ikon ☰ di bahagian atas kiri untuk melihat pelbagai halaman dalam antara muka. Anda boleh menggunakan halaman ini untuk mengurus sumber dalam ruang kerja anda.

![workspace-6](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-6.PNG)

Anda boleh mengurus ruang kerja anda menggunakan portal Azure, tetapi untuk saintis data dan jurutera operasi Pembelajaran Mesin, Azure Machine Learning Studio menyediakan antara muka pengguna yang lebih fokus untuk mengurus sumber ruang kerja.

### 2.2 Sumber Pengiraan

Sumber Pengiraan adalah sumber berasaskan awan di mana anda boleh menjalankan proses latihan model dan penerokaan data. Terdapat empat jenis sumber pengiraan yang boleh anda cipta:

- **Compute Instances**: Stesen kerja pembangunan yang boleh digunakan oleh saintis data untuk bekerja dengan data dan model. Ini melibatkan penciptaan Mesin Maya (VM) dan melancarkan instans notebook. Anda kemudian boleh melatih model dengan memanggil kluster pengiraan dari notebook.
- **Compute Clusters**: Kluster VM yang boleh diskalakan untuk pemprosesan kod eksperimen atas permintaan. Anda akan memerlukannya semasa melatih model. Kluster pengiraan juga boleh menggunakan sumber GPU atau CPU khusus.
- **Inference Clusters**: Sasaran penyebaran untuk perkhidmatan ramalan yang menggunakan model terlatih anda.
- **Attached Compute**: Pautan kepada sumber pengiraan Azure yang sedia ada, seperti Virtual Machines atau kluster Azure Databricks.

#### 2.2.1 Memilih pilihan yang tepat untuk sumber pengiraan anda

Beberapa faktor utama perlu dipertimbangkan semasa mencipta sumber pengiraan, dan pilihan tersebut boleh menjadi keputusan yang kritikal.

**Adakah anda memerlukan CPU atau GPU?**

CPU (Central Processing Unit) ialah litar elektronik yang melaksanakan arahan dalam program komputer. GPU (Graphics Processing Unit) pula adalah litar elektronik khusus yang boleh melaksanakan kod berkaitan grafik pada kadar yang sangat tinggi.

Perbezaan utama antara seni bina CPU dan GPU ialah CPU direka untuk menangani pelbagai tugas dengan cepat (diukur dengan kelajuan jam CPU), tetapi terhad dalam keupayaan tugas serentak yang boleh dijalankan. GPU pula direka untuk pengiraan selari dan oleh itu jauh lebih baik untuk tugas pembelajaran mendalam.

| CPU                                     | GPU                         |
|-----------------------------------------|-----------------------------|
| Kurang mahal                            | Lebih mahal                 |
| Tahap serentak yang lebih rendah        | Tahap serentak yang lebih tinggi |
| Lebih perlahan dalam melatih model pembelajaran mendalam | Optimum untuk pembelajaran mendalam |

**Saiz Kluster**

Kluster yang lebih besar adalah lebih mahal tetapi akan memberikan respons yang lebih baik. Oleh itu, jika anda mempunyai masa tetapi kekurangan wang, anda harus bermula dengan kluster kecil. Sebaliknya, jika anda mempunyai wang tetapi kekurangan masa, anda harus bermula dengan kluster yang lebih besar.

**Saiz VM**

Bergantung pada kekangan masa dan bajet anda, anda boleh memvariasikan saiz RAM, cakera, bilangan teras, dan kelajuan jam. Meningkatkan semua parameter ini akan lebih mahal, tetapi akan memberikan prestasi yang lebih baik.

**Instance Berdedikasi atau Keutamaan Rendah?**

Instance keutamaan rendah bermaksud ia boleh terganggu: pada dasarnya, Microsoft Azure boleh mengambil sumber tersebut dan memberikannya kepada tugas lain, dengan itu mengganggu kerja. Instance berdedikasi, atau tidak boleh terganggu, bermaksud kerja tidak akan dihentikan tanpa kebenaran anda. Ini adalah satu lagi pertimbangan antara masa dan wang, kerana instance yang boleh terganggu adalah lebih murah daripada yang berdedikasi.

#### 2.2.2 Mencipta kluster pengiraan

Dalam [ruang kerja Azure ML](https://ml.azure.com/) yang telah kita cipta sebelum ini, pergi ke bahagian pengiraan dan anda akan dapat melihat pelbagai sumber pengiraan yang telah kita bincangkan (contohnya instance pengiraan, kluster pengiraan, kluster inferens, dan pengiraan yang dilampirkan). Untuk projek ini, kita akan memerlukan kluster pengiraan untuk melatih model. Dalam Studio, klik pada menu "Compute", kemudian tab "Compute cluster" dan klik pada butang "+ New" untuk mencipta kluster pengiraan.

![22](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-1.PNG)

1. Pilih pilihan anda: Dedicated vs Low priority, CPU atau GPU, saiz VM dan bilangan teras (anda boleh mengekalkan tetapan lalai untuk projek ini).
2. Klik pada butang Next.

![23](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-2.PNG)

3. Berikan kluster nama pengiraan.
4. Pilih pilihan anda: Bilangan minimum/maksimum nod, masa tidak aktif sebelum pengurangan skala, akses SSH. Perhatikan bahawa jika bilangan minimum nod adalah 0, anda akan menjimatkan wang apabila kluster tidak aktif. Perhatikan bahawa semakin tinggi bilangan maksimum nod, semakin pendek masa latihan. Bilangan maksimum nod yang disyorkan ialah 3.  
5. Klik pada butang "Create". Langkah ini mungkin mengambil masa beberapa minit.

![29](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-3.PNG)

Hebat! Sekarang kita mempunyai kluster pengiraan, kita perlu memuatkan data ke Azure ML Studio.

### 2.3 Memuatkan Dataset

1. Dalam [ruang kerja Azure ML](https://ml.azure.com/) yang telah kita cipta sebelum ini, klik pada "Datasets" di menu kiri dan klik pada butang "+ Create dataset" untuk mencipta dataset. Pilih pilihan "From local files" dan pilih dataset Kaggle yang telah kita muat turun sebelum ini.
   
   ![24](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-1.PNG)

2. Berikan dataset anda nama, jenis, dan deskripsi. Klik Next. Muat naik data daripada fail. Klik Next.
   
   ![25](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-2.PNG)

3. Dalam Schema, tukar jenis data kepada Boolean untuk ciri-ciri berikut: anaemia, diabetes, tekanan darah tinggi, jantina, merokok, dan DEATH_EVENT. Klik Next dan Klik Create.
   
   ![26](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-3.PNG)

Bagus! Sekarang dataset telah dimuatkan dan kluster pengiraan telah dicipta, kita boleh memulakan latihan model!

### 2.4 Latihan Low code/No code dengan AutoML

Pembangunan model pembelajaran mesin tradisional memerlukan banyak sumber, memerlukan pengetahuan domain yang signifikan, dan masa untuk menghasilkan serta membandingkan berpuluh-puluh model. Pembelajaran mesin automatik (AutoML) adalah proses mengautomasi tugas-tugas pembelajaran mesin yang memakan masa dan berulang. Ia membolehkan saintis data, penganalisis, dan pembangun membina model ML dengan skala, kecekapan, dan produktiviti yang tinggi, sambil mengekalkan kualiti model. Ia mengurangkan masa yang diperlukan untuk mendapatkan model ML yang sedia untuk pengeluaran dengan mudah dan cekap. [Ketahui lebih lanjut](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

1. Dalam [ruang kerja Azure ML](https://ml.azure.com/) yang telah kita cipta sebelum ini, klik pada "Automated ML" di menu kiri dan pilih dataset yang baru sahaja anda muat naik. Klik Next.

   ![27](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-1.PNG)

2. Masukkan nama eksperimen baru, lajur sasaran (DEATH_EVENT), dan kluster pengiraan yang telah kita cipta. Klik Next.
   
   ![28](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-2.PNG)

3. Pilih "Classification" dan Klik Finish. Langkah ini mungkin mengambil masa antara 30 minit hingga 1 jam, bergantung pada saiz kluster pengiraan anda.
    
    ![30](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-3.PNG)

4. Setelah proses selesai, klik pada tab "Automated ML", klik pada eksperimen anda, dan klik pada Algoritma dalam kad "Best model summary".
    
    ![31](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-4.PNG)

Di sini anda boleh melihat deskripsi terperinci tentang model terbaik yang dihasilkan oleh AutoML. Anda juga boleh meneroka model lain yang dihasilkan dalam tab Models. Luangkan beberapa minit untuk meneroka model dalam butang Explanations (preview). Setelah anda memilih model yang ingin digunakan (di sini kita akan memilih model terbaik yang dipilih oleh AutoML), kita akan melihat cara untuk melaksanakannya.

## 3. Pelaksanaan model Low code/No code dan penggunaan endpoint
### 3.1 Pelaksanaan model

Antara muka pembelajaran mesin automatik membolehkan anda melaksanakan model terbaik sebagai perkhidmatan web dalam beberapa langkah. Pelaksanaan adalah integrasi model supaya ia boleh membuat ramalan berdasarkan data baru dan mengenal pasti potensi peluang. Untuk projek ini, pelaksanaan ke perkhidmatan web bermaksud aplikasi perubatan akan dapat menggunakan model untuk membuat ramalan langsung tentang risiko pesakit mereka mengalami serangan jantung.

Dalam deskripsi model terbaik, klik pada butang "Deploy".
    
![deploy-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-1.PNG)

15. Berikan nama, deskripsi, jenis pengiraan (Azure Container Instance), aktifkan pengesahan, dan klik pada Deploy. Langkah ini mungkin mengambil masa kira-kira 20 minit untuk diselesaikan. Proses pelaksanaan melibatkan beberapa langkah termasuk mendaftarkan model, menjana sumber, dan mengkonfigurasinya untuk perkhidmatan web. Mesej status akan muncul di bawah status Deploy. Pilih Refresh secara berkala untuk memeriksa status pelaksanaan. Ia akan dilaksanakan dan berjalan apabila statusnya adalah "Healthy".

![deploy-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-2.PNG)

16. Setelah ia dilaksanakan, klik pada tab Endpoint dan klik pada endpoint yang baru sahaja anda laksanakan. Di sini anda boleh menemui semua butiran yang perlu anda ketahui tentang endpoint tersebut.

![deploy-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-3.PNG)

Hebat! Sekarang kita mempunyai model yang dilaksanakan, kita boleh memulakan penggunaan endpoint.

### 3.2 Penggunaan endpoint

Klik pada tab "Consume". Di sini anda boleh menemui endpoint REST dan skrip Python dalam pilihan penggunaan. Luangkan masa untuk membaca kod Python tersebut.

Skrip ini boleh dijalankan terus dari mesin tempatan anda dan akan menggunakan endpoint anda.

![35](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/consumption-1.PNG)

Luangkan masa untuk memeriksa dua baris kod ini:

```python
url = 'http://98e3715f-xxxx-xxxx-xxxx-9ec22d57b796.centralus.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
```
Pembolehubah `url` adalah endpoint REST yang terdapat dalam tab consume dan pembolehubah `api_key` adalah kunci utama yang juga terdapat dalam tab consume (hanya jika anda telah mengaktifkan pengesahan). Inilah cara skrip boleh menggunakan endpoint.

18. Apabila skrip dijalankan, anda sepatutnya melihat output berikut:
    ```python
    b'"{\\"result\\": [true]}"'
    ```
Ini bermaksud bahawa ramalan kegagalan jantung untuk data yang diberikan adalah benar. Ini masuk akal kerana jika anda melihat lebih dekat pada data yang dijana secara automatik dalam skrip, semuanya adalah 0 dan palsu secara lalai. Anda boleh menukar data dengan sampel input berikut:

```python
data = {
    "data":
    [
        {
            'age': "0",
            'anaemia': "false",
            'creatinine_phosphokinase': "0",
            'diabetes': "false",
            'ejection_fraction': "0",
            'high_blood_pressure': "false",
            'platelets': "0",
            'serum_creatinine': "0",
            'serum_sodium': "0",
            'sex': "false",
            'smoking': "false",
            'time': "0",
        },
        {
            'age': "60",
            'anaemia': "false",
            'creatinine_phosphokinase': "500",
            'diabetes': "false",
            'ejection_fraction': "38",
            'high_blood_pressure': "false",
            'platelets': "260000",
            'serum_creatinine': "1.40",
            'serum_sodium': "137",
            'sex': "false",
            'smoking': "false",
            'time': "130",
        },
    ],
}
```
Skrip sepatutnya mengembalikan:
    ```python
    b'"{\\"result\\": [true, false]}"'
    ```

Tahniah! Anda baru sahaja menggunakan model yang dilaksanakan dan melatihnya di Azure ML!

> **_NOTA:_** Setelah anda selesai dengan projek ini, jangan lupa untuk memadamkan semua sumber.
## 🚀 Cabaran

Lihat dengan teliti penjelasan model dan butiran yang dihasilkan oleh AutoML untuk model-model terbaik. Cuba fahami mengapa model terbaik lebih baik daripada yang lain. Algoritma apa yang dibandingkan? Apakah perbezaan antara mereka? Mengapa yang terbaik berprestasi lebih baik dalam kes ini?

## [Kuiz selepas kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/35)

## Ulasan & Kajian Kendiri

Dalam pelajaran ini, anda telah belajar cara melatih, melaksanakan, dan menggunakan model untuk meramalkan risiko kegagalan jantung dengan cara Low code/No code di awan. Jika anda belum melakukannya, selami lebih dalam penjelasan model yang dihasilkan oleh AutoML untuk model-model terbaik dan cuba fahami mengapa model terbaik lebih baik daripada yang lain.

Anda boleh mendalami lagi AutoML Low code/No code dengan membaca [dokumentasi ini](https://docs.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

## Tugasan

[Projek Data Sains Low code/No code di Azure ML](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.