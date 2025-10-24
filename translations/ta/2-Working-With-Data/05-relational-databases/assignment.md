<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:59:38+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ta"
}
-->
# விமான நிலைய தரவுகளை காட்டுதல்

உங்களுக்கு [SQLite](https://sqlite.org/index.html) அடிப்படையில் உருவாக்கப்பட்ட [தரவுத்தளம்](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) வழங்கப்பட்டுள்ளது, இது விமான நிலையங்கள் பற்றிய தகவல்களை கொண்டுள்ளது. கீழே உள்ள ஸ்கீமா காட்டப்பட்டுள்ளது. [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) இல் [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) பயன்படுத்தி, பல நகரங்களின் விமான நிலையங்களின் தகவல்களை நீங்கள் காட்டுவீர்கள்.

## வழிமுறைகள்

இந்த பணியைத் தொடங்க, சில அடிப்படை நடவடிக்கைகளை நீங்கள் செய்ய வேண்டும். சில கருவிகளை நிறுவி, மாதிரி தரவுத்தளத்தை பதிவிறக்க வேண்டும்.

### உங்கள் கணினியை அமைத்தல்

தரவுத்தளத்துடன் தொடர்பு கொள்ள Visual Studio Code மற்றும் SQLite extension பயன்படுத்தலாம்.

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) செல்லவும் மற்றும் Visual Studio Code நிறுவுவதற்கான வழிமுறைகளை பின்பற்றவும்
1. [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ஐ Marketplace பக்கத்தில் கொடுக்கப்பட்ட வழிமுறைகளின் படி நிறுவவும்

### தரவுத்தளத்தை பதிவிறக்கி திறக்கவும்

அடுத்ததாக, தரவுத்தளத்தை பதிவிறக்கி திறக்க வேண்டும்.

1. [GitHub-இல் தரவுத்தள கோப்பை](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) பதிவிறக்கி ஒரு கோப்பகத்தில் சேமிக்கவும்
1. Visual Studio Code திறக்கவும்
1. SQLite extension இல் தரவுத்தளத்தை திறக்க **Ctl-Shift-P** (அல்லது Mac-இல் **Cmd-Shift-P**) தேர்வு செய்து `SQLite: Open database` என டைப் செய்யவும்
1. **Choose database from file** தேர்வு செய்து, நீங்கள் முன்பே பதிவிறக்கிய **airports.db** கோப்பை திறக்கவும்
1. தரவுத்தளத்தை திறந்த பிறகு (திரையில் எந்த மாற்றமும் காணப்படாது), **Ctl-Shift-P** (அல்லது Mac-இல் **Cmd-Shift-P**) தேர்வு செய்து `SQLite: New query` என டைப் செய்து புதிய கேள்வி சாளரத்தை உருவாக்கவும்

திறந்த பிறகு, புதிய கேள்வி சாளரத்தை தரவுத்தளத்திற்கு எதிராக SQL அறிக்கைகளை இயக்க பயன்படுத்தலாம். **Ctl-Shift-Q** (அல்லது Mac-இல் **Cmd-Shift-Q**) கட்டளையை பயன்படுத்தி தரவுத்தளத்திற்கு எதிராக கேள்விகளை இயக்கலாம்.

> [!NOTE] 
> SQLite extension பற்றிய கூடுதல் தகவலுக்கு, [ஆவணங்களை](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) பார்க்கலாம்

## தரவுத்தள ஸ்கீமா

ஒரு தரவுத்தளத்தின் ஸ்கீமா என்பது அதன் அட்டவணை வடிவமைப்பு மற்றும் அமைப்பு ஆகும். **airports** தரவுத்தளத்தில் இரண்டு அட்டவணைகள் உள்ளன, `cities`, இது ஐக்கிய இராச்சியம் மற்றும் ஐர்லாந்தில் உள்ள நகரங்களின் பட்டியலை கொண்டுள்ளது, மற்றும் `airports`, இது அனைத்து விமான நிலையங்களின் பட்டியலை கொண்டுள்ளது. சில நகரங்களில் பல விமான நிலையங்கள் இருக்கக்கூடியதால், தகவல்களை சேமிக்க இரண்டு அட்டவணைகள் உருவாக்கப்பட்டன. இந்த பயிற்சியில் நீங்கள் இணைப்புகளைப் பயன்படுத்தி பல நகரங்களின் தகவல்களை காட்டுவீர்கள்.

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## பணிக்குறிப்பு

கீழே உள்ள தகவல்களை திருப்பி கொடுக்க கேள்விகளை உருவாக்கவும்:

1. `Cities` அட்டவணையில் உள்ள அனைத்து நகர பெயர்கள்
1. `Cities` அட்டவணையில் ஐர்லாந்தில் உள்ள அனைத்து நகரங்கள்
1. அனைத்து விமான நிலையங்களின் பெயர்கள், அவற்றின் நகரம் மற்றும் நாடு
1. லண்டன், ஐக்கிய இராச்சியத்தில் உள்ள அனைத்து விமான நிலையங்கள்

## மதிப்பீட்டு அளவுகோல்

| சிறந்தது | போதுமானது | மேம்பாடு தேவை |

---

**புறக்கணிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.