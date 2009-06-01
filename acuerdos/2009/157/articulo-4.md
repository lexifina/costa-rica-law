Artículo 4º—Disposiciones para puestos de bolsa. Se realizan los siguientes cambios que afectan a los puestos de bolsa:
a) Se modifica el contenido del anexo 31 Suficiencia Patrimonial y Control de Límites de en seguimiento al Reglamento sobre gestión de riesgos, quedando las siguientes cuentas:
[imagen]
[imagen]
[imagen]
[imagen]
b) Se modifica el contenido del anexo 10 “Reporte de inversiones propias Puestos de Bolsa para agregar nuevas reglas de validación, según se describe a continuación:
i) Se solicita el monto del “Valor en riesgo absoluto”, el cual indica la máxima pérdida absoluta que podría sufrir la cartera de inversiones, en un plazo determinado y dado un nivel de confianza. El valor en riesgo absoluto se debe expresar en miles de colones.
ii) Se solicita el monto del “Requerimiento de capital por riesgo precio”, de acuerdo con lo requerido en el Reglamento de gestión de riesgos. El requerimiento de capital por riesgo de precio se debe expresar en miles de colones.
iii) Se modifica la tabla 6 del campo 13 Monedas, para incluir a las unidades de desarrollo (UND) con el fin de que aquellos títulos denominados en esta unidad sean debidamente categorizados. Además, se elimina de la Tabla 6 los códigos ARS “Colones y Dólares” y XEU “Ecu”.
iv) El campo 9 Código de estandarización (1=estandarizado y 0=no estandarizado) se requiere obligatorio para todos los tipos de títulos.
v) Se modifica la tabla 7 del 14 “Estado de la inversión propia”, para incluir dos nuevos códigos: “VC” indica los títulos que están comprometidos por operaciones de ventas en corto y “DC” Derecho sobre títulos que se han comprado pero que no se han recibido, para la contraparte de este tipo de operaciones.
vi) Se modifica la validación a la columna llamada “Código ISIN” de la siguiente forma:
a. El código ISIN debe guardar consistencia, con el siguiente detalle:
1. Nemotécnico del emisor
2. Nemotécnico del instrumento
3. Fecha de vencimiento
4. Moneda
5. Tipo de título
6. Periodicidad
7. Estandarización
b. El registro del código ISIN debe hacerse para todas las operaciones; excepto para las participaciones en fondos abiertos, (“Tipo de título” = 4), y para los títulos que se encuentren en el listado de excepciones que se pondrá a disposición de los regulados en la página web de la Superintendencia General de Valores.
c. En caso de inversiones en reporto tripartito (indicador = RV) o en el mercado de liquidez (Indicador = ML), se exceptúa la revisión de la consistencia del ISIN con la fecha de vencimiento indicada en el punto a).
d. En el caso de títulos internacionales, cuando el acuse de recibo indique que la información no fue cargada porque existe un error de consistencia entre el ISIN y los datos del punto a), el regulado debe comunicarse con las áreas de supervisión de la Superintendencia General de Valores para analizar el caso.
vii) Cuando se trata de una inversión en el mercado de liquidez (Nemotécnico instrumento = ML); se acepta si el “Estado de Inversión” es RV o ML. En este caso el precio de mercado (campo 27) debe ser cero.
viii) En el caso de inversiones en valores de participación de fondos abiertos (Tipo de título =4), que no hayan sido adquiridos en el exterior, el nemotécnico del instrumento debe coincidir con el código del fondo, el cual estará disponible en los boletines quincenales de fondos de inversión publicados en la página web de la Superintendencia General de Valores.
ix) Se solicita la serie de la emisión para los títulos que se encuentren en el listado de excepciones que se pondrá a disposición de los regulados en la página web de la Superintendencia General de Valores.
c) Se modifica el contenido del anexo 12 “Reporte de operaciones abiertas a plazo” para agregar cuatro nuevos campos y modificar el nombre de uno, según se describe a continuación:
i) Se incluyen los siguientes campos:
NOMBRE | DESCRIPCIÓN | FORMATO | VALIDACIONES
Tipo de operación | Indica el tipo de la operación a plazo, ya sea mercado de liquidez, reportos puros o reportos tripartitos. | Alfanumérico | No puede ser nulo Si el “Canal de Venta” = “B” (Bolsa Nacional de Valores), se debe incluir “ML” si es Mercado de liquidez, “RP” si es Reportos puros y “RT” si es Reportos tripartitos. Si el “Canal de Venta” = “I” (Internacional), se debe incluir “RP” si la operación es un Reporto puros o “OT” si es Otro tipo de Operación.
Fecha de operación | Fecha en la cual se negoció la operación a plazo. | DD/MM/AAAA | No puede ser nulo y no debe ser mayor a la fecha valor del reporte.
Tipo de identificación | Indica si la identificación es una cédula física costarricense, cédula de residencia, cédula jurídica pasaporte o alguna otra identidad. | Alfanumérico | No puede ser nulo. Indicar “CD” si es cédula de identidad física costarricense, “PS” si es Pasaporte, “CR” si es Cédula de residencia, “CJ” si es Cédula Jurídica y “OT” si es Otro tipo de identificación
Número de identificación del cliente | Se incluye el número de identificación del cliente el cual tiene asignada la posición a plazo | Alfanumérico | No puede ser nulo Si Tipo de identificación = “CD” Cédula de identidad física costarricense, los campos a incluir son 9 y sin guiones tal y como aparecen en el padrón, por ejemplo: 101110222. Si Tipo de identificación = “CJ” Cédula Jurídica, los campos a incluir son 10 y sin guiones tal y como aparecen en el padrón, por ejemplo: 3101123456. Si Tipo de identificación = “PS” Pasaporte ó “CR” Cédula de Residencia u “OT” Otra identificación, la cantidad máxima permitida de datos es de 20 campos
ii) Se modifica el nombre del campo 2 llamado “Tipo de operación” para que en adelante se lea “Posición a plazo”.
d) Se modifica el contenido del anexo 42 “Plantilla para el envío de la información sobre traspasos no onerosos”, para ampliar el detalle de los traspasos no onerosos y considerar la clasificación establecida en el SGV-A-130 Acuerdo para la implantación del Reglamento de Custodia.
e) En el Anexo 08 de los estados financieros de los puestos de bolsa (BG_PUESTOS, RA_PUESTOS y ER_PUESTOS) se modifican los números de cuenta de las siguientes cuentas:
ANEXO | CATÁLOGO | Nº DE CUENTA ANTERIOR | Nº DE CUENTA MODIFICADO | NOMBRE DE LA CUENTA
8 | RA_PUESTOS | 43809000 | 43899000 | Otros gastos con partes relacionadas
43809100 | 43899100 | Otros gastos con partes relacionadas en colones
43809200 | 43899200 | Otros gastos con partes relacionadas en dólares
ER_PUESTOS | 43809000 | 43899000 | Otros gastos con partes relacionadas
43809100 | 43899100 | Otros gastos con partes relacionadas en colones
43809200 | 43899200 | Otros gastos con partes relacionadas en dólares
