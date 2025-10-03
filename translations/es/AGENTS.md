<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T10:59:35+00:00",
  "source_file": "AGENTS.md",
  "language_code": "es"
}
-->
# AGENTS.md

## Resumen del Proyecto

Data Science for Beginners es un plan de estudios completo de 10 semanas y 20 lecciones creado por los Azure Cloud Advocates de Microsoft. El repositorio es un recurso de aprendizaje que enseña conceptos fundamentales de ciencia de datos a través de lecciones basadas en proyectos, incluyendo notebooks de Jupyter, cuestionarios interactivos y tareas prácticas.

**Tecnologías Clave:**
- **Jupyter Notebooks**: Medio principal de aprendizaje utilizando Python 3
- **Bibliotecas de Python**: pandas, numpy, matplotlib para análisis y visualización de datos
- **Vue.js 2**: Aplicación de cuestionarios (carpeta quiz-app)
- **Docsify**: Generador de sitios de documentación para acceso offline
- **Node.js/npm**: Gestión de paquetes para componentes JavaScript
- **Markdown**: Todo el contenido de las lecciones y documentación

**Arquitectura:**
- Repositorio educativo multilingüe con extensas traducciones
- Estructurado en módulos de lecciones (1-Introducción hasta 6-Ciencia-de-Datos-en-el-Mundo)
- Cada lección incluye README, notebooks, tareas y cuestionarios
- Aplicación de cuestionarios Vue.js independiente para evaluaciones antes/después de las lecciones
- Soporte para GitHub Codespaces y contenedores de desarrollo en VS Code

## Comandos de Configuración

### Configuración del Repositorio
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Configuración del Entorno de Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Configuración de la Aplicación de Cuestionarios
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

### Servidor de Documentación Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Configuración de Proyectos de Visualización
Para proyectos de visualización como meaningful-visualizations (lección 13):
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


## Flujo de Trabajo de Desarrollo

### Trabajando con Jupyter Notebooks
1. Inicia Jupyter en la raíz del repositorio: `jupyter notebook`
2. Navega a la carpeta de la lección deseada
3. Abre los archivos `.ipynb` para trabajar en los ejercicios
4. Los notebooks son autónomos con explicaciones y celdas de código
5. La mayoría de los notebooks utilizan pandas, numpy y matplotlib; asegúrate de que estén instalados

### Estructura de las Lecciones
Cada lección típicamente contiene:
- `README.md` - Contenido principal de la lección con teoría y ejemplos
- `notebook.ipynb` - Ejercicios prácticos en Jupyter notebook
- `assignment.ipynb` o `assignment.md` - Tareas prácticas
- Carpeta `solution/` - Notebooks y código de solución
- Carpeta `images/` - Materiales visuales de apoyo

### Desarrollo de la Aplicación de Cuestionarios
- Aplicación Vue.js 2 con recarga en caliente durante el desarrollo
- Cuestionarios almacenados en `quiz-app/src/assets/translations/`
- Cada idioma tiene su propia carpeta de traducción (en, fr, es, etc.)
- La numeración de los cuestionarios comienza en 0 y llega hasta 39 (40 cuestionarios en total)

### Agregar Traducciones
- Las traducciones se colocan en la carpeta `translations/` en la raíz del repositorio
- Cada idioma tiene una estructura completa de lecciones reflejada desde el inglés
- Traducción automatizada mediante GitHub Actions (co-op-translator.yml)

## Instrucciones de Pruebas

### Pruebas de la Aplicación de Cuestionarios
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Pruebas de Notebooks
- No existe un marco de pruebas automatizado para notebooks
- Validación manual: Ejecuta todas las celdas en secuencia para asegurarte de que no haya errores
- Verifica que los archivos de datos sean accesibles y que los resultados se generen correctamente
- Comprueba que las visualizaciones se rendericen adecuadamente

### Pruebas de Documentación
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Verificaciones de Calidad de Código
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Guías de Estilo de Código

### Python (Jupyter Notebooks)
- Sigue las guías de estilo PEP 8 para código Python
- Usa nombres de variables claros que expliquen los datos que se están analizando
- Incluye celdas de markdown con explicaciones antes de las celdas de código
- Mantén las celdas de código enfocadas en conceptos u operaciones individuales
- Utiliza pandas para manipulación de datos, matplotlib para visualización
- Patrón común de importación:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Sigue la guía de estilo de Vue.js 2 y las mejores prácticas
- Configuración de ESLint en `quiz-app/package.json`
- Usa componentes de archivo único de Vue (.vue files)
- Mantén una arquitectura basada en componentes
- Ejecuta `npm run lint` antes de confirmar cambios

### Documentación en Markdown
- Usa una jerarquía clara de encabezados (# ## ### etc.)
- Incluye bloques de código con especificadores de lenguaje
- Agrega texto alternativo para imágenes
- Enlaza a lecciones y recursos relacionados
- Mantén longitudes de línea razonables para facilitar la lectura

### Organización de Archivos
- Contenido de las lecciones en carpetas numeradas (01-definiendo-ciencia-de-datos, etc.)
- Soluciones en subcarpetas dedicadas `solution/`
- Las traducciones reflejan la estructura en inglés en la carpeta `translations/`
- Mantén los archivos de datos en `data/` o carpetas específicas de las lecciones

## Construcción y Despliegue

### Despliegue de la Aplicación de Cuestionarios
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Despliegue de Azure Static Web Apps
La aplicación quiz-app puede desplegarse en Azure Static Web Apps:
1. Crea un recurso de Azure Static Web App
2. Conéctalo al repositorio de GitHub
3. Configura los ajustes de construcción:
   - Ubicación de la aplicación: `quiz-app`
   - Ubicación de salida: `dist`
4. El flujo de trabajo de GitHub Actions se encargará del despliegue automático al realizar un push

### Sitio de Documentación
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- El repositorio incluye configuración de contenedor de desarrollo
- Codespaces configura automáticamente el entorno de Python y Node.js
- Abre el repositorio en Codespace a través de la interfaz de GitHub
- Todas las dependencias se instalan automáticamente

## Guías para Pull Requests

### Antes de Enviar
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Formato del Título de PR
- Usa títulos claros y descriptivos
- Formato: `[Componente] Breve descripción`
- Ejemplos:
  - `[Lección 7] Corrige error de importación en notebook de Python`
  - `[Aplicación de Cuestionarios] Agrega traducción al alemán`
  - `[Documentación] Actualiza README con nuevos requisitos`

### Verificaciones Requeridas
- Asegúrate de que todo el código se ejecute sin errores
- Verifica que los notebooks se ejecuten completamente
- Confirma que las aplicaciones Vue.js se construyan correctamente
- Comprueba que los enlaces de la documentación funcionen
- Prueba la aplicación de cuestionarios si fue modificada
- Verifica que las traducciones mantengan una estructura consistente

### Guías de Contribución
- Sigue el estilo y los patrones de código existentes
- Agrega comentarios explicativos para lógica compleja
- Actualiza la documentación relevante
- Prueba los cambios en diferentes módulos de lecciones si aplica
- Revisa el archivo CONTRIBUTING.md

## Notas Adicionales

### Bibliotecas Comunes Utilizadas
- **pandas**: Manipulación y análisis de datos
- **numpy**: Computación numérica
- **matplotlib**: Visualización y gráficos de datos
- **seaborn**: Visualización estadística de datos (algunas lecciones)
- **scikit-learn**: Aprendizaje automático (lecciones avanzadas)

### Trabajando con Archivos de Datos
- Archivos de datos ubicados en la carpeta `data/` o directorios específicos de las lecciones
- La mayoría de los notebooks esperan archivos de datos en rutas relativas
- Los archivos CSV son el formato principal de datos
- Algunas lecciones utilizan JSON para ejemplos de datos no relacionales

### Soporte Multilingüe
- Más de 40 traducciones de idiomas mediante GitHub Actions automatizadas
- Flujo de trabajo de traducción en `.github/workflows/co-op-translator.yml`
- Traducciones en la carpeta `translations/` con códigos de idioma
- Traducciones de cuestionarios en `quiz-app/src/assets/translations/`

### Opciones de Entorno de Desarrollo
1. **Desarrollo Local**: Instala Python, Jupyter, Node.js localmente
2. **GitHub Codespaces**: Entorno de desarrollo instantáneo basado en la nube
3. **Contenedores de Desarrollo en VS Code**: Desarrollo local basado en contenedores
4. **Binder**: Lanza notebooks en la nube (si está configurado)

### Guías de Contenido de las Lecciones
- Cada lección es autónoma pero se basa en conceptos previos
- Cuestionarios previos a la lección evalúan conocimientos previos
- Cuestionarios posteriores a la lección refuerzan el aprendizaje
- Las tareas proporcionan práctica práctica
- Los sketchnotes ofrecen resúmenes visuales

### Solución de Problemas Comunes

**Problemas con el Kernel de Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Fallos en npm Install:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Errores de Importación en Notebooks:**
- Verifica que todas las bibliotecas requeridas estén instaladas
- Comprueba la compatibilidad de la versión de Python (se recomienda Python 3.7+)
- Asegúrate de que el entorno virtual esté activado

**Docsify No Carga:**
- Verifica que estés sirviendo desde la raíz del repositorio
- Comprueba que `index.html` exista
- Asegúrate de tener acceso adecuado a la red (puerto 3000)

### Consideraciones de Rendimiento
- Los conjuntos de datos grandes pueden tardar en cargarse en los notebooks
- La renderización de visualizaciones puede ser lenta para gráficos complejos
- El servidor de desarrollo de Vue.js permite recarga en caliente para iteración rápida
- Las construcciones de producción están optimizadas y minificadas

### Notas de Seguridad
- No se deben comprometer datos sensibles ni credenciales
- Usa variables de entorno para cualquier clave API en lecciones en la nube
- Las lecciones relacionadas con Azure pueden requerir credenciales de cuenta de Azure
- Mantén las dependencias actualizadas para parches de seguridad

## Contribuyendo a las Traducciones
- Traducciones automatizadas gestionadas mediante GitHub Actions
- Correcciones manuales son bienvenidas para mejorar la precisión de las traducciones
- Sigue la estructura de carpetas de traducción existente
- Actualiza los enlaces de los cuestionarios para incluir el parámetro de idioma: `?loc=fr`
- Prueba las lecciones traducidas para verificar su correcta visualización

## Recursos Relacionados
- Plan de estudios principal: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Foro de Discusión: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Otros planes de estudios de Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Mantenimiento del Proyecto
- Actualizaciones regulares para mantener el contenido actualizado
- Contribuciones de la comunidad son bienvenidas
- Problemas rastreados en GitHub
- PRs revisados por los mantenedores del plan de estudios
- Revisiones y actualizaciones de contenido mensuales

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.