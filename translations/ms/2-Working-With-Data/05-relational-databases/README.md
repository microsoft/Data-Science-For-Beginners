<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T11:52:28+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "ms"
}
-->
# Bekerja dengan Data: Pangkalan Data Relasi

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Bekerja Dengan Data: Pangkalan Data Relasi - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Kemungkinan anda pernah menggunakan hamparan sebelum ini untuk menyimpan maklumat. Anda mempunyai satu set baris dan lajur, di mana baris mengandungi maklumat (atau data), dan lajur menerangkan maklumat tersebut (kadang-kadang dipanggil metadata). Pangkalan data relasi dibina berdasarkan prinsip teras lajur dan baris dalam jadual, membolehkan anda mempunyai maklumat yang tersebar merentasi pelbagai jadual. Ini membolehkan anda bekerja dengan data yang lebih kompleks, mengelakkan penduaan, dan mempunyai fleksibiliti dalam cara anda meneroka data. Mari kita terokai konsep pangkalan data relasi.

## [Kuiz pra-ceramah](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Semuanya bermula dengan jadual

Pangkalan data relasi mempunyai jadual sebagai terasnya. Sama seperti hamparan, jadual adalah koleksi lajur dan baris. Baris mengandungi data atau maklumat yang ingin kita kerjakan, seperti nama sebuah bandar atau jumlah hujan. Lajur menerangkan data yang mereka simpan.

Mari kita mulakan penerokaan dengan memulakan jadual untuk menyimpan maklumat tentang bandar. Kita mungkin mulakan dengan nama dan negara mereka. Anda boleh menyimpan ini dalam jadual seperti berikut:

| Bandar   | Negara       |
| -------- | ------------- |
| Tokyo    | Jepun        |
| Atlanta  | Amerika Syarikat |
| Auckland | New Zealand  |

Perhatikan nama lajur **bandar**, **negara** dan **populasi** menerangkan data yang disimpan, dan setiap baris mempunyai maklumat tentang satu bandar.

## Kekurangan pendekatan jadual tunggal

Kemungkinan jadual di atas kelihatan agak biasa bagi anda. Mari kita tambah beberapa data tambahan ke pangkalan data yang sedang berkembang - hujan tahunan (dalam milimeter). Kita akan fokus pada tahun 2018, 2019 dan 2020. Jika kita menambahkannya untuk Tokyo, ia mungkin kelihatan seperti ini:

| Bandar | Negara | Tahun | Jumlah |
| ------ | ------ | ----- | ------ |
| Tokyo  | Jepun  | 2020  | 1690   |
| Tokyo  | Jepun  | 2019  | 1874   |
| Tokyo  | Jepun  | 2018  | 1445   |

Apa yang anda perhatikan tentang jadual kita? Anda mungkin perasan kita menggandakan nama dan negara bandar berulang kali. Itu boleh mengambil banyak ruang simpanan, dan kebanyakannya tidak perlu mempunyai salinan berganda. Lagipun, Tokyo hanya mempunyai satu nama yang kita minati.

Baiklah, mari cuba sesuatu yang lain. Mari tambah lajur baru untuk setiap tahun:

| Bandar   | Negara       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Jepun        | 1445 | 1874 | 1690 |
| Atlanta  | Amerika Syarikat | 1779 | 1111 | 1683 |
| Auckland | New Zealand  | 1386 | 942  | 1176 |

Walaupun ini mengelakkan penduaan baris, ia menambah beberapa cabaran lain. Kita perlu mengubah struktur jadual setiap kali ada tahun baru. Selain itu, apabila data kita berkembang, menjadikan tahun sebagai lajur akan menyukarkan untuk mendapatkan dan mengira nilai.

Inilah sebabnya kita memerlukan pelbagai jadual dan hubungan. Dengan memecahkan data kita, kita boleh mengelakkan penduaan dan mempunyai lebih fleksibiliti dalam cara kita bekerja dengan data.

## Konsep hubungan

Mari kembali ke data kita dan tentukan bagaimana kita mahu memecahkan perkara. Kita tahu kita mahu menyimpan nama dan negara untuk bandar kita, jadi ini mungkin paling sesuai dalam satu jadual.

| Bandar   | Negara       |
| -------- | ------------- |
| Tokyo    | Jepun        |
| Atlanta  | Amerika Syarikat |
| Auckland | New Zealand  |

Tetapi sebelum kita buat jadual seterusnya, kita perlu tentukan bagaimana untuk merujuk setiap bandar. Kita memerlukan satu bentuk pengecam, ID atau (dalam istilah teknikal pangkalan data) kunci primer. Kunci primer adalah nilai yang digunakan untuk mengenal pasti satu baris tertentu dalam jadual. Walaupun ini boleh berdasarkan nilai itu sendiri (kita boleh gunakan nama bandar, contohnya), ia hampir selalu harus nombor atau pengecam lain. Kita tidak mahu id itu berubah kerana ia akan memutuskan hubungan. Dalam kebanyakan kes, kunci primer atau id akan menjadi nombor yang dijana secara automatik.

> ✅ Kunci primer sering disingkat sebagai PK

### bandar

| city_id | Bandar   | Negara       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Jepun        |
| 2       | Atlanta  | Amerika Syarikat |
| 3       | Auckland | New Zealand  |

> ✅ Anda akan perasan kami menggunakan istilah "id" dan "kunci primer" secara bergantian dalam pelajaran ini. Konsep di sini juga terpakai kepada DataFrame, yang akan anda terokai kemudian. DataFrame tidak menggunakan istilah "kunci primer", namun anda akan perasan ia berkelakuan hampir sama.

Dengan jadual bandar kita siap, mari simpan data hujan. Daripada menggandakan maklumat penuh tentang bandar, kita boleh gunakan id. Kita juga harus pastikan jadual baru yang dibuat mempunyai lajur *id* juga, kerana semua jadual harus mempunyai id atau kunci primer.

### hujan

| rainfall_id | city_id | Tahun | Jumlah |
| ----------- | ------- | ----- | ------ |
| 1           | 1       | 2018  | 1445   |
| 2           | 1       | 2019  | 1874   |
| 3           | 1       | 2020  | 1690   |
| 4           | 2       | 2018  | 1779   |
| 5           | 2       | 2019  | 1111   |
| 6           | 2       | 2020  | 1683   |
| 7           | 3       | 2018  | 1386   |
| 8           | 3       | 2019  | 942    |
| 9           | 3       | 2020  | 1176   |

Perhatikan lajur **city_id** dalam jadual **hujan** yang baru dibuat. Lajur ini mengandungi nilai yang merujuk kepada ID dalam jadual **bandar**. Dalam istilah data relasi teknikal, ini dipanggil **kunci asing**; ia adalah kunci primer dari jadual lain. Anda boleh anggap ia sebagai rujukan atau penunjuk. **city_id** 1 merujuk kepada Tokyo.

> [!NOTE] 
> Kunci asing sering disingkat sebagai FK

## Mendapatkan data

Dengan data kita dipisahkan ke dalam dua jadual, anda mungkin tertanya-tanya bagaimana kita mendapatkannya. Jika kita menggunakan pangkalan data relasi seperti MySQL, SQL Server atau Oracle, kita boleh menggunakan bahasa yang dipanggil Structured Query Language atau SQL. SQL (kadang-kadang disebut sequel) adalah bahasa standard yang digunakan untuk mendapatkan dan mengubah data dalam pangkalan data relasi.

Untuk mendapatkan data anda menggunakan arahan `SELECT`. Pada asasnya, anda **memilih** lajur yang anda mahu lihat **dari** jadual yang mengandungi mereka. Jika anda mahu memaparkan hanya nama bandar, anda boleh gunakan yang berikut:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` adalah tempat anda senaraikan lajur, dan `FROM` adalah tempat anda senaraikan jadual.

> [!NOTE] 
> Sintaks SQL tidak sensitif huruf besar kecil, bermakna `select` dan `SELECT` bermaksud sama. Namun, bergantung pada jenis pangkalan data yang anda gunakan, lajur dan jadual mungkin sensitif huruf besar kecil. Oleh itu, amalan terbaik adalah sentiasa anggap semua dalam pengaturcaraan adalah sensitif huruf besar kecil. Apabila menulis pertanyaan SQL, konvensyen biasa adalah meletakkan kata kunci dalam huruf besar semua.

Pertanyaan di atas akan memaparkan semua bandar. Mari bayangkan kita hanya mahu memaparkan bandar di New Zealand. Kita perlukan satu bentuk penapis. Kata kunci SQL untuk ini adalah `WHERE`, atau "di mana sesuatu adalah benar".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Menyambung data

Sehingga kini kita telah mendapatkan data dari satu jadual sahaja. Kini kita mahu gabungkan data dari kedua-dua **bandar** dan **hujan**. Ini dilakukan dengan *menyambung* mereka bersama. Anda secara efektif akan mencipta sambungan antara dua jadual, dan padankan nilai dari lajur setiap jadual.

Dalam contoh kita, kita akan padankan lajur **city_id** dalam **hujan** dengan lajur **city_id** dalam **bandar**. Ini akan padankan nilai hujan dengan bandar masing-masing. Jenis sambungan yang akan kita lakukan dipanggil *inner* join, bermakna jika ada baris yang tidak sepadan dengan apa-apa dari jadual lain, ia tidak akan dipaparkan. Dalam kes kita, setiap bandar mempunyai data hujan, jadi semuanya akan dipaparkan.

Mari kita dapatkan data hujan untuk tahun 2019 untuk semua bandar kita.

Kita akan lakukan ini secara berperingkat. Langkah pertama adalah menyambung data dengan menunjukkan lajur untuk sambungan - **city_id** seperti yang diserlahkan sebelum ini.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Kita telah menyerlahkan dua lajur yang kita mahu, dan fakta kita mahu sambungkan jadual melalui **city_id**. Kini kita boleh tambah pernyataan `WHERE` untuk tapis hanya tahun 2019.

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

Pangkalan data relasi berpusat pada pembahagian maklumat antara pelbagai jadual yang kemudian disatukan semula untuk paparan dan analisis. Ini memberikan tahap fleksibiliti yang tinggi untuk melakukan pengiraan dan manipulasi data. Anda telah melihat konsep teras pangkalan data relasi, dan cara melakukan sambungan antara dua jadual.

## 🚀 Cabaran

Terdapat banyak pangkalan data relasi yang tersedia di internet. Anda boleh terokai data dengan menggunakan kemahiran yang telah anda pelajari di atas.

## Kuiz Pasca-Ceramah

## [Kuiz pasca-ceramah](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Ulasan & Belajar Sendiri

Terdapat beberapa sumber yang tersedia di [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) untuk anda teruskan penerokaan konsep SQL dan pangkalan data relasi

- [Terangkan konsep data relasi](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Mulakan Pertanyaan dengan Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL adalah versi SQL)
- [Kandungan SQL di Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Tugasan

[Memaparkan data lapangan terbang](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->