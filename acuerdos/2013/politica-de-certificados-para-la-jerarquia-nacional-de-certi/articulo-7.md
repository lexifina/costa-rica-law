7. Perfiles de Certificados, CRL y OCSP
Este capítulo especifica el formato de las CRL y OCSP, tales como información del perfil, versión y extensiones utilizadas. En el caso de la jerarquía nacional de certificadores registrados, los OCSP son un mecanismo opcional para la CA Raíz y las CA de Políticas, debido a que son pocos los certificados emitidos y por tanto revocados por ellas. La verificación del estado de los certificados para las CA emisoras constituye un factor crítico de seguridad para diversas aplicaciones, por lo tanto deben obligatoriamente implementar los dos métodos de validación: OCSP y CRL.
7.1 Perfil del Certificado
Los certificados digitales deben cumplir con:
· Estándar X.509 versión 3.
· RFC3280: Internet X.509 Public Key Infrastructure Certificate and CRL Profile.
· RFC 3039 “Internet X.509 Public Key Infrastructure Qualified Certificates Profile.
· ISO 3166-1 “Códigos para la representación de los nombres de los países y sus subdivisiones. Parte 1: Códigos de los países”.
Cómo mínimo el certificado contiene:
Campo | Valor o restricciones
Versión | V3, los certificados deben ser X.509 versión 3.
Número de serie | Valor único emitido dentro del ámbito de cada CA emisora.
Algoritmo de firma | El Algoritmo de firma debe ser como mínimo SHA1RSA.
Emisor | Nombre de la CA Emisora. Ver sección 7.1.4.
Válido desde | Este campo especifica la fecha y hora a partir de la cual el certificado es válido. Las fechas establecidas para el periodo de validez deben ser sincronizadas con respecto al servicio de tiempo UTC-6.
Válido hasta | Este campo especifica la fecha y hora a partir de la cual el certificado deja de ser válido. Las fechas para la validez del certificado deben ser sincronizadas con el servicio de tiempo UTC-6.
Sujeto | Nombre del suscriptor. Ver sección 7.1.4.
Llave pública del sujeto | Codificado de acuerdo con el RFC 3280. Con un largo de llave mínima de 2048 bits y algoritmo RSA.
Identificador de llave de la autoridad | Este campo es usado por los diversos software de validación para ayudar a identificar a la autoridad certificadora registrada que emitió el certificado en la cadena de confianza. Referencia el campo “Subject Key Identifier” de la CA emisora del certificado.
Identificador de la llave del sujeto | Este campo es usado por software de validación para ayudar a identificar un certificado que contiene una determinada llave pública.
Política del certificado | Describe las políticas aplicables al certificado, especifica el OID y la dirección URL donde se encuentra disponible el CP respectivo.
Uso de la llave | Debe indicar los usos permitidos de la llave. Este campo debe ser marcado como un CAMPO CRÍTICO. Ver sección 1.4.1 Usos apropiados del certificado
Punto de distribución del CRL | Este campo es usado para indicar las direcciones donde puede ser encontrado el CRL correspondientes a la CA que emitió el certificado, de tal forma que se pueda validar si el certificado en cuestión ha sido revocado o no. En el caso del certificado de la CA Raíz, este atributo no debe especificarse.
Acceso a la información de la autoridad | Este campo es usado para indicar las direcciones donde puede ser encontrado el certificado de la CA emisora. Además, para indicar la dirección donde puede accederse el servicio de OCSP, de tal forma que se pueda validar si el certificado en cuestión ha sido revocado o no. En el caso del certificado de la CA Raíz, este atributo no debe especificarse.
Usos extendidos de la llave | Referencia otros propósitos de la llave, adicionales al uso. De acuerdo con la sección 7.1.2.5.
Restricciones básicas | Para el caso de la CA emisora la extensión PathLenConstraint debe ser igual a cero. Ver sección 7.1.2.4 Restricciones básicas.
7.1.1 Número(s) de versión
Todos los certificados emitidos dentro de la jerarquía nacional de certificadores registrados deben ser X.509 versión 3 o superior.
7.1.2 Extensiones del certificado
7.1.2.1 Key Usage
El “key usage” es una extensión crítica que indica el uso del certificado de acuerdo con el RFC 3280 “Internet X.509 Public Key Infrastructure Certificate and CRL Profile”. Ver sección 1.4.1 Usos apropiados del certificado.
7.1.2.2 Extensión de política de certificados
La extensión de “certificatepolicies” del X.509 versión 3 es el identificador del objeto de este CP de acuerdo con la sección 7.1.6. La extensión no es considerada como crítica.
7.1.2.3 Nombre alternativo del sujeto
La extensión “subjectAltName” es opcional y solamente se puede usar para certificados de agente electrónico de persona jurídica. En caso de ser utilizada, el uso de esta extensión debe ser “NO crítico” y únicamente está permitido el uso del nombre DNS, en concordancia con la sección 4.1.2.
7.1.2.4 Restricciones básicas
Para el caso de las CAs emisoras se debe colocar el campo “PathLenghtConstraint” con un valor de 0, para indicar que la CA no permite más sub-niveles en la ruta del certificado. Es un campo crítico.
7.1.2.5 Uso extendido de la llave
La extensión permite configurar los propósitos de la llave, y no es considerada crítica. A continuación se presenta el cuadro con los propósitos comunes:
OID | Descripción | Tipos de certificado
1.3.6.1.5.5.7.3.1 | Autenticación de servidor | Agente electrónico
1.3.6.1.5.5.7.3.2 | Autenticación del cliente | Autenticación de persona física Agente electrónico
1.3.6.1.5.5.7.3.4 | Protección del correo | Firma de persona física
1.3.6.1.5.5.7.3.8 | Sellado de tiempo | Sellado de tiempo
1.3.6.1.4.1.311.20.2.2 | Smart Card Logon | Autenticación de persona física
7.1.2.6 Puntos de distribución de los CRL
La extensión “CRL Distribution Points” contiene las direcciones URL de la localización donde las partes que confían pueden obtener el CRL para verificar el estado del certificado. La extensión NO es crítica.
7.1.2.7 Identificador de llave de Autoridad
El método para la generación del identificador está basado en la llave pública de la CA emisora del certificado, de acuerdo a lo descrito por el RFC 3280 “Internet X.509 Public Key Infraestructura Certificate and CRL Profile”. La extensión NO es crítica.
7.1.2.8 Identificador de la llave del sujeto
La extensión no es crítica, y el método para la generación del identificador de llave está basado en la llave pública del sujeto del certificado y es calculado de acuerdo con uno de los métodos descritos en el RFC 3280 “Internet X.509 Public Key Infrastructure Certificate and CRL Profile”.
7.1.3 Identificadores de objeto de algoritmos
Los certificados generados dentro de la jerarquía nacional de certificadores registrados deben usar uno de los siguientes algoritmos:
 sha-1WithRSAEncryption OID ::= {iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-1(1) 5}
 sha256WithRSAEncryption OID::= {iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-1(1) 11}
El algoritmo SHA-1 se mantiene como algoritmo válido para soportar los certificados que sean emitidos por CAs constituidas al amparo de versiones anteriores de la política, sin embargo toda CA nueva o renovada a partir de la emisión de la presente política deberá emitir certificados utilizando el algoritmo SHA256.
7.1.4 Formas del nombre
Los nombres dentro de la jerarquía nacional de certificadores registrados deben cumplir las regulaciones de la sección 3.1.1. Adicionalmente, los certificados de suscriptores generalmente deben incluir el URL donde se encuentran los términos del uso de los certificados y los acuerdos entre las partes.
7.1.5 Restricciones del nombre
Los nombres se escriben en mayúsculas y sin tildes, únicamente se debe aceptar el carácter Ñ como un caso especial para los nombres de personas físicas y jurídicas.
El código de país es de dos caracteres y se asigna de acuerdo al estándar ISO 3166-1 “Códigos para la representación de los nombres de los países y sus subdivisiones. Parte 1: Códigos de los países”.
7.1.6 Identificador de objeto de Política de Certificado
El OID de la política de certificado correspondiente a cada clase de certificado es definido acorde a la sección 1.2. El director de la DCFD le corresponde la administración de los “Identificadores de Objetos” (OID) para el Sistema Nacional de Certificación Digital.
7.1.7 Uso de la extensión “Restricciones de Política” (Policy Constraints)
Sin estipulaciones.
7.1.8 Semántica y sintaxis de los “Calificadores de Política” (Policy Qualifiers)
El calificador de la política está incluido en la extensión de “certificate policies” y contiene una referencia al URL con el CP aplicable y a los acuerdos de partes que confían.
7.1.9 Semántica de procesamiento para la extensión crítica de “Políticas de Certificado” (Certificate Policies)
Sin estipulaciones.
7.2 Perfil de la CRL
Las listas de revocación de certificados cumplen con el RFC 3280 “Internet X.509 Public Key Infrastructure Certificate and CRL Profile”y contienen los elementos básicos especificados en el siguiente cuadro:
Campo | Valor o restricciones
Versión | Ver sección 7.2.1
Algoritmo de firma | Algoritmo usado para la firma del CRL, puede ser:  sha1WithRSAEncryption (OID: 1.2.840.113549.1.1.5)  sha256WithRSAEncryption (OID:1.2.840.113549.1.1.11)
Emisor | Entidad que emite y firma la CRL.
Fecha efectiva | Fecha de emisión del CRL.
Siguiente actualización | Fecha para la cual es emitida la siguiente CRL. La frecuencia de emisión del CRL está acorde con lo requerido en la sección 4.9.7
Certificados revocados | Lista de certificados revocados, incluyendo el número de serie del certificado revocado y la fecha de revocación.
7.2.1 Número(s) de versión
La jerarquía nacional de certificadores registrados de certificación soporta las CRLs X.509 versión 2.
7.2.2 CRL y extensiones de entradas de CRL
Sin estipulación.
7.3 Perfil de OCSP
El servicio de validación de certificados en línea OCSP (Online Certificate Status Protocol) es una forma para obtener información reciente sobre el estado de un certificado.
El servicio OCSP que se implemente debe cumplir lo estipulado en el RFC2560 “X.509 Internet Public Key Infrastructure Online Certificate Status Protocol – OCSP”.
7.3.1 Número(s) de versión
Debe cumplir al menos con la versión 1 del RFC2560 “X.509 Internet Public Key Infrastructure Online Certificate Status Protocol – OCSP”.
7.3.2 Extensiones de OCSP
Sin estipulaciones.
