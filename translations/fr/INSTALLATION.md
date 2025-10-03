<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:13:41+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "fr"
}
-->
# Guide d'installation

Ce guide vous aidera à configurer votre environnement pour travailler avec le programme "Data Science for Beginners".

## Table des matières

- [Prérequis](../..)
- [Options de démarrage rapide](../..)
- [Installation locale](../..)
- [Vérifiez votre installation](../..)

## Prérequis

Avant de commencer, vous devez avoir :

- Une connaissance de base de la ligne de commande/terminal
- Un compte GitHub (gratuit)
- Une connexion internet stable pour la configuration initiale

## Options de démarrage rapide

### Option 1 : GitHub Codespaces (Recommandé pour les débutants)

La manière la plus simple de commencer est d'utiliser GitHub Codespaces, qui fournit un environnement de développement complet dans votre navigateur.

1. Accédez au [répertoire](https://github.com/microsoft/Data-Science-For-Beginners)
2. Cliquez sur le menu déroulant **Code**
3. Sélectionnez l'onglet **Codespaces**
4. Cliquez sur **Create codespace on main**
5. Attendez que l'environnement s'initialise (2-3 minutes)

Votre environnement est maintenant prêt avec toutes les dépendances préinstallées !

### Option 2 : Développement local

Pour travailler sur votre propre ordinateur, suivez les instructions détaillées ci-dessous.

## Installation locale

### Étape 1 : Installer Git

Git est nécessaire pour cloner le répertoire et suivre vos modifications.

**Windows :**
- Téléchargez depuis [git-scm.com](https://git-scm.com/download/win)
- Exécutez l'installateur avec les paramètres par défaut

**macOS :**
- Installez via Homebrew : `brew install git`
- Ou téléchargez depuis [git-scm.com](https://git-scm.com/download/mac)

**Linux :**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### Étape 2 : Cloner le répertoire

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Étape 3 : Installer Python et Jupyter

Python 3.7 ou une version supérieure est requis pour les leçons de science des données.

**Windows :**
1. Téléchargez Python depuis [python.org](https://www.python.org/downloads/)
2. Pendant l'installation, cochez "Add Python to PATH"
3. Vérifiez l'installation :
```bash
python --version
```

**macOS :**
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

**Linux :**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### Étape 4 : Configurer l'environnement Python

Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Étape 5 : Installer les bibliothèques Python

Installez les bibliothèques nécessaires pour la science des données :

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Étape 6 : Installer Node.js et npm (pour l'application de quiz)

L'application de quiz nécessite Node.js et npm.

**Windows/macOS :**
- Téléchargez depuis [nodejs.org](https://nodejs.org/) (version LTS recommandée)
- Exécutez l'installateur

**Linux :**
```bash
# Debian/Ubuntu
# WARNING: Piping scripts from the internet directly into bash can be a security risk.
# It is recommended to review the script before running it:
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# Then run:
#   sudo -E bash setup_lts.x
#
# Alternatively, you can use the one-liner below at your own risk:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Fedora
sudo dnf install nodejs

# Verify installation
node --version
npm --version
```

### Étape 7 : Installer les dépendances de l'application de quiz

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Étape 8 : Installer Docsify (optionnel)

Pour un accès hors ligne à la documentation :

```bash
npm install -g docsify-cli
```

## Vérifiez votre installation

### Tester Python et Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Votre navigateur devrait s'ouvrir avec l'interface Jupyter. Vous pouvez maintenant naviguer vers n'importe quel fichier `.ipynb` des leçons.

### Tester l'application de quiz

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

L'application de quiz devrait être accessible à l'adresse `http://localhost:8080` (ou un autre port si 8080 est occupé).

### Tester le serveur de documentation

```bash
# From the root directory of the repository
docsify serve
```

La documentation devrait être accessible à l'adresse `http://localhost:3000`.

## Utiliser les conteneurs de développement VS Code

Si vous avez Docker installé, vous pouvez utiliser les conteneurs de développement VS Code :

1. Installez [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Installez [Visual Studio Code](https://code.visualstudio.com/)
3. Installez l'extension [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Ouvrez le répertoire dans VS Code
5. Appuyez sur `F1` et sélectionnez "Remote-Containers: Reopen in Container"
6. Attendez que le conteneur se construise (uniquement la première fois)

## Prochaines étapes

- Explorez le fichier [README.md](README.md) pour une vue d'ensemble du programme
- Lisez [USAGE.md](USAGE.md) pour des exemples et des flux de travail courants
- Consultez [TROUBLESHOOTING.md](TROUBLESHOOTING.md) si vous rencontrez des problèmes
- Consultez [CONTRIBUTING.md](CONTRIBUTING.md) si vous souhaitez contribuer

## Obtenir de l'aide

Si vous rencontrez des problèmes :

1. Consultez le guide [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Recherchez les [problèmes existants sur GitHub](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Rejoignez notre [communauté Discord](https://aka.ms/ds4beginners/discord)
4. Créez un nouveau problème avec des informations détaillées sur votre problème

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.