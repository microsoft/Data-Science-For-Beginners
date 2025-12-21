<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T11:48:51+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "id"
}
-->
# Bekerja dengan Data: Basis Data Relasional

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Bekerja Dengan Data: Basis Data Relasional - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Kemungkinan besar Anda pernah menggunakan spreadsheet di masa lalu untuk menyimpan informasi. Anda memiliki satu set baris dan kolom, di mana baris berisi informasi (atau data), dan kolom menjelaskan informasi tersebut (kadang disebut metadata). Basis data relasional dibangun berdasarkan prinsip inti kolom dan baris dalam tabel, memungkinkan Anda memiliki informasi yang tersebar di beberapa tabel. Ini memungkinkan Anda bekerja dengan data yang lebih kompleks, menghindari duplikasi, dan memiliki fleksibilitas dalam cara Anda mengeksplorasi data. Mari kita jelajahi konsep basis data relasional.

## [Kuis pra-ceramah](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Semuanya dimulai dengan tabel

Basis data relasional memiliki inti berupa tabel. Sama seperti pada spreadsheet, sebuah tabel adalah kumpulan kolom dan baris. Baris berisi data atau informasi yang ingin kita kerjakan, seperti nama sebuah kota atau jumlah curah hujan. Kolom menjelaskan data yang mereka simpan.

Mari kita mulai eksplorasi kita dengan membuat tabel untuk menyimpan informasi tentang kota-kota. Kita mungkin mulai dengan nama dan negara mereka. Anda bisa menyimpannya dalam tabel seperti berikut:

| Kota     | Negara       |
| -------- | ------------- |
| Tokyo    | Jepang       |
| Atlanta  | Amerika Serikat |
| Auckland | Selandia Baru |

Perhatikan nama kolom **kota**, **negara** dan **populasi** yang menjelaskan data yang disimpan, dan setiap baris memiliki informasi tentang satu kota.

## Kekurangan pendekatan tabel tunggal

Kemungkinan besar, tabel di atas tampak cukup familiar bagi Anda. Mari kita mulai menambahkan data tambahan ke basis data kita yang sedang berkembang - curah hujan tahunan (dalam milimeter). Kita akan fokus pada tahun 2018, 2019, dan 2020. Jika kita menambahkannya untuk Tokyo, mungkin akan terlihat seperti ini:

| Kota  | Negara | Tahun | Jumlah |
| ----- | ------- | ---- | ------ |
| Tokyo | Jepang   | 2020 | 1690   |
| Tokyo | Jepang   | 2019 | 1874   |
| Tokyo | Jepang   | 2018 | 1445   |

Apa yang Anda perhatikan tentang tabel kita? Anda mungkin memperhatikan kita menduplikasi nama dan negara kota berulang-ulang. Itu bisa memakan cukup banyak penyimpanan, dan sebagian besar tidak perlu memiliki beberapa salinan. Lagi pula, Tokyo hanya memiliki satu nama yang kita minati.

Oke, mari coba hal lain. Mari tambahkan kolom baru untuk setiap tahun:

| Kota     | Negara       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Jepang       | 1445 | 1874 | 1690 |
| Atlanta  | Amerika Serikat | 1779 | 1111 | 1683 |
| Auckland | Selandia Baru | 1386 | 942  | 1176 |

Meskipun ini menghindari duplikasi baris, ini menambah beberapa tantangan lain. Kita perlu memodifikasi struktur tabel kita setiap kali ada tahun baru. Selain itu, saat data kita bertambah, memiliki tahun sebagai kolom akan membuatnya lebih sulit untuk mengambil dan menghitung nilai.

Inilah mengapa kita membutuhkan beberapa tabel dan hubungan. Dengan memecah data kita, kita dapat menghindari duplikasi dan memiliki lebih banyak fleksibilitas dalam cara kita bekerja dengan data kita.

## Konsep hubungan

Mari kembali ke data kita dan tentukan bagaimana kita ingin memecahnya. Kita tahu kita ingin menyimpan nama dan negara untuk kota-kota kita, jadi ini mungkin paling baik dalam satu tabel.

| Kota     | Negara       |
| -------- | ------------- |
| Tokyo    | Jepang       |
| Atlanta  | Amerika Serikat |
| Auckland | Selandia Baru |

Tapi sebelum kita membuat tabel berikutnya, kita perlu mencari cara untuk merujuk setiap kota. Kita membutuhkan semacam pengenal, ID atau (dalam istilah teknis basis data) kunci utama. Kunci utama adalah nilai yang digunakan untuk mengidentifikasi satu baris spesifik dalam tabel. Meskipun ini bisa berdasarkan nilai itu sendiri (kita bisa menggunakan nama kota, misalnya), sebaiknya hampir selalu berupa angka atau pengenal lain. Kita tidak ingin id pernah berubah karena itu akan memutus hubungan. Anda akan menemukan dalam sebagian besar kasus kunci utama atau id akan berupa angka yang dihasilkan secara otomatis.

> ✅ Kunci utama sering disingkat sebagai PK

### cities

| city_id | Kota     | Negara       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Jepang       |
| 2       | Atlanta  | Amerika Serikat |
| 3       | Auckland | Selandia Baru |

> ✅ Anda akan melihat kami menggunakan istilah "id" dan "kunci utama" secara bergantian selama pelajaran ini. Konsep di sini berlaku untuk DataFrame, yang akan Anda jelajahi nanti. DataFrame tidak menggunakan terminologi "kunci utama", namun Anda akan melihat mereka berperilaku hampir sama.

Dengan tabel cities kita dibuat, mari simpan curah hujan. Daripada menduplikasi informasi lengkap tentang kota, kita bisa menggunakan id. Kita juga harus memastikan tabel yang baru dibuat memiliki kolom *id* juga, karena semua tabel harus memiliki id atau kunci utama.

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

Perhatikan kolom **city_id** di dalam tabel **rainfall** yang baru dibuat. Kolom ini berisi nilai yang merujuk ke ID di tabel **cities**. Dalam istilah data relasional teknis, ini disebut **foreign key**; itu adalah kunci utama dari tabel lain. Anda bisa menganggapnya sebagai referensi atau penunjuk. **city_id** 1 merujuk ke Tokyo.

> [!NOTE] 
> Foreign key sering disingkat sebagai FK

## Mengambil data

Dengan data kita dipisah menjadi dua tabel, Anda mungkin bertanya-tanya bagaimana kita mengambilnya. Jika kita menggunakan basis data relasional seperti MySQL, SQL Server, atau Oracle, kita bisa menggunakan bahasa yang disebut Structured Query Language atau SQL. SQL (kadang diucapkan sequel) adalah bahasa standar yang digunakan untuk mengambil dan memodifikasi data dalam basis data relasional.

Untuk mengambil data Anda menggunakan perintah `SELECT`. Pada intinya, Anda **memilih** kolom yang ingin Anda lihat **dari** tabel tempat mereka berada. Jika Anda ingin menampilkan hanya nama kota, Anda bisa menggunakan berikut ini:

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
> Sintaks SQL tidak peka huruf besar/kecil, artinya `select` dan `SELECT` berarti sama. Namun, tergantung pada jenis basis data yang Anda gunakan, kolom dan tabel mungkin peka huruf besar/kecil. Oleh karena itu, praktik terbaik adalah selalu memperlakukan semuanya dalam pemrograman seolah-olah peka huruf besar/kecil. Saat menulis kueri SQL, konvensi umum adalah menulis kata kunci dalam huruf besar semua.

Kueri di atas akan menampilkan semua kota. Mari bayangkan kita hanya ingin menampilkan kota di Selandia Baru. Kita perlu semacam filter. Kata kunci SQL untuk ini adalah `WHERE`, atau "di mana sesuatu benar".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Menggabungkan data

Sampai sekarang kita telah mengambil data dari satu tabel. Sekarang kita ingin menggabungkan data dari **cities** dan **rainfall**. Ini dilakukan dengan *menggabungkan* mereka bersama. Anda secara efektif membuat sambungan antara dua tabel, dan mencocokkan nilai dari kolom masing-masing tabel.

Dalam contoh kita, kita akan mencocokkan kolom **city_id** di **rainfall** dengan kolom **city_id** di **cities**. Ini akan mencocokkan nilai curah hujan dengan kota masing-masing. Jenis gabungan yang akan kita lakukan disebut *inner* join, artinya jika ada baris yang tidak cocok dengan apa pun dari tabel lain, mereka tidak akan ditampilkan. Dalam kasus kita setiap kota memiliki curah hujan, jadi semuanya akan ditampilkan.

Mari ambil curah hujan untuk tahun 2019 untuk semua kota kita.

Kita akan melakukannya dalam beberapa langkah. Langkah pertama adalah menggabungkan data dengan menunjukkan kolom untuk sambungan - **city_id** seperti yang disorot sebelumnya.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Kita telah menyorot dua kolom yang kita inginkan, dan fakta bahwa kita ingin menggabungkan tabel berdasarkan **city_id**. Sekarang kita bisa menambahkan pernyataan `WHERE` untuk memfilter hanya tahun 2019.

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

Basis data relasional berpusat pada pembagian informasi antara beberapa tabel yang kemudian digabungkan kembali untuk ditampilkan dan dianalisis. Ini memberikan tingkat fleksibilitas tinggi untuk melakukan perhitungan dan memanipulasi data. Anda telah melihat konsep inti basis data relasional, dan bagaimana melakukan join antara dua tabel.

## 🚀 Tantangan

Ada banyak basis data relasional yang tersedia di internet. Anda dapat mengeksplorasi data dengan menggunakan keterampilan yang telah Anda pelajari di atas.

## Kuis Pasca-Ceramah

## [Kuis pasca-ceramah](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Tinjauan & Studi Mandiri

Ada beberapa sumber daya yang tersedia di [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) untuk Anda melanjutkan eksplorasi konsep SQL dan basis data relasional

- [Jelaskan konsep data relasional](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Mulai Query dengan Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL adalah versi SQL)
- [Konten SQL di Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Tugas

[Menampilkan data bandara](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->