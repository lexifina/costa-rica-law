ANEXO 1
DETALLE DE LA PLANTILLA DE CARTERAS
Las Sociedades Administradora de Fondos de Inversión deberán remitir a la SUGEVAL en forma quincenal (el 15 y el último día de cada mes), un archivo con la información de las carteras de cada fondo de inversión que administren. Será un archivo independiente por cada fondo.
La SUGEVAL ha establecido el formato de este archivo, el cual deberá ser enviado por medio del Sistema Ingresador (firmado electrónicamente y encriptado). A continuación, se detallan los campos que deberán suministrarse para cada título que conforme la cartera de un fondo de inversión. La secuencia en que se han anotado corresponde al orden en que deberán ser incorporados al archivo.
No. | Nombre | Descripción | Formato | Long. | Dec. | Validaciones
1 | Fecha de la operación | Fecha en la que aconteció la adquisición de la inversión o la fecha de la operación de recompra como comprador a hoy. | DD/MM/AAAA | 10 | | No puede ser nulo, y no puede ser mayor a la fecha valor de la cartera
2 | Canal de Venta | Medio por el cual se adquirió la inversión: a través de la Bolsa Nacional de Valores, por ventanilla o mercados internacionales | Alfanumérico | 1 | | Los valores válidos se encuentran detallados en la tabla 1 del anexo
3 | No. Operación | Número de la boleta de bolsa con la que se concretó la transacción | Numérico | 10 | | Requerido si el campo 2 (Canal de Venta) es igual a "B" (Bolsa Nacional de Valores)
4 | Tipo de Título | Indica la clase de título valor o instrumento bursátil adquirido. | Numérico | 1 | | Los valores válidos se encuentran detallados en la tabla 2 del anexo
5 | Nemotécnico del emisor | Código con el cual se identifica en forma única la entidad emisora del título valor | Alfanumérico | 15 | | Debe suministrarse únicamente si el campo 2 (canal de venta) es igual a "B" ó "V" (fue adquirido por la BNV o ventanilla). El nemotécnico debe corresponder a uno de los códigos de emisores de la BNV. También debe indicarse si el campo 2 (canal de venta) es igual a "I" (Mercados Internacionales) y el emisor está registrado en la BNV (por ejemplo para una operación asociada con la deuda externa de C.R., el nemotécnico de emisor corresponde actualmente a "G"). En el caso de operaciones de recompra se deberá indicar el emisor del título valor subyacente de la operación.
6 | Nombre del emisor | Nombre de la entidad emisora del título valor | Alfanumérico | 80 | | Debe suministrarse únicamente cuando el campo 2 (canal de venta) es igual a "I" (Mercados internacionales) y el emisor no tiene un nemotécnico en BNV.
7 | Nemotécnico del instrumento | Código con el que se identifica el instrumento | Alfanumérico | 12 | | Si el campo 2 (canal de venta) es igual a "B" ó "V" (fue adquirido por la BNV o ventanilla), el nemotécnico debe corresponder a uno de los códigos de instrumentos de la BNV. Si el campo 2 (canal de venta) es igual a "I" (Mercados internacionales), en este campo se utilizará el identificador internacional del título valor: código ISIN o CUSIP. En el caso de operaciones de recompra se deberá indicar el instrumento del título valor subyacente de la operación.
8 | Nombre del instrumento | Nombre del título valor | Alfanumérico | 100 | | Debe suministrarse únicamente cuando el campo 2 (canal de venta) es igual a "I" (Mercados internacionales)
9 | Indicador de estandarización | Indica si el título valor es estandarizado o no. | Alfanumérico | 1 | | Debe suministrarse si el campo 4 (Tipo de título) es igual a 1 (renta fija), 5 (fideicomiso de titularización de deuda) ó 7 (fideicomiso de titularización valores mixtos). Los valores válidos se detallan en la tabla 3 del anexo
10 | Sector del emisor | Indica si el emisor del título pertenece al sector público o al privado | Numérico | 1 | | Debe suministrarse si el campo 2 (canal de venta) es igual a "I" (Mercados Internacionales). Los valores válidos se encuentran en la tabla 4 del anexo.
11 | Nombre de calificadora de riesgo | Nombre de la entidad calificadora de la emisión en el caso de emisores extranjeros | Alfanumérico | 2 | | Debe suministrarse si el campo 2 (canal de venta) es igual a "I" (Mercados Internacionales). Los valores válidos se encuentran en la tabla 5 del anexo.
12 | Código de calificación | Código con el que se identifica la calificación otorgada a la emisión para los emisores extranjeros | Alfanumérico | 5 | | Debe suministrarse si el campo 2 (canal de venta) es igual a "I" (Mercados Internacionales) y corresponde a la calificación otorgada por la calificadora indicada en el campo 11.
13 | Moneda | Moneda en la cual está emitido el título valor. | Alfanumérico | 3 | | Los valores válidos se encuentran detallados en la tabla 6 del anexo.
14 | Indicador de Recompras y Préstamo de valores | Indica si el título está en el Fideicomiso de garantía por operaciones de recompra o si está en calidad de préstamo de valores | Alfanumérico | 2 | | Los valores válidos se detallan en la tabla 7 del anexo
15 | Fecha de vencimiento | Fecha en que la obligación debe ser cancelada por el emisor. | DD/MM/AAAA | 10 | | Debe suministrarse únicamente cuando el campo 4 (Tipo de título) es igual a 1 (renta fija) ó 5 (Fideicomisos de titularización de deuda). En el caso de las operaciones de recompra será la fecha de liquidación de la venta a plazo.
16 | Fecha pago interés | Fecha del último pago de intereses | DD/MM/AAAA | 10 | | Puede suministrarse únicamente cuando el campo 4 (Tipo de título) es igual a 1 (renta fija) ó 5 (Fideicomisos de titularización de deuda) y podrá ser mayor a la fecha de la cartera.
17 | Periodicidad | Número de veces al año con que se recibe el pago de intereses | Numérico | 2 | | Debe suministrarse únicamente cuando el campo 4 (Tipo de título) es igual a 1 (renta fija) ó 5 (Fideicomisos de titularización de deuda). Los valores válidos se encuentran detallados en la tabla 8 del anexo
18 | Tasa interés neta | Porcentaje de interés neto definido con la emisión del título. | Numérico | 7 | 4 | Puede suministrarse únicamente cuando el campo 4 (Tipo de título) es igual a 1 (renta fija) ó 5 (Fideicomisos de titularización de deuda). En el caso de valores de renta fija con cupón ajustable, será la tasa de referencia bruta que se utiliza para el cálculo. Para las operaciones de recompra corresponde al rendimiento de la misma.
19 | Premio | Puntos adicionales a sumar a la tasa de referencia | Numérico | 7 | 3 | Se utiliza en el caso de títulos valores de renta fija con cupón ajustable
20 | Base de cálculo | Total de días del año contemplados para el cálculo de intereses | Numérico | 3 | | Requerido si el campo 3 (Tipo de título) es igual a 1 (renta fija) ó 5 (Fideicomisos de titularización de deuda). Los valores válidos se encuentran detallados en la tabla 9 del anexo.
21 | Valor facial | Corresponde al valor estipulado en el título valor. | Numérico | 18 | 2 | Si el campo 4 (Tipo de título) es igual a 2 (renta variable) se deberá suministrar la cantidad de acciones. Si el campo 4 (Tipo de título) es igual a 3 (valores de participación de fondos cerrados) o 4 (valores de participación de fondos abiertos) se deberá suministrar la cantidad de valores de participación. No podrá ser un valor negativo o cero.
22 | Costo de adquisición | Desembolso que demandó la adquisición del título | Numérico | 18 | 2 | Requerido. No podrá ser un valor negativo o cero.
23 | Primas y descuentos acumuladas | Monto de las primas y descuentos acumuladas a la fecha valor de la cartera | Numérico | 18 | 2 | Requerido si el campo 4 (Tipo de título) es igual a 1 (renta fija) ó 5 (Fideicomisos de titularización de deuda). Si el campo 4 (Tipo de título) es igual a 2 (renta variable) deberá ser igual a cero.
24 | Ganancias o Pérdidas no realizadas | Monto de las ganancias o pérdidas no realizadas en valoración a precios de mercado a la fecha valor de la cartera | Numérico | 18 | 2 | Requerido.
25 | Valor en libros | Valor en libros del título valor a la fecha valor de la cartera. | Numérico | 18 | 2 | Requerido. Corresponde a la sumatoria del costo de adquisición, primas y descuentos acumulados y las ganancias o pérdidas no realizadas en valoración a precios de mercado. No podrá ser un valor negativo o cero.
26 | Intereses acumulados | Intereses que ha devengado la inversión a la fecha valor de la cartera | Numérico | 18 | 2 | Puede suministrarse únicamente cuando el campo 4 (Tipo de título) es igual a 1 (renta fija) ó 5 (Fideicomisos de titularización de deuda) No podrá ser un valor negativo.
27 | Precio de mercado según SAFI | Valor de mercado en que se estima la inversión de acuerdo la metodología de valoración propia de la SAFI. | Numérico | 20 | 3 | Puede quedar vacío únicamente para títulos de deuda cuyo plazo es menor a 180 días. No podrá ser un valor negativo.
28 | Código del Custodio | Identificador de la entidad nacional o internacional en el que se encuentra custodiado el título valor. | Numérico | 2 | | Los valores válidos se encuentran detallados en la tabla 10 del anexo
Formato
El archivo deberá generarse en formato texto, utilizando el caracter "tabulador" como separador de campos.
La longitud detallada en cada campo incorpora para el caso de los datos numéricos el punto decimal y la cantidad de decimales especificada. Así por ejemplo, para un campo que se haya indicado longitud: 7, decimales: 4, la parte entera únicamente contempla 2 espacios, pues de los 7, 4 son decimales y un espacio está reservado para el punto decimal.
Nombre del Archivo
El nombre del archivo debe estar compuesto por una secuencia de caracteres con la siguiente estructura:
"CARTERA" + "_" + identificador del FI en SUGEVAL + "_" + fecha de la cartera + ".txt"
Así por ejemplo, el nombre del archivo con corte al día 31 de enero del 2002 del fondo de inversión con código ALDCRE$FI en SUGEVAL sería: CARTERA_ALDCRE$FI_31012002.txt y con corte al 1 de enero del 2002, CARTERA_ALDCRE$FI_01012002.txt
Tabla 1: Canal de Venta
Código | Descripción
B | Bolsa Nacional de Valores
V | Ventanilla
I | Mercados Internacionales
Tabla 2: Tipo de Título
Código | Descripción
1 | Renta Fija
2 | Renta Variable
3 | Valores de participación fondos cerrados
4 | Valores de participación fondos abiertos
5 | Fideicomiso de Titularización de deuda
6 | Fideicomiso de Titularización de participación
7 | Fideicomiso de Titularización valores mixtos
Tabla 3: Estandarización
Código | Descripción
0 | No estandarizado
1 | Estandarizado
Tabla 4: Sector del Emisor
Código | Descripción
1 | Público
2 | Privado
Tabla 5: Sociedades Clasificadoras
Código | Descripción
SP | Standard and Poor´s
MO | Moody´s Investors Service
FI | Fitch´s Investors Service
IB | Inter Bank Company Analysis
PO | Pondera Calificadora de Riesgo
SC | Sociedad Calificadora de Riesgo
OT | Otros
Tabla 6: Moneda
Código | Descripción
CRC | Colón (Costa Rica)
EUR | Euro
GTQ | Quetzal (Guatemala)
HNL | Lempira (Honduras)
NIO | Córdoba (Nicaragua)
SVC | Colón (El Salvador)
USD | Dólar (Estados Unidos)
Tabla 7: Operaciones de recompra y préstamo de valores
Código | Descripción
RC | Operación de recompra con posición comprador a plazo
RV | Operación de recompra con posición vendedor a plazo
P | Valor en calidad de préstamo de valores
N | Título valor disponible para la venta
Tabla 8: Periodicidad
Código | Descripción
0 | Cero cupón
1 | Anual
2 | Semestral
3 | Cuatrimestral
4 | Trimestral
6 | Bimestral
12 | Mensual
Tabla 9: Base de Cálculo
Código | Descripción
360 | Base 360 días
365 | Base 365 días
Tabla 10: Custodio
Código | Descripción
1 | CEVAL
2 | Clearstream
3 | Deutsche Euroclear
4 | DTCC (Depositary Trust Clearing Company)
5 | Central Nicaraguense de Valores
6 | Central de Valores de El Salvador
7 | Bancentro Nicaragua
8 | Caja de Valores de Guatemala
9 | Central Hondureña de Valores
10 | Latin Clear de Panamá
11 | Indeval de México
