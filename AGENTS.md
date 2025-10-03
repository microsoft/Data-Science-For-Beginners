# AGENTS.md

## Project Overview

Data Science for Beginners is a comprehensive 10-week, 20-lesson curriculum created by Microsoft Azure Cloud Advocates. The repository is a learning resource that teaches foundational data science concepts through project-based lessons, including Jupyter notebooks, interactive quizzes, and hands-on assignments.

**Key Technologies:**
- **Jupyter Notebooks**: Primary learning medium using Python 3
- **Python Libraries**: pandas, numpy, matplotlib for data analysis and visualization
- **Vue.js 2**: Quiz application (quiz-app folder)
- **Docsify**: Documentation site generator for offline access
- **Node.js/npm**: Package management for JavaScript components
- **Markdown**: All lesson content and documentation

**Architecture:**
- Multi-language educational repository with extensive translations
- Structured into lesson modules (1-Introduction through 6-Data-Science-In-Wild)
- Each lesson includes README, notebooks, assignments, and quizzes
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
1. Start Jupyter in the repository root: `jupyter notebook`
2. Navigate to the desired lesson folder
3. Open `.ipynb` files to work through exercises
4. Notebooks are self-contained with explanations and code cells
5. Most notebooks use pandas, numpy, and matplotlib - ensure these are installed

### Lesson Structure
Each lesson typically contains:
- `README.md` - Main lesson content with theory and examples
- `notebook.ipynb` - Hands-on Jupyter notebook exercises
- `assignment.ipynb` or `assignment.md` - Practice assignments
- `solution/` folder - Solution notebooks and code
- `images/` folder - Supporting visual materials

### Quiz Application Development
- Vue.js 2 application with hot-reload during development
- Quizzes stored in `quiz-app/src/assets/translations/`
- Each language has its own translation folder (en, fr, es, etc.)
- Quiz numbering starts at 0 and goes up to 39 (40 quizzes total)

### Adding Translations
- Translations go in `translations/` folder at repository root
- Each language has complete lesson structure mirrored from English
- Automated translation via GitHub Actions (co-op-translator.yml)

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
- No automated test framework exists for notebooks
- Manual validation: Run all cells in sequence to ensure no errors
- Verify data files are accessible and outputs are generated correctly
- Check that visualizations render properly

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
- Use clear variable names that explain the data being analyzed
- Include markdown cells with explanations before code cells
- Keep code cells focused on single concepts or operations
- Use pandas for data manipulation, matplotlib for visualization
- Common import pattern:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```

### JavaScript/Vue.js
- Follow Vue.js 2 style guide and best practices
- ESLint configuration in `quiz-app/package.json`
- Use Vue single-file components (.vue files)
- Maintain component-based architecture
- Run `npm run lint` before committing changes

### Markdown Documentation
- Use clear headings hierarchy (# ## ### etc.)
- Include code blocks with language specifiers
- Add alt text for images
- Link to related lessons and resources
- Keep line lengths reasonable for readability

### File Organization
- Lesson content in numbered folders (01-defining-data-science, etc.)
- Solutions in dedicated `solution/` subfolders
- Translations mirror English structure in `translations/` folder
- Keep data files in `data/` or lesson-specific folders

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
The quiz-app can be deployed to Azure Static Web Apps:
1. Create Azure Static Web App resource
2. Connect to GitHub repository
3. Configure build settings:
   - App location: `quiz-app`
   - Output location: `dist`
4. GitHub Actions workflow will auto-deploy on push

### Documentation Site
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repository includes dev container configuration
- Codespaces automatically sets up Python and Node.js environment
- Open repository in Codespace via GitHub UI
- All dependencies install automatically

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
- Ensure all code runs without errors
- Verify notebooks execute completely
- Confirm Vue.js apps build successfully
- Check that documentation links work
- Test quiz application if modified
- Verify translations maintain consistent structure

### Contribution Guidelines
- Follow existing code style and patterns
- Add explanatory comments for complex logic
- Update relevant documentation
- Test changes across different lesson modules if applicable
- Review the CONTRIBUTING.md file

## Additional Notes

### Common Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization and plotting
- **seaborn**: Statistical data visualization (some lessons)
- **scikit-learn**: Machine learning (advanced lessons)

### Working with Data Files
- Data files located in `data/` folder or lesson-specific directories
- Most notebooks expect data files in relative paths
- CSV files are primary data format
- Some lessons use JSON for non-relational data examples

### Multilingual Support
- 40+ language translations via automated GitHub Actions
- Translation workflow in `.github/workflows/co-op-translator.yml`
- Translations in `translations/` folder with language codes
- Quiz translations in `quiz-app/src/assets/translations/`

### Development Environment Options
1. **Local Development**: Install Python, Jupyter, Node.js locally
2. **GitHub Codespaces**: Cloud-based instant development environment
3. **VS Code Dev Containers**: Local container-based development
4. **Binder**: Launch notebooks in cloud (if configured)

### Lesson Content Guidelines
- Each lesson is standalone but builds on previous concepts
- Pre-lesson quizzes test prior knowledge
- Post-lesson quizzes reinforce learning
- Assignments provide hands-on practice
- Sketchnotes provide visual summaries

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
- Verify all required libraries are installed
- Check Python version compatibility (Python 3.7+ recommended)
- Ensure virtual environment is activated

**Docsify Not Loading:**
- Verify you're serving from repository root
- Check that `index.html` exists
- Ensure proper network access (port 3000)

### Performance Considerations
- Large datasets may take time to load in notebooks
- Visualization rendering can be slow for complex plots
- Vue.js dev server enables hot-reload for quick iteration
- Production builds are optimized and minified

### Security Notes
- No sensitive data or credentials should be committed
- Use environment variables for any API keys in cloud lessons
- Azure-related lessons may require Azure account credentials
- Keep dependencies updated for security patches

## Contributing to Translations
- Automated translations managed via GitHub Actions
- Manual corrections welcomed for translation accuracy
- Follow existing translation folder structure
- Update quiz links to include language parameter: `?loc=fr`
- Test translated lessons for proper rendering

## Related Resources
- Main curriculum: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Discussion Forum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Other Microsoft curricula: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Project Maintenance
- Regular updates to keep content current
- Community contributions welcome
- Issues tracked on GitHub
- PRs reviewed by curriculum maintainers
- Monthly content reviews and updates
