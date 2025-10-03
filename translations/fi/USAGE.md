<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:05:09+00:00",
  "source_file": "USAGE.md",
  "language_code": "fi"
}
-->
# Käyttöopas

Tämä opas tarjoaa esimerkkejä ja yleisiä työnkulkuja Data Science for Beginners -opetussuunnitelman käyttöön.

## Sisällysluettelo

- [Kuinka käyttää tätä opetussuunnitelmaa](../..)
- [Työskentely oppituntien kanssa](../..)
- [Työskentely Jupyter Notebooks -ympäristössä](../..)
- [Kyselysovelluksen käyttö](../..)
- [Yleiset työnkulut](../..)
- [Vinkkejä itseopiskelijoille](../..)
- [Vinkkejä opettajille](../..)

## Kuinka käyttää tätä opetussuunnitelmaa

Tämä opetussuunnitelma on joustava ja sitä voi käyttää monin eri tavoin:

- **Itseopiskelu**: Käy oppitunnit läpi itsenäisesti omaan tahtiin
- **Luokkaopetus**: Käytä strukturoituna kurssina ohjatun opetuksen kanssa
- **Opintoryhmät**: Opiskele yhdessä muiden kanssa
- **Työpajamuoto**: Intensiiviset lyhytaikaiset oppimissessiot

## Työskentely oppituntien kanssa

Jokainen oppitunti noudattaa johdonmukaista rakennetta oppimisen maksimoimiseksi:

### Oppitunnin rakenne

1. **Ennakkokysely**: Testaa olemassa olevaa tietämystäsi
2. **Sketchnote** (Valinnainen): Visuaalinen yhteenveto keskeisistä käsitteistä
3. **Video** (Valinnainen): Lisävideomateriaalia
4. **Kirjallinen oppitunti**: Keskeiset käsitteet ja selitykset
5. **Jupyter Notebook**: Käytännön koodausharjoituksia
6. **Tehtävä**: Harjoittele oppimaasi
7. **Jälkikysely**: Vahvista ymmärrystäsi

### Esimerkki oppitunnin työnkulusta

```bash
# 1. Navigate to the lesson directory
cd 1-Introduction/01-defining-data-science

# 2. Read the README.md
# Open README.md in your browser or editor

# 3. Take the pre-lesson quiz
# Click the quiz link in the README

# 4. Open the Jupyter notebook (if available)
jupyter notebook

# 5. Complete the exercises in the notebook

# 6. Work on the assignment

# 7. Take the post-lesson quiz
```

## Työskentely Jupyter Notebooks -ympäristössä

### Jupyterin käynnistäminen

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Notebook-solujen suorittaminen

1. **Suorita solu**: Paina `Shift + Enter` tai napsauta "Run"-painiketta
2. **Suorita kaikki solut**: Valitse "Cell" → "Run All" valikosta
3. **Käynnistä ydin uudelleen**: Valitse "Kernel" → "Restart", jos kohtaat ongelmia

### Esimerkki: Työskentely datan kanssa Notebookissa

```python
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load a dataset
df = pd.read_csv('data/sample.csv')

# Explore the data
df.head()
df.info()
df.describe()

# Create a visualization
plt.figure(figsize=(10, 6))
plt.plot(df['column_name'])
plt.title('Sample Visualization')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```

### Työn tallentaminen

- Jupyter tallentaa automaattisesti säännöllisesti
- Tallenna manuaalisesti: Paina `Ctrl + S` (tai `Cmd + S` macOS:ssä)
- Edistymisesi tallennetaan `.ipynb`-tiedostoon

## Kyselysovelluksen käyttö

### Kyselysovelluksen suorittaminen paikallisesti

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Kyselyiden tekeminen

1. Ennakkokyselyt löytyvät oppituntien alusta
2. Jälkikyselyt löytyvät oppituntien lopusta
3. Jokaisessa kyselyssä on 3 kysymystä
4. Kyselyt on suunniteltu oppimisen vahvistamiseen, ei kattavaan testaukseen

### Kyselyiden numerointi

- Kyselyt on numeroitu 0-39 (yhteensä 40 kyselyä)
- Jokaisessa oppitunnissa on yleensä ennakko- ja jälkikysely
- Kyselyiden URL-osoitteet sisältävät kyselyn numeron: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Yleiset työnkulut

### Työnkulku 1: Täysin aloittelijan polku

```bash
# 1. Set up your environment (see INSTALLATION.md)

# 2. Start with Lesson 1
cd 1-Introduction/01-defining-data-science

# 3. For each lesson:
#    - Take pre-lesson quiz
#    - Read the lesson content
#    - Work through the notebook
#    - Complete the assignment
#    - Take post-lesson quiz

# 4. Progress through all 20 lessons sequentially
```

### Työnkulku 2: Aihekohtainen oppiminen

Jos olet kiinnostunut tietystä aiheesta:

```bash
# Example: Focus on Data Visualization
cd 3-Data-Visualization

# Explore lessons 9-13:
# - Lesson 9: Visualizing Quantities
# - Lesson 10: Visualizing Distributions
# - Lesson 11: Visualizing Proportions
# - Lesson 12: Visualizing Relationships
# - Lesson 13: Meaningful Visualizations
```

### Työnkulku 3: Projektipohjainen oppiminen

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Työnkulku 4: Pilvipohjainen data-analytiikka

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Vinkkejä itseopiskelijoille

### Pysy järjestelmällisenä

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Harjoittele säännöllisesti

- Varaa aikaa päivittäin tai viikoittain
- Suorita vähintään yksi oppitunti viikossa
- Kertaa aiempia oppitunteja säännöllisesti

### Osallistu yhteisöön

- Liity [Discord-yhteisöön](https://aka.ms/ds4beginners/discord)
- Osallistu #Data-Science-for-Beginners-kanavalle Discordissa [Discord-keskustelut](https://aka.ms/ds4beginners/discord)
- Jaa edistymisesi ja kysy kysymyksiä

### Rakenna omia projekteja

Oppituntien suorittamisen jälkeen sovella käsitteitä omiin projekteihin:

```python
# Example: Analyze your own dataset
import pandas as pd

# Load your own data
my_data = pd.read_csv('my-project/data.csv')

# Apply techniques learned
# - Data cleaning (Lesson 8)
# - Exploratory data analysis (Lesson 7)
# - Visualization (Lessons 9-13)
# - Analysis (Lesson 15)
```

## Vinkkejä opettajille

### Luokkahuoneen valmistelu

1. Tutustu [for-teachers.md](for-teachers.md) -tiedostoon yksityiskohtaisia ohjeita varten
2. Aseta yhteinen ympäristö (GitHub Classroom tai Codespaces)
3. Perusta viestintäkanava (Discord, Slack tai Teams)

### Oppituntien suunnittelu

**Ehdotettu 10 viikon aikataulu:**

- **Viikot 1-2**: Johdanto (Oppitunnit 1-4)
- **Viikot 3-4**: Työskentely datan kanssa (Oppitunnit 5-8)
- **Viikot 5-6**: Datavisualisointi (Oppitunnit 9-13)
- **Viikot 7-8**: Data-analytiikan elinkaari (Oppitunnit 14-16)
- **Viikko 9**: Pilvipohjainen data-analytiikka (Oppitunnit 17-19)
- **Viikko 10**: Reaaliaikaiset sovellukset ja lopputyöt (Oppitunti 20)

### Docsifyn suorittaminen offline-tilassa

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Tehtävien arviointi

- Tarkista opiskelijoiden notebookit suoritetuista harjoituksista
- Arvioi ymmärrystä kyselytulosten perusteella
- Arvioi lopputyöt data-analytiikan elinkaaren periaatteiden mukaan

### Tehtävien luominen

```python
# Example custom assignment template
"""
Assignment: [Topic]

Objective: [Learning goal]

Dataset: [Provide or have students find one]

Tasks:
1. Load and explore the dataset
2. Clean and prepare the data
3. Create at least 3 visualizations
4. Perform analysis
5. Communicate findings

Deliverables:
- Jupyter notebook with code and explanations
- Written summary of findings
"""
```

## Työskentely offline-tilassa

### Lataa resurssit

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Suorita dokumentaatio paikallisesti

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Suorita kyselysovellus paikallisesti

```bash
cd quiz-app
npm run serve
```

## Käännetyn sisällön käyttö

Käännökset ovat saatavilla yli 40 kielellä:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Jokainen käännös säilyttää saman rakenteen kuin englanninkielinen versio.

## Lisäresurssit

### Jatka oppimista

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Lisäoppimispolkuja
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Resursseja opiskelijoille
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Yhteisöfoorumi

### Liittyvät opetussuunnitelmat

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Apua saatavilla

- Tarkista [TROUBLESHOOTING.md](TROUBLESHOOTING.md) yleisiä ongelmia varten
- Etsi [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Liity [Discordiin](https://aka.ms/ds4beginners/discord)
- Tutustu [CONTRIBUTING.md](CONTRIBUTING.md) raportoidaksesi ongelmia tai osallistuaksesi

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.