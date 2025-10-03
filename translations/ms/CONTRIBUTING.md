<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:22:06+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ms"
}
-->
# Menyumbang kepada Data Science untuk Pemula

Terima kasih atas minat anda untuk menyumbang kepada kurikulum Data Science untuk Pemula! Kami mengalu-alukan sumbangan daripada komuniti.

## Kandungan

- [Kod Etika](../..)
- [Bagaimana Saya Boleh Menyumbang?](../..)
- [Memulakan](../..)
- [Panduan Sumbangan](../..)
- [Proses Permintaan Tarik](../..)
- [Panduan Gaya](../..)
- [Perjanjian Lesen Penyumbang](../..)

## Kod Etika

Projek ini telah mengguna pakai [Kod Etika Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Untuk maklumat lanjut, lihat [Soalan Lazim Kod Etika](https://opensource.microsoft.com/codeofconduct/faq/)  
atau hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## Bagaimana Saya Boleh Menyumbang?

### Melaporkan Pepijat

Sebelum membuat laporan pepijat, sila semak isu yang sedia ada untuk mengelakkan pendua. Apabila anda membuat laporan pepijat, sertakan sebanyak mungkin butiran:

- **Gunakan tajuk yang jelas dan deskriptif**
- **Terangkan langkah-langkah tepat untuk menghasilkan masalah**
- **Sediakan contoh spesifik** (petikan kod, tangkapan skrin)
- **Terangkan tingkah laku yang anda perhatikan dan apa yang anda jangkakan**
- **Sertakan butiran persekitaran anda** (OS, versi Python, pelayar)

### Mencadangkan Penambahbaikan

Cadangan penambahbaikan amat dialu-alukan! Apabila mencadangkan penambahbaikan:

- **Gunakan tajuk yang jelas dan deskriptif**
- **Sediakan penerangan terperinci tentang penambahbaikan yang dicadangkan**
- **Jelaskan mengapa penambahbaikan ini berguna**
- **Senaraikan ciri serupa dalam projek lain, jika berkenaan**

### Menyumbang kepada Dokumentasi

Penambahbaikan dokumentasi sentiasa dihargai:

- **Betulkan kesalahan ejaan dan tatabahasa**
- **Perbaiki kejelasan penerangan**
- **Tambah dokumentasi yang hilang**
- **Kemas kini maklumat yang sudah lapuk**
- **Tambah contoh atau kes penggunaan**

### Menyumbang Kod

Kami mengalu-alukan sumbangan kod termasuk:

- **Pelajaran atau latihan baru**
- **Pembetulan pepijat**
- **Penambahbaikan kepada buku nota sedia ada**
- **Dataset atau contoh baru**
- **Penambahbaikan aplikasi kuiz**

## Memulakan

### Prasyarat

Sebelum menyumbang, pastikan anda mempunyai:

1. Akaun GitHub
2. Git dipasang pada sistem anda
3. Python 3.7+ dan Jupyter dipasang
4. Node.js dan npm (untuk sumbangan aplikasi kuiz)
5. Kefahaman tentang struktur kurikulum

Lihat [INSTALLATION.md](INSTALLATION.md) untuk arahan persediaan terperinci.

### Fork dan Clone

1. **Fork repositori** di GitHub  
2. **Clone fork anda** secara tempatan:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Tambah remote upstream**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Buat Cawangan

Buat cawangan baru untuk kerja anda:  
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Konvensyen penamaan cawangan:  
- `feature/` - Ciri atau pelajaran baru  
- `fix/` - Pembetulan pepijat  
- `docs/` - Perubahan dokumentasi  
- `refactor/` - Penstrukturan semula kod  

## Panduan Sumbangan

### Untuk Kandungan Pelajaran

Apabila menyumbang pelajaran atau mengubah suai yang sedia ada:

1. **Ikuti struktur sedia ada**:  
   - README.md dengan kandungan pelajaran  
   - Buku nota Jupyter dengan latihan  
   - Tugasan (jika berkenaan)  
   - Pautan kepada kuiz pra dan pasca  

2. **Sertakan elemen-elemen ini**:  
   - Objektif pembelajaran yang jelas  
   - Penerangan langkah demi langkah  
   - Contoh kod dengan komen  
   - Latihan untuk latihan  
   - Pautan kepada sumber tambahan  

3. **Pastikan kebolehaksesan**:  
   - Gunakan bahasa yang jelas dan mudah  
   - Sediakan teks alt untuk imej  
   - Sertakan komen kod  
   - Pertimbangkan gaya pembelajaran yang berbeza  

### Untuk Buku Nota Jupyter

1. **Kosongkan semua output** sebelum membuat komit:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Sertakan sel markdown** dengan penerangan  

3. **Gunakan format yang konsisten**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Uji buku nota anda** sepenuhnya sebelum menghantar  

### Untuk Kod Python

Ikuti panduan gaya [PEP 8](https://www.python.org/dev/peps/pep-0008/):  
```python
# Good practices
import pandas as pd

def calculate_mean(data):
    """Calculate the mean of a dataset.
    
    Args:
        data (list): List of numerical values
        
    Returns:
        float: Mean of the dataset
    """
    return sum(data) / len(data)
```
  

### Untuk Sumbangan Aplikasi Kuiz

Apabila mengubah suai aplikasi kuiz:

1. **Uji secara tempatan**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Jalankan linter**:  
   ```bash
   npm run lint
   ```
  
3. **Bina dengan berjaya**:  
   ```bash
   npm run build
   ```
  
4. **Ikuti panduan gaya Vue.js** dan corak sedia ada  

### Untuk Terjemahan

Apabila menambah atau mengemas kini terjemahan:

1. Ikuti struktur dalam folder `translations/`  
2. Gunakan kod bahasa sebagai nama folder (contoh: `fr` untuk Bahasa Perancis)  
3. Kekalkan struktur fail yang sama seperti versi Bahasa Inggeris  
4. Kemas kini pautan kuiz untuk menyertakan parameter bahasa: `?loc=fr`  
5. Uji semua pautan dan format  

## Proses Permintaan Tarik

### Sebelum Menghantar

1. **Kemas kini cawangan anda** dengan perubahan terkini:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Uji perubahan anda**:  
   - Jalankan semua buku nota yang diubah suai  
   - Uji aplikasi kuiz jika diubah suai  
   - Pastikan semua pautan berfungsi  
   - Periksa kesalahan ejaan dan tatabahasa  

3. **Komit perubahan anda**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Tulis mesej komit yang jelas:  
   - Gunakan masa kini ("Tambah ciri" bukan "Ditambah ciri")  
   - Gunakan mood imperatif ("Gerakkan kursor ke..." bukan "Menggerakkan kursor ke...")  
   - Hadkan baris pertama kepada 72 aksara  
   - Rujuk isu dan permintaan tarik apabila relevan  

4. **Push ke fork anda**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Membuat Permintaan Tarik

1. Pergi ke [repositori](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Klik "Pull requests" → "New pull request"  
3. Klik "compare across forks"  
4. Pilih fork dan cawangan anda  
5. Klik "Create pull request"  

### Format Tajuk PR

Gunakan tajuk yang jelas dan deskriptif mengikut format ini:  
```
[Component] Brief description
```
  
Contoh:  
- `[Lesson 7] Betulkan ralat import buku nota Python`  
- `[Quiz App] Tambah terjemahan Bahasa Jerman`  
- `[Docs] Kemas kini README dengan prasyarat baru`  
- `[Fix] Betulkan laluan data dalam pelajaran visualisasi`  

### Penerangan PR

Sertakan dalam penerangan PR anda:

- **Apa**: Apakah perubahan yang anda buat?  
- **Kenapa**: Mengapa perubahan ini diperlukan?  
- **Bagaimana**: Bagaimana anda melaksanakan perubahan?  
- **Pengujian**: Bagaimana anda menguji perubahan?  
- **Tangkapan Skrin**: Sertakan tangkapan skrin untuk perubahan visual  
- **Isu Berkaitan**: Pautkan kepada isu berkaitan (contoh: "Fixes #123")  

### Proses Semakan

1. **Semakan automatik** akan dijalankan pada PR anda  
2. **Penyelenggara akan menyemak** sumbangan anda  
3. **Tanggapi maklum balas** dengan membuat komit tambahan  
4. Setelah diluluskan, **penyelenggara akan menggabungkan** PR anda  

### Selepas PR Anda Digabungkan

1. Padamkan cawangan anda:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Kemas kini fork anda:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Panduan Gaya

### Markdown

- Gunakan tahap tajuk yang konsisten  
- Sertakan baris kosong antara bahagian  
- Gunakan blok kod dengan penentu bahasa:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Tambah teks alt pada imej: `![Alt text](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.ms.png)`  
- Kekalkan panjang baris yang munasabah (sekitar 80-100 aksara)  

### Python

- Ikuti panduan gaya PEP 8  
- Gunakan nama pemboleh ubah yang bermakna  
- Tambah docstring pada fungsi  
- Sertakan petunjuk jenis jika sesuai:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Ikuti panduan gaya Vue.js 2  
- Gunakan konfigurasi ESLint yang disediakan  
- Tulis komponen modular dan boleh digunakan semula  
- Tambah komen untuk logik yang kompleks  

### Pengorganisasian Fail

- Simpan fail yang berkaitan bersama  
- Gunakan nama fail yang deskriptif  
- Ikuti struktur direktori sedia ada  
- Jangan komit fail yang tidak diperlukan (.DS_Store, .pyc, node_modules, dll.)  

## Perjanjian Lesen Penyumbang

Projek ini mengalu-alukan sumbangan dan cadangan. Kebanyakan sumbangan memerlukan anda  
bersetuju dengan Perjanjian Lesen Penyumbang (CLA) yang menyatakan bahawa anda mempunyai hak untuk,  
dan sebenarnya memberikan kami hak untuk menggunakan sumbangan anda. Untuk butiran, lawati  
https://cla.microsoft.com.  

Apabila anda menghantar permintaan tarik, bot CLA akan secara automatik menentukan sama ada anda perlu  
memberikan CLA dan menghiasi PR dengan sewajarnya (contoh: label, komen). Ikuti sahaja  
arahan yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali untuk semua repositori yang menggunakan CLA kami.  

## Ada Soalan?

- Semak [Saluran Discord #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Sertai komuniti [Discord kami](https://aka.ms/ds4beginners/discord)  
- Semak isu [sedia ada](https://github.com/microsoft/Data-Science-For-Beginners/issues) dan [permintaan tarik](https://github.com/microsoft/Data-Science-For-Beginners/pulls)  

## Terima Kasih!

Sumbangan anda menjadikan kurikulum ini lebih baik untuk semua orang. Terima kasih kerana meluangkan masa untuk menyumbang!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.