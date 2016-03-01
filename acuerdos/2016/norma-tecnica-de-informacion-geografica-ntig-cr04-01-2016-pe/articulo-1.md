REGISTRO NACIONAL
NTIG_CR04_01.2016: PERFIL OFICIAL DE MEDADATOS GEOGRÁFICOS DE COSTA RICA
VERSIÓN 1.1
[imagen]
Presentación
Tengo el agrado de presentar la Norma Técnica de Información Geográfica de Costa Rica (NTIG_CR04) denominada Perfil Oficial de Metadatos Geográficos de Costa Rica versión actualizada, la cual pretende plasmar los requerimientos de información sobre datos geográficos para la producción y publicación de información geoespacial en nuestro país.
Está alineado a los requerimientos del Sistema Nacional de Información Territorial (SNIT), así como a las consideraciones de orden técnico definidas por el Instituto Geográfico Nacional como elementos fundamentales.
Esperamos que el perfil oficial de metadatos sea un instrumento que permita la descripción de los datos, informe sobre su contenido, ofrezca al usuario la posibilidad de tener trazabilidad sobre su origen (fuentes, autor, etc.) y facilite la búsqueda de información geográfica de una forma rápida y eficaz.
Desde la perspectiva geográfica, ya sea con respecto a productores, gestores y/o usuarios de información geográfica, en la actualidad los metadatos se caracterizan por una conexión con los datos e información geoespacial, en alineamiento como parte de la normativa fundamental requerida dentro del contexto de una infraestructura de datos geoespaciales.
De esta manera, los metadatos son de gran importancia para las personas y organizaciones, tanto públicas como privadas, que utilizan y producen datos geoespaciales, para encontrar los datos que necesitan, determinar la mejor forma de utilizarlos y disponer de la herramienta adecuada para publicitarlos.
El Perfil Oficial de Metadatos Geográficos de Costa Rica tiene su origen en el ejercicio del cumplimiento de las competencias de Ley del Instituto Geográfico Nacional en materia de normalización, generación y estandarización de la información geoespacial. Esta primera versión es una iniciativa que nos facilitará el intercambio de informaciones interinstitucionales, además de promover de una manera precisa y ordenada la difusión y uso de los datos geográficos. Nuestra posición es inclusiva y abierta en cuanto a los aportes de la comunidad productora, gestora y usuaria de información geoespacial en el ámbito nacional.
Además, la definición y difusión de este documento está en concordancia con los lineamientos establecidos en el decreto N.° 37773-JP-H-MINAE-MICITT (La Gaceta N.° 134 del 12 julio de 2013), mediante el cual oficialmente se crea el Sistema Nacional de Información Territorial (SNIT) como instrumento para la producción, publicación, normativa y estandarización de la información geoespacial en nuestro país. A través del SNIT el IGN está promoviendo la generación de productos, servicios e información geográfica georreferenciada de cubrimiento nacional, regional y local, y la publicación en forma integrada y georreferenciada de información territorial producida por entes y órganos públicos, así como por personas físicas o jurídicas, y el homologar la información geoespacial estandarizada en el marco de una infraestructura de datos espaciales común.
El SNIT es un paso muy importante en el proceso de consolidación de la Infraestructura de Datos Espaciales de Costa Rica (IDECORI), que se define como el conjunto de políticas, organizaciones, estándares y tecnologías que trabajan de forma conjunta para producir, compartir y usar la información geográfica necesaria para apoyar el desarrollo del país en diversos ámbitos.
M.Sc. Max A. Lobo Hernández
Director
Instituto Geográfico Nacional
Registro Nacional
Índice de contenidos
1. Introducción………………………………………………………………………… …………….. 1
2. Antecedentes…… .............................................................................................................................. 1
3. Disposiciones generales .................................................................................................................... 2
3.1 Nomenclatura y nombre de la Norma Técnica: .................................................................... 2
3.2 Objeto:.………………………………………………………………………………………... 2
3.3 Ámbito de aplicación: ………………………………………………………………………. 2
3.4 Alcance: ………………………………………………………………………………………. 3
3.5 Aprobación técnica y oficialización: ………………………………………………………. 3
3.6 Obligatoriedad:………………………………………………………………………………. 3
3.7 Vigencia:………………………………………………………………………………………. 3
4. Clasificación de las variables del perfil…………………………………………………………. 3
5. Definiciones de los elementos presentes en el Perfil oficial de metadatos geográficos de Costa Rica .............................................................................................................................................. 4
5.1. Sección de identificación .......................................................................................................... 4
5.2. Sección de distribución........................................................................................................... 13
5.3. Sección de representación espacial ....................................................................................... 14
5.4. Sección del sistema de referencia .......................................................................................... 14
5.5. Sección de información sobre la calidad del dato .............................................................. 15
5.6. Sección de identificación del metadato ................................................................................ 17
6. Plantillas para metadatos geográficos ......................................................................................... 19
6.1 Plantilla para datos en formato raster ................................................................................... 20
6. 2 Plantilla para datos en formato vectorial ............................................................................. 24
7. Edición de metadatos con GeoNetwork como catálogo .............................................................. 25
8. Consideraciones finales ................................................................................................................. 32
9. Bibliografía ...................................................................................................................................... 33
Anexo ................................................................................................................................................... 34
Índice de figuras
Figura 1 Rectángulo geográfico envolvente .................................................................................... 12
Figura 2 Información de identificación ............................................................................................ 20
Figura 3 Punto de contacto ................................................................................................................ 21
Figura 4 Información de distribución ............................................................................................... 21
Figura 5 Información sobre representación espacial ...................................................................... 22
Figura 6 Información del sistema de referencia .............................................................................. 23
Figura 7 Información sobre calidad del dato ................................................................................... 23
Figura 8 Sección de identificación del metadato............................................................................. 24
Figura 9 Sección para crear el metadato .......................................................................................... 25
Figura 10 Selección de la plantilla de metadatos a utilizar ........................................................... 25
Figura 11 Edición de los metadatos .................................................................................................. 26
Figura 12 Ejemplo de consulta en el catálogo de metadatos ......................................................... 27
Figura 13 Visualización del metadato como resultado de la consulta en el catalogo ................ 28
Figura 14 Sección de identificación (MD)_Identificación) ............................................................. 29
Figura 15 Sección de distribución (MD_Distribución) ................................................................... 29
Figura 16 Sección de representación espacial _Representation) ................................................... 30
Figura 17 Sección del sistema de referencia (MD_Reference System) ........................................ 30
Figura 18 Sección de información sobre la calidad de dato (DQ_Data Quality) ........................ 30
Figura 19 Sección de identificación de metadato (MD_Metadata)............................................... 31
1. Introducción
Identificar la información espacial es un requisito básico para su consulta, búsqueda, definición de sus alcances y precisión. Asimismo, describir la información es un componente indispensable en la implementación de una infraestructura de datos espaciales (IDE). En esta, el componente para administrar los recursos que permiten identificar la información se define como catálogo de metadatos.
Este catálogo se debe construir conforme a normas y estándares, que establezcan la estructura para identificar la producción geoespacial y aseguren su interoperabilidad en términos de acceso, consulta, visualización y, en los casos en que se encuentre liberada, la descarga de la información.
Los metadatos son los recursos de información que describen las características de los datos presentes en un sistema. Su primera acepción fue la de “dato sobre el dato” o “información sobre los datos “. Actualmente, el enfoque también incluye información sobre el contexto, contenido y control de los datos, lo cual posibilita alcanzar objetivos como recuperar, filtrar e informar sobre licenciamiento, condiciones de uso, autentificación, evaluación, preservación e interoperabilidad (Caplan, 1995).
Un perfil de metadatos consiste en un conjunto particular de descriptores, adoptados por una determinada infraestructura de datos espaciales, según su ámbito de acción, para la documentación de productos y servicios. Diversos perfiles pueden diferir, tanto en la cantidad y el tipo de descriptores utilizados como en la forma de completar los campos. De una manera más simple, un perfil de metadatos es un subconjunto de elementos que describe la aplicación del estándar para una comunidad específica de usuarios.
2. Antecedentes
La producción de normas y estándares en el ámbito geoespacial en el ámbito internacional fue asumida por la Organización Internacional de Normalización (ISO), por medio del Comité ISO/TC 211 de Información Geográfica/Geomática, el cual inició sus trabajos en 1994 y produce normas de uso global desde el año 2000 (IPGH, 2010).
En el desarrollo del presente perfil de metadatos para Costa Rica, se utilizaron como base la norma ISO 19115:2003 Geographic Information Metadata, norma internacional en materia de metadatos para datos; y la personalización de esta norma para América Latina, denominada Perfil latinoamericano de metadatos (LAMP), el cual surge como una respuesta a la necesidad de obtener una estructura estandarizada para documentar la información geográfica de Latinoamérica y el Caribe.
A partir del año 2007, el Instituto Panamericano de Geografía e Historia (IPGH) y el Instituto Geográfico Agustín Codazzi (IGAC), junto a Global Spatial Data Infrastructure unieron esfuerzos para el desarrollo del perfil LAMP. Posteriormente, para el año 2011 presentan la propuesta de dicho perfil, con el objetivo fundamental de establecer un perfil de metadato geográfico e implementar un servicio de registro multilingüe, que cumpla los requisitos del estándar internacional ISO 19115, teniendo en cuenta los avances y las necesidades de los países de Latinoamérica y el Caribe.
En el desarrollo de soluciones para administrar metadatos, es indispensable mencionar el aporte de la Fundación Geoespacial de Recursos Abiertos (OSGeo). Es una organización internacional sin fines de lucro, cuya misión es apoyar el desarrollo colaborativo de software geoespacial de código abierto y promover su uso generalizado.
Uno de los proyectos desarrollados por la Fundación es el programa GeoNetwork, un sistema de gestión de información espacial que cumple los estándares de servicios webs para información geoespacial del Open Geospatial Consortium (OGC), dentro de los cuales se clasifica como un Catalogue Service Web (CSW). Así mismo, cumple los estándares establecidos por el Comité Técnico de la Información Geográfica Digital ISO/TC 211, entre los cuales se encuentran las normas antes mencionadas para metadatos.
En la elaboración de las diferentes plantillas, de acuerdo con el tipo de información espacial, que conforman el Perfil oficial de metadatos geográficos de Costa Rica, se usó el programa GeoNetwork. En la actualidad, este programa es una de las soluciones más utilizadas internacionalmente como catálogo de metadatos por diferentes infraestructuras de datos espaciales, como es el caso de España, Francia, Holanda, Ecuador y Chile, entre otros países.
Para el presente perfil, se elaboraron plantillas de metadatos para datos en formato raster y vectorial, según los estándares antes citados, con el objetivo de establecer y definir las variables requeridas para identificar información geoespacial básica en Costa Rica.
3. Disposiciones generales
3.1 Nomenclatura y nombre de la Norma Técnica:
NTIG_CR04_01.2016: Perfil Oficial de Metadatos Geográficos de Costa Rica
3.2 Objeto:
Plasmar los requerimientos de información sobre datos geográficos para la producción y publicación de información geoespacial en nuestro país, alineado a los requerimientos del Sistema Nacional de Información Territorial (SNIT), así como a las consideraciones de orden técnico definidas por el Instituto Geográfico Nacional como elementos fundamentales.
3.3 Ámbito de aplicación:
La presente Norma Técnica es de observancia obligatoria. La aplicación e interpretación de la presente Norma Técnica, para efectos administrativos y técnicos corresponderá al Instituto Geográfico Nacional, quien resolverá los casos no previstos por la misma y velara por su actualización conforme corresponda.
3.4 Alcance:
La Norma Técnica NTIG_CR04_01.2016: Perfil Oficial de Metadatos Geográficos de Costa Rica, constituye un marco de referencia de carácter general sobre los requisitos mínimos que deben observar los funcionarios y usuarios del Instituto Geográfico Nacional, y en general, el sector público (Poderes de la República, instituciones autónomas y semiautónomas, entes adscritos a instituciones autónomas, empresas públicas estatales, empresas públicas no estatales, entes públicos no estatales, entes administradores de fondos públicos, municipalidades y órganos municipales adscritos), sector privado, personas físicas y público en general, productor, gestor y usuario para la descripción de datos geográficos, informe sobre su contenido, ofrezca al usuario la posibilidad de tener trazabilidad sobre su origen (fuentes, autor, etc.) y facilite la búsqueda de información geográfica de una forma rápida y eficaz.
3.5 Aprobación técnica y oficialización:
La Norma Técnica de Información Geográfica denominada NTIG_CR04_01.2016:
Perfil Oficial de Metadatos Geográficos de Costa Rica, se aprobó técnicamente a las catorce horas con treinta minutos del día 12 de enero de 2016, conforme está registrado mediante el oficio N° DIG-0013-2016 de esa misma fecha, firmado por el MSc. Max A. Lobo Hernández, Director del Instituto Geográfico Nacional, y la misma queda oficializada a través de la publicación de la Directriz DIG-004 2016 del Instituto Geográfico Nacional del 12 de enero de 2016 en el Diario Oficial La Gaceta.
3.6 Obligatoriedad:
Las disposiciones contenidas en esta Directriz y respetiva Norma Técnica son de acatamiento obligatorio.
3.7 Vigencia:
La presente Norma Técnica rige a partir de la publicación de la Directriz DIG-004- 2016 del 12 de enero de 2016 en el Diario Oficial La Gaceta.
4. Clasificación de las variables del perfil
La siguiente clasificación de las variables se determinó considerando los requerimientos de producción de información geoespacial en nuestro país, y la necesidad de establecer una normativa alineada a los requerimientos del Sistema Nacional de Información Territorial (SNIT), así como a las consideraciones de orden técnico definidas por el Instituto Geográfico Nacional como elementos fundamentales que debe contener una infraestructura de datos espaciales de Costa Rica.
Las variables están agrupadas en tres categorías, con base en su importancia para la identificación, descripción y acceso de los datos. Obligatorio: El elemento del metadato geográfico debe estar presente, es decir, siempre debe incluirse.
[imagen]
Condicional: El elemento del metadato geográfico debe estar presente si se requiere por las
características del dato.
[imagen]
Opcional: El elemento del metadato geográfico puede estar o no presente, lo cual queda a
discreción del productor del conjunto de datos.
[imagen]
5. Definiciones de los elementos presentes en el Perfil oficial de metadatos geográficos de Costa Rica
El estándar ISO-19115 aporta la terminología necesaria para describir los datos geográficos; define los elementos de los metadatos, aporta un esquema o estructura a seguir y establece un conjunto de procedimientos. Es por tanto, la guía técnica que define y estructura las informaciones que se van a documentar acerca de los datos geográficos. La descripción de las diferentes secciones presentes en el Perfil oficial de metadatos geográficos para Costa Rica se describe a continuación:
5.1. Sección de identificación
Esta sección permite documentar la información básica para identificar un dato, un conjunto de datos o un servicio geográfico.
Título: Nombre otorgado y, por ende, con el cual se conoce al conjunto de datos que debe responder a las siguientes preguntas: ¿qué?, ¿dónde?, ¿quién?, ¿cuándo?
Este se creará teniendo en cuenta:
La temática de los datos
La serie y el número de hoja
La localización geográfica
El organismo productor
El año en que se creó
Título Alternativo: Es obligatorio y corresponde a un nombre en otro idioma, un nombre corto, o un acrónimo con que se identifica o se conoce al recurso o metadato generado, dos ejemplos utilizados por el IGN que ilustran lo anterior son: IGN_MTN25-San José para laHoja Topográfica San José a escala 1:25000 y IGN_DTA50 para la División Territorial Administrativa de Costa Rica. Se debe de tener en cuenta que la información geoespacial se actualiza a lo largo del tiempo, por lo tanto es indispensable el mantener invariable el texto en éste campo, independientemente del año de publicación, con el objetivo de relacionar las diferentes versiones a partir del metadato correspondiente.
Fecha: Es la fecha de referencia del recurso o conjunto de datos. El formato es: DD/MM/AAAA, y también se puede utilizar el ícono del calendario para seleccionar la fecha.
Tipo de fecha: Período de tiempo para el cual los datos tienen validez, es decir, el momento en que la representación descrita por el conjunto de datos es fiel reflejo del mundo real. La norma ISO 19115 contempla tres tipos de fecha que pueden documentarse:
Fecha de creación de los datos
Fecha de publicación de los datos
Fecha de revisión (mejorados o actualizados)
Se debe seleccionar y completar al menos uno de los tres tipos de fecha anteriores. Si no se conoce el día de creación, se completa la fecha con el día 1 del mes correspondiente; por ejemplo: 2012/11/01. Si no se conoce el día ni el mes, se debe completar la fecha con el día 1 del mes de enero del año de creación; por ejemplo: 01 /01/2012. El formato se representa de la siguiente manera: DD/MM/AAAA.
Edición: Si el recurso o el conjunto de datos se han creado por primera vez, será la primera edición. Si es posterior, por ejemplo para una hoja topográfica que se ha actualizado y, por ende, se le ha agregado información nueva, entonces será la segunda edición, y así sucesivamente.
Formato de presentación: Es la manera en que se muestra el dato. Dentro de este apartado, existen las siguientes opciones:
Digital | Impreso / Papel
Documento de texto digital Representación digital de un ítem, que en principio puede ser un documento de texto digital, pero que puede contener también ilustraciones. (Ejemplo: Word, Txt) Imagen digital Imagen análoga a cosas construidas por el | Copia impresa o documento impreso de documento de texto. Que puede además contener ilustraciones en papel, material fotográfico u otro soporte. Copia impresa de imagen Imagen semejante a cosas construidas por
[imagen]
Resumen: Es una breve síntesis descriptiva del contenido del recurso o dato y de sus características principales. Debe responder a las siguientes preguntas: ¿qué?, ¿quién?, ¿dónde?,¿cuándo?, ¿cómo? Por ejemplo, al crear un metadato para una hoja topográfica, se debe incluir lo siguiente:
Serie y número de hoja
Zona geográfica donde se ubica el conjunto de datos (provincia/ciudad)
Escala en que se encuentra
Duración o período temporal del contenido (inicio y fecha final o fecha única)
Organismo productor que lo ha realizado
Datos fuente a partir de los cuales se ha creado el recurso
Descripción general del contenido y de las entidades almacenadas
Formato de almacenamiento del conjunto de datos
Características especiales o limitaciones de los datos
Propósito: Es el motivo original de por qué se crearon los datos, o un resumen de las intenciones por las cuales se desarrolla el recurso y para qué se utilizarán los datos, como: fuente, apoyo o soporte que pueda brindar a otros datos geográficos con su creación. Un ejemplo de motivación válida sería: tener actualizada la cartografía básica nacional a esta escala.
Estado: Es el estado en que se encuentra el recurso o conjunto de datos. Se presentan las siguientes opciones:
► Completado o terminado completamente.
► Archivo histórico (el conjunto de datos tiene un valor histórico, por tratarse de una época antigua o pasada, por ejemplo, un mapa histórico. Además, los datos pueden estar almacenados dentro de la red).
► Obsoleto (por existir una nueva edición de los mapas más actualizada y, por lo tanto, los datos que se tienen no son muy relevantes).
► En curso (se actualizan continuamente).
► Planeado (existe una fecha programada para su actualización o creación).
► Requerido (los datos necesitan ser actualizados, aunque todavía no se ha establecido una fecha para ello).
► En desarrollo (los datos se están creando actualmente o se están actualizando).
Escala de los datos: Se refiere a la escala que está representado el recurso o dato geográfico, sin importar en que formato éste (raster o vector) el denominador de la escala se representará numéricamente; por ejemplo, 25000 para una escala 1: 25.000.
Frecuencia de actualización: Es la periodicidad con que se actualizan los datos y viene definida con las siguientes secuencias:
►Continuamente ►Mensualmente ► Según necesidad
►Diariamente ►Mensualmente ►Irregular (intervalos desiguales en duración)
►Semanalmente ►Bianualmente ►No programado (no planeado)
►Quincenalmente ►Anualmente ►Desconocida
Tipo de representación espacial: Es la identificación del tipo de método usado para la representación espacial de la información geográfica. Los valores posibles son:
Tipo de representación espacial
Vector: Se utilizan entidades vectoriales para representar los datos geográficos. | TIN: Es la representación de la realidad tridimensional mediante una red de triángulos irregulares.
Malla (raster): Se utiliza la estructura malla | Modelo estereoscópico: Es la visión
para representar los datos geográficos. Ejemplos: imágenes raster, imágenes satelitales, ortofotos, fotografías aéreas, imágenes de mapa raster. | tridimensional mediante la intersección de los rayos homólogos de un par de imágenes solapadas, como por ejemplo un par estereoscópico de ortofotos o imágenes satelitales.
Tabla de texto: Se utilizan datos de texto o tabulares para representar los datos geográficos. | Video: Se representa la información geográfica mediante escenas de una grabación o video.
Lenguaje: Es el idioma usado para documentar los metadatos. En nuestro caso, será el español. Existen varias opciones para escoger en el perfil. Si no aparece, en la opción Otro se especifica el lenguaje en que estará representado el conjunto de datos. Lenguaje de codificación del dato: Es el nombre completo de la codificación (nombre de la norma de codificación) para el conjunto de caracteres utilizado para los datos. Es una estandarización para que los lenguajes se puedan codificar para el uso informático. Los protocolos de Internet necesitan que se establezca una codificación para introducir los textos.
Dentro de este apartado hay varias opciones para escoger; los más comunes en el habla hispana son: el ISO-8859-1 (ISO/IEC 8859-1, Tecnologías de la Información-Conjuntos de caracteres gráficos codificados de 8-bit por byte-Parte 1: Alfabeto Latino No. 1) y el UTF-8 (Formato de Transferencia UCS de tamaño variable de 8-bit, basado en ISO/IEC 10646), pero se recomienda usar la codificación UTF-8, por codificar cualquier carácter y ser el valor predeterminado para el formato XML.
Palabras claves: Es la información sobre temas o fuentes relacionados con el conjunto de datos o frases formalizadas que se utilizan para describir un recurso o temática. Pueden utilizarse los nombres o la nomenclatura relevante presente en el recurso que se está metadateando. Las palabras claves pueden ser de varios tipos, pero para el IGN utilizaremos las referentes a:
►Palabras claves de tema: permiten incluir términos descriptivos adicionales para calificar la categoría del tema o materia particular. Ejemplos: agricultura, industria, hidrología, etc.
► Palabras claves de lugar: se utilizan para incluir referencias geográficas específicas: locales, regionales o nacionales cubiertos por el conjunto de datos o producto, como: nombre de cantón/distrito, ciudad o nombre de la provincia/nación, Ejemplos: Zapote, Curridabat, San José, Costa Rica, área metropolitana, etc.
Sin embargo, es importante mencionar que dentro del software de Geonetwork existen otras opciones, tales como:
► Palabras claves de tiempo o temporal: permiten el uso en los datos científicos e históricos e identifica un período relacionado con el conjunto de datos o producto. Por ejemplo: diurno, auge cafetalero, dinastía Ming, edad de la industrialización.
► Palabras claves de disciplina: identifica una rama de la instrucción o enseñanza específica.
► Palabras claves de estrato: identifica la capa de cualquier materia de los datos depositados. Restricciones de acceso: Son las condiciones de acceso que se aplican para garantizar la protección de privacidad o la propiedad intelectual, así como otras restricciones especiales o limitaciones para la obtención del recurso o conjunto de datos y/o servicios espaciales. Las limitaciones de acceso están compuestas por los siguientes elementos:
► Derechos de autor (copyright): Es el derecho exclusivo de publicación, producción o venta de los derechos de un trabajo literario, dramático, musical o artístico, o de uso de una marca comercial o etiqueta, garantizado por ley para un período específico de tiempo a un autor, compositor, artista o distribuidor.
► Patente: El Gobierno ha otorgado derecho exclusivo según la Ley de propiedad industrial a persona física o jurídica para fabricar, vender, usar o dar licencias, de una invención o descubrimiento.
► Pendiente de patentar: Información producida o vendida, que está en espera o pendiente de una patente.
► Otras restricciones: Otras limitaciones no listadas. En el caso de seleccionar esta opción, debe detallarse las mismas en el apartado al final de éste bloque, referido a Otras restricciones.
► Marca registrada: Nombre, símbolo u otro dispositivo de identificación del producto o servicio de su misma especie o clase en el mercado, registrado oficialmente y restringido legalmente para el uso exclusivo del propietario o fabricante.
► Licencia: Es el permiso formal que hace el titular para el uso o no uso de su producto o servicio.
► Derecho de propiedad intelectual: Derecho de beneficio financiero y de control de la distribución de una propiedad intangible, que es resultado de la creatividad, el cual está protegido por las leyes de la materia con respecto a su producto o servicio.
► Restringido: Limitado de la circulación o del acceso general.
Limitaciones de uso: Se refiere a las limitaciones que afectan el uso del recurso o conjunto de datos y/o servicios espaciales, que se aplican para garantizar la protección y privacidad o propiedad intelectual, así como otras restricciones especiales, limitaciones o seguridad. Las limitaciones de uso contemplan los siguientes elementos:
► Derechos de autor (copyright): Es el derecho exclusivo de publicación, producción o venta de los derechos de un trabajo literario, dramático, musical o artístico, o de uso de una marca comercial o etiqueta, garantizado por ley para un período específico de tiempo a un autor, compositor, artista o distribuidor.
► Patente: El Gobierno ha otorgado derecho exclusivo según la Ley de propiedad industrial a persona física o jurídica para fabricar, vender, usar o dar licencias, de una invención o descubrimiento.
► Pendiente de patentar: Información producida o vendida, que está en espera o pendiente de una patente.
► Otras restricciones: Otras limitaciones no listadas. En el caso de seleccionar esta opción, debe detallarse las mismas en el apartado al final de éste bloque, referido a Otras restricciones.
► Marca registrada: Nombre, símbolo u otro dispositivo de identificación del producto oservicio de su misma especie o clase en el mercado, registrado oficialmente y restringido legalmente para el uso exclusivo del propietario o fabricante.
► Licencia: Es el permiso formal que hace el titular para el uso o no uso de su producto oservicio.
► Derecho de propiedad intelectual: Derecho de beneficio financiero y de control de la distribución de una propiedad intangible, que es resultado de la creatividad, el cual está protegido por las leyes de la materia con respecto a su producto o servicio.
► Restringido: Limitado de la circulación o del acceso general.
Otras restricciones: Otras limitaciones, diferentes a acceso o uso.
Tema/Categoría: La norma ISO permite clasificar la temática del recurso catalogado utilizando diecinueve temas principales. Es un elemento muy importante de considerar, por cuanto una gran parte de las búsquedas de metadatos se realizan a partir de su temática, además de que el metadato puede estar dentro de varias categorías a la vez. Las categorías contempladas por ISO 19115 dentro del perfil son:
Categorías de temas según ISO 19115: 2003
01. Agricultura: Cría de animales y/o cultivos de plantas. Irrigación, agricultura, plantaciones, plagas y epidemias y enfermedades que afectan a las cosechas y al ganado.
02. Atmósfera climatológica y meteorológica: Procesos y fenómenos de la atmósfera. Cobertura nubosa, tiempo, clima, condiciones atmosféricas, cambio climático, precipitación.
03. Aguas interiores: Cuerpos de agua interior, sistema de drenaje y sus características. Ríos y glaciares, lagos de agua salada, planes de utilización de aguas, presas, corrientes, inundaciones, calidad de aguas, planes hidrológicos.
04. Biota: Flora y fauna en el medio natural. Vegetación, ciencias biológicas, ecología, vida salvaje, vida marina, pantanos.
05. Cobertura de la Tierra con mapas básicos e imágenes: Cartografía base, uso del suelo, mapas topográficos, imágenes, imágenes sin clasificar, anotaciones.
06. Economía: Actividades económicas, condiciones y empleo. Producción, trabajo, ingresos, comercio, industria, turismo, ecoturismo, silvicultura, políticas pesqueras, caza comercial y de subsistencia, exploración y explotación de recursos tales como minerales,
aceite y gas.
07. Elevación: Altura sobre y bajo el nivel del mar, altitud, batimetría, modelos digitales del terreno, pendientes y productos derivados.
08. Estructuras: Construcciones hechas por el hombre, museos, iglesias, fábricas, viviendas, monumentos, tiendas, torres.
09. Información geocientífica: Información perteneciente a las ciencias de la Tierra. Procesos y objetos geofísicos, geología, minerales, ciencias relacionadas con la composición, estructura y origen de las rocas de la Tierra, riesgo sísmico, actividad volcánica, corrimiento y/o desplazamiento de tierras, gravimetría, suelos, hidrología y erosión.
10. Inteligencia militar: Bases militares, estructuras, actividades, cuarteles, zonas de instrucción, transporte militar, alistamiento.
11. Límites: Descripciones legales del terreno. Límites administrativos y políticos.
12. Localización: Información posicional y servicios. Direcciones, redes geodésicas, puntos de control, servicios y zonas postales, nombres de lugares.
13. Medio ambiente: Productos medioambientales, protección y conservación. Contaminación ambiental, tratamiento y almacenamiento de desechos, valoración e impacto ambiental, monitorización del riesgo medioambiental, reservas naturales, paisaje.
14. Océanos: Objetos y características de las aguas saladas (excluyendo las aguas exteriores). Mareas, movimiento de marea, información de costa, arrecifes.
15. Planeamiento catastral: Información usada para tomar las decisiones más apropiadas para el uso futuro de la tierra. Mapas de uso de la tierra, mapas de zonas, levantamientos catastrales, propiedad del terreno.
16. Redes de suministro (servicios): Redes de agua, de energía, de retirada de residuos, de infraestructura de comunicaciones y servicios. Hidroelectricidad, fuentes de energía geotermal, solar y nuclear, distribución y depuración de agua, recogida y almacenamiento de aguas residuales, distribución de gas y energía, comunicación de datos, telecomunicaciones, radios, redes de comunicación.
17. Salud: Servicios de salud, ecología humana y seguridad. Dolencias y enfermedades. Factores que afectan la salud, higiene, abuso de sustancias, salud mental y física.
18. Sociedad: Características de la sociedad y las culturas. Asentamientos, antropología, arqueología, educación, creencias tradicionales, modos y costumbres, datos demográficos, áreas y actividades recreativas, valoración de impacto social.
19. Transportes: Medios y ayudas para transportar personas y mercancías. Carreteras, aeropuertos, pistas de aterrizaje, rutas, vías marítimas, túneles, cartas náuticas, localización de barcos o vehículos, cartas aeronáuticas, ferrocarriles.
Extensión geográfica: Este elemento representa el espacio geográfico cubierto por los datos y documenta las coordenadas del rectángulo geográfico envolvente o posición geográfica del conjunto de datos espaciales o producto, es un campo de carácter obligatorio siempre y cuando el conjunto de datos a documentar posea una georreferenciación o cobertura geográfica de la extensión del objeto considerado. En general, se debe ubicar la información espacial dentro de una zona geográfica, donde se introducirán las coordenadas extremas de dicha zona (coordenada o longitud límite al oeste, coordenada longitud límite al este, coordenada o latitud límite al sur y coordenada o latitud límite al norte). Estas coordenadas geográficas se expresan en grados decimales. Se recomienda emplear las coordenadas utilizando solo un número de decimales significativos:
►Dos decimales para escalas pequeñas (mayores de 1:250.000)
►Seis decimales para escalas medianas y grandes (menores de 1:250.000)
La siguiente figura ejemplifica la introducción de coordenadas dentro del rectángulo envolvente en el software de GeotNetwork:
[imagen]
Figura 1 Rectángulo geográfico envolvente
Información suplementaria: Cualquier otra información descriptiva adicional no incluida en el resumen del conjunto de datos, como puede ser el formato en que se encuentra el producto (DXF, SHP, Geo TIFF, PDF, JPG), la resolución visual, número de coordenadas, datum vertical y, en el caso de una hoja cartográfica, algunos datos contemplados en la información marginal, como pueden ser: nombre de hojas adyacentes, el intervalo de elevación de las curvas de nivel índice o auxiliares o alguna referencia o aclaración especial sobre la cuadrícula.
Punto de contacto
Permite documentar, bajo una estructura unificada, datos claves acerca de organizaciones, instituciones o personas involucradas en la creación, autoría, custodia, conservación o publicación de cualquier tipo de producto o conjunto de datos, y los mecanismos para comunicarse con ellos.
Nombre: Nombre y apellidos de la persona responsable a nivel de la institución, que representa o custodia los datos
Organización: Nombre del organismo del contacto.
Posición/cargo: De la persona del contacto (jefe de departamento, subdirección, coordinador).
Rol/función que representa: Función que desempeña la persona responsable. La norma ISO 19115 específica los siguientes roles posibles:
Rol del punto de contacto (ISO 19115: 2003)
Autor: Parte autora del recurso.
Conservador: Parte que acepta la responsabilidad de los datos y asegura un cuidado apropiado y el mantenimiento del recurso.
Distribuidor: Parte que distribuye el recurso.
Creador: Parte que ha creado el recurso.
Propietario: Parte que es dueña del recurso.
Punto de contacto: Parte con la que se puede contactar para informarse sobre el recurso y adquirirlo.
Investigador principal: Parte clave responsable de recopilar información y conducir la búsqueda.
Procesador: Parte que ha procesado los datos de tal modo que ha modificado el recurso.
Editor: Parte que edita el recurso.
Proveedor del recurso: Parte que suministra el recurso.
Usuario: Parte que usa el recurso.
Teléfono: Número de teléfono donde se puede contactar a la persona responsable.
Fax: Número de fax donde se puede contactar a la persona responsable.
Dirección: De la institución donde labora la persona responsable.
Ciudad: Nombre de ciudad donde se ubica la organización.
Provincia: Nombre de la provincia donde se ubica la organización.
Código postal: Número del código postal del contacto u organización.
País: Nombre del país donde se ubica la organización.
Correo electrónico: Dirección electrónica donde se puede contactar a la persona responsable.
Página web de la institución: Dirección web o URL de la institución.
5.2. Sección de distribución
Esta sección se refiere a la opción disponible para obtener los datos o recursos, y está compuesta por los siguientes apartados:
URL para servicio OGC: Es la dirección web para la utilización de los datos como un servicio OGC.
Protocolo: Es el tipo de acceso a la información, ya sea por servicio Web o descarga directa.
Nombre “name”: Se refiere al nombre del recurso para un servicio de descarga, por ejemplo aquellos formatos como: ZIP, KML, TIFF, PDF, etc. Y si se trata de un servicio Web, se pondrá
el nombre idéntico al nombre de la capa publicada, el cual no debe de ser muy extenso. El Instituto Geográfico Nacional por ejemplo, para el caso de la capa de Red Geodésica Nacional de Costa Rica, utilizará como “name”: RED_GEODESICA. Descripción: Descripción especifica de lo que es o hace el recurso en línea.
5.3. Sección de representación espacial
Corresponde a la documentación de los mecanismos usados para la representación espacial de datos en formato raster, lo cual permite obtener precisión acerca de los procesos de georreferenciación y georrectificación.
Número de dimensiones: Es el número de variables espaciales y temporales presentes en una imagen.
Resolución espacial: Es el tamaño del píxel presente en la imagen, se documentará la resolución espacial de la celda o píxel, expresando el valor numérico seguido de la unidad de medida: por ejemplo: 2,5 metros.
Geometría de la celda: Es la forma del píxel (área o punto) presente en la imagen.
Orientación del píxel: Es la organización de los píxeles en la imagen.
Disponibilidad de los parámetros de transformación: Se debe seleccionar su existencia o no.
Disponibilidad de puntos de control: Se debe seleccionar su existencia o no.
5.4. Sección del sistema de referencia
Descripción del sistema de referencia espacial y temporal usado en el conjunto de datos. Está compuesta por:
Título: Se refiere al nombre del sistema de la proyección de referencia del dato.
Fecha: Se refiere a la época en que se genera el elemento. Esta aplica para datos con escalas mayores a 1:1000, por ejemplo escalas utilizadas en levantamientos topográficos y procesos resultados de observaciones de los Sistemas Globales de Navegación por Satélite (GNSS).
Tipo de Fecha: Para el caso específico de Costa Rica es la fecha de creación o levantamiento en sitio del elemento, por lo se debe de seleccionar ésta opción de la lista controlada presente en la plantilla de metadatos geográficos.
Otros aspectos de la mención: Éste apartado incluye información adicional sobre:
Datum: Se refiere a la materialización del elipsoide de referencia en un territorio para tener acceso a coordenadas, latitud (Φ), longitud (λ) y altura (h). En el caso de Costa Rica el CR05 derivado de la red medida en el 2005 que materializa el elipsoide WGS84 respecto al ITRF2000 en la época 2005,83.
Elipsoide de referencia: Es un elipsoide que se utiliza como superficie matemática de referencia posicional en cálculos geodésicos, por ejemplo WGS84.
ITRF: Es un conjunto de puntos con sus coordenadas cartesianas en 3 dimensiones distribuidos en todo el mundo y que sirven como un sistema de referencia ideal, según lo definido por la Resolución N º 2 UIGG adoptada en Viena, 1991.
Época: Se refiere a la época en la cual se realiza una medición que tiene vínculo directo con la realización más actual del ITRF y que es necesario incorporar a efectos de considerar la variación de su posición en el tiempo por variaciones presentadas en la tectónica de placas. Por ejemplo la época para el dato CR05 equivale a 2005,83, que corresponde al 29 de octubre del año 2005, ésta se calcula de la siguiente manera:
Se suma la cantidad de días acumulados de cada mes del año 2005 hasta setiembre, más los 29 días del mes de octubre, esto corresponde a 302 días, los cuales se dividen por el total de días del año, o sea 365 y el resultado redondeado es 0,83. Código: Es el nombre del Código EPSG de la proyección de referencia según European Petroleum Survey Group (EPSG). Para el caso de nuestro país, se utilizará la siguiente numeración, según la proyección empleada:
Lambert Norte, EPSG: 5456
Lambert Sur, EPSG: 5457
CRTM05, EPSG: 5367
WGS84, EPSG: 4326
5.5. Sección de información sobre la calidad del dato Sección que contiene información sobre la calidad y evaluaciones de esta en la elaboración de datos geográficos, así como su clasificación y el nivel de jerarquía que presentan según el tipo de recurso.
Nivel de jerarquía: Es el nivel de jerarquía o clasificación de los datos según las especificaciones de la norma empleada. Entre algunas de las opciones por seleccionar están las siguientes:
Nivel de jerarquía
Atributo: Se aplica a categorías como por ejemplo de ríos: 1º, 2º, y 3º orden; jerarquía de carreteras: primaria, secundaria, terciaria; niveles de salinidad; etc. | Sesión de campo: La información se aplica a una sesión de campo. Ejemplo: captura de datos con GPS (Global Position System) u otros sistemas de posicionamiento satelital, levantamiento topográfico.
Tipo de atributo: La información se aplica a una característica de un objeto. Ejemplo: ríos de 1a categoría, carreteras primarias o rutas nacionales, porcentaje actual de salinidad en el agua. | Modelo: Se aplica a un modelo digital de elevaciones, modelado del drenaje de una cuenca hidrográfica, etc.
Hardware de captura: La información se aplica al hardware de captura. Ejemplo: cámara fotogramétrica, estación total, sensor remoto, etc. | Conjunto de datos no geográficos: La información se aplica a los datos no geográficos. Ejemplo: indicadores socioeconómicos, analfabetización, etc.
Sesión de captura: La información se aplica a una sesión de captura. Ejemplo: barrido de un satélite, métodos de captura indirectos. | Tipo de propiedad: La información se aplica a un tipo de propiedad del objeto, por ejemplo: quebrada permanente, quebrada intermitente.
Conjunto de datos: Es un subconjunto de datos definidos por diferentes criterios: mismo ámbito geográfico, misma información asociada. | Serie: Hace referencia a una colección o a un producto completo, por ejemplo a la serie de hojas topográficas nacionales a diferentes escalas, que cumplen las mismas especificaciones para una determinada realidad.
Grupo de dimensiones: La información se aplica a un grupo de dimensiones. Ejemplo: bandas de una imagen satelital; cada banda se puede considerar como una dimensión. | Servicio: Servicios para visualizar cartografía, transformaciones de coordenadas, seguimiento de flotas, descarga de datos, etc.
Objeto: La información se aplica a un objeto; por ejemplo: hidrografía, penínsulas, autopistas. | Software: La información se aplica a un programa o rutina de ordenador. Ejemplo: Autocad, ArcGis, MicroStation, Erdas, etc.
Clase de objeto: una característica de un determinado tipo de objeto. Por ejemplo: río Cañas, península de Osa, autopista Bernardo Soto. | Hoja (división): Cada una de las unidades que componen una serie cartográfica. La información se aplica a una hoja, como subconjunto espacial de un conjunto de datos geográficos, por ejemplo: hoja 3445- IV-SW, correspondiente a la hoja topográfica Cartago a escala 1: 25.000.
Linaje (declaración): Descripción cualitativa sobre la precisión obtenida en la captura delos datos y la calidad de las fuentes utilizadas para la creación del producto, es una explicación general del conocimiento del productor de datos del linaje de un conjunto de datos.
5.6. Sección de identificación del metadato
Identificador sobre el archivo de metadatos: Es un código interno o valor alfanumérico que identifica de forma única el metadato creado, definido por el organismo y/o institución productor de los datos; no se recomienda que el tamaño sea muy extenso.
Es requerido incorporar en la construcción del identificador del metadato, con el objetivo de disponer de un elemento básico común en la producción de metadatos de datos geoespacialesa nivel nacional los dos siguientes componentes:
CR = Código o las siglas del país al que corresponde el fichero de metadatos (Costa Rica).
IGN = Es el organismo que crea el fichero de metadatos. Se debe utilizar acrónimos o abreviaturas (ejemplo: Instituto Geográfico Nacional de Costa Rica).
El Instituto Geográfico Nacional, utiliza la siguiente estructura de codificación que puede ser utilizada como guía por otras entidades productoras de información geoespacial:
País: Código o las siglas del país al que corresponde el recurso (Costa Rica = CR).
 Institución: Organismo productor del recurso, se debe utilizar acrónimos o abreviaturas (ejemplo: Instituto Geográfico Nacional de Costa Rica = IGN).
Nombre del recurso: Se refiere al nombre del recurso el cual puede estar construido por una codificación propia, por ejemplo “Red de tendido eléctrico R1”, en el caso del IGN se dispone de una codificación para las series cartográficas, por ejemplo “MTN- 3345-I-NE”es un identificador del conjunto de datos al cual pertenece el recurso, en este caso se refiere al Mapa Topográfico Nacional, donde 3345-I-NE es la codificación propia de este recurso dentro del conjunto de datos al cual pertenece.
Escala: Número o valor representa del denominador de la escala del recurso (1:25.000
= 25.000).
Formato al que corresponde el conjunto de datos (VE = vector, RA = raster).
Utilizando como ejemplo la hoja topográfica San José a escala 1:25.000, en formato raster, el código resultante es el siguiente: CR_IGN_MTN_3345-I-NE_25000RA.
Se sugiere que el nombre del recurso esté separado de los otros componentes por guiones bajos (_).
Nota: Es importante considerar al trabajar con GeoNetwork y CatMDEdit, que estos generan un identificador aleatorio del identificador del archivo de metadato, compuesto por números y letras. En ambos casos, para poder editar y cambiar el texto por el requerido, se debe realizar fuera de éstos programas, primero que todo, debemos ubicar el archivo XML, nos posicionarnos sobre éste y con el botón derecho, lo abrimos con WordPad.
Lenguaje del metadato: Lenguaje usado para la documentación del metadato. Existen varias
opciones, pero en nuestro caso será el español.
Lenguaje de codificación del metadato: Es el nombre completo de la codificación (nombre de la norma de codificación) para el conjunto de caracteres utilizado para los metadatos.
Es una estandarización para que los lenguajes se puedan codificar para el uso informático. Los protocolos de Internet necesitan que se establezca una codificación para introducir los textos. Dentro de este apartado hay varias opciones para escoger; los más comunes en el habla hispana son: el ISO-8859-1 y el UTF-8, pero se recomienda usar la codificación UTF8, por codificar cualquier carácter y ser el valor predeterminado para el formato XML.
Fecha de creación del metadato: Fecha en que se generaron los metadatos. El formato utilizado es DD /MM/AAAA (día/mes/año).
Estándar del metadato: Nombre del estándar del metadato y la versión del perfil. En nuestro caso es ISO 19115:2003).
Versión del estándar del metadato: Versión del estándar utilizado en el perfil seleccionado para crear nuestros metadatos. La versión actual para Costa Rica correspondería con la versión: NTIG_CR04_01.2016.
Frecuencia de actualización: Es la periodicidad con que se actualizan los metadatos y viene definida con las siguientes secuencias:
► Continuamente ► Mensualmente ► Según necesidad
► Diariamente ► Trimestralmente ► Irregular
► Semanalmente ► Bianualmente ► No programado
► Quincenalmente ► Anualmente ► Desconocida
Autor del metadato
Nombre: Nombre y apellidos de la persona responsable.
Organización: Nombre del organismo del contacto.
Posición/cargo: Cargo de la persona dentro de la organización.
Rol/función que representa: Función que desempeña la persona responsable. La norma
ISO 19115 específica los siguientes roles posibles:
Autor del metadato (ISO 19115: 2003)
Autor: Parte autora del recurso.
Conservador: Parte que acepta la responsabilidad de los datos y asegura un cuidado apropiado y el mantenimiento del recurso.
Distribuidor: Parte que distribuye el recurso.
Creador: Parte que ha creado el recurso.
Propietario: Parte que es dueña del recurso.
Punto de contacto: Parte con la que se puede contactar para informarse sobre el recurso y adquirirlo.
Investigador principal: Parte clave responsable de recopilar información y conducir la
búsqueda.
Procesador: Parte que ha procesado los datos de tal modo que ha modificado el recurso.
Editor: Parte que edita el recurso.
Proveedor del recurso: Parte que suministra el recurso.
Usuario: Parte que usa el recurso.
Teléfono: Número de teléfono donde se puede contactar a la persona responsable.
Fax: Número de fax donde se puede contactar a la persona responsable.
Dirección: De la institución donde labora la persona responsable.
Ciudad: Nombre de ciudad donde se ubica la organización.
Provincia: Nombre de la provincia/estado donde se ubica la organización.
Código postal: Número del código postal del contacto u organización.
País: Nombre del país donde se ubica la organización.
Correo electrónico: Dirección electrónica donde se puede contactar a la persona responsable.
Página web de la institución: Dirección web o URL de la institución.
6. Plantillas para metadatos geográficos
Al ser la norma ISO-19115 de naturaleza abstracta y no definir la implementación, es decir, no especifica si ha de usarse un lenguaje XML, se emplea el ISO-19139 que es la norma que describe la implementación reglada y codificada de ISO-19115 a nivel de capa y de serie, presentando esquemas XML específicos para la descripción, validación e intercambio de metadatos.
Por tanto, el XML es el lenguaje elegido por organizaciones de gran renombre internacional en materia de normativa, como lo es la Infrastructure for Spatial Information in Europe (INSPIRE), para la documentación de las capas de información geográfica. Basado en lo anterior, el Instituto Geográfico Nacional generó una plantilla para datos raster y una plantilla para datos vectoriales, se clasificaron los diferentes campos como: obligatorios, condicionales y opcionales.
Se aclara que la contenidos de estas plantillas, están basadas completamente en el estándar del perfil oficial de metadatos geográficos para Costa Rica, siendo una herramienta personalizada de gran importancia, que además de facilitar al usuario público o privado, la creación de metadatos de calidad, bajo una estructura ordenada y organizada, permitirá el acceso a la información de una manera más ágil y oportuna.
6.1 Plantilla para datos en formato raster
La norma ISO 19115 para metadatos se compone de varias entidades relacionadas con la identificación, descripción y acceso de los datos. En esta plantilla se encuentran presentes las siguientes secciones:
• MD_Identification
• MD_ Distribution
• MD_Spatial_Representation
• MD_Referente_System
• DQ_DataQuality
• MD_Metadata
La sección MD_Identification contiene elementos que permiten identificar de modo único los datos (figura 2).
[imagen]
Figura 2 Información de identificación
Un apartado importante de la sección MD_Identification es el punto de contacto (figura 3), el cual se refiere a las personas y organizaciones asociadas con el conjunto de datos y a los medios para contactarlos. Incluye el nombre de la persona responsable, por parte de la institución, que representa o custodia los datos.
[imagen]
Figura 3 Punto de contacto
La sección MD_Distribution contiene elementos que especifican el formato y las opciones de acceso al recurso.
[imagen]
Figura 4 Información de distribución
La sección MD_Spatial_Representation abarca elementos para describir las características particulares de la forma de representación espacial de datos en formato raster.
[imagen]
Figura 5 Información sobre representación espacial
La sección MD_Referente_System se refiere al sistema de referencia al que corresponden los datos, donde los componentes como el título o nombre de la proyección, fecha y tipo de fecha se deben completar obligatoriamente, condicionado a si se conoce la fecha del Marco Internacional de Referencia Terrestre o International Terrestrial Reference Frame (ITRF).
Además, se identificará el código de la proyección de referencia del European Petroleum Survey Group (EPSG) en que se encuentran los datos. EPSG es una organización científica europea vinculada a la industria del petróleo, que compiló y difundió una base de datos ampliamente usada, la cual contiene un registro de elipsoides, datums, sistemas de coordenadas y proyecciones cartográficas. De manera obligatoria se requiere la proyección CRTM05 como sistema de proyección oficial del país y la proyección WGS84. Asimismo, es posible incluir varios sistemas de referencia.
Como elementos opcionales y como una personalización del perfil para Costa Rica, se han incluido dentro de la sección Información del sistema de referencia, específicamente el apartado “Otros aspectos de la mención”, el cual debe contener los datos sobre el elipsoide de referencia, datum, Marco Internacional de Referencia Terrestre o International Terrestrial Reference Frame (ITRF) y la Época a la que está directamente vinculada a la medición actual del ITRF.
[imagen]
Figura 6 Información del sistema de referencia
La sección DQ_DataQuality corresponde a la declaración sobre la precisión obtenida en la captura de los datos o en la calidad de las fuentes utilizadas para crear el producto. Además, describe las fuentes y los pasos del proceso necesario para elaborar el recurso. En esta sección, el nivel jerárquico es la descripción del tipo de información cubierto por el producto.
La calidad de los datos es el apartado más importante, dentro del perfil LAMP, después de la identificación. Su obligatoriedad persigue fomentar la correcta documentación en cuanto a la evaluación de calidad de los productos elaborados por una institución.
[imagen]
Figura 7 Información sobre calidad del dato
La sección MD_Metadata se refiere a los elementos que permiten identificar de modo único el metadato, incluyendo la información de su autor y los medios para contactarlo.
[imagen]
Figura 8 Sección de identificación del metadato
6. 2 Plantilla para datos en formato vectorial
En la sección de identificación de datos en formato vectorial, se mantienen las variables requeridas en la plantilla definida para los datos en formato raster. En la entidad de Información de identificación, específicamente en tipo de representación espacial, se seleccionará la opción vectorial. Lo referido a Información sobre la representación espacial se omite por completo.
7. Edición de metadatos con GeoNetwork como catálogo
El Instituto Geográfico Nacional, emplea para la generación de metadatos la plataforma del programa de Geonetwork. En las siguientes páginas se visualiza la creación de un metadato en formato raster, específicamente de la hoja topográfica San José a escala 1:25.000, en su primera edición del año 2012, generado con la plantilla XML de metadatos propuesta.
En la barra de menú de Administrador, debe de seleccionarse la opción de Importar nuevo Metadato y cargamos la plantilla correspondiente (raster o vectorial) a utilizar.
[imagen]
Figura 9 Sección para crear el metadato
Seguidamente, se despliegan las diferentes plantillas que ofrece el programa por defecto.
[imagen]
Figura 10 Selección de la plantilla de metadatos a utilizar
Al seleccionar la plantilla que nos interesa, dentro de la carpeta donde están guardando los archivos, escogemos la opción de metadata y le damos importar, seguidamente podemos hacer uso y editar nuestros propios datos, para nuestra capa geográfica.
[imagen]
[imagen]
Figura 11 Edición de los metadatos
El resultado de la búsqueda de los metadatos se muestra como registros del catálogo.
[imagen]
Figura 12 Ejemplo de consulta en el catálogo de metadatos
Una vez que se ha editado y guardado un metadato dentro de la plataforma de Geonetwork, lo observamos de la siguiente manera:
[imagen]
[imagen]
[imagen]
Figura 13 Visualización del metadato como resultado de la consulta en el catalogo
Algunos ejemplos de imágenes de las diferentes secciones de la plantilla de metadatos geográficos:
[imagen]
Figura 14 Sección de identificación (MD)_Identificación)
[imagen]
Figura 15 Sección de distribución (MD_Distribución)
[imagen]
Figura 16 Sección de representación espacial (MD_Spatial_Representation)
[imagen]
Figura 17 Sección del sistema de referencia (MD_Reference System)
[imagen]
Figura 18 Sección de información sobre la calidad de dato (DQ_Data Quality)
[imagen]
[imagen]
[imagen]
[imagen]
Figura 19 Sección de identificación de metadato (MD_Metadata)
8. Consideraciones finales
Se espera que esta primera versión del Perfil oficial de metadatos geográficos de Costa Rica se constituya en una herramienta de uso generalizado para quienes producen y publican información geoespacial en nuestro país.
Es preciso crear una cultura en cuanto a la documentación de información geoespacial fundamental y temática, que facilite su uso, divulgación y publicación.
Con esta herramienta se pretende aplicar, en la generación de metadatos geográficos nacionales, el uso de normas técnicas y estándares internacionales del ámbito espacial, basados en la Organización Internacional de Normalización (ISO).
La adopción del presente perfil requiere de un proceso de asimilación, el cual se puede lograr mediante actividades de capacitación y difusión en esta materia, como manuales, talleres, cursos, etc.
Para facilitar un mejor entendimiento del perfil, se incluye un anexo: que contiene la traducción de inglés al español de algunas de las listas controladas que aparecen en las plantillas de metadatos.
Adicionalmente, se adjuntan las plantillas de metadatos tanto raster como vectorial, en formato XML.
9. Bibliografía
Caplan, Priscilla (1995). You call it corn, we call it syntax-independent metadata for document-like objects. The Public Access Computer Systems Review, v. 6, n. 4. Extraído el 11 de noviembre de 2012, de http://journals.tdl.org/pacsr/index.php/pacsr/issue/view/ 241
IUGG (1991). Resolution N° 2. Extraído el 21 de noviembre de 2013, de http://www.iers.org/IERS/EN/DataProducts/ITRF/itrf.html?__nnn=true
IDEE (2012). Documento guía: metadatos de servicios. Ministerio de Fomento de España, Consejo Superior Geográfico.
IDEC (2003). ISO 19115 Esquema compatible de Metadatos. Información Geográfica – Metadatos.
Borrador final.
IGAC-IPGH, (2011). Perfil latinoamericano de metadatos geográficos – LAMP.
INEGI (2010). Acuerdo donde se aprueba la Norma Técnica para la elaboración de metadatos geográficos. Según lo acordado y emitido por la Junta de Gobierno del Instituto de Estadística y Geografía de los Estados Unidos Mexicanos. Publicado en Diario oficial, Segunda Sección, el día viernes 24 de Diciembre.
http://www.dof.gob.mx/nota_detalle.php?codigo=5172412
IPGH (2007). Propuesta IDE. Perfil de metadato latinoamericano (LAMP). Instituto Geográfico Agustín Codazzi. Centro de Investigación y Desarrollo en Información Geográfica. 40 reunión del Consejo Directivo y Simposio IDE América: Conceptos, prácticas y proyectos.
IPGH (2010). Guía de normas. Comité ISO/TC 211. Información geográfica / geomática. Grupo Consultivo de Desarrollo. Edición en español.
IPGH (2012). Material del Curso en línea de metadatos del Programa GeoSUR. Impartido del 17 de septiembre al 21 de octubre de 2012.
Ortiz, Laura, y otros (2008). Generación de metadatos según las Reglas de Implementación de Metadatos de la directiva INSPIRE. En el marco del Departament de Medi Ambient i Habitatge (DMAH) de la Generalitat de Catalunya. Extraído el 15 de abril de 2015, de
http://www.creaf.uab.es/miramon/publicat/papers/jidee08/MetadataINSPIRE_Zaba la.pdf
