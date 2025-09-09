Artículo 5. Especificación de los Formatos Oficiales
Artículo 5.1. Uso de Formatos Avanzados:
En el Sistema Nacional de Certificación Digital, se conocerán como formatos avanzados todos aquellos formatos de firma digital que definen de manera estandarizada los atributos suficientes para garantizar la verificación de la validez del certificado digital en el documento en el tiempo, que estén auspiciados por alguna entidad internacional reconocida, y que sus especificaciones técnicas sean de acceso público. Esta definición se basa en los estándares promulgados por el Instituto de Estándares de Telecomunicaciones Europeo (ETSI por sus siglas en inglés), a partir del reglamento (UE) 2024/1183 a través de la Decisión de Ejecución (UE) 2015/1506 emitido por la Unión Europea.
Los formatos oficiales de los documentos electrónicos firmados digitalmente en Costa Rica serán solo aquellos que la Dirección de Gobernanza Digital, Certificadores de Firma Digital determine. Bajo esa premisa, se define que los formatos oficiales de los documentos electrónicos firmados digitalmente en Costa Rica serán aquellos construidos con base en los formatos avanzados emitidos como normas técnicas y estándares por la ETSI, en un nivel de especificación que contemple la inclusión de todos los atributos necesarios para garantizar la verificación de su validez en el tiempo de manera irrefutable. Dichos formatos avanzados y configuración de niveles son los que se especifican a continuación:
Artículo 5.1.1. AdES (B-LTA) (archivado)
o Se recomienda el uso del nivel B-LTA cuando se necesita la conservación a largo plazo en los escenarios de firmas digitales certificadas que requieren un periodo de validez muy elevado o su extensión (cuando se exceda la vigencia de la Autoridad de Sellado de tiempo), o en los casos que existen consideraciones de seguridad como, por ejemplo: La función hash o los algoritmos de cifrado utilizada por la Autoridad de Sellado de Tiempo ya no sean robustos.
o En estos casos, se puede implementar la política de refirmado que consiste en la adición de nuevas estampas de tiempo sobre el nivel LT (llamado de archivado) esto para garantizar la validez de la firma digital más allá de eventos que puedan limitar su validez.
o Este nivel debe codificarse de acuerdo con los estándares europeos:
? CAdES (B-LTA): CMS Digital Signature (EN 319 122-1)
? PAdES (B-LTA): PDF Digital Signature (EN 319 142-1)
? XAdES (B-LTA): XML Digital Signature (EN 319 132-1)
? JAdES (B-LTA): JSON Digital Signature (ETSI TS 119 182-1)
Artículo 5.1.2. CAdES (B-LT):
o Basado en la especificación ETSI TS 101 733, en su última versión oficial.
o Para documentos con información codificada en binario. o Para su codificación en soluciones a la medida, se propone el perfil CAdES.
o Baseline Profile de la ETSI, el cual puede encontrarse en la especificación ETSI TS 103 173, en su última versión oficial.
Artículo 5.1.3. PAdES (B-LT):
o Basado en la especificación ETSI TS 102 778, en su última versión oficial. o Para documentos en formatos PDF y sus formatos extendidos.
o Para su codificación en soluciones a la medida, se propone el perfil PAdES Baseline Profile de la ETSI, el cual puede encontrarse en la especificación ETSI TS 103 172, en su última versión oficial.
Artículo 5.1.4. XAdES (B-LT)
o Basado en la especificación ETSI TS 101 903, en su última versión oficial. O Para documentos en formatos XML.
o Se recomienda para el desarrollo de soluciones informáticas en donde sea necesaria la interoperabilidad con otras instituciones.
o Para su codificación en soluciones a la medida, se propone el perfil XAdES Baseline Profile de la ETSI, el cual puede encontrarse en la especificación ETSI TS 103 171, en su última versión oficial.
Artículo 5.1.5. JAdES (B-LT) o Basado en la especificación ETSI TS 119 182-1, en su última versión oficial.
o Para documentos en formato JSON y aplicaciones basadas en arquitecturas web modernas.
o Se recomienda para entornos donde se utilicen APIs RESTful, microservicios o intercambios de datos en tiempo real con estructura ligera.
o Para su codificación en soluciones a la medida, se propone el perfil JAdES Baseline Profile de la ETSI, especificado en ETSI TS 119 182-1 y ETSI TS 119 182-2, en sus últimas versiones oficiales.
Sin importar las diferencias en codificación y forma inherentes a cada especificación, los niveles de configuración de los formatos avanzados mencionados en el presente artículo cumplen con las siguientes características determinantes para su selección:
a) Permiten la utilización de algoritmos criptográficos robustos.
b) Respetan el principio de neutralidad tecnológica:
. Son estándares abiertos.
. Pueden ser empleados en escenarios multiplataforma.
. No están sujetos a un determinado producto licenciado.
c) Cuentan con una adecuada documentación técnica.
d) Permiten la incorporación de múltiples firmas en un documento electrónico.
e) Implementan los principios de un mecanismo de firma confiable:
. Garantía de la autenticidad del documento electrónico.
. Garantía de la integridad del documento electrónico.
. Ubicación fehaciente del documento electrónico en el tiempo.
f) Especifican mecanismos estandarizados para garantizar la preservación y verificación de la validez de las firmas digitales certificadas del documento electrónico en el tiempo:
. Inclusión de estampas de tiempo en el documento electrónico.
. Inclusión de la ruta de certificación en el documento electrónico.
. Inclusión de la información de revocación en el documento electrónico.
Artículo 5.2. Responsabilidades
En el ciclo de vida de un documento electrónico firmado digitalmente mediante el uso de un formato oficial, se identifican dos conjuntos de responsabilidades relacionados con mecanismos de firma digital certificada: la firma digital certificada y la verificación de validez de la firma digital certificada. Para la emisión de un documento electrónico firmado digitalmente y para la recepción, se establecen una serie de actividades que deben realizarse para garantizar que la firma digital certificada asociada tenga valor en el tiempo. El lugar y la manera en que se codifican estos atributos en el documento electrónico corresponden con lo indicado en las especificaciones de la ETSI mencionadas anteriormente.
Artículo 5.2.1. Firma digital certificada del documento electrónico
Cuando se firma digitalmente un documento electrónico, se deberá asegurar que el sistema o sistemas que implementan los mecanismos de firma digital certificada incluyan los atributos descritos a continuación (siempre respetando el estándar que corresponda):
Nombre del Atributo | Descripción del Atributo | Etapas de proceso posibles para la inclusión del Atributo en el Documento
Resumen hash encriptado (digest) | Mecanismo criptográfico que permite garantizar la integridad y autenticidad del documento. | Emisión
Certificado del firmante | Copia del certificado del firmante que permite verificar la autoría del documento. | Emisión
Tokens de estampado de tiempo | Solicitados a una TSA de la jerarquía del Sistema Nacional de Certificación Digital. | Emisión o Recepción
Rutas de certificación | Cadenas de certificados que ubiquen el certificado del firmante y de las estampas de tiempo en la jerarquía del Sistema Nacional de Certificación Digital. | Emisión o Recepción
Información de revocación | Respuestas de validez del certificado del firmante, de las estampas de tiempo y de todos los certificados de sus respectivas rutas de certificación. | Emisión o Recepción
Dicha inclusión permitirá garantizar, a través del tiempo, la validez de la firma digital certificada que se plasme en un documento electrónico, lo cual es imprescindible para temas de gestión documental. La CA podrá brindar un firmador de documentos electrónicos, el cual se encuentre en cumplimiento de la normativa vigente.
Artículo 5.2.2. Verificación de la validez de la firma digital en el documento electrónico
Para verificar la validez de un documento electrónico firmado digitalmente en el formato oficial, es imperativo que se realicen las siguientes validaciones de los diferentes atributos que el documento contiene:
Nombre del Atributo | Descripción de la Actividad de Validación
Resumen hash encriptado (digest) | Verificar que el hash encriptado corresponda con el documento electrónico.
Certificado del Firmante | Verificar que la firma del documento corresponda con el certificado del firmante.
Tokens de estampado de tiempo | Verificar que los tokens de estampado de tiempo son de fechas previas a la fecha de vencimiento de los certificados del firmante o de las rutas de certificación e información de revocación según corresponda, y así garantizar que todos los certificados y cadenas eran vigentes y válidas cuando se usaron.
Rutas de certificación | Verificar que todos los certificados del documento correspondan a certificados de la jerarquía del Sistema Nacional de Certificación Digital.
Información de revocación | Verificar que todos los certificados del documento eran válidos (vigentes y no revocados) en el momento de su inclusión en el documento.
Artículo 5.2.3. Consideraciones para la verificación de la firma digital certificada:
La firma digital certificada es un algoritmo matemático que se le agrega al documento electrónico cuando es firmado digitalmente. Los documentos electrónicos firmados digitalmente son una manifestación expresa de la voluntad del firmante representado por un medio electrónico o informático.
La representación gráfica de una firma digital certificada, una impresión o captura de imagen de un documento electrónico firmado digitalmente, por sí solo, no cuenta con validez. La firma digital certificada se valida solamente de manera digital y deberá cumplir con la normativa vigente, lo cual incluye la Ley, reglamento y políticas.
Toda CA autorizada en el país, deberá brindar un validador de documentos electrónicos firmados digitalmente de manera pública y gratuita, que permita verificar los certificados digitales emitidos por todas las Autoridades Certificadoras autorizadas a nivel nacional en cumplimiento de la normativa vigente.
Artículo 5.2.4. Consideraciones adicionales para la inclusión de los atributos
Tal y como se desprende de la presente política y de los estándares a los que hace referencia, los atributos "Resumen hash encriptado (digest)" y "Certificado del firmante" sólo pueden agregarse en presencia de cada uno de los firmantes titulares de los certificados que realizan un ejercicio de firma sobre el documento electrónico. Los restantes atributos, "Tokens de estampado de tiempo", "Rutas de certificación" e "Información de revocación", pueden agregarse posterior al ejercicio de firmado del/de los firmantes del documento al momento de la recepción del mismo. Esto último es cierto siempre y cuando los certificados de los firmantes, y los certificados de la jerarquía, no hayan vencido ni tampoco hayan sido revocados y de acuerdo con el inciso 4.4 de esta Política acerca del cumplimiento.
El escenario descrito es una medida existente para atender el riesgo de que, al tratar de hacer una firma digital certificada en formato oficial, los servicios de respuesta en línea o los repositorios de información de revocación no estén disponibles; con el objetivo de que dicha eventualidad no limite la creación de firmas digitales certificadas en documentos electrónicos, a los que posteriormente pueden incluirse todos los atributos adicionales que permiten la verificación de la validez de la firma digital certificada del documento electrónico a largo plazo.
