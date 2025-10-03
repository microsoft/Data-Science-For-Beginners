<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:26:18+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sw"
}
-->
# Kuchangia Data Science kwa Kompyuta

Asante kwa nia yako ya kuchangia mtaala wa Data Science kwa Kompyuta! Tunakaribisha michango kutoka kwa jamii.

## Jedwali la Maudhui

- [Kanuni za Maadili](../..)
- [Ninawezaje Kuchangia?](../..)
- [Kuanza](../..)
- [Miongozo ya Michango](../..)
- [Mchakato wa Pull Request](../..)
- [Miongozo ya Mtindo](../..)
- [Mkataba wa Leseni ya Mchangiaji](../..)

## Kanuni za Maadili

Mradi huu umechukua [Kanuni za Maadili za Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/). 
Kwa maelezo zaidi angalia [Maswali Yanayoulizwa Mara kwa Mara kuhusu Kanuni za Maadili](https://opensource.microsoft.com/codeofconduct/faq/) 
au wasiliana na [opencode@microsoft.com](mailto:opencode@microsoft.com) kwa maswali au maoni ya ziada.

## Ninawezaje Kuchangia?

### Kuripoti Hitilafu

Kabla ya kuunda ripoti za hitilafu, tafadhali angalia masuala yaliyopo ili kuepuka nakala. Unapounda ripoti ya hitilafu, jumuisha maelezo mengi iwezekanavyo:

- **Tumia kichwa kilicho wazi na cha kuelezea**
- **Eleza hatua halisi za kuzalisha tatizo**
- **Toa mifano maalum** (vipande vya msimbo, picha za skrini)
- **Eleza tabia uliyotazama na kile ulichotarajia**
- **Jumuisha maelezo ya mazingira yako** (OS, toleo la Python, kivinjari)

### Kupendekeza Uboreshaji

Mapendekezo ya uboreshaji yanakaribishwa! Unapopendekeza uboreshaji:

- **Tumia kichwa kilicho wazi na cha kuelezea**
- **Toa maelezo ya kina ya uboreshaji uliopendekeza**
- **Eleza kwa nini uboreshaji huu ungekuwa muhimu**
- **Orodhesha vipengele vyovyote vinavyofanana katika miradi mingine, ikiwa inafaa**

### Kuchangia kwa Nyaraka

Uboreshaji wa nyaraka unathaminiwa kila wakati:

- **Sahihisha makosa ya tahajia na sarufi**
- **Boresha uwazi wa maelezo**
- **Ongeza nyaraka zinazokosekana**
- **Sasisha maelezo yaliyopitwa na wakati**
- **Ongeza mifano au matumizi**

### Kuchangia Msimbo

Tunakaribisha michango ya msimbo ikijumuisha:

- **Masomo mapya au mazoezi**
- **Marekebisho ya hitilafu**
- **Uboreshaji wa daftari zilizopo**
- **Seti mpya za data au mifano**
- **Uboreshaji wa programu ya maswali**

## Kuanza

### Mahitaji ya Awali

Kabla ya kuchangia, hakikisha una:

1. Akaunti ya GitHub
2. Git imewekwa kwenye mfumo wako
3. Python 3.7+ na Jupyter imewekwa
4. Node.js na npm (kwa michango ya programu ya maswali)
5. Uelewa wa muundo wa mtaala

Angalia [INSTALLATION.md](INSTALLATION.md) kwa maelezo ya kina ya usanidi.

### Fork na Clone

1. **Fork hifadhi** kwenye GitHub
2. **Clone fork yako** kwa ndani:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Ongeza remote ya upstream**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Unda Tawi

Unda tawi jipya kwa kazi yako:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Miongozo ya majina ya matawi:
- `feature/` - Vipengele vipya au masomo
- `fix/` - Marekebisho ya hitilafu
- `docs/` - Mabadiliko ya nyaraka
- `refactor/` - Marekebisho ya msimbo

## Miongozo ya Michango

### Kwa Maudhui ya Masomo

Unapochangia masomo au kurekebisha yaliyopo:

1. **Fuata muundo uliopo**:
   - README.md na maudhui ya somo
   - Daftari la Jupyter na mazoezi
   - Kazi (ikiwa inafaa)
   - Kiungo kwa maswali ya awali na ya baada

2. **Jumuisha vipengele hivi**:
   - Malengo ya kujifunza yaliyo wazi
   - Maelezo ya hatua kwa hatua
   - Mifano ya msimbo na maoni
   - Mazoezi ya mazoezi
   - Viungo kwa rasilimali za ziada

3. **Hakikisha upatikanaji**:
   - Tumia lugha iliyo wazi na rahisi
   - Toa maandishi mbadala kwa picha
   - Jumuisha maoni ya msimbo
   - Fikiria mitindo tofauti ya kujifunza

### Kwa Daftari za Jupyter

1. **Futa matokeo yote** kabla ya kujitolea:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Jumuisha seli za markdown** na maelezo

3. **Tumia muundo thabiti**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Jaribu daftari lako** kikamilifu kabla ya kuwasilisha

### Kwa Msimbo wa Python

Fuata miongozo ya mtindo wa [PEP 8](https://www.python.org/dev/peps/pep-0008/):

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

### Kwa Michango ya Programu ya Maswali

Unapobadilisha programu ya maswali:

1. **Jaribu kwa ndani**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Run linter**:
   ```bash
   npm run lint
   ```

3. **Jenga kwa mafanikio**:
   ```bash
   npm run build
   ```

4. **Fuata mwongozo wa mtindo wa Vue.js** na mifumo iliyopo

### Kwa Tafsiri

Unapoongeza au kusasisha tafsiri:

1. Fuata muundo katika folda ya `translations/`
2. Tumia msimbo wa lugha kama jina la folda (mfano, `fr` kwa Kifaransa)
3. Dumisha muundo sawa wa faili kama toleo la Kiingereza
4. Sasisha viungo vya maswali ili kujumuisha parameter ya lugha: `?loc=fr`
5. Jaribu viungo vyote na muundo

## Mchakato wa Pull Request

### Kabla ya Kuwasilisha

1. **Sasisha tawi lako** na mabadiliko ya hivi karibuni:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Jaribu mabadiliko yako**:
   - Run daftari zote zilizorekebishwa
   - Jaribu programu ya maswali ikiwa imebadilishwa
   - Hakikisha viungo vyote vinafanya kazi
   - Angalia makosa ya tahajia na sarufi

3. **Jitolee mabadiliko yako**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Andika ujumbe wa kujitolea ulio wazi:
   - Tumia wakati wa sasa ("Ongeza kipengele" si "Imeongeza kipengele")
   - Tumia hali ya amri ("Hamisha mshale hadi..." si "Inahamisha mshale hadi...")
   - Punguza mstari wa kwanza hadi herufi 72
   - Rejelea masuala na pull requests inapofaa

4. **Push kwa fork yako**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Kuunda Pull Request

1. Nenda kwenye [hifadhi](https://github.com/microsoft/Data-Science-For-Beginners)
2. Bonyeza "Pull requests" → "New pull request"
3. Bonyeza "compare across forks"
4. Chagua fork yako na tawi
5. Bonyeza "Create pull request"

### Muundo wa Kichwa cha PR

Tumia vichwa vilivyo wazi na vya kuelezea kufuata muundo huu:

```
[Component] Brief description
```

Mifano:
- `[Lesson 7] Rekebisha hitilafu ya uingizaji wa daftari la Python`
- `[Quiz App] Ongeza tafsiri ya Kijerumani`
- `[Docs] Sasisha README na mahitaji mapya`
- `[Fix] Rekebisha njia ya data katika somo la taswira`

### Maelezo ya PR

Jumuisha katika maelezo ya PR yako:

- **Nini**: Mabadiliko gani umefanya?
- **Kwa nini**: Kwa nini mabadiliko haya ni muhimu?
- **Jinsi**: Umefanyaje mabadiliko haya?
- **Upimaji**: Umejaribuje mabadiliko haya?
- **Picha za skrini**: Jumuisha picha za skrini kwa mabadiliko ya kuona
- **Masuala Yanayohusiana**: Kiungo kwa masuala yanayohusiana (mfano, "Fixes #123")

### Mchakato wa Mapitio

1. **Ukaguzi wa kiotomatiki** utaendeshwa kwenye PR yako
2. **Wadumishaji watapitia** mchango wako
3. **Shughulikia maoni** kwa kufanya ahadi za ziada
4. Mara tu imeidhinishwa, **mdumishaji ataunganisha** PR yako

### Baada ya PR Yako Kuunganishwa

1. Futa tawi lako:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. Sasisha fork yako:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Miongozo ya Mtindo

### Markdown

- Tumia viwango thabiti vya vichwa
- Jumuisha mistari tupu kati ya sehemu
- Tumia vizuizi vya msimbo na viainishi vya lugha:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Ongeza maandishi mbadala kwa picha: `![Alt text](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.sw.png)`
- Dumisha urefu wa mistari unaofaa (karibu herufi 80-100)

### Python

- Fuata mwongozo wa mtindo wa PEP 8
- Tumia majina ya kutofautisha ya vigezo
- Ongeza docstrings kwa kazi
- Jumuisha vidokezo vya aina inapofaa:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Fuata mwongozo wa mtindo wa Vue.js 2
- Tumia usanidi wa ESLint uliotolewa
- Andika vipengele vya modular, vinavyoweza kutumika tena
- Ongeza maoni kwa mantiki ngumu

### Mpangilio wa Faili

- Weka faili zinazohusiana pamoja
- Tumia majina ya faili yanayoelezea
- Fuata muundo wa saraka uliopo
- Usijitolee faili zisizo za lazima (.DS_Store, .pyc, node_modules, nk.)

## Mkataba wa Leseni ya Mchangiaji

Mradi huu unakaribisha michango na mapendekezo. Michango mingi inahitaji wewe 
kukubali Mkataba wa Leseni ya Mchangiaji (CLA) unaotangaza kwamba una haki ya, 
na kwa kweli unatoa, haki kwetu kutumia mchango wako. Kwa maelezo, tembelea 
https://cla.microsoft.com.

Unapowasilisha pull request, CLA-bot itaamua kiotomatiki ikiwa unahitaji 
kutoa CLA na kupamba PR ipasavyo (mfano, lebo, maoni). Fuata tu 
maelekezo yaliyotolewa na bot. Utahitaji kufanya hivyo mara moja tu katika hifadhi zote zinazotumia CLA yetu.

## Maswali?

- Angalia [Kituo chetu cha Discord #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- Jiunge na [jamii yetu ya Discord](https://aka.ms/ds4beginners/discord)
- Pitia masuala yaliyopo [issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) na [pull requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## Asante!

Michango yako inafanya mtaala huu kuwa bora kwa kila mtu. Asante kwa kuchukua muda kuchangia!

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo rasmi. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.