DIRECCIÓN GENERAL DE ADUANAS
CIRCULAR DNP-096-2003
Señores
Jefes de División, Departamentos, Asesorías
Gerentes de Aduana, Depositarios Aduaneros,
Autoridades Portuarias
Funcionarios Servicio Nacional de Aduanas
ASUNTO: Traslado de inventarios de mercancías en Depósitos Aduaneros, instalaciones portuarias y bodegas de aduana al nuevo Sistema TICA
Estimados señores:
Como es de su conocimiento, el Servicio Nacional de Aduanas se encuentra realizando un ambicioso proyecto, dirigido al diseño e implementación de un nuevo modelo aduanero centralizado, caracterizado por la utilización de un formato único de declaración electrónica aduanera; que involucra tecnología avanzada y de fácil acceso a la base de datos, agiliza la integración de los procesos aduaneros, ejerce un mayor control de las operaciones aduaneras y posibilita la interacción con Auxiliares de la Función Pública aduanera, y demás instituciones involucradas en el comercio exterior.
Este nuevo modelo de gestión, denominado Tecnología de Información para el Control Aduanero (TICA), incluye los mecanismos necesarios para que las entidades estatales y las empresas privadas que forman parte del Sistema Aduanero Nacional, tengan además un rápido acceso a la información y puedan realizar trámites y consultas las 24 horas del día, los 365 días del año.
El Servicio Nacional de Aduanas proyecta para que a partir de finales del mes de abril del 2004, se inicie la implantación paulatina del nuevo modelo, lo que necesariamente conlleva, el tratamiento adecuado de la información que se encontrase vigente a esa fecha, en las bases de datos del SIA y que deben trasladarse al nuevo sistema de gestión TICA.
Como es sabido, en la actualidad el registro y control de los inventarios de mercancías que se encuentran en las instalaciones de los Depósitos Aduaneros, Bodegas de Aduana y Zonas Portuarias, es manejado en los módulos SALF y OPEM del Sistema de Información Aduanera (SIA). La etapa para el traslado hacia TICA, de los datos relacionados con los inventarios, está prevista para desarrollarse gradualmente en las diferentes aduanas, a partir del mes de marzo del 2004. Para estos efectos, el día 5 de diciembre recién pasado se entregaron a las empresas desarrolladoras de software, los formatos y estructuras requeridas para la declaración ante aduana de las operaciones ejecutadas en el mantenimiento de inventarios en las instalaciones de los depositarios aduaneros.
Lo anterior se considera fundamental, a efectos de proseguir con la siguiente etapa del proyecto, sea la implantación del procedimiento de importación, de manera tal, que al momento en que se implemente dicho procedimiento, cada aduana cuente con los inventarios de mercancías actualizados en el nuevo sistema para su sometimiento a cualquier régimen.
Esta Dirección General, dentro de las alternativas valoradas para el traslado de los datos, ha considerado fundamental que los depositarios aduaneros y las autoridades portuarias presenten los datos de los saldos disponibles, según sus registros, debidamente certificados y sujetos a posterior validación por parte de la aduana. Igualmente, las aduanas deberán proceder a levantar los inventarios de las mercancías que obran en sus bodegas.
Por ello, los depositarios aduaneros y las autoridades portuarias, deberán actualizar y presentar ante la aduana de su jurisdicción, los inventarios de las mercancías depositadas en sus recintos, cumpliendo el siguiente cronograma:
Entrega | Fecha
Entrega de inventarios actualizados para pruebas de certificación de cumplimiento del formato indicado. | 20 de febrero 2004
Entrega de inventarios preliminares. | 1º de abril 2004
Entrega de inventarios para carga inicial TICA - Aduana Central. (*) | 30 de abril 2004
Inventario para carga inicial TICA - Aduana Santamaría. (*) | 4 de junio 2004
Inventario para carga inicial TICA - Aduana Limón. (*) | 11 de junio 2004
Inventario para carga inicial TICA - Aduana Caldera. (*) | 11 de junio 2004
Inventario para carga inicial TICA - Aduana Peñas Blancas. (*) | 6 de agosto 2004
Inventario para carga inicial TICA - Aduana Paso Canoas. (*) | 6 de agosto 2004
(*) Estas entregas deben realizarse a más tardar a las 4:00 p. m. de la fecha indicada, reflejando las existencias de inventario reales a las 12: 00 m. d. de ese día, cuando se hará efectivo el cese de operaciones como paso previo al cambio de sistema. A partir de esta entrega se iniciará el procedimiento de carga de datos al nuevo sistema TICA.
Estos inventarios se presentarán impresos y en medio electrónico, cumpliendo el formato adjunto. En el contenido del inventario general, deberá indicarse, además de las mercancías que se encuentran dentro del plazo de depósito fiscal, las que están en las siguientes situaciones: abandono, sujetas a destrucción o donación, comisos y las que se encuentran en el régimen de reempaque y distribución.
A fin de garantizar la calidad y oportunidad de los inventarios presentados, cada aduana coordinará en forma directa, con los depositarios aduaneros y autoridades portuarias bajo su jurisdicción, las visitas de inspección y validación necesarias.
Esta Dirección General solicita, se cumpla a cabalidad con los requerimientos aquí planteados, caso contrario no será posible tramitar declaraciones a un régimen determinado, siendo responsabilidad del depositario o de la autoridad portuaria ante los usuarios finales la no remisión oportuna de la información requerida.
INTERCAMBIO DE INFORMACIÓN ENTRE LUGARES DE UBICACIÓN DE MERCANCÍAS Y LA DIRECCIÓN GENERAL DE ADUANAS Formato de Mensaje de Depósito VERSIÓN 1.O mensajesTica@hacienda.go.cr (c) Ministerio de Hacienda Ave 1 y 3, Calle Central, San José Tel. (506) 257-5069 · Fax (506) 233-1143
Detalle del mensaje para intercambio de datos
A continuación se listan las tablas con los diferentes registros que componen un mensaje, detallando los campos que los componen.
Significado de las columnas de las tablas:
Campo: Número secuencial para identificar los campos dentro de cada registro o bloque.
Nombre: Nombre del campo que debe ser utilizado en la confección del archivo XML. Los nombres señalados con un asterisco (*) pertenece a la llave primaria.
Descripción: Indicación del significado del campo.
Tipo: Definición del tipo de dato correspondiente al campo.
Largo: Tamaño del campo. Se debe utilizar "el punto" como separador decimal. Ej. Num 4,2 corresponde a un formato 99.99
O/C: Indica si el campo es Obligatorio o Condicional.
Operación: Indica el tipo de operación (según listado adjunto).
Validación: Indica el nombre de las tablas que contienen los valores utilizados en el campo, o puede indicar restricciones aplicables al campo.
Instructivo de llenado: Instrucciones básicas para completar el mensaje de intercambio de información.
Tipo de registro
A = Inclusión.
B = Eliminación. Será un borrado lógico (no se borra físicamente) y se deja no utilizable.
M = Modificación o agregado de información.
Tipos de operación
I = Ingreso
R= Registro del consignatario
E = Endoso
C = Cesión de derechos
F = Fraccionamiento
A = Agrupamiento
S = Registro de Sobrante
G = Registro de Faltante
T = Termina permanencia en contenedor
0 (cero) = Inventario Inicial
Campo | Nombre | Descripción | Tipo | Largo | 0/C | Operación | Validación | Instructivo de llenado
1 | YSKEntDep* | Código de Ubicación | Char | 4 | 0 | I, R, E, C, F, A, S, G, 0, T | . | Se consignará e) código asignado a la ubicación donde se recibe o localice la mercancía.
2 | YSKEntNro* | Número Movimiento de inventario de Entrada | Num | 15 | 0 | I,R,E,C,F, A, S, G, 0, T | Mayor que cero | Numero del movimiento de inventarío asignado por el responsable de la ubicación, para registrar el ingreso de la mercancía, operaciones del régimen de reempaque y distribución, cesión de derechos, endosos, registro del consignatario, sobrantes y faltantes, termino de permanencia de mercancía en contenedor y carga de inventarlo inicial de registros de SAIF.
3 | YSKEntAno* | Afta Movimiento de Inventario de Entrada | Num | 4 | 0 | I, R, E, C, F, A,S,G,0,T | Mayor que cero. Debe corresponder al año del movimiento que se desea registrar. Debe ser menor o igual al año actual | Año del movimiento de inventario asignado por el responsable de la ubicación, para registrar el ingreso de la mercancía, operaciones del régimen de reempaque y distribución, cesión de derechos, endosos, registro del consignatario, sobrantes y faltantes, termino de permanencia de mercancía en contenedor y carga de inventarlo inicia! de registros de SALF.
4 | YSKEntTpoTra | Modalidad de Transporte | Char | 3 | C | I | Es obligatorio si tipo Documento = Manifiesto y Tipo Operación = I Cuando el documento de carga corresponda a un manifiesto se completarán los campos 4 al 10. | Se consignará el código de la modalidad de transporte mediante el cual ingresaron las mercancías a territorio aduanero, 1 se trata de ingreso marítimo y 4 si se trata de ingreso aéreo.
5 | YSKEntTpoMic | Tipo de Manifiesto | Char | 1 | C | I | Es obligatorio si Tipo Documento = Manifiesto y Tipo Operación = I | Se consignará "0" si es un manifiesto de ingreso, o "1" si es un manifiesto de salida.
6 | YSKEntNroMic | Número de manifiesto | Char | 8 | C | I | Es obligatorio si tipo Documento = Manifiesto y Tipo Operación =I | Número de viaje o escala en ingreso marítimo o el número de vuelo en ingreso aéreo, que será conformado por ocho caracteres: dos correspondientes al código de la línea aérea y seis correspondientes al número de vuelo.
7 | YSKRgDepId | Código de ubicación de ingreso | Char | 4 | C | I | Es obligatorio si tipo Documento = Manifiesto y Tipo Operación = 1 | Se consigna el código de ubicación asignado al puerto o aeropuerto de ingreso de las mercancías.
8 | YSKEntFchArr | Fecha Estimada de Arribo | Date | 10 | C | I | Es obligatorio si tipo Documento = Manifiesto y Tipo Operación =1 Formato: AAAA-MM-DD (Referencia: estándar XML) | Se consignará la fecha estimada de arribo de la nave al puerto o aeropuerto consignada en el manifiesto.
Campo | Nombre | Descripción | Tipo | Largo | 0/C | Operación | Validación | Instructivo de llenado
9 | YSKEntNroCon | Número de Referencia del Conocimiento de Embarque | Char | 25 | C | I | Es obligatorio si tipo Documento = Manifiesto y Tipo Operación = I | Se consignaré el número correlativo que el sistema asigna a cada conocimiento de embarque individualizado. Tratándose de un sobrante de bultos consigna la palabra desconocido.
10 | YSKEntNroLin | Número de Línea del Conocimiento de Embarque. | Num | 3 | C | 1 | Es obligatorio si tipo Documento = Manifiesto y Tipo Operación = I | Número que identifica la línea en un conocimiento de embarque y que corresponde al asignado por el sistema en el ingreso.
11 | YSKEntDocTpo | Tipo de Documento de Ingreso | Char | 2 | C | I,A,F,S,G | Es obligatorio si tipo Operación = I, A, F, S o G. | Se consignará el código del documento de ingreso de las mercancías al lugar de ubicación. Cuando el tipo de documento corresponda a: -un manifiesto deberá completarse los campos del 4 al 10 -DUA tránsito o autorización de reempaque y distribución deberá completar los campos de 12 al 15. -Otros tipo de documentos, deberé completar los campos de 12 al 14.
12 | YSKEntDocAdu | Código de Aduana. | Char | 3 | C | I,S. G | Es obligatorio si tipo Documento es diferente de manifiesto y Tipo Operación = l, S o G | Se consignará el código de la aduana que emitió el DUA de tránsito. Para otro tipo de documentos de ingreso se consignará el código de la aduana de jurisdicción del lugar de ubicación de las mercancías.
13 | YSKEntDocAno | Año del Documento | Num | 4 | C | I,S,G | Es obligatorio si tipo documento es diferente de Manifiesto y Tipo Operación = I, S o G. Debe ser mayor que cero y menor o igual al año actual | Se consignará el año del documento que autoriza la inclusión del movimiento de inventario.
14 | YSKEntDocNro | Número del Documento de Ingreso | Char | 6 | C | 1.8,0 | Es obligatorio si tipo documento es diferente de Manifiesto y Tipo Operación | Se consignará el número del documento de Ingreso de las mercancías al lugar de ubicación.
Campo | Nombre | Descripción | Tipo | Largo | 0/C | Operación | Validación | Instructivo de llenado
. | . | . | . | . | . | . | = 1, S, o G Debe ser mayor que cero. | .
15 | YSKEntDocLin | Número de Línea | Char | 4 | C | I,S, G | Obligatorio si tipo de documento = DUA | Se consignará el número de línea de mercancías descrita en el DUA de tránsito y en la autorización de reempaque y distribución.
16 | YSKEntFchRea | Pecha Ingreso a lugar de Ubicación | Date | 10 | C | I | Obligatorio cuando tipo operación es 1. Formato AAAA-MM-DD | Se consignará la fecha de ingreso de la mercancía al lugar de ubicación.
17 | YSKEntPchReg | Fecha Ingreso al Régimen | Date | 10 | C | I,O | Obligatorio cuando tipo operación es l, O y si el tipo de documento que ampara el ingreso de la mercancía no es un DUA Tratándose de una modificación de este campo y el documento de ingreso distinto de DUA, se utilizará el tipo de registro = M y la fecha debe ser menor a la consignada en el mensaje anterior. Formato AAAA-MM-DD | Se consignará la fecha de ingreso de la mercancía al régimen, en caso de no consignarse el sistema asignará la fecha de día. Tratándose del envió del inventario inicial deberá corresponder a la fecha de ingreso al régimen registrada en el sistema SALF, para cada uno de los registros.
18 | YSKEntPesBru | Peso Bruto | Num | 18,3 | C | I,C,F,A,S, G,O | Es obligatorio y mayor que cero si Tipo de Operación es diferente de R, E. | Se consignará el peso total en kg. de las mercancías incluyendo el embalaje,
19 | YSKEntPesNet | Peso Neto | Num | 18.3 | C | I,C,F,A,S, G | Es obligatorio y mayor que cero si Tipo de Operación es diferente de R, E. | Se consignará el peso neto total! en kg. de la mercancía.
20 | YSKEntTpoBul | Tipo de Bulto | Char | 3 | C | I, C, F, A, S, G,O | Es obligatorio si tipo Registro = A y Tipo de Operación es diferente de R, E, | Código de embalaje mínimo asociado a la línea de la mercancía.
21 | YSKEntTotBui | Cantidad Total de Bultos | Num | 18,3 | C | I, C, F, A, S, G,0 | Es obligatorio y mayor que cero si Tipo Registro = A y Tipo de Operación es diferente de R, E. | Se consignará por línea de mercancía el número total de bultos recibidos. Esta cantidad se obtendrá como producto de la tarea de despaletización cuando corresponda. Sólo en caso de mercancía a granel aplica los decimales. En caso de registrar sobrantes y faltantes registrará la cantidad correspondientes.
22 | YSKEntNCM | Código Partida Arancelaria | Char | 10 | C | A,F | Obligatorio si tipo de operación es A o F | Se consignará el código de la partida arancelaria de las mercancías que se sometan al régimen de reempaque y distribución.
Campo | Nombre | Descripción | Tipo | Largo | 0/C | Operación | Validación | Instructivo de llenado
23 | YSKEntMarc | Marcas y Referencias de bultos | Char | 30 | C | I, C, F, A, S, G,O | . | Se consignará marcas, series y referencias de los bultos por línea de mercancía.
24 | YSKEntCndBul | Condición del Bulto | Char | 4 | C | I,O,S | Es obligatorio si tipo Operación =I, O o S o Tipo Registro = A | Se registrará la condición o estado de los bultos a su ingreso al lugar de ubicación 1 Perfecto estado, 2: Abierto 3: Saqueado 4: Dañada
25 | YSKEntDsc | Descripción de la Mercancía | Char | 300 | O | I,C,F,A,S, G,O | . | Se consignará la descripción de la mercancías por línea (marca, modelo, serie, entre otros datos).
26 | YSKEntMerPeI | Código de Mercancía Peligrosa | Char | 4 | C | I,C,F,A,S, G,O | Valida contra Tabla Tipo de mercancía peligrosa | Se consignará el código internacional por línea de mercancía.
27 | YSKEntTpoReg | Tipo de Registro | Cha | 1 | O | I, R, E, C, F, A, S, G, O | A= inclusión B = Eliminación. Será un borrado lógico (no se borra físicamente) y se deja no utilizable. M = Modificación o agregado de información. | Se anotará el código de registro asociado al tipo de operación sea A: inclusión en el sistema, M; modificación de un registro previamente ingresado, B: Eliminación de un registro existente.
28 | YSKEntCsgCDoc | Tipo de identificación legal del consignatario | char | 1 | C | R.E.C | Obligatorio si tipo Operación = C, E, R. | Se consignará el tipo de identificación legal del consignatario si se dispone de dicha información. En caso contrario será obligatorio previo a la importación, para lo que el representante del lugar de ubicación deberá enviar un mensaje con tipo de registro = M y tipo de operación = R para completar la información.
29 | YSKEntCsgNDoc | Identificación legal del consignatario | Char | 12 | C | R.E.C. | Es obligatorio si Tipo Operación = C, E, R | Se consignará la identificación legal del consignatario, si se dispone de dicha información. En caso contrario será obligatorio previo a la importación, para lo que el representante del lugar de ubicación deberá enviar un mensaje con tipo de registro = M y tipo de operación = R para completar la información. Tratándose de una identificación tipo P o R deberá consignarse los primeros 12 dígitos del número.
30 | YSKEntRSCsg | Nombre o Razón Social de! Consignatario | Char | 60 | O | I,R,E,C,F, A, S, G, O | | Se consignará el nombre de la persona física o jurídica a quien está consignada la mercancía, cuando no se haya declarado un RUC en los campos 27 y 28.
31 | YSKEnTpoOp | Tipo de Operación | Char | 1 | O | I,R,E.C,F, A, S, G,O, T | Valores posibles de este campo: I = Ingreso //R= Registro del | Se consignará el código de operación que se realiza dentro del lugar de ubicación. La T deberá enviarla el responsable de la ubicación al
Campo | Nombre | Descripción | Tipo | Largo | 0/C | Operación | Validación | Instructivo de llenado
. | . | . | . | . | . | . | consignatario // E = Endoso // C = Cesión de Derechos // F = Fraccionamiento // A= Agrupamiento) // S =Registro de Sobrante // G = Registro de Faltante//0 (cero) = Inventario Inicia) // T= Termina permanencia en contenedor. | vencimiento del plazo otorgado por la DGA para el desalmacenaje de mercancías autorizadas a permanecer en el contenedor, lo que implicará la eliminación del número de autorización dado por la aduana y texto de justificación enviados en el registro del ingreso.
32 | YSKEntFchEnd | Fecha de Endoso/ Cestón de derechos | Date | 10 | C | E,C | Obligatorio si tipo de operación es E o C. Debe ser posterior o igual a la fecha de ingreso y menor o igual a la fecha de hoy. | Se consigna la fecha de cuando se realizó el endoso o la cesión de derechos.
33 | YSKEntNroActa | Número de Autorización | Num | 8 | C | F,A,T | Obligatorio para el régimen de reempaque y distribución y comunicación de permanencia de mercancía a bordo de la UT, o sea, es obligatorio si Tipo de Operación = F, A, T y tipo de registro = A cuando se haya autorizado despacho a bordo. | Número de autorización que la aduana de control otorga a la solicitud de reempaque y distribución y a la permanencia de mercancías dentro de la UT.
34 | YSKEntTxtActa | Texto de la Solicitud de Corrección | Char | 100 | C | I, R. E, C, F, A, S, G, T | Obligatorio si tipo de registro = M o A cuando se haya autorizado despacho a bordo. | Se consignará una síntesis de la solicitud de corrección, o la frase "permanencia de la mercancía en la UT" para cuando haya sido autorizado por la aduana,
35 | YSKEntNroRef | Número de movimiento de inventario | Num | 15 | C | F,A,C,S,G | Es obligatorio si Tipo Operación = (F, A, C, S , G) Debe ser mayor que cero | Se consignará el número del movimiento de Inventario que se afecta por el tipo de operación que se le quiere realizar a las mercancías.
36 | YSKEntAnoRet | Ano del movimiento de inventario. | Num | 4 | C | F,A,C,S,G | Es obligatorio si Tipo Operación = (F, A, C, S, G) Debe ser mayor que cero y menor o igual al año actual | Se consignará el ano que tiene registrado et movimiento de inventario que se afecta por el tipo de operación que se le quiere realizar a las mercancías.
37 | VSKEntSulOpe | Cantidad de bultos utíHzados | Num | 18 | C | F,A,C | Obligatorio y mayor que cero si Tipo Operación = (F, A, C,) | Indica la cantidad de bultos utilizados del movimiento de inventario inicial que serán sometidos a los procesos del Régimen de Reempaque y Distribución o Cesión de Derechos.
38 | YSKEntCodAge | Identificación legal de! Agente | Char | 12 | C | A,F | Obligatorio y mayor que cero para Tipo de operación A, F. | Se consignará el número de identificación legal del agente de aduanas, que solicita el Régimen de Reempaque y Distribución.
39 | YSKEntProclld | Código de Producto | Char | 18 | C | I | Obligatorio para el tipo de mercancía que DGA haya establecido. | Se consignará el código de producto para mercancías específicas por línea de ingreso. (SE PROGRAMARA PERO NO SERÁ EXIGIDO POR EL MOMENTO).
Campo | Nombre | Descripción | Tipo | Largo | 0/C | Operación | Validación | Instructivo de llenado
40 | YSKEntObs | Observaciones | Char | 300 | C | I, R, E, C, F, A, S, G. O, T | . | Se consignará cualquier información adicional qué estime conveniente informar el responsable del lugar de ubicación.
41 | YSKEntCedFun | identificación del Funcionario Aduanero | Char | 12 | C | I | Es obligatorio si hubo participación de funcionario aduanero en la descarga. | Se consignará la identificación legal del funcionario aduanero, que participó en la supervisión de la descarga.
42 | YSKEntUniMec | Unidad de Medida | Char | 3 | O | I, F,A | Tabla de Unidad de Medida | Código de unidad de medida de tas mercancías. Ej. Kilogramos, litros, etc.
Salidas de Mercancías en Ubicación
En el caso de las salidas, todos los campos del bloque se utilizan para registrar la operación de salida y no existe otro tipo de operación, por eso se omite esta columna en la tabla.
Campo | Nombre | Descripción | Tipo | Largo | 0/C | Validación | Instructivo de llenado
1 | YSKSalDep* | Código de Ubicación* | Char | 4 | O | . | Se consignará el código asignado a la ubicación de donde sale la mercancía.
2 | YSKSaINro* | Número Movimiento de Inventario Salida* | Num | 15 | O | Mayor que cero | Número del movimiento de inventario asignado por el responsable de la ubicación para registrar la salida de la mercancía.
3 | YSKSalAno* | Año Movimiento de Operación de Salida* | Num | 4 | O | Mayor que cero y debe corresponder al año actual | Año de! Movimiento de salida asignado por e! responsable de la ubicación, para registrar esta operación.
4 | YSKSalDocTpo | Tipo del documento de salida | Char | 2 | C | Es obligatorio si tipo de registro es A o M. | Se consignará el código del documento de salida de las mercancías del lugar de ubicación.
5 | YSKSalDocAdu | Código de Aduana | Char | 3 | C | Es obligatorio si tipo de registro es A o M. | Se consignará el código de la aduana que emitió el DUA que autoriza la salida de las mercancías. Para otro tipo de documentos de salida se consignará el código de la Aduana de Jurisdicción del lugar de ubicación de las mercancías.
6 | YSKSalDocAno | Año del documento de salida | Num | 4 | C | Mayor que cero Es obligatorio si tipo de registro es A o M. | Se consignará el año del documento que autoriza el movimiento de salida.
7 | YSKSalDocNro | Número del documento de salida | Char | 6 | C | Mayor que cero Es obligatorio si tipo de registro es A o M. | Se consignará e) número del documento de salida de las mercancías.
8 | YSKSalDocLin | Número de Línea | Char | 4 | C | Obligatorio si tipo de documento = DUA | Se consignará el número de línea que registra el DUA de autorización de salida.
9 | YSKSalTpoBul | Tipo de Bulto | Char | 3 | C | Es obligatorio si tipo de registro es A o M. | Código de embalaje mínimo asociado a la línea de salida de la mercancía.
10 | YSKSalTotBul | Cantidad Tota! de Bultos. | Num | 18.3 | C | Mayor que cero. Es obligatorio si Tipo Registro es A o M | Se consignará !a cantidad total de bultos por línea de mercancía que salen del lugar de ubicación. Sólo en caso de mercancía a granel aplica los decimales.
11 | YSKSalTpoReg | Tipo de Registro | Char | 1 | O | A: Inclusión en el sistema. M: Modificación de un registro previamente | Se anotará e! código de registro asociado al tipo de operación.
Campo | Nombre | Descripción | Tipo | Largo | 0/C | Validación | Instructivo de llenado
. | . | . | . | . | . | ingresado. B. Eliminación de un registro existente. | .
12 | YSKSalDepDst | Código de ubicación de Destino | Char | 4 | C | Es obligatorio si Tipo Documento = DUA de tránsito, VAD, Golfito / reexportación / exportación | Se consignará el código asignado al lugar de ubicación de destino de las mercancías. Tratándose de una exportación o reexportación el código de lugar de ubicación salida.
13 | YSKEntNro | Número Movimiento de inventarlo de Entrada | Num | 15 | C | Es obligatorio si tipo de registro = A, M | Número del movimiento de inventario que tienen registradas las mercancías a la entrada a la ubicación
14 | YSKEntAno | Año Movimiento de Inventario de Entrada | Num | 4 | C | Es obligatorio al tipo de registro = A, M | Ano del movimiento de inventario que tienen registradas las mercancías a la entrada a la ubicación.
15 | YSKSalFchReg | Fecha de Salida | Date | . | C | Formato AAAA-MM-OD Obligatorio en tipo de registro = A | Se consignará la fecha de la solicitud de la salida.
16 | YSKSalObs | Observaciones | Char | 80 | C | Es obligatorio si Tipo de Registro = B, M | Se consignarán cualquier información adicional que estime conveniente Informar el responsable de lugar de ubicación. Tratándose de una eliminación será siempre obligatorio indicando las razones por las cuales desea eliminar e! registro.
Datos para respuesta
Campo | Nombre | Descripción | Tipo | Largo | Validación
1 | YSKMenCas* | Casilla a la cual responder Mensaje* | Char | 4 | Es obligatorio
2 | YSKMenNro* | Numero del mensaje * | Char | 14 | Mayor que cero, Número del mensaje (dado por el Depositario)
3 | YSKMenFch | Fecha de envió del mensaje | Date | 8 | Es obligatorio, <= hoy
4 | YSKMenHor | Hora de envió mensaje | Char | 8 | Es obligatorio
5 | YSKMenVan | Van que envía el mensaje | Char | 3 | Puede ser null
6 | YSKMenGar | RUC del garante del mensaje | Char | 12 | .
Mensaje de respuesta
Archivo con nomenclatura XXXXnnnn.res
Campo | Nombre | Descripción | Tipo | Largo
1 | YSKResSec* | Secuencial* | Num | 8
2 | YSKResDep | Código de Depósito | Char | 4
3 | YSKResNro | Número de Entrada/Salida | Num | 15
4 | YSKResAno | Año de Entrada/Salida | Num | 4
5 | YSKResMovTpo | Tipo de Movimiento (ENT: entrada, SAL: salida) | Char | 3
6 | YSKResTpoErr | Tipo Error (S: Error, N: Advierte, A: Aviso) | Char | 1
7 | YSKResCodErr | Código de Error | Char | 4
8 | YSKResDscErr | Descripción del Error | Char | 254
9 | YSKResMenNro | Numero del Mensaje | Char | 14
10 | YSKResValErr | Valor del campo donde ocurrió el error | Char | 100
11 | YSKResFch | Fecha de Envío de la Respuesta | Num | 8
12 | YSKResHora | Hora de Envió de la Respuesta | Char | 8
San José, 8 de diciembre del 2003.
