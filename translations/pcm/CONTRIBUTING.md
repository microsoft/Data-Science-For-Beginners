<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-11-18T18:12:09+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pcm"
}
-->
# How to Contribute to Data Science for Beginners

Tank you say you wan contribute to di Data Science for Beginners curriculum! We dey happy to see community people wey wan help.

## Table of Contents

- [Code of Conduct](../..)
- [How I Fit Contribute?](../..)
- [How to Start](../..)
- [Contribution Guidelines](../..)
- [Pull Request Process](../..)
- [Style Guidelines](../..)
- [Contributor License Agreement](../..)

## Code of Conduct

Dis project dey follow di [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
If you wan sabi more, check di [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)  
or send email to [opencode@microsoft.com](mailto:opencode@microsoft.com) if you get any question or comment.

## How I Fit Contribute?

### Report Bugs

Before you go report bug, abeg check di issues wey don dey already so you no go repeat di same thing. If you wan report bug, abeg add plenty details:

- **Use clear and correct title**
- **Explain di steps wey fit make di problem show**
- **Add example** (code snippets, screenshots)
- **Talk wetin you see and wetin you dey expect**
- **Add your environment details** (OS, Python version, browser)

### Suggest Improvements

We dey happy to see suggestions for improvement! If you wan suggest something:

- **Use clear and correct title**
- **Explain di improvement well well**
- **Talk why e go make sense**
- **Mention any similar feature for other projects, if e dey**

### Help with Documentation

We dey always appreciate better documentation:

- **Correct typo and grammar mistake**
- **Make explanation clear**
- **Add di documentation wey dey miss**
- **Update old information**
- **Add example or use case**

### Contribute Code

We dey welcome code contributions like:

- **New lessons or exercises**
- **Bug fixes**
- **Better notebooks**
- **New datasets or examples**
- **Improve quiz app**

## How to Start

### Wetin You Need

Before you start, make sure say you get:

1. GitHub account
2. Git for your system
3. Python 3.7+ and Jupyter
4. Node.js and npm (if na quiz app you wan work on)
5. You sabi di curriculum structure

Check [INSTALLATION.md](INSTALLATION.md) for setup instructions.

### Fork and Clone

1. **Fork di repo** for GitHub  
2. **Clone your fork** for your computer:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Add upstream remote**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```


### Create Branch

Create new branch for your work:  
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Branch naming style:  
- `feature/` - For new features or lessons  
- `fix/` - For bug fixes  
- `docs/` - For documentation changes  
- `refactor/` - For code wey you wan rearrange  

## Contribution Guidelines

### For Lesson Content

If you wan add or change lesson:

1. **Follow di structure wey dey already**:  
   - README.md for di lesson content  
   - Jupyter notebook for exercises  
   - Assignment (if e dey)  
   - Link to pre and post quizzes  

2. **Add dis things**:  
   - Clear learning objectives  
   - Step-by-step explanation  
   - Code examples with comments  
   - Exercises to practice  
   - Links to more resources  

3. **Make am easy for everybody**:  
   - Use simple language  
   - Add alt text for images  
   - Put comments for code  
   - Think about different learning styles  

### For Jupyter Notebooks

1. **Clear all outputs** before you commit:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Add markdown cells** to explain things  

3. **Use same format everywhere**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Test di notebook** well before you submit  

### For Python Code

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide:  
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
  

### For Quiz App Contributions

If you dey work on di quiz app:

1. **Test am for your computer**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Run linter**:  
   ```bash
   npm run lint
   ```
  
3. **Make sure e build well**:  
   ```bash
   npm run build
   ```
  
4. **Follow Vue.js style guide** and di pattern wey dey already  

### For Translations

If you wan add or update translations:

1. Follow di structure for `translations/` folder  
2. Use di language code as folder name (e.g., `fr` for French)  
3. Keep di same file structure as English version  
4. Update quiz links to include language parameter: `?loc=fr`  
5. Test all links and formatting  

## Pull Request Process

### Before You Submit

1. **Update your branch** with di latest changes:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Test wetin you change**:  
   - Run all di notebooks wey you change  
   - Test quiz app if you touch am  
   - Check all links  
   - Look for spelling and grammar mistake  

3. **Commit your changes**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Write clear commit messages:  
   - Use present tense ("Add feature" no be "Added feature")  
   - Use imperative mood ("Move cursor to..." no be "Moves cursor to...")  
   - First line no pass 72 characters  
   - Mention issues and pull requests if e dey relevant  

4. **Push to your fork**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Create di Pull Request

1. Go to di [repo](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Click "Pull requests" → "New pull request"  
3. Click "compare across forks"  
4. Select your fork and branch  
5. Click "Create pull request"  

### PR Title Style

Use clear, correct title like dis:  
```
[Component] Brief description
```
  
Examples:  
- `[Lesson 7] Fix Python notebook import error`  
- `[Quiz App] Add German translation`  
- `[Docs] Update README with new prerequisites`  
- `[Fix] Correct data path in visualization lesson`  

### PR Description

For your PR description, talk about:  

- **Wetin**: Wetin you change?  
- **Why**: Why di change dey important?  
- **How**: How you take do am?  
- **Testing**: How you test am?  
- **Screenshots**: Add screenshots if e get visual change  
- **Related Issues**: Link di issues wey e relate to (e.g., "Fixes #123")  

### Review Process

1. **Automated checks** go run for your PR  
2. **Maintainers go review** wetin you submit  
3. **Fix any feedback** by adding more commits  
4. Once dem approve am, **maintainer go merge** your PR  

### After Dem Merge Your PR

1. Delete your branch:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Update your fork:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Style Guidelines

### Markdown

- Use same heading levels  
- Put blank lines between sections  
- Use code blocks with language specifiers:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Add alt text for images: `![Alt text](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.pcm.png)`  
- No make line too long (around 80-100 characters)  

### Python

- Follow PEP 8 style guide  
- Use good variable names  
- Add docstrings for functions  
- Add type hints if e make sense:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Follow Vue.js 2 style guide  
- Use di ESLint config wey we provide  
- Write modular, reusable components  
- Add comments for any complex logic  

### File Arrangement

- Keep related files together  
- Use good file names  
- Follow di directory structure wey dey already  
- No commit unnecessary files (.DS_Store, .pyc, node_modules, etc.)  

## Contributor License Agreement

We dey welcome contributions and suggestions. Most contributions go need you to agree to Contributor License Agreement (CLA) wey go show say you get di right to, and you dey give us di right to use wetin you contribute. For details, visit https://cla.microsoft.com.  

When you submit pull request, CLA-bot go check if you need to provide CLA and go mark di PR well (e.g., label, comment). Just follow di instructions wey di bot go give you. You go only do dis one time for all repos wey dey use our CLA.  

## Questions?

- Check our [Discord Channel #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Join our [Discord community](https://aka.ms/ds4beginners/discord)  
- Look di [issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) and [pull requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls) wey don dey already  

## Tank You!

Na your contribution dey make dis curriculum better for everybody. Tank you say you take time to contribute!  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make una sabi say automatik transleshion fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey una suppose trust. For important informashon, e good make una use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretashon wey fit happen because una use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->