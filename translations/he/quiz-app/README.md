<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-28T15:58:09+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "he"
}
-->
# חידונים

החידונים האלה הם חידוני טרום ואחרי הרצאה עבור תוכנית הלימודים למדעי הנתונים בכתובת https://aka.ms/datascience-beginners

## הוספת סט חידונים מתורגם

הוסף תרגום לחידון על ידי יצירת מבני חידון תואמים בתיקיות `assets/translations`. החידונים המקוריים נמצאים ב-`assets/translations/en`. החידונים מחולקים לכמה קבוצות. ודא שהמספור תואם את החלק המתאים של החידון. ישנם 40 חידונים בסך הכל בתוכנית הלימודים הזו, עם המספור שמתחיל מ-0.

לאחר עריכת התרגומים, ערוך את קובץ index.js בתיקיית התרגום כדי לייבא את כל הקבצים בהתאם למוסכמות ב-`en`.

ערוך את קובץ `index.js` ב-`assets/translations` כדי לייבא את הקבצים המתורגמים החדשים.

לאחר מכן, ערוך את התפריט הנפתח ב-`App.vue` באפליקציה הזו כדי להוסיף את השפה שלך. התאמה בין הקיצור המקומי לשם התיקייה עבור השפה שלך.

לבסוף, ערוך את כל קישורי החידונים בשיעורים המתורגמים, אם הם קיימים, כדי לכלול את הלוקליזציה הזו כפרמטר שאילתה: `?loc=fr` לדוגמה.

## הגדרת הפרויקט

```
npm install
```

### קומפילציה וטעינה מחדש לפיתוח

```
npm run serve
```

### קומפילציה ומזעור עבור הפקה

```
npm run build
```

### בדיקת קוד ותיקון קבצים

```
npm run lint
```

### התאמת הגדרות

ראה [הפניה להגדרות](https://cli.vuejs.org/config/).

קרדיטים: תודה לגרסה המקורית של אפליקציית החידונים הזו: https://github.com/arpan45/simple-quiz-vue

## פריסה ל-Azure

הנה מדריך שלב אחר שלב שיעזור לך להתחיל:

1. בצע Fork למאגר GitHub  
ודא שקוד האפליקציה הסטטית שלך נמצא במאגר GitHub שלך. בצע Fork למאגר הזה.

2. צור אפליקציה סטטית ב-Azure  
- צור [חשבון Azure](http://azure.microsoft.com)  
- עבור ל-[פורטל Azure](https://portal.azure.com)  
- לחץ על "Create a resource" וחפש "Static Web App".  
- לחץ על "Create".  

3. הגדר את האפליקציה הסטטית  
- בסיסי:  
  - Subscription: בחר את המנוי שלך ב-Azure.  
  - Resource Group: צור קבוצת משאבים חדשה או השתמש בקיימת.  
  - Name: ספק שם לאפליקציה הסטטית שלך.  
  - Region: בחר את האזור הקרוב ביותר למשתמשים שלך.  

- #### פרטי פריסה:  
  - Source: בחר "GitHub".  
  - GitHub Account: אשר ל-Azure גישה לחשבון GitHub שלך.  
  - Organization: בחר את הארגון שלך ב-GitHub.  
  - Repository: בחר את המאגר שמכיל את האפליקציה הסטטית שלך.  
  - Branch: בחר את הענף שממנו תרצה לפרוס.  

- #### פרטי בנייה:  
  - Build Presets: בחר את המסגרת שבה האפליקציה שלך נבנתה (לדוגמה, React, Angular, Vue וכו').  
  - App Location: ציין את התיקייה שמכילה את קוד האפליקציה שלך (לדוגמה, / אם היא נמצאת בשורש).  
  - API Location: אם יש לך API, ציין את מיקומו (אופציונלי).  
  - Output Location: ציין את התיקייה שבה נוצר פלט הבנייה (לדוגמה, build או dist).  

4. סקירה ויצירה  
סקור את ההגדרות שלך ולחץ על "Create". Azure יגדיר את המשאבים הנדרשים וייצור קובץ GitHub Actions במאגר שלך.

5. קובץ GitHub Actions Workflow  
Azure ייצור באופן אוטומטי קובץ GitHub Actions Workflow במאגר שלך (.github/workflows/azure-static-web-apps-<name>.yml). קובץ זה יטפל בתהליך הבנייה והפריסה.

6. מעקב אחר הפריסה  
עבור ללשונית "Actions" במאגר GitHub שלך.  
אתה אמור לראות Workflow פועל. Workflow זה יבנה ויפרס את האפליקציה הסטטית שלך ל-Azure.  
לאחר שה-Workflow יושלם, האפליקציה שלך תהיה זמינה בכתובת ה-URL שסופקה על ידי Azure.

### דוגמה לקובץ Workflow

הנה דוגמה לאיך קובץ GitHub Actions Workflow עשוי להיראות:  
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

### משאבים נוספים  
- [תיעוד אפליקציות סטטיות ב-Azure](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [תיעוד GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד אנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.