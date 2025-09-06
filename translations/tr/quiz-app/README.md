<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-28T11:30:16+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "tr"
}
-->
# Quizler

Bu quizler, https://aka.ms/datascience-beginners adresindeki veri bilimi müfredatının ders öncesi ve sonrası quizleridir.

## Çevirilmiş bir quiz seti ekleme

Bir quiz çevirisi eklemek için `assets/translations` klasörlerinde eşleşen quiz yapıları oluşturun. Orijinal quizler `assets/translations/en` klasöründe bulunmaktadır. Quizler birkaç gruba ayrılmıştır. Numara sıralamasını doğru quiz bölümüyle hizalamayı unutmayın. Bu müfredatta toplamda 40 quiz bulunmaktadır ve numaralandırma 0'dan başlamaktadır.

Çevirileri düzenledikten sonra, `en` klasöründeki kurallara uygun olarak çeviri klasöründeki `index.js` dosyasını düzenleyerek tüm dosyaları içe aktarın.

`assets/translations` klasöründeki `index.js` dosyasını düzenleyerek yeni çevrilmiş dosyaları içe aktarın.

Son olarak, bu uygulamadaki `App.vue` dosyasındaki açılır menüyü düzenleyerek dilinizi ekleyin. Yerelleştirilmiş kısaltmayı dilinizin klasör adıyla eşleştirin.

Eğer varsa, çevrilmiş derslerdeki tüm quiz bağlantılarını düzenleyerek bu yerelleştirmeyi bir sorgu parametresi olarak ekleyin: örneğin `?loc=fr`.

## Proje kurulumu

```
npm install
```

### Geliştirme için derler ve hızlı yeniden yükler

```
npm run serve
```

### Üretim için derler ve küçültür

```
npm run build
```

### Dosyaları kontrol eder ve düzeltir

```
npm run lint
```

### Yapılandırmayı özelleştirme

[Configuration Reference](https://cli.vuejs.org/config/) adresine bakın.

Teşekkürler: Bu quiz uygulamasının orijinal versiyonu için teşekkürler: https://github.com/arpan45/simple-quiz-vue

## Azure'a dağıtım

Başlamak için adım adım bir rehber:

1. GitHub Deposu Çatallayın  
Statik web uygulamanızın kodunun GitHub deponuzda olduğundan emin olun. Bu depoyu çatallayın.

2. Azure Statik Web Uygulaması Oluşturun  
- Bir [Azure hesabı](http://azure.microsoft.com) oluşturun.  
- [Azure portalına](https://portal.azure.com) gidin.  
- “Create a resource” seçeneğine tıklayın ve “Static Web App” arayın.  
- “Create” seçeneğine tıklayın.  

3. Statik Web Uygulamasını Yapılandırın  
- Temel Bilgiler:  
  - Abonelik: Azure aboneliğinizi seçin.  
  - Kaynak Grubu: Yeni bir kaynak grubu oluşturun veya mevcut birini kullanın.  
  - Ad: Statik web uygulamanız için bir ad sağlayın.  
  - Bölge: Kullanıcılarınıza en yakın bölgeyi seçin.  

- #### Dağıtım Detayları:  
  - Kaynak: “GitHub” seçeneğini seçin.  
  - GitHub Hesabı: Azure'un GitHub hesabınıza erişmesine izin verin.  
  - Organizasyon: GitHub organizasyonunuzu seçin.  
  - Depo: Statik web uygulamanızı içeren depoyu seçin.  
  - Dal: Dağıtım yapmak istediğiniz dalı seçin.  

- #### Yapı Detayları:  
  - Yapı Ön Ayarları: Uygulamanızın hangi framework ile oluşturulduğunu seçin (örneğin, React, Angular, Vue, vb.).  
  - Uygulama Konumu: Uygulama kodunuzu içeren klasörü belirtin (örneğin, kökteyse /).  
  - API Konumu: Bir API'niz varsa, konumunu belirtin (isteğe bağlı).  
  - Çıktı Konumu: Yapı çıktısının oluşturulduğu klasörü belirtin (örneğin, build veya dist).  

4. Gözden Geçir ve Oluştur  
Ayarlarınızı gözden geçirin ve “Create” seçeneğine tıklayın. Azure gerekli kaynakları ayarlayacak ve deponuzda bir GitHub Actions iş akışı oluşturacaktır.

5. GitHub Actions İş Akışı  
Azure, deponuzda otomatik olarak bir GitHub Actions iş akışı dosyası oluşturacaktır (.github/workflows/azure-static-web-apps-<name>.yml). Bu iş akışı, yapı ve dağıtım sürecini yönetecektir.

6. Dağıtımı İzleme  
GitHub deponuzdaki “Actions” sekmesine gidin.  
Bir iş akışının çalıştığını görmelisiniz. Bu iş akışı, statik web uygulamanızı Azure'a oluşturacak ve dağıtacaktır.  
İş akışı tamamlandığında, uygulamanız sağlanan Azure URL'sinde canlı olacaktır.

### Örnek İş Akışı Dosyası

GitHub Actions iş akışı dosyasının nasıl görünebileceğine dair bir örnek:  
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

### Ek Kaynaklar  
- [Azure Statik Web Uygulamaları Belgeleri](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Belgeleri](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı bir yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul etmiyoruz.