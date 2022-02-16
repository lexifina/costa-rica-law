DIRECCIÓN GENERAL DE ADUANAS
RESOLUCIÓN DE ALCANCE GENERAL
RES-DGA-022-2022
DIRECCIÓN GENERAL DE ADUANAS, SAN JOSE, A LAS 08:50 HORAS DEL DIECINUEVE
DE ENERO DEL AÑO DOS MIL VEINTIDOS.
CONSIDERANDO
1. Que el artículo 6 de la Ley General de Aduanas, Nº 7557, del 20 de octubre de 1995, publicada en la Gaceta Nº 212, del 8 de noviembre de 1995, establece que uno de los fines del régimen jurídico es facilitar y agilizar las operaciones de comercio exterior.
2. Que el artículo 9 de la Ley General de Aduanas, establece como funciones del Servicio Nacional de Aduanas (SNA), actualizar los procedimientos aduaneros y proponer las modificaciones de las normas, para adaptarlas a los cambios técnicos, tecnológicos y a los requerimientos del Comercio Internacional.
3. Que el artículo 11 de la Ley General de Aduanas señala que la Dirección General de Aduanas (DGA) es el órgano superior jerárquico nacional en materia aduanera, que en el uso de su competencia le corresponde la dirección técnica y administrativa de las func iones aduaneras que esta ley y las demás disposiciones del ramo le conceden al SNA, la emisión de políticas y directrices para las actividades de las aduanas y dependencias a su cargo.
4. Que el artículo 30 literal h) de la Ley General de Aduanas señala que los auxiliares deben cumplir con las demás obligaciones que les fijan esta ley y sus reglamentos y con las disposiciones que establezca la autoridad aduanera, mediante resolución administrativa o convenio.
5. Que la resolución RES-DGA-203-2005 del 22 de junio del 2005, publicada en el Alcance Nº 23 a La Gaceta Nº 143 de fecha 26 de julio del 2005, recoge los procedimientos aduaneros vigentes en el Sistema Aduanero Nacional.
6. Que según el artículo 392, del RECAUCA IV, publicado en el Alcance # 51 de la Gaceta # 49, del 11 de marzo de 2021, en las DUAS de tránsito se debe declarar el valor de las mercancías de acuerdo a la factura comercial que las ampara.
7. Que le corresponde a la Dirección de Gestión Técnica preparar las directrices, normas, formatos y documentos que, asociados a los procesos aduaneros, estandaricen los criterios y unifiquen la aplicación de las normas técnicas vigentes, tendientes a facilitar el comercio. 33º)
Por tanto:
Con base en las potestades otorgadas en el REGLAMENTO DEL CÓDIGO ADUANERO UNIFORME CENTROAMERICANO, publicado en el Alcance # 51 de la Gaceta # 49, del 11 de marzo de 2021, la Ley General de Aduanas, Ley Nº 7557, del 20 de octubre de 1995 y sus reformas, e l Reglamento a la Ley General de Aduanas, Decreto Nº 25270-H, del 14 de junio de 1996 y sus reformas.
EL DIRECTOR GENERAL DE ADUANAS, RESUELVE:
Emitir los siguientes lineamientos para que los auxiliares de la función pública aduanera en los envíos del mensaje de las DUAS del régimen de tránsito (código 80), incluyan el valor de las mercancías de acuerdo a la factura comercial, cuando se trate de una compraventa internacional, o documento equivalente, de conformidad al artículo 392, del RECAUCA IV, publicado en el Alcance # 51 de la Gaceta # 49, del 11 de marzo de 2021.
1. Todas las DUAs del régimen de tránsito (código 80) deben tener declarado en el bloque B (correspondiente al encabezado de la DUA), los siguientes dos campos :
1.1 Campo B21: TVAD_INCR (Monto Total de Valor en Aduana para Importación/ exportación/reexportación).
1.2 Campo B27: TOT_FACT (Totalizador de los montos de facturas o documento que la sustituya).
1.3 Cuando no se incluyan estos dos campos, el declarante recibirá un mensaje con un error crítico tipo "S" que indicará lo siguiente: "Según RECAUCA IV, artículo 392, se debe declarar el valor de las mercancías de acuerdo a la factura comercial".
2. Adicionalmente, los valores contenidos en los campos B21: TVAD_INCR Monto Total de Valor en Aduana para Importación/ exportación/reexportación) y B27:TOT_FACT (Totalizador de los montos de facturas o documento que la sustituya), serán validados con el campo E11 VAL_FACTU (Monto total de factura), donde se indica el monto total consignado en la factura comercial, en la moneda pactada. Además, si la DUA contiene varias facturas, es decir, varios bloques E: Datos Generales de las Facturas en la Moneda Pactada (VALFAC01), entonces los valores contenidos en los campos B21 TVAD_INCR y B27 TOT_FACT, deben corresponder a la sumatoria de todas las facturas, es decir la suma de los valores contenidos en los campos E11 de cada factura en cada bloque E.
3. Los campos B21 y B27 pueden, pero no deben totalizarse ni validarse con los campos de las líneas de la DUA (Bloque C), ni de las líneas de la factura (Bloque F). Por ejemplo: transporte, seguro y otros gastos; asociados todos estos últimos con el término incoterm, ya que para las DUAS de tránsito (régimen 80) no se deben declarar los valores de los campos de transporte, de seguro, de otros gastos, ni el término incoterm.
En la DUA lo indicado se reflejaría de la siguiente manera:
[imagen]
4. Modificar el formato de mensaje de DUA versión 3.15 para que los campos B21 y B27 se lea de la siguiente manera:
Campo | Nombre | Descripción | Tipo | Largo | O/C | Validación | Instructivo de llenado | I | DS | T | E
B21 | TVAD_INCR | Monto Total de Valor en Aduana para Importación/ exportación/reexportación/tránsito | Num | 17.2 | O | | Corresponde a la suma total del v alor en aduana (campo VAD_INCR ) por línea de mercancía del DUA Para tránsito deberá consignar el v alor de cero, con excepción de reexportación. *En caso de las DUAs del régimen de tránsito, este campo no totaliza los campos de las líneas, sino solamente se v alida que coincida con el monto declarado en el campo E11 VAL_FACTU del bloque E. | SI | SI | NO SI* | SI
B27 | TOT_FACT | Totalizador de los montos de f acturas o documento que la sustituy a. | Num | 17.2 | O | | Corresponde a la suma total del v alor Factura (campo VGAS_FACT) | SI | SI | NO SI* | SI
[imagen]
5. Comunicar que para la fecha prevista para la vigencia de esta resolución, en la aplicación informática TICA serán efectivas las adiciones y ajustes necesarios para que los Auxiliares de la Función Pública Aduanera declarantes del régimen de tránsito , puedan ejecutar los lineamientos anteriormente señalados.
6. Indicar que los ajustes a la aplicación informática deben ser considerados por los desarrolladores externos para que preparen y adapten los programas que utilizan para la transmisión al TICA de los mensajes de las Declaraciones Únicas Aduaneras (DUAS).
7. Notificar a las Direcciones de Gestión Técnica, Gestión de Riesgo y Fiscalización, para lo que corresponda.
La presente resolución rige a partir de las cero horas del día 16 de febrero de 2022.
Comuníquese y publíquese en el Diario Oficial La Gaceta.
