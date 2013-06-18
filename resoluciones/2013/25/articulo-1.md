DIRECCIÓN GENERAL DE ADUANAS
RESOLUCIÓN DE ALCANCE GENERAL
RES-DGA-025-2013.—Dirección General de Aduanas, San José, a las nueve horas y trece minutos del día 31 de enero del 2013.
Considerando:
I.—Que el artículo 6 de la Ley General de Aduanas, Nº 7557 del 20 de octubre de 1995 publicada en La Gaceta Nº 212 del 8 de noviembre de 1995 y sus reformas, establece que uno de los fines del régimen jurídico es facilitar y agilizar las operaciones de comercio exterior.
II.—Que el artículo 9 de la Ley General de Aduanas, establece como funciones del Servicio Nacional de Aduanas, actualizar los procedimientos aduaneros y proponer las modificaciones de las normas, para adaptarlas a los cambios técnicos, tecnológicos y a los requerimientos del Comercio Internacional.
III.—Que el artículo 11 de la Ley General de Aduanas, señala que la Dirección General de Aduanas es el órgano superior jerárquico nacional en materia aduanera, que en el uso de su competencia le corresponde la dirección técnica y administrativa de las funciones aduaneras que esta ley y las demás disposiciones del ramo le conceden al Servicio Nacional de Aduanas, la emisión de políticas y directrices para las actividades de las aduanas y dependencias a su cargo.
IV.—Que el artículo 198 de la Ley General de Aduanas establece los recursos de impugnación de los actos de la aduana, que puede interponer el destinario del acto de notificación de la nueva determinación de la obligación tributaria aduanera.
V.—Que el artículo 6 del Reglamento a la Ley General de Aduanas indica que le corresponde al Director General determinar, emitir las políticas y directrices que orienten las decisiones y acciones hacia el efectivo cumplimiento de los fines del régimen jurídico aduanero y la consecución de los objetivos del Servicio Nacional de Aduanas.
VI.—Que para efectos de aprovechar las facilidades que brinda el uso de la herramienta informática, la Dirección General considera necesario modificar el “Mensaje de Notificaciones del Módulo de Ok y Observaciones”, a fin de incorporar un campo 9 al Bloque de Aceptación / Rechazo del Ajuste, que tendrá tres opciones para seleccionar el tipo de recurso de impugnación que se vaya a interponer contra los actos de la aduana. Por tanto:
Con fundamento en las consideraciones de hecho y derecho de cita, potestades y demás atribuciones aduaneras que otorgan los artículos 6°, 7° y 8° del Segundo Protocolo de Modificación al Código Aduanero Uniforme Centroamericano, 3, 5 de su Reglamento así como los ordinales 6, 9, 11, 55, 59 y 61 de la Ley General de Aduanas, Nº 7557 del 20 de octubre de 1995 y sus reformas.
EL DIRECTOR GENERAL DE ADUANAS, RESUELVE:
1º—Publicar el siguiente mensaje:
“Mensaje de Notificaciones del Módulo de Ok y Observaciones”
Dicho mensaje estará disponible en la siguiente dirección electrónica:
http://www.hacienda.go.cr/Msib21/Espanol/TICA/tc_mensajes.htm
(Nota de Sinalevi: La presente norma se extrajo del sitio web de Dirección General de Aduanas, y se transcribe a continuación:)
Detalle de campos de mensajería sistema ticA
FORMATO DE MENSAJE DE NOTIFICACIONES DEL MODULO OK Y OBSERVACIONES
VERSIÓN 1.13
Tel. (506) 257-5069 • Fax (506) 233-1143
Mensaje para el envío de Notificaciones en el Módulo de OK y Observaciones
Este mensaje permitirá:
1. Al TICA notificar al auxiliar los ajustes y posible reliquidación efectuadas sobre los DUAs. Este mensaje será emitido del TICA hacia el AUXILIAR.
2. Al auxiliar responde con un mensaje donde consigna la aceptación o rechazo del ajuste notificado. Este mensaje será emitido del AUXILIAR hacia el TICA.
3. Al TICA informar al auxiliar de la carga de la respuesta de la notificación.
Nombre de los archivos:
Los nombres de los archivos recibidos por el AUXILIAR tendrán la siguiente estructura de nombre:
<Casilla origen>-<ID transacción>-<Casilla destino>-<nombre>.<extensión>, donde
<Casilla origen> | : Corresponde a los 4 dígitos identificadores de la casilla origen dentro de la VAN. En este caso será la casilla asignada al TICA. Colocado por la VAN.
<ID transacción> | : Corresponde a un identificador único asignado al mensaje por parte de la VAN. Colocado por la VAN.
<Casilla destino> | : Corresponde a los 4 dígitos identificadores de la casilla destino dentro de la VAN. En este caso será la casilla asignada al AUXILIAR.
<nombre> | : Corresponde a un nombre asignado por el TICA al archivo.
<extensión> | : Identifica el tipo de archivo recibido por el AUXILIAR: “not” para la notificación inicial enviada por el TICA “nar” para la respuesta enviada por el TICA ante de la carga de la aceptación o rechazo de la respuesta dada por el auxiliar.
Los nombres de los archivos enviados por el AUXILIAR tendrán la siguiente estructura de nombre:
<Casilla destino>-<nombre>.<extensión>, donde
<Casilla destino> | : Corresponde a los 4 dígitos identificadores de la casilla destino dentro de la VAN. En este caso será la casilla asignada al TICA.
<nombre> | : Corresponde a un nombre asignado por el AUXILIAR al archivo.
<extensión> | : Identifica el tipo de archivo enviado al TICA. Para el caso del mensaje de aceptación o rechazo de la notificación será “nor”.
Tomar nota que los guiones separadores de cada componente del nombre de los archivos son obligatorios.
Detalle del mensaje para intercambio de datos
A continuación se listan las tablas con los diferentes bloques que componen un mensaje, detallando los campos que los componen.
NOTA:
· Las modificaciones con respecto a la versión anterior están marcadas de color naranja.
Significado de las columnas de las tablas:
Campo: Número secuencial para identificar los campos dentro de cada bloque o registro.
Nombre: Nombre del campo que debe ser utilizado en la confección del archivo XML. Los nombres señalados con un asterisco (*) pertenece a la llave primaria.
Descripción: Indicación del significado del campo.
Tipo: Definición del tipo de dato correspondiente al campo.
Largo: Tamaño del campo. Se debe utilizar “el punto“como separador decimal. (Ej. Num 4.2 corresponde a un formato 99.99)
O/C: Indica si el campo es Obligatorio o Condicional. Para los casos condicionales, ver la casilla de Instructivo de llenado.
Validación: Indica el nombre de las tablas que contienen los valores utilizados en el campo o puede indicar restricciones aplicables al campo.
Instructivo de llenado: Instrucciones básicas para completar el mensaje de intercambio de información.
Bloque del Mensaje de Notificación de Ajustes realizados a un DUA.
Notificación de Ajustes (YVGNOTRE)
Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación.
1 | YVGNoId* | Identificador de la notificación. Corresponde al número secuencial de notificaciones emitidas por el TICA. | Number | 8,0 | O |
2 | YVGNoCodAdu | Código de aduana de aceptación del DUA que se esta notificando. | Char | 3 | O | Utilizar tabla “Aduanas”
3 | YVGNoAnoPre | Año de aceptación del DUA que se esta notificando. | Char | 4 | O |
4 | YVGNoNumCor | Número de aceptación del DUA que se esta notificando. | Char | 6 | O |
5 | YVGNoNroSec | Nro. Secuencial notificado. Es el número secuencial de notificaciones por DUA. | Number | 2,0 | O |
6 | YVGNoFecEnv | Fecha en que se registro de la notificación. | Date | | O | Formato AAAA-MM-DD
7 | YVGNoTIncMN | Monto total en moneda nacional que dio la reliquidación. | Number | 18,2 | O |
8 | YVGNoTReIMN | Monto total en moneda nacional de la diferencia entre la liquidación y la reliquidación. | Number | 18,2 | O |
9 | YVGNoObs | Observaciones. Texto descriptivo ingresado por el vista sobre los cambios aplicados al DUA. El texto recibido tendrá los siguientes bloques de información: Identificación del Acto y Base Legal. Motivación. Correcciones y/o ajustes realizados. Prevenciones. Identificación de funcionario y fecha de emisión. | LongChar | 5000 | O |
Bloques del Mensaje de Aceptación o Rechazo del Ajuste Notificado.
Aceptación / Rechazo del Ajuste – Bloque de control (YVGNOTARCTR)
Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación | Instructivo de llenado
1 | YVGNOARCDOC | Tipo de identificación del declarante | Char | 1 | O | Utilizar tabla “Códigos Generales” ,tipo 27 “Tipo Documento Personal” | Se consignarán el tipo de identificación legal que corresponde. Ej. F: Cédula física
2 | YVGNOARNDOC | Número de identificación del declarante | Char | 12 | O | | Se consignará el número del documento de identificación legal. Tratándose de una empresa jurídica corresponde al número de cédula jurídica y de una persona física a su número de cédula. Cuando la identificación sea por tipo P o R deberá consignarse los primeros 12 dígitos del número.
Aceptación / Rechazo del Ajuste (YVGNOTAR)
Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación | Instructivo de llenado
1 | YVGNOARNOID* | Identificador de la notificación. | Number | 8,0 | O | | Corresponde al número secuencial de la notificación a la que se desea dar respuesta.
2 | YVGNOARCODADU | Código de aduana de aceptación | Char | 3 | O | Utilizar tabla “Aduanas” | Campo llave del DUA
3 | YVGNOARANOPRE | Año Presentación de aceptación | Char | 4 | O | | Campo llave del DUA.
4 | YVGNOARNUMCOR | Número correlativo de aceptación | Char | 6 | O | | Campo llave del DUA.
5 | YVGNOARACEREC | Respuesta de la notificación | Char | 1 | O | | Consignará “A” cuando acepta el ajuste notificado a través del mensaje enviado por la aduana y “R” cuando no lo acepta.
6 | YVGEntFinan | Entidad Financiera | Char | 3 | C | Utilizar tabla “Entidades Financieras” | En caso de que el ajuste notificado por la aduana sea aceptado por el declarante y además exista un monto a pagar asociado a dicho ajuste, el declarante debe consignar en este campo el código de la entidad financiera elegida para realizar el pago de dicho monto. En caso de que el auxiliar acepte el ajuste, pero no consigne información en este campo, el cobro será dirigido a la cuenta cliente especificada en el DUA sobre el cual se realizó la actuación. Tratándose de Tránsito acogido a Convenio Centroamericano, el cobro será realizado de manera análoga al cobro de declaraciones aduaneras de oficio.
7 | YVGNROCUENTA | Número de Cuenta (sin los 3 dígitos del banco) | Char | 14 | C | | En caso de que el ajuste notificado por la aduana sea aceptado por el declarante y además exista un monto a pagar asociado a dicho ajuste, el declarante debe consignar en este campo el número de cuenta cliente registrada en entidad financiera, sin los dígitos que hacen referencia al código de la entidad financiera, elegida para realizar el pago de dicho monto. En caso de que el auxiliar acepte el ajuste, pero no consigne información en este campo, el cobro será dirigido a la cuenta cliente especificada en el DUA sobre el cual se realizó la actuación. Tratándose de Tránsito acogido a Convenio Centroamericano, el cobro será realizado de manera análoga al cobro de declaraciones aduaneras de oficio.
8 | YVGDUECUENTA | Indicador del dueño de la cuenta cliente | Char | | | | Indicador de si la cuenta cliente corresponde al declarante o al importador.
9 | YVGNOARTIPREC | Tipo de Recurso de Impugnación | Char | 3 | O | Obligatorio si la respuesta en el Campo 5 es “R” | Cuando la respuesta en el campo 5 sea “R”, el declarante deberá declarar según corresponda: REC: Interpone recurso de Reconsideración APE: Interpone recurso de Apelación AMB: Interpone ambos recursos de Reconsideración y Apelación
Bloque del Mensaje de respuesta de la carga de la aceptación o rechazo.
Respuesta a la Aceptación / Rechazo del Ajuste (YVGNOTARRES)
Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación
1 | YVGNOARNOID* | Identificador de la notificaciones. Corresponde al número secuencial de notificaciones emitidas por el TICA. | Number | 8,0 | O |
2 | YVGNOARCODERR* | Código de error. Corresponde al código de error del resultado de la carga. | Char | 4 | O | Utilizar tabla “Errores”
3 | YVGNOARAYUERR | Ayuda error Pequeña reseña que ayuda a ubicar el error dentro del programa. Brinda una pequeña ayuda del lugar donde se presentó el error | Char | 200 | O |
