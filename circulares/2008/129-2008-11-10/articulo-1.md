DIRECCIÓN GENERAL DE ADUANAS
San José, 10 de noviembre de 2008 CIRCULAR DGT-129-2008
Señores
Exportadores, Agencias y Agentes de Aduanas,
Desarrolladores de Software
Directores, Gerentes de Aduanas
Jefes de Departamentos, Asesorías,
Funcionarios del Servicio Nacional de Aduanas
Funcionarios Aduaneros
S. M.
Asunto: Envío de Campos Modificables en el DUA de Exportación
Estimados señores:
La Dirección General de Aduanas en el uso de las facultades establecidas en el artículo 11 de la Ley Nº 7557 Ley General de Aduanas de fecha 20 de octubre de 1995, sus reformas y modificaciones y los artículos 6 y 7 del decreto ejecutivo Nº 34475-H Reglamento de la Nueva Estructura Organizacional del Servicio Nacional de Aduanas, considera oportuno recordarles cuales son los campos definidos como no modificables en la Declaración Única Aduanera de Exportación (DUA) para lograr una confirmación exitosa de la información; lo anterior en cumplimiento con lo regulado en el artículo 345 del Reglamento a la Ley General de Aduanas y lo definido en la resolución RES-DGA-155-2008 del 28 de abril de 2008 que oficializa el Manual de Procedimientos de Exportación.
Es importante recordar que el DUA contiene una serie de campos, que pueden ser modificados por el declarante únicamente cuando el exportador no cuente con la certeza de algunos de los datos al momento de realizar la declaración o cuando estas modificaciones no afecten la naturaleza de las mercancías. Las mencionadas variaciones se pueden efectuar en cualquier momento a través del envío de mensajes de modificación (segundos mensajes), pero antes de la asignación del tipo de revisión. Una vez autorizado el levante, la información sólo puede ser variada al momento del envío del mensaje de confirmación.
A continuación se detalla, según sea el caso, los campos que No pueden ser variados en segundos mensajes o en el mensaje de confirmación con respecto a la información previamente declarada:
A. Campos No Modificables en Segundos Mensajes
Encabezado del DUA-Bloque de datos generales (IMPHDR01)
Campo | Nombre | Descripción
B5 | TIPO_OPERA | Modalidad asociada al Régimen.
B6 | TIPO_DOCUM | Tipo de Identificación del Exportador
B7 | NUME_DOCUM | No. de Identificación del Exportador
B8 | CNIV_COIMP | Nivel Comercial del Exportador
B9 | DESP_URGE | Forma de Despacho Elegida por el Declarante
B12 | CODI_ALMA | Lugar de Ubicación de la Mercancía.
B13 | COD_BANCO | Entidad Financiera
B14 | COD_CUENTA | Número de Cuenta (sin los 3 dígitos del banco)
B17 | NUM_GARAN | Número de Garantía
B18 | TOT_GARAN | Monto Total de Garantía
B28 | TIPO_TRAN | Normal y Correlación para importación (y Repetitivo solo para granel)/consolidación, normal o repetitivo para tránsito), si se permita la modificación en segundos mensajes. (Así reformado mediante resolución DGA-032 del 1° de febrero de 2010)
B31 | MON_ASOC | Momento de Declaración del Inventario
B32 | TIPO_CARGA | Origen del Tipo de Inventario
B33 | AFORO_INM | Solicitud de Asignación del tipo de revisión.
B37 | VER_FAB | Verifica en empresa
Líneas de mercancías del DUA-Detalle de la declaración (IMPDET01)
Campo | Nombre | Descripción
C5 | PART_NANDI | Partida Arancelaria
C12 | SEST_MERCA | Condición física de la mercancía.
C13 | CODI_CER | Código de Excepción para el Control de la Presentación de los Documentos
C14 | CONV_INTER | Acuerdos, Convenios o Tratados
C15 | PAIS_ORIGE | País Origen
C17 | PUER_EMBAR | País de Procedencia (importación/Tránsito)
C19 | CADUREGPRE | Aduana del D.U.A./ documento precedente
C20 | FANOREGPRE | Año del D.U.A/ Documento Precedente
C21 | NDCLREGPRE | Número del D.U.A/ Documento Precedente
C22 | TDOCREGPRE | Tipo de Documento Precedente
C52 | PLAZO | Plazo
B Campos no modificables en DUAs objeto de verificación
documental y reconocimiento físico (semáforo rojo)
Encabezado del DUA-Bloque de datos generales (IMPHDR01)
Campo | Nombre | Descripción
B5 | TIPO_OPERA | Modalidad asociada al Régimen.
B6 | TIPO_DOCUM | Tipo de Identificación del Exportador
B7 | NUME_DOCUM | No. de Identificación del Exportador
B8 | CNIV_COIMP | Nivel Comercial del Exportador
B9 | DESP_URGE | Forma de Despacho Elegida por el Declarante
B12 | CODI_ALMA | Lugar de Ubicación de la Mercancía.
B13 | COD_BANCO | Entidad Financiera
B14 | COD_CUENTA | Número de Cuenta (sin los 3 dígitos del banco)
B17 | NUM_GARAN | Número de Garantía
B18 | TOT_GARAN | Monto Total de Garantía
B21 | TVAD_INCR | Monto total de valor en Aduana para Importación.
B22 | TCANT_BULT | Totalizador de la Cantidad Declarada en el Campo CANT_BULTO
B23 | TPESO_NETO | Totalizador de la Cantidad Declarada en el Campo PESO _ NETO
B24 | TPESO_BRUT | Totalizador de Cantidad de Declarada en el Campo PESO _ BRUTO
B25 | TQUNIFIS | Totalizador de la Cantidad Declaradas en el Campo UNID_FIQTY
B26 | TQUNICOM | Totalizador del Monto de la Cantidad Declarada en el Campo QUNICOM
B28 | TIPO_TRAN | Normal y Correlación para importación (y Repetitivo solo para granel) / consolidación, normal o repetitivo para tránsito
B31 | MON_ASOC | Momento de Declaración del Inventario
B32 | TIPO_CARGA | Origen del Tipo de Inventario
B33 | AFORO_INM | Solicitud de Asignación del tipo de revisión.
B37 | VER_FAB | Verifica en empresa
Líneas de mercancías del DUA-Detalle de la declaración (IMPDET01)
Campo | Nombre | Descripción
C5 | PART_NANDI | Partida Arancelaria
C6 | DESC_COMER | Descripción Comercial 01
C7 | DESC_FOPRE | Descripción Comercial 02
C8 | DESC_MATCO | Descripción Comercial 03
C9 | DESC_USOAP | Descripción Comercial 04
C10 | DESC_OTROS | Descripción Comercial 05
C11 | MARCAS_NUM | Marcas y Números de los bultos
C12 | SEST_MERCA | Condición física de la mercancía.
C13 | CODI_CER | Código de Excepción para el Control de la Presentación de los Documentos
C14 | CONV_INTER | Acuerdos, Convenios o Tratados
C15 | PAIS_ORIGE | País Origen
C17 | PUER_EMBAR | País de Procedencia (importación/Tránsito)
C19 | CADUREGPRE | Aduana del D.U.A./ documento precedente
C20 | FANOREGPRE | Año del D.U.A/ Documento Precedente
C21 | NDCLREGPRE | Número del D.U.A/ Documento Precedente
C22 | TDOCREGPRE | Tipo de Documento Precedente
C28 | VAD_INCR | Valor en Aduana, por línea del DUA.
C29 | CANT_BULTO | Cantidad de Bultos
C30 | CLASE | Tipo de Bultos
C31 | UNID_FIQTY | Cantidad Unidades de Volumen Físico
B32 | TIPO_CARGA | Origen del Tipo de Inventario
C33 | QUNICOM | Cantidad Unidad Comercial
C35 | PESO_NETO | Peso Neto
C36 | PESO_BRUTO | Peso Bruto
C52 | PLAZO | Plazo
C Campos no modificables en DUA sin verificación documental
y reconocimiento físico (semáforo verde)
Encabezado del DUA-Bloque de datos generales (IMPHDR01)
Campo | Nombre | Descripción
B5 | TIPO_OPERA | Modalidad asociada al Régimen.
B6 | TIPO_DOCUM | Tipo de Identificación del Exportador
B7 | NUME_DOCUM | No. de Identificación del Exportador
B8 | CNIV_COIMP | Nivel Comercial del Exportador
B9 | DESP_URGE | Forma de Despacho Elegida por el Declarante
B12 | CODI_ALMA | Lugar de Ubicación de la Mercancía.
B13 | COD_BANCO | Entidad Financiera
B14 | COD_CUENTA | Número de Cuenta (sin los 3 dígitos del banco)
B17 | NUM_GARAN | Número de Garantía
B18 | TOT_GARAN | Monto Total de Garantía
B28 | TIPO_TRAN | Normal y Correlación para importación (y Repetitivo solo para granel) / consolidación, normal o repetitivo para tránsito
B31 | MON_ASOC | Momento de Declaración del Inventario
B32 | TIPO_CARGA | Origen del Tipo de Inventario
B33 | AFORO_INM | Solicitud de Asignación del tipo de revisión.
B37 | VER_FAB | Verifica en empresa
Líneas de Mercancías del DUA-Detalle de la declaración (IMPDET01)
Campo | Nombre | Descripción
C5 | PART_NANDI | Partida Arancelaria
C12 | SEST_MERCA | Condición física de la mercancía.
C13 | CODI_CER | Código de Excepción para el Control de la Presentación de los Documentos
C14 | CONV_INTER | Acuerdos, Convenios o Tratados
C15 | PAIS_ORIGE | País Origen
C17 | PUER_EMBAR | País de Procedencia (importación/Tránsito)
C19 | CADUREGPRE | Aduana del D.U.A./ documento precedente
C20 | FANOREGPRE | Año del D.U.A/ Documento Precedente
C21 | NDCLREGPRE | Número del D.U.A/ Documento Precedente
C22 | TDOCREGPRE | Tipo de Documento Precedente
C52 | PLAZO | Plazo
Es importante recordar que los demás campos no indicados en las tablas anteriores están autorizados ser variados con el mensaje de confirmación o segundos mensajes. Además; que el declarante debe enviar el mensaje para la confirmación o segundo mensaje del DUA, confeccionando el archivo tanto con los campos del mensaje que desea variar como los que no; de lo contrario, el sistema asume que lo está limpiando, es decir graba un nulo o blanco en el DUA y se pierde lo enviado en el mensaje inicial. Esto quiere decir que siempre deben enviar el valor del campo, ya sea en el mensaje inicial, segundos mensajes o mensaje final; tratándose del campo “Fecha de embarque/Salida” (FECH_EMBAR) debe ser actualizado con el mensaje de confirmación para su correcta comunicación a las entidades gubernamentales competentes.
Publíquese en el Diario Oficial La Gaceta.
Dirección General de Aduanas
