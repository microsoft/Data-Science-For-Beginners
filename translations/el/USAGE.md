<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:02:48+00:00",
  "source_file": "USAGE.md",
  "language_code": "el"
}
-->
# Οδηγός Χρήσης

Αυτός ο οδηγός παρέχει παραδείγματα και κοινές ροές εργασίας για τη χρήση του προγράμματος σπουδών "Data Science for Beginners".

## Πίνακας Περιεχομένων

- [Πώς να Χρησιμοποιήσετε Αυτό το Πρόγραμμα Σπουδών](../..)
- [Εργασία με Μαθήματα](../..)
- [Εργασία με Jupyter Notebooks](../..)
- [Χρήση της Εφαρμογής Κουίζ](../..)
- [Κοινές Ροές Εργασίας](../..)
- [Συμβουλές για Αυτοδίδακτους](../..)
- [Συμβουλές για Δασκάλους](../..)

## Πώς να Χρησιμοποιήσετε Αυτό το Πρόγραμμα Σπουδών

Αυτό το πρόγραμμα σπουδών έχει σχεδιαστεί για να είναι ευέλικτο και μπορεί να χρησιμοποιηθεί με πολλούς τρόπους:

- **Αυτοκαθοδηγούμενη μάθηση**: Εργαστείτε ανεξάρτητα με τα μαθήματα με τον δικό σας ρυθμό
- **Διδασκαλία στην τάξη**: Χρησιμοποιήστε το ως δομημένο μάθημα με καθοδηγούμενη διδασκαλία
- **Ομάδες μελέτης**: Μάθετε συνεργατικά με συναδέλφους
- **Μορφή εργαστηρίου**: Εντατικές συνεδρίες μάθησης μικρής διάρκειας

## Εργασία με Μαθήματα

Κάθε μάθημα ακολουθεί μια συνεπή δομή για τη μέγιστη μάθηση:

### Δομή Μαθήματος

1. **Κουίζ πριν το μάθημα**: Δοκιμάστε τις υπάρχουσες γνώσεις σας
2. **Σχεδιάγραμμα** (Προαιρετικό): Οπτική περίληψη βασικών εννοιών
3. **Βίντεο** (Προαιρετικό): Συμπληρωματικό βίντεο περιεχόμενο
4. **Γραπτό Μάθημα**: Βασικές έννοιες και εξηγήσεις
5. **Jupyter Notebook**: Ασκήσεις προγραμματισμού
6. **Εργασία**: Εξασκηθείτε σε όσα μάθατε
7. **Κουίζ μετά το μάθημα**: Ενισχύστε την κατανόησή σας

### Παράδειγμα Ροής Εργασίας για ένα Μάθημα

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

## Εργασία με Jupyter Notebooks

### Ξεκινώντας το Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Εκτέλεση Κελιών Notebook

1. **Εκτέλεση κελιού**: Πατήστε `Shift + Enter` ή κάντε κλικ στο κουμπί "Run"
2. **Εκτέλεση όλων των κελιών**: Επιλέξτε "Cell" → "Run All" από το μενού
3. **Επανεκκίνηση πυρήνα**: Επιλέξτε "Kernel" → "Restart" αν αντιμετωπίσετε προβλήματα

### Παράδειγμα: Εργασία με Δεδομένα σε Notebook

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

### Αποθήκευση της Εργασίας σας

- Το Jupyter αποθηκεύει αυτόματα περιοδικά
- Χειροκίνητη αποθήκευση: Πατήστε `Ctrl + S` (ή `Cmd + S` σε macOS)
- Η πρόοδός σας αποθηκεύεται στο αρχείο `.ipynb`

## Χρήση της Εφαρμογής Κουίζ

### Εκτέλεση της Εφαρμογής Κουίζ Τοπικά

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Συμμετοχή σε Κουίζ

1. Τα κουίζ πριν το μάθημα συνδέονται στην αρχή κάθε μαθήματος
2. Τα κουίζ μετά το μάθημα συνδέονται στο τέλος κάθε μαθήματος
3. Κάθε κουίζ έχει 3 ερωτήσεις
4. Τα κουίζ έχουν σχεδιαστεί για να ενισχύουν τη μάθηση, όχι για εξαντλητική αξιολόγηση

### Αρίθμηση Κουίζ

- Τα κουίζ αριθμούνται από 0-39 (40 συνολικά κουίζ)
- Κάθε μάθημα συνήθως έχει ένα κουίζ πριν και μετά
- Οι διευθύνσεις URL των κουίζ περιλαμβάνουν τον αριθμό του κουίζ: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Κοινές Ροές Εργασίας

### Ροή Εργασίας 1: Διαδρομή για Απόλυτους Αρχάριους

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

### Ροή Εργασίας 2: Μάθηση με Ειδικό Θέμα

Αν σας ενδιαφέρει ένα συγκεκριμένο θέμα:

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

### Ροή Εργασίας 3: Μάθηση με Βάση Έργα

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Ροή Εργασίας 4: Επιστήμη Δεδομένων στο Cloud

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Συμβουλές για Αυτοδίδακτους

### Οργανωθείτε

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Εξασκηθείτε Τακτικά

- Αφιερώστε συγκεκριμένο χρόνο κάθε μέρα ή εβδομάδα
- Ολοκληρώστε τουλάχιστον ένα μάθημα την εβδομάδα
- Επανεξετάστε προηγούμενα μαθήματα περιοδικά

### Εμπλακείτε με την Κοινότητα

- Γίνετε μέλος της [κοινότητας Discord](https://aka.ms/ds4beginners/discord)
- Συμμετέχετε στο κανάλι #Data-Science-for-Beginners στο Discord [Συζητήσεις Discord](https://aka.ms/ds4beginners/discord)
- Μοιραστείτε την πρόοδό σας και κάντε ερωτήσεις

### Δημιουργήστε Δικά σας Έργα

Αφού ολοκληρώσετε τα μαθήματα, εφαρμόστε τις έννοιες σε προσωπικά έργα:

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

## Συμβουλές για Δασκάλους

### Ρύθμιση Τάξης

1. Ανατρέξτε στο [for-teachers.md](for-teachers.md) για λεπτομερείς οδηγίες
2. Ρυθμίστε ένα κοινό περιβάλλον (GitHub Classroom ή Codespaces)
3. Δημιουργήστε ένα κανάλι επικοινωνίας (Discord, Slack ή Teams)

### Σχεδιασμός Μαθημάτων

**Προτεινόμενο Πρόγραμμα 10 Εβδομάδων:**

- **Εβδομάδα 1-2**: Εισαγωγή (Μαθήματα 1-4)
- **Εβδομάδα 3-4**: Εργασία με Δεδομένα (Μαθήματα 5-8)
- **Εβδομάδα 5-6**: Οπτικοποίηση Δεδομένων (Μαθήματα 9-13)
- **Εβδομάδα 7-8**: Κύκλος Ζωής Επιστήμης Δεδομένων (Μαθήματα 14-16)
- **Εβδομάδα 9**: Επιστήμη Δεδομένων στο Cloud (Μαθήματα 17-19)
- **Εβδομάδα 10**: Εφαρμογές στον Πραγματικό Κόσμο & Τελικά Έργα (Μάθημα 20)

### Εκτέλεση του Docsify για Πρόσβαση Χωρίς Σύνδεση

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Βαθμολόγηση Εργασιών

- Ελέγξτε τα notebooks των μαθητών για ολοκληρωμένες ασκήσεις
- Ελέγξτε την κατανόηση μέσω των βαθμολογιών κουίζ
- Αξιολογήστε τα τελικά έργα χρησιμοποιώντας τις αρχές του κύκλου ζωής της επιστήμης δεδομένων

### Δημιουργία Εργασιών

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

## Εργασία Χωρίς Σύνδεση

### Λήψη Πόρων

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Εκτέλεση Τεκμηρίωσης Τοπικά

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Εκτέλεση Εφαρμογής Κουίζ Τοπικά

```bash
cd quiz-app
npm run serve
```

## Πρόσβαση σε Μεταφρασμένο Περιεχόμενο

Οι μεταφράσεις είναι διαθέσιμες σε 40+ γλώσσες:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Κάθε μετάφραση διατηρεί την ίδια δομή με την αγγλική έκδοση.

## Πρόσθετοι Πόροι

### Συνεχίστε τη Μάθηση

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Πρόσθετες διαδρομές μάθησης
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Πόροι για μαθητές
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Φόρουμ κοινότητας

### Σχετικά Προγράμματα Σπουδών

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Λήψη Βοήθειας

- Ελέγξτε το [TROUBLESHOOTING.md](TROUBLESHOOTING.md) για κοινά προβλήματα
- Αναζητήστε [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Γίνετε μέλος του [Discord](https://aka.ms/ds4beginners/discord)
- Ανατρέξτε στο [CONTRIBUTING.md](CONTRIBUTING.md) για να αναφέρετε προβλήματα ή να συνεισφέρετε

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.