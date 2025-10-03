<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T10:58:33+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fr"
}
-->
# AGENTS.md

## Aperçu du projet

Data Science for Beginners est un programme complet de 10 semaines et 20 leçons créé par les Cloud Advocates de Microsoft Azure. Le dépôt est une ressource d'apprentissage qui enseigne les concepts fondamentaux de la science des données à travers des leçons basées sur des projets, incluant des notebooks Jupyter, des quiz interactifs et des exercices pratiques.

**Technologies clés :**
- **Jupyter Notebooks** : Principal support d'apprentissage utilisant Python 3
- **Bibliothèques Python** : pandas, numpy, matplotlib pour l'analyse et la visualisation des données
- **Vue.js 2** : Application de quiz (dossier quiz-app)
- **Docsify** : Générateur de site de documentation pour un accès hors ligne
- **Node.js/npm** : Gestion des packages pour les composants JavaScript
- **Markdown** : Tout le contenu des leçons et la documentation

**Architecture :**
- Dépôt éducatif multilingue avec de nombreuses traductions
- Structuré en modules de leçons (1-Introduction à 6-Data-Science-In-Wild)
- Chaque leçon inclut un README, des notebooks, des exercices et des quiz
- Application de quiz Vue.js autonome pour les évaluations avant/après leçon
- Support pour GitHub Codespaces et les conteneurs de développement VS Code

## Commandes d'installation

### Configuration du dépôt
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Configuration de l'environnement Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Configuration de l'application de quiz
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### Serveur de documentation Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Configuration des projets de visualisation
Pour les projets de visualisation comme meaningful-visualizations (leçon 13) :
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## Flux de travail de développement

### Travailler avec les notebooks Jupyter
1. Démarrez Jupyter à la racine du dépôt : `jupyter notebook`
2. Naviguez vers le dossier de la leçon souhaitée
3. Ouvrez les fichiers `.ipynb` pour travailler sur les exercices
4. Les notebooks sont autonomes avec des explications et des cellules de code
5. La plupart des notebooks utilisent pandas, numpy et matplotlib - assurez-vous qu'ils sont installés

### Structure des leçons
Chaque leçon contient généralement :
- `README.md` - Contenu principal de la leçon avec théorie et exemples
- `notebook.ipynb` - Exercices pratiques dans un notebook Jupyter
- `assignment.ipynb` ou `assignment.md` - Exercices pratiques
- Dossier `solution/` - Notebooks et code de solution
- Dossier `images/` - Matériaux visuels de support

### Développement de l'application de quiz
- Application Vue.js 2 avec rechargement à chaud pendant le développement
- Les quiz sont stockés dans `quiz-app/src/assets/translations/`
- Chaque langue a son propre dossier de traduction (en, fr, es, etc.)
- La numérotation des quiz commence à 0 et va jusqu'à 39 (40 quiz au total)

### Ajouter des traductions
- Les traductions se trouvent dans le dossier `translations/` à la racine du dépôt
- Chaque langue a une structure complète de leçons miroir de l'anglais
- Traduction automatisée via GitHub Actions (co-op-translator.yml)

## Instructions de test

### Test de l'application de quiz
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Test des notebooks
- Aucun cadre de test automatisé n'existe pour les notebooks
- Validation manuelle : Exécutez toutes les cellules dans l'ordre pour vérifier qu'il n'y a pas d'erreurs
- Vérifiez que les fichiers de données sont accessibles et que les sorties sont générées correctement
- Assurez-vous que les visualisations s'affichent correctement

### Test de la documentation
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Vérifications de la qualité du code
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Directives de style de code

### Python (Notebooks Jupyter)
- Suivez les directives de style PEP 8 pour le code Python
- Utilisez des noms de variables clairs qui expliquent les données analysées
- Incluez des cellules Markdown avec des explications avant les cellules de code
- Gardez les cellules de code centrées sur des concepts ou opérations uniques
- Utilisez pandas pour la manipulation des données, matplotlib pour la visualisation
- Modèle d'importation commun :
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Suivez le guide de style Vue.js 2 et les meilleures pratiques
- Configuration ESLint dans `quiz-app/package.json`
- Utilisez des composants Vue à fichier unique (.vue)
- Maintenez une architecture basée sur les composants
- Exécutez `npm run lint` avant de valider les modifications

### Documentation Markdown
- Utilisez une hiérarchie claire des titres (# ## ### etc.)
- Incluez des blocs de code avec des spécificateurs de langage
- Ajoutez du texte alternatif pour les images
- Liez les leçons et ressources connexes
- Gardez des longueurs de ligne raisonnables pour la lisibilité

### Organisation des fichiers
- Contenu des leçons dans des dossiers numérotés (01-defining-data-science, etc.)
- Solutions dans des sous-dossiers dédiés `solution/`
- Les traductions reflètent la structure anglaise dans le dossier `translations/`
- Gardez les fichiers de données dans `data/` ou des dossiers spécifiques aux leçons

## Construction et déploiement

### Déploiement de l'application de quiz
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Déploiement Azure Static Web Apps
L'application de quiz peut être déployée sur Azure Static Web Apps :
1. Créez une ressource Azure Static Web App
2. Connectez-vous au dépôt GitHub
3. Configurez les paramètres de construction :
   - Emplacement de l'application : `quiz-app`
   - Emplacement de sortie : `dist`
4. Le workflow GitHub Actions déploiera automatiquement lors d'un push

### Site de documentation
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Le dépôt inclut une configuration de conteneur de développement
- Codespaces configure automatiquement l'environnement Python et Node.js
- Ouvrez le dépôt dans Codespace via l'interface GitHub
- Toutes les dépendances s'installent automatiquement

## Directives pour les pull requests

### Avant de soumettre
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Format du titre de la PR
- Utilisez des titres clairs et descriptifs
- Format : `[Composant] Brève description`
- Exemples :
  - `[Leçon 7] Corrige l'erreur d'importation du notebook Python`
  - `[Application de quiz] Ajoute la traduction en allemand`
  - `[Docs] Met à jour le README avec les nouveaux prérequis`

### Vérifications requises
- Assurez-vous que tout le code s'exécute sans erreurs
- Vérifiez que les notebooks s'exécutent complètement
- Confirmez que les applications Vue.js se construisent avec succès
- Vérifiez que les liens de la documentation fonctionnent
- Testez l'application de quiz si elle a été modifiée
- Vérifiez que les traductions maintiennent une structure cohérente

### Directives de contribution
- Suivez le style et les modèles de code existants
- Ajoutez des commentaires explicatifs pour les logiques complexes
- Mettez à jour la documentation pertinente
- Testez les modifications dans différents modules de leçons si applicable
- Consultez le fichier CONTRIBUTING.md

## Notes supplémentaires

### Bibliothèques couramment utilisées
- **pandas** : Manipulation et analyse des données
- **numpy** : Calcul numérique
- **matplotlib** : Visualisation et tracé des données
- **seaborn** : Visualisation statistique des données (certaines leçons)
- **scikit-learn** : Apprentissage automatique (leçons avancées)

### Travailler avec les fichiers de données
- Les fichiers de données se trouvent dans le dossier `data/` ou dans des répertoires spécifiques aux leçons
- La plupart des notebooks attendent des fichiers de données dans des chemins relatifs
- Les fichiers CSV sont le format de données principal
- Certaines leçons utilisent JSON pour des exemples de données non relationnelles

### Support multilingue
- Plus de 40 traductions linguistiques via GitHub Actions automatisés
- Workflow de traduction dans `.github/workflows/co-op-translator.yml`
- Traductions dans le dossier `translations/` avec des codes de langue
- Traductions des quiz dans `quiz-app/src/assets/translations/`

### Options d'environnement de développement
1. **Développement local** : Installez Python, Jupyter, Node.js localement
2. **GitHub Codespaces** : Environnement de développement instantané basé sur le cloud
3. **Conteneurs de développement VS Code** : Développement local basé sur des conteneurs
4. **Binder** : Lancez les notebooks dans le cloud (si configuré)

### Directives de contenu des leçons
- Chaque leçon est autonome mais s'appuie sur des concepts précédents
- Les quiz avant la leçon testent les connaissances préalables
- Les quiz après la leçon renforcent l'apprentissage
- Les exercices offrent une pratique concrète
- Les sketchnotes fournissent des résumés visuels

### Résolution des problèmes courants

**Problèmes de noyau Jupyter :**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Échecs d'installation npm :**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Erreurs d'importation dans les notebooks :**
- Vérifiez que toutes les bibliothèques requises sont installées
- Vérifiez la compatibilité de la version Python (Python 3.7+ recommandé)
- Assurez-vous que l'environnement virtuel est activé

**Docsify ne se charge pas :**
- Vérifiez que vous servez depuis la racine du dépôt
- Assurez-vous que `index.html` existe
- Vérifiez l'accès réseau approprié (port 3000)

### Considérations de performance
- Les grands ensembles de données peuvent prendre du temps à charger dans les notebooks
- Le rendu des visualisations peut être lent pour les tracés complexes
- Le serveur de développement Vue.js permet un rechargement à chaud pour une itération rapide
- Les constructions de production sont optimisées et minifiées

### Notes de sécurité
- Aucune donnée sensible ou identifiant ne doit être soumis
- Utilisez des variables d'environnement pour les clés API dans les leçons cloud
- Les leçons liées à Azure peuvent nécessiter des identifiants de compte Azure
- Gardez les dépendances à jour pour les correctifs de sécurité

## Contribuer aux traductions
- Les traductions automatisées sont gérées via GitHub Actions
- Les corrections manuelles sont les bienvenues pour améliorer la précision des traductions
- Suivez la structure existante des dossiers de traduction
- Mettez à jour les liens des quiz pour inclure le paramètre de langue : `?loc=fr`
- Testez les leçons traduites pour un rendu correct

## Ressources connexes
- Programme principal : https://aka.ms/datascience-beginners
- Microsoft Learn : https://docs.microsoft.com/learn/
- Student Hub : https://docs.microsoft.com/learn/student-hub
- Forum de discussion : https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Autres programmes Microsoft : ML for Beginners, AI for Beginners, Web Dev for Beginners

## Maintenance du projet
- Mises à jour régulières pour garder le contenu à jour
- Contributions de la communauté bienvenues
- Problèmes suivis sur GitHub
- PRs examinées par les mainteneurs du programme
- Revues et mises à jour mensuelles du contenu

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.