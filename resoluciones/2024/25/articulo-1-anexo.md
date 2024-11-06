Anexo N° 1
Este anexo presenta un listado de los datos que los Operadores de Plataformas Digitales deberán incluir en su respectivo Reporte DPI, el cual se debe elaborar a través de un archivo XML, de acuerdo con las Reglas modelo para la presentación de informes por parte de Operadores de Plataformas Digitales emitidas por la Organización para la Cooperación y Desarrollo Económicos (OCDE) en el marco de la Convención sobre Asistencia Administrativa Mutua en Materia Fiscal de la OCDE.
Es importante destacar que este anexo comprende una guía orientativa sobre el contenido del Reporte, no como un modelo o guía para el formato de reporte definitivo. Además, el listado está sujeto a cambios según las disposiciones de la OCDE, los cuales serán comunicados oportunamente a través de los canales oficiales del Ministerio de Hacienda.
Anexo 1: Reporte DPI: Listado de datos a reportar por secciones.
1. En el encabezado del mensaje se identifica el remitente, el destinatario, el tipo de mensaje y el período de informe.
Elemento | Elemento en español | Descripción | Requerimiento
SendingEntityIN | Entidad emisora | Identifica al operador de plataforma informante que envía el mensaje a través de un número de identificación definido a nivel nacional. | Opcional
TransmittingCountry | País transmisor | Jurisdicción de la Autoridad Competente que transmite el mensaje de DPI. | Validación
ReceivingCountr | País receptor | Jurisdicción de la Autoridad Competente que recibe el mensaje DPI. |
MessageType | Tipo de mensaje | Tipo de mensaje que se envía. La única entrada permitida para los mensajes intercambiados en virtud de las Reglas Modelo en este campo es "DPI" | Validación
Warning | Advertencia | Instrucciones de precaución específicas sobre el uso del contenido del mensaje DPI. | Validación
Contact | Contacto | Información de contacto específica relativa al remitente del mensaje. | Validación
MessageRefID | ID de referencia del mensaje | Identificador único del mensaje del remitente (creado por el remitente) que identifica el mensaje concreto que se envía. | Validación
Elemento | Elemento en español | Descripción | Requerimiento
| | El RefID del mensaje debe comenzar con el código del país de la jurisdicción remitente, a continuación, el año del periodo declarable, luego el código del país receptor antes de un identificador único. |
MessageTypeIndic | Indicación de tipo de mensaje | Tipo de información que se envía, es decir, si se trata de información nueva o si el mensaje pretende corregir o eliminar información enviada previamente. | Validación
ReportingPeriod | Periodo del informe | Año al que se refiere la información del mensaje DPI en formato aaaa-MMDD, sobre la base del año natural en el que finalizó el período de declaración. | Validación
Timestamp | Marca de tiempo | Fecha y hora en que se compiló el mensaje. Se prevé que este elemento sea rellenado automáticamente. | Validación
2. Tipo de organización: El tipo de organización define la información que debe incluirse en el esquema DPI XML en relación con una entidad, en particular, ya sea el operador de la plataforma o un vendedor. Se compone de los siguientes elementos, cuyos detalles se exponen más adelante:
Elemento | Elemento en español | Descripción | Requerimiento
ResCountryCode | Código país según nomenclatura ISO | Código o códigos del país de residencia de la entidad. | Opcional (Obligatorio)
TIN (TIN_Type) | Número identificativo | Número de identificación fiscal (NIF) utilizado por la administración tributaria de la jurisdicción de residencia de la entidad | Validación
Entity IN (OrganisationIN_Ty pe) | Entidad IN (Tipo de Organización) | Número identificación de entidad (EIN). | Opcional (Obligatorio)
VAT | IVA | Este dato se suministra cuando se dispone de un número de identificación relacionado al Impuesto al Valor Agregado. | Opcional (Obligatorio)
Elemento | Elemento en español | Descripción | Requerimiento
Organisation Name | Nombre de la organización | Nombre o razón social | Validación
PlatformBusinessNa me | Nombre de la empresa | Nombre comercial de la plataforma o plataformas sobre las que informa el operador de la plataforma | Opcional (Obligatorio)
Address (Address_Type) | Dirección | Campos referentes a país, cantón, distrito, calle, edificio, piso, código postal, señas de la entidad (o persona). | Validación
OECDLegalAddress Type_EnumType | Tipo de dirección | Permite identificar el atributo (carácter legal de esa dirección): residencial, comercial, etc. |
Address Fix (AddressFix_Type) | Corrección de dirección | Campos referentes a país, cantón, distrito, calle, edificio, piso, código postal, señas de la entidad (o persona). | Opcional
Nexus_EnumType | Nexo | Motivo por el que se comunicará la información a la autoridad competente de un Estado miembro de la Unión Europea. | Opcional (Obligatorio)
AssumedReporting | Informes asumidos | Este campo indica si otro operador de plataforma de elaboración de informes ha asumido la responsabilidad de reportar información sobre un vendedor reportable en lugar del operador original. | Opcional (Obligatorio)
3. El tipo de persona Parte, que se utiliza para identificar a los vendedores individuales.
Elemento | Elemento en español | Descripción | Requerimiento
ResCountryCode | Código de país | Código de país que identifica la residencia principal del Vendedor individual, conforme los requisitos de diligencia debida establecidos en las Reglas Modelo de la OCDE. | Validación
TIN Type | TIN | Número de identificación fiscal (NIF) utilizado por la administración tributaria | Validación
Elemento | Elemento en español | Descripción | Requerimiento
| | de la jurisdicción de residencia del Vendedor individual. |
VAT | IVA | Este dato se suministra cuando se dispone de un número de identificación relacionado al Impuesto al Valor Agregado. | Opcional (Obligatorio)
NamePerson_Type | Nombre | Este dato permite indicar tanto el nombre de nacimiento como el nombre después del matrimonio. | Validación
Address (Address_Type) | Dirección | Campos referentes a país, cantón, distrito, calle, edificio, piso, código postal, señas de la entidad (o persona). | Validación
BirthInfo | Información de nacimiento | Información de nacimiento de un Vendedor Individual | Validación
BirthPlace (BirthPlace_Type) | Lugar de nacimiento | Información sobre el lugar de nacimiento del Vendedor Individual. | Validación
4. El Cuerpo DPI, que contiene tres subsecciones:
Elemento | Elemento en español | Descripción | Requerimiento
PlatformOperator | Operador de la plataforma | Identifica al operador de la plataforma, según el tipo de Organización. Campo en el que se especifica el informe concreto dentro del mensaje DPI que se transmite. Permite identificar los informes que requieren corrección (para más información, véase la sección Correcciones). | Validación
Other Platform Operators | Otros operadores de plataformas | Permite identificar al: - Operador de plataformas sustituto (este asume la responsabilidad de reportar en nombre del operador principal), o bien - Operador de plataformas | Opcional (Obligatorio)
Elemento | Elemento en español | Descripción | Requerimiento
| | intermediario (involucrado en la cadena, para el que el operador de plataforma principal asume la responsabilidad de reportar) |
Reportable Seller | Vendedor reportable | Se compone de los elementos: - Identidad del vendedor reportable sujeto a intercambio según las Reglas Modelo de la OCDE: Se compone de los elementos Vendedor Entidad y Vendedor Persona Física, en función de la forma jurídica del Vendedor Reportable. Además, cada tipo de identidad del vendedor se compone de los elementos Estándar y GVS, que reflejan los dos tipos de procedimientos de diligencia debida en los que puede basarse un Operador de Plataforma Reportable para determinar la identidad y la residencia fiscal de una Entidad o persona física Vendedora: Estándar y GVS (Government Verification Service) - Actividades Relevantes: incluye información sobre las Actividades Relevantes prestadas por dicho Vendedor Reportable (cantidad y tipos de actividades: Bienes inmuebles, Servicios personales, Venta de bienes y Alquiler de transporte) y la | Opcional (Obligatorio)
Elemento | Elemento en español | Descripción | Requerimiento
| | Contraprestación derivada de las mismas (se divide en cuatro elementos, que representan los trimestres durante los cuales se pagó o abonó la Contraprestación a un Vendedor Reportable) y a su vez se compone de la comisión y el impuesto retenidos por el Operador de la Plataforma al Vendedor. Esto para cada uno de los tipos de las actividades relevantes mencionadas anteriormente. - Especificación del documento: identifica el informe que se está transmitiendo dentro del mensaje. Permite localizar y corregir errores en informes específicos. |
El tipo “Validación” en la columna Requerimiento corresponde a casillas cuyo carácter obligatorio está relacionado al contenido de otros elementos.
