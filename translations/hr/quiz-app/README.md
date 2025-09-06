<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-30T19:49:58+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "hr"
}
-->
# Kvizovi

Ovi kvizovi su uvodni i završni kvizovi za kurikulum znanosti o podacima na https://aka.ms/datascience-beginners

## Dodavanje prevedenog seta kvizova

Dodajte prijevod kviza kreiranjem odgovarajućih struktura kvizova u mapama `assets/translations`. Izvorni kvizovi nalaze se u `assets/translations/en`. Kvizovi su podijeljeni u nekoliko grupa. Pazite da uskladite numeraciju s odgovarajućim dijelom kviza. Ukupno postoji 40 kvizova u ovom kurikulumu, a brojevi počinju od 0.

Nakon uređivanja prijevoda, uredite datoteku `index.js` u mapi za prijevod kako biste uvezli sve datoteke prema konvencijama u `en`.

Uredite datoteku `index.js` u `assets/translations` kako biste uvezli nove prevedene datoteke.

Zatim uredite padajući izbornik u `App.vue` u ovoj aplikaciji kako biste dodali svoj jezik. Uskladite lokaliziranu skraćenicu s nazivom mape za vaš jezik.

Na kraju, uredite sve poveznice kvizova u prevedenim lekcijama, ako postoje, kako biste uključili ovu lokalizaciju kao parametar upita: `?loc=fr`, na primjer.

## Postavljanje projekta

```
npm install
```

### Kompajlira i automatski ponovno učitava za razvoj

```
npm run serve
```

### Kompajlira i minimizira za produkciju

```
npm run build
```

### Provjerava i popravlja datoteke

```
npm run lint
```

### Prilagodba konfiguracije

Pogledajte [Referencu za konfiguraciju](https://cli.vuejs.org/config/).

Zahvale: Zahvaljujemo na originalnoj verziji ove aplikacije za kvizove: https://github.com/arpan45/simple-quiz-vue

## Postavljanje na Azure

Evo korak-po-korak vodiča koji će vam pomoći da započnete:

1. Forkajte GitHub repozitorij  
Provjerite je li vaš kod za statičnu web aplikaciju u vašem GitHub repozitoriju. Forkajte ovaj repozitorij.

2. Kreirajte Azure Static Web App  
- Kreirajte [Azure račun](http://azure.microsoft.com)  
- Idite na [Azure portal](https://portal.azure.com)  
- Kliknite na “Create a resource” i potražite “Static Web App”.  
- Kliknite “Create”.

3. Konfigurirajte Static Web App  
- Osnovno: Pretplata: Odaberite svoju Azure pretplatu.  
- Grupa resursa: Kreirajte novu grupu resursa ili koristite postojeću.  
- Naziv: Unesite naziv za svoju statičnu web aplikaciju.  
- Regija: Odaberite regiju najbližu vašim korisnicima.

- #### Detalji implementacije:  
- Izvor: Odaberite “GitHub”.  
- GitHub račun: Autorizirajte Azure za pristup vašem GitHub računu.  
- Organizacija: Odaberite svoju GitHub organizaciju.  
- Repozitorij: Odaberite repozitorij koji sadrži vašu statičnu web aplikaciju.  
- Grana: Odaberite granu iz koje želite implementirati.

- #### Detalji izgradnje:  
- Predlošci izgradnje: Odaberite okvir na kojem je vaša aplikacija izgrađena (npr. React, Angular, Vue, itd.).  
- Lokacija aplikacije: Navedite mapu koja sadrži kod vaše aplikacije (npr. / ako je u korijenu).  
- Lokacija API-ja: Ako imate API, navedite njegovu lokaciju (opcionalno).  
- Lokacija izlaza: Navedite mapu u kojoj se generira izlaz izgradnje (npr. build ili dist).

4. Pregled i kreiranje  
Pregledajte svoje postavke i kliknite “Create”. Azure će postaviti potrebne resurse i kreirati GitHub Actions workflow u vašem repozitoriju.

5. GitHub Actions Workflow  
Azure će automatski kreirati GitHub Actions workflow datoteku u vašem repozitoriju (.github/workflows/azure-static-web-apps-<name>.yml). Ovaj workflow će upravljati procesom izgradnje i implementacije.

6. Praćenje implementacije  
Idite na karticu “Actions” u svom GitHub repozitoriju.  
Trebali biste vidjeti workflow koji se pokreće. Ovaj workflow će izgraditi i implementirati vašu statičnu web aplikaciju na Azure.  
Kada workflow završi, vaša aplikacija će biti dostupna na pruženom Azure URL-u.

### Primjer datoteke workflowa

Evo primjera kako bi GitHub Actions workflow datoteka mogla izgledati:  
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

### Dodatni resursi  
- [Dokumentacija za Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [Dokumentacija za GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden koristeći AI uslugu za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.