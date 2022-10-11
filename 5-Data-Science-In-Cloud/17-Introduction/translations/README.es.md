# Introducción a la Ciencia de Datos en la Nube

|![ Sketchnote de [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Ciencia de Datos en la Nube: Introducción - _Sketchnote de [@nitya](https://twitter.com/nitya)_ |

En esta lección, aprenderás los principios fundamentales de la Nube, luego verás por qué puede ser interesante para ti usar los servicios de la Nube para ejecutar tus proyectos de ciencia de datos y veremos algunos ejemplos de proyectos de ciencia de datos ejecutándose en la Nube.

## [Examen previo a la lección](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## ¿Qué es la Nube?

La Nube o Cómputo en la Nube, es la distribución de un amplio rango de servicios de cómputo de pago por uso alojados en una infraestructura a través de internet. Los servicios incluyen soluciones tales como almacenamiento, bases de datos, redes, software, analítica y servicios inteligentes.

Solemos diferenciar las nubres Públicas, Privadas e Híbridas como sigue:

* Nube pública: una nuve pública pertenece y es operada por un proveedor de servicios de terceros el cual distribuye sus recursos de cómputo a través de internet al público.
* Nube privada: se refiere a los recursos de cómputo en la nube usados de forma exclusiva por un único negocio u organización, con servicios y una infrestructura mantenida en una red privada.
* Nube híbrida: la bure híbrida es una sistema que combina las nubes públicas y privadas. Los usuarios optan por centros de datos en sus instalaciones, mientras permiten que datos y aplicaciones se ejecuten en una o más nubes públicas.

La mayoría de servicios de cómputo en la nube caen en tres categorías: Infraestructura como servicio (IaaS), Plataforma como servicio (PaaS) y Software como servicio (SaaS).

* Infraestructura como Servicio (IaaS): los usuarios rentan una infraestructura de TI tales como servidores y máquinas virtuales (VMs), almacenamiento, redes, sistemas operativos.
* Plataforma como Servicio (PaaS): los usuarios rentan un ambiente para desarroller, probar, liberar y administrar aplicaciones de software. Los usuarios no necesitan preocuparse por configurar y administrar la infraestructura subyacente de los servidores, almacenamiento, red y bases de datos necesarias para el desarrollo.
* Software como Servicio (SaaS): los usuarios obtienen acceso a aplicaciones de software a través de Internet, bajo demanda y típicamente por una suscripción. Los usuarios no necesitan preocuparse por el alojamiento y administración de las aplicaciones software, la infraestructura subyacente o el mantenimiento, como actualizaciones de software y parches de seguridad.

Algunos de los más grandes proveedores de la Nube son Amazon Web Services, Google Cloud Platform y Microsoft Azure.

## ¿Por qué elegir la Nube para Ciencia de Datos?

Los desarrolladores y profesionales de TI eligen trabajar con la Nube for diversas razones, incluyendo las siguientes:

* Innovación: puedes potenciar tus aplicaciones al integrar servicios innovadores creados por los proveedores de la Nube agregándolos directamente a tus apps.
* Flexibilidad: sólo pagas por los servicios que necesitas y puedes elegir entre un amplio rango de servicios. Típicamente pagas por consumo y adaptas tus servicios de acuerdo a cómo evolucionan tus necesidades.
* Presupuesto: no necesitas realizar inversiones iniciales para pagar hardware y software, configurar y ejecutar centros de datos y sólo pagas por lo que usas.
* Escalabilidad: tus recursos escalan de acuerdo a las necesidades de tu proyecto, lo cual significa que tus apps pueden usar más o menos poder de cómputo, almacenamiento y ancho de banda, al adaptarse a los factores externos par aun tiempo especificado.
* Productividad: puedes enfocarte en un negocio en lugar de invertir tiempo en tareas que pueden ser gestionadas por alguien más, tal como la administración de centros de datos.
* Fiabilidad: el Cómputo en la Nube ofrece varias formas de respaldar tus datos de forma continua y configurar planes de cuperación ante desastres para mantener tu negocio y servicios en marcha, aún en tiempos de crisis.
* Seguridad: te puedes beneficiar de políticas, tecnologías y controles que fortalezcan la seguridad de tu proyecto.

Estas son algunas de las razones más comunes por qué la gente elige usar los servicios en la Nube. Ahora que tienes un mejor entendimiento de qué es la Nube y cuáles son sus principales beneficios, veamos más específicamente acerca de los trabajos de los Científicos de Datos y desarrolladores que trabajan con datos, y cómo la Nube puede ayudarlos con varios desafíos que pueden enfrentar:

* Almacenar grandes cantidades de datos: en lugar de comprar, administrar y proteger grandes servidores, puedes almacenar tus datos directamente en la nube, con soluciones tales como Azure Cosmos DB, Azure SQL Database y el almacenamiento de Azure Data Lake.
* Realizar Integración de Datos: la integración de datos es una parte esencial de la Ciencia de Datos, que te permite realizar una transición desde recolectar datos hasta la toma de acciones. Con los servicios de integración de datos que ofrece la nube, puedes recolectar, transformar e integrar datos desde varias fuentes en un sólo almacén de datos, con Data Factory.
* Procesamiento de datos: procesar vastas cantidades de datos requiere mucho poder de cómputo, y no cualquiera tiene acceso a máquinas lo suficientemente poderosas para ello, lo cual es el motivo para que mucha gente elija aprovechar directamente el gran poder de cómputo de la nube para ejecutar y desplegar sus soluciones.
* Usar servicios de analítica de datos: servicios de la nube como Azure Synapse Analytics, Azure Stream Analytics y Azure Databricks para ayudarte a convertir tus datos en conocimiento procesable.
* Usar srevicios de Aprendizaje Automático e Inteligecia de datos: En lugar de iniciar desde cero, puedes usar algoritmos de aprendizaje automático ofrecidos por el proveedor de la nube, con servicios como AzureML. También puedes suar servicios cognitivos como voz a texto, texto a voz, visión por computador y más.

## Ejemplos de Ciencia de Datos en la Nube

Hagamos esto más tangible al mirar algunos escenarios.

### Análisis de sentimiento de medios sociales en tiempo real

Comenzaremos con un escenario comúnmente estudiado por la gente que comienza en el aprendizaje automático: análisis de sentimiento en medios sociales en tiempo real.

Digamos que manejas un sitio web de medios informativos y quieres aprovechar los datos en tiempo real para entender qué contenido podría interesarle a tus lectores. Para saber más acerca de ello, puedes construir un programa que realice análisis de sentimienot en tiempo real de los datos de publicaciones en Twitter, sobre temas que son relevantes para tus lectores.

Los indicadores clave que buscarás es el volumen de tweets sobre temas específicos (hashtags) y sentimiento, el cual es establecido usando herramientas de analítica que realizan análisis de sentimiento alrededor de los temas especificados.

Los pasos necesarios para crear este proyecto son los siguientes:

* Crea un centro de eventos para la entrada de transmisión, el cual recolectará los datos de Twitter
* Configura e inicia una aplicación cliente de Twitter, la cual llamará a las APIs de transmisión de Twitter
* Crea un job de Stream Analytics
* Especifica la entrada y query del job
* Crea un sink de salida y especifica la salida del job
* Inicia el job

Para ver el proceso completo revisa la [documentación](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Análisis de artículos científicos

Tomemos otro ejemplo de un proyecto creado por [Dmitry Soshnikov](http://soshnikov.com), uno de los autores de este curso.

Dmitry creó una herramienta que analiza artículos de COVID. Al revisar este proyecto, verás cómo puedes crear una herramienta que extraiga conocimiento de artículos científicos, obtenga conocimiento y ayude a los investigadores a navegar a través de grandes colecciones de artículos de una forma eficiente.

Veamos los distintos pasos usados para esto:

* Extracción y pre-procesamiento de la información con [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Uso de [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) para paralelizar el procesamiento
* Almacén y consulta de la información con [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Crea un tablero interactivo para la exploración de datos y visualización usando Power BI

Para ver el proceso completo, visita [Dmitry’s blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Como puedes ver, podemos aprovechar los servicios en la Nube de muchas formas para realizar Ciencia de Datos.

## Nota al pie

Fuentes:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/

## Examen posterior a la lección

[Examen posterior a la lección](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Asignación

[Investifación de mercado](../translations/assignment.es.md)
