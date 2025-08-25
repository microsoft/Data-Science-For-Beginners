<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "14b2a7f1c63202920bd98eeb913f5614",
  "translation_date": "2025-08-24T21:54:19+00:00",
  "source_file": "5-Data-Science-In-Cloud/18-Low-Code/README.md",
  "language_code": "es"
}
-->
# Ciencia de Datos en la Nube: El enfoque "Low code/No code"

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/18-DataScience-Cloud.png)|
|:---:|
| Ciencia de Datos en la Nube: Low Code - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Tabla de contenidos:

- [Ciencia de Datos en la Nube: El enfoque "Low code/No code"](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Cuestionario previo a la clase](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [1. Introducción](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.1 ¿Qué es Azure Machine Learning?](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.2 El Proyecto de Predicción de Insuficiencia Cardíaca:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.3 El Conjunto de Datos de Insuficiencia Cardíaca:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [2. Entrenamiento Low code/No code de un modelo en Azure ML Studio](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.1 Crear un espacio de trabajo en Azure ML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.2 Recursos de Cómputo](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.1 Elegir las opciones correctas para tus recursos de cómputo](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.2 Crear un clúster de cómputo](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.3 Cargar el conjunto de datos](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.4 Entrenamiento Low code/No code con AutoML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [3. Despliegue del modelo Low code/No code y consumo del endpoint](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.1 Despliegue del modelo](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.2 Consumo del endpoint](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [🚀 Desafío](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Cuestionario posterior a la clase](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Revisión y Autoestudio](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Tarea](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  
## [Cuestionario previo a la clase](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/34)
## 1. Introducción
### 1.1 ¿Qué es Azure Machine Learning?

La plataforma en la nube de Azure incluye más de 200 productos y servicios diseñados para ayudarte a dar vida a nuevas soluciones. Los científicos de datos dedican mucho esfuerzo a explorar y preprocesar datos, y a probar varios tipos de algoritmos de entrenamiento de modelos para producir modelos precisos. Estas tareas consumen tiempo y, a menudo, hacen un uso ineficiente de hardware de cómputo costoso.

[Azure ML](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) es una plataforma basada en la nube para construir y operar soluciones de aprendizaje automático en Azure. Incluye una amplia gama de características y capacidades que ayudan a los científicos de datos a preparar datos, entrenar modelos, publicar servicios predictivos y monitorear su uso. Lo más importante es que les ayuda a aumentar su eficiencia al automatizar muchas de las tareas que consumen tiempo asociadas con el entrenamiento de modelos; y les permite usar recursos de cómputo basados en la nube que escalan de manera efectiva para manejar grandes volúmenes de datos, incurriendo en costos solo cuando realmente se utilizan.

Azure ML proporciona todas las herramientas que los desarrolladores y científicos de datos necesitan para sus flujos de trabajo de aprendizaje automático. Estas incluyen:

- **Azure Machine Learning Studio**: un portal web en Azure Machine Learning para opciones de bajo código y sin código para entrenamiento de modelos, despliegue, automatización, seguimiento y gestión de activos. El estudio se integra con el SDK de Azure Machine Learning para una experiencia fluida.
- **Jupyter Notebooks**: prototipado rápido y pruebas de modelos de ML.
- **Azure Machine Learning Designer**: permite arrastrar y soltar módulos para construir experimentos y luego desplegar pipelines en un entorno de bajo código.
- **Interfaz de AutoML**: automatiza tareas iterativas del desarrollo de modelos de aprendizaje automático, permitiendo construir modelos de ML con alta escala, eficiencia y productividad, manteniendo la calidad del modelo.
- **Etiquetado de datos**: una herramienta asistida de ML para etiquetar datos automáticamente.
- **Extensión de aprendizaje automático para Visual Studio Code**: proporciona un entorno de desarrollo completo para construir y gestionar proyectos de ML.
- **CLI de aprendizaje automático**: comandos para gestionar recursos de Azure ML desde la línea de comandos.
- **Integración con frameworks de código abierto** como PyTorch, TensorFlow, Scikit-learn y muchos más para entrenar, desplegar y gestionar el proceso de aprendizaje automático de principio a fin.
- **MLflow**: una biblioteca de código abierto para gestionar el ciclo de vida de tus experimentos de aprendizaje automático. **MLFlow Tracking** es un componente de MLflow que registra y rastrea las métricas de tus ejecuciones de entrenamiento y artefactos de modelos, independientemente del entorno de tu experimento.

### 1.2 El Proyecto de Predicción de Insuficiencia Cardíaca:

No hay duda de que crear y construir proyectos es la mejor manera de poner a prueba tus habilidades y conocimientos. En esta lección, vamos a explorar dos formas diferentes de construir un proyecto de ciencia de datos para la predicción de ataques de insuficiencia cardíaca en Azure ML Studio, a través de Low code/No code y mediante el SDK de Azure ML, como se muestra en el siguiente esquema:

![project-schema](../../../../translated_images/project-schema.736f6e403f321eb48d10242b3f4334dc6ccf0eabef8ff87daf52b89781389fcb.es.png)

Cada enfoque tiene sus propios pros y contras. El enfoque Low code/No code es más fácil para comenzar, ya que implica interactuar con una interfaz gráfica (GUI), sin necesidad de conocimientos previos de programación. Este método permite probar rápidamente la viabilidad del proyecto y crear un POC (Prueba de Concepto). Sin embargo, a medida que el proyecto crece y necesita estar listo para producción, no es factible crear recursos a través de la GUI. Necesitamos automatizar todo programáticamente, desde la creación de recursos hasta el despliegue de un modelo. Aquí es donde saber cómo usar el SDK de Azure ML se vuelve crucial.

|                   | Low code/No code | SDK de Azure ML           |
|-------------------|------------------|---------------------------|
| Experiencia en código | No requerida     | Requerida                  |
| Tiempo de desarrollo   | Rápido y fácil   | Depende de la experiencia en código |
| Listo para producción  | No               | Sí                        |

### 1.3 El Conjunto de Datos de Insuficiencia Cardíaca: 

Las enfermedades cardiovasculares (ECV) son la principal causa de muerte a nivel mundial, representando el 31% de todas las muertes en el mundo. Factores de riesgo ambientales y conductuales como el uso de tabaco, dieta poco saludable y obesidad, inactividad física y consumo nocivo de alcohol podrían usarse como características para modelos de estimación. Poder estimar la probabilidad de desarrollar una ECV podría ser de gran utilidad para prevenir ataques en personas de alto riesgo.

Kaggle ha puesto a disposición pública un [conjunto de datos de insuficiencia cardíaca](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) que vamos a usar para este proyecto. Puedes descargar el conjunto de datos ahora. Este es un conjunto de datos tabular con 13 columnas (12 características y 1 variable objetivo) y 299 filas. 

|    | Nombre de la variable      | Tipo            | Descripción                                               | Ejemplo           |
|----|---------------------------|-----------------|-----------------------------------------------------------|-------------------|
| 1  | age                       | numérico        | Edad del paciente                                         | 25                |
| 2  | anaemia                   | booleano        | Disminución de glóbulos rojos o hemoglobina               | 0 o 1            |
| 3  | creatinine_phosphokinase  | numérico        | Nivel de la enzima CPK en la sangre                       | 542               |
| 4  | diabetes                  | booleano        | Si el paciente tiene diabetes                             | 0 o 1            |
| 5  | ejection_fraction         | numérico        | Porcentaje de sangre que sale del corazón en cada contracción | 45                |
| 6  | high_blood_pressure       | booleano        | Si el paciente tiene hipertensión                         | 0 o 1            |
| 7  | platelets                 | numérico        | Plaquetas en la sangre                                    | 149000            |
| 8  | serum_creatinine          | numérico        | Nivel de creatinina sérica en la sangre                   | 0.5               |
| 9  | serum_sodium              | numérico        | Nivel de sodio sérico en la sangre                        | jun               |
| 10 | sex                       | booleano        | Mujer u hombre                                            | 0 o 1            |
| 11 | smoking                   | booleano        | Si el paciente fuma                                       | 0 o 1            |
| 12 | time                      | numérico        | Período de seguimiento (días)                             | 4                 |
|----|---------------------------|-----------------|-----------------------------------------------------------|-------------------|
| 21 | DEATH_EVENT [Objetivo]    | booleano        | Si el paciente muere durante el período de seguimiento    | 0 o 1            |

Una vez que tengas el conjunto de datos, podemos comenzar el proyecto en Azure.

## 2. Entrenamiento Low code/No code de un modelo en Azure ML Studio
### 2.1 Crear un espacio de trabajo en Azure ML
Para entrenar un modelo en Azure ML, primero necesitas crear un espacio de trabajo en Azure ML. El espacio de trabajo es el recurso de nivel superior para Azure Machine Learning, proporcionando un lugar centralizado para trabajar con todos los artefactos que creas al usar Azure Machine Learning. El espacio de trabajo mantiene un historial de todas las ejecuciones de entrenamiento, incluidos registros, métricas, resultados y una instantánea de tus scripts. Usas esta información para determinar qué ejecución de entrenamiento produce el mejor modelo. [Aprende más](https://docs.microsoft.com/azure/machine-learning/concept-workspace?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

Se recomienda usar el navegador más actualizado que sea compatible con tu sistema operativo. Los siguientes navegadores son compatibles:

- Microsoft Edge (El nuevo Microsoft Edge, última versión. No Microsoft Edge legacy)
- Safari (última versión, solo Mac)
- Chrome (última versión)
- Firefox (última versión)

Para usar Azure Machine Learning, crea un espacio de trabajo en tu suscripción de Azure. Luego puedes usar este espacio de trabajo para gestionar datos, recursos de cómputo, código, modelos y otros artefactos relacionados con tus cargas de trabajo de aprendizaje automático.

> **_NOTA:_** Tu suscripción de Azure se cobrará una pequeña cantidad por almacenamiento de datos mientras el espacio de trabajo de Azure Machine Learning exista en tu suscripción, por lo que te recomendamos eliminar el espacio de trabajo de Azure Machine Learning cuando ya no lo estés utilizando.

1. Inicia sesión en el [portal de Azure](https://ms.portal.azure.com/) usando las credenciales de Microsoft asociadas con tu suscripción de Azure.
2. Selecciona **＋Crear un recurso**
   
   ![workspace-1](../../../../translated_images/workspace-1.ac8694d60b073ed1ae8333d71244dc8a9b3e439d54593724f98f1beefdd27b08.es.png)

   Busca Machine Learning y selecciona el mosaico de Machine Learning.

   ![workspace-2](../../../../translated_images/workspace-2.ae7c486db8796147075e4a56566aa819827dd6c4c8d18d64590317c3be625f17.es.png)

   Haz clic en el botón de crear.

   ![workspace-3](../../../../translated_images/workspace-3.398ca4a5858132cce584db9df10c5a011cd9075eb182e647a77d5cac01771eea.es.png)

   Completa la configuración como sigue:
   - Suscripción: Tu suscripción de Azure
   - Grupo de recursos: Crea o selecciona un grupo de recursos
   - Nombre del espacio de trabajo: Ingresa un nombre único para tu espacio de trabajo
   - Región: Selecciona la región geográfica más cercana a ti
   - Cuenta de almacenamiento: Nota la nueva cuenta de almacenamiento predeterminada que se creará para tu espacio de trabajo
   - Key vault: Nota el nuevo key vault predeterminado que se creará para tu espacio de trabajo
   - Application insights: Nota el nuevo recurso de application insights predeterminado que se creará para tu espacio de trabajo
   - Registro de contenedor: Ninguno (se creará automáticamente la primera vez que despliegues un modelo en un contenedor)

    ![workspace-4](../../../../translated_images/workspace-4.bac87f6599c4df63e624fc2608990f965887bee551d9dedc71c687b43b986b6a.es.png)

   - Haz clic en crear + revisar y luego en el botón de crear.
3. Espera a que se cree tu espacio de trabajo (esto puede tardar unos minutos). Luego ve a él en el portal. Puedes encontrarlo a través del servicio de Azure Machine Learning.
4. En la página de resumen de tu espacio de trabajo, lanza Azure Machine Learning Studio (o abre una nueva pestaña del navegador y navega a https://ml.azure.com), e inicia sesión en Azure Machine Learning Studio usando tu cuenta de Microsoft. Si se te solicita, selecciona tu directorio y suscripción de Azure, y tu espacio de trabajo de Azure Machine Learning.
   
![workspace-5](../../../../translated_images/workspace-5.a6eb17e0a5e6420018b08bdaf3755ce977f96f1df3ea363d2476a9dce7e15adb.es.png)

5. En Azure Machine Learning Studio, alterna el ícono ☰ en la parte superior izquierda para ver las diferentes páginas de la interfaz. Puedes usar estas páginas para gestionar los recursos en tu espacio de trabajo.

![workspace-6](../../../../translated_images/workspace-6.8dd81fe841797ee17f8f73916769576260b16c4e17e850d277a49db35fd74a15.es.png)

Puedes gestionar tu espacio de trabajo usando el portal de Azure, pero para los científicos de datos e ingenieros de operaciones de aprendizaje automático, Azure Machine Learning Studio proporciona una interfaz de usuario más enfocada para gestionar los recursos del espacio de trabajo.

### 2.2 Recursos de Cómputo

Los recursos de cómputo son recursos basados en la nube en los que puedes ejecutar procesos de entrenamiento de modelos y exploración de datos. Hay cuatro tipos de recursos de cómputo que puedes crear:

- **Instancias de cómputo**: Estaciones de trabajo de desarrollo que los científicos de datos pueden usar para trabajar con datos y modelos. Esto implica la creación de una máquina virtual (VM) y el lanzamiento de una instancia de notebook. Luego puedes entrenar un modelo llamando a un clúster de cómputo desde el notebook.
- **Clústeres de cómputo**: Clústeres escalables de máquinas virtuales para el procesamiento bajo demanda de código de experimentos. Los necesitarás al entrenar un modelo. Los clústeres de cómputo también pueden emplear recursos especializados de GPU o CPU.
- **Clústeres de inferencia**: Objetivos de despliegue para servicios predictivos que usan tus modelos entrenados.
- **Compute adjunto**: Enlaza con recursos de cómputo existentes en Azure, como Máquinas Virtuales o clústeres de Azure Databricks.

#### 2.2.1 Elegir las opciones correctas para tus recursos de cómputo

Hay algunos factores clave a considerar al crear un recurso de cómputo, y esas decisiones pueden ser críticas.

**¿Necesitas CPU o GPU?**

Una CPU (Unidad Central de Procesamiento) es el circuito electrónico que ejecuta las instrucciones de un programa de computadora. Una GPU (Unidad de Procesamiento Gráfico) es un circuito electrónico especializado que puede ejecutar código relacionado con gráficos a una velocidad muy alta.

La principal diferencia entre la arquitectura de CPU y GPU es que una CPU está diseñada para manejar una amplia gama de tareas rápidamente (medido por la velocidad del reloj de la CPU), pero está limitada en la concurrencia de tareas que pueden ejecutarse. Las GPUs están diseñadas para la computación paralela y, por lo tanto, son mucho mejores para tareas de aprendizaje profundo.

| CPU                                     | GPU                         |
|-----------------------------------------|-----------------------------|
| Menos costosa                           | Más costosa                 |
| Menor nivel de concurrencia             | Mayor nivel de concurrencia |
| Más lenta en entrenar modelos de aprendizaje profundo | Óptima para aprendizaje profundo |

**Tamaño del clúster**

Los clústeres más grandes son más costosos, pero ofrecen mejor capacidad de respuesta. Por lo tanto, si tienes tiempo pero no suficiente dinero, deberías comenzar con un clúster pequeño. Por el contrario, si tienes dinero pero no mucho tiempo, deberías comenzar con un clúster más grande.

**Tamaño de la VM**

Dependiendo de tus restricciones de tiempo y presupuesto, puedes variar el tamaño de tu RAM, disco, número de núcleos y velocidad del reloj. Incrementar todos esos parámetros será más costoso, pero resultará en un mejor rendimiento.

**¿Instancias dedicadas o de baja prioridad?**

Una instancia de baja prioridad significa que es interrumpible: esencialmente, Microsoft Azure puede tomar esos recursos y asignarlos a otra tarea, interrumpiendo así un trabajo. Una instancia dedicada, o no interrumpible, significa que el trabajo nunca será terminado sin tu permiso.  
Esta es otra consideración de tiempo vs dinero, ya que las instancias interrumpibles son menos costosas que las dedicadas.

#### 2.2.2 Crear un clúster de cómputo

En el [espacio de trabajo de Azure ML](https://ml.azure.com/) que creamos anteriormente, ve a la sección de cómputo y podrás ver los diferentes recursos de cómputo que acabamos de discutir (es decir, instancias de cómputo, clústeres de cómputo, clústeres de inferencia y cómputo adjunto). Para este proyecto, necesitaremos un clúster de cómputo para entrenar el modelo. En el Studio, haz clic en el menú "Compute", luego en la pestaña "Compute cluster" y haz clic en el botón "+ New" para crear un clúster de cómputo.

![22](../../../../translated_images/cluster-1.b78cb630bb543729b11f60c34d97110a263f8c27b516ba4dc47807b3cee5579f.es.png)

1. Elige tus opciones: Dedicado vs Baja prioridad, CPU o GPU, tamaño de la VM y número de núcleos (puedes mantener la configuración predeterminada para este proyecto).  
2. Haz clic en el botón Next.

![23](../../../../translated_images/cluster-2.ea30cdbc9f926bb9e05af3fdbc1f679811c796dc2a6847f935290aec15526e88.es.png)

3. Asigna un nombre al clúster de cómputo.  
4. Elige tus opciones: Número mínimo/máximo de nodos, segundos de inactividad antes de reducir el tamaño, acceso SSH. Ten en cuenta que si el número mínimo de nodos es 0, ahorrarás dinero cuando el clúster esté inactivo. Ten en cuenta que mientras mayor sea el número máximo de nodos, más corto será el tiempo de entrenamiento. El número máximo de nodos recomendado es 3.  
5. Haz clic en el botón "Create". Este paso puede tardar unos minutos.

![29](../../../../translated_images/cluster-3.8a334bc070ec173a329ce5abd2a9d727542e83eb2347676c9af20f2c8870b3e7.es.png)

¡Genial! Ahora que tenemos un clúster de cómputo, necesitamos cargar los datos en Azure ML Studio.

### 2.3 Cargar el conjunto de datos

1. En el [espacio de trabajo de Azure ML](https://ml.azure.com/) que creamos anteriormente, haz clic en "Datasets" en el menú de la izquierda y haz clic en el botón "+ Create dataset" para crear un conjunto de datos. Elige la opción "From local files" y selecciona el conjunto de datos de Kaggle que descargamos anteriormente.

   ![24](../../../../translated_images/dataset-1.e86ab4e10907a6e9c2a72577b51db35f13689cb33702337b8b7032f2ef76dac2.es.png)

2. Asigna un nombre, un tipo y una descripción a tu conjunto de datos. Haz clic en Next. Sube los datos desde los archivos. Haz clic en Next.

   ![25](../../../../translated_images/dataset-2.f58de1c435d5bf9ccb16ccc5f5d4380eb2b50affca85cfbf4f97562bdab99f77.es.png)

3. En el esquema, cambia el tipo de datos a Boolean para las siguientes características: anaemia, diabetes, high blood pressure, sex, smoking y DEATH_EVENT. Haz clic en Next y luego en Create.

   ![26](../../../../translated_images/dataset-3.58db8c0eb783e89236a02bbce5bb4ba808d081a87d994d5284b1ae59928c95bf.es.png)

¡Perfecto! Ahora que el conjunto de datos está listo y el clúster de cómputo está creado, podemos comenzar el entrenamiento del modelo.

### 2.4 Entrenamiento con poco o ningún código usando AutoML

El desarrollo tradicional de modelos de aprendizaje automático consume muchos recursos, requiere un conocimiento significativo del dominio y tiempo para producir y comparar docenas de modelos.  
El aprendizaje automático automatizado (AutoML) es el proceso de automatizar las tareas iterativas y que consumen tiempo del desarrollo de modelos de aprendizaje automático. Permite a científicos de datos, analistas y desarrolladores construir modelos de ML con gran escala, eficiencia y productividad, manteniendo la calidad del modelo. Reduce el tiempo necesario para obtener modelos de ML listos para producción, con gran facilidad y eficiencia. [Más información](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

1. En el [espacio de trabajo de Azure ML](https://ml.azure.com/) que creamos anteriormente, haz clic en "Automated ML" en el menú de la izquierda y selecciona el conjunto de datos que acabas de cargar. Haz clic en Next.

   ![27](../../../../translated_images/aml-1.67281a85d3a1e2f34eb367b2d0f74e1039d13396e510f363cd8766632106d1ec.es.png)

2. Introduce un nuevo nombre para el experimento, la columna objetivo (DEATH_EVENT) y el clúster de cómputo que creamos. Haz clic en Next.

   ![28](../../../../translated_images/aml-2.c9fb9cffb39ccbbe21ab9810ae937195d41a489744e15cff2b8477ed4dcae1ec.es.png)

3. Elige "Classification" y haz clic en Finish. Este paso puede tardar entre 30 minutos y 1 hora, dependiendo del tamaño de tu clúster de cómputo.

   ![30](../../../../translated_images/aml-3.a7952e4295f38cc6cdb0c7ed6dc71ea756b7fb5697ec126bc1220f87c5fa9231.es.png)

4. Una vez que la ejecución esté completa, haz clic en la pestaña "Automated ML", selecciona tu ejecución y haz clic en el algoritmo en la tarjeta "Best model summary".

   ![31](../../../../translated_images/aml-4.7a627e09cb6f16d0aa246059d9faee3d1725cc4258d0c8df15e801f73afc7e2c.es.png)

Aquí puedes ver una descripción detallada del mejor modelo que AutoML generó. También puedes explorar otros modelos generados en la pestaña Models. Tómate unos minutos para explorar los modelos en el botón Explanations (vista previa). Una vez que hayas elegido el modelo que deseas usar (aquí elegiremos el mejor modelo seleccionado por AutoML), veremos cómo podemos implementarlo.

## 3. Implementación del modelo con poco o ningún código y consumo del endpoint
### 3.1 Implementación del modelo

La interfaz de aprendizaje automático automatizado te permite implementar el mejor modelo como un servicio web en unos pocos pasos. La implementación es la integración del modelo para que pueda hacer predicciones basadas en nuevos datos e identificar posibles áreas de oportunidad. Para este proyecto, la implementación como un servicio web significa que las aplicaciones médicas podrán consumir el modelo para hacer predicciones en vivo sobre el riesgo de ataque cardíaco de sus pacientes.

En la descripción del mejor modelo, haz clic en el botón "Deploy".

![deploy-1](../../../../translated_images/deploy-1.ddad725acadc84e34553c3d09e727160faeb32527a9fb8b904c0f99235a34bb6.es.png)

15. Asigna un nombre, una descripción, el tipo de cómputo (Azure Container Instance), habilita la autenticación y haz clic en Deploy. Este paso puede tardar unos 20 minutos en completarse. El proceso de implementación incluye varios pasos, como registrar el modelo, generar recursos y configurarlos para el servicio web. Aparecerá un mensaje de estado bajo Deploy status. Selecciona Refresh periódicamente para verificar el estado de la implementación. Estará implementado y en ejecución cuando el estado sea "Healthy".

![deploy-2](../../../../translated_images/deploy-2.94dbb13f239086473aa4bf814342fd40483d136849b080f02bafbb995383940e.es.png)

16. Una vez implementado, haz clic en la pestaña Endpoint y selecciona el endpoint que acabas de implementar. Aquí puedes encontrar todos los detalles que necesitas saber sobre el endpoint.

![deploy-3](../../../../translated_images/deploy-3.fecefef070e8ef3b28e802326d107f61ac4e672d20bf82d05f78d025f9e6c611.es.png)

¡Increíble! Ahora que tenemos un modelo implementado, podemos comenzar a consumir el endpoint.

### 3.2 Consumo del endpoint

Haz clic en la pestaña "Consume". Aquí puedes encontrar el endpoint REST y un script de Python en la opción de consumo. Tómate un momento para leer el código de Python.

Este script se puede ejecutar directamente desde tu máquina local y consumirá tu endpoint.

![35](../../../../translated_images/consumption-1.700abd196452842a020c7d745908637a6e4c5c50494ad1217be80e283e0de154.es.png)

Tómate un momento para revisar estas 2 líneas de código:

```python
url = 'http://98e3715f-xxxx-xxxx-xxxx-9ec22d57b796.centralus.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
```  
La variable `url` es el endpoint REST que se encuentra en la pestaña de consumo y la variable `api_key` es la clave primaria que también se encuentra en la pestaña de consumo (solo en caso de que hayas habilitado la autenticación). Así es como el script puede consumir el endpoint.

18. Al ejecutar el script, deberías ver el siguiente resultado:  
    ```python
    b'"{\\"result\\": [true]}"'
    ```  
Esto significa que la predicción de insuficiencia cardíaca para los datos proporcionados es verdadera. Esto tiene sentido porque si observas más de cerca los datos generados automáticamente en el script, todo está en 0 y falso por defecto. Puedes cambiar los datos con la siguiente muestra de entrada:

```python
data = {
    "data":
    [
        {
            'age': "0",
            'anaemia': "false",
            'creatinine_phosphokinase': "0",
            'diabetes': "false",
            'ejection_fraction': "0",
            'high_blood_pressure': "false",
            'platelets': "0",
            'serum_creatinine': "0",
            'serum_sodium': "0",
            'sex': "false",
            'smoking': "false",
            'time': "0",
        },
        {
            'age': "60",
            'anaemia': "false",
            'creatinine_phosphokinase': "500",
            'diabetes': "false",
            'ejection_fraction': "38",
            'high_blood_pressure': "false",
            'platelets': "260000",
            'serum_creatinine': "1.40",
            'serum_sodium': "137",
            'sex': "false",
            'smoking': "false",
            'time': "130",
        },
    ],
}
```  
El script debería devolver:  
    ```python
    b'"{\\"result\\": [true, false]}"'
    ```  

¡Felicidades! Acabas de consumir el modelo implementado y entrenado en Azure ML.

> **_NOTA:_** Una vez que termines el proyecto, no olvides eliminar todos los recursos.

## 🚀 Desafío

Observa detenidamente las explicaciones y detalles del modelo que AutoML generó para los mejores modelos. Intenta entender por qué el mejor modelo es mejor que los otros. ¿Qué algoritmos se compararon? ¿Cuáles son las diferencias entre ellos? ¿Por qué el mejor modelo tiene un mejor rendimiento en este caso?

## [Cuestionario posterior a la lección](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/35)

## Revisión y autoestudio

En esta lección, aprendiste cómo entrenar, implementar y consumir un modelo para predecir el riesgo de insuficiencia cardíaca de manera sencilla, sin necesidad de mucho código, en la nube. Si aún no lo has hecho, profundiza en las explicaciones del modelo que AutoML generó para los mejores modelos e intenta entender por qué el mejor modelo es mejor que los demás.

Puedes profundizar más en AutoML con poco o ningún código leyendo esta [documentación](https://docs.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

## Tarea

[Proyecto de Ciencia de Datos con poco o ningún código en Azure ML](assignment.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.