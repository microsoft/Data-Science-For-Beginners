# Definiendo la ciencia de datos

| ![ Boceto por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Definiendo la ciencia de datos - Boceto por [@nitya](https://twitter.com/nitya)_               |

---

[![Video definiendo la ciencia de datos](../images/video-def-ds.png)](https://youtu.be/beZ7Mb_oz9I)

## [Cuestionario antes de la lección](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/0)

## ¿Qué son los datos?
En nuestra vida cotidiana estamos rodeados de datos. El texto que estás leyendo ahora mismo son datos.  La lista de tus contactos en tu teléfono móvil son datos, como lo es la hora que muestra tu reloj. Como seres humanos, operamos naturalmente condatos como por ejemplo contando el dinero que tenemos o escribiendo cartas a nuestros amigos.

Sin embargo, los datos se volvieron mucho más importantes con la creación de los ordenadores.  La función principal de los ordenadores es realizar cálculos, pero necesitan datos para operar. Por ello, debemos entender cómo los ordenadores almacenan y procesan estos datos.

Con la aparición de Internet, aumentó el papel de los ordenadores como dispositivos de tratamiento de datos.  Si lo pensamos bien, ahora utilizamos los ordenadores cada vez más para el procesamiento de datos y la comunicación, incluso más que para los cálculos propiamente dichos. Cuando escribimos un correo electrónico a un amigo o buscamos información en Internet, estamos creando, almacenando, transmitiendo y manipulando datos.

> Te acuerdas de la última vez que utilizaste un ordenador sólo para hacer un cálculo? 

## ¿Qué es la ciencia de datos?

En [Wikipedia](https://en.wikipedia.org/wiki/Data_science), **la ciencia de datos** se define como *un campo científico que utiliza métodos científicos para extraer conocimientos y percepciones de datos estructurados y no estructurados, y aplicar conocimientos procesables de los datos en una amplia gama de dominios de aplicación*. 

Esta definición destaca los siguientes aspectos importantes de la ciencia de datos:

* El objetivo principal de la ciencia de datos es **extraer conocimiento** de los datos, es decir, **comprender** los datos, encontrar algunas relaciones ocultas entre ellos y construir un **modelo**.

* La ciencia de los datos utiliza **métodos científicos**, como la probabilidad y la estadística.  De hecho, cuando se introdujo por primera vez el término *ciencia de los datos*, hubo quiens argumentó que la ciencia de los datos no era más que un nuevo nombre elegante para la estadística. Hoy en día es evidente que el campo es mucho más amplio.

* Los conocimientos obtenidos deben aplicarse para producir algunas **perspectivas aplicables**, es decir, percepciones prácticas que puedan ser aplicadas a situaciones empresariales reales.

* Deberíamos ser capaces de operar tanto con datos **estructurados** como con datos **no estructurados**.  Volveremos a hablar de los diferentes tipos de datos más adelante en el curso.

* **El dominio de aplicación** es un concepto importante, y los científicos de datos suelen necesitar al menos cierto grado de experiencia en el dominio del problema, por ejemplo: finanzas, medicina, marketing, etc.

> Otro aspecto importante de la ciencia de los datos es que estudia cómo se pueden recopilar, almacenar y utilizar los datos mediante ordenadores.  Mientras que la estadística nos proporciona fundamentos matemáticos, la ciencia de los datos aplica conceptos matemáticos para extraer realmente información de los datos.

Una de las formas (atribuida a [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) de ver la ciencia de los datos es considerarla como un paradigma nuevo de la ciencia:
* **Empírico**, en el que nos basamos principalmente en las observaciones y los resultados de los experimentos
* **Teórico**, donde los nuevos conceptos surgen de los conocimientos científicos existentes
* **Computacional**, donde descubrimos nuevos principios basados en algunos experimentos computacionales
* **Controlado por los datos**, basado en el descubrimiento de relaciones y patrones en los datos  

## Otros campos relacionados

Dado que los datos son omnipresentes, la propia ciencia de los datos es también un campo muy amplio, que toca muchas otras disciplinas.

<dl>
<dt>Bases de datos</dt>
<dd>
Una consideración crítica es **cómo almacenar** los datos, es decir, cómo estructurarlos de forma que permitan un procesamiento más rápido.  Hay diferentes tipos de bases de datos que almacenan datos estructurados y no estructurados, que <a href="../../../2-Working-With-Data/README.md">consideraremos en nuestro curso</a>.
</dd>
<dt>Big Data</dt>
<dd>
A menudo necesitamos almacenar y procesar cantidades muy grandes de datos con una estructura relativamente sencilla.  Existen enfoques y herramientas especiales para almacenar esos datos de forma distribuida en un núcleo de ordenadores, y procesarlos de forma eficiente.
</dd>
<dt>Machine Learning o Aprendizaje automático</dt>
<dd>
Una forma de entender los datos es **construir un modelo** que sea capaz de predecir un resultado deseado.  El desarrollo de modelos a partir de los datos se denomina **aprendizaje automático**. Quizá quieras echar un vistazo a nuestro curso <a href="https://aka.ms/ml-beginners">Machine Learning for Beginners</a> para aprender más sobre el tema.
</dd>
<dt>Inteligencia artificial</dt>
<dd>
Un área del Machine learning llamada inteligencia artificial (IA o AI, por sus siglas en inglés) también está basada en datos, e involucra construir modelos muy complejos que imitan los procesos de pensamiento humanos.  Métodos de inteligencia artificial a menudo permiten transformar datos no estructurados (como el lenguaje natural) en descubrimientos estructurados sobre ellos. 
</dd>
<dt>Visualización</dt>
<dd>
Cantidades muy grandes de datos son incomprensibles para un ser humano, pero una vez que creamos visualizaciones útiles con esos datos, podemos darles más sentido y sacar algunas conclusiones. Por ello, es importante conocer muchas formas de visualizar la información, algo que trataremos en <a href="../../../3-Data-Visualization/README.md">la sección 3</a> de nuestro curso. Campos relacionados también incluyen la **Infografía**, y la **Interacción Persona-Ordenador** en general. 
</dd>
</dl>

## Tipos de datos

Como ya hemos dicho, los datos están en todas partes. Sólo hay que obtenerlos de la forma adecuada. Es útil distinguir entre **datos estructurados** y **datos no estructurados**. Los primeros suelen estar representados de alguna forma bien estructurada, a menudo como una tabla o un número de tablas, mientras que los segundos son simplemente una colección de archivos. A veces también podemos hablar de **datos semiestructurados**, que tienen algún tipo de estructura que puede variar mucho.


| Structured                                                                   | Semi-structured                                                                                | Unstructured                            |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| List of people with their phone numbers                                      | Wikipedia pages with links                                                                     | Text of Encyclopaedia Britannica        |
| Temperature in all rooms of a building at every minute for the last 20 years | Collection of scientific papers in JSON format with authors, data of publication, and abstract | File share with corporate documents     |
| Data for age and gender of all people entering the building                  | Internet pages                                                                                 | Raw video feed from surveillance camera |

## Dónde conseguir datos

Hay muchas fuentes de datos posibles, y será imposible enumerarlas todas. Sin embargo, vamos a mencionar algunos de los lugares típicos donde se pueden obtener datos:

* **Estructurados**
  - **Internet de las cosas** (IoT), que incluye datos de diferentes sensores, como los de temperatura o presión, proporciona muchos datos útiles.  Por ejemplo, si un edificio de oficinas está equipado con sensores IoT, podemos controlar automáticamente la calefacción y la iluminación para minimizar los costes. 
  - **Encuestas** que pedimos a los usuarios que completen después de una compra, o después de visitar un sitio web.
  - **El análisis del comportamiento** puede, por ejemplo, ayudarnos a entender hasta qué punto se adentra un usuario en un sitio, y cuál es el motivo típico por el que lo abandonan.
* **No estructurado**
  - Los textos pueden ser una rica fuente de información, como la puntuación general del sentimiento, o la extracción de palabras clave y el significado semántico.
  - Imágenes o vídeos. Un vídeo de una cámara de vigilancia puede utilizarse para estimar el tráfico en la carretera e informar a la gente sobre posibles atascos.
  - Los **registros** del servidor web pueden utilizarse para entender qué páginas de nuestro sitio son las más visitadas, y durante cuánto tiempo.
* **Semiestructurados**
  - Los gráficos de las redes sociales pueden ser una gran fuente de datos sobre la personalidad de los usuarios y su eficacia para difundir información.
  - Cuando tenemos un montón de fotografías de una fiesta, podemos intentar extraer datos de **dinámica de grupos** construyendo un gráfico de las personas que se hacen fotos entre sí.

Al conocer las distintas fuentes posibles de datos, se puede intentar pensar en diferentes escenarios en los que se pueden aplicar técnicas de ciencia de datos para conocer mejor la situación y mejorar los procesos empresariales. 

## Qué puedes hacer con los datos

En Data Science, nos centramos en los siguientes pasos del camino de los datos:

<dl>
<dt>1) Adquisición de datos</dt>
<dd>
El primer paso es recoger los datos.  Aunque en muchos casos puede ser un proceso sencillo, como los datos que llegan a una base de datos desde una aplicación web, a veces necesitamos utilizar técnicas especiales. Por ejemplo, los datos de los sensores de IoT pueden ser abrumadores, y es una buena práctica utilizar puntos finales de almacenamiento en búfer, como IoT Hub, para recoger todos los datos antes de su posterior procesamiento.
</dd>
<dt>2) Almacenamiento de los datos</dt>
<dd>
El almacenamiento de datos puede ser un reto, especialmente si hablamos de big data. A la hora de decidir cómo almacenar los datos, tiene sentido anticiparse a la forma en que se consultarán los datos en el futuro.  Hay varias formas de almacenar los datos:
<ul>
<li>Una base de datos relacional almacena una colección de tablas y utiliza un lenguaje especial llamado SQL para consultarlas.  Normalmente, las tablas se organizan en diferentes grupos llamados esquemas.  En muchos casos hay que convertir los datos de la forma original para que se ajusten al esquema.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">una base de datos no SQL</a>, como <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, no impone esquemas a los datos y permite almacenar datos más complejos, por ejemplo, documentos JSON jerárquicos o gráficos. Sin embargo, las bases de datos NoSQL no tienen las ricas capacidades de consulta de SQL, y no pueden asegurar la integridad referencial, i.e. reglas sobre cómo se estructuran los datos en las tablas y que rigen las relaciones entre ellas.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Los lagos de datos</a> se utilizan para grandes colecciones de datos en bruto y sin estructurar. Los lagos de datos se utilizan a menudo con big data, donde los datos no caben en una sola máquina, y tienen que ser almacenados y procesados por un clúster de servidores. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> es el formato de datos que se suele utilizar junto con big data.</li> 
</ul>
</dd>
<dt>3) Procesamiento de los datos</dt>
<dd>
Esta es la parte más emocionante del viaje de los datos, que consiste en convertir los datos de su forma original a una forma que pueda utilizarse para la visualización/entrenamiento de modelos.  Cuando se trata de datos no estructurados, como texto o imágenes, es posible que tengamos que utilizar algunas técnicas de IA para extraer **características** de los datos, convirtiéndolos así en formato estructurado.
</dd>
<dt>4) Visualización / Descubrimientos humanos</dt>
<dd>
A menudo, para entender los datos, necesitamos visualizarlos.  Al contar con muchas técnicas de visualización diferentes en nuestra caja de herramientas, podemos encontrar la vista adecuada para hacer una percepción.  A menudo, un científico de datos necesita "jugar con los datos", visualizándolos muchas veces y buscando algunas relaciones.  También podemos utilizar técnicas estadísticas para probar una hipótesis o demostrar una correlación entre diferentes datos.
</dd>
<dt>5) Entrenar un modelo predictivo</dt>
<dd>
Dado que el objetivo final de la ciencia de datos es poder tomar decisiones basadas en los datos, es posible que queramos utilizar las técnicas de <a href="http://github.com/microsoft/ml-for-beginners">Machine Learning</a> para construir un modelo predictivo. A continuación, podemos utilizarlo para hacer predicciones utilizando nuevos conjuntos de datos con estructuras similares.
</dd>
</dl>

Por supuesto, dependiendo de los datos reales, algunos pasos podrían faltar (por ejemplo, cuando ya tenemos los datos en la base de datos, o cuando no necesitamos el entrenamiento del modelo), o algunos pasos podrían repetirse varias veces (como el procesamiento de datos).

## Digitalización y transformación digital

En la última década, muchas empresas han empezado a comprender la importancia de los datos a la hora de tomar decisiones empresariales.  Para aplicar los principios de la ciencia de los datos a la gestión de una empresa, primero hay que recopilar algunos datos, es decir, traducir los procesos empresariales a formato digital. Esto se conoce como **digitalización**.  La aplicación de técnicas de ciencia de datos a estos datos para orientar las decisiones puede conducir a un aumento significativo de la productividad (o incluso al pivote del negocio), lo que se denomina **transformación digital**.

Veamos un ejemplo.  Supongamos que tenemos un curso de ciencia de datos (como éste) que impartimos en línea a los estudiantes, y queremos utilizar la ciencia de datos para mejorarlo.  ¿Cómo podemos hacerlo?

Podemos empezar preguntándonos "¿Qué se puede digitalizar?".  La forma más sencilla sería medir el tiempo que tarda cada alumno en completar cada módulo, y medir los conocimientos obtenidos haciendo un examen de opción múltiple al final de cada módulo.  Haciendo una media del tiempo que tardan en completarlo todos los alumnos, podemos averiguar qué módulos causan más dificultades a los estudiantes, y trabajar en su simplificación.

> Se puede argumentar que este enfoque no es ideal, ya que los módulos pueden tener diferentes longitudes.  Probablemente sea más justo dividir el tiempo por la longitud del módulo (en número de caracteres), y comparar esos valores en su lugar.

Cuando empezamos a analizar los resultados de los exámenes de opción múltiple, podemos intentar determinar qué conceptos les cuesta entender a los alumnos y utilizar esa información para mejorar el contenido.  Para ello, tenemos que diseñar los exámenes de forma que cada pregunta se corresponda con un determinado concepto o trozo de conocimiento.

Si queremos complicarnos aún más, podemos representar el tiempo que se tarda en cada módulo en función de la categoría de edad de los alumnos.  Podríamos descubrir que para algunas categorías de edad se tarda un tiempo inadecuado en completar el módulo, o que los estudiantes abandonan antes de completarlo.  Esto puede ayudarnos a proporcionar recomendaciones de edad para el módulo, y minimizar la insatisfacción de la gente por expectativas erróneas.

## 🚀 Challenge

En este reto, trataremos de encontrar conceptos relevantes para el campo de la Ciencia de los Datos a través de textos.  Tomaremos un artículo de Wikipedia sobre la Ciencia de los Datos, descargaremos y procesaremos el texto, y luego construiremos una nube de palabras como esta:

![Word Cloud para ciencia de datos](images/ds_wordcloud.png)

Visite [`notebook.ipynb`](notebook.ipynb) para leer el código.  También puedes ejecutar el código y ver cómo realiza todas las transformaciones de datos en tiempo real. 

> Si no sabe cómo ejecutar código en un "jupyter notebook", eche un vistazo a [este artículo](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).



## [Cuestionario después de la lección](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/1)

## Tareas

* **Tarea 1**: Modifica el código anterior para encontrar conceptos relacionados para los campos de **Big Data** y **Machine Learning**.
* **Tarea 2**: [Piensa sobre escenarios de la ciencia de datos](assignment.md)

## Créditos

Esta lección ha sido escrita con ♥️ por [Dmitry Soshnikov](http://soshnikov.com)
