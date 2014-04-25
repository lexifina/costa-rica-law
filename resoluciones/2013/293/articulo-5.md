5. Comuníquese a las aduanas, Procomer, Auxiliares de la Función Pública Aduanera en sus casilleros electrónico por medio de la VAN y a los Desarrolladores del Software certificados del Sistema TICA.
[imagen]
Mensaje para el envío de Solicitud
Este mensaje permitirá al declarante enviar al TICA la información de las solicitudes de operación en sus instalaciones. Para el caso de solicitudes de Reempaque y Distribución el mensaje deberá ser emitido por el agente aduanero.
Para Donaciones, Destrucciones, Mermas o Reciclaje de mercancías bajo los regímenes de Zonas Francas y Perfeccionamiento Activo, Traslado de mercancías a depósito aduanero, Traslado de sobrantes de bultos; el mensaje podrá ser enviado por la propia empresa beneficiaria o una agencia de aduanas, y existirá una respuesta de parte del TICA.
Nombre de los archivos
Los archivos deben venir nombrados según el siguiente estándar:
Los nombres de los archivos enviados por el declarante tendrán la siguiente estructura de nombre:
<Casilla destino>-<nombre>.<extensión>, donde
<Casilla destino> : Corresponde a los 4 dígitos identificadores de la casilla destino dentro de la VAN. En este caso será la casilla asignada al TICA.
<nombre> : Corresponde a un nombre asignado por el declarante al archivo.
<extensión> : Identifica el tipo de archivo enviado al TICA. En este caso será “sks”.
Los nombres de los archivos de respuesta que recibirá el declarante tendrán la siguiente estructura de nombre:
<Casilla origen>-<ID transacción>-<Casilla destino>-<nombre>.<extensión>, donde
<Casilla origen> : Corresponde a los 4 dígitos identificadores de la casilla origen dentro de la VAN. En este caso será la casilla asignada al TICA. Colocado por la VAN.
<ID transacción> : Corresponde a un identificador único asignado al mensaje por parte de la VAN. Colocado por la VAN.
<Casilla destino> : Corresponde a los 4 dígitos identificadores de la casilla destino dentro de la VAN. En este caso será la casilla asignada al declarante.
<nombre> : Corresponde a un nombre asignado por el declarante al archivo original.
<extensión> : Identifica el tipo de archivo recibido por el declarante. En este caso será “ska”.
Tomar nota que los guiones separadores de cada componente del nombre de los archivos son obligatorios.
Detalle del mensaje para intercambio de datos
A continuación se listan las tablas con los diferentes registros que componen un mensaje, detallando los campos que los componen.
Significado de las columnas de las tablas
Campo: Número secuencial para identificar los campos dentro de cada registro o bloque.
Nombre: Nombre del campo que debe ser utilizado en la confección del archivo XML. Los nombres señalados con un asterisco (*) pertenece a la llave primaria.
Descripción: Indicación del significado del campo.
Tipo: Definición del tipo de dato correspondiente al campo.
Largo: Tamaño del campo. Se debe utilizar “el punto“ como separador decimal. Ej. Num 4.2 corresponde a un formato 99.99
O/C: Indica si el campo es Obligatorio o Condicional.
Validación: Indica el nombre de las tablas que contienen los valores utilizados en el campo, o puede indicar restricciones aplicables al campo.
Instructivo de llenado: Instrucciones básicas para completar el mensaje de intercambio de información.
Tipo de Operaciones sobre Inventarios
CODIGO | DESCRIPCION | DECLARANTE (YSKMENGAR) | UBIC. DE LA MERCANCIA (YSKSOLDEP) | UBICACIÓN DESTINO (YSKSOLUBIDEST) | CÓDIGO DE AUTORIZACIÓN
B | Reciclaje | 1004, 1015, 1025 | G, | No requerida |
C | Saldo Inicial PA | 1004, 1015 | G | No requerida |
D | Destrucción | 1004, 1015, 1025 | G, H | No requerida |
M | Movilizaciones | 1004, 1015, 1025, 1051 | A | A,H, G | 0322
N | Donación | 1004, 1015, 1025 | G, H | No requerida |
P | Traspaso o Préstamo mercancía PA | 1004, 1015 | G | G | 0324
Q | Merma | 1004, 1015 | G | No requerida |
R | Reempaque y Distribución | 1004 | A | No requerida |
T | Traslado | 1004, 1023, 1025, 1051 | H | A | 0310
Z | Sobrante | 1004, 1015, 1025 | G, H | A |
Datos de Control (YSKDATMEN)
Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación | Instructivo de llenado
1 | YSKMENCAS* | Casilla a la cual responder Mensaje* | Char | 4 | O | | Se consignará el número de casillero electrónico del declarante, dado por la Red de Valor Agregado (conocido por sus siglas en inglés como VAN).
2 | YSKMENNRO* | Numero del mensaje* | Char | 14 | O | Mayor que cero, Número del mensaje (dado por el Agente) | Se consigna el número de envío asignado por el declarante a la operación que está llevando a cabo. Para cada Declarante debe ser un secuencial único durante el año, por lo que deberá reinicializarse al comenzar un nuevo año. En caso de error se podrá utilizar el mismo número, pero una vez validado el mensaje por el sistema no podrá repetirse.
3 | YSKMENFCH | Fecha de envío del mensaje | Date | 10 | O | Es obligatorio, <= hoy AAAA-MM-DD | Se registra la fecha registrada en el sistema.
4 | YSKMENHOR | Hora de envío mensaje | Char | 8 | O | Es obligatorio HH:MM:SS | Se registra la hora registrada en el sistema.
5 | YSKMENVAN | Van que envía el mensaje | Char | 4 | O | Debe venir en mayúscula | Código de VAN
6 | YSKMENGAR | Identificación legal de la agencia/declarant e que envía el mensaje | Char | 12 | O | | Se consignará el número de identificación legal de la agencia de aduanas en caso de que el agente pertenezca a una agencia específica. Si el agente no pertenece a una agencia se consigna la misma identificación del Agente. Las empresas de ZF y PA consignarán su propia identificación legal, cuando sea la propia empresa la que declara y envía el mensaje Los responsables del envío de este mensaje aplica de la siguiente forma: B: Reciclaje empresa de ZF y PA o agente de aduanas. C. Carga Inicial: agente de aduanas o empresa de PA D: Destrucción empresa de ZF y PA o agente de aduanas. M: Movilización entre depósitos aduaneros: agente de aduanas o agencia de aduanas autorizada para declarar tránsito o transportista nacional terrestre o empresas de zonas francas, si se trata de mercancías ingresadas al régimen de ZF que se localizan en un depósito aduanero. N: Donación empresa de ZF y PA o agente de aduanas. R: Reempaque y Distribución solo agente de aduanas T: Traslado de ZF: agente de aduanas, agencia de aduanas autorizada para declarar tránsito, transportista nacional terrestre y empresa de ZF. P: Autorización de traspaso o préstamo de mercancías de PA agente de aduanas o empresa de PA. Q: Reporte de Mermas de PA. Agente de aduana o la empresa de PA Z: Sobrante de ZF/PA agente de aduanas o empresa de ZF y PA.
7 | YSKMENAGE | Número de identificación legal del agente/declarante que envía el mensaje | Char | 12 | O | | Se consignará el número de documento de identificación legal del agente de aduanas responsable de la solicitud En el caso de ZF y PA se consigna la identificación del empleado de la empresa; cuando sea la propia empresa la que declara y envía el mensaje de solicitud. Para las identificaciones de tipo P o R deberá se consignará los primeros 12 dígitos del número. Los responsables del envío de este mensaje aplica de la siguiente forma: B: Reciclaje empresa de ZF y PA o agente de aduanas. R: Reempaque y Distribución solo agente de aduanas D: Destrucción empresa de ZF y PA o agente de aduanas. N: Donación empresa de ZF y PA o agente de aduanas. Z: Sobrante de ZF/PA agente de aduanas o empresa de ZF y PA. T: Traslado de mercancías de ZF a depósito aduanero. Traslado de ZF: agente de aduanas, agencia de aduanas autorizada para declarar tránsito, transportista nacional terrestre y empresa de ZF. M: Movilización entre depósitos aduaneros: agente de aduanas o agencia de aduanas autorizada para declarar tránsito, o transportista nacional terrestre o empresa de zonas francas, si se trata de mercancías bajo el régimen de ZF que se localizan en un depósito aduanero. P: Autorización de traspaso o préstamo de mercancías de PA agente de aduanas o empresa de PA. Q: Reporte de Mermas de PA. Agente de aduana o la empresa de PA
Encabezado de la Solicitud de Operación (YSKSOLAUT)
Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación | Instructivo de llenado
1 | YSKSOLDEP* | Depósito | Char | 4 | O | Aplica únicamente para ubicaciones tipo A/H/D/G y con autorización para el proceso de operación. Utilizar tabla “Ubicaciones” | Se consignará el código asignado al depósito aduanero/empresa de ZF o PA donde se localiza las mercancías.
2 | YSKSOLNRO* | Número de Solicitud | Num | 8 | O | | Número interno que asigna el agente de aduanas o empresa de ZF o PA a la solicitud, preferiblemente debe ser consecutivo por año.
3 | YSKSOLTPODOC | Tipo de Identificación | Char | 1 | O | No aplica en tipo de solicitud: R | Se debe consignar el código del tipo de identificación legal (cédula jurídica o física) de la empresa de ZF/PA responsable de la solicitud. Cuando el tipo de solicitud es M, se consigna el código del tipo de identificación del consignatario del movimiento de inventario.
4 | YSKSOLNRODOC | No.de Identificación | Char | 12 | O | No aplica en tipo de solicitud: R | Se debe consignar el número de identificación legal (cédula jurídica o física) de la empresa de ZF/PA. Para tipo de solicitud M se consigna el número de identificación del consignatario de las mercancías en el movimiento de inventario.
5 | YSKSOLFCH | Fecha Estimada de operación | Date | 8 | O | AA-MM-DD No aplica en tipo de solicitud: Z, T, M, P, Q y C | Fecha estimada para el inicio de la operación, la cual debe ser un día hábil de operación de la aduana de control.
6 | YSKSOLHOR | Hora Estimada de operación | Char | 8 | O | HH:MM:SS No aplica en tipo de solicitud: Z, T, M, P, Q y C | Hora estimada para iniciar la operación, la cual debe estar al menos dos horas antes del horario de finalización de operación de la aduana de control
7 | YSKTPOPERA | Tipo de Solicitud | Char | 1 | O | | Se consignará el tipo de operación de solicitud: B: Reciclaje empresa de ZF y PA o agente de aduanas. C: Carga Inicial materia prima PA D: Destrucción de ZF/PA M: Movilización de mercancías sometidas al régimen depósito fiscal 80-16 N: Donación de ZF/PA P: Autorización de traspaso o préstamo de mercancías de PA Q: Reporte de Mermas de PA R: Reempaque y Distribución T:Traslado de ZF 80-71 Z:Sobrante de ZF/PA
8 | YSKTPOMERCA | Tipo de mercancías | Char | 1 | C | Aplica únicamente cuando el Tipo de Solicitud es D o B realizadas por empresas de ZF/PA. | Se indicará si las mercancías son: P: perecedera N: No perecedera No aplica en tipo de solicitud: Z
9 | YSKSOLTDDEST | Tipo de Documento de identificación del beneficiario de la donación o reciclaje en ZF o PA | Char | 1 | C | En cado de tipo de solicitud N controla contra la categoría 1057 En caso de tipo de solicitud B controla contra la categoría 1069 | Se debe consignar el código del tipo de identificación del beneficiario de la donación o de la empresa responsable del reciclaje. Este campo aplica únicamente para las Donaciones o Reciclaje en ZF o PA.
10 | YSKSOLNDDEST | Número de Documento del Destinatario de la donación o reciclaje en ZF o PA | Char | 12 | C | C En caso de tipo de solicitud N controla contra la categoría 1057. En caso de tipo de solicitud B controla contra la categoría 1069 | Se debe consignar el número de identificación del beneficiario de la donación o de la empresa autorizada para reciclaje. Para el caso de beneficiarios autorizados por la municipalidad, consigna el número de identificación de la municipalidad. Este campo se debe declarar únicamente para las Donaciones o Reciclajes en ZF o PA.
11 | YSKSOLUBIDEST | Ubicación destino | Char | 4 | C | C Obligatorio para las solicitudes tipo T, M, Z y P | Se consignará el código asignado a la ubicación destino de las mercancías.
12 | YSKSOLOBS | Observaciones | Char | 1250 | C | Obligatorio en tipo de solicitud M | Se puede consignar cualquier tipo de información que le interese manifestar. Para el tipo de solicitud M es obligatorio consignar la justificación del motivo de la solicitud de movilización. Dicha solicitud solamente se podrá presentar en los casos que a continuación se detallan: Excepcionalmente mercancías destinadas a los regímenes de zona franca y perfeccionamiento activo. mercancías que ingresando amparadas a un conocimiento de embarque matriz (consolidado) se haya indicado en el conocimiento de embarque individualizado como lugar de destino final, una ubicación diferente a la seleccionada por el consignatario de mayor volumen. Mercancías ingresadas al amparo de una DTI.
Detalle de la Solicitud de Operación (YSKSOLAUT1)
Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación | Instructivo de llenado
1 | YSKSOLMOVNRO* | Número de Movimiento | Num | 15 | O | | Número del movimiento de inventario asignado por el responsable del depósito aduanero a la mercancía que va ser objeto de la operación solicitada. Para el caso de solicitudes de empresas de ZF, corresponde a un número consecutivo asignado por la propia empresa que identifica el tipo de mercancía objeto de los distintos tipos de solicitudes. Este secuencial debe comenzar en 1 todos los años
2 | YSKSOLMOVANO* | Año del Movimiento de Inventario | Num | 4 | O | | Año del movimiento de inventario asignado por el responsable del depósito aduanero a la mercancía que va ser objeto de la operación solicitada. En caso de ZF es el año de su propio secuencial.
3 | YSKSOLBUL | Cantidad de Bultos | Num | 18.3 | O | | Cantidad de bultos del movimiento de inventario que se van a emplear en el proceso de operación. En caso de solicitud de destrucción o donación en empresas de ZF y PA corresponde a las unidades físicas. Deberá consignarse las unidades físicas en los siguientes tipos de solicitudes: B: Reciclaje de ZF/PA C: Carga Inicial de PA D: Destrucción de ZF /PA N: Donación de ZF/PA T: Traslado de mercancías de ZF a depósito aduanero P: Autorización de traspaso o préstamo de mercancías de PA Q: Reporte de Mermas de PA
4 | YSKSOLTPOBUL | Tipo de bulto | Char | 3 | O | | Código de embalaje mínimo de las mercancías objeto de solicitud de tipo de operación.
5 | YSKSOLMOVPAR | Partida Arancelaria | Char | 10 | O | | Se consignará el código arancelario a nivel de diez caracteres, que corresponda a la mercancía declarada en la línea, de acuerdo al Sistema Arancelario Centroamericano (SAC), vigente al momento del registro y numeración del DUA.
6 | YSKSOLMOVDSC | Descripción Comercial | Char | 300 | O | | Se consignará la descripción de la mercancía incluida en la línea, entendiéndose como tal la denominación de las mismas en términos suficientemente claros y detallados.
7 | YSKSOLUNICAN | Cantidad Unidades Físicas | Num | 18.3 | O | No aplica en tipo de solicitud: R, Z y M | Se consignará la cantidad total de unidades físicas que se declaran en la línea, en términos del campo (Código Unidad Física).
8 | YSKSOLUNICOD | Código Unidades Físicas | Char | 3 | O | Tabla General 29 No aplica en tipo de solicitud: R, Z y M | Se consignará el código de la unidad física.
9 | YSKSOLPESBRU | Peso Bruto | Num | 18.3 | O | | Se consignará el peso bruto en kilogramos de las mercancías objeto del tipo de solicitud.
10 | YSKSOLFCHPA | Fecha de Ingreso a Régimen de PA | Date | 10 | C | Es obligatorio, <= hoy AAAA-MM-DD Obligatorio en C: Carga Inicial de PA | Consignar la fecha de internamiento de la de materia prima e insumos al Régimen de PA que debe corresponder a la fecha de aceptación.
11 | CADUREGPRE | Aduana del D.U.A./ documento precedente | Char | 3 | C | Utilizar tabla “Aduanas | Se consignará el código correspondiente a la aduana del DUA o del documento precedente.
12 | FANOREGPRE | Año del D.U.A/ Documento Precedente | Char | 4 | C | Obligatorio para una tipo de solicitud C de una empresa categoría 1015 | Se consignará el año de presentación del DUA de internamiento al Régimen de PA
13 | NDCLREGPRE | Número del D.U.A/ Documento Precedente | Char | 6 | C | Obligatorio para una tipo de solicitud C de una empresa categoría 1015 | Se consignará el número del DUA de internamiento al Régimen de PA
14 | TDOCREGPRE | Tipo de Documento Precedente | Char | 2 | C | Obligatorio para una tipo de solicitud C de una empresa categoría 1015 | Se consignará el código del tipo del documento precedente. 19 si es del TICA 01 si es del SIA 65 se es factura de compra local
15 | NUME_SERPR | No. Línea del D.U.A/ Documento Precedente | Char | 4 | C | Obligatorio para una tipo de solicitud C de una empresa categoría 1015 | Se consignará el número de línea correspondiente del al documento precedente
Mensaje de respuesta (YSKRESAUT)
Archivo con nomenclatura XXXXnnnn.SKA
Campo | Nombre | Descripción | Tipo | Largo
1 | YSKAUTRESSEC | Secuencial | Num | 8
2 | YSKSOLAGE | Agente que envió mensaje | Char | 12
3 | YSKSOLDEP | Depósito | Char | 4
4 | YSKSOLNRO | Número de solicitud | Num | 8
5 | YSKAUTAPR | Aprobación/ Solicita Documentación /Rechazo de autorización (A/D/ R) | Char | 1
6 | YSKAUTNRO | Número de autorización dado por el sistema ( si se aprobó la solicitud) | Num | 8
7 | YSKAUTPART | Indica S si el funcionario aduanero va a participar en el proceso de revisión o N cuando no participa | Char | 1
8 | YSKAUTFUN | Identificación del Funcionario aduanero asignado cuando hay participación aduanera | Char | 15
9 | YSKAUTOBS | Observaciones | Char | 200
10 | YSKAUTFCH | Fecha de Envío de la Respuesta (AAAA-MM-DD) | Num | 10
11 | YSKAUTHOR | Hora de Envío de la Respuesta (HH:MM:SS) | Char | 8
12 | YSKAUTCODERR | Código de Error | Char | 4
13 | YSKAUTDSCERR | Descripción del Error | Char | 254
14 | YSKAUTVALERR | Valor del campo donde ocurrió el error | Char | 400
15 | YSKAUTDEPDST | Depósito destino | Char | 4
Ejemplo: <?xml version = '1.0' encoding = 'ISO-8859-1' ?>
<ROOT xmlns="http://www.hacienda.go.cr/TICA" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<ROWSET_YSKDATMEN>
<ROW_YSKDATMEN NUM="1">
<YSKMENCAS>AGEN</YSKMENCAS>
<YSKMENNRO>17</YSKMENNRO>
<YSKMENFCH>2010-1129</YSKMENFCH>
<YSKMENHOR>14:00</YSKMENHOR>
<YSKMENVAN>VA</YSKMENVAN>
<YSKMENGAR>301200957727</YSKMENGAR>
<YSKMENAGE>12345671</YSKMENAGE>
</ROW_YSKDATMEN>
</ROWSET_YSKDATMEN>
<ROWSET_YSKSOLAUT>
<ROW_YSKSOLAUT NUM="1">
<YSKSOLDEP>2000</YSKSOLDEP>
<YSKSOLNRO>32</YSKSOLNRO>
<YSKSOLFCH>2010-11-29</YSKSOLFCH>
<YSKSOLHOR>08:20:00</YSKSOLHOR>
<YSKSOLOBS>NADA</YSKSOLOBS>
<YSKTPOPERA>D</ YSKTPOPERA>
<ROWSET_YSKSOLAUT1>
<ROW_YSKSOLAUT1 NUM="1">
<YSKSOLMOVNRO>9900550</YSKSOLMOVNRO> <YSKSOLMOVANO>2005</YSKSOLMOVANO>
<YSKSOLBUL>1.0</YSKSOLBUL>
<YSKSOLMOVDSC>PRUEBA</YSKSOLMOVDSC> <YSKSOLMOVPAR>010110</YSKSOLMOVPAR>
< YSKSOLFCHPA>2010-12-05</ YSKSOLFCHPA>
<CADUREGPRE>005</CADUREGPRE>
<FANOREGPRE>2010</FANOREGPRE>
<NDCLREGPRE>000123</NDCLREGPRE>
<TDOCREGPRE>19</TDOCREGPRE>
<NUME_SERPR>0001</NUME_SERPR>
</ROW_YSKSOLAUT1>
</ROWSET_YSKSOLAUT1>
</ROW_YSKSOLAUT>
</ROWSET_YSKSOLAUT>
</ROOT>
