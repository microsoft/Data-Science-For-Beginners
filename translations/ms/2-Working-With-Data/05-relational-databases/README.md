<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-04T20:45:07+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "ms"
}
-->
# Bekerja dengan Data: Pangkalan Data Relasi

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Bekerja dengan Data: Pangkalan Data Relasi - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Kemungkinan besar anda pernah menggunakan hamparan elektronik untuk menyimpan maklumat. Anda mempunyai set baris dan lajur, di mana baris mengandungi maklumat (atau data), dan lajur menerangkan maklumat tersebut (kadangkala dipanggil metadata). Pangkalan data relasi dibina berdasarkan prinsip teras ini, iaitu lajur dan baris dalam jadual, membolehkan anda menyebarkan maklumat ke beberapa jadual. Ini membolehkan anda bekerja dengan data yang lebih kompleks, mengelakkan penduaan, dan mempunyai fleksibiliti dalam cara anda meneroka data. Mari kita terokai konsep pangkalan data relasi.

## [Kuiz pra-kuliah](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Semuanya bermula dengan jadual

Pangkalan data relasi mempunyai jadual sebagai terasnya. Sama seperti hamparan elektronik, jadual adalah koleksi lajur dan baris. Baris mengandungi data atau maklumat yang ingin kita kerjakan, seperti nama bandar atau jumlah hujan. Lajur menerangkan data yang disimpan.

Mari kita mulakan penerokaan dengan membuat jadual untuk menyimpan maklumat tentang bandar. Kita mungkin bermula dengan nama dan negara mereka. Anda boleh menyimpan ini dalam jadual seperti berikut:

| Bandar   | Negara         |
| -------- | ------------- |
| Tokyo    | Jepun          |
| Atlanta  | Amerika Syarikat |
| Auckland | New Zealand    |

Perhatikan nama lajur **bandar**, **negara**, dan **populasi** yang menerangkan data yang disimpan, dan setiap baris mempunyai maklumat tentang satu bandar.

## Kekurangan pendekatan jadual tunggal

Kemungkinan besar, jadual di atas kelihatan agak biasa bagi anda. Mari kita tambahkan beberapa data tambahan ke pangkalan data kita yang sedang berkembang - hujan tahunan (dalam milimeter). Kita akan fokus pada tahun 2018, 2019, dan 2020. Jika kita menambahkannya untuk Tokyo, ia mungkin kelihatan seperti ini:

| Bandar | Negara | Tahun | Jumlah |
| ----- | ------- | ---- | ------ |
| Tokyo | Jepun   | 2020 | 1690   |
| Tokyo | Jepun   | 2019 | 1874   |
| Tokyo | Jepun   | 2018 | 1445   |

Apa yang anda perhatikan tentang jadual kita? Anda mungkin perasan kita menggandakan nama dan negara bandar berulang kali. Ini boleh mengambil ruang penyimpanan yang agak banyak, dan sebahagian besarnya tidak perlu untuk mempunyai salinan berganda. Lagipun, Tokyo hanya mempunyai satu nama yang kita minati.

Baiklah, mari kita cuba sesuatu yang lain. Mari kita tambahkan lajur baru untuk setiap tahun:

| Bandar   | Negara         | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Jepun          | 1445 | 1874 | 1690 |
| Atlanta  | Amerika Syarikat | 1779 | 1111 | 1683 |
| Auckland | New Zealand    | 1386 | 942  | 1176 |

Walaupun ini mengelakkan penggandaan baris, ia menambah beberapa cabaran lain. Kita perlu mengubah struktur jadual kita setiap kali ada tahun baru. Selain itu, apabila data kita berkembang, mempunyai tahun sebagai lajur akan menjadikannya lebih sukar untuk mendapatkan dan mengira nilai.

Inilah sebabnya kita memerlukan beberapa jadual dan hubungan. Dengan memecahkan data kita, kita boleh mengelakkan penggandaan dan mempunyai lebih banyak fleksibiliti dalam cara kita bekerja dengan data kita.

## Konsep hubungan

Mari kita kembali kepada data kita dan tentukan bagaimana kita mahu memecahkannya. Kita tahu kita mahu menyimpan nama dan negara untuk bandar kita, jadi ini mungkin paling sesuai dalam satu jadual.

| Bandar   | Negara         |
| -------- | ------------- |
| Tokyo    | Jepun          |
| Atlanta  | Amerika Syarikat |
| Auckland | New Zealand    |

Tetapi sebelum kita membuat jadual seterusnya, kita perlu memikirkan cara untuk merujuk setiap bandar. Kita memerlukan beberapa bentuk pengenal pasti, ID atau (dalam istilah pangkalan data teknikal) kunci utama. Kunci utama adalah nilai yang digunakan untuk mengenal pasti satu baris tertentu dalam jadual. Walaupun ini boleh berdasarkan nilai itu sendiri (kita boleh menggunakan nama bandar, sebagai contoh), ia hampir selalu harus menjadi nombor atau pengenal pasti lain. Kita tidak mahu ID itu berubah kerana ia akan merosakkan hubungan. Anda akan dapati dalam kebanyakan kes kunci utama atau ID akan menjadi nombor yang dijana secara automatik.

> ✅ Kunci utama sering disingkatkan sebagai PK

### bandar

| bandar_id | Bandar   | Negara         |
| --------- | -------- | ------------- |
| 1         | Tokyo    | Jepun          |
| 2         | Atlanta  | Amerika Syarikat |
| 3         | Auckland | New Zealand    |

> ✅ Anda akan perasan kita menggunakan istilah "id" dan "kunci utama" secara bergantian semasa pelajaran ini. Konsep di sini juga terpakai kepada DataFrames, yang akan anda terokai kemudian. DataFrames tidak menggunakan istilah "kunci utama", namun anda akan perasan ia berfungsi dengan cara yang sama.

Dengan jadual bandar kita dibuat, mari kita simpan data hujan. Daripada menggandakan maklumat penuh tentang bandar, kita boleh menggunakan ID. Kita juga harus memastikan jadual yang baru dibuat mempunyai lajur *id* juga, kerana semua jadual harus mempunyai ID atau kunci utama.

### hujan

| hujan_id | bandar_id | Tahun | Jumlah |
| -------- | --------- | ---- | ------ |
| 1        | 1         | 2018 | 1445   |
| 2        | 1         | 2019 | 1874   |
| 3        | 1         | 2020 | 1690   |
| 4        | 2         | 2018 | 1779   |
| 5        | 2         | 2019 | 1111   |
| 6        | 2         | 2020 | 1683   |
| 7        | 3         | 2018 | 1386   |
| 8        | 3         | 2019 | 942    |
| 9        | 3         | 2020 | 1176   |

Perhatikan lajur **bandar_id** dalam jadual **hujan** yang baru dibuat. Lajur ini mengandungi nilai yang merujuk kepada ID dalam jadual **bandar**. Dalam istilah data relasi teknikal, ini dipanggil **kunci asing**; ia adalah kunci utama dari jadual lain. Anda boleh menganggapnya sebagai rujukan atau penunjuk. **bandar_id** 1 merujuk kepada Tokyo.

> [!NOTE] Kunci asing sering disingkatkan sebagai FK

## Mendapatkan data

Dengan data kita dipisahkan ke dalam dua jadual, anda mungkin tertanya-tanya bagaimana kita mendapatkannya semula. Jika kita menggunakan pangkalan data relasi seperti MySQL, SQL Server atau Oracle, kita boleh menggunakan bahasa yang dipanggil Structured Query Language atau SQL. SQL (kadangkala disebut sebagai sequel) adalah bahasa standard yang digunakan untuk mendapatkan dan mengubah data dalam pangkalan data relasi.

Untuk mendapatkan data, anda menggunakan arahan `SELECT`. Pada dasarnya, anda **memilih** lajur yang ingin anda lihat **dari** jadual yang mengandungi mereka. Jika anda ingin memaparkan hanya nama bandar, anda boleh menggunakan yang berikut:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` adalah tempat anda menyenaraikan lajur, dan `FROM` adalah tempat anda menyenaraikan jadual.

> [NOTE] Sintaks SQL tidak sensitif huruf besar, bermakna `select` dan `SELECT` adalah sama. Walau bagaimanapun, bergantung pada jenis pangkalan data yang anda gunakan, lajur dan jadual mungkin sensitif huruf besar. Oleh itu, adalah amalan terbaik untuk sentiasa menganggap segala-galanya dalam pengaturcaraan seperti ia sensitif huruf besar. Apabila menulis pertanyaan SQL, konvensyen biasa adalah meletakkan kata kunci dalam huruf besar.

Pertanyaan di atas akan memaparkan semua bandar. Bayangkan kita hanya mahu memaparkan bandar di New Zealand. Kita memerlukan beberapa bentuk penapis. Kata kunci SQL untuk ini adalah `WHERE`, atau "di mana sesuatu adalah benar".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Menggabungkan data

Sehingga kini kita telah mendapatkan data dari satu jadual. Sekarang kita mahu menggabungkan data dari kedua-dua **bandar** dan **hujan**. Ini dilakukan dengan *menggabungkan* mereka bersama. Anda akan secara efektif mencipta sambungan antara dua jadual, dan memadankan nilai dari lajur dari setiap jadual.

Dalam contoh kita, kita akan memadankan lajur **bandar_id** dalam **hujan** dengan lajur **bandar_id** dalam **bandar**. Ini akan memadankan nilai hujan dengan bandar masing-masing. Jenis gabungan yang akan kita lakukan dipanggil *inner* join, bermakna jika ada baris yang tidak sepadan dengan apa-apa dari jadual lain, ia tidak akan dipaparkan. Dalam kes kita, setiap bandar mempunyai data hujan, jadi semuanya akan dipaparkan.

Mari kita dapatkan data hujan untuk tahun 2019 untuk semua bandar kita.

Kita akan melakukannya secara berperingkat. Langkah pertama adalah menggabungkan data bersama dengan menunjukkan lajur untuk sambungan - **bandar_id** seperti yang disorot sebelum ini.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Kita telah menyorot dua lajur yang kita mahu, dan fakta bahawa kita mahu menggabungkan jadual bersama dengan **bandar_id**. Sekarang kita boleh menambah pernyataan `WHERE` untuk menapis hanya tahun 2019.

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

Pangkalan data relasi berpusat pada membahagikan maklumat antara beberapa jadual yang kemudian digabungkan semula untuk paparan dan analisis. Ini memberikan tahap fleksibiliti yang tinggi untuk melakukan pengiraan dan memanipulasi data. Anda telah melihat konsep teras pangkalan data relasi, dan bagaimana untuk melakukan gabungan antara dua jadual.

## 🚀 Cabaran

Terdapat banyak pangkalan data relasi yang tersedia di internet. Anda boleh meneroka data dengan menggunakan kemahiran yang telah anda pelajari di atas.

## Kuiz Pasca-Kuliah

## [Kuiz pasca-kuliah](https://ff-quizzes.netlify.app/en/ds/)

## Kajian & Pembelajaran Kendiri

Terdapat beberapa sumber yang tersedia di [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) untuk anda meneruskan penerokaan konsep SQL dan pangkalan data relasi

- [Terangkan konsep data relasi](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Mulakan Pertanyaan dengan Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL adalah versi SQL)
- [Kandungan SQL di Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Tugasan

[Judul Tugasan](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.