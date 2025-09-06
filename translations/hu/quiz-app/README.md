<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-26T16:18:15+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "hu"
}
-->
# Kvízek

Ezek a kvízek a data science tananyag előtti és utáni kvízei, amely elérhető itt: https://aka.ms/datascience-beginners  
## Fordított kvízkészlet hozzáadása

Fordított kvízt úgy adhatsz hozzá, hogy létrehozod a megfelelő kvízstruktúrákat az `assets/translations` mappákban. Az eredeti kvízek az `assets/translations/en` mappában találhatók. A kvízek több csoportba vannak osztva. Ügyelj arra, hogy a számozás igazodjon a megfelelő kvízszekcióhoz. Összesen 40 kvíz van ebben a tananyagban, a számozás 0-tól kezdődik.

A fordítások szerkesztése után szerkeszd az `index.js` fájlt a fordítási mappában, hogy importáld az összes fájlt az `en` mappában található konvenciók szerint.

Szerkeszd az `index.js` fájlt az `assets/translations` mappában, hogy importáld az új fordított fájlokat.

Ezután szerkeszd a legördülő menüt az `App.vue` fájlban ebben az alkalmazásban, hogy hozzáadd a nyelvedet. Azonosítsd a lokalizált rövidítést a nyelved mappanevével.

Végül szerkeszd az összes kvíz linket a fordított leckékben, ha léteznek, hogy tartalmazzák ezt a lokalizációt mint lekérdezési paramétert: például `?loc=fr`.

## Projekt beállítása

```
npm install
```

### Fejlesztéshez fordít és automatikusan újratölt

```
npm run serve
```

### Termeléshez fordít és minimalizál

```
npm run build
```

### Fájlokat ellenőriz és javít

```
npm run lint
```

### Konfiguráció testreszabása

Lásd: [Konfigurációs hivatkozás](https://cli.vuejs.org/config/).

Köszönet az eredeti kvíz alkalmazás verziójáért: https://github.com/arpan45/simple-quiz-vue

## Azure-ra telepítés

Íme egy lépésről lépésre útmutató, hogy elkezdhesd:

1. Forkolj egy GitHub repót  
Győződj meg róla, hogy a statikus webalkalmazásod kódja a GitHub repódban van. Forkold ezt a repót.

2. Hozz létre egy Azure statikus webalkalmazást  
- Hozz létre egy [Azure fiókot](http://azure.microsoft.com)  
- Lépj be az [Azure portálra](https://portal.azure.com)  
- Kattints a „Create a resource” gombra, és keress rá a „Static Web App”-ra.  
- Kattints a „Create” gombra.

3. Konfiguráld a statikus webalkalmazást  
- Alapok:  
  - Előfizetés: Válaszd ki az Azure előfizetésedet.  
  - Erőforráscsoport: Hozz létre egy új erőforráscsoportot, vagy használj egy meglévőt.  
  - Név: Adj nevet a statikus webalkalmazásodnak.  
  - Régió: Válaszd ki a felhasználóidhoz legközelebbi régiót.  

- #### Telepítési részletek:  
  - Forrás: Válaszd a „GitHub”-ot.  
  - GitHub fiók: Engedélyezd az Azure számára, hogy hozzáférjen a GitHub fiókodhoz.  
  - Szervezet: Válaszd ki a GitHub szervezetedet.  
  - Repó: Válaszd ki azt a repót, amely tartalmazza a statikus webalkalmazásodat.  
  - Ág: Válaszd ki azt az ágat, amelyből telepíteni szeretnél.  

- #### Build részletek:  
  - Build előbeállítások: Válaszd ki azt a keretrendszert, amelyre az alkalmazásod épül (pl. React, Angular, Vue stb.).  
  - Alkalmazás helye: Add meg azt a mappát, amely tartalmazza az alkalmazásod kódját (pl. / ha a gyökérben van).  
  - API helye: Ha van API-d, add meg annak helyét (opcionális).  
  - Kimeneti hely: Add meg azt a mappát, ahol a build kimenete generálódik (pl. build vagy dist).  

4. Áttekintés és létrehozás  
Tekintsd át a beállításaidat, és kattints a „Create” gombra. Az Azure létrehozza a szükséges erőforrásokat, és létrehoz egy GitHub Actions munkafolyamatot a repódban.

5. GitHub Actions munkafolyamat  
Az Azure automatikusan létrehoz egy GitHub Actions munkafolyamat fájlt a repódban (.github/workflows/azure-static-web-apps-<name>.yml). Ez a munkafolyamat kezeli a build és telepítési folyamatot.

6. A telepítés nyomon követése  
Lépj a „Actions” fülre a GitHub repódban.  
Látnod kell egy futó munkafolyamatot. Ez a munkafolyamat felépíti és telepíti a statikus webalkalmazásodat az Azure-ra.  
Amint a munkafolyamat befejeződik, az alkalmazásod élő lesz az Azure által biztosított URL-en.

### Példa munkafolyamat fájl

Íme, hogyan nézhet ki egy GitHub Actions munkafolyamat fájl:  
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

### További források  
- [Azure Static Web Apps Dokumentáció](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Dokumentáció](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.