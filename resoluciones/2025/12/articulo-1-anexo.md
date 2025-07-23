Anexo I: Guía para llenado de Reporte CRS - Datos a reportar por
secciones
Este anexo presenta un listado de los datos que los Entidades Financieras deberán incluir en su respectivo Reporte CRS, el cual se debe elaborar a través de un archivo XML (lenguaje de marcado extensible, por sus siglas en inglés), de acuerdo con el Estándar para el intercambio automático de información sobre cuentas financieras, emitido por la Organización para la Cooperación y Desarrollo Económicos (OCDE) en el marco de la Convención sobre Asistencia Administrativa Mutua en Materia Fiscal.
Este anexo comprende una guía orientativa sobre el contenido del Reporte, no constituye un modelo o formato de reporte definitivo. Además, el listado de los datos está sujeto a cambios según las disposiciones de la OCDE, los cuales serán comunicados oportunamente a través de los canales oficiales del Ministerio de Hacienda.
1. El encabezado del mensaje identifica la Administración Tributaria que envía el mensaje. Especifica cuando fue creado el mensaje, a qué periodo se refiere (usualmente un año), la naturaleza del reporte
(original, corrección, suplementario, etc.)
Elemento | Elemento en español | Descripción | Requerimiento
SendingCompanyIN | Número identificativo de Empresa remitente | Número de identificación de la empresa que está enviando el reporte. Aunque no se utiliza para el intercambio entre Autoridades Competentes bajo el CRS, para reportes internos, este elemento sería obligatorio y serviría para identificar la Institución Financiera que reporta a la autoridad tributaria mediante el TIN (Número de Identificación Tributaria) interno. Puede contener de 1 a 200 caracteres. | Opcional
TransmittingCountry | País transmisor | Este elemento identifica la jurisdicción desde la cual se envía la información del reporte. Si el remitente es una administración tributaria, el país de transmisión será la jurisdicción de esa administración. Se utiliza el código de país de 2 caracteres basado en el estándar ISO 3166- 1 Alpha 2 para identificar el país de transmisión. En el caso de | Obligatorio
Elemento | Elemento en español | Descripción | Requerimiento
| | reportes internos, este elemento contendría el código de país nacional. |
ReceivingCountry | País receptor | Este elemento identifica la jurisdicción de la administración tributaria que es el destinatario previsto del mensaje. Se utiliza el código de país de 2 caracteres basado en el estándar ISO 3166- 1 Alpha 2 para identificar el país receptor. En el contexto de reportes internos, este elemento contendría el código de país nacional de la autoridad tributaria receptora. | Validación
MessageType | Tipo de mensaje | Tipo de mensaje que se está enviando. En el contexto del Intercambio Automático de Información (AEOI) bajo el Estándar de Reporte Común (CRS), el único valor permitido para este campo es "CRS". | Validación
Warning | Advertencia | Este elemento se utiliza para proporcionar advertencias, notas o información adicional relevante sobre el contenido del mensaje CRS, permite editar hasta 4,000 caracteres. Es importante utilizar este campo de manera adecuada para brindar claridad y contexto adicional cuando sea necesario. | Opcional
Contact | Contacto | Campo de texto libre que permite introducir información de contacto del remitente del mensaje. | Opcional
MessageRefID | Identificación de referencia del mensaje | Permite tanto al remitente como al receptor identificar el mensaje de manera única para futuras consultas o correcciones. | Validación
MessageTypeIndic | Indicador de tipo de mensaje | Identifica si los datos contenidos en el mensaje son nuevos, corregidos o si se trata de un mensaje que informa que no hay datos para reportar. Los posibles | Validación
Elemento | Elemento en español | Descripción | Requerimiento
| | valores que puede contener son los siguientes: - CRS701: El mensaje contiene información nueva. - CRS702: El mensaje contiene correcciones/eliminaciones de información enviada previamente. - CRS703: El mensaje informa que no hay datos para reportar. |
CorrMessageRefID | Corrección de un reporte | Este elemento se utiliza específicamente en el contexto de correcciones dentro del esquema XML. Permite identificar el mensaje al que se refiere la corrección, lo que facilita el seguimiento y la vinculación de la corrección con el mensaje original. | Opcional (No CRS)
ReportingPeriod | Periodo del reporte | Identifica el último día del período de reporte al que se refiere el mensaje en formato "YYYY-MM- DD" | Validación
Timestamp | Marca de tiempo | Identifica la fecha y hora en que se compiló el mensaje. | Validación
2. Datos de la persona que ejerce el control o del titular de la cuenta, si se trata de una persona física
Elemento | Elemento en español | Descripción | Requerimiento
ResCountryCode | Código de país de residencia | Código del país de residencia fiscal de la persona sobre la que se informa. En el caso de los informes nacionales, si la persona está certificada o es tratada como residente fiscal en más de una jurisdicción, este elemento puede repetirse. | Validación
Elemento | Elemento en español | Descripción | Requerimiento
TIN | Número de identificación tributaria | Número de identificación fiscal (TIN) utilizado por la administración tributaria receptora para identificar al titular de la cuenta individual. | Obligatorio
Name | Nombre | Se refiere al nombre de la persona titular de una cuenta individual, contiene atributos si se trata del nombre de nacimiento, nombre posterior al matrimonio, sobre nombre y otras variables. | Validación
Address | Dirección | Dirección utilizada para reportar la ubicación física del titular de la cuenta individual. Este elemento incluye subelementos como calle, número, ciudad, código postal, entre otros. | Validación
BirthInfo | Información de nacimiento | Lugar y fecha de nacimiento de un titular de cuenta individual. | (Opcional) Obligatorio
3. Titular de la cuenta si se trata de una entidad
Elemento | Elemento en español | Descripción | Requerimiento
ResCountryCode | Código de país de residencia | Código del país de residencia fiscal de la organización declarante o declarada. | (Opcional) Obligatorio
IN | Número de identificación | Número de identificación para identificar a un titular de cuenta entidad (organización). | (Opcional) Obligatorio
Name | Nombre | Nombre de la organización que actúa como titular de la cuenta | Validación
Address | Dirección | Dirección utilizada para reportar la ubicación física de la entidad titular de la cuenta individual. Este elemento incluye subelementos como calle, número, ciudad, código postal, entre otros. | Validación
4. Cuerpo del Reporte CRS
Elemento | Elemento en español | Descripción | Requerimiento
Reporting FI | Reporte de Entidad Financiera | Identifica la entidad financiera que actúa como intermediaria entre los titulares de cuentas financieras y las autoridades fiscales | Validación
ReportingGroup | Grupo informante | Incluye detalles como la identificación del patrocinador (Sponsor) o intermediario (Intermediary) en el caso de que una Institución Financiera utilice un tercero para presentar la información en su nombre. | Validación
Account Report | Cuenta | Incluye el informe concreto dentro del mensaje CRS que se está transmitiendo | (Opcional) Obligatorio
Account Number | Número de cuenta | Número de identificador único que permite a las autoridades fiscales rastrear y verificar la información relacionada con una cuenta específica. Puede ser: - El número de cuenta de una Cuenta de Custodia o Cuenta de Depósito; - El código (ISIN u otro) relacionado con una Deuda o Participación (si no se mantiene en una cuenta de custodia); o - El código de identificación de un Contrato de Seguro de Valor en Efectivo o Contrato de Anualidad. | Validación
Account Holder | Titular de la cuenta | Entidad o persona que es titular de la cuenta financiera reportada. | Validación
Controlling Person | Persona que ejerce el control (controlador) | Persona que tiene influencia significativa sobre una entidad o una estructura legales, lo que puede incluir a individuos que poseen un porcentaje determinado de participación | (Opcional) Obligatorio
Elemento | Elemento en español | Descripción | Requerimiento
| | en la entidad, aquellos que ejercen control de gestión, o aquellos que se benefician económicamente de la entidad o estructura legal |
Account Balance | Saldo de la cuenta | Incluye detalles como el monto del saldo de la cuenta, la moneda en la que se encuentra expresado el saldo, y la precisión de los decimales utilizados para representar el saldo. | Validación
Payment | Pago | Información relacionada con los pagos realizados a la cuenta financiera reportada durante el período de reporte. Se pueden incluir diferentes tipos de pagos que se hayan realizado a la cuenta financiera reportada, como intereses, dividendos, ganancias brutas/redenciones, u otros tipos de pagos específicos. Cada tipo de pago se identifica utilizando un código específico, como CRS501 para dividendos, CRS502 para intereses, CRS503 para ganancias brutas/redenciones, entre otros. | No indica
