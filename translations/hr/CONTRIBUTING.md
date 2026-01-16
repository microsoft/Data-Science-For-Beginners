<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:41:49+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hr"
}
-->
# Doprinos Data Science for Beginners

Hvala vam na interesu za doprinos kurikulumu Data Science for Beginners! Pozdravljamo doprinose iz zajednice.

## Sadržaj

- [Kodeks ponašanja](../..)
- [Kako mogu doprinijeti?](../..)
- [Početak rada](../..)
- [Smjernice za doprinos](../..)
- [Proces podnošenja Pull Requesta](../..)
- [Smjernice za stil](../..)
- [Ugovor o licenci za doprinos](../..)

## Kodeks ponašanja

Ovaj projekt usvojio je [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Za više informacija pogledajte [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
ili kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) s dodatnim pitanjima ili komentarima.

## Kako mogu doprinijeti?

### Prijava grešaka

Prije nego što prijavite grešku, provjerite postojeće probleme kako biste izbjegli dupliciranje. Kada prijavljujete grešku, uključite što više detalja:

- **Koristite jasan i opisni naslov**
- **Opišite točne korake za reprodukciju problema**
- **Pružite konkretne primjere** (isječci koda, snimke zaslona)
- **Opišite ponašanje koje ste primijetili i ono što ste očekivali**
- **Uključite detalje o vašem okruženju** (OS, verzija Pythona, preglednik)

### Predlaganje poboljšanja

Prijedlozi za poboljšanja su dobrodošli! Kada predlažete poboljšanja:

- **Koristite jasan i opisni naslov**
- **Pružite detaljan opis predloženog poboljšanja**
- **Objasnite zašto bi ovo poboljšanje bilo korisno**
- **Navedite slične značajke u drugim projektima, ako je primjenjivo**

### Doprinos dokumentaciji

Poboljšanja dokumentacije uvijek su cijenjena:

- **Ispravite pravopisne i gramatičke pogreške**
- **Poboljšajte jasnoću objašnjenja**
- **Dodajte nedostajuću dokumentaciju**
- **Ažurirajte zastarjele informacije**
- **Dodajte primjere ili slučajeve upotrebe**

### Doprinos kodu

Pozdravljamo doprinose kodu, uključujući:

- **Nove lekcije ili vježbe**
- **Ispravke grešaka**
- **Poboljšanja postojećih bilježnica**
- **Nove skupove podataka ili primjere**
- **Poboljšanja aplikacije za kvizove**

## Početak rada

### Preduvjeti

Prije nego što doprinesete, osigurajte da imate:

1. GitHub račun
2. Git instaliran na vašem sustavu
3. Python 3.7+ i Jupyter instaliran
4. Node.js i npm (za doprinose aplikaciji za kvizove)
5. Poznavanje strukture kurikuluma

Pogledajte [INSTALLATION.md](INSTALLATION.md) za detaljne upute o postavljanju.

### Fork i kloniranje

1. **Forkajte repozitorij** na GitHubu
2. **Klonirajte svoj fork** lokalno:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Dodajte upstream remote**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Kreiranje grane

Kreirajte novu granu za svoj rad:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Konvencije za imenovanje grana:
- `feature/` - Nove značajke ili lekcije
- `fix/` - Ispravke grešaka
- `docs/` - Promjene u dokumentaciji
- `refactor/` - Refaktoriranje koda

## Smjernice za doprinos

### Za sadržaj lekcija

Kada doprinosite lekcijama ili mijenjate postojeće:

1. **Pratite postojeću strukturu**:
   - README.md sa sadržajem lekcije
   - Jupyter bilježnica s vježbama
   - Zadatak (ako je primjenjivo)
   - Link na kvizove prije i poslije lekcije

2. **Uključite ove elemente**:
   - Jasni ciljevi učenja
   - Objašnjenja korak po korak
   - Primjeri koda s komentarima
   - Vježbe za praksu
   - Linkovi na dodatne resurse

3. **Osigurajte pristupačnost**:
   - Koristite jasan, jednostavan jezik
   - Pružite alt tekst za slike
   - Uključite komentare u kodu
   - Razmotrite različite stilove učenja

### Za Jupyter bilježnice

1. **Očistite sve izlaze** prije nego što ih pošaljete:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Uključite markdown ćelije** s objašnjenjima

3. **Koristite dosljedno formatiranje**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Testirajte svoju bilježnicu** u potpunosti prije slanja

### Za Python kod

Pratite [PEP 8](https://www.python.org/dev/peps/pep-0008/) smjernice za stil:

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

### Za doprinose aplikaciji za kvizove

Kada mijenjate aplikaciju za kvizove:

1. **Testirajte lokalno**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Pokrenite linter**:
   ```bash
   npm run lint
   ```

3. **Uspješno izgradite**:
   ```bash
   npm run build
   ```

4. **Pratite Vue.js smjernice za stil** i postojeće obrasce

### Za prijevode

Kada dodajete ili ažurirate prijevode:

1. Pratite strukturu u mapi `translations/`
2. Koristite kod jezika kao naziv mape (npr. `fr` za francuski)
3. Održavajte istu strukturu datoteka kao engleska verzija
4. Ažurirajte linkove kvizova da uključuju parametar jezika: `?loc=fr`
5. Testirajte sve linkove i formatiranje

## Proces podnošenja Pull Requesta

### Prije slanja

1. **Ažurirajte svoju granu** s najnovijim promjenama:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Testirajte svoje promjene**:
   - Pokrenite sve izmijenjene bilježnice
   - Testirajte aplikaciju za kvizove ako je izmijenjena
   - Provjerite da svi linkovi rade
   - Provjerite pravopisne i gramatičke pogreške

3. **Pošaljite svoje promjene**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Napišite jasne poruke commit-a:
   - Koristite sadašnje vrijeme ("Dodaj značajku" umjesto "Dodano značajku")
   - Koristite imperativni način ("Pomakni kursor na..." umjesto "Pomakne kursor na...")
   - Ograničite prvu liniju na 72 znaka
   - Referencirajte probleme i pull requestove kada je relevantno

4. **Pushajte na svoj fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Kreiranje Pull Requesta

1. Idite na [repozitorij](https://github.com/microsoft/Data-Science-For-Beginners)
2. Kliknite "Pull requests" → "New pull request"
3. Kliknite "compare across forks"
4. Odaberite svoj fork i granu
5. Kliknite "Create pull request"

### Format naslova PR-a

Koristite jasne, opisne naslove prema ovom formatu:

```
[Component] Brief description
```

Primjeri:
- `[Lekcija 7] Ispravi grešku uvoza u Python bilježnici`
- `[Aplikacija za kvizove] Dodaj prijevod na njemački`
- `[Dokumentacija] Ažuriraj README s novim preduvjetima`
- `[Ispravak] Ispravi putanju podataka u lekciji o vizualizaciji`

### Opis PR-a

Uključite u opis PR-a:

- **Što**: Koje ste promjene napravili?
- **Zašto**: Zašto su ove promjene potrebne?
- **Kako**: Kako ste implementirali promjene?
- **Testiranje**: Kako ste testirali promjene?
- **Snimke zaslona**: Uključite snimke zaslona za vizualne promjene
- **Povezani problemi**: Link na povezane probleme (npr. "Fixes #123")

### Proces pregleda

1. **Automatske provjere** će se pokrenuti na vašem PR-u
2. **Održavatelji će pregledati** vaš doprinos
3. **Odgovorite na povratne informacije** dodavanjem dodatnih commitova
4. Kada bude odobreno, **održavatelj će spojiti** vaš PR

### Nakon što je vaš PR spojen

1. Obrišite svoju granu:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. Ažurirajte svoj fork:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Smjernice za stil

### Markdown

- Koristite dosljedne razine naslova
- Uključite prazne linije između sekcija
- Koristite blokove koda s oznakama jezika:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Dodajte alt tekst slikama: `![Alt tekst](../../translated_images/hr/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`
- Održavajte razumnu duljinu linija (oko 80-100 znakova)

### Python

- Pratite PEP 8 smjernice za stil
- Koristite smislena imena varijabli
- Dodajte docstringove funkcijama
- Uključite tipne oznake gdje je primjenjivo:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Pratite Vue.js 2 smjernice za stil
- Koristite pruženu ESLint konfiguraciju
- Pišite modularne, ponovno upotrebljive komponente
- Dodajte komentare za složenu logiku

### Organizacija datoteka

- Držite povezane datoteke zajedno
- Koristite opisne nazive datoteka
- Pratite postojeću strukturu direktorija
- Nemojte slati nepotrebne datoteke (.DS_Store, .pyc, node_modules, itd.)

## Ugovor o licenci za doprinos

Ovaj projekt pozdravlja doprinose i prijedloge. Većina doprinosa zahtijeva da
pristanete na Ugovor o licenci za doprinos (CLA) kojim izjavljujete da imate pravo,
i zapravo dajete prava za korištenje vašeg doprinosa. Za detalje, posjetite
https://cla.microsoft.com.

Kada pošaljete pull request, CLA-bot će automatski odrediti trebate li
pružiti CLA i označiti PR na odgovarajući način (npr. oznaka, komentar). Jednostavno slijedite
upute koje pruža bot. To ćete morati učiniti samo jednom za sve repozitorije koji koriste naš CLA.

## Pitanja?

- Provjerite naš [Discord kanal #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- Pridružite se našoj [Discord zajednici](https://aka.ms/ds4beginners/discord)
- Pregledajte postojeće [probleme](https://github.com/microsoft/Data-Science-For-Beginners/issues) i [pull requestove](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## Hvala!

Vaši doprinosi čine ovaj kurikulum boljim za sve. Hvala vam što ste odvojili vrijeme za doprinos!

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.