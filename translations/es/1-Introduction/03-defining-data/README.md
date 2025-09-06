<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T13:45:32+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "es"
}
-->
# Definiendo Datos

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definiendo Datos - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Los datos son hechos, información, observaciones y mediciones que se utilizan para hacer descubrimientos y tomar decisiones informadas. Un punto de datos es una unidad única de datos dentro de un conjunto de datos, que es una colección de puntos de datos. Los conjuntos de datos pueden venir en diferentes formatos y estructuras, y generalmente estarán basados en su fuente, o de dónde provienen los datos. Por ejemplo, las ganancias mensuales de una empresa podrían estar en una hoja de cálculo, pero los datos de frecuencia cardíaca por hora de un reloj inteligente podrían estar en formato [JSON](https://stackoverflow.com/a/383699). Es común que los científicos de datos trabajen con diferentes tipos de datos dentro de un conjunto de datos.

Esta lección se centra en identificar y clasificar los datos según sus características y sus fuentes.

## [Cuestionario Previo a la Clase](https://ff-quizzes.netlify.app/en/ds/quiz/4)

## Cómo se Describen los Datos

### Datos Crudos
Los datos crudos son datos que provienen de su fuente en su estado inicial y no han sido analizados ni organizados. Para entender lo que está sucediendo con un conjunto de datos, es necesario organizarlos en un formato que pueda ser comprendido tanto por humanos como por la tecnología que puedan usar para analizarlos más a fondo. La estructura de un conjunto de datos describe cómo está organizado y puede clasificarse como estructurada, no estructurada y semiestructurada. Estos tipos de estructura variarán dependiendo de la fuente, pero en última instancia encajarán en estas tres categorías.

### Datos Cuantitativos
Los datos cuantitativos son observaciones numéricas dentro de un conjunto de datos y, por lo general, pueden analizarse, medirse y usarse matemáticamente. Algunos ejemplos de datos cuantitativos son: la población de un país, la altura de una persona o las ganancias trimestrales de una empresa. Con un análisis adicional, los datos cuantitativos podrían usarse para descubrir tendencias estacionales del Índice de Calidad del Aire (AQI) o estimar la probabilidad de tráfico en hora punta en un día laboral típico.

### Datos Cualitativos
Los datos cualitativos, también conocidos como datos categóricos, son datos que no pueden medirse objetivamente como las observaciones de datos cuantitativos. Generalmente son varios formatos de datos subjetivos que capturan la calidad de algo, como un producto o proceso. A veces, los datos cualitativos son numéricos pero no se usarían típicamente de manera matemática, como números de teléfono o marcas de tiempo. Algunos ejemplos de datos cualitativos son: comentarios en videos, la marca y modelo de un automóvil o el color favorito de tus amigos más cercanos. Los datos cualitativos podrían usarse para entender qué productos prefieren los consumidores o identificar palabras clave populares en currículums de solicitudes de empleo.

### Datos Estructurados
Los datos estructurados son datos organizados en filas y columnas, donde cada fila tendrá el mismo conjunto de columnas. Las columnas representan un valor de un tipo particular y estarán identificadas con un nombre que describe lo que representa el valor, mientras que las filas contienen los valores reales. Las columnas a menudo tendrán un conjunto específico de reglas o restricciones sobre los valores, para garantizar que los valores representen con precisión la columna. Por ejemplo, imagina una hoja de cálculo de clientes donde cada fila debe tener un número de teléfono y los números de teléfono nunca contienen caracteres alfabéticos. Podría haber reglas aplicadas a la columna de números de teléfono para asegurarse de que nunca esté vacía y solo contenga números.

Un beneficio de los datos estructurados es que pueden organizarse de tal manera que puedan relacionarse con otros datos estructurados. Sin embargo, debido a que los datos están diseñados para estar organizados de una manera específica, realizar cambios en su estructura general puede requerir mucho esfuerzo. Por ejemplo, agregar una columna de correo electrónico a la hoja de cálculo de clientes que no puede estar vacía significa que tendrás que averiguar cómo agregar estos valores a las filas existentes de clientes en el conjunto de datos.

Ejemplos de datos estructurados: hojas de cálculo, bases de datos relacionales, números de teléfono, extractos bancarios.

### Datos No Estructurados
Los datos no estructurados generalmente no pueden categorizarse en filas o columnas y no contienen un formato o conjunto de reglas a seguir. Debido a que los datos no estructurados tienen menos restricciones en su estructura, es más fácil agregar nueva información en comparación con un conjunto de datos estructurado. Si un sensor que captura datos sobre la presión barométrica cada 2 minutos recibe una actualización que ahora le permite medir y registrar la temperatura, no requiere alterar los datos existentes si son no estructurados. Sin embargo, esto puede hacer que analizar o investigar este tipo de datos lleve más tiempo. Por ejemplo, un científico que quiere encontrar la temperatura promedio del mes anterior a partir de los datos del sensor, pero descubre que el sensor registró una "e" en algunos de sus datos para indicar que estaba roto en lugar de un número típico, lo que significa que los datos están incompletos.

Ejemplos de datos no estructurados: archivos de texto, mensajes de texto, archivos de video.

### Datos Semiestructurados
Los datos semiestructurados tienen características que los convierten en una combinación de datos estructurados y no estructurados. Generalmente no se ajustan a un formato de filas y columnas, pero están organizados de una manera que se considera estructurada y pueden seguir un formato fijo o un conjunto de reglas. La estructura variará entre fuentes, como una jerarquía bien definida o algo más flexible que permita una fácil integración de nueva información. Los metadatos son indicadores que ayudan a decidir cómo se organizan y almacenan los datos y tendrán varios nombres, según el tipo de datos. Algunos nombres comunes para los metadatos son etiquetas, elementos, entidades y atributos. Por ejemplo, un mensaje de correo electrónico típico tendrá un asunto, cuerpo y un conjunto de destinatarios y puede organizarse según quién o cuándo se envió.

Ejemplos de datos semiestructurados: HTML, archivos CSV, JavaScript Object Notation (JSON).

## Fuentes de Datos

Una fuente de datos es la ubicación inicial de donde se generaron los datos, o donde "viven", y variará según cómo y cuándo se recopilaron. Los datos generados por sus usuarios se conocen como datos primarios, mientras que los datos secundarios provienen de una fuente que ha recopilado datos para uso general. Por ejemplo, un grupo de científicos que recopila observaciones en una selva tropical se consideraría primario, y si deciden compartirlo con otros científicos, se consideraría secundario para aquellos que lo utilicen.

Las bases de datos son una fuente común y dependen de un sistema de gestión de bases de datos para alojar y mantener los datos, donde los usuarios utilizan comandos llamados consultas para explorar los datos. Los archivos como fuentes de datos pueden ser archivos de audio, imagen y video, así como hojas de cálculo como Excel. Las fuentes de internet son una ubicación común para alojar datos, donde se pueden encontrar tanto bases de datos como archivos. Las interfaces de programación de aplicaciones, también conocidas como APIs, permiten a los programadores crear formas de compartir datos con usuarios externos a través de internet, mientras que el proceso de web scraping extrae datos de una página web. Las [lecciones en Trabajando con Datos](../../../../../../../../../2-Working-With-Data) se centran en cómo usar varias fuentes de datos.

## Conclusión

En esta lección hemos aprendido:

- Qué son los datos
- Cómo se describen los datos
- Cómo se clasifican y categorizan los datos
- Dónde se pueden encontrar los datos

## 🚀 Desafío

Kaggle es una excelente fuente de conjuntos de datos abiertos. Usa la [herramienta de búsqueda de conjuntos de datos](https://www.kaggle.com/datasets) para encontrar algunos conjuntos de datos interesantes y clasifica de 3 a 5 conjuntos de datos con este criterio:

- ¿Los datos son cuantitativos o cualitativos?
- ¿Los datos son estructurados, no estructurados o semiestructurados?

## [Cuestionario Posterior a la Clase](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Revisión y Autoestudio

- Esta unidad de Microsoft Learn, titulada [Clasifica tus Datos](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), tiene un desglose detallado de datos estructurados, semiestructurados y no estructurados.

## Tarea

[Clasificando Conjuntos de Datos](assignment.md)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.