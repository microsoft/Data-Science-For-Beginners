<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "661dad02c3ac239644d34c1eb51e76f8",
  "translation_date": "2025-09-06T20:13:57+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "es"
}
-->
# El Ciclo de Vida de la Ciencia de Datos: Analizando

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Ciclo de Vida de la Ciencia de Datos: Analizando - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

## [Cuestionario Previo a la Clase](https://ff-quizzes.netlify.app/en/ds/quiz/28)

El análisis en el ciclo de vida de los datos confirma que los datos pueden responder a las preguntas planteadas o resolver un problema en particular. Este paso también puede centrarse en confirmar que un modelo aborda correctamente estas preguntas y problemas. Esta lección se enfoca en el Análisis Exploratorio de Datos o EDA, que son técnicas para definir características y relaciones dentro de los datos y que pueden ser utilizadas para preparar los datos para el modelado.

Usaremos un conjunto de datos de ejemplo de [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) para mostrar cómo esto puede aplicarse con Python y la biblioteca Pandas. Este conjunto de datos contiene un conteo de algunas palabras comunes encontradas en correos electrónicos, las fuentes de estos correos son anónimas. Utiliza el [notebook](notebook.ipynb) en este directorio para seguir el contenido.

## Análisis Exploratorio de Datos

La fase de captura del ciclo de vida es donde se adquieren los datos, así como los problemas y preguntas en cuestión, pero ¿cómo sabemos que los datos pueden ayudar a respaldar el resultado final? 
Recuerda que un científico de datos puede hacerse las siguientes preguntas al adquirir los datos:
-   ¿Tengo suficientes datos para resolver este problema?
-   ¿Los datos tienen una calidad aceptable para este problema?
-   Si descubro información adicional a través de estos datos, ¿deberíamos considerar cambiar o redefinir los objetivos?

El Análisis Exploratorio de Datos es el proceso de conocer los datos y puede ser utilizado para responder estas preguntas, así como para identificar los desafíos de trabajar con el conjunto de datos. Centrémonos en algunas de las técnicas utilizadas para lograr esto.

## Perfilado de Datos, Estadísticas Descriptivas y Pandas

¿Cómo evaluamos si tenemos suficientes datos para resolver este problema? El perfilado de datos puede resumir y recopilar información general sobre nuestro conjunto de datos mediante técnicas de estadísticas descriptivas. El perfilado de datos nos ayuda a entender qué está disponible para nosotros, y las estadísticas descriptivas nos ayudan a entender cuántas cosas están disponibles para nosotros.

En algunas de las lecciones anteriores, hemos utilizado Pandas para proporcionar algunas estadísticas descriptivas con la función [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Esta función proporciona el conteo, valores máximos y mínimos, media, desviación estándar y cuantiles en los datos numéricos. Utilizar estadísticas descriptivas como la función `describe()` puede ayudarte a evaluar cuánto tienes y si necesitas más.

## Muestreo y Consultas

Explorar todo en un conjunto de datos grande puede ser muy laborioso y es una tarea que generalmente se deja a una computadora. Sin embargo, el muestreo es una herramienta útil para entender los datos y nos permite tener una mejor comprensión de lo que hay en el conjunto de datos y lo que representa. Con una muestra, puedes aplicar probabilidad y estadísticas para llegar a algunas conclusiones generales sobre tus datos. Aunque no hay una regla definida sobre cuántos datos deberías muestrear, es importante notar que mientras más datos muestrees, más precisa será la generalización que puedas hacer sobre los datos.

Pandas tiene la función [`sample()` en su biblioteca](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) donde puedes pasar un argumento indicando cuántas muestras aleatorias deseas recibir y utilizar.

Las consultas generales de los datos pueden ayudarte a responder algunas preguntas y teorías generales que puedas tener. En contraste con el muestreo, las consultas te permiten tener control y enfocarte en partes específicas de los datos sobre las que tienes preguntas. 
La función [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) en la biblioteca Pandas te permite seleccionar columnas y recibir respuestas simples sobre los datos a través de las filas recuperadas.

## Exploración con Visualizaciones

No tienes que esperar hasta que los datos estén completamente limpios y analizados para comenzar a crear visualizaciones. De hecho, tener una representación visual mientras exploras puede ayudar a identificar patrones, relaciones y problemas en los datos. Además, las visualizaciones proporcionan un medio de comunicación con aquellos que no están involucrados en la gestión de los datos y pueden ser una oportunidad para compartir y aclarar preguntas adicionales que no se abordaron en la etapa de captura. Consulta la [sección sobre Visualizaciones](../../../../../../../../../3-Data-Visualization) para aprender más sobre algunas formas populares de explorar visualmente.

## Exploración para identificar inconsistencias

Todos los temas de esta lección pueden ayudar a identificar valores faltantes o inconsistentes, pero Pandas proporciona funciones para verificar algunos de estos. [isna() o isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) pueden verificar valores faltantes. Una parte importante de explorar estos valores dentro de tus datos es investigar por qué terminaron de esa manera en primer lugar. Esto puede ayudarte a decidir qué [acciones tomar para resolverlos](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Cuestionario Posterior a la Clase](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Tarea

[Explorando para respuestas](assignment.md)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.