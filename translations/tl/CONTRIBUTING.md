<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:24:07+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tl"
}
-->
# Pag-aambag sa Data Science para sa mga Nagsisimula

Salamat sa iyong interes na mag-ambag sa kurikulum ng Data Science para sa mga Nagsisimula! Bukas kami sa mga kontribusyon mula sa komunidad.

## Talaan ng Nilalaman

- [Code of Conduct](../..)
- [Paano Ako Makakapag-ambag?](../..)
- [Pagsisimula](../..)
- [Mga Alituntunin sa Pag-aambag](../..)
- [Proseso ng Pull Request](../..)
- [Mga Alituntunin sa Estilo](../..)
- [Kasunduan sa Lisensya ng Kontribyutor](../..)

## Code of Conduct

Ang proyektong ito ay gumagamit ng [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Para sa karagdagang impormasyon, tingnan ang [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
o makipag-ugnayan sa [opencode@microsoft.com](mailto:opencode@microsoft.com) para sa anumang karagdagang tanong o komento.

## Paano Ako Makakapag-ambag?

### Pag-uulat ng Mga Bug

Bago gumawa ng ulat ng bug, mangyaring suriin ang mga umiiral na isyu upang maiwasan ang mga duplicate. Kapag gumagawa ng ulat ng bug, isama ang mas maraming detalye hangga't maaari:

- **Gumamit ng malinaw at deskriptibong pamagat**
- **Ilarawan ang eksaktong mga hakbang upang maulit ang problema**
- **Magbigay ng mga tiyak na halimbawa** (mga code snippet, screenshot)
- **Ilarawan ang napansin mong pag-uugali at ang inaasahan mo**
- **Isama ang mga detalye ng iyong kapaligiran** (OS, bersyon ng Python, browser)

### Pagsasagawa ng Mga Mungkahi

Malugod naming tinatanggap ang mga mungkahi para sa pagpapabuti! Kapag nagmumungkahi ng mga enhancement:

- **Gumamit ng malinaw at deskriptibong pamagat**
- **Magbigay ng detalyadong paglalarawan ng mungkahi**
- **Ipaliwanag kung bakit magiging kapaki-pakinabang ang enhancement na ito**
- **Banggitin ang anumang katulad na tampok sa ibang mga proyekto, kung naaangkop**

### Pag-aambag sa Dokumentasyon

Palaging pinahahalagahan ang mga pagpapabuti sa dokumentasyon:

- **Ayusin ang mga typo at gramatikal na error**
- **Pagandahin ang kalinawan ng mga paliwanag**
- **Magdagdag ng nawawalang dokumentasyon**
- **I-update ang mga lumang impormasyon**
- **Magdagdag ng mga halimbawa o use case**

### Pag-aambag ng Code

Malugod naming tinatanggap ang mga kontribusyon sa code kabilang ang:

- **Mga bagong aralin o ehersisyo**
- **Pag-aayos ng mga bug**
- **Pagpapabuti sa mga umiiral na notebook**
- **Mga bagong dataset o halimbawa**
- **Mga enhancement sa quiz application**

## Pagsisimula

### Mga Kinakailangan

Bago mag-ambag, tiyakin na mayroon ka ng:

1. Isang GitHub account
2. Git na naka-install sa iyong sistema
3. Python 3.7+ at Jupyter na naka-install
4. Node.js at npm (para sa mga kontribusyon sa quiz app)
5. Pamilyar sa istruktura ng kurikulum

Tingnan ang [INSTALLATION.md](INSTALLATION.md) para sa detalyadong mga tagubilin sa setup.

### Fork at Clone

1. **I-fork ang repository** sa GitHub
2. **I-clone ang iyong fork** nang lokal:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Magdagdag ng upstream remote**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Gumawa ng Branch

Gumawa ng bagong branch para sa iyong trabaho:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Mga convention sa pangalan ng branch:
- `feature/` - Mga bagong tampok o aralin
- `fix/` - Pag-aayos ng mga bug
- `docs/` - Mga pagbabago sa dokumentasyon
- `refactor/` - Pag-refactor ng code

## Mga Alituntunin sa Pag-aambag

### Para sa Nilalaman ng Aralin

Kapag nag-aambag ng mga aralin o binabago ang mga umiiral na:

1. **Sundin ang umiiral na istruktura**:
   - README.md na may nilalaman ng aralin
   - Jupyter notebook na may mga ehersisyo
   - Assignment (kung naaangkop)
   - Link sa pre at post quizzes

2. **Isama ang mga elementong ito**:
   - Malinaw na layunin sa pag-aaral
   - Hakbang-hakbang na mga paliwanag
   - Mga halimbawa ng code na may mga komento
   - Mga ehersisyo para sa pagsasanay
   - Mga link sa karagdagang mapagkukunan

3. **Tiyakin ang accessibility**:
   - Gumamit ng malinaw, simpleng wika
   - Magbigay ng alt text para sa mga larawan
   - Isama ang mga komento sa code
   - Isaalang-alang ang iba't ibang estilo ng pag-aaral

### Para sa Jupyter Notebooks

1. **I-clear ang lahat ng output** bago mag-commit:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Isama ang mga markdown cell** na may mga paliwanag

3. **Gumamit ng pare-parehong format**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Subukan ang iyong notebook** nang buo bago isumite

### Para sa Python Code

Sundin ang [PEP 8](https://www.python.org/dev/peps/pep-0008/) na mga alituntunin sa estilo:

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

### Para sa Mga Kontribusyon sa Quiz App

Kapag binabago ang quiz application:

1. **Subukan nang lokal**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Patakbuhin ang linter**:
   ```bash
   npm run lint
   ```

3. **Mag-build nang matagumpay**:
   ```bash
   npm run build
   ```

4. **Sundin ang Vue.js style guide** at umiiral na mga pattern

### Para sa Mga Pagsasalin

Kapag nagdaragdag o nag-a-update ng mga pagsasalin:

1. Sundin ang istruktura sa folder na `translations/`
2. Gamitin ang code ng wika bilang pangalan ng folder (hal., `fr` para sa French)
3. Panatilihin ang parehong istruktura ng file tulad ng bersyong Ingles
4. I-update ang mga link ng quiz upang isama ang parameter ng wika: `?loc=fr`
5. Subukan ang lahat ng link at format

## Proseso ng Pull Request

### Bago Isumite

1. **I-update ang iyong branch** gamit ang pinakabagong mga pagbabago:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Subukan ang iyong mga pagbabago**:
   - Patakbuhin ang lahat ng binagong notebook
   - Subukan ang quiz app kung binago
   - Tiyakin na gumagana ang lahat ng link
   - Suriin ang spelling at gramatika

3. **I-commit ang iyong mga pagbabago**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Sumulat ng malinaw na mga mensahe ng commit:
   - Gumamit ng present tense ("Magdagdag ng tampok" hindi "Nagdagdag ng tampok")
   - Gumamit ng imperative mood ("Ilipat ang cursor sa..." hindi "Inililipat ang cursor sa...")
   - Limitahan ang unang linya sa 72 karakter
   - Banggitin ang mga isyu at pull request kung naaangkop

4. **I-push sa iyong fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Paglikha ng Pull Request

1. Pumunta sa [repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. I-click ang "Pull requests" → "New pull request"
3. I-click ang "compare across forks"
4. Piliin ang iyong fork at branch
5. I-click ang "Create pull request"

### Format ng Pamagat ng PR

Gumamit ng malinaw, deskriptibong pamagat na sumusunod sa format na ito:

```
[Component] Brief description
```

Mga halimbawa:
- `[Lesson 7] Ayusin ang error sa import ng Python notebook`
- `[Quiz App] Magdagdag ng German na pagsasalin`
- `[Docs] I-update ang README na may bagong mga kinakailangan`
- `[Fix] Itama ang landas ng data sa aralin ng visualization`

### Deskripsyon ng PR

Isama sa iyong deskripsyon ng PR:

- **Ano**: Anong mga pagbabago ang ginawa mo?
- **Bakit**: Bakit kinakailangan ang mga pagbabagong ito?
- **Paano**: Paano mo ipinatupad ang mga pagbabago?
- **Pagsubok**: Paano mo sinubukan ang mga pagbabago?
- **Mga Screenshot**: Isama ang mga screenshot para sa mga visual na pagbabago
- **Mga Kaugnay na Isyu**: I-link ang mga kaugnay na isyu (hal., "Fixes #123")

### Proseso ng Review

1. **Automated checks** ang tatakbo sa iyong PR
2. **Susuriin ng mga maintainer** ang iyong kontribusyon
3. **Tugunan ang feedback** sa pamamagitan ng paggawa ng karagdagang mga commit
4. Kapag naaprubahan, **i-merge ng maintainer** ang iyong PR

### Pagkatapos Ma-merge ang Iyong PR

1. Tanggalin ang iyong branch:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. I-update ang iyong fork:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Mga Alituntunin sa Estilo

### Markdown

- Gumamit ng pare-parehong antas ng heading
- Isama ang mga blankong linya sa pagitan ng mga seksyon
- Gumamit ng mga code block na may mga specifier ng wika:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Magdagdag ng alt text sa mga larawan: `![Alt text](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.tl.png)`
- Panatilihin ang makatwirang haba ng linya (mga 80-100 karakter)

### Python

- Sundin ang PEP 8 style guide
- Gumamit ng makabuluhang pangalan ng variable
- Magdagdag ng mga docstring sa mga function
- Isama ang mga type hint kung naaangkop:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Sundin ang Vue.js 2 style guide
- Gumamit ng ESLint configuration na ibinigay
- Sumulat ng modular, reusable na mga component
- Magdagdag ng mga komento para sa kumplikadong lohika

### Organisasyon ng File

- Panatilihin ang magkakaugnay na mga file na magkakasama
- Gumamit ng deskriptibong pangalan ng file
- Sundin ang umiiral na istruktura ng direktoryo
- Huwag mag-commit ng mga hindi kinakailangang file (.DS_Store, .pyc, node_modules, atbp.)

## Kasunduan sa Lisensya ng Kontribyutor

Malugod na tinatanggap ng proyektong ito ang mga kontribusyon at mungkahi. Karamihan sa mga kontribusyon ay nangangailangan sa iyo na
sumang-ayon sa isang Contributor License Agreement (CLA) na nagsasaad na mayroon kang karapatang,
at aktwal na ginagawa, ibigay sa amin ang mga karapatan na gamitin ang iyong kontribusyon. Para sa mga detalye, bisitahin ang
https://cla.microsoft.com.

Kapag nagsumite ka ng pull request, awtomatikong matutukoy ng CLA-bot kung kailangan mong
magbigay ng CLA at palamutihan ang PR nang naaangkop (hal., label, komento). Sundin lamang ang
mga tagubilin na ibinigay ng bot. Kailangan mo lamang gawin ito nang isang beses sa lahat ng mga repository na gumagamit ng aming CLA.

## Mga Tanong?

- Suriin ang aming [Discord Channel #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- Sumali sa aming [Discord community](https://aka.ms/ds4beginners/discord)
- Suriin ang mga umiiral na [issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) at [pull requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## Salamat!

Ang iyong mga kontribusyon ay nagpapabuti sa kurikulum para sa lahat. Salamat sa paglalaan ng oras upang mag-ambag!

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.