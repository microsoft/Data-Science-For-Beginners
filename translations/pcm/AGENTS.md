<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-11-18T18:13:11+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pcm"
}
-->
# AGENTS.md

## Project Overview

Data Science for Beginners na one complete 10-week, 20-lesson curriculum wey Microsoft Azure Cloud Advocates create. Dis repository na learning resource wey dey teach basic data science concepts through project-based lessons, including Jupyter notebooks, interactive quizzes, and hands-on assignments.

**Key Technologies:**
- **Jupyter Notebooks**: Na di main learning tool wey dey use Python 3
- **Python Libraries**: pandas, numpy, matplotlib for data analysis and visualization
- **Vue.js 2**: Quiz application (quiz-app folder)
- **Docsify**: Documentation site generator for offline access
- **Node.js/npm**: Package management for JavaScript components
- **Markdown**: All lesson content and documentation

**Architecture:**
- Multi-language educational repository wey get plenty translations
- E dey structured into lesson modules (1-Introduction through 6-Data-Science-In-Wild)
- Each lesson get README, notebooks, assignments, and quizzes
- Standalone Vue.js quiz application for pre/post-lesson assessments
- GitHub Codespaces and VS Code dev containers support

## Setup Commands

### Repository Setup
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python Environment Setup
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Quiz Application Setup
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

### Docsify Documentation Server
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Visualization Projects Setup
For visualization projects like meaningful-visualizations (lesson 13):
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

## Development Workflow

### Working with Jupyter Notebooks
1. Start Jupyter for di repository root: `jupyter notebook`
2. Go di lesson folder wey you wan work on
3. Open `.ipynb` files to work through di exercises
4. Notebooks dey self-contained with explanations and code cells
5. Most notebooks dey use pandas, numpy, and matplotlib - make sure say dem dey installed

### Lesson Structure
Each lesson dey usually contain:
- `README.md` - Main lesson content with theory and examples
- `notebook.ipynb` - Hands-on Jupyter notebook exercises
- `assignment.ipynb` or `assignment.md` - Practice assignments
- `solution/` folder - Solution notebooks and code
- `images/` folder - Supporting visual materials

### Quiz Application Development
- Vue.js 2 application wey get hot-reload during development
- Quizzes dey stored for `quiz-app/src/assets/translations/`
- Each language get im own translation folder (en, fr, es, etc.)
- Quiz numbering dey start from 0 go reach 39 (40 quizzes total)

### Adding Translations
- Translations dey go `translations/` folder for repository root
- Each language dey mirror di complete lesson structure from English
- Automated translation dey happen via GitHub Actions (co-op-translator.yml)

## Testing Instructions

### Quiz Application Testing
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Notebook Testing
- No automated test framework dey for notebooks
- Manual validation: Run all cells one by one to make sure say no error dey
- Check say data files dey accessible and outputs dey correct
- Confirm say visualizations dey render well

### Documentation Testing
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Code Quality Checks
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```

## Code Style Guidelines

### Python (Jupyter Notebooks)
- Follow PEP 8 style guidelines for Python code
- Use clear variable names wey explain di data wey you dey analyze
- Add markdown cells with explanations before code cells
- Make code cells dey focus on one concept or operation
- Use pandas for data manipulation, matplotlib for visualization
- Common import pattern:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```

### JavaScript/Vue.js
- Follow Vue.js 2 style guide and best practices
- ESLint configuration dey for `quiz-app/package.json`
- Use Vue single-file components (.vue files)
- Maintain component-based architecture
- Run `npm run lint` before you commit changes

### Markdown Documentation
- Use clear headings hierarchy (# ## ### etc.)
- Add code blocks with language specifiers
- Put alt text for images
- Link to related lessons and resources
- Keep line lengths reasonable for readability

### File Organization
- Lesson content dey inside numbered folders (01-defining-data-science, etc.)
- Solutions dey for dedicated `solution/` subfolders
- Translations dey mirror English structure for `translations/` folder
- Keep data files for `data/` or lesson-specific folders

## Build and Deployment

### Quiz Application Deployment
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps Deployment
Di quiz-app fit deploy to Azure Static Web Apps:
1. Create Azure Static Web App resource
2. Connect am to GitHub repository
3. Configure build settings:
   - App location: `quiz-app`
   - Output location: `dist`
4. GitHub Actions workflow go auto-deploy when you push

### Documentation Site
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repository get dev container configuration
- Codespaces dey automatically set up Python and Node.js environment
- Open repository for Codespace via GitHub UI
- All dependencies go install automatically

## Pull Request Guidelines

### Before Submitting
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR Title Format
- Use clear, descriptive titles
- Format: `[Component] Brief description`
- Examples:
  - `[Lesson 7] Fix Python notebook import error`
  - `[Quiz App] Add German translation`
  - `[Docs] Update README with new prerequisites`

### Required Checks
- Make sure say all code dey run without errors
- Verify say notebooks dey execute completely
- Confirm say Vue.js apps dey build successfully
- Check say documentation links dey work
- Test quiz application if you modify am
- Verify say translations dey maintain consistent structure

### Contribution Guidelines
- Follow di existing code style and patterns
- Add explanatory comments for complex logic
- Update relevant documentation
- Test changes across different lesson modules if e apply
- Review di CONTRIBUTING.md file

## Additional Notes

### Common Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization and plotting
- **seaborn**: Statistical data visualization (some lessons)
- **scikit-learn**: Machine learning (advanced lessons)

### Working with Data Files
- Data files dey for `data/` folder or lesson-specific directories
- Most notebooks dey expect data files for relative paths
- CSV files na di main data format
- Some lessons dey use JSON for non-relational data examples

### Multilingual Support
- 40+ language translations dey via automated GitHub Actions
- Translation workflow dey for `.github/workflows/co-op-translator.yml`
- Translations dey for `translations/` folder with language codes
- Quiz translations dey for `quiz-app/src/assets/translations/`

### Development Environment Options
1. **Local Development**: Install Python, Jupyter, Node.js for your system
2. **GitHub Codespaces**: Cloud-based instant development environment
3. **VS Code Dev Containers**: Local container-based development
4. **Binder**: Launch notebooks for cloud (if configured)

### Lesson Content Guidelines
- Each lesson dey standalone but e dey build on previous concepts
- Pre-lesson quizzes dey test prior knowledge
- Post-lesson quizzes dey reinforce wetin you don learn
- Assignments dey provide hands-on practice
- Sketchnotes dey provide visual summaries

### Troubleshooting Common Issues

**Jupyter Kernel Issues:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm Install Failures:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Import Errors in Notebooks:**
- Check say all required libraries dey installed
- Confirm Python version compatibility (Python 3.7+ recommended)
- Make sure say virtual environment dey activated

**Docsify Not Loading:**
- Confirm say you dey serve from repository root
- Check say `index.html` dey
- Make sure say network access dey okay (port 3000)

### Performance Considerations
- Large datasets fit take time to load for notebooks
- Visualization rendering fit slow for complex plots
- Vue.js dev server dey enable hot-reload for quick iteration
- Production builds dey optimized and minified

### Security Notes
- No sensitive data or credentials suppose dey committed
- Use environment variables for any API keys for cloud lessons
- Azure-related lessons fit need Azure account credentials
- Keep dependencies updated for security patches

## Contributing to Translations
- Automated translations dey managed via GitHub Actions
- Manual corrections dey welcome to improve translation accuracy
- Follow di existing translation folder structure
- Update quiz links to include language parameter: `?loc=fr`
- Test translated lessons to make sure say dem dey render well

## Related Resources
- Main curriculum: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Discussion Forum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Other Microsoft curricula: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Project Maintenance
- Regular updates dey to keep content current
- Community contributions dey welcome
- Issues dey tracked for GitHub
- PRs dey reviewed by curriculum maintainers
- Monthly content reviews and updates

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important mata, e good make professional human transleto check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->