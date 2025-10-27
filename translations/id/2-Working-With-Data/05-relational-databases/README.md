<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T19:00:14+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "id"
}
-->
# Bekerja dengan Data: Basis Data Relasional

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Bekerja dengan Data: Basis Data Relasional - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Kemungkinan besar Anda pernah menggunakan spreadsheet sebelumnya untuk menyimpan informasi. Anda memiliki serangkaian baris dan kolom, di mana baris berisi informasi (atau data), dan kolom menjelaskan informasi tersebut (kadang disebut metadata). Basis data relasional dibangun berdasarkan prinsip inti ini, yaitu kolom dan baris dalam tabel, yang memungkinkan Anda memiliki informasi yang tersebar di beberapa tabel. Hal ini memungkinkan Anda bekerja dengan data yang lebih kompleks, menghindari duplikasi, dan memiliki fleksibilitas dalam mengeksplorasi data. Mari kita jelajahi konsep-konsep dalam basis data relasional.

## [Kuis sebelum kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Semuanya dimulai dengan tabel

Basis data relasional memiliki inti berupa tabel. Sama seperti spreadsheet, tabel adalah kumpulan kolom dan baris. Baris berisi data atau informasi yang ingin kita olah, seperti nama kota atau jumlah curah hujan. Kolom menjelaskan data yang disimpannya.

Mari kita mulai eksplorasi dengan membuat tabel untuk menyimpan informasi tentang kota-kota. Kita mungkin memulai dengan nama dan negara mereka. Anda dapat menyimpannya dalam tabel seperti berikut:

| Kota     | Negara        |
| -------- | ------------- |
| Tokyo    | Jepang        |
| Atlanta  | Amerika Serikat |
| Auckland | Selandia Baru |

Perhatikan nama kolom **kota**, **negara**, dan **populasi** yang menjelaskan data yang disimpan, dan setiap baris memiliki informasi tentang satu kota.

## Kelemahan pendekatan tabel tunggal

Kemungkinan besar, tabel di atas tampak cukup familiar bagi Anda. Mari kita mulai menambahkan beberapa data tambahan ke basis data kita yang sedang berkembang - curah hujan tahunan (dalam milimeter). Kita akan fokus pada tahun 2018, 2019, dan 2020. Jika kita menambahkannya untuk Tokyo, mungkin akan terlihat seperti ini:

| Kota  | Negara | Tahun | Jumlah |
| ----- | ------- | ---- | ------ |
| Tokyo | Jepang   | 2020 | 1690   |
| Tokyo | Jepang   | 2019 | 1874   |
| Tokyo | Jepang   | 2018 | 1445   |

Apa yang Anda perhatikan dari tabel kita? Anda mungkin menyadari bahwa kita menduplikasi nama dan negara kota berulang kali. Hal ini dapat memakan cukup banyak ruang penyimpanan, dan sebagian besar tidak perlu memiliki banyak salinan. Bagaimanapun, Tokyo hanya memiliki satu nama yang kita minati.

Baiklah, mari kita coba sesuatu yang lain. Mari kita tambahkan kolom baru untuk setiap tahun:

| Kota     | Negara        | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Jepang        | 1445 | 1874 | 1690 |
| Atlanta  | Amerika Serikat | 1779 | 1111 | 1683 |
| Auckland | Selandia Baru | 1386 | 942  | 1176 |

Meskipun ini menghindari duplikasi baris, hal ini menimbulkan beberapa tantangan lainnya. Kita perlu memodifikasi struktur tabel setiap kali ada tahun baru. Selain itu, saat data kita bertambah, memiliki tahun sebagai kolom akan membuatnya lebih sulit untuk mengambil dan menghitung nilai.

Inilah mengapa kita membutuhkan beberapa tabel dan hubungan. Dengan memecah data kita, kita dapat menghindari duplikasi dan memiliki lebih banyak fleksibilitas dalam cara kita bekerja dengan data.

## Konsep hubungan

Mari kita kembali ke data kita dan tentukan bagaimana kita ingin membaginya. Kita tahu bahwa kita ingin menyimpan nama dan negara untuk kota-kota kita, jadi ini mungkin paling baik disimpan dalam satu tabel.

| Kota     | Negara        |
| -------- | ------------- |
| Tokyo    | Jepang        |
| Atlanta  | Amerika Serikat |
| Auckland | Selandia Baru |

Namun sebelum kita membuat tabel berikutnya, kita perlu mencari cara untuk merujuk setiap kota. Kita membutuhkan semacam pengidentifikasi, ID atau (dalam istilah basis data teknis) kunci utama. Kunci utama adalah nilai yang digunakan untuk mengidentifikasi satu baris spesifik dalam tabel. Meskipun ini bisa didasarkan pada nilai itu sendiri (misalnya kita bisa menggunakan nama kota), sebaiknya selalu menggunakan angka atau pengidentifikasi lainnya. Kita tidak ingin ID berubah karena akan merusak hubungan. Anda akan menemukan bahwa dalam banyak kasus, kunci utama atau ID akan berupa angka yang dihasilkan secara otomatis.

> ✅ Kunci utama sering disingkat sebagai PK

### cities

| city_id | Kota     | Negara        |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Jepang        |
| 2       | Atlanta  | Amerika Serikat |
| 3       | Auckland | Selandia Baru |

> ✅ Anda akan melihat bahwa kami menggunakan istilah "id" dan "kunci utama" secara bergantian selama pelajaran ini. Konsep-konsep ini juga berlaku untuk DataFrames, yang akan Anda eksplorasi nanti. DataFrames tidak menggunakan terminologi "kunci utama", namun Anda akan melihat bahwa mereka berperilaku hampir sama.

Dengan tabel kota kita yang telah dibuat, mari kita simpan data curah hujan. Daripada menduplikasi informasi lengkap tentang kota, kita dapat menggunakan ID. Kita juga harus memastikan tabel yang baru dibuat memiliki kolom *id* juga, karena semua tabel harus memiliki ID atau kunci utama.

### rainfall

| rainfall_id | city_id | Tahun | Jumlah |
| ----------- | ------- | ---- | ------ |
| 1           | 1       | 2018 | 1445   |
| 2           | 1       | 2019 | 1874   |
| 3           | 1       | 2020 | 1690   |
| 4           | 2       | 2018 | 1779   |
| 5           | 2       | 2019 | 1111   |
| 6           | 2       | 2020 | 1683   |
| 7           | 3       | 2018 | 1386   |
| 8           | 3       | 2019 | 942    |
| 9           | 3       | 2020 | 1176   |

Perhatikan kolom **city_id** di dalam tabel **rainfall** yang baru dibuat. Kolom ini berisi nilai-nilai yang merujuk pada ID di tabel **cities**. Dalam istilah data relasional teknis, ini disebut **kunci asing**; ini adalah kunci utama dari tabel lain. Anda dapat menganggapnya sebagai referensi atau penunjuk. **city_id** 1 merujuk ke Tokyo.

> [!NOTE] 
> Kunci asing sering disingkat sebagai FK

## Mengambil data

Dengan data kita yang dipisahkan ke dalam dua tabel, Anda mungkin bertanya-tanya bagaimana cara mengambilnya. Jika kita menggunakan basis data relasional seperti MySQL, SQL Server, atau Oracle, kita dapat menggunakan bahasa yang disebut Structured Query Language atau SQL. SQL (kadang diucapkan sequel) adalah bahasa standar yang digunakan untuk mengambil dan memodifikasi data dalam basis data relasional.

Untuk mengambil data, Anda menggunakan perintah `SELECT`. Pada intinya, Anda **memilih** kolom yang ingin Anda lihat **dari** tabel tempat mereka berada. Jika Anda ingin menampilkan hanya nama-nama kota, Anda dapat menggunakan perintah berikut:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` adalah tempat Anda mencantumkan kolom, dan `FROM` adalah tempat Anda mencantumkan tabel.

> [!NOTE] 
> Sintaks SQL tidak peka huruf besar-kecil, artinya `select` dan `SELECT` memiliki arti yang sama. Namun, tergantung pada jenis basis data yang Anda gunakan, kolom dan tabel mungkin peka huruf besar-kecil. Oleh karena itu, praktik terbaik adalah selalu memperlakukan semuanya dalam pemrograman seolah-olah peka huruf besar-kecil. Saat menulis kueri SQL, konvensi umum adalah menulis kata kunci dalam huruf besar semua.

Kueri di atas akan menampilkan semua kota. Bayangkan kita hanya ingin menampilkan kota-kota di Selandia Baru. Kita membutuhkan semacam filter. Kata kunci SQL untuk ini adalah `WHERE`, atau "di mana sesuatu itu benar".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Menggabungkan data

Sampai sekarang kita telah mengambil data dari satu tabel. Sekarang kita ingin menggabungkan data dari **cities** dan **rainfall**. Ini dilakukan dengan *menggabungkan* mereka bersama. Anda pada dasarnya akan membuat sambungan antara dua tabel, dan mencocokkan nilai-nilai dari kolom dari masing-masing tabel.

Dalam contoh kita, kita akan mencocokkan kolom **city_id** di **rainfall** dengan kolom **city_id** di **cities**. Ini akan mencocokkan nilai curah hujan dengan kota masing-masing. Jenis penggabungan yang akan kita lakukan disebut *inner* join, yang berarti jika ada baris yang tidak cocok dengan apa pun dari tabel lain, mereka tidak akan ditampilkan. Dalam kasus kita, setiap kota memiliki data curah hujan, jadi semuanya akan ditampilkan.

Mari kita ambil data curah hujan untuk tahun 2019 untuk semua kota kita.

Kita akan melakukannya secara bertahap. Langkah pertama adalah menggabungkan data dengan menunjukkan kolom untuk sambungan - **city_id** seperti yang telah disorot sebelumnya.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Kami telah menyoroti dua kolom yang kami inginkan, dan fakta bahwa kami ingin menggabungkan tabel bersama dengan **city_id**. Sekarang kita dapat menambahkan pernyataan `WHERE` untuk menyaring hanya tahun 2019.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Ringkasan

Basis data relasional berpusat pada pembagian informasi di antara beberapa tabel yang kemudian digabungkan kembali untuk ditampilkan dan dianalisis. Hal ini memberikan tingkat fleksibilitas yang tinggi untuk melakukan perhitungan dan manipulasi data lainnya. Anda telah melihat konsep inti dari basis data relasional, dan bagaimana melakukan penggabungan antara dua tabel.

## 🚀 Tantangan

Ada banyak basis data relasional yang tersedia di internet. Anda dapat mengeksplorasi data dengan menggunakan keterampilan yang telah Anda pelajari di atas.

## Kuis Setelah Kuliah

## [Kuis setelah kuliah](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Tinjauan & Studi Mandiri

Ada beberapa sumber daya yang tersedia di [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) untuk melanjutkan eksplorasi Anda tentang konsep SQL dan basis data relasional

- [Deskripsikan konsep data relasional](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Memulai Query dengan Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL adalah versi SQL)
- [Konten SQL di Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Tugas

[Judul Tugas](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.