<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "577a611517482c3ceaf76d3d8142cba9",
  "translation_date": "2025-09-05T13:35:07+00:00",
  "source_file": "2-Working-With-Data/07-python/README.md",
  "language_code": "es"
}
-->
# Trabajando con Datos: Python y la Biblioteca Pandas

| ![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/07-WorkWithPython.png) |
| :-------------------------------------------------------------------------------------------------------: |
|                 Trabajando con Python - _Sketchnote por [@nitya](https://twitter.com/nitya)_                 |

[![Video Introductorio](../../../../2-Working-With-Data/07-python/images/video-ds-python.png)](https://youtu.be/dZjWOGbsN4Y)

Aunque las bases de datos ofrecen formas muy eficientes de almacenar datos y consultarlos utilizando lenguajes de consulta, la forma más flexible de procesar datos es escribir tu propio programa para manipularlos. En muchos casos, realizar una consulta en una base de datos sería una forma más efectiva. Sin embargo, en algunos casos, cuando se necesita un procesamiento de datos más complejo, no se puede realizar fácilmente utilizando SQL.  
El procesamiento de datos se puede programar en cualquier lenguaje de programación, pero hay ciertos lenguajes que son de nivel más alto en lo que respecta al trabajo con datos. Los científicos de datos suelen preferir uno de los siguientes lenguajes:

* **[Python](https://www.python.org/)**, un lenguaje de programación de propósito general, que a menudo se considera una de las mejores opciones para principiantes debido a su simplicidad. Python tiene muchas bibliotecas adicionales que pueden ayudarte a resolver muchos problemas prácticos, como extraer tus datos de un archivo ZIP o convertir una imagen a escala de grises. Además de la ciencia de datos, Python también se utiliza frecuentemente para el desarrollo web.  
* **[R](https://www.r-project.org/)** es una herramienta tradicional desarrollada con el procesamiento de datos estadísticos en mente. También contiene un gran repositorio de bibliotecas (CRAN), lo que lo convierte en una buena opción para el procesamiento de datos. Sin embargo, R no es un lenguaje de propósito general y rara vez se utiliza fuera del ámbito de la ciencia de datos.  
* **[Julia](https://julialang.org/)** es otro lenguaje desarrollado específicamente para la ciencia de datos. Está diseñado para ofrecer un mejor rendimiento que Python, lo que lo convierte en una excelente herramienta para la experimentación científica.  

En esta lección, nos centraremos en usar Python para un procesamiento de datos sencillo. Asumiremos que tienes un conocimiento básico del lenguaje. Si deseas un recorrido más profundo por Python, puedes consultar uno de los siguientes recursos:

* [Aprende Python de una manera divertida con gráficos de tortuga y fractales](https://github.com/shwars/pycourse) - Curso introductorio rápido basado en GitHub sobre programación en Python  
* [Da tus primeros pasos con Python](https://docs.microsoft.com/en-us/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) Ruta de aprendizaje en [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)  

Los datos pueden venir en muchas formas. En esta lección, consideraremos tres formas de datos: **datos tabulares**, **texto** e **imágenes**.

Nos centraremos en algunos ejemplos de procesamiento de datos, en lugar de ofrecerte una visión completa de todas las bibliotecas relacionadas. Esto te permitirá obtener la idea principal de lo que es posible y te dejará con el entendimiento de dónde encontrar soluciones a tus problemas cuando las necesites.

> **El consejo más útil**. Cuando necesites realizar una operación específica en datos que no sabes cómo hacer, intenta buscarla en internet. [Stackoverflow](https://stackoverflow.com/) suele contener muchos ejemplos útiles de código en Python para muchas tareas típicas.  

## [Cuestionario previo a la lección](https://ff-quizzes.netlify.app/en/ds/quiz/12)

## Datos Tabulares y Dataframes

Ya te has encontrado con datos tabulares cuando hablamos de bases de datos relacionales. Cuando tienes muchos datos y están contenidos en muchas tablas vinculadas diferentes, definitivamente tiene sentido usar SQL para trabajar con ellos. Sin embargo, hay muchos casos en los que tenemos una tabla de datos y necesitamos obtener algún **entendimiento** o **perspectiva** sobre estos datos, como la distribución, la correlación entre valores, etc. En la ciencia de datos, hay muchos casos en los que necesitamos realizar algunas transformaciones de los datos originales, seguidas de visualización. Ambos pasos se pueden realizar fácilmente utilizando Python.

Hay dos bibliotecas más útiles en Python que pueden ayudarte a trabajar con datos tabulares:  
* **[Pandas](https://pandas.pydata.org/)** te permite manipular los llamados **Dataframes**, que son análogos a las tablas relacionales. Puedes tener columnas con nombres y realizar diferentes operaciones en filas, columnas y dataframes en general.  
* **[Numpy](https://numpy.org/)** es una biblioteca para trabajar con **tensores**, es decir, **arreglos** multidimensionales. Un arreglo tiene valores del mismo tipo subyacente y es más simple que un dataframe, pero ofrece más operaciones matemáticas y genera menos sobrecarga.  

También hay un par de otras bibliotecas que deberías conocer:  
* **[Matplotlib](https://matplotlib.org/)** es una biblioteca utilizada para la visualización de datos y la creación de gráficos  
* **[SciPy](https://www.scipy.org/)** es una biblioteca con algunas funciones científicas adicionales. Ya nos hemos encontrado con esta biblioteca al hablar de probabilidad y estadística  

Aquí hay un fragmento de código que normalmente usarías para importar esas bibliotecas al inicio de tu programa en Python:  
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import ... # you need to specify exact sub-packages that you need
```  

Pandas se centra en unos pocos conceptos básicos.

### Series

**Series** es una secuencia de valores, similar a una lista o un arreglo de numpy. La principal diferencia es que las series también tienen un **índice**, y cuando operamos con series (por ejemplo, las sumamos), el índice se toma en cuenta. El índice puede ser tan simple como el número de fila entero (es el índice utilizado por defecto al crear una serie a partir de una lista o arreglo), o puede tener una estructura compleja, como un intervalo de fechas.

> **Nota**: Hay algo de código introductorio de Pandas en el cuaderno adjunto [`notebook.ipynb`](../../../../2-Working-With-Data/07-python/notebook.ipynb). Solo describimos algunos ejemplos aquí, y definitivamente puedes consultar el cuaderno completo.

Considera un ejemplo: queremos analizar las ventas de nuestro puesto de helados. Generemos una serie de números de ventas (número de artículos vendidos cada día) durante un período de tiempo:  
```python
start_date = "Jan 1, 2020"
end_date = "Mar 31, 2020"
idx = pd.date_range(start_date,end_date)
print(f"Length of index is {len(idx)}")
items_sold = pd.Series(np.random.randint(25,50,size=len(idx)),index=idx)
items_sold.plot()
```  
![Gráfico de Series Temporales](../../../../2-Working-With-Data/07-python/images/timeseries-1.png)  

Ahora supongamos que cada semana organizamos una fiesta para amigos y tomamos 10 paquetes adicionales de helado para la fiesta. Podemos crear otra serie, indexada por semana, para demostrar eso:  
```python
additional_items = pd.Series(10,index=pd.date_range(start_date,end_date,freq="W"))
```  
Cuando sumamos dos series, obtenemos el número total:  
```python
total_items = items_sold.add(additional_items,fill_value=0)
total_items.plot()
```  
![Gráfico de Series Temporales](../../../../2-Working-With-Data/07-python/images/timeseries-2.png)  

> **Nota** que no estamos utilizando la sintaxis simple `total_items+additional_items`. Si lo hiciéramos, recibiríamos muchos valores `NaN` (*Not a Number*) en la serie resultante. Esto se debe a que hay valores faltantes para algunos puntos del índice en la serie `additional_items`, y sumar `NaN` a cualquier cosa resulta en `NaN`. Por lo tanto, necesitamos especificar el parámetro `fill_value` durante la suma.

Con las series temporales, también podemos **re-muestrear** la serie con diferentes intervalos de tiempo. Por ejemplo, supongamos que queremos calcular el volumen promedio de ventas mensuales. Podemos usar el siguiente código:  
```python
monthly = total_items.resample("1M").mean()
ax = monthly.plot(kind='bar')
```  
![Promedios Mensuales de Series Temporales](../../../../2-Working-With-Data/07-python/images/timeseries-3.png)  

### DataFrame

Un DataFrame es esencialmente una colección de series con el mismo índice. Podemos combinar varias series juntas en un DataFrame:  
```python
a = pd.Series(range(1,10))
b = pd.Series(["I","like","to","play","games","and","will","not","change"],index=range(0,9))
df = pd.DataFrame([a,b])
```  
Esto creará una tabla horizontal como esta:  
|     | 0   | 1    | 2   | 3   | 4      | 5   | 6      | 7    | 8    |
| --- | --- | ---- | --- | --- | ------ | --- | ------ | ---- | ---- |
| 0   | 1   | 2    | 3   | 4   | 5      | 6   | 7      | 8    | 9    |
| 1   | I   | like | to  | use | Python | and | Pandas | very | much |

También podemos usar Series como columnas y especificar nombres de columnas utilizando un diccionario:  
```python
df = pd.DataFrame({ 'A' : a, 'B' : b })
```  
Esto nos dará una tabla como esta:

|     | A   | B      |
| --- | --- | ------ |
| 0   | 1   | I      |
| 1   | 2   | like   |
| 2   | 3   | to     |
| 3   | 4   | use    |
| 4   | 5   | Python |
| 5   | 6   | and    |
| 6   | 7   | Pandas |
| 7   | 8   | very   |
| 8   | 9   | much   |

**Nota** que también podemos obtener este diseño de tabla transponiendo la tabla anterior, por ejemplo, escribiendo  
```python
df = pd.DataFrame([a,b]).T..rename(columns={ 0 : 'A', 1 : 'B' })
```  
Aquí `.T` significa la operación de transponer el DataFrame, es decir, cambiar filas y columnas, y la operación `rename` nos permite renombrar columnas para que coincidan con el ejemplo anterior.

Aquí hay algunas de las operaciones más importantes que podemos realizar en DataFrames:

**Selección de columnas**. Podemos seleccionar columnas individuales escribiendo `df['A']` - esta operación devuelve una Serie. También podemos seleccionar un subconjunto de columnas en otro DataFrame escribiendo `df[['B','A']]` - esto devuelve otro DataFrame.

**Filtrar** solo ciertas filas según criterios. Por ejemplo, para dejar solo las filas con la columna `A` mayor que 5, podemos escribir `df[df['A']>5]`.

> **Nota**: La forma en que funciona el filtrado es la siguiente. La expresión `df['A']<5` devuelve una serie booleana, que indica si la expresión es `True` o `False` para cada elemento de la serie original `df['A']`. Cuando se utiliza una serie booleana como índice, devuelve un subconjunto de filas en el DataFrame. Por lo tanto, no es posible usar expresiones booleanas arbitrarias de Python, por ejemplo, escribir `df[df['A']>5 and df['A']<7]` sería incorrecto. En su lugar, debes usar la operación especial `&` en series booleanas, escribiendo `df[(df['A']>5) & (df['A']<7)]` (*los paréntesis son importantes aquí*).

**Crear nuevas columnas calculables**. Podemos crear fácilmente nuevas columnas calculables para nuestro DataFrame utilizando expresiones intuitivas como esta:  
```python
df['DivA'] = df['A']-df['A'].mean() 
```  
Este ejemplo calcula la divergencia de A respecto a su valor promedio. Lo que realmente sucede aquí es que estamos calculando una serie y luego asignando esta serie al lado izquierdo, creando otra columna. Por lo tanto, no podemos usar operaciones que no sean compatibles con series, por ejemplo, el siguiente código es incorrecto:  
```python
# Wrong code -> df['ADescr'] = "Low" if df['A'] < 5 else "Hi"
df['LenB'] = len(df['B']) # <- Wrong result
```  
El último ejemplo, aunque sintácticamente correcto, nos da un resultado incorrecto porque asigna la longitud de la serie `B` a todos los valores en la columna, y no la longitud de los elementos individuales como pretendíamos.

Si necesitamos calcular expresiones complejas como esta, podemos usar la función `apply`. El último ejemplo se puede escribir de la siguiente manera:  
```python
df['LenB'] = df['B'].apply(lambda x : len(x))
# or 
df['LenB'] = df['B'].apply(len)
```  

Después de las operaciones anteriores, terminaremos con el siguiente DataFrame:

|     | A   | B      | DivA | LenB |
| --- | --- | ------ | ---- | ---- |
| 0   | 1   | I      | -4.0 | 1    |
| 1   | 2   | like   | -3.0 | 4    |
| 2   | 3   | to     | -2.0 | 2    |
| 3   | 4   | use    | -1.0 | 3    |
| 4   | 5   | Python | 0.0  | 6    |
| 5   | 6   | and    | 1.0  | 3    |
| 6   | 7   | Pandas | 2.0  | 6    |
| 7   | 8   | very   | 3.0  | 4    |
| 8   | 9   | much   | 4.0  | 4    |

**Seleccionar filas según números** se puede hacer utilizando la construcción `iloc`. Por ejemplo, para seleccionar las primeras 5 filas del DataFrame:  
```python
df.iloc[:5]
```  

**Agrupación** se utiliza a menudo para obtener un resultado similar a las *tablas dinámicas* en Excel. Supongamos que queremos calcular el valor promedio de la columna `A` para cada número dado de `LenB`. Entonces podemos agrupar nuestro DataFrame por `LenB` y llamar a `mean`:  
```python
df.groupby(by='LenB').mean()
```  
Si necesitamos calcular el promedio y el número de elementos en el grupo, entonces podemos usar la función más compleja `aggregate`:  
```python
df.groupby(by='LenB') \
 .aggregate({ 'DivA' : len, 'A' : lambda x: x.mean() }) \
 .rename(columns={ 'DivA' : 'Count', 'A' : 'Mean'})
```  
Esto nos da la siguiente tabla:

| LenB | Count | Mean     |
| ---- | ----- | -------- |
| 1    | 1     | 1.000000 |
| 2    | 1     | 3.000000 |
| 3    | 2     | 5.000000 |
| 4    | 3     | 6.333333 |
| 6    | 2     | 6.000000 |

### Obtener Datos
Hemos visto lo fácil que es construir Series y DataFrames a partir de objetos de Python. Sin embargo, los datos generalmente vienen en forma de un archivo de texto o una tabla de Excel. Afortunadamente, Pandas nos ofrece una forma sencilla de cargar datos desde el disco. Por ejemplo, leer un archivo CSV es tan simple como esto:  
```python
df = pd.read_csv('file.csv')
```  
Veremos más ejemplos de cómo cargar datos, incluyendo cómo obtenerlos desde sitios web externos, en la sección "Desafío".

### Imprimir y Graficar

Un Científico de Datos a menudo tiene que explorar los datos, por lo que es importante poder visualizarlos. Cuando un DataFrame es grande, muchas veces queremos asegurarnos de que estamos haciendo todo correctamente imprimiendo las primeras filas. Esto se puede hacer llamando a `df.head()`. Si lo ejecutas desde Jupyter Notebook, imprimirá el DataFrame en una forma tabular agradable.

También hemos visto el uso de la función `plot` para visualizar algunas columnas. Aunque `plot` es muy útil para muchas tareas y admite diferentes tipos de gráficos mediante el parámetro `kind=`, siempre puedes usar la biblioteca `matplotlib` directamente para graficar algo más complejo. Cubriremos la visualización de datos en detalle en lecciones separadas del curso.

Este resumen cubre los conceptos más importantes de Pandas; sin embargo, la biblioteca es muy rica y no hay límite para lo que puedes hacer con ella. ¡Ahora apliquemos este conocimiento para resolver un problema específico!

## 🚀 Desafío 1: Analizando la Propagación del COVID

El primer problema en el que nos enfocaremos es el modelado de la propagación epidémica del COVID-19. Para ello, utilizaremos los datos sobre el número de personas infectadas en diferentes países, proporcionados por el [Center for Systems Science and Engineering](https://systems.jhu.edu/) (CSSE) de la [Universidad Johns Hopkins](https://jhu.edu/). El conjunto de datos está disponible en [este repositorio de GitHub](https://github.com/CSSEGISandData/COVID-19).

Como queremos demostrar cómo trabajar con datos, te invitamos a abrir [`notebook-covidspread.ipynb`](../../../../2-Working-With-Data/07-python/notebook-covidspread.ipynb) y leerlo de principio a fin. También puedes ejecutar las celdas y realizar algunos desafíos que hemos dejado para ti al final.

![Propagación del COVID](../../../../2-Working-With-Data/07-python/images/covidspread.png)

> Si no sabes cómo ejecutar código en Jupyter Notebook, consulta [este artículo](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## Trabajando con Datos No Estructurados

Aunque los datos a menudo vienen en forma tabular, en algunos casos necesitamos trabajar con datos menos estructurados, como texto o imágenes. En este caso, para aplicar las técnicas de procesamiento de datos que hemos visto, necesitamos de alguna manera **extraer** datos estructurados. Aquí hay algunos ejemplos:

* Extraer palabras clave de un texto y ver con qué frecuencia aparecen.
* Usar redes neuronales para extraer información sobre objetos en una imagen.
* Obtener información sobre las emociones de las personas en un video.

## 🚀 Desafío 2: Analizando Artículos sobre COVID

En este desafío, continuaremos con el tema de la pandemia de COVID y nos enfocaremos en procesar artículos científicos sobre el tema. Existe el [Conjunto de Datos CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) con más de 7000 artículos (en el momento de escribir esto) sobre COVID, disponible con metadatos y resúmenes (y para aproximadamente la mitad de ellos también se proporciona el texto completo).

Un ejemplo completo de análisis de este conjunto de datos utilizando el servicio cognitivo [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health/?WT.mc_id=academic-77958-bethanycheum) se describe [en este blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Discutiremos una versión simplificada de este análisis.

> **NOTE**: No proporcionamos una copia del conjunto de datos como parte de este repositorio. Es posible que primero necesites descargar el archivo [`metadata.csv`](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) desde [este conjunto de datos en Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge). Es posible que se requiera registrarse en Kaggle. También puedes descargar el conjunto de datos sin registrarte [desde aquí](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html), pero incluirá todos los textos completos además del archivo de metadatos.

Abre [`notebook-papers.ipynb`](../../../../2-Working-With-Data/07-python/notebook-papers.ipynb) y léelo de principio a fin. También puedes ejecutar las celdas y realizar algunos desafíos que hemos dejado para ti al final.

![Tratamiento Médico COVID](../../../../2-Working-With-Data/07-python/images/covidtreat.png)

## Procesamiento de Datos de Imágenes

Recientemente, se han desarrollado modelos de IA muy potentes que nos permiten comprender imágenes. Hay muchas tareas que se pueden resolver utilizando redes neuronales preentrenadas o servicios en la nube. Algunos ejemplos incluyen:

* **Clasificación de Imágenes**, que puede ayudarte a categorizar una imagen en una de las clases predefinidas. Puedes entrenar fácilmente tus propios clasificadores de imágenes utilizando servicios como [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum).
* **Detección de Objetos** para identificar diferentes objetos en una imagen. Servicios como [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) pueden detectar una serie de objetos comunes, y puedes entrenar un modelo de [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum) para detectar objetos específicos de interés.
* **Detección de Rostros**, incluyendo edad, género y emociones. Esto se puede hacer a través de [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum).

Todos estos servicios en la nube se pueden llamar utilizando [Python SDKs](https://docs.microsoft.com/samples/azure-samples/cognitive-services-python-sdk-samples/cognitive-services-python-sdk-samples/?WT.mc_id=academic-77958-bethanycheum), y por lo tanto se pueden incorporar fácilmente en tu flujo de trabajo de exploración de datos.

Aquí hay algunos ejemplos de exploración de datos a partir de fuentes de datos de imágenes:
* En el blog [Cómo Aprender Ciencia de Datos sin Programar](https://soshnikov.com/azure/how-to-learn-data-science-without-coding/) exploramos fotos de Instagram, tratando de entender qué hace que las personas den más "me gusta" a una foto. Primero extraemos tanta información como sea posible de las imágenes utilizando [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum), y luego usamos [Azure Machine Learning AutoML](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml/?WT.mc_id=academic-77958-bethanycheum) para construir un modelo interpretable.
* En el [Taller de Estudios Faciales](https://github.com/CloudAdvocacy/FaceStudies) usamos [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum) para extraer emociones de personas en fotografías de eventos, con el fin de tratar de entender qué hace felices a las personas.

## Conclusión

Ya sea que tengas datos estructurados o no estructurados, con Python puedes realizar todos los pasos relacionados con el procesamiento y la comprensión de datos. Es probablemente la forma más flexible de procesar datos, y esa es la razón por la que la mayoría de los científicos de datos usan Python como su herramienta principal. ¡Aprender Python en profundidad es probablemente una buena idea si estás comprometido con tu camino en la ciencia de datos!

## [Cuestionario posterior a la lección](https://ff-quizzes.netlify.app/en/ds/quiz/13)

## Revisión y Autoestudio

**Libros**  
* [Wes McKinney. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](https://www.amazon.com/gp/product/1491957662)

**Recursos en Línea**  
* Tutorial oficial [10 minutos con Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)  
* [Documentación sobre Visualización en Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)

**Aprendiendo Python**  
* [Aprende Python de Forma Divertida con Turtle Graphics y Fractales](https://github.com/shwars/pycourse)  
* [Da tus Primeros Pasos con Python](https://docs.microsoft.com/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) en la Ruta de Aprendizaje de [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

## Tarea

[Realiza un estudio de datos más detallado para los desafíos anteriores](assignment.md)

## Créditos

Esta lección ha sido creada con ♥️ por [Dmitry Soshnikov](http://soshnikov.com)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.