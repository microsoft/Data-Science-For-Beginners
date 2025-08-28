<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-28T19:06:29+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "id"
}
-->
# Kuis

Kuis-kuis ini adalah kuis sebelum dan sesudah pelajaran untuk kurikulum data science di https://aka.ms/datascience-beginners

## Menambahkan Set Kuis Terjemahan

Tambahkan terjemahan kuis dengan membuat struktur kuis yang sesuai di folder `assets/translations`. Kuis asli berada di `assets/translations/en`. Kuis-kuis ini dibagi menjadi beberapa kelompok. Pastikan untuk menyelaraskan penomoran dengan bagian kuis yang sesuai. Total ada 40 kuis dalam kurikulum ini, dengan penomoran dimulai dari 0.

Setelah mengedit terjemahan, edit file `index.js` di folder terjemahan untuk mengimpor semua file sesuai dengan konvensi di `en`.

Edit file `index.js` di `assets/translations` untuk mengimpor file terjemahan baru.

Kemudian, edit dropdown di `App.vue` dalam aplikasi ini untuk menambahkan bahasa Anda. Cocokkan singkatan lokal dengan nama folder untuk bahasa Anda.

Terakhir, edit semua tautan kuis di pelajaran yang diterjemahkan, jika ada, untuk menyertakan lokalisasi ini sebagai parameter kueri: `?loc=fr` misalnya.

## Pengaturan Proyek

```
npm install
```

### Kompilasi dan pemuatan ulang otomatis untuk pengembangan

```
npm run serve
```

### Kompilasi dan minifikasi untuk produksi

```
npm run build
```

### Linting dan perbaikan file

```
npm run lint
```

### Kustomisasi konfigurasi

Lihat [Referensi Konfigurasi](https://cli.vuejs.org/config/).

Kredit: Terima kasih kepada versi asli dari aplikasi kuis ini: https://github.com/arpan45/simple-quiz-vue

## Mendeploy ke Azure

Berikut adalah panduan langkah demi langkah untuk membantu Anda memulai:

1. Fork Repositori GitHub  
Pastikan kode aplikasi web statis Anda ada di repositori GitHub Anda. Fork repositori ini.

2. Buat Azure Static Web App  
- Buat akun [Azure](http://azure.microsoft.com)  
- Buka [portal Azure](https://portal.azure.com)  
- Klik “Create a resource” dan cari “Static Web App”.  
- Klik “Create”.  

3. Konfigurasi Static Web App  
- **Dasar**:  
  - Subscription: Pilih langganan Azure Anda.  
  - Resource Group: Buat grup sumber daya baru atau gunakan yang sudah ada.  
  - Name: Berikan nama untuk aplikasi web statis Anda.  
  - Region: Pilih wilayah yang paling dekat dengan pengguna Anda.  

- **Detail Deployment**:  
  - Source: Pilih “GitHub”.  
  - GitHub Account: Berikan otorisasi kepada Azure untuk mengakses akun GitHub Anda.  
  - Organization: Pilih organisasi GitHub Anda.  
  - Repository: Pilih repositori yang berisi aplikasi web statis Anda.  
  - Branch: Pilih cabang yang ingin Anda deploy.  

- **Detail Build**:  
  - Build Presets: Pilih framework yang digunakan aplikasi Anda (misalnya, React, Angular, Vue, dll.).  
  - App Location: Tentukan folder yang berisi kode aplikasi Anda (misalnya, / jika berada di root).  
  - API Location: Jika Anda memiliki API, tentukan lokasinya (opsional).  
  - Output Location: Tentukan folder tempat output build dihasilkan (misalnya, build atau dist).  

4. Tinjau dan Buat  
Tinjau pengaturan Anda dan klik “Create”. Azure akan menyiapkan sumber daya yang diperlukan dan membuat workflow GitHub Actions di repositori Anda.

5. Workflow GitHub Actions  
Azure secara otomatis akan membuat file workflow GitHub Actions di repositori Anda (.github/workflows/azure-static-web-apps-<name>.yml). Workflow ini akan menangani proses build dan deployment.

6. Pantau Deployment  
Buka tab “Actions” di repositori GitHub Anda.  
Anda akan melihat workflow yang sedang berjalan. Workflow ini akan membangun dan mendeploy aplikasi web statis Anda ke Azure.  
Setelah workflow selesai, aplikasi Anda akan aktif di URL Azure yang disediakan.

### Contoh File Workflow

Berikut adalah contoh file workflow GitHub Actions:  
name: Azure Static Web Apps CI/CD  
```
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v2
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "quiz-app" # App source code path
          api_location: ""API source code path optional
          output_location: "dist" #Built app content directory - optional
```

### Sumber Daya Tambahan  
- [Dokumentasi Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [Dokumentasi GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.