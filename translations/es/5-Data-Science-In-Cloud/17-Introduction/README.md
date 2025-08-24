<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-24T00:28:46+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "es"
}
-->
# Introducción a la Ciencia de Datos en la Nube

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Ciencia de Datos en la Nube: Introducción - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

En esta lección, aprenderás los principios fundamentales de la Nube, luego verás por qué puede ser interesante utilizar servicios en la Nube para ejecutar tus proyectos de ciencia de datos y revisaremos algunos ejemplos de proyectos de ciencia de datos realizados en la Nube.

## [Cuestionario Previo a la Clase](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## ¿Qué es la Nube?

La Nube, o Computación en la Nube, es la entrega de una amplia gama de servicios de computación bajo demanda, alojados en una infraestructura a través de internet. Los servicios incluyen soluciones como almacenamiento, bases de datos, redes, software, análisis y servicios inteligentes.

Normalmente diferenciamos entre Nube Pública, Privada e Híbrida de la siguiente manera:

* Nube pública: una nube pública es propiedad y está operada por un proveedor de servicios en la nube de terceros que entrega sus recursos de computación a través de Internet al público.
* Nube privada: se refiere a recursos de computación en la nube utilizados exclusivamente por una sola empresa u organización, con servicios e infraestructura mantenidos en una red privada.
* Nube híbrida: la nube híbrida es un sistema que combina nubes públicas y privadas. Los usuarios optan por un centro de datos local, mientras permiten que los datos y las aplicaciones se ejecuten en una o más nubes públicas.

La mayoría de los servicios de computación en la nube se dividen en tres categorías: Infraestructura como Servicio (IaaS), Plataforma como Servicio (PaaS) y Software como Servicio (SaaS).

* Infraestructura como Servicio (IaaS): los usuarios alquilan una infraestructura de TI como servidores y máquinas virtuales (VMs), almacenamiento, redes, sistemas operativos.
* Plataforma como Servicio (PaaS): los usuarios alquilan un entorno para desarrollar, probar, entregar y gestionar aplicaciones de software. Los usuarios no necesitan preocuparse por configurar o gestionar la infraestructura subyacente de servidores, almacenamiento, redes y bases de datos necesarias para el desarrollo.
* Software como Servicio (SaaS): los usuarios obtienen acceso a aplicaciones de software a través de Internet, bajo demanda y típicamente mediante una suscripción. Los usuarios no necesitan preocuparse por alojar y gestionar la aplicación de software, la infraestructura subyacente o el mantenimiento, como actualizaciones de software y parches de seguridad.

Algunos de los mayores proveedores de servicios en la nube son Amazon Web Services, Google Cloud Platform y Microsoft Azure.

## ¿Por qué elegir la Nube para la Ciencia de Datos?

Los desarrolladores y profesionales de TI eligen trabajar con la Nube por muchas razones, incluyendo las siguientes:

* Innovación: puedes potenciar tus aplicaciones integrando servicios innovadores creados por los proveedores de la Nube directamente en tus aplicaciones.
* Flexibilidad: solo pagas por los servicios que necesitas y puedes elegir entre una amplia gama de servicios. Normalmente pagas según el uso y adaptas tus servicios según tus necesidades cambiantes.
* Presupuesto: no necesitas hacer inversiones iniciales para comprar hardware y software, configurar y operar centros de datos locales, y puedes simplemente pagar por lo que usas.
* Escalabilidad: tus recursos pueden escalar según las necesidades de tu proyecto, lo que significa que tus aplicaciones pueden usar más o menos poder de computación, almacenamiento y ancho de banda, adaptándose a factores externos en cualquier momento.
* Productividad: puedes enfocarte en tu negocio en lugar de gastar tiempo en tareas que pueden ser gestionadas por otros, como administrar centros de datos.
* Fiabilidad: la computación en la nube ofrece varias formas de respaldar continuamente tus datos y puedes configurar planes de recuperación ante desastres para mantener tu negocio y servicios funcionando, incluso en tiempos de crisis.
* Seguridad: puedes beneficiarte de políticas, tecnologías y controles que fortalecen la seguridad de tu proyecto.

Estas son algunas de las razones más comunes por las que las personas eligen usar servicios en la Nube. Ahora que tenemos una mejor comprensión de qué es la Nube y cuáles son sus principales beneficios, veamos más específicamente los trabajos de los científicos de datos y desarrolladores que trabajan con datos, y cómo la Nube puede ayudarlos con varios desafíos que podrían enfrentar:

* Almacenar grandes cantidades de datos: en lugar de comprar, gestionar y proteger grandes servidores, puedes almacenar tus datos directamente en la nube, con soluciones como Azure Cosmos DB, Azure SQL Database y Azure Data Lake Storage.
* Realizar integración de datos: la integración de datos es una parte esencial de la Ciencia de Datos, que te permite hacer la transición de la recopilación de datos a la toma de decisiones. Con los servicios de integración de datos ofrecidos en la nube, puedes recopilar, transformar e integrar datos de diversas fuentes en un único almacén de datos, con Data Factory.
* Procesar datos: procesar grandes cantidades de datos requiere mucho poder de computación, y no todos tienen acceso a máquinas lo suficientemente potentes para ello, por lo que muchas personas optan por aprovechar directamente el enorme poder de computación de la nube para ejecutar y desplegar sus soluciones.
* Usar servicios de análisis de datos: servicios en la nube como Azure Synapse Analytics, Azure Stream Analytics y Azure Databricks te ayudan a convertir tus datos en información procesable.
* Usar servicios de aprendizaje automático e inteligencia de datos: en lugar de empezar desde cero, puedes usar algoritmos de aprendizaje automático ofrecidos por el proveedor de la nube, con servicios como AzureML. También puedes usar servicios cognitivos como conversión de voz a texto, texto a voz, visión por computadora y más.

## Ejemplos de Ciencia de Datos en la Nube

Hagamos esto más tangible revisando un par de escenarios.

### Análisis de sentimiento en redes sociales en tiempo real

Comenzaremos con un escenario comúnmente estudiado por personas que inician con el aprendizaje automático: análisis de sentimiento en redes sociales en tiempo real.

Supongamos que diriges un sitio web de noticias y quieres aprovechar datos en vivo para entender qué contenido podría interesar a tus lectores. Para saber más sobre esto, puedes construir un programa que realice análisis de sentimiento en tiempo real de datos provenientes de publicaciones en Twitter, sobre temas relevantes para tus lectores.

Los indicadores clave que observarás son el volumen de tweets sobre temas específicos (hashtags) y el sentimiento, que se establece utilizando herramientas de análisis que realizan análisis de sentimiento en torno a los temas especificados.

Los pasos necesarios para crear este proyecto son los siguientes:

* Crear un centro de eventos para la entrada de transmisión, que recolectará datos de Twitter.
* Configurar y iniciar una aplicación cliente de Twitter, que llamará a las APIs de transmisión de Twitter.
* Crear un trabajo de Stream Analytics.
* Especificar la entrada y consulta del trabajo.
* Crear un destino de salida y especificar la salida del trabajo.
* Iniciar el trabajo.

Para ver el proceso completo, consulta la [documentación](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Análisis de artículos científicos

Tomemos otro ejemplo de un proyecto creado por [Dmitry Soshnikov](http://soshnikov.com), uno de los autores de este currículo.

Dmitry creó una herramienta que analiza artículos sobre COVID. Al revisar este proyecto, verás cómo puedes crear una herramienta que extraiga conocimiento de artículos científicos, obtenga información y ayude a los investigadores a navegar eficientemente a través de grandes colecciones de artículos.

Veamos los diferentes pasos utilizados para esto:

* Extraer y preprocesar información con [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Usar [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) para paralelizar el procesamiento.
* Almacenar y consultar información con [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Crear un panel interactivo para la exploración y visualización de datos usando Power BI.

Para ver el proceso completo, visita el [blog de Dmitry](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Como puedes ver, podemos aprovechar los servicios en la Nube de muchas maneras para realizar Ciencia de Datos.

## Nota al pie

Fuentes:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Cuestionario Posterior a la Clase

[Cuestionario posterior a la clase](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Tarea

[Investigación de Mercado](assignment.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.