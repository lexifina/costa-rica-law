DIRECCIÓN GENERAL DE ADUANAS
RES-DGA-013-2011.—San José, a las nueve horas del once de enero de dos mil once.
Considerando
I.—Que el artículo 6 de la Ley General de Aduanas, N° 7557 del 20 de octubre de 1995 publicada en La Gaceta N° 212 del 8 de noviembre de 1995 y sus reformas, establece que uno de los fines del régimen jurídico es facilitar y agilizar las operaciones de comercio exterior.
II.—Que el artículo 9 de la Ley General de Aduanas, establece como funciones de Servicio Nacional de Aduanas, actualizar los procedimientos aduaneros y proponer las modificaciones de las normas, para adaptarlas a los cambios técnicos, tecnológicos y a los requerimientos del Comercio Internacional.
III.—Que el artículo 11 de la Ley General de Aduanas, señala que la Dirección General de Aduanas es el órgano superior jerárquico nacional en materia aduanera, que en el uso de su competencia le corresponde la dirección técnica y administrativa de las funciones aduaneras que esta ley y las demás disposiciones del ramo le conceden al Servicio Nacional de Aduanas, la emisión de políticas y directrices para las actividades de las aduanas y dependencias a su cargo.
IV.—Que el artículo 6 del Reglamento a la Ley General de Aduanas indica que le corresponde al Director General determinar, emitir las políticas y directrices que orienten las decisiones y acciones hacia el efectivo cumplimiento de los fines de régimen jurídico aduanero y la consecución de los objetivos del Servicio Nacional de Aduanas.
V.—Que con la resolución RES-DGA-322-2010 de las diez horas del diecisiete de .setiembre de dos mil diez, se modificó al “Manual de Procedimientos Aduaneros” oficializado mediante Resolución RES-DGA-203-2005 de fecha 22 de junio de dos mil cinco, publicado en el Alcance Nº 23 a La Gaceta Nº 143 específicamente: en lo que respecta al “Procedimiento de Exportación” y al “Procedimiento de Zonas Francas”.
VI.—Que dicha modificación establece que el estacionamiento transitorio debe dar pre-llegada a los viajes generados por DUAs de exportación o reexportación, cuando las UT y sus mercancías sean ingresadas a un ET, previo a su embarque.
VII.—Que en razón de lo indicado en el punto anterior, procede esta Dirección modificar el mensaje: Mensaje de Solicitud de Creación de Viajes Versión 1.4, en lo relacionado al campo TRTENTSAL (tipo de viaje), en el cual se deberá indicar la letra P para registrar la pre-llegada a un viaje asociado a DUA de exportación o reexportación. Por tanto,
Con fundamento en las consideraciones de hecho y derecho de cita, potestades y demás atribuciones aduaneras que otorgan los artículos 6, 9, 11, de la Ley General de Aduanas Nº 7557 del 20 de octubre 1995 y sus reformas y 6 y 7 del Reglamento a Ley General de Aduanas:
EL DIRECTOR GENERAL DE ADUANAS, RESUELVE:
1º—Publicar el Mensaje de Solicitud de Creación de Viajes Versión 1.5., mismo que se encuentra disponible en la siguiente dirección electrónica:
http:/www.hacienda.go.cr/Msib21/Espanol/TICA/tc_mensajes.htm.
(Nota de Sinalevi: La presente norma se extrajo del sitio Web del Ministerio de Hacienda http://www.hacienda.go.cr/NR/rdonlyres/AC3E200F-CB1D-4B9F-B3C7-6009EB270ECB/26981/MENSAJECREACIONDEVIAJESVERSION15.pdf, y se transcribe a continuación:)
(Nota de Sinalevi: Mediante resolución N° RES-DGA-308-2013 se reforma la presente resolución y actualiza el Mensaje de Solicitud de Creación de Viajes versión 1.5 por la versión 1.6 que se transcribe a continuación:)
DETALLE DE CAMPOS DEL MENSAJE DE SOLICITUD DE CREACIÓN DE VIAJES
Formato de Mensaje de Solicitud de Creación de Viajes
VERSION 1.6
consulTica@hacienda.go.cr
Ministerio de Hacienda
Ave 1 y 3, Calle Central, San José
Tel. (506) 257-5069 • Fax (506) 233-1143
Mensaje para la Solicitud de Creación de Viajes
Este mensaje permitirá al auxiliar solicitar al TICA la creación de un viaje de mercancías o bien dar la salida a un viaje ya existente en el TICA. Este mensaje será emitido por el AUXILIAR hacia el TICA y existirá una consulta Web por parte del TICA para que el auxiliar verifique el resultado de la solicitud. Es utilizado tanto para las operativas de tránsito y traslados de mercancías.
Nombre de los archivos:
Los archivos deben venir nombrados según el siguiente estándar:
Los nombres de los archivos enviados por el AUXILIAR tendrán la siguiente estructura de nombre:
<Casilla destino>-<nombre>.<extensión>, donde <Casilla destino> | : Corresponde a los 4 dígitos identificadores de la casilla destino dentro de la VAN. En este caso será la casilla asignada al TICA.
<nombre> | : Corresponde a un nombre asignado por el AUXILIAR al archivo.
<extensión> | : Identifica el tipo de archivo enviado al TICA. En este caso será “TRM”.
Detalle del mensaje para intercambio de datos
A continuación se listan las tablas con los diferentes bloques que componen un mensaje, detallando los campos que los componen.
NOTA:
Las modificaciones con respecto a la versión anterior están marcadas de color naranja.
Significado de las columnas de las tablas:
Campo: Número secuencial para identificar los campos dentro de cada bloque o registro.
Nombre: Nombre del campo que debe ser utilizado en la confección del archivo XML. Los nombres señalados con un asterisco (*) pertenece a la llave primaria.
Descripción: Indicación del significado del campo.
Tipo: Definición del tipo de dato correspondiente al campo.
Largo: Tamaño del campo. Se debe utilizar “el punto“ como separador decimal. (Ej. Num 4.2 corresponde a un formato 99.99)
O/C: Indica si el campo es Obligatorio o Condicional. Para los casos condicionales, ver la casilla de Instructivo de llenado.
Validación: Indica el nombre de las tablas que contienen los valores utilizados en el campo o puede indicar restricciones aplicables al campo.
Instructivo de llenado: Instrucciones básicas para completar el mensaje de intercambio de información.
Tipo de Movimientos (Campo TRTENTSAL):
S = Salida de un Viaje del recinto
E = Entrada de un viaje a recinto
M = Modificación de la ruta de un viaje, siempre y cuando dicho viaje este en estado INI (inicial) y no corresponde a un viaje asociado a DUA
D = Anulación de un Viaje, siempre y cuando este se encuentre en estada INI (Inicial) y no sea un viaje asociado a un DUA
P = Pre-Llegada, registra la llegada de un viaje asociado a un DUA de exportación o reexportación a Estacionamiento Transitorio para su posterior traslado a Puerto y así poder completar el viaje registrando su llegada continuar con el proceso del DUA de exportación o reexportación.
Tipo de Viajes a utilizar en la creación de Viajes, solo en Operativa Aérea (Campo TRTMOVMATZ):
AEN = Creación de un viaje sobre carga aérea normal, sin hacer rebaja de inventario, el destino de este viaje siempre debe ser un Deposito fiscal.
AER = Creación de un viaje sobre carga aérea de la cual se va a rebajar inventario, el destino de este viaje debe ser INTEL (H-129, código de ubicación) o alguna otra ubicación de régimen especial (coordinar con área de procedimientos para definir estos).
ERN = Creación de viajes sobre carga courier distinta de tipo „A‟, no realiza rebaja de inventario, el destino de este viaje debe ser siempre un Deposito fiscal.
ERR = Creación de viajes sobre carga courier de tipo „A‟, realiza rebaja del inventario, el declarante debe ser el mismo que el consignatario de la guía courier madre o a la guía courier hijo en caso de que la guía declarada no sea un hijo. El destino siempre debe ser un Depósito fiscal.
RED = Crea un viaje saliendo desde un depósito fiscal hacia otro depósito, cuando se trata de carga aérea, la cual luego de completado el viaje del CTRM al depósito de desconsolidación, se redestina la carga otro depósito pues no va a ingresar al inventario o régimen del primer deposito (deposito de desconsolidación).
Otras consideraciones:
Para el uso de los esquemas es necesario que se considere lo siguiente:
1. Si se envía fechas nulas, deben colocar el siguiente texto: xsi:nil=”4rae”
Ejemplo: <FECH_VENC xsi:nil=”4rae”></ FECH_VENC>
La línea del ROOT debe venir como sigue:
<ROOT xmlns=”http://www.hacienda.go.cr/TICA” xmlns:xsi=”http://www.w3.org/2001/XMLSchema-instance”>
Bloques del Mensaje de Creación, salida y recepción de viajes.
Encabezado del Viaje (TRTMovPorton) Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación | Instructivo de Llenado
1 | TRTVJID | Número o identificador del Viaje | Num | 16 | O | Para la Creación de un Viaje se deberá consignar este campo “cero”, esto debido a que en la trasmisión inicial de ceración el sistema no ha asignado el número de viaje. Para realizar la salida, modificación de la ruta, Anulación del viaje o recepción del viaje, el auxiliar o responsable deber indicar el número asignado al viaje que generó el sistema de información Aduanero. El cual está compuesto por el año y un consecutivo numérico.
2 | TRTMOVORD | Numero de Ordinal del Viaje | Num | 3 | O | Numero secuencial que identifica el movimiento del viaje, si existen varios destinos se identifica el número del movimiento (ordinal) por cada tramo del viaje. En la creación del viaje siempre debe ser 1.
3 | TRTMOVRCT | Recinto que Despacha o recibe el viaje | Char | 4 | O | Utilizar tabla “Ubicaciones” | Se debe consignar el código de la ubicación de donde inicia o finaliza el viaje.
4 | TRTENTSAL | Tipo de viaje | Char | 1 | O | Se debe consignar S cuando el viaje es de salida y E si el viaje es de entrada, M si se está modificando la ruta del viaje, D si se está anulando el viaje, P se está registrando la pre-Llegada de un viaje asociado a DUA de exportación o reexportación.
5 | TRTMOVPAISTRANS | Código de País del Transportista | Char | 3 | O | RGPAIS | El sistema verificará que el código de país del transportista, sea Costa Rica o bien un país centroamericano, incluyendo Panamá.
6 | TRTMOVTRANSIDTIPO | Tipo de identificación del Transportista | Char | 1 | O | Tabla RGEMPCAT | Se debe consignar el tipo de identificación del transportista, „F‟ persona física, „P‟ pasaporte, „J‟ Jurídica, „R‟ residencia.
7 | TRTMOVTRANSID | Identificación del Transportista | Char | C | 12 | Identificación del documento, Tabla RGEMPCAT, | El sistema validará dicho numero contra el registro de transportistas auxiliares de la función pública, en caso de ser un transportista Internacional buscara que sea un transportista centroamericano.
8* | TRTMOVCHOFERIDTIPO | Tipo de identificación | Char | 1 | C | Se consigna el tipo de identificación legal de conductor del medio de transporte.
9* | TRTMOVCHOFERID | Número de identificación del chofer | Char | 12 | C | Se debe consignar número de identificación legal del chofer que realizara el viaje.
10* | TRTMOVCHOFERNOMBRE | Nombre completo del chofer | Char | 50 | C | Se consignará el nombre con los dos apellidos del chofer que realizará el viaje. |
11* | TRTMOVMAT | Matrícula del cabezal | Char | 25 | O | Se consignará el número de matrícula que tiene el cabezal que realizará el viaje, sin guiones, espacios en blanco o caracteres especiales. |
12 | TRTNACMAT | País de Matrícula del cabezal | Char | 3 | O | Utilizar tabla “países”. | Se consignará el código del país donde se encuentra inscrita la matrícula del cabezal. |
13 | TRTMOVMATR | Matricula del remolque | Char | 25 | C | Se consignara el número de matrícula del remolque que se utilizará para el viaje. |
14 | TRTMOVMATZ | Matricula del semiremolque, Cuando se trate de una creación de viaje en Operativa aérea o de depósito fiscal, este campo corresponderá al Tipo de Viaje que se declara. | Char | 25 | C | Se consignara la matricula del semi remolque que se utilizara para el viaje. Cuando se trata de una creación de viaje en operativa aérea o de depósito fiscal, este campo es obligatorio y deberá corresponder al tipo de viaje que se esté declarando. Cuando se trate de una creación de un viaje producto de un traslado de un contenedor en Operativa Marítima, este campo es obligatorio y deberá corresponder al tipo de viaje que se esté declarando. (Ver apartado de Tipos de Viaje, en pagina 4 de este manual) |
15 | TRTMOVPESO | Peso Bruto | Num | 18.3 | O | > 0 | Peso bruto de la mercancía que se traslada, incluyendo los embalajes de las mismas. Cuanto la UT se presenta vacía se debe indicar el peso de la UT. |
16 | TRTMOVBULT | Cantidad de Bultos | Num | 18.3 | O | >=0 | Total de bultos que se llevan en el viaje, cuando se trata de mercancía a granel corresponde a total de kilos, litros u otros. Cuando corresponde a una UT vacía, se debe indicar valor 0. |
17 | TRTMOVFCHDESCARGA | Fecha programada para la descarga | DateTime | 19 | C | Formato: AAAA-MM-DDTHH:MM:SS >= Fecha Llegada<= Plazo de 24 horas según horario de la aduana. | Fecha que tiene programada para la descarga de la unidad de transporte, y se empleara en el mensaje de finalización del viaje cuando se obligatorio descargar las mercancías. Se enviará cuando se trate de una finalización de viaje y sea obligatorio la descarga de la mercancía. |
18 | TRTRTADST | Código de ubicación destino. | Char | 4 | C | Utilizar tabla “Ubicaciones” | Se consigna el código de la ubicación destino del viaje, es obligatorio si se trata de una salida |
19 | TRTMOVCGTPOTRANS | Tipo de transporte en que llega el Manifiesto | Char | 3 | C | 1 Marítimo, 4 Aéreo, 7 Terrestre | Se deberá consignar el tipo de transporte de ingreso de mercancías al país. Este campo es obligatorio cuanto se realice la creación de viaje contra Manifiesto. |
20 | TRTMOVCGTPOMIC | Tipo de Manifiesto | Char | 1 | C | 0 Ingreso, 1 Salida, 2 manifiesto de Paso | Se consignara el tipo de Manifiesto que corresponda a saber ingreso, salida o paso. Este campo es obligatorio cuanto se realice la creación de viaje contra Manifiesto. |
21 | TRTMOVCGNROMIC | Numero de Manifiesto | Char | 8 | C | Numero de Manifiesto dado | Se consignara el número de manifiesto asignado Este campo es obligatorio cuanto se realice la creación de |
22 | TRTMOVCGFCHARR | Fecha Estimada de Arribo o Salida del MIC | Date | 8 | C | Fecha Estimada de arribo o salida del MIC | Se consignara la fecha asignada en el manifiesto como fecha estimada de arribo o de salida, Este campo es obligatorio cuanto se realice la creación de viaje contra Manifiestos. |
23 | TRTMOVPORPRC | Portación de precinto electrónico | Char | 1 | O | S= Si debe instalarse/ porta. N= No debe instalarse/no porta | Se consigna S si la UT debe instalársele un precinto electrónico o lo porta y N si la UT no debe instalársele o no lo porta. La opción N aplica cuando por Criterios de Riesgo no le corresponde portar precinto electrónico, la Aduana de Control lo autoriza a no portarlo o se supera el plazo de una hora hábil para ser autorizarlo por la Aduana. Además debe indicar en casilla de observaciones que la Aduana lo autorizó a no portar dicho dispositivo o no respondió a la solicitud del declarante, presentada mediante correo electrónico. |
| | | | | | | | | | | | | | | | | | | | | | | | | |
Datos de Actas de un Viaje (TRTMovPortActas)
| Este bloque solo aplica cuando el viaje se autoriza asociado a un acta Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación | Instructivo de llenado
| 1 | TRTACTID | Identificador del Acta | Num | 4 | C | Número asignado por el sistema al acta que se crea. Cuando el viaje se realice amparado a un acta, corresponde al número emitido por la autoridad competente.
| 2 | TRTACTOBS | Observaciones | Char | 500 | O | Se consignará la información del acta del viaje.
Datos del Contenedores o Guía aérea o Movimiento de Inventario (TRTMovPortCont) Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación | Instructivo de llenado |
1 | TRTMOVCONT | Corresponde al Número de contenedor o el número de secuenciador de cada guía aérea o el número de movimiento de inventario en depósito y los últimos 2 dígitos del año. | Char | 17 | O | Tratándose de ingreso marítimo: En la Creación de los viajes se deberá consignar el número de contenedor o Unidad de Transporte. Tratándose de ingreso aéreo: En la Creación de los viajes se deberá consignar el secuenciador (número asignado por el sistema a la guía aérea). Tratándose de movilización de mercancías entre depositarios aduaneros de la misma jurisdicción: En la Creación de los viajes se deberá consignar el número de movimiento de entrada al depósito Fiscal y los 2 |
| Para viajes asociados a operativa terrestre este dato corresponden al número de secuenciador dado por el Tica a cada una de las cartas de porte asociadas al manifiesto. | últimos dígitos del año indicados al final del número de movimiento de inventario. (Ejemplo: si el inventario es el 8025 y es el año 2005, entonces el valor indicado debe ser 802505). Para efectuar las operaciones de salida y llegada de los viajes en las instalaciones de los auxiliares se deberá consignar el número de contenedor en el se movilizan las mercancías. Tratándose de ingreso terrestre con manifiestos de carga, en la creación de los viajes se deberá consignar el secuenciador (numero asignados por el sistema a la carta de porte). |
| 2 | TRTMOVTOTBUL | Cantidad de bultos que se rebajarán del movimiento de inventario de entrada a depósito. | Num | 18.3 | C | Este debe ser menor o igual a la cantidad de bultos registrados en el movimiento de entrada a depósito. | Se consignará la cantidad de bultos que se van a trasladar en el viaje según el movimiento de inventario indicado en el campo TrtMovCont. Este campo es obligatorio cuanto se realice la creación contra movimientos de inventario en depósito. |
| 3 | TRTMOVCSOLPERM | Solicitud de Permanencia a Bordo | Char | 1 | C | Se consignará S si se requiere permanencia a bordo. |
| 4 | TRTMOVCODSOLPERM | Código Solicitud de Permanencia a Bordo | Char | 2 | C | Obligatorio si se solicita Permanencia a Bordo | Corresponde al código que identifica el tipo de mercancía autorizada para la permanencia a bordo. |
| 5 | TRTMOVCSOLPERMJUSTI | Justificación Permanencia a Bordo | Char | 100 | C | Obligatorio si se solicita Permanencia a Bordo | Corresponde a la justificación dada por el auxiliar del por qué de la Permanencia a Bordo |
| Datos de los Precintos (TRTMovPortPrec) Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación | Instructivo de llenado |
| 1 | TRTMOVPRC | Precinto | C | 15 | C | Se consignará el número de precinto que trae la Unidad de Transporte asociada al Viaje. |
| 2 | TRTMOVPRCTPO | Tipo de Precinto | C | 1 | O | Se consigna los siguientes códigos según el tipo de precinto que porte la UT. P : Precinto Metálico (lata) S: Precinto de Seguridad (botella) E: Precinto Electrónico. N: Cuando la UT por sus características no puede utilizar precinto. |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
Bloques del Mensaje de Respuesta:
Datos del Mensaje de Respuesta (TRTMOVRESPUUESTA) Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación | Instructivo de llenado
1 | TRMOVRESCODIGO | Código del Resultado | C | 4 | O | Se consigna el código de respuesta resultante de la carga del mensaje
2 | TRMOVRESDESC | Descripción del Resultado de la carga | C | 254 | O | Corresponde a la descripción del resultado de la carga del mensaje. (ver Lista de Códigos de resultado de la carga)
3 | TRMOVJID | Número de Viaje | N | 16 | C | Se consigna el numero de viaje resultante o bien el número de viaje al que está asociado el mensaje.
4 | TRMOVCONT | Numero de Contenedor | C | 17 | O | Indicará el número de contenedor declarado en el mensaje cuando es operativa marítima, para las demás este valor será nulo.
5 | TRMOVNUMPERABORD | Número solicitud de Permanencia a Bordo | N | 8 | O | Se consigna en caso de ser una respuesta a un mensaje de llegada o entrada a recinto con solicitud de permanencia a bordo, el número asignado a dicha solicitud.
| | | | | | | | | | | | |
Ejemplo de mensaje de Solicitud de Creación de Viaje
(Operativa marítima)
<?xml version=”1.0” encoding=”ISO-8859-1”?>
<ROOT xmlns=”http://www.hacienda.go.cr/TICA” xmlns:xsi=”http://www.w3.org/2001/XMLSchema-instance”>
<ROWSET_TRTMOVPORTON>
<ROW_TRTMOVPORTON NUM=”1”>
<TRTVJID>0</TRTVJID>
<TRTMOVORD>1</TRTMOVORD>
<TRTMOVRCT>P002</TRTMOVRCT>
<TRTENTSAL>S</TRTENTSAL>
<TRTMOVPAISTRANS>188</ TRTMOVPAISTRANS>
<TRTMOVTRANSIDTIPO>J</TRTMOVTRANSIDTIPO>
<TRTMOVTRANSID>1911425</TRTMOVTRANSID>
<TRTMOVCHOFERIDTIPO>P</TRTMOVCHOFERIDTIPO>
<TRTMOVCHOFERID>1841491</TRTMOVCHOFERID>
<TRTMOVCHOFERNOMBRE>Bruno Diaz</TRTMOVCHOFERNOMBRE>
<TRTNACMAT>188</TRTNACMAT>
<TRTMOVMAT>CR-2010</TRTMOVMAT>
<TRTMOVMATR>CR-2011</TRTMOVMATR>
<TRTMOVMATZ>CR-2011</TRTMOVMATZ>
<TRTMOVPESO>340</TRTMOVPESO>
<TRTMOVBULT>1</TRTMOVBULT>
<TRTRTADST>A158</TRTRTADST>
<TRTMOVCGTPOTRANS>1</TRTMOVCGTPOTRANS>
<TRTMOVCGTPOMIC>0</TRTMOVCGTPOMIC>
<TRTMOVCGNROMIC>AUX</TRTMOVCGNROMIC>
<TRTMOVCGFCHARR>2004-11-15</TRTMOVCGFCHARR>
<ROWSET_TRTMOVPORTACTAS>
<ROW_TRTMOVPORTACTAS NUM=”1”>
<TRTACTID>1</TRTACTID>
<TRTACTOBS>Solicitud de creación de viaje</TRTACTOBS>
</ROW_TRTMOVPORTACTAS>
</ROWSET_TRTMOVPORTACTAS>
<ROWSET_TRTMOVPORTCONT>
<ROW_TRTMOVPORTCONT NUM=”1”>
<TRTMOVCONT>ITLU-753011-0</TRTMOVCONT>
</ROW_TRTMOVPORTCONT>
</ROWSET_TRTMOVPORTCONT>
<ROWSET_TRTMOVPORTPREC>
<ROW_TRTMOVPORTPREC NUM=”1”>
<TRTMOVPRC>Presinto1</TRTMOVPRC>
</ROW_TRTMOVPORTPREC>
</ROWSET_TRTMOVPORTPREC>
</ROW_TRTMOVPORTON>
</ROWSET_TRTMOVPORTON>
</ROOT>
Ejemplo de mensaje de Llegada de un Viaje
(Cuando se indica fecha de descarga y solicitud de permanencia a bordo)
<?xml version=”1.0” encoding=”ISO-8859-1”?>
<ROOT xmlns=”http://www.hacienda.go.cr/TICA” xmlns:xsi=”http://www.w3.org/2001/XMLSchema-instance”>
<ROWSET_TRTMOVPORTON>
<ROW_TRTMOVPORTON NUM=”1”>
<TRTVJID>2006251</TRTVJID>
<TRTMOVORD>1</TRTMOVORD>
<TRTMOVRCT>A158</TRTMOVRCT>
<TRTENTSAL>E</TRTENTSAL>
<TRTMOVPAISTRANS>188</TRTMOVPAISTRANS>
<TRTMOVTRANSIDTIPO>F</TRTMOVTRANSIDTIPO>
<TRTMOVTRANSID>12345</TRTMOVTRANSID>
<TRTMOVCHOFERIDTIPO>P</TRTMOVCHOFERIDTIPO>
<TRTMOVCHOFERID>1841491</TRTMOVCHOFERID>
<TRTMOVCHOFERNOMBRE>Bruno Diaz</TRTMOVCHOFERNOMBRE>
<TRTNACMAT>340</TRTNACMAT>
<TRTMOVMAT>HN-2010</TRTMOVMAT>
<TRTMOVMATR>HN-2011</TRTMOVMATR>
<TRTMOVMATZ>TR-2011</TRTMOVMATZ>
<TRTMOVPESO>340</TRTMOVPESO>
<TRTMOVBULT>1</TRTMOVBULT>
<TRTRTADST>A158</TRTRTADST>
<TRTMOVFCHDESCARGA>2004-09-23T03:20:00</TRTMOVFCHDESCARGA>
<ROWSET_TRTMOVPORTACTAS>
<ROW_TRTMOVPORTACTAS NUM=”1”>
<TRTACTOBS>esta es un acta de llegada del un viaje</TRTACTOBS>
<TRTACTID>1</TRTACTID>
</ROW_TRTMOVPORTACTAS>
</ROWSET_TRTMOVPORTACTAS>
<ROWSET_TRTMOVPORTCONT>
<ROW_TRTMOVPORTCONT NUM=”1”>
<TRTMOVCONT>MOLU-273637-2</TRTMOVCONT>
<TRTMOVCSOLPERM>S</TRTMOVCSOLPERM>
<TRTMOVCODSOLPER>01</TRTMOVCODSOLPER>
< TRTMOVCSOLPERMJUSTI>SE REQUIERE DE UN
REMOLCADOR ESPECIAL PARA BAJAR LA CARGA DEL CONTENDOR</ TRTMOVCSOLPERMJUSTI>
</ROW_TRTMOVPORTCONT>
</ROWSET_TRTMOVPORTCONT>
<ROWSET_TRTMOVPORTPREC>
<ROW_TRTMOVPORTPREC NUM=”1”>
<TRTMOVPRC>Presinto1</TRTMOVPRC>
</ROW_TRTMOVPORTPREC>
</ROWSET_TRTMOVPORTPREC>
</ROW_TRTMOVPORTON>
</ROWSET_TRTMOVPORTON></ROOT>
Ejemplo de mensaje de Anulación de un Viaje
(El estado de viaje debe ser INI y no debe estar asociado a un DUA)
<?xml version="1.0" encoding="ISO-8859-1"?>
<ROOT xmlns="http://www.hacienda.go.cr/TICA" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<ROWSET_TRTMOVPORTON>
<ROW_TRTMOVPORTON NUM="1">
<TRTVJID>200688</TRTVJID>
<TRTMOVORD>1</TRTMOVORD>
<TRTMOVRCT>P005</TRTMOVRCT>
<TRTENTSAL>D</TRTENTSAL>
<TRTMOVPAISTRANS>188</TRTMOVPAISTRANS>
<TRTMOVTRANSIDTIPO>J</TRTMOVTRANSIDTIPO>
<TRTMOVTRANSID>301208034704</TRTMOVTRANSID>
<TRTMOVCHOFERIDTIPO>F</TRTMOVCHOFERIDTIPO>
<TRTMOVCHOFERID>103720526</TRTMOVCHOFERID>
<TRTMOVCHOFERNOMBRE>Mirando Q Gerardo</TRTMOVCHOFERNOMBRE>
<TRTNACMAT>320</TRTNACMAT>
<TRTMOVMAT>GT-2010</TRTMOVMAT>
<TRTMOVMATR>GT-2011</TRTMOVMATR>
<TRTMOVMATZ>FDT-013</TRTMOVMATZ>
<TRTMOVPESO>1000.000</TRTMOVPESO>
<TRTMOVBULT>1</TRTMOVBULT>
<TRTRTADST>A159</TRTRTADST>
<TRTMOVCGTPOTRANS>1</TRTMOVCGTPOTRANS>
<TRTMOVCGTPOMIC>0</TRTMOVCGTPOMIC>
<TRTMOVCGNROMIC>20050021</TRTMOVCGNROMIC>
<TRTMOVCGFCHARR>2005-07-28</TRTMOVCGFCHARR>
<ROWSET_TRTMOVPORTCONT>
<ROW_TRTMOVPORTCONT NUM="1">
<TRTMOVCONT>AMFU-854358-5</TRTMOVCONT>
</ROW_TRTMOVPORTCONT>
</ROWSET_TRTMOVPORTCONT>
<ROWSET_TRTMOVPORTPREC>
<ROW_TRTMOVPORTPREC NUM="1">
<TRTMOVPRC>00444400</TRTMOVPRC>
</ROW_TRTMOVPORTPREC>
</ROWSET_TRTMOVPORTPREC>
</ROW_TRTMOVPORTON>
</ROWSET_TRTMOVPORTON>
</ROOT>
Ejemplo de mensaje de Respuesta
<?xml version="1.0" encoding="ISO-8859-1" ?>
<ROOT xmlns="http://www.hacienda.go.cr/TICA">
<ROWSET_TRTMOVPORTONRESP>
E:\Documents and Settings\urenasl\Configuración local\Archivos temporales de Internet\avendanora\Configuración local\Van\TR\LOG_OUT\0535Crea Nuevo viajeEJ1.TRS - # <ROW_TRTMOVRESPUUESTA NUM="1">
<TRMOVRESCODIGO>4000</TRMOVRESCODIGO>
<TRMOVRESDESC>Carga Exitosa</TRMOVRESDESC>
<TRMOVJID>2006251</TRMOVJID>
<TRMOVCONT>TRLU-152534-3</TRMOVCONT>
</ROW_TRTMOVRESPUUESTA>
</ROWSET_TRTMOVPORTONRESP>
</ROOT>
