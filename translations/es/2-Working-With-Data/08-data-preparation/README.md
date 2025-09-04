<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90a815d332aea41a222f4c6372e7186e",
  "translation_date": "2025-09-04T13:55:05+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "es"
}
-->
# Trabajando con Datos: Preparación de Datos

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Preparación de Datos - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

## [Cuestionario Previo a la Clase](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Dependiendo de su origen, los datos sin procesar pueden contener algunas inconsistencias que generarán desafíos en el análisis y modelado. En otras palabras, estos datos pueden clasificarse como "sucios" y necesitarán ser limpiados. Esta lección se centra en técnicas para limpiar y transformar los datos para manejar los desafíos de datos faltantes, inexactos o incompletos. Los temas cubiertos en esta lección utilizarán Python y la biblioteca Pandas y serán [demostrados en el notebook](notebook.ipynb) dentro de este directorio.

## La importancia de limpiar los datos

- **Facilidad de uso y reutilización**: Cuando los datos están organizados y normalizados correctamente, es más fácil buscarlos, utilizarlos y compartirlos con otros.

- **Consistencia**: La ciencia de datos a menudo requiere trabajar con más de un conjunto de datos, donde conjuntos de datos de diferentes fuentes necesitan ser combinados. Asegurarse de que cada conjunto de datos individual tenga una estandarización común garantizará que los datos sigan siendo útiles cuando se fusionen en un solo conjunto de datos.

- **Precisión del modelo**: Los datos que han sido limpiados mejoran la precisión de los modelos que dependen de ellos.

## Objetivos y estrategias comunes de limpieza

- **Explorar un conjunto de datos**: La exploración de datos, que se cubre en una [lección posterior](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), puede ayudarte a descubrir datos que necesitan ser limpiados. Observar visualmente los valores dentro de un conjunto de datos puede establecer expectativas sobre cómo será el resto, o proporcionar una idea de los problemas que pueden resolverse. La exploración puede involucrar consultas básicas, visualizaciones y muestreo.

- **Formateo**: Dependiendo de la fuente, los datos pueden tener inconsistencias en cómo se presentan. Esto puede causar problemas al buscar y representar el valor, donde se ve dentro del conjunto de datos pero no se representa correctamente en visualizaciones o resultados de consultas. Los problemas comunes de formateo incluyen resolver espacios en blanco, fechas y tipos de datos. Resolver problemas de formateo generalmente depende de las personas que están utilizando los datos. Por ejemplo, los estándares sobre cómo se presentan las fechas y los números pueden diferir según el país.

- **Duplicaciones**: Los datos que tienen más de una ocurrencia pueden producir resultados inexactos y generalmente deben eliminarse. Esto puede ser una ocurrencia común al combinar dos o más conjuntos de datos. Sin embargo, hay casos en los que las duplicaciones en conjuntos de datos combinados contienen piezas que pueden proporcionar información adicional y pueden necesitar ser preservadas.

- **Datos faltantes**: Los datos faltantes pueden causar inexactitudes, así como resultados débiles o sesgados. A veces, estos pueden resolverse mediante una "recarga" de los datos, rellenando los valores faltantes con cálculos y código como Python, o simplemente eliminando el valor y los datos correspondientes. Hay numerosas razones por las cuales los datos pueden faltar, y las acciones que se toman para resolver estos valores faltantes pueden depender de cómo y por qué faltaron en primer lugar.

## Explorando información de DataFrames
> **Objetivo de aprendizaje:** Al final de esta subsección, deberías sentirte cómodo encontrando información general sobre los datos almacenados en DataFrames de pandas.

Una vez que hayas cargado tus datos en pandas, es probable que estén en un DataFrame (consulta la [lección anterior](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) para una descripción detallada). Sin embargo, si el conjunto de datos en tu DataFrame tiene 60,000 filas y 400 columnas, ¿cómo puedes empezar a entender con qué estás trabajando? Afortunadamente, [pandas](https://pandas.pydata.org/) proporciona herramientas convenientes para observar rápidamente información general sobre un DataFrame, además de las primeras y últimas filas.

Para explorar esta funcionalidad, importaremos la biblioteca Python scikit-learn y utilizaremos un conjunto de datos icónico: el **conjunto de datos Iris**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |longitud del sépalo (cm)|ancho del sépalo (cm)|longitud del pétalo (cm)|ancho del pétalo (cm)|
|----------------------------------------|-------------------------|---------------------|-------------------------|---------------------|
|0                                       |5.1                      |3.5                  |1.4                      |0.2                  |
|1                                       |4.9                      |3.0                  |1.4                      |0.2                  |
|2                                       |4.7                      |3.2                  |1.3                      |0.2                  |
|3                                       |4.6                      |3.1                  |1.5                      |0.2                  |
|4                                       |5.0                      |3.6                  |1.4                      |0.2                  |

- **DataFrame.info**: Para comenzar, el método `info()` se utiliza para imprimir un resumen del contenido presente en un `DataFrame`. Veamos este conjunto de datos para ver qué tenemos:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
A partir de esto, sabemos que el conjunto de datos *Iris* tiene 150 entradas en cuatro columnas sin entradas nulas. Todos los datos están almacenados como números de punto flotante de 64 bits.

- **DataFrame.head()**: A continuación, para verificar el contenido real del `DataFrame`, usamos el método `head()`. Veamos las primeras filas de nuestro `iris_df`:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: Por otro lado, para verificar las últimas filas del `DataFrame`, usamos el método `tail()`:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Conclusión:** Incluso solo observando los metadatos sobre la información en un DataFrame o los primeros y últimos valores en uno, puedes obtener una idea inmediata sobre el tamaño, la forma y el contenido de los datos con los que estás trabajando.

## Tratando con Datos Faltantes
> **Objetivo de aprendizaje:** Al final de esta subsección, deberías saber cómo reemplazar o eliminar valores nulos de DataFrames.

La mayoría de las veces, los conjuntos de datos que deseas usar (o tienes que usar) tienen valores faltantes. Cómo se manejan los datos faltantes conlleva sutiles compensaciones que pueden afectar tu análisis final y los resultados en el mundo real.

Pandas maneja los valores faltantes de dos maneras. La primera que has visto antes en secciones anteriores: `NaN`, o Not a Number. Este es un valor especial que forma parte de la especificación de punto flotante IEEE y solo se utiliza para indicar valores faltantes de punto flotante.

Para valores faltantes aparte de los flotantes, pandas utiliza el objeto `None` de Python. Aunque puede parecer confuso que encuentres dos tipos diferentes de valores que esencialmente dicen lo mismo, hay razones programáticas sólidas para esta elección de diseño y, en la práctica, ir por esta ruta permite que pandas ofrezca un buen compromiso para la gran mayoría de los casos. No obstante, tanto `None` como `NaN` tienen restricciones que debes tener en cuenta con respecto a cómo pueden ser utilizados.

Consulta más sobre `NaN` y `None` en el [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Detectando valores nulos**: En `pandas`, los métodos `isnull()` y `notnull()` son tus métodos principales para detectar datos nulos. Ambos devuelven máscaras booleanas sobre tus datos. Usaremos `numpy` para valores `NaN`:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Observa detenidamente la salida. ¿Algo te sorprende? Aunque `0` es un nulo aritmético, sigue siendo un entero perfectamente válido y pandas lo trata como tal. `''` es un poco más sutil. Aunque lo usamos en la Sección 1 para representar un valor de cadena vacío, sigue siendo un objeto de cadena y no una representación de nulo según pandas.

Ahora, demos la vuelta a esto y usemos estos métodos de una manera más parecida a cómo los usarás en la práctica. Puedes usar máscaras booleanas directamente como un índice de ``Series`` o ``DataFrame``, lo cual puede ser útil al intentar trabajar con valores faltantes (o presentes) aislados.

> **Conclusión**: Tanto los métodos `isnull()` como `notnull()` producen resultados similares cuando los usas en `DataFrame`s: muestran los resultados y el índice de esos resultados, lo cual te ayudará enormemente mientras trabajas con tus datos.

- **Eliminando valores nulos**: Más allá de identificar valores faltantes, pandas proporciona un medio conveniente para eliminar valores nulos de `Series` y `DataFrame`s. (Particularmente en conjuntos de datos grandes, a menudo es más aconsejable simplemente eliminar los valores faltantes [NA] de tu análisis que manejarlos de otras maneras). Para ver esto en acción, volvamos a `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Nota que esto debería parecerse a tu salida de `example3[example3.notnull()]`. La diferencia aquí es que, en lugar de simplemente indexar los valores enmascarados, `dropna` ha eliminado esos valores faltantes de la `Series` `example1`.

Dado que los `DataFrame`s tienen dos dimensiones, ofrecen más opciones para eliminar datos.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(¿Notaste que pandas convirtió dos de las columnas a flotantes para acomodar los `NaN`s?)

No puedes eliminar un solo valor de un `DataFrame`, por lo que tienes que eliminar filas o columnas completas. Dependiendo de lo que estés haciendo, podrías querer hacer una u otra, y pandas te da opciones para ambas. Dado que en la ciencia de datos las columnas generalmente representan variables y las filas representan observaciones, es más probable que elimines filas de datos; la configuración predeterminada para `dropna()` es eliminar todas las filas que contienen cualquier valor nulo:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Si es necesario, puedes eliminar valores NA de columnas. Usa `axis=1` para hacerlo:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Nota que esto puede eliminar muchos datos que podrías querer conservar, particularmente en conjuntos de datos más pequeños. ¿Qué pasa si solo quieres eliminar filas o columnas que contienen varios o incluso todos los valores nulos? Especificas esas configuraciones en `dropna` con los parámetros `how` y `thresh`.

Por defecto, `how='any'` (si deseas verificarlo por ti mismo o ver qué otros parámetros tiene el método, ejecuta `example4.dropna?` en una celda de código). Podrías especificar alternativamente `how='all'` para eliminar solo filas o columnas que contengan todos los valores nulos. Ampliemos nuestro ejemplo de `DataFrame` para ver esto en acción.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

El parámetro `thresh` te da un control más detallado: estableces el número de valores *no nulos* que una fila o columna necesita tener para ser conservada:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Aquí, la primera y última fila han sido eliminadas, porque contienen solo dos valores no nulos.

- **Rellenando valores nulos**: Dependiendo de tu conjunto de datos, a veces puede tener más sentido rellenar valores nulos con valores válidos en lugar de eliminarlos. Podrías usar `isnull` para hacer esto en el lugar, pero eso puede ser laborioso, particularmente si tienes muchos valores que rellenar. Dado que esta es una tarea tan común en la ciencia de datos, pandas proporciona `fillna`, que devuelve una copia de la `Series` o `DataFrame` con los valores faltantes reemplazados por uno de tu elección. Creemos otra `Series` de ejemplo para ver cómo funciona esto en la práctica.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Puedes rellenar todas las entradas nulas con un solo valor, como `0`:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Puedes **rellenar hacia adelante** los valores nulos, es decir, usar el último valor válido para rellenar un nulo:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
También puedes **rellenar hacia atrás** para propagar el siguiente valor válido hacia atrás para rellenar un nulo:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Como podrías imaginar, esto funciona igual con `DataFrame`s, pero también puedes especificar un `axis` a lo largo del cual rellenar valores nulos. Tomando nuevamente el `example2` previamente utilizado:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Nota que cuando no hay un valor previo disponible para rellenar hacia adelante, el valor nulo permanece.
> **Conclusión:** Hay múltiples formas de manejar valores faltantes en tus conjuntos de datos. La estrategia específica que utilices (eliminarlos, reemplazarlos, o incluso cómo los reemplazas) debe estar dictada por las particularidades de esos datos. Desarrollarás un mejor sentido de cómo tratar los valores faltantes cuanto más interactúes y trabajes con conjuntos de datos.

## Eliminando datos duplicados

> **Objetivo de aprendizaje:** Al final de esta subsección, deberías sentirte cómodo identificando y eliminando valores duplicados de los DataFrames.

Además de los datos faltantes, a menudo encontrarás datos duplicados en conjuntos de datos del mundo real. Afortunadamente, `pandas` proporciona una forma sencilla de detectar y eliminar entradas duplicadas.

- **Identificando duplicados: `duplicated`**: Puedes identificar fácilmente valores duplicados utilizando el método `duplicated` en pandas, que devuelve una máscara booleana indicando si una entrada en un `DataFrame` es un duplicado de una anterior. Vamos a crear otro ejemplo de `DataFrame` para ver esto en acción.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Eliminando duplicados: `drop_duplicates`:** simplemente devuelve una copia de los datos en los que todos los valores `duplicated` son `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Tanto `duplicated` como `drop_duplicates` por defecto consideran todas las columnas, pero puedes especificar que examinen solo un subconjunto de columnas en tu `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Conclusión:** Eliminar datos duplicados es una parte esencial de casi todos los proyectos de ciencia de datos. Los datos duplicados pueden alterar los resultados de tus análisis y proporcionarte resultados inexactos.


## 🚀 Desafío

Todo el material discutido está disponible como un [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Además, hay ejercicios presentes después de cada sección, ¡inténtalos!

## [Cuestionario posterior a la clase](https://ff-quizzes.netlify.app/en/ds/)



## Revisión y autoestudio

Existen muchas formas de descubrir y abordar la preparación de tus datos para análisis y modelado, y limpiar los datos es un paso importante que requiere experiencia práctica. Prueba estos desafíos de Kaggle para explorar técnicas que esta lección no cubrió.

- [Desafío de Limpieza de Datos: Parseo de Fechas](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Desafío de Limpieza de Datos: Escalar y Normalizar Datos](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Tarea

[Evaluando Datos de un Formulario](assignment.md)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.