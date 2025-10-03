<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T13:18:40+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "es"
}
-->
# Contribuir a Ciencia de Datos para Principiantes

¡Gracias por tu interés en contribuir al currículo de Ciencia de Datos para Principiantes! Apreciamos las contribuciones de la comunidad.

## Tabla de Contenidos

- [Código de Conducta](../..)
- [¿Cómo puedo contribuir?](../..)
- [Primeros pasos](../..)
- [Guías de contribución](../..)
- [Proceso de Pull Request](../..)
- [Guías de estilo](../..)
- [Acuerdo de Licencia para Contribuidores](../..)

## Código de Conducta

Este proyecto ha adoptado el [Código de Conducta de Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).  
Para más información, consulta las [Preguntas Frecuentes sobre el Código de Conducta](https://opensource.microsoft.com/codeofconduct/faq/)  
o contacta a [opencode@microsoft.com](mailto:opencode@microsoft.com) para cualquier pregunta o comentario adicional.

## ¿Cómo puedo contribuir?

### Reportar errores

Antes de crear reportes de errores, revisa los problemas existentes para evitar duplicados. Al crear un reporte de error, incluye tantos detalles como sea posible:

- **Usa un título claro y descriptivo**  
- **Describe los pasos exactos para reproducir el problema**  
- **Proporciona ejemplos específicos** (fragmentos de código, capturas de pantalla)  
- **Describe el comportamiento observado y lo que esperabas**  
- **Incluye detalles de tu entorno** (SO, versión de Python, navegador)

### Sugerir mejoras

¡Las sugerencias de mejoras son bienvenidas! Al sugerir mejoras:

- **Usa un título claro y descriptivo**  
- **Proporciona una descripción detallada de la mejora sugerida**  
- **Explica por qué esta mejora sería útil**  
- **Enumera características similares en otros proyectos, si aplica**

### Contribuir a la documentación

Las mejoras en la documentación siempre son apreciadas:

- **Corrige errores tipográficos y gramaticales**  
- **Mejora la claridad de las explicaciones**  
- **Añade documentación faltante**  
- **Actualiza información desactualizada**  
- **Incluye ejemplos o casos de uso**

### Contribuir con código

Aceptamos contribuciones de código, incluyendo:

- **Nuevas lecciones o ejercicios**  
- **Corrección de errores**  
- **Mejoras a notebooks existentes**  
- **Nuevos conjuntos de datos o ejemplos**  
- **Mejoras a la aplicación de cuestionarios**

## Primeros pasos

### Requisitos previos

Antes de contribuir, asegúrate de tener:

1. Una cuenta de GitHub  
2. Git instalado en tu sistema  
3. Python 3.7+ y Jupyter instalados  
4. Node.js y npm (para contribuciones a la aplicación de cuestionarios)  
5. Familiaridad con la estructura del currículo  

Consulta [INSTALLATION.md](INSTALLATION.md) para instrucciones detalladas de configuración.

### Hacer un fork y clonar

1. **Haz un fork del repositorio** en GitHub  
2. **Clona tu fork** localmente:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Añade el remoto upstream**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Crear una rama

Crea una nueva rama para tu trabajo:  
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Convenciones para nombrar ramas:  
- `feature/` - Nuevas características o lecciones  
- `fix/` - Corrección de errores  
- `docs/` - Cambios en la documentación  
- `refactor/` - Refactorización de código  

## Guías de contribución

### Para contenido de lecciones

Al contribuir con lecciones o modificar las existentes:

1. **Sigue la estructura existente**:  
   - README.md con el contenido de la lección  
   - Notebook de Jupyter con ejercicios  
   - Tarea (si aplica)  
   - Enlace a cuestionarios previos y posteriores  

2. **Incluye estos elementos**:  
   - Objetivos de aprendizaje claros  
   - Explicaciones paso a paso  
   - Ejemplos de código con comentarios  
   - Ejercicios para practicar  
   - Enlaces a recursos adicionales  

3. **Asegúrate de que sea accesible**:  
   - Usa lenguaje claro y sencillo  
   - Proporciona texto alternativo para imágenes  
   - Incluye comentarios en el código  
   - Considera diferentes estilos de aprendizaje  

### Para notebooks de Jupyter

1. **Limpia todas las salidas** antes de hacer el commit:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Incluye celdas de markdown** con explicaciones  

3. **Usa un formato consistente**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Prueba tu notebook** completamente antes de enviarlo  

### Para código en Python

Sigue las guías de estilo de [PEP 8](https://www.python.org/dev/peps/pep-0008/):  
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
  

### Para contribuciones a la aplicación de cuestionarios

Al modificar la aplicación de cuestionarios:

1. **Prueba localmente**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Ejecuta el linter**:  
   ```bash
   npm run lint
   ```
  
3. **Construye exitosamente**:  
   ```bash
   npm run build
   ```
  
4. **Sigue la guía de estilo de Vue.js** y los patrones existentes  

### Para traducciones

Al añadir o actualizar traducciones:

1. Sigue la estructura en la carpeta `translations/`  
2. Usa el código de idioma como nombre de carpeta (por ejemplo, `fr` para francés)  
3. Mantén la misma estructura de archivos que la versión en inglés  
4. Actualiza los enlaces de los cuestionarios para incluir el parámetro de idioma: `?loc=fr`  
5. Prueba todos los enlaces y el formato  

## Proceso de Pull Request

### Antes de enviar

1. **Actualiza tu rama** con los últimos cambios:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Prueba tus cambios**:  
   - Ejecuta todos los notebooks modificados  
   - Prueba la aplicación de cuestionarios si fue modificada  
   - Verifica que todos los enlaces funcionen  
   - Revisa errores ortográficos y gramaticales  

3. **Haz commit de tus cambios**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Escribe mensajes de commit claros:  
   - Usa tiempo presente ("Añadir característica" en lugar de "Añadido característica")  
   - Usa modo imperativo ("Mover cursor a..." en lugar de "Mueve cursor a...")  
   - Limita la primera línea a 72 caracteres  
   - Referencia problemas y pull requests cuando sea relevante  

4. **Haz push a tu fork**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Crear el Pull Request

1. Ve al [repositorio](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Haz clic en "Pull requests" → "New pull request"  
3. Haz clic en "compare across forks"  
4. Selecciona tu fork y rama  
5. Haz clic en "Create pull request"  

### Formato del título del PR

Usa títulos claros y descriptivos siguiendo este formato:  
```
[Component] Brief description
```
  
Ejemplos:  
- `[Lesson 7] Fix Python notebook import error`  
- `[Quiz App] Add German translation`  
- `[Docs] Update README with new prerequisites`  
- `[Fix] Correct data path in visualization lesson`  

### Descripción del PR

Incluye en la descripción de tu PR:

- **Qué**: ¿Qué cambios realizaste?  
- **Por qué**: ¿Por qué son necesarios estos cambios?  
- **Cómo**: ¿Cómo implementaste los cambios?  
- **Pruebas**: ¿Cómo probaste los cambios?  
- **Capturas de pantalla**: Incluye capturas para cambios visuales  
- **Problemas relacionados**: Enlace a problemas relacionados (por ejemplo, "Fixes #123")  

### Proceso de revisión

1. **Se ejecutarán verificaciones automáticas** en tu PR  
2. **Los mantenedores revisarán** tu contribución  
3. **Aborda los comentarios** realizando commits adicionales  
4. Una vez aprobado, un **mantenedor fusionará** tu PR  

### Después de que tu PR sea fusionado

1. Elimina tu rama:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Actualiza tu fork:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Guías de estilo

### Markdown

- Usa niveles de encabezado consistentes  
- Incluye líneas en blanco entre secciones  
- Usa bloques de código con especificadores de lenguaje:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Añade texto alternativo a las imágenes: `![Texto alternativo](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.es.png)`  
- Mantén las líneas con una longitud razonable (alrededor de 80-100 caracteres)  

### Python

- Sigue la guía de estilo PEP 8  
- Usa nombres de variables significativos  
- Añade docstrings a las funciones  
- Incluye sugerencias de tipo cuando sea apropiado:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Sigue la guía de estilo de Vue.js 2  
- Usa la configuración de ESLint proporcionada  
- Escribe componentes modulares y reutilizables  
- Añade comentarios para lógica compleja  

### Organización de archivos

- Mantén los archivos relacionados juntos  
- Usa nombres de archivo descriptivos  
- Sigue la estructura de directorios existente  
- No hagas commit de archivos innecesarios (.DS_Store, .pyc, node_modules, etc.)

## Acuerdo de Licencia para Contribuidores

Este proyecto acepta contribuciones y sugerencias. La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia para Contribuidores (CLA) declarando que tienes el derecho de, y efectivamente, nos otorgas los derechos para usar tu contribución. Para más detalles, visita  
https://cla.microsoft.com.

Cuando envíes un pull request, un bot de CLA determinará automáticamente si necesitas proporcionar un CLA y decorará el PR apropiadamente (por ejemplo, etiqueta, comentario). Simplemente sigue las instrucciones proporcionadas por el bot. Solo necesitarás hacer esto una vez en todos los repositorios que usen nuestro CLA.

## ¿Preguntas?

- Consulta nuestro [Canal de Discord #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Únete a nuestra [comunidad de Discord](https://aka.ms/ds4beginners/discord)  
- Revisa los [problemas existentes](https://github.com/microsoft/Data-Science-For-Beginners/issues) y [pull requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls)  

## ¡Gracias!

Tus contribuciones hacen que este currículo sea mejor para todos. ¡Gracias por tomarte el tiempo de contribuir!

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.