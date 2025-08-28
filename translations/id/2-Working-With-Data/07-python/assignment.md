<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-28T18:11:50+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "id"
}
-->
# Tugas Pemrosesan Data dalam Python

Dalam tugas ini, kami meminta Anda untuk mengembangkan lebih lanjut kode yang telah kita mulai dalam tantangan sebelumnya. Tugas ini terdiri dari dua bagian:

## Pemodelan Penyebaran COVID-19

 - [ ] Plot grafik *R* untuk 5-6 negara berbeda dalam satu grafik untuk perbandingan, atau menggunakan beberapa grafik berdampingan.
 - [ ] Lihat bagaimana jumlah kematian dan kesembuhan berkorelasi dengan jumlah kasus terinfeksi.
 - [ ] Cari tahu berapa lama rata-rata penyakit berlangsung dengan mengamati korelasi visual antara tingkat infeksi dan tingkat kematian serta mencari beberapa anomali. Anda mungkin perlu melihat data dari berbagai negara untuk mengetahuinya.
 - [ ] Hitung tingkat fatalitas dan bagaimana tingkat tersebut berubah seiring waktu. *Anda mungkin perlu mempertimbangkan durasi penyakit dalam hitungan hari untuk menggeser satu deret waktu sebelum melakukan perhitungan.*

## Analisis Makalah COVID-19

- [ ] Bangun matriks ko-occurence dari berbagai jenis obat, dan lihat obat mana yang sering muncul bersama (misalnya disebutkan dalam satu abstrak). Anda dapat memodifikasi kode untuk membangun matriks ko-occurence untuk obat-obatan dan diagnosis.
- [ ] Visualisasikan matriks ini menggunakan heatmap.
- [ ] Sebagai tantangan tambahan, visualisasikan ko-occurence obat-obatan menggunakan [chord diagram](https://en.wikipedia.org/wiki/Chord_diagram). [Pustaka ini](https://pypi.org/project/chord/) mungkin dapat membantu Anda menggambar chord diagram.
- [ ] Sebagai tantangan tambahan lainnya, ekstrak dosis dari berbagai obat (seperti **400mg** dalam *ambil 400mg chloroquine setiap hari*) menggunakan regular expressions, dan bangun dataframe yang menunjukkan berbagai dosis untuk berbagai obat. **Catatan**: pertimbangkan nilai numerik yang berada dalam jarak teks yang dekat dengan nama obat.

## Rubrik

Unggul | Memadai | Perlu Peningkatan
--- | --- | -- |
Semua tugas selesai, diilustrasikan secara grafis dan dijelaskan, termasuk setidaknya satu dari dua tantangan tambahan | Lebih dari 5 tugas selesai, tidak ada tantangan tambahan yang dicoba, atau hasilnya tidak jelas | Kurang dari 5 (tetapi lebih dari 3) tugas selesai, visualisasi tidak membantu menunjukkan poin

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.