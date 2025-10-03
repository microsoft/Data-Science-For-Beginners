<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:28:33+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "fr"
}
-->
# Guide de dépannage

Ce guide propose des solutions aux problèmes courants que vous pourriez rencontrer en travaillant avec le programme Data Science for Beginners.

## Table des matières

- [Problèmes avec Python et Jupyter](../..)
- [Problèmes de packages et dépendances](../..)
- [Problèmes avec Jupyter Notebook](../..)
- [Problèmes avec l'application de quiz](../..)
- [Problèmes avec Git et GitHub](../..)
- [Problèmes avec la documentation Docsify](../..)
- [Problèmes de données et fichiers](../..)
- [Problèmes de performance](../..)
- [Obtenir de l'aide supplémentaire](../..)

## Problèmes avec Python et Jupyter

### Python introuvable ou mauvaise version

**Problème :** `python: command not found` ou mauvaise version de Python

**Solution :**

```bash
# Check Python version
python --version
python3 --version

# If Python 3 is installed as 'python3', create an alias
# On macOS/Linux, add to ~/.bashrc or ~/.zshrc:
alias python=python3
alias pip=pip3

# Or use python3 explicitly
python3 -m pip install jupyter
```

**Solution pour Windows :**
1. Réinstallez Python depuis [python.org](https://www.python.org/)
2. Pendant l'installation, cochez "Add Python to PATH"
3. Redémarrez votre terminal/ligne de commande

### Problèmes d'activation de l'environnement virtuel

**Problème :** L'environnement virtuel ne s'active pas

**Solution :**

**Windows :**
```bash
# If you get execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

**macOS/Linux :**
```bash
# Ensure the activate script is executable
chmod +x venv/bin/activate

# Then activate
source venv/bin/activate
```

**Vérifiez l'activation :**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Problèmes de kernel Jupyter

**Problème :** "Kernel introuvable" ou "Kernel cesse de fonctionner"

**Solution :**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problème :** Mauvaise version de Python dans Jupyter

**Solution :**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Problèmes de packages et dépendances

### Erreurs d'importation

**Problème :** `ModuleNotFoundError: No module named 'pandas'` (ou autres packages)

**Solution :**

```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install missing package
pip install pandas

# Install all common packages
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

# Verify installation
python -c "import pandas; print(pandas.__version__)"
```

### Échecs d'installation avec pip

**Problème :** `pip install` échoue avec des erreurs de permission

**Solution :**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problème :** `pip install` échoue avec des erreurs de certificat SSL

**Solution :**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Conflits de versions de packages

**Problème :** Versions de packages incompatibles

**Solution :**

```bash
# Create fresh virtual environment
python -m venv venv-new
source venv-new/bin/activate  # or venv-new\Scripts\activate on Windows

# Install packages with specific versions if needed
pip install pandas==1.3.0
pip install numpy==1.21.0

# Or let pip resolve dependencies
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

## Problèmes avec Jupyter Notebook

### Jupyter ne démarre pas

**Problème :** La commande `jupyter notebook` est introuvable

**Solution :**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Le notebook ne se charge pas ou ne se sauvegarde pas

**Problème :** "Notebook failed to load" ou erreurs de sauvegarde

**Solution :**

1. Vérifiez les permissions des fichiers
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Vérifiez la corruption des fichiers
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Effacez le cache de Jupyter
```bash
jupyter notebook --clear-cache
```

### Les cellules ne s'exécutent pas

**Problème :** Cellule bloquée sur "In [*]" ou prend trop de temps

**Solution :**

1. **Interrompez le kernel** : Cliquez sur le bouton "Interrupt" ou appuyez sur `I, I`
2. **Redémarrez le kernel** : Menu Kernel → Restart
3. **Vérifiez les boucles infinies** dans votre code
4. **Effacez les sorties** : Cell → All Output → Clear

### Les graphiques ne s'affichent pas

**Problème :** Les graphiques `matplotlib` ne s'affichent pas dans le notebook

**Solution :**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternative pour des graphiques interactifs :**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Problèmes avec l'application de quiz

### Échec de npm install

**Problème :** Erreurs pendant `npm install`

**Solution :**

```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install

# If still failing, try with legacy peer deps
npm install --legacy-peer-deps
```

### L'application de quiz ne démarre pas

**Problème :** `npm run serve` échoue

**Solution :**

```bash
# Check Node.js version
node --version  # Should be 12.x or higher

# Reinstall dependencies
cd quiz-app
rm -rf node_modules package-lock.json
npm install

# Try different port
npm run serve -- --port 8081
```

### Port déjà utilisé

**Problème :** "Port 8080 is already in use"

**Solution :**

```bash
# Find and kill process on port 8080
# macOS/Linux:
lsof -ti:8080 | xargs kill -9

# Windows:
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# Or use a different port
npm run serve -- --port 8081
```

### Le quiz ne se charge pas ou affiche une page blanche

**Problème :** L'application de quiz se charge mais affiche une page blanche

**Solution :**

1. Vérifiez les erreurs dans la console du navigateur (F12)
2. Effacez le cache et les cookies du navigateur
3. Essayez un autre navigateur
4. Assurez-vous que JavaScript est activé
5. Vérifiez si des bloqueurs de publicité interfèrent

```bash
# Rebuild the app
npm run build
npm run serve
```

## Problèmes avec Git et GitHub

### Git non reconnu

**Problème :** `git: command not found`

**Solution :**

**Windows :**
- Installez Git depuis [git-scm.com](https://git-scm.com/)
- Redémarrez le terminal après l'installation

**macOS :**

> **Note :** Si vous n'avez pas Homebrew installé, suivez les instructions sur [https://brew.sh/](https://brew.sh/) pour l'installer d'abord.
```bash
# Install via Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

**Linux :**
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo dnf install git      # Fedora
```

### Échec du clonage

**Problème :** `git clone` échoue avec des erreurs d'authentification

**Solution :**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permission refusée (publickey)

**Problème :** L'authentification par clé SSH échoue

**Solution :**

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add key to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Add public key to GitHub
# Copy key: cat ~/.ssh/id_ed25519.pub
# Add at: https://github.com/settings/keys
```

## Problèmes avec la documentation Docsify

### Commande Docsify introuvable

**Problème :** `docsify: command not found`

**Solution :**

```bash
# Install globally
npm install -g docsify-cli

# If permission error on macOS/Linux
sudo npm install -g docsify-cli

# Verify installation
docsify --version

# If still not found, add npm global path
# Find npm global path
npm config get prefix

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$PATH:/usr/local/bin"
```

### La documentation ne se charge pas

**Problème :** Docsify fonctionne mais le contenu ne se charge pas

**Solution :**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Les images ne s'affichent pas

**Problème :** Les images affichent une icône de lien cassé

**Solution :**

1. Vérifiez que les chemins des images sont relatifs
2. Assurez-vous que les fichiers d'image existent dans le dépôt
3. Effacez le cache du navigateur
4. Vérifiez que les extensions de fichiers correspondent (sensible à la casse sur certains systèmes)

## Problèmes de données et fichiers

### Erreurs de fichier introuvable

**Problème :** `FileNotFoundError` lors du chargement des données

**Solution :**

```python
import os

# Check current working directory
print(os.getcwd())

# Use absolute path
data_path = os.path.join(os.getcwd(), 'data', 'filename.csv')
df = pd.read_csv(data_path)

# Or use relative path from notebook location
df = pd.read_csv('../data/filename.csv')

# Verify file exists
print(os.path.exists('data/filename.csv'))
```

### Erreurs de lecture de CSV

**Problème :** Erreurs lors de la lecture des fichiers CSV

**Solution :**

```python
import pandas as pd

# Try different encodings
df = pd.read_csv('file.csv', encoding='utf-8')
# or
df = pd.read_csv('file.csv', encoding='latin-1')
# or
df = pd.read_csv('file.csv', encoding='ISO-8859-1')

# Handle missing values
df = pd.read_csv('file.csv', na_values=['NA', 'N/A', ''])

# Specify delimiter if not comma
df = pd.read_csv('file.csv', delimiter=';')
```

### Erreurs de mémoire avec de grands ensembles de données

**Problème :** `MemoryError` lors du chargement de grands fichiers

**Solution :**

```python
# Read in chunks
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Process chunk
    chunks.append(chunk)
df = pd.concat(chunks)

# Or read specific columns only
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])

# Use more efficient data types
df = pd.read_csv('file.csv', dtype={'column_name': 'int32'})
```

## Problèmes de performance

### Performance lente des notebooks

**Problème :** Les notebooks fonctionnent très lentement

**Solution :**

1. **Redémarrez le kernel et effacez les sorties**
   - Kernel → Restart & Clear Output

2. **Fermez les notebooks inutilisés**

3. **Optimisez le code :**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Échantillonnez les grands ensembles de données :**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Plantages du navigateur

**Problème :** Le navigateur plante ou devient non réactif

**Solution :**

1. Fermez les onglets inutilisés
2. Effacez le cache du navigateur
3. Augmentez la mémoire du navigateur (Chrome : `chrome://settings/system`)
4. Utilisez JupyterLab à la place :
```bash
pip install jupyterlab
jupyter lab
```

## Obtenir de l'aide supplémentaire

### Avant de demander de l'aide

1. Consultez ce guide de dépannage
2. Recherchez dans [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Consultez [INSTALLATION.md](INSTALLATION.md) et [USAGE.md](USAGE.md)
4. Essayez de rechercher le message d'erreur en ligne

### Comment demander de l'aide

Lorsque vous créez un problème ou demandez de l'aide, incluez :

1. **Système d'exploitation** : Windows, macOS ou Linux (quelle distribution)
2. **Version de Python** : Exécutez `python --version`
3. **Message d'erreur** : Copiez le message d'erreur complet
4. **Étapes pour reproduire** : Ce que vous avez fait avant que l'erreur ne se produise
5. **Ce que vous avez essayé** : Solutions que vous avez déjà tentées

**Exemple :**
```
**Operating System:** macOS 12.0
**Python Version:** 3.9.7
**Error Message:** ModuleNotFoundError: No module named 'pandas'
**Steps to Reproduce:**
1. Activated virtual environment
2. Started Jupyter notebook
3. Tried to import pandas

**What I've Tried:**
- Ran pip install pandas
- Restarted Jupyter
```

### Ressources communautaires

- **GitHub Issues** : [Créer un problème](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord** : [Rejoignez notre communauté](https://aka.ms/ds4beginners/discord)
- **Discussions** : [Discussions GitHub](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn** : [Forums de questions/réponses](https://docs.microsoft.com/answers/)

### Documentation associée

- [INSTALLATION.md](INSTALLATION.md) - Instructions d'installation
- [USAGE.md](USAGE.md) - Comment utiliser le programme
- [CONTRIBUTING.md](CONTRIBUTING.md) - Comment contribuer
- [README.md](README.md) - Aperçu du projet

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.