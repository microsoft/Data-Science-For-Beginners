# Definiendo Datos

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definiendo Datos - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Los datos son hechos, información, observaciones y mediciones que se usan para hacer descubrimientos y apoyar decisiones informadas. Un punto de datos es una unidad única de datos dentro de un conjunto de datos, que es una colección de puntos de datos. Los conjuntos de datos pueden venir en diferentes formatos y estructuras, y usualmente estarán basados en su fuente, o de dónde provienen los datos. Por ejemplo, las ganancias mensuales de una empresa podrían estar en una hoja de cálculo, pero los datos de frecuencia cardíaca por hora de un reloj inteligente pueden estar en formato [JSON](https://stackoverflow.com/a/383699). Es común que los científicos de datos trabajen con diferentes tipos de datos dentro de un conjunto de datos.

Esta lección se enfoca en identificar y clasificar datos por sus características y sus fuentes.

## [Cuestionario Pre-Clase](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Cómo se Describe un Dato

### Datos Crudos
Los datos crudos son datos que han llegado de su fuente en su estado inicial y no han sido analizados u organizados. Para entender qué está pasando con un conjunto de datos, debe organizarse en un formato que pueda ser entendido por humanos así como por la tecnología que pueda usarse para analizarlo más a fondo. La estructura de un conjunto de datos describe cómo está organizado y puede clasificarse en estructurado, no estructurado y semi-estructurado. Estos tipos de estructura variarán dependiendo de la fuente, pero en última instancia encajarán en estas tres categorías.

### Datos Cuantitativos
Los datos cuantitativos son observaciones numéricas dentro de un conjunto de datos y típicamente pueden ser analizados, medidos y usados matemáticamente. Algunos ejemplos de datos cuantitativos son: la población de un país, la altura de una persona o las ganancias trimestrales de una empresa. Con un análisis adicional, los datos cuantitativos podrían usarse para descubrir tendencias estacionales del Índice de Calidad del Aire (AQI) o estimar la probabilidad del tráfico en hora pico en un día típico laboral.

### Datos Cualitativos
Los datos cualitativos, también conocidos como datos categóricos, son datos que no pueden ser medidos objetivamente como las observaciones cuantitativas. Generalmente son varios formatos de datos subjetivos que capturan la calidad de algo, como un producto o un proceso. A veces, los datos cualitativos son numéricos y no se usan típicamente de forma matemática, como números de teléfono o marcas de tiempo. Algunos ejemplos de datos cualitativos son: comentarios en video, la marca y modelo de un auto o el color favorito de tus amigos más cercanos. Los datos cualitativos podrían usarse para entender qué productos prefieren los consumidores o identificar palabras clave populares en currículums de solicitudes de empleo.

### Datos Estructurados
Los datos estructurados son datos que están organizados en filas y columnas, donde cada fila tendrá el mismo conjunto de columnas. Las columnas representan un valor de un tipo particular y serán identificadas con un nombre que describe lo que representa el valor, mientras que las filas contienen los valores reales. Las columnas a menudo tendrán un conjunto específico de reglas o restricciones sobre los valores, para asegurar que los valores representen con precisión la columna. Por ejemplo, imagina una hoja de cálculo de clientes donde cada fila debe tener un número telefónico y los números telefónicos nunca contienen caracteres alfabéticos. Puede haber reglas aplicadas en la columna de números telefónicos para asegurarse que nunca esté vacía y que contenga solo números.

Un beneficio de los datos estructurados es que pueden organizarse de tal manera que puedan relacionarse con otros datos estructurados. Sin embargo, debido a que los datos están diseñados para organizarse de una manera específica, hacer cambios en su estructura general puede requerir mucho esfuerzo. Por ejemplo, agregar una columna de correo electrónico a la hoja de clientes que no puede estar vacía significa que deberás descubrir cómo añadir esos valores a las filas existentes de clientes en el conjunto de datos.

Ejemplos de datos estructurados: hojas de cálculo, bases de datos relacionales, números telefónicos, estados de cuenta bancarios

### Datos No Estructurados
Los datos no estructurados típicamente no pueden categorizarse en filas o columnas y no contienen un formato o conjunto de reglas a seguir. Debido a que los datos no estructurados tienen menos restricciones en su estructura, es más fácil añadir nueva información en comparación con un conjunto de datos estructurado. Si un sensor que captura datos de presión barométrica cada 2 minutos recibe una actualización que ahora le permite medir y registrar la temperatura, no requiere alterar los datos existentes si estos son no estructurados. Sin embargo, esto puede hacer que analizar o investigar este tipo de datos tome más tiempo. Por ejemplo, un científico que quiere encontrar la temperatura promedio del mes anterior a partir de los datos del sensor, pero descubre que el sensor registró una "e" en algunos de sus datos para indicar que estaba roto en lugar de un número típico, lo que significa que los datos están incompletos.

Ejemplos de datos no estructurados: archivos de texto, mensajes de texto, archivos de video

### Semi-estructurado
Los datos semi-estructurados tienen características que los hacen una combinación de datos estructurados y no estructurados. Típicamente no se conforman a un formato de filas y columnas, pero están organizados de una manera que se considera estructurada y pueden seguir un formato fijo o conjunto de reglas. La estructura varía entre fuentes, desde una jerarquía bien definida a algo más flexible que permite una fácil integración de nueva información. Los metadatos son indicadores que ayudan a decidir cómo se organizan y almacenan los datos y tendrán varios nombres, basados en el tipo de dato. Algunos nombres comunes para los metadatos son etiquetas, elementos, entidades y atributos. Por ejemplo, un mensaje de correo electrónico típico tendrá un asunto, cuerpo y un conjunto de destinatarios, y puede organizarse por quién o cuándo fue enviado.

Ejemplos de datos semi-estructurados: HTML, archivos CSV, JavaScript Object Notation (JSON)

## Fuentes de Datos

Una fuente de datos es la ubicación inicial de donde se generaron los datos, o dónde "viven" y variará dependiendo de cómo y cuándo fueron recolectados. Los datos generados por sus usuarios se conocen como datos primarios, mientras que los datos secundarios provienen de una fuente que ha recolectado datos para uso general. Por ejemplo, un grupo de científicos recolectando observaciones en una selva tropical sería considerado primario, y si deciden compartirlo con otros científicos, sería considerado secundario para aquellos que lo usan.

Las bases de datos son una fuente común y dependen de un sistema de gestión de base de datos para alojar y mantener los datos donde los usuarios usan comandos llamados consultas para explorar los datos. Los archivos como fuentes de datos pueden ser archivos de audio, imagen y video, así como hojas de cálculo como Excel. Las fuentes de internet son una ubicación común para alojar datos, donde se pueden encontrar bases de datos así como archivos. Las interfaces de programación de aplicaciones, también conocidas como APIs, permiten a los programadores crear formas de compartir datos con usuarios externos a través de internet, mientras que el proceso de web scraping extrae datos de una página web. Las [lecciones en Trabajando con Datos](../../../../../../../../../2-Working-With-Data) se enfocan en cómo usar varias fuentes de datos.

## Conclusión

En esta lección hemos aprendido:

- Qué son los datos
- Cómo se describen los datos
- Cómo se clasifican y categorizan los datos
- Dónde se pueden encontrar los datos

## 🚀 Desafío

Kaggle es una excelente fuente de conjuntos de datos abiertos. Usa la [herramienta de búsqueda de conjuntos de datos](https://www.kaggle.com/datasets) para encontrar algunos conjuntos de datos interesantes y clasifica de 3 a 5 conjuntos con este criterio:

- ¿Son los datos cuantitativos o cualitativos?
- ¿Son los datos estructurados, no estructurados o semi-estructurados?

## [Cuestionario Post-clase](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Repaso y Autoestudio

- Esta unidad de Microsoft Learn, titulada [Identificar formatos de datos](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) tiene un desglose detallado de datos estructurados, semi-estructurados y no estructurados.

## Tarea

[Clasificando Conjuntos de Datos](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->