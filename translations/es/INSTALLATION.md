<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:13:59+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "es"
}
-->
# Guía de Instalación

Esta guía te ayudará a configurar tu entorno para trabajar con el plan de estudios de Ciencia de Datos para Principiantes.

## Tabla de Contenidos

- [Requisitos previos](../..)
- [Opciones de inicio rápido](../..)
- [Instalación local](../..)
- [Verificar tu instalación](../..)

## Requisitos previos

Antes de comenzar, deberías tener:

- Familiaridad básica con la línea de comandos/terminal
- Una cuenta de GitHub (gratuita)
- Conexión a internet estable para la configuración inicial

## Opciones de inicio rápido

### Opción 1: GitHub Codespaces (Recomendado para principiantes)

La forma más fácil de comenzar es con GitHub Codespaces, que proporciona un entorno de desarrollo completo en tu navegador.

1. Ve al [repositorio](https://github.com/microsoft/Data-Science-For-Beginners)
2. Haz clic en el menú desplegable **Code**
3. Selecciona la pestaña **Codespaces**
4. Haz clic en **Create codespace on main**
5. Espera a que el entorno se inicialice (2-3 minutos)

¡Tu entorno ahora está listo con todas las dependencias preinstaladas!

### Opción 2: Desarrollo local

Para trabajar en tu propia computadora, sigue las instrucciones detalladas a continuación.

## Instalación local

### Paso 1: Instalar Git

Git es necesario para clonar el repositorio y realizar un seguimiento de tus cambios.

**Windows:**
- Descarga desde [git-scm.com](https://git-scm.com/download/win)
- Ejecuta el instalador con la configuración predeterminada

**macOS:**
- Instala mediante Homebrew: `brew install git`
- O descarga desde [git-scm.com](https://git-scm.com/download/mac)

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### Paso 2: Clonar el repositorio

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Paso 3: Instalar Python y Jupyter

Se requiere Python 3.7 o superior para las lecciones de ciencia de datos.

**Windows:**
1. Descarga Python desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, marca "Add Python to PATH"
3. Verifica la instalación:
```bash
python --version
```

**macOS:**
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

**Linux:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### Paso 4: Configurar el entorno de Python

Se recomienda usar un entorno virtual para mantener las dependencias aisladas.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Paso 5: Instalar paquetes de Python

Instala las bibliotecas necesarias para ciencia de datos:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Paso 6: Instalar Node.js y npm (Para la aplicación de cuestionarios)

La aplicación de cuestionarios requiere Node.js y npm.

**Windows/macOS:**
- Descarga desde [nodejs.org](https://nodejs.org/) (se recomienda la versión LTS)
- Ejecuta el instalador

**Linux:**
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

### Paso 7: Instalar dependencias de la aplicación de cuestionarios

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Paso 8: Instalar Docsify (Opcional)

Para acceso offline a la documentación:

```bash
npm install -g docsify-cli
```

## Verificar tu instalación

### Probar Python y Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Tu navegador debería abrirse con la interfaz de Jupyter. Ahora puedes navegar a cualquier archivo `.ipynb` de las lecciones.

### Probar la aplicación de cuestionarios

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

La aplicación de cuestionarios debería estar disponible en `http://localhost:8080` (o en otro puerto si el 8080 está ocupado).

### Probar el servidor de documentación

```bash
# From the root directory of the repository
docsify serve
```

La documentación debería estar disponible en `http://localhost:3000`.

## Usar contenedores de desarrollo de VS Code

Si tienes Docker instalado, puedes usar contenedores de desarrollo de VS Code:

1. Instala [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Instala [Visual Studio Code](https://code.visualstudio.com/)
3. Instala la extensión [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Abre el repositorio en VS Code
5. Presiona `F1` y selecciona "Remote-Containers: Reopen in Container"
6. Espera a que el contenedor se construya (solo la primera vez)

## Próximos pasos

- Explora el [README.md](README.md) para obtener una visión general del plan de estudios
- Lee [USAGE.md](USAGE.md) para flujos de trabajo comunes y ejemplos
- Consulta [TROUBLESHOOTING.md](TROUBLESHOOTING.md) si encuentras problemas
- Revisa [CONTRIBUTING.md](CONTRIBUTING.md) si deseas contribuir

## Obtener ayuda

Si encuentras problemas:

1. Consulta la guía [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Busca problemas existentes en [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Únete a nuestra [comunidad de Discord](https://aka.ms/ds4beginners/discord)
4. Crea un nuevo problema con información detallada sobre tu situación

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.