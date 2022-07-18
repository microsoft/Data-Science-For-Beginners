# Visualización de Cantidades

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Visualización de cantidades - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

En esta lección explorarás cómo utilizar una de las muchas librerías de Python disponibles para aprender a crear interesantes visualizaciones relacionadas al concepto de cantidad. Utilizando un conjunto de datos limpios sobre las aves de Minnesota, podrás aprender muchos datos interesantes sobre la vida silvestre local.
## [Cuestionario previo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Observar la envergadura con Matplotlib

Una excelente librería para crear gráficos tanto simples como sofisticados de varios tipos es [Matplotlib](https://matplotlib.org/stable/index.html). En términos generales, el proceso de ploteamiento de datos utilizando estas librerías incluye la identificación de las partes del dataframe que desea enfocar, la realización de cualquier transformación en los datos necesarios, la asignación de los valores de los ejes x e y, la decisión de qué tipo de gráfico mostrar, y luego mostrar el gráfico. Matplotlib ofrece una gran variedad de visualizaciones, pero para esta lección, vamos a concentrarnos en las más apropiadas para visualizar cantidad: gráficos de líneas, gráficos de dispersión y gráficos de barras.

> ✅ Usa el gráfico que mejor se adapte a la estructura de tus datos y a la historia que quieres contar. 
> - Para analizar tendencias a lo largo del tiempo: línea
> - Para comparar valores: barra, columna, pastel, diagrama de dispersión
> - Para mostrar cómo se relacionan las partes con un todo: pastel
> - Para mostrar la distribución de los datos: gráfico de dispersión, barra
> - Para mostrar tendencias: línea, columna
> - Para mostrar relaciones entre valores: línea, gráfico de dispersión, burbuja

Si tienes un conjunto de datos y necesitas descubrir qué cantidad de un elemento determinado está incluido, una de las primeras tareas que tienes que hacer será inspeccionar sus valores. 

✅ Hay muy buenas "hojas de trucos" disponibles para Matplotlib [aquí](https://matplotlib.org/cheatsheets/cheatsheets.pdf).

## Construir un gráfico de líneas sobre los valores de la envergadura de las aves

Abre el archivo `notebook.ipynb` en la raíz de la carpeta de esta lección y añada una celda.

> Nota: los datos están almacenados en la raíz de este repositorio en la carpeta `/data`.

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```
Estos datos son una mezcla de texto y números:


|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Empecemos por graficar algunos de los datos numéricos utilizando un gráfico de líneas básico. Supongamos que queremos ver la envergadura máxima de estas interesantes aves.

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```
![Envergadura máxima](../images/max-wingspan.png)

¿Qué nota inmediatamente? Parece que hay al menos un valor atípico: ¡esa es una gran envergadura! Una envergadura de 2.300 centímetros equivale a 23 metros: ¿hay pterodáctilos vagando por Minnesota? Vamos a investigar.

Aunque podrías hacer una ordenación rápida en Excel para encontrar esos valores atípicos, que probablemente sean errores tipográficos, continúa el proceso de visualización trabajando desde el gráfico.

Añade etiquetas al eje x para mostrar qué tipo de aves hay en cuestión:

```
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.xticks(rotation=45)
x = birds['Name'] 
y = birds['MaxWingspan']

plt.plot(x, y)

plt.show()
```
![envergadura con etiquetas](../images/max-wingspan-labels.png)

Incluso con la rotación de las etiquetas ajustada a 45 grados, hay demasiado para leer. Vamos a probar una estrategia diferente: etiquetar sólo los valores atípicos y poner las etiquetas dentro del gráfico. Puedes utilizar un gráfico de dispersión para tener más espacio para el etiquetado:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)

for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
    
plt.show()
```

¿Qué está pasando aquí? Has utilizado `tick_params` para ocultar las etiquetas inferiores y luego has creado un bucle sobre tu conjunto de datos de aves. Al trazar el gráfico con pequeños puntos azules redondos utilizando `bo`, has comprobado si hay algún pájaro con una envergadura máxima superior a 500 y has mostrado su etiqueta junto al punto si es así. Desplazaste las etiquetas un poco en el eje Y (`y * (1 - 0.05)`) y utilizaste el nombre del ave como etiqueta.

¿Qué descubrimos?

![valores atípicos](../images/labeled-wingspan.png)
## Filtra tus datos

Tanto el águila calva como el halcón de las praderas, aunque probablemente sean aves muy grandes, parecen estar mal etiquetadas, con un "0" adicional a su envergadura máxima. Es poco probable que te encuentres con un águila calva de 25 metros de envergadura, pero si es así, ¡háznoslo saber! Vamos a crear un nuevo marco de datos sin esos dos valores atípicos:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()
```

Al filtrar los valores atípicos, sus datos son ahora más coherentes y comprensibles.

![gráfico de dispersión de la envergadura](../images/scatterplot-wingspan.png)

Ahora que tenemos un conjunto de datos más limpio, al menos en lo que respecta a la envergadura, vamos a descubrir más cosas sobre estas aves.

Aunque los gráficos de líneas y de dispersión pueden mostrar información sobre los valores de los datos y sus distribuciones, queremos pensar en los valores inherentes a este conjunto de datos. Podrías crear visualizaciones para responder a las siguientes preguntas sobre la cantidad:

> ¿Cuántas categorías de aves hay y cuál es su número?
> ¿Cuántas aves están extinguidas, en peligro de extinción, son raras o comunes?
> ¿Cuántos hay de los distintos géneros y tipos en la terminología de Linneo?
## Explorar los gráficos de barras

Los gráficos de barras son prácticos cuando se necesita mostrar agrupaciones de datos. Exploremos las categorías de aves que existen en este conjunto de datos para ver cuál es la más común por número.

En el archivo del cuaderno, crea un gráfico de barras básico

✅ Nota, puedes filtrar las dos aves atípicas que identificamos en la sección anterior, editar la errata de su envergadura, o déjalas para estos ejercicios que no dependen de los valores de envergadura.

Si desea crear un gráfico de barras, puede seleccionar los datos en los que desea centrarse. Los gráficos de barras se pueden crear a partir de datos sin procesar:

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```
![datos completos en forma de gráfico de barras](../images/full-data-bar.png)

Este gráfico de barras, sin embargo, es ilegible porque hay demasiados datos no agrupados. Necesitas seleccionar sólo los datos que quieres graficar, así que veamos la longitud de las aves según su categoría. 

Filtra tus datos para incluir sólo la categoría del pájaro. 

✅ Observa que usas Pandas para manejar los datos, y luego dejas que Matplotlib haga el gráfico.

Como hay muchas categorías, puedes mostrar este gráfico verticalmente y ajustar su altura para tener en cuenta todos los datos:

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```
![categoría y altura](../images/category-counts.png)

Este gráfico de barras muestra una buena visión del número de aves en cada categoría. En un abrir y cerrar de ojos, se ve que el mayor número de aves de esta región se encuentra en la categoría de patos/gatos/aves acuáticas. Minnesota es el "país de los 10.000 lagos", así que no es de extrañar.

✅ Prueba otros conteos en este conjunto de datos. ¿Le sorprende algo?

## Comparación de datos

Puedes probar diferentes comparaciones de datos agrupados creando nuevos ejes. Intenta una comparación de la longitud máxima de un pájaro, basada en su categoría:

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```
![comparación de datos](../images/category-length.png)

Aquí no hay nada sorprendente: los colibríes tienen la menor longitud máxima en comparación con los pelícanos o los gansos. ¡Es bueno cuando los datos tienen un sentido lógico!

Puede crear visualizaciones más interesantes de los gráficos de barras superponiendo los datos. Superpongamos la longitud mínima y máxima en una categoría de aves determinada:

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```
En este gráfico, puedes ver el rango por categoría de ave de la longitud mínima y la longitud máxima. Se puede decir con seguridad que, dados estos datos, cuanto más grande es el ave, mayor es su rango de longitud. ¡Fascinante!

![valores superpuestos](../images/superimposed.png)

## 🚀 Desafío

Este conjunto de datos sobre aves ofrece una gran cantidad de información sobre diferentes tipos de aves dentro de un ecosistema concreto. Busca en Internet y comprueba si puedes encontrar otros conjuntos de datos orientados a las aves. Practica la construcción de tablas y gráficos en torno a estas aves para descubrir datos que no conocías.

## [Cuestionario posterior a la clase](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Repaso y Autoestudio

Esta primera lección has recibido alguna información sobre cómo utilizar Matplotlib para visualizar cantidades. Investiga sobre otras formas de trabajar con conjuntos de datos para su visualización. [Plotly](https://github.com/plotly/plotly.py) es otra forma que no cubriremos en estas lecciones, así que echa un vistazo a lo que puede ofrecer.
## Asignación

[Líneas, dispersiones y barras](assignment.es.md)
