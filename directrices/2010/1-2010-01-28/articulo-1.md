DIRECCIÓN GENERAL DE ADUANAS
DIRECTRIZ
DIR-DGT-001-2010
Señores:
Empresas de Zona Franca,
Agencias y Agentes de Aduanas,
Desarrolladores de Software, Asesorías,
Directores, Gerentes, Subgerentes de Aduana,
Jefes de Departamento, Jefes de Sección,
Funcionarios Aduaneros,
Servicio Nacional de Aduanas
Asunto: Campos modificables en el DUA de Internamiento de Zona Franca
Estimados señores:
Por medio de la presente, la Dirección General de Aduanas, emite la directriz denominada “Campos modificables en el DUA de Internamiento de Zona Franca” con fundamento en los artículos 9º, 11 y 12 de la Ley General de Aduanas, Ley Nº 7557, sus reformas y modificaciones y artículos 6º párrafo primero y 7º inciso a) de Reglamento a la Ley General de Aduanas.
I. MOTIVACIÓN
Es una atribución de la Dirección General de Aduanas y la Dirección de Gestión Técnica las funciones aduaneras previstas en la Ley General de Aduanas y demás disposiciones. Para tal cometido se emiten circulares, directrices y resoluciones de alcance general.
En aplicación de dichas competencias, la Dirección General de Aduanas, mediante la resolución RES-DGA-352-2009 con fecha 18 de noviembre de 2009 y su modificación RES-DGA-364-2009 de fecha 20 de noviembre de 2009, se comunicó que a partir del 1 de febrero de 2010, se implementará en la Aduana Santamaría el Procedimiento para el Internamiento al Régimen de Mercancías en Zonas Francas en el Sistema de Información para el Control Aduanero TIC@.
II. OBJETIVO
La presente directriz tiene como objetivo indicar los campos que pueden ser modificados en el DUA de Internamiento de mercancías al Régimen de Zona Franca. Esta directriz podrá ser consultada y accesada a través de la página Web del Ministerio de Hacienda, en la siguiente dirección electrónica:
https://www.hacienda.go.cr/Msib21/Espanol/Direccion+General+de+Aduanas/IMPLEMENTACION+ZN+PA.htm
III. ALCANCE
Esta directriz es de uso obligatorio para los usuarios del Servicio Nacional de Aduanas que deben modificar información contenidas en las declaraciones de internamiento al Régimen de Zonas Francas.
IV. FUNDAMENTO LEGAL
Esta Directriz encuentra fundamento en los artículos 7º y 9º del Código Aduanero Uniforme Centroamericano, publicado en La Gaceta Nº 130 del 8 de julio de 2003; 5, 6 incisos b), 9 inciso e), 11, 12, 22, 24 inciso j) y 30 inciso d) de la Ley General de Aduanas, Nº 7557 del 20 de octubre de 1995 publicada en La Gaceta Nº 212 del 08 de noviembre de 1995 y sus reformas y los artículos 6º y 7º, inciso b) del Reglamento a la Ley General de Aduanas.
V. VIGENCIA
Rige a partir del 1º de febrero de 2010. Comuníquese y publíquese en el Diario Oficial La Gaceta.
CAMPOS MODIFICABLES EN EL DUA DE INTERNAMIENTO
DE ZONA FRANCA EN EL MENSAJE DE CONFIRMACIÓN
I.—Sujetos favorecidos: Los sujetos favorecidos para la aplicación de esta directriz son las empresas Beneficiarias del Régimen de Zonas Francas, agentes y agencias de aduanas que gestionen Declaraciones de Internamiento al Régimen.
II.—Ámbito de aplicación: Esta directriz es aplicable a la oportunidad que se otorga al declarante de modificar información contenida en un DUA de internamiento al Régimen de Zonas Francas, en estado ORD con forma de despacho Normal o VAD, al que le haya correspondido “sin revisión o “revisión documental”.
III.—Contenido:
1. El DUA de internamiento al Régimen de Zonas Francas contiene una serie de campos que pueden ser modificados con el mensaje de confirmación, siempre que dichos cambios no afecten la naturaleza de las mercancías declarada en el DUA.
2. Los campos que pueden ser objeto de modificación en el DUA de Internamiento de Zonas Francas con el mensaje de confirmación son los siguientes:
Encabezado del DUA –Bloque de Datos Generales (IMPHDR01)
Campo | Nombre | Descripción
B16 | MAUTOLIQUI | Monto total de la obligación Tributaria Aduanera
B21 | TVAD_INCR | Monto Total de Valor en Aduana para Importación/ exportación/reexportación
B23 | TPESO_NETO | Totalizador de la Cantidad Declarada en el Campo PESO _ NETO
B24 | TPESO_BRUTO | Totalizador de Cantidad de Declarada en el Campo PESO _ BRUTO
B25 | TQUNIFIS | Totalizador de la Cantidad Declaradas en el Campo UNID_FIQTY
B26 | TQUNICOM | Totalizador del Monto de la Cantidad Declarada en el Campo QUNICOM
B27 | TOT_FACT | Totalizador de los montos de facturas o documento que la sustituya
B29 | DOBS | Observaciones
Líneas de Mercancías del DUA –
Detalle de la Declaración (IMPDET01)
Campo | Nombre | Descripción
C6 | DESC_COMER | Descripción Comercial
C11 | MARCAS_NUM | Marcas y Números de los bultos
C24 | VGAS_FACT | Monto de la Factura, por línea de DUA
C25 | VGAS_SEGUR | Monto de Seguro, por línea de DUA
C26 | VGAS_TREMB | Monto de transporte, por línea de DUA
C27 | VGAS_OTROS | Monto de Adicciones y Deducciones por línea de DUA
C31 | UNID_FIQTY | Cantidad Unidades de Volumen Físico
C33 | QUNICOM | Cantidad Unidad Comercial
C35 | PESO_NETO | Peso Neto
C36 | PESO_BRUTO | Peso Bruto
Bloque de Datos del Proveedor (IMPPRO01)
Campo | Nombre | Descripción
D4 | NUM_PROVE | Número de proveedor
D5 | NOMB_PROVE | Nombre del proveedor /exportador
D6 | COND_PROVE | Nivel del proveedor /exportador
D7 | CONT_PROVE | Otros datos del proveedor/Exportador
D8 | DIRE_PROVE | Domicilio del proveedor/Exportador
D9 | CODI_PAIS | País del proveedor/Exportador
Bloque de Datos de las Líneas de la Factura (FACDET01)
Campo | Nombre | Descripción
F9 | PRODUC-DESC | Descripción de la Mercancía
F11 | VAL_UNIDAD | Precio unitario de la Mercancía
F12 | MARCA | Marca de la Mercancía
F13 | FACMODELO | Modelo de la Mercancía
3. Es importante recordar que los campos no indicados en las tablas anteriores no están autorizados para ser variados en el mensaje de confirmación. El declarante debe enviar el mensaje para la confirmación del DUA confeccionando el archivo tanto con los campos del mensaje que desea modificar como los que no, de lo contrario el Sistema asume que lo está limpiando, es decir graba un nulo o blanco en el DUA y se pierde lo enviado en el mensaje inicial.
San José, 28 de enero del 2010.
