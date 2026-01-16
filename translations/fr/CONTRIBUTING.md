<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T13:17:17+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fr"
}
-->
# Contribuer à Data Science pour les Débutants

Merci de votre intérêt pour contribuer au programme Data Science pour les Débutants ! Nous accueillons les contributions de la communauté.

## Table des Matières

- [Code de Conduite](../..)
- [Comment Puis-je Contribuer ?](../..)
- [Premiers Pas](../..)
- [Directives de Contribution](../..)
- [Processus de Pull Request](../..)
- [Directives de Style](../..)
- [Accord de Licence du Contributeur](../..)

## Code de Conduite

Ce projet a adopté le [Code de Conduite Open Source de Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Pour plus d'informations, consultez la [FAQ sur le Code de Conduite](https://opensource.microsoft.com/codeofconduct/faq/) ou contactez [opencode@microsoft.com](mailto:opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## Comment Puis-je Contribuer ?

### Signaler des Bugs

Avant de créer des rapports de bugs, veuillez vérifier les problèmes existants pour éviter les doublons. Lorsque vous créez un rapport de bug, incluez autant de détails que possible :

- **Utilisez un titre clair et descriptif**
- **Décrivez les étapes exactes pour reproduire le problème**
- **Fournissez des exemples spécifiques** (extraits de code, captures d'écran)
- **Décrivez le comportement observé et celui attendu**
- **Incluez les détails de votre environnement** (OS, version de Python, navigateur)

### Suggérer des Améliorations

Les suggestions d'améliorations sont les bienvenues ! Lors de la proposition d'améliorations :

- **Utilisez un titre clair et descriptif**
- **Fournissez une description détaillée de l'amélioration suggérée**
- **Expliquez pourquoi cette amélioration serait utile**
- **Listez les fonctionnalités similaires dans d'autres projets, si applicable**

### Contribuer à la Documentation

Les améliorations de la documentation sont toujours appréciées :

- **Corrigez les fautes de frappe et les erreurs grammaticales**
- **Améliorez la clarté des explications**
- **Ajoutez de la documentation manquante**
- **Mettez à jour les informations obsolètes**
- **Ajoutez des exemples ou des cas d'utilisation**

### Contribuer au Code

Nous accueillons les contributions au code, notamment :

- **Nouvelles leçons ou exercices**
- **Corrections de bugs**
- **Améliorations des notebooks existants**
- **Nouveaux ensembles de données ou exemples**
- **Améliorations de l'application de quiz**

## Premiers Pas

### Prérequis

Avant de contribuer, assurez-vous d'avoir :

1. Un compte GitHub
2. Git installé sur votre système
3. Python 3.7+ et Jupyter installés
4. Node.js et npm (pour les contributions à l'application de quiz)
5. Une bonne compréhension de la structure du programme

Consultez [INSTALLATION.md](INSTALLATION.md) pour des instructions détaillées sur la configuration.

### Fork et Clone

1. **Forkez le dépôt** sur GitHub  
2. **Clonez votre fork** localement :  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Ajoutez un remote upstream** :  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Créer une Branche

Créez une nouvelle branche pour votre travail :  
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Conventions de nommage des branches :  
- `feature/` - Nouvelles fonctionnalités ou leçons  
- `fix/` - Corrections de bugs  
- `docs/` - Modifications de la documentation  
- `refactor/` - Refactorisation du code  

## Directives de Contribution

### Pour le Contenu des Leçons

Lors de la contribution ou de la modification des leçons existantes :

1. **Suivez la structure existante** :  
   - README.md avec le contenu de la leçon  
   - Notebook Jupyter avec des exercices  
   - Devoir (si applicable)  
   - Lien vers les quiz avant et après  

2. **Incluez ces éléments** :  
   - Objectifs d'apprentissage clairs  
   - Explications étape par étape  
   - Exemples de code avec commentaires  
   - Exercices pour la pratique  
   - Liens vers des ressources supplémentaires  

3. **Assurez l'accessibilité** :  
   - Utilisez un langage clair et simple  
   - Fournissez du texte alternatif pour les images  
   - Ajoutez des commentaires dans le code  
   - Prenez en compte différents styles d'apprentissage  

### Pour les Notebooks Jupyter

1. **Effacez toutes les sorties** avant de valider :  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Ajoutez des cellules markdown** avec des explications  

3. **Utilisez un formatage cohérent** :  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Testez complètement votre notebook** avant de le soumettre  

### Pour le Code Python

Suivez les directives de style [PEP 8](https://www.python.org/dev/peps/pep-0008/) :  
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
  

### Pour les Contributions à l'Application de Quiz

Lors de la modification de l'application de quiz :

1. **Testez localement** :  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Exécutez le linter** :  
   ```bash
   npm run lint
   ```
  
3. **Construisez avec succès** :  
   ```bash
   npm run build
   ```
  
4. **Suivez le guide de style Vue.js** et les modèles existants  

### Pour les Traductions

Lors de l'ajout ou de la mise à jour des traductions :

1. Suivez la structure du dossier `translations/`  
2. Utilisez le code langue comme nom de dossier (par ex., `fr` pour le français)  
3. Maintenez la même structure de fichiers que la version anglaise  
4. Mettez à jour les liens des quiz pour inclure le paramètre de langue : `?loc=fr`  
5. Testez tous les liens et le formatage  

## Processus de Pull Request

### Avant de Soumettre

1. **Mettez à jour votre branche** avec les dernières modifications :  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Testez vos modifications** :  
   - Exécutez tous les notebooks modifiés  
   - Testez l'application de quiz si modifiée  
   - Vérifiez que tous les liens fonctionnent  
   - Corrigez les fautes d'orthographe et de grammaire  

3. **Validez vos modifications** :  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Rédigez des messages de commit clairs :  
   - Utilisez le présent ("Ajoute une fonctionnalité" et non "Ajouté une fonctionnalité")  
   - Utilisez l'impératif ("Déplace le curseur vers..." et non "Déplace le curseur vers...")  
   - Limitez la première ligne à 72 caractères  
   - Faites référence aux problèmes et pull requests lorsque pertinent  

4. **Poussez sur votre fork** :  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Créer la Pull Request

1. Allez sur le [dépôt](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Cliquez sur "Pull requests" → "New pull request"  
3. Cliquez sur "compare across forks"  
4. Sélectionnez votre fork et branche  
5. Cliquez sur "Create pull request"  

### Format du Titre de la PR

Utilisez des titres clairs et descriptifs suivant ce format :  
```
[Component] Brief description
```
  
Exemples :  
- `[Leçon 7] Corrige l'erreur d'importation dans le notebook Python`  
- `[Application de Quiz] Ajoute la traduction en allemand`  
- `[Docs] Met à jour le README avec les nouveaux prérequis`  
- `[Fix] Corrige le chemin des données dans la leçon de visualisation`  

### Description de la PR

Incluez dans la description de votre PR :  
- **Quoi** : Quelles modifications avez-vous apportées ?  
- **Pourquoi** : Pourquoi ces modifications sont-elles nécessaires ?  
- **Comment** : Comment avez-vous implémenté les modifications ?  
- **Tests** : Comment avez-vous testé les modifications ?  
- **Captures d'écran** : Ajoutez des captures d'écran pour les modifications visuelles  
- **Problèmes liés** : Lien vers les problèmes liés (par ex., "Fixes #123")  

### Processus de Revue

1. **Des vérifications automatisées** seront exécutées sur votre PR  
2. **Les mainteneurs examineront** votre contribution  
3. **Répondez aux commentaires** en apportant des commits supplémentaires  
4. Une fois approuvée, un **mainteneur fusionnera** votre PR  

### Après la Fusion de Votre PR

1. Supprimez votre branche :  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Mettez à jour votre fork :  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Directives de Style

### Markdown

- Utilisez des niveaux de titres cohérents  
- Ajoutez des lignes vides entre les sections  
- Utilisez des blocs de code avec spécificateurs de langage :  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Ajoutez du texte alternatif aux images : `![Texte alternatif](../../translated_images/fr/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`  
- Gardez des longueurs de ligne raisonnables (environ 80-100 caractères)  

### Python

- Suivez le guide de style PEP 8  
- Utilisez des noms de variables significatifs  
- Ajoutez des docstrings aux fonctions  
- Incluez des annotations de type lorsque c'est approprié :  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Suivez le guide de style Vue.js 2  
- Utilisez la configuration ESLint fournie  
- Écrivez des composants modulaires et réutilisables  
- Ajoutez des commentaires pour les logiques complexes  

### Organisation des Fichiers

- Regroupez les fichiers liés  
- Utilisez des noms de fichiers descriptifs  
- Suivez la structure de répertoires existante  
- Ne validez pas de fichiers inutiles (.DS_Store, .pyc, node_modules, etc.)  

## Accord de Licence du Contributeur

Ce projet accueille les contributions et suggestions. La plupart des contributions nécessitent que vous acceptiez un Accord de Licence du Contributeur (CLA) déclarant que vous avez le droit, et que vous accordez effectivement, les droits nécessaires pour utiliser votre contribution. Pour plus de détails, visitez [https://cla.microsoft.com](https://cla.microsoft.com).

Lorsque vous soumettez une pull request, un bot CLA déterminera automatiquement si vous devez fournir un CLA et annotera la PR en conséquence (par ex., étiquette, commentaire). Suivez simplement les instructions fournies par le bot. Vous n'aurez à le faire qu'une seule fois pour tous les dépôts utilisant notre CLA.

## Questions ?

- Consultez notre [Canal Discord #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Rejoignez notre [communauté Discord](https://aka.ms/ds4beginners/discord)  
- Consultez les [problèmes existants](https://github.com/microsoft/Data-Science-For-Beginners/issues) et les [pull requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls)  

## Merci !

Vos contributions rendent ce programme meilleur pour tout le monde. Merci de prendre le temps de contribuer !

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.