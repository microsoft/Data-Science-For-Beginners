<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-28T18:14:54+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ms"
}
-->
# Memaparkan data lapangan terbang

Anda telah diberikan [pangkalan data](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) yang dibina menggunakan [SQLite](https://sqlite.org/index.html) yang mengandungi maklumat tentang lapangan terbang. Skema pangkalan data ditunjukkan di bawah. Anda akan menggunakan [sambungan SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) dalam [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) untuk memaparkan maklumat tentang lapangan terbang di pelbagai bandar.

## Arahan

Untuk memulakan tugasan ini, anda perlu melakukan beberapa langkah. Anda perlu memasang beberapa alat dan memuat turun pangkalan data contoh.

### Sediakan sistem anda

Anda boleh menggunakan Visual Studio Code dan sambungan SQLite untuk berinteraksi dengan pangkalan data.

1. Pergi ke [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) dan ikuti arahan untuk memasang Visual Studio Code
1. Pasang sambungan [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) seperti yang diarahkan pada halaman Marketplace

### Muat turun dan buka pangkalan data

Seterusnya, anda akan memuat turun dan membuka pangkalan data.

1. Muat turun [fail pangkalan data dari GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) dan simpan ke dalam direktori
1. Buka Visual Studio Code
1. Buka pangkalan data dalam sambungan SQLite dengan memilih **Ctl-Shift-P** (atau **Cmd-Shift-P** pada Mac) dan taip `SQLite: Open database`
1. Pilih **Choose database from file** dan buka fail **airports.db** yang anda muat turun sebelum ini
1. Selepas membuka pangkalan data (anda tidak akan melihat sebarang kemas kini pada skrin), buat tetingkap pertanyaan baru dengan memilih **Ctl-Shift-P** (atau **Cmd-Shift-P** pada Mac) dan taip `SQLite: New query`

Setelah dibuka, tetingkap pertanyaan baru boleh digunakan untuk menjalankan pernyataan SQL terhadap pangkalan data. Anda boleh menggunakan arahan **Ctl-Shift-Q** (atau **Cmd-Shift-Q** pada Mac) untuk menjalankan pertanyaan terhadap pangkalan data.

> [!NOTE] Untuk maklumat lanjut tentang sambungan SQLite, anda boleh merujuk kepada [dokumentasi](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Skema pangkalan data

Skema pangkalan data adalah reka bentuk dan struktur jadualnya. Pangkalan data **airports** mempunyai dua jadual, `cities`, yang mengandungi senarai bandar di United Kingdom dan Ireland, dan `airports`, yang mengandungi senarai semua lapangan terbang. Oleh kerana beberapa bandar mungkin mempunyai lebih daripada satu lapangan terbang, dua jadual telah dibuat untuk menyimpan maklumat ini. Dalam latihan ini, anda akan menggunakan gabungan (joins) untuk memaparkan maklumat bagi pelbagai bandar.

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (teks)      |
| country (teks)   |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (teks)                      |
| code (teks)                      |
| city_id (FK kepada id dalam **Cities**) |

## Tugasan

Cipta pertanyaan untuk mendapatkan maklumat berikut:

1. semua nama bandar dalam jadual `Cities`
1. semua bandar di Ireland dalam jadual `Cities`
1. semua nama lapangan terbang beserta bandar dan negara mereka
1. semua lapangan terbang di London, United Kingdom

## Rubrik

| Cemerlang | Memadai | Perlu Penambahbaikan |
| --------- | -------- | -------------------- |

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.