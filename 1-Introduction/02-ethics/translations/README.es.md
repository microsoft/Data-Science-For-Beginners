# Introducción a la ética de datos

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Ética para ciencia de datos - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

---

Todos somos ciudadanos de datos viviendo en un gobernado por datos.

Las tendencias de mercado nos dicen que para 2022, 1 de cada 3 grandes organizaciones comprará y venderá sus datos en línea a través de [mercados e intercambios](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Como **desarrolladores de Apps**, lo encontraremos más fácil y barato que integrar conocimientos dirigidos por datos y automatización dirigida por algoritmos en las experiencias de usuario del día a día. Pero como la AI se vuelve cada vez más presente, necesitarempos entender lso daños potenciales causados por el [armamentismo](https://www.youtube.com/watch?v=TQHs8SA1qpk) de dichos algoritmos a escala.

Las tendencias también indican que crearemos y consumiremos más de [180 zettabytes](https://www.statista.com/statistics/871513/worldwide-data-created/) de datos para el 2025. Como **científicos de datos**, esto nos da niveles de acceso sin precedentes a datos personales. Esto significa que podemos construir perfiles conductuales de usuarios e influenciar en la toma de decisiones en formas que crea una [ilusión de libre elección](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) mientras empuja a los usuarios hacia los resultados que preferimos. También plantea preguntas más amplias respecto a la privacidad de datos y protección de los usuarios.

La ética de datos son _barreras de seguridad necesarias_ para la ciencia de datos e ingeniería, ayudándonos a minimizar daños potenciales y consecuencias no deseadas de nuestras acciones dirigidas por datos. El [Hype Cycle de Gartner para AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifica tendencias relevantes en ética digital, AI responsable, y gobernanza de AI como factores clave para mega-tendencias mayores alrededor de la _democratización_ e _industrialización_ de la AI.

![Hype Cycle de Gartner para AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

En esta lección, exploraremos la fascinante área de la ética de datos - desde los conceptos clave y desafíos, hasta los casos de estudio y conceptos de AI aplicados como gobernanza - que ayuda a establecer una cultura de ética en equipos y organizaciones que trabajan con datos y AI.




## [Examen previo a la lección](https://red-water-0103e7a0f.azurestaticapps.net/quiz/2) 🎯

## Definiciones básicas

Empecemos entendiendo la terminología básica.

La palabra "ética" proviene de la [palabra griega "ethikos"](https://en.wikipedia.org/wiki/Ethics) (y su raíz "ethos") lo cual significa _carácter o naturaleza moral_. 

La **ética** se trata de valores compartidos y principios morales que gobiernan nuestro comportamiento en sociedad. La ética se basa no en leyes sino en normas más ampliamente aceptadas de lo que es "correcto vs lo incorrecto". Sin embargo, las consideraciones éticas pueden influenciar iniciativas de gobernanza corporativa y regulaciones de gobernanza que crean más incentivos para el cumplimiento.

La **ética de datos** es una [nueva rama de la ética](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) que "estudia y evalua problemas morales relacionados a _datos, algoritmos y prácticas correspondientes_"- Aquí, los **"datos"** se centran en acciones relacionadas a la generación, grabación, curación, procesamiento de difusión, intercambio y uso de **"algoritmos"** centrados en AI, agentes, aprendizaje automático, y robots, así como **"prácticas"** enfocadas en temas como inovación responsable, programación, hackeo y códigos de ética.

**Ética aplicada** es la [aplicación práctica de consideraciones morales](https://en.wikipedia.org/wiki/Applied_ethics). Es el proceso de investigar activamente cuestiones éticas en el contexto de _acciones del mundo real, productos y procesos_, y tomar medidas correctivas para hacer que estos se alinean con nuestros valores éticos definidos.

**Cultura ética** trata de [_operacionalizar_ la ética aplicada](https://hbr.org/2019/05/how-to-design-an-ethical-organization) para confirmar que nuestros principios éticos y prácticas son adoptados de forma consistente y escalable a través de toda la organización. Una cultura ética exitosa define principios éticos a nivel organización, provee incentivos significativos para el cumplimiento y refuerza las normas éticas alentando y amplificando los comportamientos deseados en cada nivel de la organización.


## Conceptos éticos

En esta sección, duscutiremos conceptos como **valores compartidos** (principios) y **retos éticos** (problemas) para la ética de datos - y explora **casos de estudio** que te ayudan a entender estos conceptos en el contexto del mundo real.

### 1. Principios éticos

Cada estrategia de ética de datos comienza por la definición de _principios éticos_ - los "valores compartidos" que describen los comportamientos aceptables, y guían acciones de conformidad, en nuestros proyectos de datos y AI. Puedes definir estos a nivel individual o de equipo. Sin embargo, la mayoría de las grandes organizaciones describen estos en una misión _ética de AI_ o marco de trabajo que es definido a niveles corporativos y refuerza consistentement a través de todos los equipos.

**Ejemplo:** La misión [responsable de AI](https://www.microsoft.com/en-us/ai/responsible-ai) de Microsoft se lee: _"Estamos comprometidos al avance de principios éticos dirigidos por AI que anteponen primero a la gente"_ - identificando 6 principios éticos en el marco de trabajo descrito a continuación:

![AI responsable en Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Exploremos brevemente estos principios. La _transparencia_ y _responsabilidad_ son los valores fundamentales sobre los que se cimientan otros principios - iniciemos aquí:

* [**Responsabilidad**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) hace a los practicantes _responsables_ por sus datos y operaciones de AI, en cumplimiento con estos principios éticos.
* [**Transparencia**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) asegura que los datos y acciones de AI sean _entendibles_ (interpretables) para los usuarios, explicando el qué y el porqué detrás de las decisiones.
* [**Justicia**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - se centra en asegurar que la AI trata a _todas las personas_ justamente, dirigiendo cualquier sesgo sistémico o social-ético implícito in datos y sistemas.
* [**Fiabilidad y seguridad**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - asegura que la AI se comporta _consistentemente_ con los valores definidos, minimizando daños potenciales o consecuencias no intencionadas.
* [**Privacidad & seguridad**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - se trata del entendimiento del linaje de datos, y provee _privacidad de datos y protecciones relacionadas_ a los usuarios.

* [**Inclusión**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - trata del diseño de soluciones AI con la intención, adaptándolas para reunir un _amplio rango de necesidades humanas_ y capacidades.

> 🚨 Piensa cual podría ser tu misión de ética de datos. Explorar marcos de trabajo éticos de AI de otras organizaciones - aquí tienes ejemplos de [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) , y[Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). ¿Qué valores compartidos tienen en común? ¿Cómo se relacionan estos principios al producto de AI o industria en la cual operan?

### 2. Desafíos éticos

Una vez que tenemos pricipios éticos definidos, el siguiente paos es evaluar nuestros datos y acciones AI para ver si estos se alinean con los valores compartidos. Piensa en tus acciones en 2 categorías: _recolección de datos_ y _diseño de algoritmos_.

Con la recolección de datos, las acciones probablemente involucren **datos personales** o información de identificación personal (PII) para individuos vivos identificables. Esto incluye [diversos artículos de datos no personales](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) que _colectivamente_ identifican a un individuo. Los desafíos éticos pueden relacionarse con _privacidad de datos_, _propiedad de los datos_, y temas relacionados como _consentimiento informado_ y _derechos de propiedad intelectual_ para los usuarios.

Con el diseño de algoritmo, las acciones involucran la recolección y curación de **conjuntos de datos**, luego usarlos para entrenar y desplegar **modelos de datos** que predicen resultados o automatizan decisiones en contexto del mundo real. Los desafíos éticos pueden surgir de _conjuntos de datos sesgados_, problemas con la _calidad de los datos_, _injusticia_, y _malinterpretación_ in los algoritmo - incluyendo algunos problemas que son sistémicos por naturaleza.

En ambos casos, los desafíos éticos destacan áreas donde nuestas acciones pueden encontrar conflictos con nuestros valores compartidos. Para detectar, mitigar, minimizar, o eliminar estas preocupaciones - necesitamos realizar preguntas morales de "sí/no" relacionadas a nuestas acciones, luego tomar acciones correctivas según sea necesario. Demos un vistazo a algunos desafíos éticos y las preguntas morales que plantean:


#### 2.1 Propiedad de los datos

La recolección de datos suele involucrar datos que pueden identificar los sujetos de datos. La [propiedad de los datos](https://permission.io/blog/data-ownership) trata del _control_ y [_derechos de usuario_](https://permission.io/blog/data-ownership) relacionados a la creación, procesamiento y dispersión de los datos.

Las preguntas morales que debemos hacer son:
 * ¿Quién posea los datos? (usuario u organización)
 * ¿Qué derechos tienen los sujetos de datos? (ejemplo: acceso, eliminación, portabilidad)
 * ¿Qué derechos tienen las organizaciones? (ejemplo: rectificar revisiones de usuarios maliciosos)

#### 2.2 Consentimiento informado

[Consentimiento informado](https://legaldictionary.net/informed-consent/) define el acto de los usuarios al aceptar una acción (como la recolección de datos) con un _completo entendimiento_ de hechos relevantes incluyendo el propósito, riesgos potenciales y alternativas.

Las preguntas a explorar son:
 * ¿El usuario (sujeto de datos) otorgó el permiso para el uso y cpatura de datos?
 * ¿El usuario entendió el propósito para el cual los datos fueron capturados?
 * ¿EL usuario entendió los riesgos potenciales de su participación?

#### 2.3 Propiedad intelectual

La [propiedad intelectual](https://en.wikipedia.org/wiki/Intellectual_property) se refiere a creaciones intangibles resultado de la iniciativa humana, que puede _tener valor económico_ para individuos o negocios.

Las preguntas a explorar son:
 * ¿Los datos recolectados tiene valor económico para un usuario o negocio?
 * ¿El **usuario** tiene propiedad intelectual en este ámbito?
 * ¿La **organización** tiene propiedad intelectual en este ámbito?
 * Si estos derechos existen, ¿cómo los protegemos?

#### 2.4 Privacidad de datos

La [privacidad de datos](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) o privacidad de la información se refiere a la preservación de la privacidad del usuario y la protección de la identidad del usuario respecto a información de identificación personal.

Las preguntas a explorar son:
 * ¿Están los datos (personales) de los usuarios seguros contra hackeos y filtraciones?
 * ¿Están los datos de usuario accesibles sólo para usuarios y contextos autorizados?
 * ¿Se preserva el anonimato de los usuarios cuando los datos son compartidos o esparcidos?
 * ¿Puede un usuario ser desidentificado de conuntos de datos anonimizados?


#### 2.5 Derecho al olvido

El [derecho al olvido](https://en.wikipedia.org/wiki/Right_to_be_forgotten) o [derecho a la eliminación](https://www.gdpreu.org/right-to-be-forgotten/) provee protección adicional a datos personales de los usuarios. Especialmente, brinda a los usuarios el derecho a solicitar la eliminación o remoción de datos personales de búsquedas de internet y otras ubicaciones, _bajo circunstancias específicas_ - permitiéndoles un nuevo comienzo en línea sin las acciones pasadas siendo retenidas contra él.

Las preguntas a explorar son:
 * ¿El sistema permite a los sujetos de datos solicitar eliminación?
 * ¿La remoción del consentimiento del usuario debería disparar la eliminación automatizada?
 * ¿Se recolectaron los datos sin consentimiento o por medios no legítimos?
 * ¿Estamos de acuerdo con las regulaciones de gobierno para la privacidad de los datos?


#### 2.6 Sesgo del conjunto de datos

Un conjunto de datos o [sesgo de recopilación](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) pretende seleccionar un subconjunto _no representativo_ de datos para el desarrollo de un algorítmo, creando una potencial injusticia en los resultados para distintos grupos. Los tipos de sesgos incluyen selección o muestreo de sesgo, sesgo voluntario y sesgo de instrumento.

Las preguntas a explorar son:
 * ¿Reclutamos un conjunto representativo de sujetos de datos?
 * ¿Probamos nuestros conjuntos de datos recoletados o curados para distintos sesgos?
 * ¿Podemos mitigar o eliminar los sesgos descubiertos?

#### 2.7 Calidad de los datos

[La calidad de los datos](https://lakefs.io/data-quality-testing/) se enfoca en la validez de los conjuntos de datos curados que se usan para desarrollar nuestros algoritmos, comprobando si las características y registros cumplen los requerimientos para el nivel de precisión necesario para nuestros propósitos de AI.

Las preguntas a explorar son:
 * ¿Capturamos _características_ válidas para nuestro caso de uso?
 * ¿Los datos fueron capturados _consistentemente_ a través de las distintas fuentes de datos?
 * ¿Están _completos_ los conjuntos de datos para las distintas condiciones o escenarios?
 * ¿La información es capturada de forma _precisa_ reflejando la realidad?

#### 2.8 Justicia del algoritmo

[La justicia del algoritmo](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) verifica que el diseño del algoritmo discrimina sistemáticamente contra subgrupos específicos de sujetos de datos que conlleven a [daños potenciales](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) en _asignación_, (donde los recursos son negados o retenidos para ese grupo) y _calidad del servicio_ (donde la AI no es tan precisa para algunos subgrupos como lo es para otros).

Las preguntas a explorar son:
 * ¿Evaluamos la precisión del modelo para distintos subgrupos y condiciones?
 * ¿Escrutinamos el sistema buscando daños potenciales (por ejemplo, estereotipos?
 * ¿Podemos revisar los datos o retener re-entrenar modelos para mitigar daños potenciales?

Explora recursos como [Listas de comprogación de justicia de AI](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) para aprender más.

#### 2.9 Malinterpretación

[La malinterpretación de datos](https://www.sciencedirect.com/topics/computer-science/misrepresentation) trata de preguntarse si estamos comunicando ideas honestamente de los datos reportados en una forma engañosa para soportar la narrativa deseada.

Las preguntas a explorar son:
 * ¿Estamos reportando datos incompletos o inexactos?
 * ¿Estamos visualizando los datos de tal forma conllevan a conclusiones engañosas?
 * ¿Estamos usando técnicas estadísticas selectivas para manipular los resultados?
 * ¿Existen explicaciones alternativas par pueden ofrecer una conclusión distinta?

#### 2.10 Libertad de elección
La [ilusión de libertad de elección](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) ocurre cuando un sistema "elige arquitecturas" usando algoritmos de toma de decisiones para empujar a la gente hacia la elección de un resultado preferido mientras aparenta darles opciones y control. Estos [patrones obscuros](https://www.darkpatterns.org/) pueden causar daño social y económico a los usuarios. Ya que las decisiones del usuario impactan en los perfiles de comportamiento, estas acciones dirigen potencialmente a futuras elecciones que pueden amplificar y extender el impacto de estos daños.

Las preguntas a explorar son:
 * ¿El usuario entendió las implicaciones de realizar dicha elección?
 * ¿El usuario estaba conciente de las opciones (alternativas) y los pros y contrar de cada una?
 * ¿El usuario puede revertir una elección influenciada o automatizada posteriormente?

### 3. Casos de estudio

Para poner estos desafíos éticos en contexto del mundo real, ayuda ver casos de estudio que destacan el daño potencial y las consecuencias a individuos y sociedad, cuando dichas violaciones éticas son pasadas por alto.

Aquí hay algunos ejemplos:

| Desafío de ética | Caso de estudio  | 
|--- |--- |
| **Consentimiento informado** | 1972 - [Estudio de sífilis Tuskegee](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - A los hombres afroamericanos que participaron en el estudio le fue prometido tratamiento médico gratuito _pero fueron engañados_ por los investigadores quienes fallaron al informar a los sujetos en sus diagnósticos o en la disponibilidad del tratamiento. Muchos sujetos murieron y los compañeros o hijos fueron afectados; el estudio duró 40 años. | 
| **Privacidad de los datos** |  2007 - El [premio de datos de Netflix](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) otorgó a investigadores con _10M de clasificaciones anóminas de 50K clientes_ para ayudar a mejorar los algoritmos de recomendación. Sin embargo, los investigadores fueron capaces de correlacionar datos anónimos con datos personalmente identificables en _conjuntos de datos externos_ (por ejemplo, comentarios en IMDb) - efectivamente "des-anonimizando" a algunos subscriptores de Netflix.|
| **Sesgo de colección**  | 2013 - La ciudad de Boston [desarrolló Street Bump](https://www.boston.gov/transportation/street-bump), una app que permite a los ciudadanos reportar baches, dando a la ciudad mejores datos de la carretera para encontrar y reparar desperfectos. Sin embargo, [la gente en los grupos con menores ingresos tuvieron menos acceso a autos y teléfonos](https://hbr.org/2013/04/the-hidden-biases-in-big-data), haciendo sus problemas de carretera invisibles para la app. Los desarrolladores trabajaron en conjunto con académicos para cambiar _el acceso equitativo y brecha digital_ y así fuese más justo. |
| **Justicia de algoritmos**  | 2018 - El [estudio de tonos de género](http://gendershades.org/overview.html) del MIT evaluó la precisión de productos de clasificación de género , exponiendo brechas en la precisión para mujeres y personas de color. Una [tarjeta 2019 de Apple](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) parecía ofrecer menos crédit a mujeres que a hombres. Ambos ilustraron problemas en sesgos de algoritmos llevando a daños socio-económicos.
| **Malinterpretación de datos** | 2020 - El [departamento de salud pública de Georgia liberó gráficos de COVID-19](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) que parecían malinformar a los ciudadanos acerca de las tendencias en los casos confirmados sin orden cronológico en el eje x. Esto ilustra la malinterpretación a través de visualizaciones engañosas. |
| **Ilusión de libertad de elección** | 2020 - La aplicación de aprendizaje [ABCmouse pagó $10M para asentar una queja FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) donde los padres fueron engañados para pagar subscripciones que no podían cancelar. Esto ilustra los patrones obscuros en arquitecturas de elección, donde los usuarios fueron empujados hacia elecciones potencialmente dañinas. |
| **Privacidad de los datos y derechos de usuario** | 2021 - La [infracción de datos](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) de Facebook expuso datos de 530M de usuarios, resultando en un acuerdo de $5B para la FTC. Sin embargo, esto rechazó notificar a los usuarios de la brecha violando los derechos de usuarios alrededor de la transparencia y acceso de datos. |

¿Quieres explorar más casos de estudio? Revisa los siguientes recursos:
* [Ética desenvuelta](https://ethicsunwrapped.utexas.edu/case-studies) - dilemas éticos en diversas industrias.
* [Curso de ética en ciencia de datos](https://www.coursera.org/learn/data-science-ethics#syllabus) - referencía los casos de estudio explorados.
* [Donde las cosas han ido mal](https://deon.drivendata.org/examples/) - lista de comprobación de deon con ejemplos

> 🚨 Piensa en los casos de estudio que has visto - ¿has experimentado o sido afectado por un desafío ético similar en tu vida? ¿Puedes pensar en al menos otro caso de estudio que ilustre uno de los desafíos éticos que discutimos en esta sección?

## Ética aplicada

Hemos hablado de conceptos éticos, desafíos y casos de estudio en contextos del mundo real. Pero ¿cómo podemos _aplicar_ los principios éticos y prácticas en nuestros proyectos? y ¿cómo _aplicamos_ estas prácticas para una mejor gobernanza? Exploremos algunas soluciones del mundo real:

### 1. Códigos profesionales

Los códigos profesionales ofrecen una opción para que las organizaciones "incentiven" a los miembros a apoyar sus principios éticos y su misión. Los códigos son _guías morales_ para el comportamiento profesional, que ayudan a los empleados o miembros a tomar decisiones que se alinea con sus principios de organización. Estas son tan buenas como el cumplimiento voluntario de los miembros; sin embargo, muchas organizaciones ofrecen incentivos adicionales y penalizaciones para motivar el cumplimiento de los miembros.

Los ejemplos incluyen:

 * Código de ética de [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/)
 * Código de conducta  de la [Asociación de ciencia de datos](http://datascienceassn.org/code-of-conduct.html) (creado en 2013)
 * [Código de ética y conducta profesional de ACM](https://www.acm.org/code-of-ethics) (desde 1993)

> 🚨 ¿Perteneces a una organización profesional de ingeniería o ciencia de datos? Explora su sitio para ver si definen un código de ética profesional. ¿Qué te dice acerca de sus principios éticos? ¿Cómo "incentivan" a los miembros para que sigan el código?

### 2. Listas de comprobación de ética

Mientras los códigos profesionales defiene los _comportamientos éticos_ requerido por sus practicantes, estos tienen [limitaciones conocidas](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) en su aplicación, particularmente en proyectos a gran escala. En su lugar, muchos expertos en ciencia de datos [abogan por listas de comprobación](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), que pueden **conectar principios a prácticas** en formas más determinísticas y accionables.

Las listas de comprobación convierten preguntas en tareas de "sí/no" que pueden ser operadas, permitiendo darles seguimiento como parte de flujos de trabajo de liberación de productos estándar.

Los ejemplos incluyen:
 * [Deon](https://deon.drivendata.org/) - una lista de comprobación de ética de datos de propósito general creada a partir de [recomendaciones de la industria](https://deon.drivendata.org/#checklist-citations) con una herramienta de línea de comandos para su fácil integración.
 * [Lista de comprobación de auditoría de privacidad](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - provee orientación general para prácticas de manejo de la información desde perspectivas legales y sociales.
 * [Lista de comprobación de justicia de AI](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - creada por practicantes de AI para soportar la adopción e integración de controles justos en los ciclos de desarrollo de AI.
 * [22 preguntas para ética en datos y AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - marcos de trabajo más abiertos, estructurados para la exploración inicial de problemas éticos en contextos de diseño, implementación y organización.

### 3. Regulaciones éticas

La ética trata de definir valores compartidos y hacer lo correcto _voluntariamente_. El **cumplimiento** trata de _seguir la ley_ donde se define. La **gobernanza** cubre ampliamente todas las formas en las cuales las organizaciones operan para hacer cumplir los principios éticos y seguir las leyes establecidas.

Hoy en día, la gobernanza toma dos formas dentro de la organización. Primero, define los principios **éticos de AI** y establece prácticas para promover la adopción en todos los proyectos relacionados a AI en la organización. Segundo, trata de cumplir con todoso los mandatos de gobierno en **regulaciones de protección de datos** para las regiones en las cuales opera.

Ejemplos de protección de datos y regulaciones de privacidad:

 * `1974`, [Ley de privacidad de EE.UU.](https://www.justice.gov/opcl/privacy-act-1974) - regula al  _gobierno federal_ la recolección, uso y divulgación de información personal.
 * `1996`, [Ley de responsabilidad y portabilidad de seguro de salud de EE.UU. (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - protege los datos de salud personales.
 * `1998`, [Ley de protección de la privacidad en línea para niños de EE.UU. (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - protege la privacidad de los datos para menores de 13 años.
 * `2018`, [Regulación de protección general de los datos (GDPR)](https://gdpr-info.eu/) - provee derechos de usuario, protección de datos y privacidad.
 * `2018`, [Ley de privacidad para los consumidores de California (CCPA)](https://www.oag.ca.gov/privacy/ccpa) da a los consumidores más _derechos_ sobre sus datos (personales).
 * `2021`, [Ley China de protección de la información personal](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) recién establecida, crea una de las regulaciones más grandes a nivel mundial respecto a privacidad de los datos.

> 🚨 La Unión Europea definió la GDPR (regulación general de protección de datos) quedando como una de las regulaciones a la privacidad de los datos más influyentes de hoy en día. ¿Sabías que también define [8 derechos de usuario](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) para la protección de la privacidad digital de los ciudadanos y datos personales? Aprende más acerca de qué son y porqué importan.


### 4. Cultura ética

Nota que existe una brecha intangible entre _cumplimiento_ (hacer suficiente para cumplir "lo designado por ley") y atender [problemas sistémicos](https://www.coursera.org/learn/data-science-ethics/home/week/4) (como la osificación, asimetría de la información e injusticia distribucional) que acelera el armamento de la AI.

Lo último requier [enfoques colaborativos para definir culturas de ética](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) que construyan conexiones emocionales y valores compartidos consistentes _a través de las organizaciones_ en la industria. Esto hace un llamado a [culturas de ética de datos más formalizadas](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) en las organizaciones - permitiendo a _cualquiera_ tirar del [cordón de Andon](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (para plantear cuestiones éticas desde el principio en el proceso) y hacer de las _evaluaciones éticas_ (por ejemplo, en la contratación) un criterio principal en la formación de equipos en proyectos de AI. 

---
## [Examen posterior a la lección](https://red-water-0103e7a0f.azurestaticapps.net/quiz/3) 🎯
## Revisión y auto-estudio

Los siguientes cursos y libros te facilitarán el entendimiento de conceptos éticos principales y desafíos, mientras que los casos de estudio y herramientas te ayudarán con las prácticas éticas aplicadas en contextos del mundo real. Aquí tienes algunos recursos con los que comenzar.

* [Aprendizaje automático para principiantes](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lecciones de justicia, de Microsoft.
* [Principios de AI responsable](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - ruta de aprendizaje gratuito de Microsoft Learn.
* [Ética y Ciencia de Datos](https://resources.oreilly.com/examples/0636920203964) - Libro electrónico de O'Reilly (M. Loukides, H. Mason et. al)
* [Ética de Ciencia de Datos](https://www.coursera.org/learn/data-science-ethics#syllabus) - curso en línea de la Universidad de Michigan.
* [Ética desenvuelta](https://ethicsunwrapped.utexas.edu/case-studies) - casos de estudio de la Universidad de Texas.

# Asignación 

[Escribe un caso de estudio de ética de datos](assignment.md)
