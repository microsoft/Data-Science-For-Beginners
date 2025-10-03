<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:28:59+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "es"
}
-->
# Guía de Solución de Problemas

Esta guía ofrece soluciones a problemas comunes que podrías encontrar mientras trabajas con el currículo de Ciencia de Datos para Principiantes.

## Tabla de Contenidos

- [Problemas con Python y Jupyter](../..)
- [Problemas con Paquetes y Dependencias](../..)
- [Problemas con Jupyter Notebook](../..)
- [Problemas con la Aplicación de Cuestionarios](../..)
- [Problemas con Git y GitHub](../..)
- [Problemas con la Documentación Docsify](../..)
- [Problemas con Datos y Archivos](../..)
- [Problemas de Rendimiento](../..)
- [Obteniendo Ayuda Adicional](../..)

## Problemas con Python y Jupyter

### Python No Encontrado o Versión Incorrecta

**Problema:** `python: command not found` o versión incorrecta de Python

**Solución:**

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

**Solución en Windows:**
1. Reinstala Python desde [python.org](https://www.python.org/)
2. Durante la instalación, marca "Add Python to PATH"
3. Reinicia tu terminal o línea de comandos

### Problemas de Activación del Entorno Virtual

**Problema:** El entorno virtual no se activa

**Solución:**

**Windows:**
```bash
# If you get execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Ensure the activate script is executable
chmod +x venv/bin/activate

# Then activate
source venv/bin/activate
```

**Verifica la activación:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Problemas con el Kernel de Jupyter

**Problema:** "Kernel no encontrado" o "El kernel sigue fallando"

**Solución:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problema:** Versión incorrecta de Python en Jupyter

**Solución:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Problemas con Paquetes y Dependencias

### Errores de Importación

**Problema:** `ModuleNotFoundError: No module named 'pandas'` (u otros paquetes)

**Solución:**

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

### Fallos en la Instalación con Pip

**Problema:** `pip install` falla con errores de permisos

**Solución:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problema:** `pip install` falla con errores de certificados SSL

**Solución:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Conflictos de Versiones de Paquetes

**Problema:** Versiones incompatibles de paquetes

**Solución:**

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

## Problemas con Jupyter Notebook

### Jupyter No Inicia

**Problema:** El comando `jupyter notebook` no se encuentra

**Solución:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### El Notebook No Carga o No Guarda

**Problema:** "Notebook failed to load" o errores al guardar

**Solución:**

1. Verifica los permisos del archivo
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Revisa si el archivo está corrupto
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Limpia la caché de Jupyter
```bash
jupyter notebook --clear-cache
```

### La Celda No Se Ejecuta

**Problema:** La celda se queda en "In [*]" o tarda demasiado

**Solución:**

1. **Interrumpe el kernel**: Haz clic en el botón "Interrupt" o presiona `I, I`
2. **Reinicia el kernel**: Menú Kernel → Restart
3. **Revisa si hay bucles infinitos** en tu código
4. **Limpia la salida**: Cell → All Output → Clear

### Gráficos No Se Muestran

**Problema:** Los gráficos de `matplotlib` no aparecen en el notebook

**Solución:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternativa para gráficos interactivos:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Problemas con la Aplicación de Cuestionarios

### Fallos en npm install

**Problema:** Errores durante `npm install`

**Solución:**

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

### La Aplicación de Cuestionarios No Inicia

**Problema:** `npm run serve` falla

**Solución:**

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

### Puerto Ya en Uso

**Problema:** "Port 8080 is already in use"

**Solución:**

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

### Cuestionario No Carga o Página en Blanco

**Problema:** La aplicación de cuestionarios carga pero muestra una página en blanco

**Solución:**

1. Revisa los errores en la consola del navegador (F12)
2. Limpia la caché y las cookies del navegador
3. Prueba con otro navegador
4. Asegúrate de que JavaScript esté habilitado
5. Verifica si los bloqueadores de anuncios están interfiriendo

```bash
# Rebuild the app
npm run build
npm run serve
```

## Problemas con Git y GitHub

### Git No Reconocido

**Problema:** `git: command not found`

**Solución:**

**Windows:**
- Instala Git desde [git-scm.com](https://git-scm.com/)
- Reinicia el terminal después de la instalación

**macOS:**

> **Nota:** Si no tienes Homebrew instalado, sigue las instrucciones en [https://brew.sh/](https://brew.sh/) para instalarlo primero.
```bash
# Install via Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

**Linux:**
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo dnf install git      # Fedora
```

### Fallos al Clonar

**Problema:** `git clone` falla con errores de autenticación

**Solución:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permiso Denegado (publickey)

**Problema:** Fallos en la autenticación con clave SSH

**Solución:**

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

## Problemas con la Documentación Docsify

### Comando Docsify No Encontrado

**Problema:** `docsify: command not found`

**Solución:**

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

### La Documentación No Carga

**Problema:** Docsify se ejecuta pero el contenido no carga

**Solución:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Imágenes No Se Muestran

**Problema:** Las imágenes muestran el ícono de enlace roto

**Solución:**

1. Verifica que las rutas de las imágenes sean relativas
2. Asegúrate de que los archivos de imagen existan en el repositorio
3. Limpia la caché del navegador
4. Verifica que las extensiones de los archivos coincidan (sensible a mayúsculas en algunos sistemas)

## Problemas con Datos y Archivos

### Errores de Archivo No Encontrado

**Problema:** `FileNotFoundError` al cargar datos

**Solución:**

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

### Errores al Leer CSV

**Problema:** Errores al leer archivos CSV

**Solución:**

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

### Errores de Memoria con Conjuntos de Datos Grandes

**Problema:** `MemoryError` al cargar archivos grandes

**Solución:**

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

## Problemas de Rendimiento

### Rendimiento Lento del Notebook

**Problema:** Los notebooks se ejecutan muy lentamente

**Solución:**

1. **Reinicia el kernel y limpia la salida**
   - Kernel → Restart & Clear Output

2. **Cierra notebooks que no estés usando**

3. **Optimiza el código:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Muestra una muestra de conjuntos de datos grandes:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Fallos del Navegador

**Problema:** El navegador falla o se vuelve no responsivo

**Solución:**

1. Cierra pestañas que no estés usando
2. Limpia la caché del navegador
3. Aumenta la memoria del navegador (Chrome: `chrome://settings/system`)
4. Usa JupyterLab en lugar de Jupyter Notebook:
```bash
pip install jupyterlab
jupyter lab
```

## Obteniendo Ayuda Adicional

### Antes de Pedir Ayuda

1. Revisa esta guía de solución de problemas
2. Busca en [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Consulta [INSTALLATION.md](INSTALLATION.md) y [USAGE.md](USAGE.md)
4. Intenta buscar el mensaje de error en línea

### Cómo Pedir Ayuda

Cuando crees un problema o pidas ayuda, incluye:

1. **Sistema Operativo**: Windows, macOS o Linux (qué distribución)
2. **Versión de Python**: Ejecuta `python --version`
3. **Mensaje de Error**: Copia el mensaje de error completo
4. **Pasos para Reproducir**: Qué hiciste antes de que ocurriera el error
5. **Qué Has Intentado**: Soluciones que ya intentaste

**Ejemplo:**
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

### Recursos Comunitarios

- **GitHub Issues**: [Crea un problema](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Únete a nuestra comunidad](https://aka.ms/ds4beginners/discord)
- **Discussions**: [Discusiones en GitHub](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Foros de preguntas y respuestas](https://docs.microsoft.com/answers/)

### Documentación Relacionada

- [INSTALLATION.md](INSTALLATION.md) - Instrucciones de configuración
- [USAGE.md](USAGE.md) - Cómo usar el currículo
- [CONTRIBUTING.md](CONTRIBUTING.md) - Cómo contribuir
- [README.md](README.md) - Descripción general del proyecto

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.