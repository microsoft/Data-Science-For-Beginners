# Definiendo la Ciencia de Datos

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png)|
|:---:|
|Definiendo la Ciencia de Datos - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

---

[![Video definiendo la Ciencia de Datos](images/video-def-ds.png)](https://youtu.be/pqqsm5reGvs)

## [Examen previo a la lección](https://red-water-0103e7a0f.azurestaticapps.net/quiz/0)

## ¿Qué son los Datos?
En nuestra vida diaria, estamos constantemente rodeados por datos. El texto que estás leyendo ahora son datos,
la lista de números telefónicos de tus amigos en tu móvil son datos, también como la hora actual que se muestra en tu reloj.
Como seres humanos, operamos naturalmente con datos, contando el dinero que tenemos o escribiendo cartas a nuestros amigos.

Sin embargo, los datos se vuelven más críticos con la creación de las computadoras. El rol principal de las computadoras
es realizar cálculos, pero éstas necesitan datos para operar. Por lo cual, necesitamos entender cómo las computadoras 
almacenan y procesan los datos.

Con el surgimiento de internet, el rol de las computadoras como dispositivos para la manipulación de datos incrementó.
Si lo piensas, ahora usamos computadoras mucho más para la comunicación y el procesamiento de datos, en lugar de para hacer cálculos. Cuando escribimos un correo electrónico a un amigo o buscamos alguna información en internet - estamos
creando, almacenando, transmitiendo y manipulando datos.

> ¿Recuerdas la última vez que usaste una computadora para realmente calcular algo?

## ¿Qué es Ciencia de Datos?

En [Wikipedia](https://en.wikipedia.org/wiki/Data_science), se define la **Ciencia de Datos** como *un campo de las ciencias que usa métodos científicos para extraer conocimiento y perspectivas de datos estructurados y no estructurados, y
aplicar el conocimiento y conocimiento práctico de los datos a través de un amplio rango de dominios de aplicación*.

Ésta definición destaca los siguientes aspectos importantes para la ciencia de datos: 

* El objetivo principal para la ciencia de datos es **extraer conocimiento** de los datos, en otras palabras - **entender** los datos, encontrar relaciones ocultas y construir un **modelo**.
* La ciencia de datos usa **métodos científicos**, como la probabilidad y estadística. De hecho, cuando el término **ciencia de datos** fue usado por primera vez, algunas personas argumentaron que la ciencia de datos era solo un nuevo nombre elegante para estadística. En estos días se ha vuelto evidente que es un campo mucho más amplio. 
* El conocimiento obtenido puede ser aplicado para producir **conocimiento práctico**.
* Seremos capace de operar tanto datos **estructurados** y **no estructurados**. Más adelante en el curso discutiremos los diferentes tupos de datos. 
* El **dominio de la aplicación** es un concepto importante, y un científico de datos necesita al menos cierta experiencia en el dominio del problema.

> Otro aspecto importante de la Ciencia de Datos es que esta estudia como los datos son obtenidos, almacenados y operados usando computadoras. Mientras la estadística nos da los fundamentos matemáticos, la ciencia de datos aplica los conceptos matemáticos para realmente extraer conocimiento de los datos.

Una de las formas (atribuidas a [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) de ver a la ciencia de datos es considerarla como un paradigma separado de la ciencia:
* **Empírica**, en la que confíamos mayormente en observaciones y resultados de experimientos
* **Teórica**, donde surgen nuevos conceptos desde el conocimiento científico existente
* **Computacional**, donde descubrimos nuevos principios basados en algunos experimentos computacionales
* **Dirigidos por datos**, basados en el descubrimiento de relaciones y patrones en los datos

## Otros campos relacionados

Ya que los datos son un concepto predominante, la ciencia de datos en sí misma también es un amplio campo, abarcando muchas otras disciplinas relacionadas.

<dl>
<dt>Bases de datos</dt>
<dd>
La cosa más obvia a considerar es **cómo almacenar** los datos, por ejemplo como estructurarlos de tal formar que se procesen más rápido. Existen distintos tipos de bases de datos que almacenan datos estructurados y no estructurados, los
cuales [consideraremos en este curso] (../../2-Working-With-Data/README.md).
</dd>
<dt>Big Data</dt>
<dd>
Usualmente necesitamos almacenar y procesar enormes cantidades de datos con estructuras relativamente simples. Existen
formas especiales y herramientas para almacenar los datos en una forma distribuida on un clúster de computadoras, y procesarlas eficientemente.
</dd>
<dt>Aprendizaje automático</dt>
<dd>
Una de las formas de entender los datos es **construir un modelo** que será capaz de predecir el resultado deseado. Ser capaz de aprender esos modelos de los datos es el área de estudio del **aprendizaje automático**. Querrás dar un vistazo a nuestro currículum de [Aprendizaje automático para principiantes](https://github.com/microsoft/ML-For-Beginners/) para profundizar en ese campo.
</dd>
<dt>Inteligencia aritifcial</dt>
<dd>
Así como el aprendizaje automático, la inteligencia artificial también depende de los datos, e involucra la construcción de modelos altamente complejos que expondrán un comportamiento similar a un ser humano. Además, los métodos de AI usualmente nos permiten convertir datos no estructurados (por ejemplo, lenguaje natural) en datos estructurados extrayendo conocimiento útil.
</dd>
<dt>Visualización</dt>
<dd>
Cantidades descomunales de datos son incomprensibles para un ser humano, pero una vez que creamos visualizaciones útiles - podemos iniciar haciendo más sentido de los datos, y extrayendo algunas conclusiones. Por lo tanto, es importante conocer diversas formas de visualizar la información - lo cual cubriremos en la [Sección 3](../../3-Data-Visualization/README.md) de nuestro curso. Campos relacionados incluyen **infografías**, e **interacción humano-computadora** en general. 
</dd>
</dl>

## Tipos de datos

Como ya se ha mencionado - los datos están en todas partes, ¡sólo necesitamos capturarlos en la forma correcta! Es útil distinguir entre datos **estructurados** y **no estructurados**. Los primeros típicamente son representados en una forma bien estructurada, usualmente como una tabla o conunto de tablas, mientras que los últimos es sólo una colección de archivos. Algunas veces podemos hablar de datos **semi-estructurados**, que tienen cierta estructura la cual podría variar mucho.

| Estructurado | Semi-estructurado | No estructurado |
|------------- |-------------------|-----------------|
| Lista de personas con sus números telefónicos | Páginas de wikipedia con enlaces | Texto de la enciclopedia Británica |
| Temperatura en todas las habitaciones de un edificio a cada minuto por los últimos 20 años | Colección de documentos científicos en formato JSON con autores, fecha de publicación, y resumen | Recurso compartido de archivos con documentos corporativos |
| Datos por edad y género de todas las personas que entrar al edificio | Páginas de internet | Vídeo sin procesar de cámara de vigilancia |

## Dónde obtener datos

Hay múltiples fuentes de datos, y ¡sería imposible listarlas todas! Sin embargo, mencionemos algunos de los lugares típicos en dónde obtener datos:

* **Estructurados**
  - **Internet de las cosas**, incluyendo datos de distintos sensore, como sensores de temperatura o presión, proveen muchos datos útiles. Por ejemplo, si una oficina es equipada con sensores IoT, podemos controlar automáticamente la calefacción e iluminación para minimizar costos.
  - **Encuestas** que realizamos a los usuarios después de pagar un producto o después de visitar un sitio web.
  - **Análisis de comportamiento** podemos, por ejemplo, ayudarnos a entender que tanto profundiza un usuario en un sitio, y cuál es la razón típica por la cual lo deja.
* **No estructurados**
  - Los **Textos** pueden ser una fuente rica en conocimiento práctico, empezando por el **sentimiento principal** generalizado, hasta la extracción de palabras clave e incluso algún significado semántico.
  - **Imágenes** o **Video**. Un video de una cámara de vigilancia puede ser usado para estimar el tráfico en carretera, e informar a las personas acerca de posibles embotellamientos.
  - **Bitácoras** de servidores web pueden ser usadas para entender qué páginas de nuestro sitio son las más visitadas y por cuánto tiempo.
* **Semi-estructurados**
  - Grafos de **redes sociales** pueden ser una gran fuente de datos acerca de la la personalidad del usuario y efectividad potencial de difusión de la información.
  - Cuando tenemos un conjunto de fotografías de una fiesta, podemos intentar extraer datos de la **dinámica de grupos** construyendo un grafo de personas tomándose fotos unas a otras.

Conociendo posibles fuentes de datos diversas, puedes intentar pensar en distintos escenarios donde se pueden aplicar técnicas de ciencia de datos para conocer mejor la situación, y mejroar los procesos de negocio.

## Qué puedes hacer con los datos

En la ciencia de datos, nos enfocamos en los siguientes pasos del viaje de los datos:

<dl>
<dt>1) Adquisición de datos</dt>
<dd>
El primer paso es reunir los datos. Mientras que en muchos casos esto puede ser un proceso simple, como datos obtenidos des una base de datos de una aplicación web. algunas veces necesitamos usar técnicas especiales. Por ejemplo, los datos obtenidos desde sensorres IoT pueden ser inmensos, y es una buena práctica el uso de endpoints búfer como IoT Hub para para reunir todos los datos antes de procesarlos.
</dd>
<dt>2) Almacenamiento de datos</dt>
<dd>
Almacenar los datos puede ser desafiante, especialmente si hablamos de big data. Al decidir cómo almacer datos, hace sentido anticiparse a la forma en la cual serán consultados. Existen varias formas de almacenar los datos:
<ul>
<li>Las bases de datos relacionales almacenan una colección de tabla, y usan un lenguaje especial llamado SQL para consultalos. Típicamente, las tablas estarían conectadas unas a otras mediante un esquema. En muchas ocasiones necesitamos convertir los datos desde la fuente original para que se ajusten al esquema.</li>
<li>Bases de datos <a href="https://en.wikipedia.org/wiki/NoSQL">NoSQL</a>, como <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=acad-31812-dmitryso">CosmosDB</a>, no exigen un esquema de datos, y permiten almacenar datos más complejos, por ejemplo, documentos JSON jerárquicos o grafos. Sin embargo, Las bases de datos NoSQL no tienen capacidades de consulta SQL sofisticadas, y no requieren integridad referencial entre los datos.</li>
<li>El almacenamiento en <a href="https://en.wikipedia.org/wiki/Data_lake">lago de datos</a> se usa para grandes colecciones de datos sin procesamiento. Los lagos de datos suelen ser usados con big data, donde todos los datos no pueden ser reunidos en un único equipo, y tienen que ser almacenados y procesados por un clúster. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> es un formato de datos que se utiliza comúnmente en conjunto con big data.</li> 
</ul>
</dd>
<dt>3) Procesamiento de datos</dt>
<dd>
Esta es la parte más emocionante del viaje de los datos, el cual involucra el procesamiento de los datos desde su forma original hasta la forma en que puede ser usada por visualizaciones/modelo de entrenamiento. Cuando tratamos con datos no estructurados como texto o imágenes, debemos usar algunas técnias de IA para extraer las **características** de los datos, y así convertirlos a su forma estructurada.
</dd>
<dt>4) Visualización / entendimiento humano</dt>
<dd>
Usualmente para entender los datos necesitamos visualizarlos. Teniendo diversas ténicas de visualización en nuestro arsenal podemos encontrar la visualización adecuada para comprenderla. Comúnmente, un científico de datos necesita "jugar con los datos", visualizádolos varias veces y buscando alguna relación. Además, debemos usar técnicas de estadística para probar algunas hipótesis o probar la correlación entre distintas porciones de datos.
</dd>
<dt>5) Entrenando modelos predictivos</dt>
<dd>
Ya que el principal objetivo de la ciencia de datos es ser capaz de tomar decisiones basándonos en los datos, debemos usar técnicas de <a href="http://github.com/microsoft/ml-for-beginners">aprendizaje automático</a> para construir modelos predictivos que serán capces de resolver nuestros problemas.
</dd>
</dl>

Por supuesto, dependiendo de los datos reales algunos pasos serán omitidos (por ejemplo, cuando ya tenemos los datos en la base de datos, o cuando no necesitamos modelo de entrenamiento), o algunos pasos deben ser repetidos varias veces (como el procesamiento de datos).

## Digitalización y transformación digital

En la última década, muchos negocios comenzaron a entender la importancia de los datos al tomar decisiones de negocio. Para aplicar los principios de ciencia de datos para dirigir un negocio primero necesitas reunir algunos datos, por ejemplo, de alguna forma digitalizar los procesos de negocio. Esto es conocido como **digitalización**, y seguido usar técnicas de ciencia de datos para guiar decisiones esto usualmente conlleva a un incremento significativo de la productividad (o incluso negocios pivote), llamado **transformación digital**.

Consideremos el siguiente ejemplo. Supongaos, tenemos un curso de ciencia de datos (como éste), el cual ofrecemos en línea a los estudiante, y queremos usar ciencia de datos para mejorarl. ¿Cómo podemos hacerlo?

Podemos comenzar pensando "¿qué puede ser digitalizado?". La forma más simple sería medir el tiempo que le toma a cada estuddiante completar cada módulo, y el conocimiento obtenido (por ejemplo, realizando exámenes de opción múltiple al final de cada módulo). Promediando el tiempo en concluir de todos los estudiantes, y trabajar en simplificarlos.

> Argumentarás que este enfoque no es idóneo, porque los módulos pueden tener distinta duración. Problablemente es más justo dividir el tiempo por la longitud del módulo (en número de caracteres), y comparar esos valores en su lugar.

Cuando comenzamos analizando los resultados de los exámenes de opción múltiple, intentamos encontrar conceptos específicos que los estudiantes entendieron vagamente,y mejorar el contenido. Para hacerlo, necesitamos diseñar exámenes de tal forma que cada pregunta se relacione a un concepto concreto o porción de conocimiento.

Si queremos hacerlo aún más complejo, podemos trazar el tiempo invertido en cada módulo contra la categoría de edad de los estudiantes. Encontraremos que para algunas categorías de edad les toma ciertamente más tiempo el completar el módulo, o algunos estudiantes abandonan el curso en cierto punto. Esot nos puede ayudar a sugerir recomendaciones de módulos por edad, y así minimizar el descontengo de la gente por falsas expectativas.

## 🚀 Desafío

En este desafío, intentaremos encontrar los conceptos relevante para el campo de la Ciencia de Datos consultando algunos textos. Tomarermos un artículo de Wikipedia de Ciecnia de Datos, descargaremos y procesaremos el texto, y luego construiremos una nube de palabras como esta:

![Nube de palabras para Ciencia de Datos](images/ds_wordcloud.png)

Visita [`notebook.ipynb`](notebook.ipynb) para leer el código.También pueder ejecutarlo y ver como realiza todas las transformaciones de los datos en tiempo real.

> Si no sabes como ejecutar el código en Jupyter Notebook, da un vistazo a [este artículo](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).



## [Cuestionario porterior a la lección](https://red-water-0103e7a0f.azurestaticapps.net/quiz/1)

## Ejercicios

* **Tarea 1**: Modifica el código anterior para encontrar conceptos relacionados para los campos de **Big Data** y **Machine Learning**
* **Tarea 2**: [Piensa en los escenarios para la Ciencia de Datos](assignment.md)

## Créditos

Esta lección ha sido escrita con ♥️ por [Dmitry Soshnikov](http://soshnikov.com)
