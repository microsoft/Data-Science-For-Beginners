<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-28T18:54:16+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "ms"
}
-->
# Kajian Kecil Diabetes

Dalam tugasan ini, kita akan bekerja dengan dataset kecil pesakit diabetes yang diambil dari [sini](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | UMUR | JANTINA | BMI | BP | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|------|---------|-----|----|----|----|----|----|----|----|----|
| 0 | 59   | 2       | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48   | 1       | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72   | 2       | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ...     | ...  | ...  | ... | ... | ... | ... | ... | ... | ... |

## Arahan

* Buka [notebook tugasan](assignment.ipynb) dalam persekitaran jupyter notebook
* Lengkapkan semua tugasan yang disenaraikan dalam notebook, iaitu:
   * [ ] Kira nilai purata dan varians untuk semua nilai
   * [ ] Plotkan boxplot untuk BMI, BP dan Y berdasarkan jantina
   * [ ] Apakah taburan bagi pemboleh ubah Umur, Jantina, BMI dan Y?
   * [ ] Uji korelasi antara pemboleh ubah yang berbeza dengan perkembangan penyakit (Y)
   * [ ] Uji hipotesis bahawa tahap perkembangan diabetes adalah berbeza antara lelaki dan wanita
   
## Rubrik

Cemerlang | Memadai | Perlu Penambahbaikan
--- | --- | --- |
Semua tugasan yang diperlukan lengkap, digambarkan secara grafik dan dijelaskan | Kebanyakan tugasan lengkap, penjelasan atau kesimpulan daripada grafik dan/atau nilai yang diperoleh tidak disertakan | Hanya tugasan asas seperti pengiraan purata/varians dan plot asas lengkap, tiada kesimpulan dibuat daripada data

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.