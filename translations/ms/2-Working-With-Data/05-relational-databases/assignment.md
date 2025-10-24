<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:57:08+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ms"
}
-->
# Memaparkan data lapangan terbang

Anda telah diberikan [pangkalan data](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) yang dibina menggunakan [SQLite](https://sqlite.org/index.html) yang mengandungi maklumat tentang lapangan terbang. Skema ditunjukkan di bawah. Anda akan menggunakan [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) dalam [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) untuk memaparkan maklumat tentang lapangan terbang di pelbagai bandar.

## Arahan

Untuk memulakan tugasan ini, anda perlu melakukan beberapa langkah. Anda perlu memasang beberapa alat dan memuat turun pangkalan data contoh.

### Sediakan sistem anda

Anda boleh menggunakan Visual Studio Code dan SQLite extension untuk berinteraksi dengan pangkalan data.

1. Pergi ke [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) dan ikuti arahan untuk memasang Visual Studio Code
1. Pasang [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) seperti yang diarahkan di halaman Marketplace

### Muat turun dan buka pangkalan data

Seterusnya, anda akan memuat turun dan membuka pangkalan data.

1. Muat turun [fail pangkalan data dari GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) dan simpan ke direktori
1. Buka Visual Studio Code
1. Buka pangkalan data dalam SQLite extension dengan memilih **Ctl-Shift-P** (atau **Cmd-Shift-P** pada Mac) dan taip `SQLite: Open database`
1. Pilih **Choose database from file** dan buka fail **airports.db** yang anda muat turun sebelum ini
1. Selepas membuka pangkalan data (anda tidak akan melihat kemas kini pada skrin), buat tetingkap kueri baru dengan memilih **Ctl-Shift-P** (atau **Cmd-Shift-P** pada Mac) dan taip `SQLite: New query`

Setelah dibuka, tetingkap kueri baru boleh digunakan untuk menjalankan pernyataan SQL terhadap pangkalan data. Anda boleh menggunakan arahan **Ctl-Shift-Q** (atau **Cmd-Shift-Q** pada Mac) untuk menjalankan kueri terhadap pangkalan data.

> [!NOTE] 
> Untuk maklumat lanjut tentang SQLite extension, anda boleh merujuk kepada [dokumentasi](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Skema pangkalan data

Skema pangkalan data adalah reka bentuk dan struktur jadualnya. Pangkalan data **airports** mempunyai dua jadual, `cities`, yang mengandungi senarai bandar di United Kingdom dan Ireland, dan `airports`, yang mengandungi senarai semua lapangan terbang. Oleh kerana beberapa bandar mungkin mempunyai banyak lapangan terbang, dua jadual telah dibuat untuk menyimpan maklumat tersebut. Dalam latihan ini, anda akan menggunakan gabungan untuk memaparkan maklumat bagi pelbagai bandar.

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

## Tugasan

Buat kueri untuk mengembalikan maklumat berikut:

1. semua nama bandar dalam jadual `Cities`
1. semua bandar di Ireland dalam jadual `Cities`
1. semua nama lapangan terbang dengan bandar dan negara mereka
1. semua lapangan terbang di London, United Kingdom

## Rubrik

| Cemerlang | Memadai | Perlu Penambahbaikan |
| --------- | -------- | -------------------- |

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.