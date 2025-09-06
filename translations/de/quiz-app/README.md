<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-24T22:12:33+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "de"
}
-->
# Quizfragen

Diese Quizfragen sind die Vor- und Nachbereitungsquizfragen für den Data-Science-Lehrplan unter https://aka.ms/datascience-beginners

## Hinzufügen eines übersetzten Quiz-Sets

Fügen Sie eine Quiz-Übersetzung hinzu, indem Sie passende Quiz-Strukturen in den Ordnern `assets/translations` erstellen. Die ursprünglichen Quizfragen befinden sich in `assets/translations/en`. Die Quizfragen sind in mehrere Gruppen unterteilt. Stellen Sie sicher, dass die Nummerierung mit dem entsprechenden Quizabschnitt übereinstimmt. Insgesamt gibt es 40 Quizfragen in diesem Lehrplan, beginnend mit der Nummer 0.

Nachdem Sie die Übersetzungen bearbeitet haben, bearbeiten Sie die Datei `index.js` im Übersetzungsordner, um alle Dateien gemäß den Konventionen in `en` zu importieren.

Bearbeiten Sie die Datei `index.js` in `assets/translations`, um die neuen übersetzten Dateien zu importieren.

Bearbeiten Sie anschließend das Dropdown-Menü in `App.vue` in dieser App, um Ihre Sprache hinzuzufügen. Stimmen Sie die lokalisierte Abkürzung mit dem Ordnernamen für Ihre Sprache ab.

Bearbeiten Sie schließlich alle Quiz-Links in den übersetzten Lektionen, falls vorhanden, um diese Lokalisierung als Abfrageparameter hinzuzufügen: `?loc=fr` zum Beispiel.



## Projektsetup

```
npm install
```

### Kompiliert und lädt für die Entwicklung neu

```
npm run serve
```

### Kompiliert und minimiert für die Produktion

```
npm run build
```

### Überprüft und behebt Dateien

```
npm run lint
```

### Konfiguration anpassen

Siehe [Konfigurationsreferenz](https://cli.vuejs.org/config/).

Credits: Dank an die ursprüngliche Version dieser Quiz-App: https://github.com/arpan45/simple-quiz-vue

## Bereitstellung auf Azure

Hier ist eine Schritt-für-Schritt-Anleitung, die Ihnen den Einstieg erleichtert:

1. Forken Sie ein GitHub-Repository  
Stellen Sie sicher, dass der Code Ihrer statischen Web-App in Ihrem GitHub-Repository ist. Forken Sie dieses Repository.

2. Erstellen Sie eine Azure Static Web App  
- Erstellen Sie ein [Azure-Konto](http://azure.microsoft.com)  
- Gehen Sie zum [Azure-Portal](https://portal.azure.com)  
- Klicken Sie auf „Create a resource“ und suchen Sie nach „Static Web App“.  
- Klicken Sie auf „Create“.  

3. Konfigurieren Sie die Static Web App  
- Grundlagen:  
  - Abonnement: Wählen Sie Ihr Azure-Abonnement aus.  
  - Ressourcengruppe: Erstellen Sie eine neue Ressourcengruppe oder verwenden Sie eine vorhandene.  
  - Name: Geben Sie einen Namen für Ihre statische Web-App an.  
  - Region: Wählen Sie die Region, die Ihren Nutzern am nächsten liegt.  

- #### Bereitstellungsdetails:  
  - Quelle: Wählen Sie „GitHub“.  
  - GitHub-Konto: Autorisieren Sie Azure, auf Ihr GitHub-Konto zuzugreifen.  
  - Organisation: Wählen Sie Ihre GitHub-Organisation aus.  
  - Repository: Wählen Sie das Repository, das Ihre statische Web-App enthält.  
  - Branch: Wählen Sie den Branch, von dem aus Sie bereitstellen möchten.  

- #### Build-Details:  
  - Build-Voreinstellungen: Wählen Sie das Framework aus, mit dem Ihre App erstellt wurde (z. B. React, Angular, Vue usw.).  
  - App-Standort: Geben Sie den Ordner an, der Ihren App-Code enthält (z. B. /, wenn er sich im Root befindet).  
  - API-Standort: Falls Sie eine API haben, geben Sie deren Standort an (optional).  
  - Ausgabe-Standort: Geben Sie den Ordner an, in dem die Build-Ausgabe generiert wird (z. B. build oder dist).  

4. Überprüfen und Erstellen  
Überprüfen Sie Ihre Einstellungen und klicken Sie auf „Create“. Azure wird die erforderlichen Ressourcen einrichten und einen GitHub Actions-Workflow in Ihrem Repository erstellen.

5. GitHub Actions Workflow  
Azure erstellt automatisch eine GitHub Actions-Workflow-Datei in Ihrem Repository (.github/workflows/azure-static-web-apps-<name>.yml). Dieser Workflow übernimmt den Build- und Bereitstellungsprozess.

6. Überwachen der Bereitstellung  
Gehen Sie zum Tab „Actions“ in Ihrem GitHub-Repository.  
Sie sollten sehen, dass ein Workflow ausgeführt wird. Dieser Workflow wird Ihre statische Web-App auf Azure erstellen und bereitstellen.  
Sobald der Workflow abgeschlossen ist, ist Ihre App unter der bereitgestellten Azure-URL live.

### Beispiel-Workflow-Datei

Hier ist ein Beispiel, wie die GitHub Actions-Workflow-Datei aussehen könnte:  
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

### Zusätzliche Ressourcen  
- [Azure Static Web Apps Dokumentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Dokumentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.