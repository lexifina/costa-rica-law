3. Identificación y autenticación
3.1 Nombres
3.1.1 Tipos de nombres
En la sección 3.1.4 se explican las reglas para interpretación del código de identificación, la que, en el caso de las personas físicas nacionales corresponde al número de cédula, para personas físicas extranjeras o diplomáticas, al número único de permanencia y para las personas jurídicas corresponde al número de cédula de persona jurídica. El uso del campo número de serie (serial number OID 2.5.4.5) se establece de acuerdo al RFC 3039 “Internet X.509 Public Key Infrastructure Qualified Certificates Profile” como un atributo del nombre distintivo del sujeto.
A continuación se presentan los formatos de los nombres para el suscriptor del certificado dependiendo de su tipo. Cuando los datos se encuentran en itálica significan que son valores de ejemplo.
En el caso de la CA Raíz:
Atributo | Valor | Descripción
Country (C) | CR | El código de país es asignado de acuerdo al estándar ISO 31663. 3 Norma ISO 3166 “Códigos para la representación de los nombres de los países y sus subdivisiones. Parte 1: Códigos de los países”. Esta norma establece los códigos de dos caracteres para la asignación del país
Organization (O) | MICIT | El Ministerio de Ciencia, Tecnología y Telecomunicaciones es el responsable de la Raíz Nacional.
Organization Unit (OU) | DCFD | La Dirección de Certificadores de Firma Digital.
Common Name | CA RAIZ NACIONAL – COSTA RICA | Nombre de la CA Raíz.
Serial Number {OID:2.5.4.5} | CPJ-2-100-098311 | Número de cédula de persona jurídica en el Registro Nacional. El prefijo CPJ corresponde a Cédula Persona Jurídica.
En el caso de las CA de Políticas:
Atributo | Valor | Descripción
Country (C) | CR | El código de país es asignado de acuerdo al estándar ISO 3166.
Organization (O) | MICIT | El Ministerio de Ciencia, Tecnología y Telecomunicaciones es el responsable de las CA de Políticas.
Organization Unit (OU) | DCFD | La Dirección de Certificadores de Firma Digital.
Common Name | CA POLITICA PERSONA FISICA – COSTA RICA | CA POLITICA + Nombre de la política – COSTA RICA
Serial Number {OID:2.5.4.5} | CPJ-2-100-098311 | Número de cédula de persona jurídica en el Registro Nacional. El prefijo CPJ corresponde a Cédula Persona Jurídica.
En el caso de las CA emisoras:
Atributo | Valor | Descripción
Country (C) | CR | El código de país es asignado de acuerdo al estándar ISO 3166.
Organization (O) | CORP. EJEMPLO S.A4 4 Los valores en itálica son colocados a manera de ejemplo. | Nombre de la empresa o institución definido en la certificación de personería jurídica.
Organization Unit (OU) | CA EJEMPLO | Unidad organizacional de la persona jurídica responsable de la CA emisora.
Common Name | CA EJEMPLO - PERSONA FISICA | CA + Nombre CA - Política. La Política puede ser: PERSONA FISICA, PERSONA JURÍDICA, SELLADO DE TIEMPO, u otra definida por la CA Raíz.
Serial Number {OID:2.5.4.5} | CPJ-9-999-999999 | Número de cédula de persona jurídica en el Registro Nacional, debe ser validada durante el proceso de registro.
En el caso de suscriptor persona física:
Atributo | Valor | Descripción
Country (C) | CR | El código de país es asignado de acuerdo al estándar ISO 3166.
Organization (O) | PERSONA FISICA | La política identifica si se trata de un certificado para: Persona Física, Persona Jurídica o Sellado de Tiempo, o bien otra definida por la jerarquía nacional de certificadores registrados.
Organization Unit (OU) | CIUDADANO | La clase de certificado es: CIUDADANO, EXTRANJERO o DIPLOMATICO.
Common Name | JUAN PEREZ PEREZ (FIRMA) | Nombre del suscriptor, según documento de identificación oficial, en mayúsculas y sin tildes El propósito debe ser FIRMA o AUTENTICACION.
Serial Number {OID:2.5.4.5} | CPF-01-0449-0161 | El formato del documento de identificación se especifica en la sección 3.1.4 “Reglas para la interpretación de varias formas de nombres”.
Surname (SN) {OID:2.5.4.4} | PEREZ PEREZ | Se registran los dos apellidos del suscriptor, en mayúsculas y sin tildes.
GivenName (G) {OID:2.5.4.42} | JUAN | Se registra el nombre del suscriptor, en mayúsculas y sin tildes.
En el caso de suscriptor para persona jurídica:
Atributo | Valor | Descripción
Country (C) | CR | El código de país es asignado de acuerdo al estándar ISO 3166.
Organization (O) | PERSONA JURÍDICA | La política identifica si se trata de un certificado para: Persona Física, Persona Jurídica o Sellado de Tiempo, o bien otra definida por la jerarquía nacional de certificadores registrados.
Organization Unit (OU) | | Identificador opcional para unidades organizacionales vinculadas jurídicamente a la persona jurídica solicitante.
Common Name | CORTE SUPREMA DE | Razón social/Nombre de la persona jurídica que
JUSTICIA (SELLO ELECTRONICO) | | solicita el certificado, según la información del Registro de Personas Jurídicas de Registro Nacional. El propósito debe ser SELLO ELECTRÓNICO o AGENTE ELECTRÓNICO.
Serial Number {OID:2.5.4.5} | CPJ-2-300-042155 | El formato de la cédula de persona jurídica se especifica en la sección 3.1.4 “Reglas para la interpretación de varias formas de nombres”.
Subject Alternative Name {OID:2.5.29.17} | Dns=www.poder-judicial.go.cr | Valor opcional donde se coloca el nombre del dominio, y aplica únicamente para los certificados de AGENTE ELECTRÓNICO.
En el caso de suscriptor para autoridad de sellado de tiempo:
Atributo | Valor | Descripción
Country (C) | CR | El código de país es asignado de acuerdo al estándar ISO 3166.
Organization (O) | LABORATORIO COSTARRICENSE DE METROLOGIA | Nombre de la empresa o institución que solicita el certificado.
Organization Unit (OU) | 0001 | Identificador consecutivo para la autoridad de sellado de tiempo. Este campo es responsabilidad de la empresa o institución proporcionarlo, y es utilizado para mantener la continuidad del negocio.
Common Name | TSA LABORATORIO COSTARRICENSE DE METROLOGIA | TSA + Nombre de la persona jurídica, según la información del Registro de Personas Jurídicas de Registro Nacional. Se concatena el propósito de TSA (Time Stamping Authority) para indicar que es una autoridad de sellado de tiempo.
Serial Number {OID:2.5.4.5} | CPJ-3-007-351220 | El formato de la cédula de persona jurídica se especifica en la sección 3.1.4 “Reglas para la interpretación de varias formas de nombres”.
3.1.2 Necesidad de nombres significativos
El nombre significativo corresponde al nombre especificado en el documento oficial presentado por el solicitante en el momento de registro. Además para evitar errores de interpretación en el nombre de personas físicas, se registra el nombre y los apellidos en atributos separados (GivenName y SurName, respectivamente).
3.1.3 Anonimato o pseudónimos de los suscriptores
De acuerdo con la ley 8454, “Ley de certificados, firmas digitales y documentos electrónicos” y su reglamento, los certificados de firma digital no admiten anonimato para cumplir con el requisito de “No Repudio”. El pseudónimo no se considera un nombre significativo del solicitante y no se utilizará como parte del certificado.
3.1.4 Reglas para la interpretación de varias formas de nombres
Certificados de CA emisora
La cédula de persona jurídica es definida por el Registro de Personas Jurídicas de Registro Nacional y debe cumplir el siguiente formato:
Tipo de documento | Prefijo | Formato
Cédula de persona jurídica | CPJ | CPJ-9-999-999999
Certificados de firma digital y autenticación de persona física
El nombre común tiene concatenado el propósito del certificado entre paréntesis, el cual puede ser únicamente uno de los siguientes:
 (FIRMA)
 (AUTENTICACION)
El número de cédula de persona física y el número único de permanencia deben cumplir el siguiente formato:
Tipo de documento | Prefijo | Formato
Cédula de persona física | CPF | CPF-99-9999-9999
Número único de permanencia | NUP | NUP-9XXX999999995 5 El número único de permanencia (NUP) está conformado por los siguientes elementos: · Código de No Nacional, es un dígito, y siempre se asignan los números 1 o 5. · Código de país, es un código alfanumérico de acuerdo con el ISO-3166 “Códigos para la representación de los nombres de los países y sus subdivisiones. Parte 1: Códigos de los países.” con formato de 3 letras, por ejemplo: NIC = Nicaragua, CRI = Costa Rica, USA = Estados Unidos de América, COL= Colombia, etc. · Consecutivo por país, corresponde a la numeración de seis dígitos, que representa la cantidad de personas que han ingresado con estatus migratorio al país en el momento de la inscripción. · Dígitos de verificación, son dos dígitos que verifican la consistencia de la notación para ese extranjero.
Certificados de sello electrónico y agente electrónico de persona jurídica y de autoridad de sellado de tiempo
La cédula de persona jurídica debe cumplir el siguiente formato:
Tipo de documento | Prefijo | Formato
Cédula de persona jurídica | CPJ | CPJ-9-999-999999
3.1.5 Unicidad de los nombres
Para cada suscriptor, la CA emisora debe asegurar que el “nombre distintivo del suscriptor” (subject distinguished name) es único dentro de la jerarquía nacional de certificadores registrados, a través de una verificación dentro del proceso de inscripción.
3.1.6 Reconocimiento, autenticación y rol de las marcas registradas
La jerarquía nacional de certificadores registrados no arbitrará, mediará o resolverá ninguna disputa concerniente a la propiedad de nombres de dominio, nombres de empresas, instituciones o personas jurídicas, o marcas registradas.
3.2 Validación inicial de identidad
3.2.1 Método para probar posesión de la llave privada
El solicitante del certificado debe demostrar que posee la llave privada correspondiente a la llave pública que estará listada en el certificado. El método de prueba de posesión de la llave privada puede ser el PKCS#10, u otras demostraciones criptográficas equivalentes, aprobadas por la DCFD.
3.2.2 Autenticación de identidad de persona jurídica
La identidad de la persona jurídica solicitante debe ser confirmada por la CA emisora, o por la RA, donde aplique, de acuerdo con los procedimientos establecidos. Como mínimo, se debe verificar
el nombre o razón social, la cédula de persona jurídica y representante legal debidamente acreditado contra las bases de datos oficiales correspondientes.
En el caso de los certificados de persona jurídica, si el solicitante requiere incluir información en el campo “unidad organizacional” (Organization Unit), la CA emisora, o donde aplique, la RA deberá solicitar toda la información necesaria al suscriptor para garantizar el vínculo jurídico entre la unidad organizacional en cuestión y la persona jurídica solicitante.
En el caso de los certificados de agente electrónico de persona jurídica, si el solicitante requiere incluir uno o más nombres DNS en el campo “nombre alternativo del sujeto” (Subject Alternative Name, o también conocido como SAN por sus siglas en inglés), la CA emisora, o donde aplique, la RA, debe verificar la información de DNS suministrada por el solicitante, contra los datos oficiales correspondientes.
3.2.3 Autenticación de identidad de persona física
Para la identificación de la persona física la CA emisora o RA verifica la validez y vigencia del documento legalmente aceptado, presentado por el solicitante. Este proceso debe realizarse en forma presencial (cara a cara).
La CA emisora, o donde aplique, la RA, debe verificar la información suministrada por el solicitante contra los datos oficiales correspondientes.
3.2.4 Información del suscriptor no verificada
No aplica, la información incluida en el certificado es verificada durante el proceso de autenticación de la identidad.
3.2.5 Validación de la Autoridad
La CA emisora, o donde aplique, la RA, debe validar la autoridad que posee el solicitante para gestionar un tipo de certificado específico. Además, debe validar que el solicitante no posea impedimentos legales de acuerdo a la información oficial vigente para tales efectos.
En el caso de certificados de persona física, debe validar que sea mayor de edad.
En el caso de certificados de persona jurídica, debe validarse que sea un personero o un representante con facultades suficientes para hacer la solicitud de los certificados.
La CA emisora, o donde aplique, la RA, debe verificar la información suministrada por el solicitante contra los datos oficiales correspondientes.
3.2.6 Criterios para interoperabilidad
Se permitirá la interoperabilidad de los certificados emitidos, siempre y cuando la CA emisora cumpla con la política de la raíz y estén adscritas a la jerarquía nacional de certificadores registrados. La homologación de certificados extranjeros se hará de acuerdo con la legislación aplicable y los procedimientos establecidos por la DCFD para tales casos.
3.3 Identificación y autenticación para solicitudes de re-emisión de llaves
3.3.1 Identificación y autenticación para re-emisión de llaves rutinaria
No se permite la re-emisión de certificados. En dado caso, se debe optar por un nuevo certificado.
3.3.2 Identificación y autenticación para la re-emisión de llaves después de una revocación
Bajo estas circunstancias la re-emisión de llaves no aplica.
3.4 Identificación y autenticación para solicitudes de revocación
Los procedimientos de revocación deben asegurar, previo a cualquier revocación, que la solicitud de revocación ha sido generada por el suscriptor del certificado o por una entidad autorizada para tales propósitos.
Los procedimientos aceptados para la autenticación de solicitudes de revocación presentadas por el suscriptor incluyen alguno de los siguientes medios:
 La recepción de un mensaje firmado digitalmente por el suscriptor del certificado.
 Mediante la validación de una “frase de desafío” (challenge phrase).
 Presencialmente, a través de los procesos de autenticación de identidad (secciones 3.2.2 y 3.2.3).
 Cualquier otro medio aprobado por la DCFD que permita una autenticación robusta.
Los procedimientos aceptados para la autenticación de solicitudes de revocación presentadas por una entidad autorizada para tales efectos (ver sección 4.9.2), incluye la recepción de un mensaje firmado por una autoridad competente.
