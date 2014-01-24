MUNICIPALIDAD DE HEREDIA
Acuerdo tomado en la Sesión Extraordinaria N° doscientos ochenta y dos-dos mil trece, celebrada por la Municipalidad del Cantón Central de Heredia, el día jueves 10 de octubre del dos mil trece:
“GUÍA METODOLÓGICA DE DESARROLLO
DE SISTEMAS DE INFORMACIÓN”
Introducción
El desempeño de las instituciones, involucra necesariamente la tecnología, herramientas ya sea de hardware o software con las que se busca proporcionar mejores servicios al usuario final.
Para desarrollar proyectos grandes y complejos es necesario seguir una metodología. Si un proyecto involucra más de tres personas, nos sería útil para una buena comunicación y buen desempeño a lo largo de todo el proyecto.
Una metodología de desarrollo de software es un proceso organizado para la producción de software, que especifica el ciclo de vida a utilizar, indicando además qué personas deben desempeñar cada rol en el desarrollo de las actividades.
El modelo de ciclo de vida para el desarrollo de software, nos dice el orden en que se realizaran las diferentes etapas (espiral/cascada) y lo que hay que obtener en cada una de ellas a lo largo del desarrollo del proyecto.
Un proceso de desarrollo de software es un conjunto de actividades necesarias para transformar los requerimientos del usuario en un sistema software.
Una etapa son los diferentes pasos a seguir durante el desarrollo del software. Determinado orden de estos pasos se los conoce como ciclo de vida. Ejemplo captura de requerimientos, análisis del problema, diseño, implementación, testing, mantenimiento.
Un rol, es el papel que debe desempeñar una persona en el desarrollo del software, como por ejemplo analista, diseñador, programador, tester, etc.
Un modelo/diagrama, es un lenguaje visual que se aplica en cada etapa del ciclo de vida. Permite para visualizar, especificar, construir y documentar.
El tipo de metodología va a depender del sistema que se quiere implementar; existen distintas metodologías que fueron surgiendo de acuerdo a la evolución de los lenguajes de programación, actualmente, aspectos como el aumento de rendimiento, escalabilidad y reducción de costos en los sistemas de información, ha llevado a utilizar las mejores prácticas en mercado de desarrollo, como la programación orientada a objetos OBJETOS (UML/RUP, Unified Modeling Language/ Rational Unified Process)
Dentro de las características de las metodologías orientadas a objetos, se tiene:
➢ Énfasis en la abstracción de datos.
➢ Funciones y datos encapsulados en entidades fuertemente relacionadas.
➢ Facilidades de mantenimiento y extensión.
➢ Mapeo directo a entidades del mundo real.
Qué es UML
UML es un lenguaje de modelado estándar para escribir planos de software.
Puede utilizarse para visualizar, especificar, construir y documentar los artefactos de un sistema con gran cantidad de software.
Proporciona un conjunto de diagramas que me permite modelar los diferentes aspectos del sistema y su principal objetivo es la comunicación de información.
Características principales:
• Es independiente del proceso, aunque para utilizarlo óptimamente se debería usar en un proceso que fuese dirigido por los casos de uso, centrado en la arquitectura, iterativo e incremental.
• El vocabulario y las reglas de un lenguaje como UML indican cómo crear y leer modelos bien formados, pero no dice que modelos se deben crear ni cuando se deberían crear. Esta tarea corresponde al proceso de desarrollo del software.
• Detrás de cada símbolo en la notación de UML hay una semántica bien definida, de esta manera un desarrollador puede escribir un modelo en UML, y otro desarrollador o incluso otra herramienta, puede interpretar ese modelo sin ambigüedad.
• UML está pensado principalmente para sistemas con gran cantidad de software.
• No está limitado al modelado de software.
Diagramas soportados por UML:
Dinámica / comportamental | Estructural
Diagrama de Casos de Uso | Diagrama de Clases
Diagrama de Actividades | Diagrama de Objetos
Diagrama de Transición de Estados | Diagrama de Componentes
Diagramas de Interacción D. de Colaboración D. de Secuencia | Diagrama de Despliegue
ü Diagrama de Casos de Uso: son importantes para visualizar, especificar y documentar el comportamiento de un sistema, un subsistema o una clase. Modela las necesidades a satisfacer y los límites del sistema.
ü Diagrama de Actividades: es un tipo especial de diagrama de transición de estados que muestra el flujo de actividades que se tiene que desarrollar dentro de un sistema para un fin “X”.
ü Diagrama de Transición de Estados: muestra una máquina de estados que consta de estados, eventos, transiciones y actividades. Son especialmente importantes en el modelado del comportamiento de una interfaz, una clase o una colaboración.
o Un estado es una situación durante la vida de un objeto.
o Un evento es un estímulo que provoca un cambio de estados.
o Una actividad es una ejecución computacional no atómica.
o Una acción es una ejecución computacional atómica.
ü Diagrama de Interacción: es un diagrama que muestra una interacción entre objetos que se mandan mensajes y sus relaciones.
ü Diagrama de Colaboración: es un tipo de diagrama de Interacción que resalta la organización estructural de los objetos que envían y reciben mensajes.
ü Diagrama de Secuencia: es un tipo de diagrama de Interacción que resalta el orden temporal de los mensajes enviados entre los distintos objetos.
ü Diagrama de Clases: muestra un conjunto de clases colaboración e interfaces así también como sus relaciones. Son los más utilizados en sistemas orientados a objetos y son la base para los diagramas de objetos, componentes y de despliegue. Representan elementos lógicos de un sistema.
ü Diagrama de Objetos: muestra un conjunto de objetos y sus relaciones.
ü Representan una instancia del diagrama de clases. Es sacarle una foto al sistema en tiempo de ejecución.
ü Diagrama de Componentes: Muestra la organización y dependencia de un conjunto de componentes. Modela los aspectos físicos de los sistemas orientados a objetos esto implica ejecutables, bibliotecas, tablas, archivos, documentos, etc.
ü Diagrama de Despliegue: muestra la configuración de nodos de procesamiento en tiempo de ejecución y los componentes que residen en ellos. Modela la topología del hardware en la que se ejecuta el sistema.
[imagen]
Figura 1 Mapeo de la herencia de diagramas soportados por UML
La visualización, especificación, construcción y documentación de un sistema con gran cantidad de software requiere que el sistema sea visto desde varias perspectivas.
La arquitectura de un sistema es quizás el artefacto más importante que puede emplearse para manejar estos diferentes puntos de vista y controlar el desarrollo iterativo e incremental de un sistema a lo largo de su ciclo de vida.
La arquitectura de un sistema con gran cantidad de software puede describirse mejor a través de cinco vistas interrelacionadas. Cada vista es una proyección de la organización y la estructura del sistema, centrada en un aspecto particular de ese sistema.
- Vista de Casos de Uso: Describe el comportamiento del sistema tal y como es percibido por los usuarios finales.
- Vista de Diseño: Soporta principalmente los requerimientos funcionales del sistema.
- Vista de Procesos: Comprende principalmente el funcionamiento, capacidad de crecimiento y rendimiento del sistema.
- Vista de Implementación: Se preocupa de los componentes y archivos que deben ensamblarse para producir un sistema en ejecución.
- Vista de Despliegue: Se preocupa de la distribución, entrega e instalación de las partes que constituyen el sistema físico.
Cada una de estas 5 vistas puede existir por sí mismas, de forma que diferentes usuarios puedan centrarse en las cuestiones de la arquitectura del sistema que más les interesen.
[imagen] [imagen]
Ciclo de vida
Se llama Ciclo de Vida al lapso de tiempo que se requiere para obtener una o varias piezas de software, ya sea que se trate de una aplicación tradicional, uno o varios componentes que no interactúan con el usuario, una aplicación Web o un sitio Web (portal).
RUP es un proceso de desarrollo de software y junto con el Lenguaje Unificado de Modelado (UML), constituye la metodología estándar más utilizada para el análisis, implementación y documentación de sistemas orientados a objetos.
RUP soporta diagramas UML para validar y verificar los sistemas que se estén desarrollando. Se caracteriza por ser iterativo e incremental, estar centrado en la arquitectura y guiado por los casos de uso. Incluye artefactos (que son los productos tangibles del proceso como por ejemplo, el modelo de casos de uso, el código fuente, etc.) y roles (papel que desempeña una persona en un determinado momento, una persona puede desempeñar distintos roles a lo largo del proceso).
Entre sus características principales, están:
- Forma disciplinada de asignar tareas y responsabilidades (quién hace, qué, cuándo y cómo).
- Pretende implementar las mejores prácticas en Ingeniería de Software.
- Desarrollo iterativo e incremental.
- Administración de requisitos.
- Uso de arquitectura basada en componentes.
- Control de cambios.
- Modelado visual del software.
- Verificación de la calidad del software.
- Diseñado para ser flexible y extensible.
El ciclo de vida RUP es una implementación del Desarrollo en espiral. Fue creado ensamblando los elementos en secuencias semiordenadas. El ciclo de vida organiza las tareas en fases e iteraciones. El ciclo que da origen a la primera versión se denomina Ciclo Inicial, las versiones que siguen a continuación se obtienen en los denominados Ciclos de Evolución.
Los ciclos de vida, también llamados proyectos, son dirigidos desde 2 perspectivas:
• Dirección o Administración, que atiende los aspectos financieros, estratégicos y humanos.
• Técnica: que atiende los aspectos como la calidad, la ingeniería y los métodos y técnicas de diseño y desarrollo.
Desde el punto de vista de administración, el ciclo de vida del desarrollo de software se organiza en 4 fases, las cuales indican el progreso del proyecto:
• Concepción. Donde se define el alcance del proyecto, se especifica la visión del producto final y se define el caso de negocios.
• Elaboración. Donde se realiza el planeamiento de las actividades, los recursos requeridos, y la especificación de las características y el diseño de la arquitectura.
• Construcción. Donde se construye el producto, evoluciona de la visión, la arquitectura y los planes hasta que el producto esté listo para transferir a sus usuarios.
• Transición. Donde se realiza la instalación del producto, entrenamiento, apoyo y mantenimiento hasta que los usuarios queden satisfechos.
[imagen]
Desde una perspectiva de alto nivel, el proceso se descompone en 2 dimensiones:
Ø El eje horizontal o Dimensión Dinámica, representa los aspectos dinámicos del proceso: el horizonte de tiempo del ciclo de vida, y se expresa en términos de Fases, Iteraciones e Hitos (el Cuando Temporal).
Ø El eje vertical o Dimensión Estática, representa los aspectos estáticos del proceso llamados también componentes, y se expresa en términos de Actividades, Artefactos y Trabajadores (tiene que ver con el Cómo, Qué y Quién). A su vez las actividades se organizan en Flujos de Trabajo o Workflows (el Cuando atemporal).
A menos que la producción de software se detenga, el producto puede evolucionar dentro del siguiente ciclo de generación de software (Evolución), donde se repite la misma secuencia de fases pero con énfasis en otros aspectos tales como los cambios en la arquitectura del software, el nuevo esquema de base de datos o el impacto de los nuevos requerimientos.
[imagen]
En la práctica los ciclos se pueden superponer, las primeras fases de un ciclo pueden comenzar mucho antes que las últimas del anterior. En algunos casos las iteraciones pueden ejecutarse en paralelo. Desde la perspectiva Técnica, el desarrollo de software es visto como una sucesión de iteraciones a través de las cuales el software producido evoluciona por incrementos. Cada iteración es concluida por la liberación de un producto ejecutable, el cual puede ser un subconjunto de la visión global, útil desde el punto de vista del ingeniero o del usuario.
De esta manera, las dos perspectivas se reconcilian al final de cada fase, mientras que se sincronizan al final de cada iteración. En otras palabras cada fase se descompone en una o más iteraciones.
[imagen]
Porqué UML, porque RUP ¿?
En principio sería útil aclarar que UML y RUP son dos cosas distintas. Mientras que UML es sólo un lenguaje visual y de modelado, RUP es un proceso de desarrollo de software.
RUP se basa en el desarrollo iterativo e incremental. Y este proceso es relativamente complicado si no lleva una adecuada documentación. Para hacer más fácil el trabajo, dividen a las actividades en disciplinas y dentro de éstas proponen el uso de modelos. Cada disciplina atacará cierta actividad o tarea desde un punto de vista.
Es aquí donde entra UML. Como UML ofrece un amplio conjunto de diagramas para representar las ideas desde diferentes, y complementarios, punto de vista, RUP aprovecha esta ventaja y adoptan a UML como una herramienta más para realizar, diseñar y documentar el desarrollo de sistemas.
En síntesis, RUP propone usar UML para llevar la documentación del sistema, facilitar la etapa del diseño y posterior construcción o desarrollo, transmitir ideas y ayudar al equipo a comunicarlas.
Ahora bien, UML tiene mayor sentido cuando se está hablando de un análisis, diseño y programación bajo el paradigma OO (Orientado a Objetos), aunque uno puede, si así lo desea, extrapolar el concepto de un diagrama para transmitir una idea fuera del paradigma OO. Como por ej., el diagrama de actividad que en ocasiones se lo emplea para representar el flujo de información y los procesos de un área o departamento de una empresa.
Recordar que como proceso, RUP no impone el uso del paradigma de programación. Si bien el concepto UP nació para facilitar los proyectos que hacían uso de la orientación a objetos, nada impide seguir otro paradigma. Los modelos o procesos de desarrollo sólo se limitan a ofrecer un marco de trabajo y una forma de estructurar las actividades.
1. Fases
Se entiende por Fase al lapso de tiempo que existe entre dos hitos. Durante el transcurso de la misma, se alcanza un conjunto de objetivos bien definidos, se completan artefactos y se toman decisiones acerca de avanzar o no a la siguiente fase.
Las fases no son idénticas en términos de tiempo y esfuerzo, pueden variar considerablemente de un proyecto a otro, de acuerdo a sus discriminantes.
2. FASE DE CONCEPTUALIZACIÓN O INICIO
En esta fase se conceptualiza el desarrollo del proyecto de desarrollo. En esta fase se establece los casos del negocio para un producto nuevo, se especifica el alcance del producto y lo transforma en un proyecto concreto. A continuación se hace la especificación de las principales tareas que involucra esta fase.
[imagen]
Solicitud del sistema: donde se expresa la necesidad, los beneficios, y la justificación de desarrollar un nuevo sistema de información incluyendo la información que sea solicitada ante las jefaturas o comité de aprobación para este tipo de solicitud.
Informe de Diagnóstico: donde se especifican los resultados de la valoración efectuada sobre la solicitud señalando las posibilidades de solución para la realización del sistema, mediante el desarrollo de casos de negocio, se expresan las diferentes aristas para dar solución a la necesidad expresa en la solicitud realizada.
Selección de solución: Basados en la información recolectada en el informe de diagnóstico, se cuenta con datos con los que, junto con las expectativas del negocio y su valoración en riesgos, el comité directivo se seleccionará la alternativa que mejor se acople a la situación, pudiendo ser tomada alguna de las siguientes:
▪ Seleccionar alguna de las alternativas recomendadas
▪ Posponer el proyecto para un momento más oportuno, esto de acuerdo con los intereses y prioridades de la Institución
▪ Cancelar el proyecto ya que el mismo no es viable desde el punto de vista operativo, económico o técnico o porque las prioridades Institucionales así lo requieren.
Gestión de Desarrollo del Proyecto: De ser seleccionada una de las alternativas propuestas, se procede con la planificación del desarrollo de proyecto.
El resultado principal es la decisión de seguir o no seguir con la siguiente fase e invertir tiempo y dinero en analizar en detalle que es lo que será construido, cómo y qué tan factible es, para ello, el Administrador del Proyecto, en coordinación con el Líder Administrativo del Proyecto y todo el Equipo de Trabajo debe iniciar la planificación y documentación de todas las actividades del Proyecto de Desarrollo de Software, en lo que será la concepción del Plan de Proyecto. (Ver Plantillas y artefactos/01_Ejemplo de Plan de Proyecto) .
Toda fase posee un conjunto de criterios de entrada y otros de salida, los primeros son necesidades expresadas de alguna forma y los segundos son el resultado que se debe obtener:
[imagen]
2.1. UN CASO DE NEGOCIO
El desarrollo del caso de negocio consiste en ocho pasos, los cuales hacen alusión a procedimientos que deben estar definidos por la propia entidad, como lo es la evaluación de riesgos, o los análisis financieros, sin embargo se pueden ver detalles de los mismos en el documento completo de ISACA, Val IT: casos de negocio, la siguiente ilustración menciona dichos pasos:
[imagen]
2.2. ELABORACIÓN DEL DOCUMENTO DE ADMINISTRACIÓN DE RIESGOS.
Dentro del informe de diagnóstico en el desarrollo del caso de negocio, se identificaron riesgos, los cuales se consideran insumos, para elaborar un documento más detallado de la administración de éstos y otros riesgos. En el caso específico de la Institución se cuenta con el formato llamado Matrices SEVRI, entonces debe referirse a ellos para la documentación de éste ítem. (Ver Plantillas y artefactos/Matrices SEVRI.xlsx)
Para esto, el Líder Técnico conjuntamente con el Líder de Proyecto o contraparte asignada deberá hacer un análisis de riesgos del proyecto basándose en cuatro aspectos fundamentales:
a) Tamaño y complejidad: Lo cual tiene una estrecha relación entre el tiempo y costo asociado al proyecto.
b) Tipo de tecnología: Experiencia anterior con el tipo de tecnología a utilizar y el tipo de sistema.
c) Grado de estructuración: Definición y variabilidad de los procesos y del equipo de trabajo.
d) Grado de impacto: A mayor impacto y cobertura (departamental, institucional u organizacional) mayor riesgo debido a que implica un alto grado de coordinación y comunicación
2.3. ADMINISTRACIÓN DE LA CONFIGURACIÓN
En el desarrollo de la documentación del proyecto en desarrollo, debe implementar actividades para asegurar la actualización de la documentación así como la configuración de los artefactos.
Los cambios técnicos en cuanto a modificación y suma de requerimientos deben contar con la aprobación de los integrantes del equipo técnico, mediante el procedimiento usual de aprobación de requerimientos nuevos.
Adicionalmente, se debe contemplar la naturaleza de la tecnología en que se basa el desarrollo, pues deben tenerse en cuenta las implicaciones de dependencia por obsolescencia, soporte o licenciamiento del mismo.
2.4. MODELADO DEL NEGOCIO
Para poder extraer lo que el cliente desea como parte de la solución, es necesario tener un entendimiento del proceso de negocio y del negocio en sí en el que se desenvolverá el sistema a desarrollar. Esto permitirá reconocer y documentar los procesos del negocio involucrados, y elaborar una propuesta de mejora a estos procesos. De ser necesario, los procesos pueden ser redefinidos. Esta etapa consta de dos fases:
• Documentación de los procesos actuales del negocio, en este aspecto puede utilizarse más de un documento o dependiendo de la complejidad o cantidad de procesos del proyecto.
• Propuesta de mejora del negocio: Debe seguirse la misma estrategia del punto anterior con la misma plantilla, identificando las mejoras inducidas al negocio.
Para el modelado de negocio, se recomienda el uso del lenguaje unificado de modelado o UML, ya que permite de una manera gráfica perfilar las iteraciones y características entre los diferentes actores de un caso de uso que son bastante intuitivas para personas con perfil no técnico.
2.5. IDENTIFICACIÓN DE REQUERIMIENTOS
En esta fase se debe realizar un análisis a partir de la documentación de los procesos actuales para identificar necesidades y características que serán descritas en el documento de Visión, que una vez finalizado será insumo para identificar los casos de uso del sistema y su diagrama.
Todo cambio en requerimientos debe ser administrado a través del Procedimiento de Administración de cambios a requerimientos.
[imagen]
Las principales Actividades involucradas en la Captura de Requerimientos son: Identificar Actores y Casos de Uso; Priorizar los Casos de Uso; Detallar Casos de Uso; Prototipar la Interfaz con el Usuario y Estructurar el Modelo de Casos de Uso.
2.6. CIERRE DE LA FASE DE CONCEPTUALIZACIÓN
La fase de conceptualización debe ser formalizada mediante una o varias presentaciones con los respectivos resúmenes de los artefactos generados.
Adicionalmente, debe gestionarse en esta oportunidad el recibo conforme del documento de especificación de requerimientos, por parte del usuario patrocinador y los usuarios expertos.
3. FASE DE ELABORACIÓN
La fase de elaboración tiene como objetivo analizar el problema en mayor detalle para definir y estabilizar la arquitectura del sistema de información, así como la especificación de casos de uso identificados durante la fase de conceptualización.
3.1. PLANIFICACIÓN DE LA FASE DE ELABORACIÓN
Se pretende esbozar la cantidad y contenido de las iteraciones y realizar una primera planificación, actualizando Plan de Proyecto (Ver Plantillas y artefactos/02_Ejemplo de Plan de iteracion), se debe tomar en cuenta los casos de uso identificados en la fase anterior de tal forma que los de mayor complejidad, riesgo y prioridad sean abordados en las primeras iteraciones.
En esta etapa se construye un prototipo arquitectónico ejecutable (viable) en una o más iteraciones, dependiendo del alcance, tamaño, riesgo y novedad del proyecto, partiendo y limitándose (no-mandatario) a los casos de uso principales identificados en la fase de Concepción.
[imagen]
Al final de esta fase hay otra vez una decisión de seguir o no seguir, para invertir en construir el producto internamente u ofrecer el desarrollo completo a un contratista. Los planes producidos deben ser lo suficientemente detallados como para mitigar los riesgos que permitan determinar los costos y la programación del desarrollo completo.
3.2. ESPECIFICACIÓN DE CASOS DE USO
Para especificar cada caso de uso, se utiliza la plantilla de Especificación de Caso de Uso (ver Plantillas y artefactos/03_Ejemplo_Rup_Especificaciones_CU), cuyo propósito es describir paso a paso la interacción de los actores con el sistema.
3.3. DISEÑO DE PROTOTIPO DE INTERFAZ DE USUARIO
Una vez especificados los casos de uso se puede realizar un diseño no funcional de las interfaces (o pantallas) con las que interactuará el usuario con la aplicación. Esta actividad adelanta el proceso de construcción del proyecto con respecto a lo esperado por el usuario.
3.4. MODELO DE ANÁLISIS Y DISEÑO DE ARQUITECTURA
La finalidad es estabilizar una arquitectura la cual sea suficientemente sólida para ello es necesario definir el diagrama de clases, secuencia, componentes, estados e implementación, así como el modelo de base de datos.
[imagen]
Durante esta actividad es de gran importancia referirse al catálogo de componentes y servicios de software institucionales, con el objetivo de no duplicar esfuerzos en la programación reutilizando los servicios requeridos, logrando además el desarrollo de la aplicación con el paradigma SOA (arquitectura orientada a servicios).
[imagen] erios de Entrada
[imagen]
Figura: 6 Las principales Actividades involucradas en el Diseño
3.5. CIERRE DE LA FASE DE ELABORACIÓN
Se debe formalizar el cierre de esta fase, mediante una presentación con el resumen de los artefactos generados al grupo de trabajo así como los usuarios expertos.
4. FASE DE CONSTRUCCIÓN
Esta fase por lo general se divide en varias iteraciones, partiendo de los lineamientos de base de la arquitectura y evolucionando en pasos o incrementos hasta llegar al producto final. Los artefactos preparados en las fases previas son revisados y expandidos estabilizándose conforme avanza la construcción del sistema. También se producen nuevos artefactos además del software en sí mismo: documentación interna, documentación para usuarios y pruebas. Por cada iteración se tiene:
Criterios de Entrada
[imagen]
Hacia el fin de esta fase, artefactos y criterios de salida adicionales deben ser producidos para la última iteración, para ello debe haber un plan de entrega que contiene:
P Soporte.
P Entrenamiento.
P Estrategia de transición.
P Producción de medios a replicar (manuales, CDs).
P Documentación para el usuario.
4.1. PLANIFICACIÓN DE LA FASE DE CONSTRUCCIÓN
Se pretende esbozar la cantidad y contenido de las iteraciones y realizar la planificación, actualizando el Plan de Proyecto (ver plantillas y artefactos/02_Ejemplo de Plan de iteracion). Para esto se tiene como insumo las especificaciones de casos de uso (tomando en cuenta prioridad funcional para el usuario) y el documento de arquitectura de software (tomando en cuenta la complejidad de los diagramas desarrollados).
Además como parte de esta actividad debemos crear un plan de pruebas, que será ejecutado por cada módulo culminado en el proyecto en sus respectivas iteraciones. Para esta tarea utilizar la plantilla Plan de pruebas (ver Plantillas y artefactos/04_Ejemplo de Plan de pruebas).*
4.2. CONFIGURACIÓN EQUIPOS E INSTALACIÓN DE HERRAMIENTAS
Se debe implementar las actividades para lograr un adecuado Control de Versiones y Administración de Cambios, para que cada uno de los miembros del equipo de trabajo cuente con los recursos tecnológicos y las herramientas para el desarrollo de las distintas tareas a desarrollar durante la Fase de Construcción. Es importante que el equipo de trabajo cuente con los mecanismos de comunicación e integración, de tal forma que el esfuerzo colectivo sea eficiente y eficaz.( repositorio virtual)
Se debe contar con los protocolos para registrar, extraer, modificar y publicar los artefactos construidos, según se establece en el Plan de Control de Versiones y Control de Cambios. En esta actividad se deben implementar los siguientes ambientes de trabajo:
• Ambiente de desarrollo: donde se realiza la ejecución del desarrollo de código fuente para la herramienta, pruebas unitarias e integrales.
• Ambiente de pruebas: consiste en un ambiente donde se realizan las pruebas funcionales con los encargados de la ejecución de pruebas para el proyecto, así como con los usuarios finales responsables del proceso de validación de la herramienta.
4.3. CONSTRUCCIÓN DE COMPONENTES
4.4.
En esta etapa, se debe comprobar la funcionalidad de cada uno de los componentes establecidos en fase de Análisis y Diseño, evidenciando su funcionalidad al integrarse a la solución completa.
Se espera además, obtener los siguientes entregables:
o Código fuente: el cual debe respetar los estándares definidos por el área de Desarrollo de sistemas. (como por ejemplo nomenclatura y documentación para los componentes, procedimientos de integración, interfaces de usuario, etc.)
o Scripts
o Lista de chequeo para la revisión de entrega de los componentes aprobados y entregados.
o Sistema de documentación y ayuda en línea.
o Manual de usuario
En esta fase es posible, tener que actualizar documentación del proyecto, como lo son:
o Documentación de especificación de casos de uso.
o Documentación de arquitectura de software y los modelos dependientes de este documento.
o Lista de Riesgos.
o Plan de pruebas.
[imagen]
4.5. TRANSFERENCIA TECNOLÓGICA
Esta etapa, tiene la tarea de entregar mediante documentación electrónica o física, y/o mediante sesiones de trabajo, todo el conocimiento técnico adquirido por los desarrolladores, a los encargados de dar el mantenimiento a la aplicación. Es recomendable repetir esta actividad en cada iteración de esta fase.
Esta actividad debe incluir, incluir todos los datos de conocimientos de cada uno de los productos desarrollados, es decir acerca de:
• Documento de Arquitectura de Software,
• Documentación Técnica de Bases de Datos,
• Herramientas de desarrollo y plataforma tecnológica.
• Proceso de configuración y parametrización de la aplicación
• Mantenimiento básico del software,
• Migración de Datos
• Procesos de respaldo de la base de datos,
• Restauración de los respaldos
• Solución a problemas básicos en caso de fallo.
4.6. EJECUCIÓN DE PLAN DE PRUEBAS
Se debe contar con un ambiente de Desarrollo de Pruebas, para probar los paquetes de instalación que generados a partir de n componentes que han sido aprobados para prueba. Para estos efectos se debe trasladar el código del ambiente de desarrollo al ambiente de pruebas y ejecutar el Plan de Pruebas (ver Plantillas y artefactos/04_Ejemplo de Plan de pruebas).* en lo que se refiere a pruebas de funcionalidad (casos de uso), pruebas de seguridad, pruebas de configuración.
Cada conjunto de pruebas se realiza con un juego diferentes de datos y bajo la responsabilidad de distintas personas o funciones.
Posteriormente el probador completará el apartado del documento de Plan de pruebas en cuanto a la documentación de resultados.
• Se deben establecer los mecanismos para llevar registro y seguimiento de resolución de defectos, errores o cambios.
• Se debe realizar la aprobación de pruebas según la naturaleza de la
o pruebas funcionales de casos de uso (usuarios finales),
o pruebas de seguridad y configuración (arquitecto) de ambiente para la operación del sistema.
o Esta aprobación se llevará a cabo con la plantilla de aprobación de artefacto.
Al finalizar cada iteración se deben realizar pruebas integrales entre los módulos desarrollados, así como las interfaces que existan con otros sistemas
[imagen]
4.7. CIERRE DE FASE DE CONSTRUCCIÓN
Esta fase se debe formalizar con una o varias presentaciones con su respectivo resumen de los artefactos generados.
5. FASE DE TRANSICIÓN
La fase de transición es la fase donde el producto es puesto en las manos de los usuarios e involucra actividades de instalación, configuración, soporte a la comunidad de usuarios y correcciones, si hicieran falta.
La fase termina cuando el usuario se encuentra satisfecho con el producto. Debe existir una aceptación formal. En este punto algunas de las valoraciones acumuladas durante el proyecto pueden ser reutilizadas en el próximo ciclo o en otro proyecto. Se debe tener especial cuidado en las versiones, tanto de las aplicaciones como del software de soporte, así como la documentación.
Antes de iniciar el Plan piloto deben estar construidos los manuales del Sistema o la ayuda en línea, junto con el material de la capacitación al usuario y los técnicos que se encargarán del soporte y mantenimiento del software.
[imagen]
5.1. PLANIFICACIÓN DE LA FASE DE TRANSICIÓN
Se pretende esbozar la cantidad y contenido de las iteraciones y actualizar el Plan de Proyecto (Ver plantillas y artefactos/ 01_Ejemplo de Plan de Proyecto).Generalmente se realiza una iteración para la creación de documentos y capacitación y una segunda iteración para la ejecución del plan piloto.
5.2. TRANSFERENCIA TECNOLÓGICA DE PUESTA EN PRODUCCIÓN
Esta actividad pretende transferir conocimientos sobre aspectos de configuración, administración y funcionamiento de la aplicación a los funcionarios que tienen la responsabilidad de mantener operando el sistema.
Se debe entregar el manual de instalación y configuración para crear el ambiente de producción al personal encargado de mantener en operación el sistema, así como el manual de usuario.
Se debe implementar un Plan de Capacitación para Usuarios finales: se convoca a los usuarios líderes que serán capacitados, los cuales a su vez deberán capacitar al resto de usuarios involucrados. Además se entrega la documentación pertinente (manual de usuario), la cual será guía de referencia para la capacitación del sistema.
5.3. EJECUCIÓN DEL PLAN PILOTO
Consiste en operar el software desarrollado, por espacio de un tiempo limitado, en un ambiente controlado y una carga de datos establecida, en el ambiente de los usuarios.
Además, se efectúa una revisión y evaluación de los resultados obtenidos para establecer la entrada o no a Producción del Sistema Implementado y el descontinuar la operación del sistema actual de información (en caso de que exista). De ser necesario se solventan problemas de capacitación, ajustes en la documentación, scripts de instalación y otros artefactos.
6. PROCESO DE CIERRE DEL PROYECTO
Al terminar la Fase de Transición, el software o sistema de información está listo como versión oficial en producción. Está instalada y liberada oficialmente en el Ambiente de Producción.
De existir una metodología de Administración de proyectos, debería seguirse los lineamientos que esta indique.
Glosario:
Artefacto: Los artefactos son piezas de información que se producen, modifican o utilizan a lo largo de todo el ciclo de vida, algunos tienen mayor preponderancia al inicio, otros al final. Su característica común es que:
P Son productos tangibles (un plan, un documento de requisitos, un modelo gráfico, una porción de código).
P Son la materia prima y la salida de las actividades.
P Se realiza un estricto control de versiones sobre ellos.
P En conjunto forman los Entregables.
Dado que el proceso no está conducido o basado en documentos, la documentación debe permanecer limitada a pocos documentos pero que aporten un valor real al proyecto tanto desde el punto de vista de dirección como del punto de vista técnico. Por eso existen una serie de documentos típicos que no deben faltar:
Meta o Hito (Milestone): Identifica dentro del plan de un proyecto, un instante en el cual se hará una revisión del estado del producto con respecto al plan. Debe existir un entregable que será utilizado para verificar que la meta haya sido alcanzada. Puede ser en general interpretado como punto de control.
Prototipo: Una versión, la cual no está sujeta a cambios de dirección o control de configuraciones.
