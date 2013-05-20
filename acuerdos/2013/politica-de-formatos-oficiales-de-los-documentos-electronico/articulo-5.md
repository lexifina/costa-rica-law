5. Especificación de los Formatos Oficiales
5.1 Uso de Formatos Avanzados
En el Sistema Nacional de Certificación Digital, se conocerán como formatos avanzados todos aquellos formatos de firma digital que definen de manera estandarizada los atributos suficientes para garantizar la verificación de la validez del documento en el tiempo, que estén auspiciados por alguna entidad internacional reconocida, y que sus especificaciones técnicas sean de acceso público. Esta definición se basa en los estándares promulgados por el Instituto de Estándares de Telecomunicaciones Europeo (ETSI por sus siglas en inglés), a partir de la Directiva 1999/93/EC emitida por la Unión Europea.
Los formatos oficiales de los documentos electrónicos firmados digitalmente en Costa Rica serán solo aquellos que la Dirección de Certificadores de Firma Digital determine. Bajo esa premisa, se define que los formatos oficiales de los documentos electrónicos firmados digitalmente en Costa Rica serán aquellos construidos con base en los formatos avanzados emitidos como normas técnicas y estándares por la ETSI, en un nivel de especificación que contemple la inclusión de todos los atributos necesarios para garantizar la verificación de su validez en el tiempo de manera irrefutable. Dichos formatos avanzados y configuración de niveles son los que se especifican a continuación:
 CAdES-X-L
o Basado en la especificación ETSI TS 101 733, en su última versión oficial.
o Para documentos con información codificada en binario.
o Para su codificación en soluciones a la medida, se propone el perfil CAdES Baseline Profile de la ETSI, el cual puede encontrarse en la especificación ETSI TS 103 173, en su última versión oficial.
 PAdES Long Term (PAdES LTV)
o Basado en la especificación ETSI TS 102 778, en su última versión oficial.
o Para documentos en formatos PDF y sus formatos extendidos.
o Para su codificación en soluciones a la medida, se propone el perfil PAdES Baseline Profile de la ETSI, el cual puede encontrarse en la especificación ETSI TS 103 172, en su última versión oficial.
 XAdES-X-L
o Basado en la especificación ETSI TS 101 903, en su última versión oficial.
o Para documentos en formatos XML.
o Se recomienda para el desarrollo de soluciones informáticas en donde sea necesaria la interoperabilidad con otras instituciones.
o Para su codificación en soluciones a la medida, se propone el perfil XAdES Baseline Profile de la ETSI, el cual puede encontrarse en la especificación ETSI TS 103 171, en su última versión oficial.
Sin importar las diferencias en codificación y forma inherentes a cada especificación, los niveles de configuración de los formatos avanzados aquí mencionados cumplen con las siguientes características determinantes para su selección:
 Permiten la utilización de algoritmos criptográficos robustos.
 Respetan el principio de neutralidad tecnológica:
o Son estándares abiertos.
o Pueden ser empleados en escenarios multiplataforma.
o No están sujetos a un determinado producto licenciado.
 Cuentan con una adecuada documentación técnica.
 Permiten la incorporación de múltiples firmas en un documento electrónico.
 Implementan los principios de un mecanismo de firma confiable:
o Garantía de la autenticidad del documento electrónico.
o Garantía de la integridad del documento electrónico.
o Ubicación fehaciente del documento electrónico en el tiempo.
 Especifican mecanismos estandarizados para garantizar la preservación y verificación de la validez de las firmas digitales del documento electrónico en el tiempo:
o Inclusión de sellos de tiempo en el documento electrónico.
o Inclusión de la ruta de certificación en el documento electrónico.
o Inclusión de la información de revocación en el documento electrónico.
5.2 Responsabilidades
En el ciclo de vida de un documento electrónico firmado digitalmente mediante el uso de un formato oficial, se identifican dos conjuntos de responsabilidades relacionados con mecanismos de firma digital: la firma digital y la verificación de validez de la firma digital. Para la emisión de un documento electrónico firmado digitalmente, y para la recepción o verificación de su validez, se establecen una serie de actividades que deben realizarse para garantizar que la firma digital asociada tenga valor en el tiempo. El lugar y la manera en que se codifican estos atributos en el documento electrónico corresponden con lo indicado en las especificaciones de la ETSI mencionadas anteriormente.
5.2.1 Firma digital del documento electrónico
Cuando se firma digitalmente un documento electrónico, será responsabilidad del sistema o sistemas que implementan los mecanismos de firma digital incluir los atributos descritos a continuación (siempre respetando el estándar que corresponda):
Nombre del Atributo | Descripción del Atributo | Etapas de proceso posibles para la inclusión del Atributo en el Documento
Resumen hash encriptado (digest) | Mecanismo criptográfico que permite garantizar la integridad y autenticidad del documento. | Emisión
Certificado del firmante | Copia del certificado del firmante que permite verificar la autoría del documento. | Emisión
Tokens de sellado de tiempo1 1 Los tokens de sellado de tiempo que se utilizan de manera estandarizada en los formatos oficiales son para determinar la existencia de un conjunto de datos en un momento determinado del tiempo (por ejemplo, para garantizar que el certificado no estaba vencido al momento de la firma), y no necesariamente para identificar el momento de realizaci鏮 de la firma por parte del firmante ni del momento de la recepci鏮 del documento por parte de un receptor del mismo. Pueden utilizarse otros tokens de sellado de tiempo, adecuadamente controlados y documentados en las herramientas, para tales fines. | Solicitados a una TSA de la jerarquía del Sistema Nacional de Certificación Digital. | Emisión, Recepción o Validación
Rutas de certificación | Cadenas de certificados que ubiquen el certificado del firmante y de los sellos de tiempo en la jerarquía del Sistema Nacional de Certificación Digital. | Emisión, Recepción o Validación
Información de revocación | Respuestas de validez del certificado del firmante, de los sellos de tiempo y de todos los certificados de sus respectivas rutas de certificación. | Emisión, Recepción o Validación
5.2.2 Verificación de la validez de la firma digital en el documento electrónico
Cuando se verifica la validez de un documento electrónico firmado digitalmente en el formato oficial, es imperativo que se realicen las siguientes validaciones de los diferentes atributos que el documento contiene:
Nombre del Atributo | Descripción de la Actividad de Validación
Resumen hash encriptado (digest) | Verificar que el hash encriptado corresponda con el documento electrónico.
Certificado del firmante | Verificar que la firma del documento corresponda con el certificado del firmante.
Tokens de sellado de tiempo | Verificar que los tokens de sellado de tiempo son de fechas previas a la fecha de vencimiento de los certificados del firmante o de las rutas de certificación e información de revocación según corresponda, y así garantizar que todos los certificados y cadenas eran vigentes y válidas cuando se usaron.
Rutas de certificación | Verificar que todos los certificados del documento correspondan a certificados de la jerarquía del Sistema Nacional de Certificación Digital.
Información de revocación | Verificar que todos los certificados del documento eran válidos (vigentes y no revocados) en el momento de su inclusión en el documento.
5.2.3 Consideraciones adicionales para la inclusión de los atributos
Tal y como se desprende de la presente política y de los estándares a los que hace referencia, los atributos “Resumen hash encriptado (digest)” y “Certificado del firmante” solo pueden agregarse en presencia de cada uno de los firmantes titulares de los certificados que realizan un ejercicio de firma sobre el documento electrónico. Los restantes atributos, “Tokens de sellado de tiempo”, “Rutas de certificación” e “Información de revocación”, pueden agregarse posterior al ejercicio de firmado del/de los firmantes del documento, ya sea al momento de la recepción o durante la validación del documento. Esto último es cierto siempre y cuando los certificados de los firmantes, y los certificados de la jerarquía, no hayan vencido ni tampoco hayan sido revocados.
El escenario descrito es una medida existente para atender el riesgo de que, al tratar de hacer una firma digital en formato oficial, los servicios de respuesta en línea o los repositorios de información de revocación no estén disponibles; con el objetivo de que dicha eventualidad no limite la creación de firmas digitales en documentos electrónicos, a los que posteriormente pueden incluirse todos los atributos adicionales que permiten la verificación de la validez de la firma digital del documento electrónico a largo plazo.
