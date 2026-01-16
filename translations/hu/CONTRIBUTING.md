<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:28:37+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hu"
}
-->
# Hozzájárulás az Adattudomány Kezdőknek programhoz

Köszönjük, hogy érdeklődsz az Adattudomány Kezdőknek tananyaghoz való hozzájárulás iránt! Örömmel fogadjuk a közösség hozzájárulásait.

## Tartalomjegyzék

- [Magatartási kódex](../..)
- [Hogyan járulhatok hozzá?](../..)
- [Első lépések](../..)
- [Hozzájárulási irányelvek](../..)
- [Pull Request folyamat](../..)
- [Stílusirányelvek](../..)
- [Hozzájárulói licencszerződés](../..)

## Magatartási kódex

Ez a projekt a [Microsoft Nyílt Forráskódú Magatartási Kódexét](https://opensource.microsoft.com/codeofconduct/) alkalmazza.  
További információért lásd a [Magatartási Kódex GYIK](https://opensource.microsoft.com/codeofconduct/faq/) oldalt, vagy lépj kapcsolatba az [opencode@microsoft.com](mailto:opencode@microsoft.com) címen bármilyen további kérdéssel vagy megjegyzéssel.

## Hogyan járulhatok hozzá?

### Hibák jelentése

Mielőtt hibajelentést készítenél, ellenőrizd a meglévő problémákat, hogy elkerüld a duplikációt. Hibajelentés készítésekor adj meg minél több részletet:

- **Használj egyértelmű és leíró címet**
- **Írd le pontosan a probléma reprodukálásának lépéseit**
- **Adj meg konkrét példákat** (kódrészletek, képernyőképek)
- **Írd le az észlelt viselkedést és azt, amit vártál**
- **Add meg a környezeted részleteit** (operációs rendszer, Python verzió, böngésző)

### Fejlesztési javaslatok

Fejlesztési javaslatokat szívesen fogadunk! Javaslat készítésekor:

- **Használj egyértelmű és leíró címet**
- **Adj részletes leírást a javasolt fejlesztésről**
- **Magyarázd el, miért lenne hasznos ez a fejlesztés**
- **Sorolj fel hasonló funkciókat más projektekben, ha releváns**

### Dokumentációhoz való hozzájárulás

A dokumentáció fejlesztése mindig értékes:

- **Javítsd a helyesírási és nyelvtani hibákat**
- **Tedd érthetőbbé a magyarázatokat**
- **Egészítsd ki a hiányzó dokumentációt**
- **Frissítsd az elavult információkat**
- **Adj példákat vagy felhasználási eseteket**

### Kódhoz való hozzájárulás

Szívesen fogadjuk a kódhoz való hozzájárulásokat, például:

- **Új leckék vagy gyakorlatok**
- **Hibajavítások**
- **Meglévő notebookok fejlesztése**
- **Új adathalmazok vagy példák**
- **Kvíz alkalmazás fejlesztései**

## Első lépések

### Előfeltételek

Hozzájárulás előtt győződj meg róla, hogy rendelkezel:

1. GitHub fiókkal
2. Git telepítve van a rendszereden
3. Python 3.7+ és Jupyter telepítve van
4. Node.js és npm (kvíz alkalmazás hozzájárulásokhoz)
5. Ismered a tananyag struktúráját

Lásd [INSTALLATION.md](INSTALLATION.md) a részletes telepítési útmutatóért.

### Fork és Klónozás

1. **Forkold a repót** GitHubon  
2. **Klónozd a forkodat** helyben:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Add hozzá az upstream távoli repót**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Ág létrehozása

Hozz létre egy új ágat a munkádhoz:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Ágnevezési konvenciók:  
- `feature/` - Új funkciók vagy leckék  
- `fix/` - Hibajavítások  
- `docs/` - Dokumentációs változtatások  
- `refactor/` - Kód átszervezése  

## Hozzájárulási irányelvek

### Leckék tartalmához

Leckék hozzáadásakor vagy meglévők módosításakor:

1. **Kövesd a meglévő struktúrát**:  
   - README.md a lecke tartalmával  
   - Jupyter notebook gyakorlatokkal  
   - Feladat (ha releváns)  
   - Link az előzetes és utólagos kvízekhez  

2. **Tartalmazza az alábbi elemeket**:  
   - Egyértelmű tanulási célok  
   - Lépésről lépésre magyarázatok  
   - Kódpéldák kommentekkel  
   - Gyakorlatok gyakorlásra  
   - Linkek további forrásokhoz  

3. **Biztosítsd az akadálymentességet**:  
   - Használj világos, egyszerű nyelvezetet  
   - Adj meg alternatív szöveget a képekhez  
   - Tartalmazz kódkommenteket  
   - Vedd figyelembe a különböző tanulási stílusokat  

### Jupyter Notebookokhoz

1. **Töröld az összes kimenetet** mielőtt elköteleznéd:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Tartalmazz markdown cellákat** magyarázatokkal  

3. **Használj következetes formázást**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Teszteld teljesen a notebookot** beküldés előtt  

### Python kódhoz

Kövesd a [PEP 8](https://www.python.org/dev/peps/pep-0008/) stílusirányelveket:  
```python
# Good practices
import pandas as pd

def calculate_mean(data):
    """Calculate the mean of a dataset.
    
    Args:
        data (list): List of numerical values
        
    Returns:
        float: Mean of the dataset
    """
    return sum(data) / len(data)
```
  

### Kvíz alkalmazás hozzájárulásokhoz

A kvíz alkalmazás módosításakor:

1. **Teszteld helyben**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Futtasd a lintert**:  
   ```bash
   npm run lint
   ```
  
3. **Építsd sikeresen**:  
   ```bash
   npm run build
   ```
  
4. **Kövesd a Vue.js stílusirányelveket** és meglévő mintákat  

### Fordításokhoz

Fordítások hozzáadásakor vagy frissítésekor:

1. Kövesd a `translations/` mappa struktúráját  
2. Használd a nyelvkódot mappanévként (pl. `fr` francia esetén)  
3. Tartsd meg az angol verzió fájlstruktúráját  
4. Frissítsd a kvíz linkeket, hogy tartalmazzák a nyelvi paramétert: `?loc=fr`  
5. Teszteld az összes linket és formázást  

## Pull Request folyamat

### Beküldés előtt

1. **Frissítsd az ágad** a legújabb változásokkal:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Teszteld a változtatásaidat**:  
   - Futtasd az összes módosított notebookot  
   - Teszteld a kvíz alkalmazást, ha módosítottad  
   - Ellenőrizd az összes link működését  
   - Ellenőrizd a helyesírási és nyelvtani hibákat  

3. **Kötelezd el a változtatásaidat**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Írj egyértelmű commit üzeneteket:  
   - Használj jelen időt ("Funkció hozzáadása" nem "Funkció hozzáadva")  
   - Használj felszólító módot ("Mozgasd a kurzort..." nem "Mozgatja a kurzort...")  
   - Korlátozd az első sort 72 karakterre  
   - Hivatkozz problémákra és pull requestekre, ha releváns  

4. **Pushold a forkodra**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Pull Request létrehozása

1. Lépj a [repo](https://github.com/microsoft/Data-Science-For-Beginners) oldalára  
2. Kattints a "Pull requests" → "New pull request" gombra  
3. Kattints a "compare across forks" gombra  
4. Válaszd ki a forkodat és ágadat  
5. Kattints a "Create pull request" gombra  

### PR cím formátuma

Használj egyértelmű, leíró címeket az alábbi formátumban:  
```
[Component] Brief description
```
  
Példák:  
- `[Lecke 7] Python notebook import hiba javítása`  
- `[Kvíz alkalmazás] Német fordítás hozzáadása`  
- `[Dokumentáció] README frissítése új előfeltételekkel`  
- `[Javítás] Adatútvonal javítása vizualizációs leckében`  

### PR leírás

A PR leírásában szerepeljen:  

- **Mi**: Milyen változtatásokat végeztél?  
- **Miért**: Miért szükségesek ezek a változtatások?  
- **Hogyan**: Hogyan valósítottad meg a változtatásokat?  
- **Tesztelés**: Hogyan tesztelted a változtatásokat?  
- **Képernyőképek**: Mellékelj képernyőképeket vizuális változtatásokhoz  
- **Kapcsolódó problémák**: Hivatkozz kapcsolódó problémákra (pl. "Fixes #123")  

### Áttekintési folyamat

1. **Automatikus ellenőrzések** futnak a PR-eden  
2. **Karbantartók átnézik** a hozzájárulásodat  
3. **Válaszolj a visszajelzésekre** további commitokkal  
4. Ha jóváhagyják, egy **karbantartó összevonja** a PR-t  

### Miután a PR-t összevonták

1. Töröld az ágad:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Frissítsd a forkodat:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Stílusirányelvek

### Markdown

- Használj következetes címsorszinteket  
- Hagyj üres sorokat a szakaszok között  
- Használj kódblokkokat nyelvi specifikációval:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Adj alternatív szöveget a képekhez: `![Alt szöveg](../../translated_images/hu/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`  
- Tartsd a sorhosszokat ésszerű határok között (kb. 80-100 karakter)  

### Python

- Kövesd a PEP 8 stílusirányelveket  
- Használj értelmes változóneveket  
- Adj docstringeket a függvényekhez  
- Használj típusjelzéseket, ahol releváns:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Kövesd a Vue.js 2 stílusirányelveket  
- Használj a megadott ESLint konfigurációt  
- Írj moduláris, újrafelhasználható komponenseket  
- Adj kommenteket a bonyolult logikához  

### Fájlok szervezése

- Tartsd az összefüggő fájlokat együtt  
- Használj leíró fájlneveket  
- Kövesd a meglévő könyvtárstruktúrát  
- Ne kötelezz el felesleges fájlokat (.DS_Store, .pyc, node_modules stb.)  

## Hozzájárulói licencszerződés

Ez a projekt szívesen fogad hozzájárulásokat és javaslatokat. A legtöbb hozzájárulás megköveteli, hogy  
elfogadj egy Hozzájárulói Licencszerződést (CLA), amely kijelenti, hogy jogod van, és ténylegesen megadod nekünk a jogokat a hozzájárulásod felhasználására. Részletekért látogass el a  
https://cla.microsoft.com oldalra.

Amikor pull requestet nyújtasz be, egy CLA-bot automatikusan meghatározza, hogy szükséges-e  
CLA-t biztosítanod, és megfelelően megjelöli a PR-t (pl. címke, megjegyzés). Egyszerűen kövesd a  
bot által megadott utasításokat. Ezt csak egyszer kell megtenned az összes CLA-t használó repó esetében.

## Kérdések?

- Nézd meg a [Discord csatornánkat #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Csatlakozz a [Discord közösségünkhöz](https://aka.ms/ds4beginners/discord)  
- Nézd át a meglévő [problémákat](https://github.com/microsoft/Data-Science-For-Beginners/issues) és [pull requesteket](https://github.com/microsoft/Data-Science-For-Beginners/pulls)  

## Köszönjük!

A hozzájárulásaid jobbá teszik ezt a tananyagot mindenki számára. Köszönjük, hogy időt szánsz a hozzájárulásra!

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.