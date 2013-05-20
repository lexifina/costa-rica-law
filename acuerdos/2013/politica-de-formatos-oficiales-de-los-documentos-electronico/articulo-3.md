3. Definiciones, conceptos generales y abreviaturas
3.1 Definiciones y conceptos generales
Para los propósitos del presente documento, se aplican los siguientes términos y definiciones:
Documento electrónico: cualquier manifestación con carácter representativo o declarativo, expresada o transmitida por un medio electrónico o informático. En otras palabras, cualquier conjunto de datos creado, preservado, transmitido o visualizado por medios electrónicos puede ser considerado un documento electrónico.
Documento electrónico firmado digitalmente: aquel documento electrónico, cualesquiera que sean su contenido, contexto y estructura, que tiene lógicamente asociada una firma digital. En otras palabras, es un objeto conceptual que contiene tanto el documento electrónico como una firma digital, sin importar que estos dos elementos puedan encontrarse representados por conjuntos de datos diferentes.
Token de sellado de tiempo: Respuesta estandarizada de una TSA que permite relacionar un conjunto de datos con un tiempo concreto, estableciendo así evidencia de que el dato existía antes de ese tiempo. Los token de sellado se emiten de acuerdo al RFC 3161 “Internet X.509 Public Key Infrastructure Time Stamp Protocol (TSP)”. También se conocen con el nombre de estampas de tiempo.
Autoridad de Sellado de Tiempo (TSA por sus siglas en inglés Time Stamping Authority): sistema de emisión y gestión de token de sellado de tiempo basado en una firma digital acreditada dentro de la jerarquía nacional de certificadores registrados.
Ruta de certificación: corresponde a la cadena de certificados que soportan un certificado en particular, empezando en el certificado raíz y terminando en el certificado en cuestión, siempre dentro de la jerarquía nacional según el Sistema Nacional de Certificación Digital.
Información de revocación: se refiere al conjunto de datos que permiten determinar la validez de un certificado en un momento dado del tiempo. Los mecanismos tradicionales de información de revocación son las Listas de Revocación de Certificados (CRLs por sus siglas en inglés) y la respuesta del Protocolo En Línea de Estado de Certificados (OCSP por sus siglas en inglés).
Listas de Revocación de Certificados (CRLs): mantiene un listado de todos los certificados que han sido revocados y del momento en que se dio su revocación. La autoridad certificadora define un tiempo de validez para la CRL, de tal forma que una vez que caduque debe ser actualizada.
Protocolo en Línea de Estado de Certificados (OCSP): protocolo de implementación de servicios de respuesta en línea del estado de un certificado en el momento en que es solicitado. Requiere de comunicación en línea con la autoridad certificadora.
Formato de Firma Digital: especificación donde se define la estructura y codificación de un documento firmado digitalmente.
3.2 Abreviaturas
Abreviatura | Descripción
CA | Autoridad Certificadora (Certificate Authority)
CAdES | CMS Advanced Electronic Signature
CRL | Lista de Revocación de Certificados (Certificate Revocation List)
OCSP | Protocolo En Línea de Estado de Certificado (Online Certificate Status Protocol)
PAdES | PDF Advanced Electronic Signature
TSA | Autoridad de Sellado de Tiempo (Time-Stamping Authority)
TST | Token de Sellado de Tiempo (Time-Stamp Token)
XAdES | XML Advanced Electronic Signature
