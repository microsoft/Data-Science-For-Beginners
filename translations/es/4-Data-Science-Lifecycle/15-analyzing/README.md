<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-24T00:44:58+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "es"
}
-->
# El Ciclo de Vida de la Ciencia de Datos: Analizando

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Ciclo de Vida de la Ciencia de Datos: Analizando - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

## Cuestionario Previo a la Clase

## [Cuestionario Previo a la Clase](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

El análisis en el ciclo de vida de los datos confirma que los datos pueden responder a las preguntas planteadas o resolver un problema en particular. Este paso también puede centrarse en confirmar que un modelo aborda correctamente estas preguntas y problemas. Esta lección se enfoca en el Análisis Exploratorio de Datos o EDA, que son técnicas para definir características y relaciones dentro de los datos y que pueden usarse para preparar los datos para el modelado.

Usaremos un conjunto de datos de ejemplo de [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) para mostrar cómo se puede aplicar esto con Python y la biblioteca Pandas. Este conjunto de datos contiene un conteo de algunas palabras comunes encontradas en correos electrónicos, las fuentes de estos correos son anónimas. Usa el [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) en este directorio para seguir el contenido.

## Análisis Exploratorio de Datos

La fase de captura del ciclo de vida es donde se adquieren los datos, así como los problemas y preguntas a abordar, pero ¿cómo sabemos si los datos pueden ayudar a respaldar el resultado final? 
Recuerda que un científico de datos puede hacerse las siguientes preguntas al adquirir los datos:
-   ¿Tengo suficientes datos para resolver este problema?
-   ¿Los datos tienen una calidad aceptable para este problema?
-   Si descubro información adicional a través de estos datos, ¿deberíamos considerar cambiar o redefinir los objetivos?

El Análisis Exploratorio de Datos es el proceso de familiarizarse con los datos y puede usarse para responder estas preguntas, así como para identificar los desafíos de trabajar con el conjunto de datos. Centrémonos en algunas de las técnicas utilizadas para lograr esto.

## Perfilado de Datos, Estadísticas Descriptivas y Pandas
¿Cómo evaluamos si tenemos suficientes datos para resolver este problema? El perfilado de datos puede resumir y recopilar información general sobre nuestro conjunto de datos a través de técnicas de estadísticas descriptivas. El perfilado de datos nos ayuda a entender qué está disponible para nosotros, y las estadísticas descriptivas nos ayudan a entender cuántas cosas están disponibles para nosotros.

En algunas de las lecciones anteriores, hemos usado Pandas para proporcionar algunas estadísticas descriptivas con la [función `describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Proporciona el conteo, valores máximos y mínimos, media, desviación estándar y cuantiles en los datos numéricos. Usar estadísticas descriptivas como la función `describe()` puede ayudarte a evaluar cuánto tienes y si necesitas más.

## Muestreo y Consultas
Explorar todo en un conjunto de datos grande puede ser muy lento y es una tarea que generalmente se deja a una computadora. Sin embargo, el muestreo es una herramienta útil para comprender los datos y permite tener una mejor idea de lo que hay en el conjunto de datos y lo que representa. Con una muestra, puedes aplicar probabilidad y estadísticas para llegar a algunas conclusiones generales sobre tus datos. Aunque no hay una regla definida sobre cuántos datos deberías muestrear, es importante notar que mientras más datos muestrees, más precisa será la generalización que puedas hacer sobre los datos. 

Pandas tiene la [función `sample()` en su biblioteca](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) donde puedes pasar un argumento de cuántas muestras aleatorias te gustaría recibir y usar.

Las consultas generales de los datos pueden ayudarte a responder algunas preguntas y teorías generales que puedas tener. En contraste con el muestreo, las consultas te permiten tener control y enfocarte en partes específicas de los datos sobre las que tienes preguntas. 
La [función `query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) en la biblioteca Pandas te permite seleccionar columnas y recibir respuestas simples sobre los datos a través de las filas recuperadas.

## Exploración con Visualizaciones
No tienes que esperar hasta que los datos estén completamente limpios y analizados para comenzar a crear visualizaciones. De hecho, tener una representación visual mientras exploras puede ayudar a identificar patrones, relaciones y problemas en los datos. Además, las visualizaciones proporcionan un medio de comunicación con aquellos que no están involucrados en la gestión de los datos y pueden ser una oportunidad para compartir y aclarar preguntas adicionales que no se abordaron en la etapa de captura. Consulta la [sección sobre Visualizaciones](../../../../../../../../../3-Data-Visualization) para aprender más sobre algunas formas populares de explorar visualmente.

## Exploración para identificar inconsistencias
Todos los temas de esta lección pueden ayudar a identificar valores faltantes o inconsistentes, pero Pandas proporciona funciones para verificar algunos de estos. [isna() o isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) pueden verificar valores faltantes. Una parte importante de explorar estos valores dentro de tus datos es explorar por qué terminaron de esa manera en primer lugar. Esto puede ayudarte a decidir qué [acciones tomar para resolverlos](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Cuestionario Previo a la Clase](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Tarea

[Explorando para obtener respuestas](assignment.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.