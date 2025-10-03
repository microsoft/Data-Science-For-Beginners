<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:52:04+00:00",
  "source_file": "USAGE.md",
  "language_code": "es"
}
-->
# Guía de Uso

Esta guía proporciona ejemplos y flujos de trabajo comunes para utilizar el currículo de Ciencia de Datos para Principiantes.

## Tabla de Contenidos

- [Cómo Usar Este Currículo](../..)
- [Trabajando con las Lecciones](../..)
- [Trabajando con Jupyter Notebooks](../..)
- [Usando la Aplicación de Cuestionarios](../..)
- [Flujos de Trabajo Comunes](../..)
- [Consejos para Autoaprendices](../..)
- [Consejos para Profesores](../..)

## Cómo Usar Este Currículo

Este currículo está diseñado para ser flexible y puede utilizarse de varias maneras:

- **Aprendizaje autodidacta**: Trabaja en las lecciones de forma independiente a tu propio ritmo.
- **Instrucción en el aula**: Úsalo como un curso estructurado con instrucción guiada.
- **Grupos de estudio**: Aprende de manera colaborativa con compañeros.
- **Formato de taller**: Sesiones intensivas de aprendizaje a corto plazo.

## Trabajando con las Lecciones

Cada lección sigue una estructura consistente para maximizar el aprendizaje:

### Estructura de la Lección

1. **Cuestionario previo a la lección**: Evalúa tus conocimientos existentes.
2. **Sketchnote** (Opcional): Resumen visual de conceptos clave.
3. **Video** (Opcional): Contenido de video complementario.
4. **Lección escrita**: Conceptos principales y explicaciones.
5. **Jupyter Notebook**: Ejercicios prácticos de codificación.
6. **Asignación**: Practica lo que has aprendido.
7. **Cuestionario posterior a la lección**: Refuerza tu comprensión.

### Ejemplo de Flujo de Trabajo para una Lección

```bash
# 1. Navigate to the lesson directory
cd 1-Introduction/01-defining-data-science

# 2. Read the README.md
# Open README.md in your browser or editor

# 3. Take the pre-lesson quiz
# Click the quiz link in the README

# 4. Open the Jupyter notebook (if available)
jupyter notebook

# 5. Complete the exercises in the notebook

# 6. Work on the assignment

# 7. Take the post-lesson quiz
```

## Trabajando con Jupyter Notebooks

### Iniciando Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Ejecutando Celdas del Notebook

1. **Ejecutar una celda**: Presiona `Shift + Enter` o haz clic en el botón "Run".
2. **Ejecutar todas las celdas**: Selecciona "Cell" → "Run All" en el menú.
3. **Reiniciar el kernel**: Selecciona "Kernel" → "Restart" si encuentras problemas.

### Ejemplo: Trabajando con Datos en un Notebook

```python
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load a dataset
df = pd.read_csv('data/sample.csv')

# Explore the data
df.head()
df.info()
df.describe()

# Create a visualization
plt.figure(figsize=(10, 6))
plt.plot(df['column_name'])
plt.title('Sample Visualization')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```

### Guardando tu Trabajo

- Jupyter guarda automáticamente de forma periódica.
- Guardar manualmente: Presiona `Ctrl + S` (o `Cmd + S` en macOS).
- Tu progreso se guarda en el archivo `.ipynb`.

## Usando la Aplicación de Cuestionarios

### Ejecutando la Aplicación de Cuestionarios Localmente

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Realizando Cuestionarios

1. Los cuestionarios previos a la lección están vinculados al inicio de cada lección.
2. Los cuestionarios posteriores a la lección están vinculados al final de cada lección.
3. Cada cuestionario tiene 3 preguntas.
4. Los cuestionarios están diseñados para reforzar el aprendizaje, no para evaluar exhaustivamente.

### Numeración de Cuestionarios

- Los cuestionarios están numerados del 0 al 39 (40 cuestionarios en total).
- Cada lección generalmente tiene un cuestionario previo y posterior.
- Las URLs de los cuestionarios incluyen el número del cuestionario: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Flujos de Trabajo Comunes

### Flujo de Trabajo 1: Ruta para Principiantes Completos

```bash
# 1. Set up your environment (see INSTALLATION.md)

# 2. Start with Lesson 1
cd 1-Introduction/01-defining-data-science

# 3. For each lesson:
#    - Take pre-lesson quiz
#    - Read the lesson content
#    - Work through the notebook
#    - Complete the assignment
#    - Take post-lesson quiz

# 4. Progress through all 20 lessons sequentially
```

### Flujo de Trabajo 2: Aprendizaje Específico por Tema

Si te interesa un tema específico:

```bash
# Example: Focus on Data Visualization
cd 3-Data-Visualization

# Explore lessons 9-13:
# - Lesson 9: Visualizing Quantities
# - Lesson 10: Visualizing Distributions
# - Lesson 11: Visualizing Proportions
# - Lesson 12: Visualizing Relationships
# - Lesson 13: Meaningful Visualizations
```

### Flujo de Trabajo 3: Aprendizaje Basado en Proyectos

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Flujo de Trabajo 4: Ciencia de Datos en la Nube

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Consejos para Autoaprendices

### Mantente Organizado

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Practica Regularmente

- Dedica tiempo específico cada día o semana.
- Completa al menos una lección por semana.
- Revisa lecciones anteriores periódicamente.

### Participa en la Comunidad

- Únete a la [comunidad de Discord](https://aka.ms/ds4beginners/discord).
- Participa en el canal #Data-Science-for-Beginners en Discord [Discusiones en Discord](https://aka.ms/ds4beginners/discord).
- Comparte tu progreso y haz preguntas.

### Crea Tus Propios Proyectos

Después de completar las lecciones, aplica los conceptos en proyectos personales:

```python
# Example: Analyze your own dataset
import pandas as pd

# Load your own data
my_data = pd.read_csv('my-project/data.csv')

# Apply techniques learned
# - Data cleaning (Lesson 8)
# - Exploratory data analysis (Lesson 7)
# - Visualization (Lessons 9-13)
# - Analysis (Lesson 15)
```

## Consejos para Profesores

### Configuración del Aula

1. Revisa [for-teachers.md](for-teachers.md) para obtener orientación detallada.
2. Configura un entorno compartido (GitHub Classroom o Codespaces).
3. Establece un canal de comunicación (Discord, Slack o Teams).

### Planificación de Lecciones

**Horario sugerido de 10 semanas:**

- **Semana 1-2**: Introducción (Lecciones 1-4).
- **Semana 3-4**: Trabajando con Datos (Lecciones 5-8).
- **Semana 5-6**: Visualización de Datos (Lecciones 9-13).
- **Semana 7-8**: Ciclo de Vida de la Ciencia de Datos (Lecciones 14-16).
- **Semana 9**: Ciencia de Datos en la Nube (Lecciones 17-19).
- **Semana 10**: Aplicaciones del Mundo Real y Proyectos Finales (Lección 20).

### Ejecutando Docsify para Acceso Sin Conexión

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Evaluación de Asignaciones

- Revisa los notebooks de los estudiantes para verificar ejercicios completados.
- Evalúa la comprensión a través de los puntajes de los cuestionarios.
- Evalúa los proyectos finales utilizando principios del ciclo de vida de la ciencia de datos.

### Creando Asignaciones

```python
# Example custom assignment template
"""
Assignment: [Topic]

Objective: [Learning goal]

Dataset: [Provide or have students find one]

Tasks:
1. Load and explore the dataset
2. Clean and prepare the data
3. Create at least 3 visualizations
4. Perform analysis
5. Communicate findings

Deliverables:
- Jupyter notebook with code and explanations
- Written summary of findings
"""
```

## Trabajando Sin Conexión

### Descargar Recursos

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Ejecutar Documentación Localmente

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Ejecutar la Aplicación de Cuestionarios Localmente

```bash
cd quiz-app
npm run serve
```

## Accediendo a Contenido Traducido

Las traducciones están disponibles en más de 40 idiomas:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Cada traducción mantiene la misma estructura que la versión en inglés.

## Recursos Adicionales

### Continuar Aprendiendo

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Rutas de aprendizaje adicionales.
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Recursos para estudiantes.
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Foro comunitario.

### Currículos Relacionados

- [AI para Principiantes](https://aka.ms/ai-beginners).
- [ML para Principiantes](https://aka.ms/ml-beginners).
- [Desarrollo Web para Principiantes](https://aka.ms/webdev-beginners).
- [Generative AI para Principiantes](https://aka.ms/genai-beginners).

## Obteniendo Ayuda

- Revisa [TROUBLESHOOTING.md](TROUBLESHOOTING.md) para problemas comunes.
- Busca en [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues).
- Únete a nuestro [Discord](https://aka.ms/ds4beginners/discord).
- Revisa [CONTRIBUTING.md](CONTRIBUTING.md) para reportar problemas o contribuir.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.