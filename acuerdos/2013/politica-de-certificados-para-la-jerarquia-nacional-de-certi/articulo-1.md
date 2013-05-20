El Ministerio de Ciencia, Tecnología y Telecomunicaciones
y la Dirección de Certificadores de Firma Digital
Con fundamento en la Ley de Certificados, Firmas Digitales y Documentos Electrónicos N° 8454 y el artículo 29 del Decreto Ejecutivo N° 33018-MICIT Reglamento a la Ley de Certificados, Firmas Digitales y Documentos Electrónicos, informan sobre la entrada en vigencia de las siguientes políticas:
Versión 1.1 de la “Política de Certificados para la Jerarquía Nacional de Certificadores Registrados”.
(Nota de Sinalevi: La presente norma fue proporcionada por el Ministerio de Ciencia, Tecnología y Telecomunicaciones, y se transcribe a continuación:)
[imagen]
POLÍTICA DE CERTIFICADOS PARA LA JERARQUÍA NACIONAL DE CERTIFICADORES REGISTRADOS
Dirección de Certificadores de Firma Digital
Ministerio de Ciencia, Tecnología y Telecomunicaciones
Índice
1. Introducción ................................................................................................................... 1
1.1 Resumen ......................................................................................................................... 1
1.2 Nombre e identificación del documento ........................................................................ 2
1.3 Participantes en la PKI .................................................................................................... 3
1.4 Uso del certificado.......................................................................................................... 3
1.5 Administración de la Política .......................................................................................... 4
1.6 Definiciones y acrónimos ............................................................................................... 5
2. Responsabilidades de publicación y del repositorio ....................................................... 6
2.1 Repositorios ................................................................................................................... 6
2.2 Publicación de información de certificación .................................................................. 6
2.3 Tiempo o frecuencia de publicación ............................................................................... 6
2.4 Controles de acceso a los repositorios ........................................................................... 6
3. Identificación y autenticación ........................................................................................ 7
3.1 Nombres ......................................................................................................................... 7
3.2 Validación inicial de identidad ...................................................................................... 10
3.3 Identificación y autenticación para solicitudes de re-emisión de llaves ...................... 11
3.4 Identificación y autenticación para solicitudes de revocación ..................................... 11
4. Requerimientos operacionales del ciclo de vida del certificado .................................. 13
4.1 Solicitud de certificado ................................................................................................. 13
4.2 Procesamiento de la solicitud de certificado................................................................ 15
4.3 Emisión de certificado .................................................................................................. 15
4.4 Aceptación de certificado ............................................................................................. 16
4.5 Uso del par de llaves y del certificado .......................................................................... 16
4.6 Renovación de certificado ............................................................................................ 18
4.7 Re-emisión de llaves de certificado .............................................................................. 18
4.8 Modificación de certificados ........................................................................................ 19
4.9 Revocación y suspensión de certificado ....................................................................... 19
4.10 Servicios de estado de certificado ................................................................................ 24
4.11 Finalización de la suscripción ....................................................................................... 25
4.12 Custodia y recuperación de llave.................................................................................. 25
5. Controles operacionales, de gestión y de instalaciones ............................................... 26
5.1 Controles físicos ........................................................................................................... 26
5.2 Controles procedimentales .......................................................................................... 27
5.3 Controles de personal .................................................................................................. 28
5.4 Procedimientos de bitácora de auditoría ..................................................................... 29
5.5 Archivado de registros.................................................................................................. 31
5.6 Cambio de llave ............................................................................................................ 32
5.7 Recuperación de desastre y compromiso .................................................................... 33
5.8 Terminación de una CA o RA ........................................................................................ 34
6. Controles técnicos de seguridad .................................................................................. 35
6.1 Generación e instalación del par de llaves ................................................................... 35
6.2 Controles de ingeniería del módulo criptográfico y protección de la llave privada .... 37
6.3 Otros aspectos de gestión del par de llaves ................................................................. 40
6.4 Datos de activación ...................................................................................................... 41
6.5 Controles de seguridad del computador ...................................................................... 41
6.6 Controles técnicos del ciclo de vida ............................................................................. 42
6.7 Controles de seguridad de red ..................................................................................... 42
6.8 Sellado de tiempo (“Time-Stamping”) .......................................................................... 43
7. Perfiles de Certificados, CRL y OCSP ............................................................................. 44
7.1 Perfil del Certificado ..................................................................................................... 44
7.2 Perfil de la CRL .............................................................................................................. 47
7.3 Perfil de OCSP ............................................................................................................... 47
8. Auditoría de cumplimiento y otras evaluaciones ......................................................... 48
8.1 Frecuencia o circunstancias de evaluación................................................................... 48
8.2 Identidad/calidades del evaluador ............................................................................... 48
8.3 Relación del evaluador con la entidad evaluada .......................................................... 48
8.4 Aspectos cubiertos por la evaluación ........................................................................... 49
8.5 Acciones tomadas como resultado de una deficiencia ................................................ 49
8.6 Comunicación de resultados ........................................................................................ 49
9. Otros asuntos legales y comerciales ............................................................................ 50
9.1 Tarifas ........................................................................................................................... 50
9.2 Responsabilidad financiera .......................................................................................... 50
9.3 Confidencialidad de la información comercial ............................................................. 50
9.4 Privacidad de información personal ............................................................................. 51
9.5 Derechos de propiedad intelectual .............................................................................. 51
9.6 Representaciones y garantías ....................................................................................... 52
9.7 Renuncia de garantías .................................................................................................. 52
9.8 Limitaciones de responsabilidad legal .......................................................................... 52
9.9 Indemnizaciones........................................................................................................... 52
9.10 Plazo y Finalización ...................................................................................................... 53
9.11 Notificación individual y comunicaciones con participantes ........................................ 53
9.12 Enmiendas .................................................................................................................... 53
9.13 Disposiciones para resolución de disputas ................................................................... 53
9.14 Ley gobernante ............................................................................................................ 54
9.15 Cumplimiento con la ley aplicable ................................................................................ 54
9.16 Disposiciones varias ..................................................................................................... 54
9.17 Otras disposiciones ...................................................................................................... 54
10. Anexo A: Definiciones y acrónimos .............................................................................. 55
10.1 Definiciones .................................................................................................................. 55
10.2 Abreviaturas: ................................................................................................................ 60
11 Anexo B: Documentos de referencia ............................................................................ 61
1. Introducción
Este documento define las Políticas de Certificado (en adelante CP) dictadas por la Dirección de Certificadores de Firma Digital (en adelante DCFD) para el Sistema Nacional de Certificación Digital.
La autoridad certificadora registrada debe implementar las políticas en los servicios de certificación que incluyen: la emisión, gestión, suspensión y revocación de los certificados.
Las siguientes secciones describen las políticas de acatamiento obligatorio que deben ser implementadas por la Autoridad Certificadora Raíz (en adelante CA Raíz) y por cualquier otra Autoridad Certificadora Registrada (en adelante CA) en los niveles inferiores de la jerarquía nacional de certificadores registrados. Sin embargo, este documento no pretende ser una guía exhaustiva para la evaluación del cumplimiento de los requisitos necesarios para un proceso de acreditación. La guía detallada para la evaluación de una autoridad certificadora que desea incorporarse al sistema de certificación nacional, debe solicitarse a la DCFD, y la misma se adhiere a los lineamientos establecidos en: la norma INTE-ISO-21188:2007 “Infraestructura de llave pública para servicios financieros — Estructura de prácticas y políticas”.
Este CP se ha desarrollado conforme a lo estipulado en el RFC 3647: ”Internet X.509 Public Key Infrastructure. Certificate Policy and Certification Practices Framework”.
1.1 Resumen
Estas Políticas de Certificado (CP) son específicamente aplicables a:
· Autoridad Certificadora Raíz (CA Raíz).
· Autoridades Certificadoras de Políticas (CA de Políticas) dentro de la jerarquía nacional de certificadores registrados.
· Autoridades Certificadoras emisoras (CA emisoras) que se registren ante la DCFD, y que emitan los certificados a las entidades finales.
· Suscriptores y partes que confían.
Las políticas nacionales contemplan los siguientes tipos de certificados, definidos en este documento como:
· Certificados para CA emisoras.
· Certificados de autenticación de persona física.
· Certificados de firma digital de persona física.
· Certificados de agente electrónico (autenticación) de persona jurídica.
· Certificados de sello electrónico (firma digital) de persona jurídica.
· Certificados de autoridades de sellado de tiempo (TSA).
Los diferentes tipos de certificados están definidos en la política y se implementan a través de una jerarquía de tres niveles: el primero corresponde a la raíz nacional, el segundo nivel corresponde a las autoridades certificadoras de políticas y el tercer nivel a las CA emisoras de certificados.
El siguiente diagrama detalla la estructura de la jerarquía nacional de certificadores registrados:
[imagen]
1.2 Nombre e identificación del documento
Este documento es la “Política de Certificados para la Jerarquía Nacional de Certificadores Registrados” y se referencia mediante el identificador de objeto (OID): 2.16.188.1.1.1.1
Sección | Descripción
2 | joint-iso-itu-t
16 | Country
188 | Costa Rica
1 | Organización
1 | Dirección de Certificadores de Firma Digital
1 | Políticas
1 | Política de Certificados para la jerarquía nacional de certificadores registrados
Las políticas derivadas para la jerarquía nacional de certificadores registrados son:
Política para certificados generados por la jerarquía nacional de certificadores registrados | OID
Política de certificados de CA emisora del Sistema Nacional de Certificación Digital | 2.16.188.1.1.1.1.1
Política de certificados de persona física del Sistema Nacional de Certificación Digital · Firma digital · Autenticación | 2.16.188.1.1.1.1.2 2.16.188.1.1.1.1.3
Política de sellado de tiempo del Sistema Nacional de Certificación Digital | 2.16.188.1.1.1.1.5
Política de certificados de persona jurídica del Sistema Nacional de Certificación Digital · Sello electrónico · Agente electrónico | 2.16.188.1.1.1.1.6 2.16.188.1.1.1.1.7
1.3 Participantes en la PKI
1.3.1 Autoridades certificadoras
Las autoridades certificadoras (CA) son todas las entidades autorizadas a emitir certificados de llave pública dentro de la jerarquía nacional de certificadores registrados. Esto incluye:
· CA Raíz.
· CA de Políticas.
· CA emisoras.
La CA Raíz y las CAs de Políticas son parte de la jerarquía nacional administrada por el Ministerio de Ciencia, Tecnología y Telecomunicaciones (MICITT). Ambas se regulan a través de la Dirección de Certificadores de Firma Digital (DCFD). Las CAs emisoras deben implementar esta política, para formar parte de la jerarquía nacional de certificadores registrados.
1.3.2 Autoridades de Registro
Una Autoridad de Registro (RA) es una entidad que verifica la identidad de los solicitantes que aplican por un certificado. La RA debe validar los requisitos de identificación del solicitante, dependiendo del tipo de certificado y de la especificación de la política pertinente. Además, tramita las solicitudes de revocación para los certificados y valida la información contenida en las solicitudes de certificados. Las Autoridades de Registro se regulan en el documento de “Directrices para las Autoridades de Registro. Características de cumplimiento de Autoridades de Registro (RA) de la jerarquía nacional de certificadores registrados de Costa Rica” emitido por la DCFD para este propósito.
1.3.3 Suscriptores
Se define como suscriptor a todos los usuarios finales a quienes se les ha emitido un certificado por una CA, dentro de la jerarquía nacional de certificadores registrados. El suscriptor puede ser una persona física o una persona jurídica.
1.3.4 Partes que confían
Una parte que confía es una persona física o jurídica que actúa confiando en un certificado y/o en las firmas digitales generadas a partir de un certificado, emitidos bajo la jerarquía nacional de certificadores registrados. Una parte que confía puede o no ser también un suscriptor.
1.3.5 Otros participantes
Sin estipulaciones.
1.4 Uso del certificado
1.4.1 Usos apropiados del certificado
Tipo | Descripción de uso apropiado
Certificados de CA emisora |  Operar la infraestructura PKI y emitir certificados a suscriptores dentro de la cadena de confianza. o Digital Signature. o Certificate Signing. o Off-line CRL Signing. o CRL Signing.
Certificados de firma digital de persona física |  Firma digital o Digital Signature. o Non-Repudiation.
Certificados de autenticación de persona física |  Autenticación o Digital Signature. o Key Encipherment.
Certificados de sello electrónico de persona jurídica |  Sello electrónico o Digital Signature. o Non-Repudiation.
Certificados de agente electrónico de persona jurídica |  Agente electrónico o Digital Signature. o Key Encipherment. o Data Encipherment.
Certificados de Autoridad de Sellado de Tiempo (TSA) |  Sellado de tiempo o Digital Signature. o Non-Repudiation.
1.4.2 Usos prohibidos del certificado
Los certificados emitidos deben ser utilizados dentro del marco de la Ley 8454 “Ley de certificados, firmas digitales y documentos electrónicos” y su reglamento. Cualquier otro uso del certificado no especificado en la Ley 8454, su reglamento y en esta CP (y sus políticas asociadas) está fuera del alcance y responsabilidad de estas políticas.
1.5 Administración de la Política
1.5.1 Organización que administra el documento
Dirección de Certificadores de Firma Digital
Ministerio de Ciencia, Tecnología y Telecomunicaciones, dirección: San José, 50 metros Este del Museo Nacional. Apartado Postal: 5589-1000 San José, Costa Rica. Correo electrónico: firmadigital@micit.go.cr o informacion@firmadigital.go.cr
1.5.2 Persona de contacto
Jefatura de la Dirección de Certificadores de Firma Digital: Director de Certificadores de Firma Digital, correo electrónico: firmadigital@micit.go.cr o informacion@firmadigital.go.cr. Tel. (506) 2248-1515, ext. 189.
1.5.3 Persona que determina la adecuación de la CPS a la Política
El Director de la Dirección de Certificadores de Firma Digital será el encargado de determinar la adecuación de la declaración de prácticas de certificación (CPS) de todas las autoridades certificadoras que desean pertenecer a la jerarquía nacional de certificadores registrados.
1.5.4 Procedimientos de aprobación de la CP
La política y las subsecuentes enmiendas o modificaciones deben ser propuestas por la DCFD o por el Comité Asesor de Políticas, y presentadas al Director de la DCFD, quien posterior a su análisis y correcciones, las somete a consulta pública (salvo casos de urgencia) en la que se invitará a las entidades públicas y privadas, organizaciones representativas y público en general a ofrecer comentarios y sugerencias pertinentes; todo conforme a los artículo 3611 y 3622 de la Ley
1 Artículo 361.-
1. Se concederá audiencia a las entidades descentralizadas sobre los proyectos de disposiciones generales que puedan afectarlas.
2. Se concederá a las entidades representativas de intereses de carácter general o corporativo afectados por la disposición la oportunidad de exponer su parecer, dentro del plazo de diez días, salvo cuando se opongan a ello razones de interés público o de urgencia debidamente consignadas en el anteproyecto.
3. Cuando, a juicio del Poder Ejecutivo o del Ministerio, la naturaleza de la disposición lo aconseje, el anteproyecto será sometido a la información pública, durante el plazo que en cada caso se señale.
2 Artículo 362.- En la disposición general se han de consignar expresamente las anteriores que quedan total o parcialmente reformadas o derogadas.
General de Administración Pública (LGAP). La encargada de la aprobación final de la CP es la DCFD.
1.6 Definiciones y acrónimos
Ver Anexo A: Definiciones y acrónimos
