<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-28T18:14:41+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "id"
}
-->
# Menampilkan data bandara

Anda telah diberikan sebuah [database](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) yang dibangun menggunakan [SQLite](https://sqlite.org/index.html) yang berisi informasi tentang bandara. Skema database ditampilkan di bawah ini. Anda akan menggunakan [ekstensi SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) di [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) untuk menampilkan informasi tentang bandara di berbagai kota.

## Instruksi

Untuk memulai tugas ini, Anda perlu melakukan beberapa langkah. Anda perlu menginstal beberapa alat dan mengunduh database contoh.

### Siapkan sistem Anda

Anda dapat menggunakan Visual Studio Code dan ekstensi SQLite untuk berinteraksi dengan database.

1. Kunjungi [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) dan ikuti instruksi untuk menginstal Visual Studio Code
1. Instal ekstensi [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) seperti yang dijelaskan di halaman Marketplace

### Unduh dan buka database

Selanjutnya, Anda akan mengunduh dan membuka database.

1. Unduh [file database dari GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) dan simpan ke direktori
1. Buka Visual Studio Code
1. Buka database di ekstensi SQLite dengan memilih **Ctl-Shift-P** (atau **Cmd-Shift-P** di Mac) dan mengetik `SQLite: Open database`
1. Pilih **Choose database from file** dan buka file **airports.db** yang telah Anda unduh sebelumnya
1. Setelah membuka database (tidak akan ada pembaruan yang terlihat di layar), buat jendela query baru dengan memilih **Ctl-Shift-P** (atau **Cmd-Shift-P** di Mac) dan mengetik `SQLite: New query`

Setelah terbuka, jendela query baru dapat digunakan untuk menjalankan pernyataan SQL terhadap database. Anda dapat menggunakan perintah **Ctl-Shift-Q** (atau **Cmd-Shift-Q** di Mac) untuk menjalankan query terhadap database.

> [!NOTE] Untuk informasi lebih lanjut tentang ekstensi SQLite, Anda dapat melihat [dokumentasi](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Skema database

Skema database adalah desain dan struktur tabelnya. Database **airports** memiliki dua tabel, `cities`, yang berisi daftar kota di Inggris dan Irlandia, dan `airports`, yang berisi daftar semua bandara. Karena beberapa kota mungkin memiliki lebih dari satu bandara, dua tabel dibuat untuk menyimpan informasi tersebut. Dalam latihan ini, Anda akan menggunakan join untuk menampilkan informasi dari berbagai kota.

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## Tugas

Buat query untuk mengembalikan informasi berikut:

1. semua nama kota dalam tabel `Cities`
1. semua kota di Irlandia dalam tabel `Cities`
1. semua nama bandara beserta kota dan negaranya
1. semua bandara di London, Inggris

## Rubrik

| Unggul     | Memadai   | Perlu Perbaikan | 
| ---------- | --------- | --------------- |

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.