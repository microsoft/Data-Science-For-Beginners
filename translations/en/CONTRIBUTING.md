<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T13:15:56+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "en"
}
-->
# Contributing to Data Science for Beginners

Thank you for your interest in contributing to the Data Science for Beginners curriculum! We welcome contributions from the community.

## Table of Contents

- [Code of Conduct](../..)
- [How Can I Contribute?](../..)
- [Getting Started](../..)
- [Contribution Guidelines](../..)
- [Pull Request Process](../..)
- [Style Guidelines](../..)
- [Contributor License Agreement](../..)

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information, see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (code snippets, screenshots)
- **Describe the behavior you observed and what you expected**
- **Include your environment details** (OS, Python version, browser)

### Suggesting Enhancements

Enhancement suggestions are welcome! When suggesting enhancements:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any similar features in other projects, if applicable**

### Contributing to Documentation

Documentation improvements are always appreciated:

- **Fix typos and grammatical errors**
- **Improve clarity of explanations**
- **Add missing documentation**
- **Update outdated information**
- **Add examples or use cases**

### Contributing Code

We welcome code contributions including:

- **New lessons or exercises**
- **Bug fixes**
- **Improvements to existing notebooks**
- **New datasets or examples**
- **Quiz application enhancements**

## Getting Started

### Prerequisites

Before contributing, ensure you have:

1. A GitHub account
2. Git installed on your system
3. Python 3.7+ and Jupyter installed
4. Node.js and npm (for quiz app contributions)
5. Familiarity with the curriculum structure

See [INSTALLATION.md](INSTALLATION.md) for detailed setup instructions.

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Create a Branch

Create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch naming conventions:
- `feature/` - New features or lessons
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring

## Contribution Guidelines

### For Lesson Content

When contributing lessons or modifying existing ones:

1. **Follow the existing structure**:
   - README.md with lesson content
   - Jupyter notebook with exercises
   - Assignment (if applicable)
   - Link to pre and post quizzes

2. **Include these elements**:
   - Clear learning objectives
   - Step-by-step explanations
   - Code examples with comments
   - Exercises for practice
   - Links to additional resources

3. **Ensure accessibility**:
   - Use clear, simple language
   - Provide alt text for images
   - Include code comments
   - Consider different learning styles

### For Jupyter Notebooks

1. **Clear all outputs** before committing:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Include markdown cells** with explanations

3. **Use consistent formatting**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Test your notebook** completely before submitting

### For Python Code

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines:

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

When modifying the quiz application:

1. **Test locally**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Run linter**:
   ```bash
   npm run lint
   ```

3. **Build successfully**:
   ```bash
   npm run build
   ```

4. **Follow Vue.js style guide** and existing patterns

### For Translations

When adding or updating translations:

1. Follow the structure in `translations/` folder
2. Use the language code as folder name (e.g., `fr` for French)
3. Maintain the same file structure as English version
4. Update quiz links to include language parameter: `?loc=fr`
5. Test all links and formatting

## Pull Request Process

### Before Submitting

1. **Update your branch** with the latest changes:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Test your changes**:
   - Run all modified notebooks
   - Test quiz app if modified
   - Verify all links work
   - Check for spelling and grammar errors

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Write clear commit messages:
   - Use present tense ("Add feature" not "Added feature")
   - Use imperative mood ("Move cursor to..." not "Moves cursor to...")
   - Limit first line to 72 characters
   - Reference issues and pull requests when relevant

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Creating the Pull Request

1. Go to the [repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. Click "Pull requests" → "New pull request"
3. Click "compare across forks"
4. Select your fork and branch
5. Click "Create pull request"

### PR Title Format

Use clear, descriptive titles following this format:

```
[Component] Brief description
```

Examples:
- `[Lesson 7] Fix Python notebook import error`
- `[Quiz App] Add German translation`
- `[Docs] Update README with new prerequisites`
- `[Fix] Correct data path in visualization lesson`

### PR Description

Include in your PR description:

- **What**: What changes did you make?
- **Why**: Why are these changes necessary?
- **How**: How did you implement the changes?
- **Testing**: How did you test the changes?
- **Screenshots**: Include screenshots for visual changes
- **Related Issues**: Link to related issues (e.g., "Fixes #123")

### Review Process

1. **Automated checks** will run on your PR
2. **Maintainers will review** your contribution
3. **Address feedback** by making additional commits
4. Once approved, a **maintainer will merge** your PR

### After Your PR is Merged

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

- Use consistent heading levels
- Include blank lines between sections
- Use code blocks with language specifiers:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Add alt text to images: `![Alt text](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.en.png)`
- Keep line lengths reasonable (around 80-100 characters)

### Python

- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Include type hints where appropriate:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Follow Vue.js 2 style guide
- Use ESLint configuration provided
- Write modular, reusable components
- Add comments for complex logic

### File Organization

- Keep related files together
- Use descriptive file names
- Follow existing directory structure
- Don't commit unnecessary files (.DS_Store, .pyc, node_modules, etc.)

## Contributor License Agreement

This project welcomes contributions and suggestions. Most contributions require you to
agree to a Contributor License Agreement (CLA) declaring that you have the right to,
and actually do, grant us the rights to use your contribution. For details, visit
https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need
to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the
instructions provided by the bot. You will only need to do this once across all repositories using our CLA.

## Questions?

- Check our [Discord Channel #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- Join our [Discord community](https://aka.ms/ds4beginners/discord)
- Review existing [issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) and [pull requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## Thank You!

Your contributions make this curriculum better for everyone. Thank you for taking the time to contribute!

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.