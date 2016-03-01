6. Publicación: La Norma Técnica de Información Geográfica denominada NTIG_CR03_01.2016: Modelo de Datos Geográficos de Costa Rica, Escalas 1:1.000, 1:5.000 y 1:25.000 está disponible completa para acceso público a través de la página web oficial del Sistema Nacional de Información Territorial (SNIT): www.snitcr.go.cr
(Nota de Sinalevi: La presente norma se extrajo del sitio web del Instituto Geográfico Nacional, por lo que se transcribe a continuación:)
[imagen]
NTIG_CR03_01.2016: Modelo de Datos Geográficos de Costa Rica, Escalas 1:1.000, 1:5.000 y 1:25.000
[imagen]
Presentación
Tengo el agrado de presentar la Norma Técnica de Información Geográfica de Costa Rica (NTIG_CR03) denominada Modelo de Datos Geográficos de Costa Rica, Escalas 1:1.000, 1:5.000 y 1:25.000 versión de enero de 2016, el cual nos permite operacionalizar los objetos geográficos descritos en el Catálogo de Objetos Geográficos para Datos Fundamentales de Costa Rica, en una base de datos geoespacial, su codificación se deriva de la norma NTIG_CR02_01_2016.
Esperamos que el modelo de datos geográficos sea un instrumento que permita proveer de información técnica sobre datos geoespaciales para la producción y publicación de información geoespacial en nuestro país. Está alineado a los requerimientos del Sistema Nacional de Información Territorial (SNIT), así como a las consideraciones de orden técnico definidas por el Instituto Geográfico Nacional como elementos fundamentales.
Desde la perspectiva geográfica, ya sea con respecto a productores, gestores y/o usuarios de información, en la actualidad los metadatos se caracterizan por una conexión con los datos e información geoespacial, en alineamiento como parte de la normativa fundamental requerida dentro del contexto de una infraestructura de datos geoespaciales.
De esta manera, el modelo de datos geográficos es de gran importancia para las personas y organizaciones, tanto públicas como privadas, que utilizan y producen datos geoespaciales, para encontrar los datos que necesitan, determinar la mejor forma de utilizarlos y disponer de la herramienta adecuada para su producción.
El Modelo de Datos Geográficos de Costa Rica, Escalas 1:1.000, 1:5.000 y 1:25.000 tiene su origen en el ejercicio del cumplimiento de las competencias de Ley del Instituto Geográfico Nacional en materia de normalización, generación y estandarización de la información geospacial. Esta primera versión es una iniciativa que nos facilitará el intercambio de informaciones interinstitucionales, además de promover de una manera precisa y ordenada la difusión y uso de los datos geográficos. Nuestra posición es inclusiva y abierta en cuanto a los aportes de la comunidad productora, gestora y usuaria de información geoespacial en el ámbito nacional.
Además, la definición y difusión de este documento está en concordancia con los lineamientos establecidos en el decreto N.° 37773-JP-H-MINAE-MICITT (La Gaceta N.° 134 del 12 julio de 2013), mediante el cual oficialmente se crea el Sistema Nacional de Información Territorial (SNIT) como instrumento para la producción, publicación, normativa y estandarización de la información geoespacial en nuestro país. A través del SNIT el IGN está promoviendo la generación de productos, servicios e información geográfica georreferenciada de cubrimiento nacional, regional y local, y la publicación en forma integrada y georreferenciada de información territorial producida por entes y órganos públicos, así como por personas físicas o jurídicas, y el homologar la información geoespacial estandarizada en el marco de una infraestructura de datos espaciales común.
El SNIT es un paso muy importante en el proceso de consolidación de la Infraestructura de Datos Espaciales de Costa Rica (IDECORI), que se define como el conjunto de políticas, organizaciones, estándares y tecnologías que trabajan de forma conjunta para producir, compartir y usar la información geográfica necesaria para apoyar el desarrollo del país en diversos ámbitos.
M.Sc. Max A. Lobo Hernández
Director
Instituto Geográfico Nacional
Índice de contenidos
1. Introducción ............................................................................................................................................... 1
2. Antecedentes .............................................................................................................................................. 1
3. Disposiciones generales .............................................................................................................................. 2
3.1 Nomenclatura y nombre de la Norma Técnica ................................................................................... 2
3.2 Objeto ............................................................................................................................................... 2
3.3 Ámbito de aplicación ............................................................................................................................... 2
3.4 Alcance ................................................................................................................................................... 2
3.5 Aprobación técnica y oficialización ........................................................................................................ 2
3.6 Obligatoriedad ........................................................................................................................................ 3
3.7 Vigencia .................................................................................................................................................. 3
4. Modelo de datos geográficos ...................................................................................................................... 3
5. Consideraciones finales ............................................................................................................................ 35
6. Bibliografía .............................................................................................................................................. 35
Índice de tablas
Tabla 1 Control Geodésico ............................................................................................................................. 4
Tabla 2 Relieve ............................................................................................................................................... 4
Tabla 3 Infraestructura Vial y Transporte .................................................................................................... 7
Tabla 4 Edificaciones y Construcciones ...................................................................................................... 13
Tabla 5 Elementos Hidrográficos y Marinos ............................................................................................. 25
Tabla 6 Límites ............................................................................................................................................. 29
Tabla 7 Cobertura y Usos del Suelo ............................................................................................................ 33
Tabla 8 Catastro ........................................................................................................................................... 33
Tabla 9 Líneas Auxiliares............................................................................................................................ 34
1. Introducción
Si bien este instrumento se ha desarrollado como un requerimiento para los proyectos de producción de ortofotos y cartografía, su ámbito de aplicación no se circunscribe a la creación e implementación de bases de datos geográficos por parte del Instituto Geográfico Nacional y del Registro Nacional, sino que también a otras instituciones y organizaciones involucradas en la producción de datos geográficos a nivel nacional.
Este modelo de datos trabaja en forma conjunta con el catálogo de objetos fundamentales teniendo como punto de conexión entre ambos documentos el código particular a cada objeto geográfico en una forma más estructurada y homogenizada. Estos nos permite conseguir con certeza una mayor calidad de los mismos, al tener comprensión y claridad en cada una de sus definiciones, descripciones de los diferentes tipos de objetos, atributos, dominios y relaciones, lo cual además nos proporciona un ahorro tanto de recursos económicos, como en tiempo de procesamiento.
Esta norma técnica le permite al usuario y productor de la cartografía determinar el método de captura o restitución fotogramétrica de los distintos objetos geográficos a partir de la ortofoto; sean, accidentes del relieve como curvas de nivel, ríos, cobertura vegetal, accidentes costeros, entre otros; así como infraestructura como edificaciones de distintos tipos o la red vial.
2. Antecedentes
Este modelo de datos geográficos tiene su génesis en el ejercicio del cumplimiento de las competencias de Ley del Instituto Geográfico Nacional, en materia de normalización y estandarización de la información geoespacial, ésta primera versión es una iniciativa que nos facilitará el intercambio de información interinstitucionales, además de promover de una manera precisa y ordenada la difusión y uso de los datos geográficos.
El modelo de datos geográficos de Costa Rica, para las escalas 1:1.000, 1:5.000 y 1:25.000, se constituye en la primera versión del modelo de datos oficial para la producción, homologación y estandarización de las bases de datos geoespaciales, publicadas en la plataforma del Sistema Nacional de Información Territorial y por consiguiente para la Infraestructura Nacional de Datos Espaciales de Costa Rica (IDECORI).
3. Disposiciones generales
3.1 Nomenclatura y nombre de la Norma Técnica
NTIG_CR03_01.2016: Modelo de Datos Geográficos de Costa Rica, Escalas 1:1.000, 1:5.000 y 1:25.000
3.2 Objeto
La presente Norma Técnica tiene por objeto proporcionar los elementos necesarios para modelar un fenómeno del mundo real en formato 2D o 3D, así como identificar la geometría del objeto geográfico dentro de una base de datos según escala de representación de la realidad espacial. La descripción del Formato de captura de la información geoespacial, así como su geometría y método de captura podrá ser aplicado a tres diferentes escalas: 1:1000, 1:5000 y 1:25000.
3.3 Ámbito de aplicación
La presente Norma Técnica es de observancia obligatoria. La aplicación e interpretación de la presente Norma Técnica, para efectos administrativos y técnicos corresponderá al Instituto Geográfico Nacional, quien resolverá los casos no previstos por la misma y velará por su actualización conforme corresponda.
3.4 Alcance
La Norma Técnica NTIG_CR03_01.2016: Modelo de Datos Geográficos de Costa Rica, Escalas 1:1.000, 1:5.000 y 1:25.000, constituye un marco de referencia de carácter general sobre los requisitos mínimos que deben observar los funcionarios y usuarios del Instituto Geográfico Nacional, y en general, el sector público (Poderes de la República, instituciones autónomas y semiautónomas, entes adscritos a instituciones autónomas, empresas públicas estatales, empresas públicas no estatales, entes públicos no estatales, entes administradores de fondos públicos, municipalidades y órganos municipales adscritos), sector privado, personas físicas y público en general, productor, gestor y usuario para operacionalizar los objetos geográficos descritos en el Catálogo de Objetos Geográficos para Datos Fundamentales de Costa Rica, en una base de datos geoespacial, su codificación se deriva de la norma NTIG_CR02_01_2016: Catálogo de Objetos Geográficos Fundamentales de Costa Rica.
3.5 Aprobación técnica y oficialización
La Norma Técnica de Información Geográfica denominada NTIG_CR03_01.2016: “Modelo de Datos Geográficos de Costa Rica, Escalas 1:1.000, 1:5.000 y 1:25.000”, se aprobó técnicamente a las catorce horas del día 12 de enero de 2016, conforme está registrado mediante el oficio N° DIG-0012-2016 de esa misma fecha, firmado por el MSc. Max A. Lobo Hernández, Director del Instituto Geográfico Nacional, y la misma queda oficializada a través de la publicación de la Directriz DIG-003-2016 del Instituto Geográfico Nacional del 12 de enero de 2016 en el Diario Oficial La Gaceta.
3.6 Obligatoriedad
Las disposiciones contenidas en esta Directriz y respetiva Norma Técnica son de acatamiento obligatorio.
3.7 Vigencia
La presente Norma Técnica rige a partir de la publicación de la Directriz DIG-003-2016 del 12 de enero de 2016 en el Diario Oficial La Gaceta.
4. Modelo de datos geográficos
En esta sección se desarrolla en forma detallada el modelo de datos para los diferentes objetos geográficos, se incluyen diversas tablas correspondientes con los temas del catálogo de objetos geográficos. La estructura de las tablas presenta una columna para los temas, otra para el código de los objetos, una pequeña descripción de cada uno de ellos, y en las siguientes columnas se incluye la geometría para las tres escalas, y finalmente y de gran importancia, se describe el método de captura de dicho objeto a partir de una ortofoto u ortoimagen.
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
5. Consideraciones finales
Es necesario indicar que la cantidad de objetos geográficos establecidos en el catálogo de objetos es mayor que la cantidad de objetos geográficos incluidos en el modelo de datos, ya que este último se ha diseñado en función a las necesidades de los diversos procesos de contratación para proyectos de producción de ortofotos y cartografía, que son requeridos en su totalidad por el Registro Nacional, y en específico por el Registro Inmobiliario (escalas 1:1.000 y 1:5.000) y el Instituto Geográfico Nacional (1:25.000). Por lo que no se descarta que a futuro el mismo requiera ser ampliando, contemplando nuevas necesidades del Registro Nacional, o incluyendo las de otras instituciones.
6. Bibliografía
IDECA. (2011). Instructivo para la Catalogación de Datos Geográficos (versión. 2.0 Infraestructura de Datos Espaciales para el Distrito Capital). Bogotá, Colombia: Unidad Administrativa Especial de Catastro Digital.
IGAC-CIAF. (2005). Catálogo de Objetos (versión. 1.3). Bogotá, Colombia.
IGM. (2007). Catálogo de Objetos Geográficos (versión. 04). Quito, Ecuador.
IGN. (2010). Normas de Ejecución de los Temas III y IV de INSPIRE, Especificación de Datos de Nombres Geográficos. Madrid, España: Ministerio de Fomento.
IGN. (2011). Catálogo de Objetos y Simbolo para la Producción de Cartografía Básica a Escala 1:10.000 (versión,. 1.0). Lima, Perú: Ministerio de Defensa, editor.
IPGH. (2010). Guía de normas. Comité ISO/TC 211. Información geográfica / geomática (Español ed.). Grupo Consultivo de Desarrollo.
