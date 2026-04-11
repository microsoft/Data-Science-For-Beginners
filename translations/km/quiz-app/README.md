# ព្រឹត្តិការណ៍សួរសំណួរ

ព្រឹត្តិការណ៍សួរសំណួរទាំងនេះគឺជាព្រឹត្តិការណ៍សួរសំណួរមុននិងក្រោយមេរៀនសម្រាប់មេរៀនវិទ្យាសាស្ត្រទិន្នន័យនៅ https://aka.ms/datascience-beginners
## ការបន្ថែមកំណត់ត្រាព្រឹត្តិការណ៍សួរសំណួរដែលបានបកប្រែ

បន្ថែមការបកប្រែព្រឹត្តិការណ៍សួរសំណួរដោយបង្កើតរចនាសម្ព័ន្ធព្រឹត្តិការណ៍សួរសំណួរដែលផ្គូផ្គងគ្នានៅក្នុងថត `assets/translations`។ ព្រឹត្តិការណ៍សួរសំណួរដើមមាននៅក្នុង `assets/translations/en`។ ព្រឹត្តិការណ៍សួរសំណួរត្រូវបានបំបែកជា​ចំនួនជាក្រុម​ពីរ នៃថ្នាក់សួរសំណួរ។ ត្រូវប្រាកដថាអ្នកត្រូវតាមលេខរៀងជាមួយផ្នែកព្រឹត្តិការណ៍សួរសំនួរដូចគ្នា។ មានព្រឹត្តិការណ៍សួរសំណួរចំនួន ៤០ ក្នុងមេរៀននេះ ហើយលេខរាប់ចាប់ពី 0 ។

បន្ទាប់ពីកែសម្រួលការបកប្រែ សូមកែសម្រួលឯកសារ index.js នៅក្នុងថតបកប្រែដើម្បីនាំចូលឯកសារទាំងអស់ដោយអនុវត្តតាមទំនាក់ទំនងនៅក្នុង `en`។

កែសម្រួលឯកសារ `index.js` នៅក្នុង `assets/translations` ដើម្បីនាំចូលឯកសារបកប្រែថ្មី។

បន្ទាប់មក កែសម្រួលផ្ទាំងជាលំហូរនៅក្នុង `App.vue` នៅក្នុងកម្មវិធីនេះ ដើម្បីបន្ថែមភាសារបស់អ្នក។ ត្រូវផ្គូផ្គងការបំប្លែងខ្លីរបស់ភាសារឱ្យស្របជាមួយឈ្មោះថតសម្រាប់ភាសារបស់អ្នក។

ចុងក្រោយ កែសម្រួលតំណភ្ជាប់ព្រឹត្តិការណ៍សួរសំណួរទាំងអស់នៅក្នុងមេរៀនដែលបានបកប្រែ ប្រសិនបើមាន ដើម្បីបញ្ចូលការបំប្លែងភាសានេះជាប៉ារ៉ាម៉ែត្រសំណួរ៖ `?loc=fr` ជាឧទាហរណ៍។


## ការតំឡើងគម្រោង

```
npm install
```

### កំណត់រួច ហើយផ្ទុកឡើងវិញសម្រាប់ការអភិវឌ្ឍន៍

```
npm run serve
```

### កំណត់រួច ហើយបង្រួមសម្រាប់ការផលិត

```
npm run build
```

### ត្រួតពិនិត្យ និងកែសម្រួលឯកសារ

```
npm run lint
```

### ប្ដូរតំរូវការកំណត់

មើល [យោងការកំណត់](https://cli.vuejs.org/config/)។

គាំទ្រ៖ អរគុណចំពោះកំណែដើមនៃកម្មវិធីព្រឹត្តិការណ៍សួរសំណួរនេះ៖ https://github.com/arpan45/simple-quiz-vue

## ការបង្ហោះទៅ Azure

នេះជាមេរៀនជំហានក្រោយជំហាន់ដើម្បីជួយអ្នកចាប់ផ្តើម៖

1. Fork រត់បញ្ជី GitHub
ធ្វើឱ្យប្រាកដថាកូដកម្មវិធីអេបស្ទាតរបស់អ្នកមាននៅក្នុងរត់បញ្ជី GitHub របស់អ្នក។ Fork រត់បញ្ជីនេះ។

2. បង្កើត Azure Static Web App
- បង្កើតគណនី [Azure](http://azure.microsoft.com)
- ចូលទៅកាន់ [Azure portal](https://portal.azure.com) 
- ចុច “Create a resource” ហើយស្វែងរក “Static Web App”។
- ចុច “Create”។

3. កំណត់ Static Web App
- មូលដ្ឋាន៖ Subscription: ជ្រើសរើសការចុះបញ្ជី Azure របស់អ្នក។
- Resource Group: បង្កើតក្រុមធនធានថ្មី ឬប្រើក្រុមដែលមានរួច។
- Name: ផ្តល់ឈ្មោះសម្រាប់កម្មវិធីអេបស្ទាតរបស់អ្នក។
- តំបន់៖ ជ្រើសតំបន់ដែលនៅក្បែរពេលអ្នកប្រើប្រាស់របស់អ្នក។

- #### ព័ត៌មានការបង្ហោះ:
- ប្រភព៖ ជ្រើស "GitHub"។
- គណនី GitHub៖ អនុញ្ញាត Azure ដើម្បីចូលប្រើគណនី GitHub របស់អ្នក។
- អង្គភាព៖ ជ្រើសអង្គភាព GitHub របស់អ្នក។
- រត់បញ្ជី៖ ជ្រើសរត់បញ្ជីដែលមានកម្មវិធីអេបស្ទាតរបស់អ្នក។
- សាខា៖ ជ្រើសសាខាដែលអ្នកចង់បង្ហោះពី។

- #### ព័ត៌មានផលិត៖
- Build Presets: ជ្រើសផ្ទាំងការងារដែលកម្មវិធីរបស់អ្នកត្រូវបានកំណត់ជាមួយ (ឧ. React, Angular, Vue, ជាដើម)។
- App Location: បញ្ជាក់ថតដែលមានកូដកម្មវិធីរបស់អ្នក (ឧ. / ប្រសិនបើវានៅក្នុងថតដើម)។
- API Location: ប្រសិនបើអ្នកមាន API សូមបញ្ជាក់ទីតាំង (ជាជម្រើស)។
- Output Location: បញ្ជាក់ថតដែលផលិតផលបង្កើត (ឧ. build ឬ dist)។

4. ពិនិត្យ និងបង្កើត
ពិនិត្យការកំណត់របស់អ្នកហើយចុច “Create”។ Azure នឹងរៀបចំធនធានត្រឹមត្រូវ និងបង្កើត workflow GitHub Actions នៅក្នុងរត់បញ្ជីរបស់អ្នក។

5. Workflow GitHub Actions
Azure នឹងបង្កើតឯកសារ workflow GitHub Actions ដោយស្វ័យប្រវត្តិ នៅក្នុងរត់បញ្ជីរបស់អ្នក (.github/workflows/azure-static-web-apps-<name>.yml)។ Workflow នេះនឹងគ្រប់គ្រងដំណើរការបង្កើត និងការបង្ហោះ។

6. តាមដានការបង្ហោះ
ចូលទៅកាន់ផ្ទាំង “Actions” នៅក្នុងរត់បញ្ជី GitHub របស់អ្នក។
អ្នកគួរតែឃើញ workflow កំពុងដំណើរការ។ Workflow នេះនឹងបង្កើត និងបង្ហោះកម្មវិធីអេបស្ទាតរបស់អ្នកទៅ Azure។
ពេល workflow សម្រេចរួច ពាក្យសុំរបស់អ្នកនឹងមាននៅលើ URL Azure ដែលបានផ្ដល់។

### ឧទាហរណ៍ឯកសារ Workflow

នេះគឺជាឧទាហរណ៍នៃរូបរាងឯកសារ workflow GitHub Actions:
name: ការបង្ហោះ CI/CD របស់ Azure Static Web Apps
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

### ឯកសារបន្ថែម
- [ឯកសារព័ត៌មាន Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [ឯកសារព័ត៌មាន GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំដើម្បីឱ្យមានភាពត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវខ្លះ។ ឯកសារដើមជាភាសាម្ដងខ្លួនគួរត្រូវបានគិតជាទីតាំងប្រភពដ៏មានសុពលភាព។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមផ្តល់អាទិភាពនូវការបកប្រែដោយមនុស្សមានជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសប្រកបដោយការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->