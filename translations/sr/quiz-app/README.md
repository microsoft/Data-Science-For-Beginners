<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-30T19:49:43+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "sr"
}
-->
# Квизови

Ови квизови су пред- и пост-предавачки квизови за наставни план и програм науке о подацима на https://aka.ms/datascience-beginners

## Додавање преведеног сета квизова

Додајте превод квиза креирањем одговарајућих структура квиза у фасцикли `assets/translations`. Канонски квизови се налазе у `assets/translations/en`. Квизови су подељени у неколико група. Обавезно ускладите нумерацију са одговарајућим одељком квиза. У овом наставном плану и програму има укупно 40 квизова, а бројање почиње од 0.

Након уређивања превода, измените датотеку `index.js` у фасцикли за преводе да бисте увезли све датотеке пратећи конвенције у `en`.

Измените датотеку `index.js` у `assets/translations` да бисте увезли нове преведене датотеке.

Затим измените падајући мени у `App.vue` у овој апликацији да бисте додали свој језик. Ускладите локализовану скраћеницу са именом фасцикле за ваш језик.

На крају, измените све линкове квизова у преведеним лекцијама, ако постоје, да укључе ову локализацију као параметар упита: `?loc=fr`, на пример.

## Постављање пројекта

```
npm install
```

### Компилирање и аутоматско учитавање за развој

```
npm run serve
```

### Компилирање и минимизирање за продукцију

```
npm run build
```

### Провера и исправке датотека

```
npm run lint
```

### Прилагођавање конфигурације

Погледајте [Референцу конфигурације](https://cli.vuejs.org/config/).

Кредити: Захвалност оригиналној верзији ове апликације за квизове: https://github.com/arpan45/simple-quiz-vue

## Деплојовање на Azure

Ево корак-по-корак водича који ће вам помоћи да започнете:

1. Форкујте GitHub репозиторијум  
Уверите се да је код ваше статичке веб апликације у вашем GitHub репозиторијуму. Форкујте овај репозиторијум.

2. Креирајте Azure статичку веб апликацију  
- Креирајте [Azure налог](http://azure.microsoft.com)  
- Идите на [Azure портал](https://portal.azure.com)  
- Кликните на „Create a resource“ и потражите „Static Web App“.  
- Кликните на „Create“.  

3. Конфигуришите статичку веб апликацију  
- Основно:  
  - Subscription: Изаберите вашу Azure претплату.  
  - Resource Group: Креирајте нову групу ресурса или користите постојећу.  
  - Name: Унесите име за вашу статичку веб апликацију.  
  - Region: Изаберите регион најближи вашим корисницима.  

- #### Детаљи деплојовања:  
  - Source: Изаберите „GitHub“.  
  - GitHub Account: Овластите Azure да приступи вашем GitHub налогу.  
  - Organization: Изаберите вашу GitHub организацију.  
  - Repository: Изаберите репозиторијум који садржи вашу статичку веб апликацију.  
  - Branch: Изаберите грану са које желите да деплојујете.  

- #### Детаљи изградње:  
  - Build Presets: Изаберите оквир у коме је ваша апликација направљена (нпр. React, Angular, Vue, итд.).  
  - App Location: Наведите фасциклу која садржи код ваше апликације (нпр. / ако је у корену).  
  - API Location: Ако имате API, наведите његову локацију (опционо).  
  - Output Location: Наведите фасциклу где се генерише излаз изградње (нпр. build или dist).  

4. Преглед и креирање  
Прегледајте своја подешавања и кликните на „Create“. Azure ће поставити неопходне ресурсе и креирати GitHub Actions workflow у вашем репозиторијуму.

5. GitHub Actions Workflow  
Azure ће аутоматски креирати GitHub Actions workflow датотеку у вашем репозиторијуму (.github/workflows/azure-static-web-apps-<name>.yml). Овај workflow ће обрадити процес изградње и деплојовања.

6. Праћење деплојовања  
Идите на картицу „Actions“ у вашем GitHub репозиторијуму.  
Требало би да видите workflow који се извршава. Овај workflow ће изградити и деплојовати вашу статичку веб апликацију на Azure.  
Када workflow буде завршен, ваша апликација ће бити доступна на обезбеђеном Azure URL-у.

### Пример датотеке workflow-а

Ево примера како би GitHub Actions workflow датотека могла изгледати:  
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

### Додатни ресурси  
- [Azure Static Web Apps документација](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions документација](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неспоразумевања или погрешна тумачења настала услед коришћења овог превода.