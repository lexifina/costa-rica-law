Artículo 5º—Disposiciones para sociedades administradoras y fondos de inversión. Se realizan los siguientes cambios que afectan a las sociedades administradoras y fondos de inversión:
a) Se modifica el contenido del anexo 18 “Plantilla de Carteras” de las sociedades administradoras de fondos de inversión para agregar nuevas reglas de validación, según se describe a continuación:
i) Se solicita el monto del “Valor en riesgo absoluto”, el cual indica la máxima pérdida absoluta que podría sufrir la cartera de inversiones, en un plazo determinado y dado un nivel de confianza. El valor en riesgo absoluto se debe expresar en miles.
ii) En el caso de la sociedad administradora, se solicita el monto del “Requerimiento de capital por riesgo precio”, de acuerdo con lo requerido en el Reglamento de gestión de riesgos. El requerimiento de capital por riesgo de precio se debe expresar en miles de colones.
iii) El campo 9 Código de estandarización (1=estandarizado y 0=no estandarizado) se requiere obligatorio para todos los tipos de títulos.
iv) Se modifica la validación a la columna llamada “Código ISIN” de la siguiente forma:
a. El código ISIN debe guardar consistencia, con el siguiente detalle:
1. Nemotécnico del emisor
2. Nemotécnico del instrumento
3. Fecha de vencimiento
4. Moneda
5. Tipo de título
6. Periodicidad
7. Estandarización
b. El registro del código ISIN debe hacerse para todas las operaciones; excepto para las participaciones en fondos abiertos, (“Tipo de título” = 4), y para los títulos que se encuentren en el listado de excepciones que se pondrá a disposición de los regulados en la página web de la Superintendencia General de Valores.
c. En caso de inversiones en reporto tripartito (indicador = RV), se exceptúa la revisión de la consistencia del ISIN con la fecha de vencimiento indicada en el punto a).
d. En el caso de títulos internacionales, cuando el acuse de recibo indique que la información no fue cargada porque existe un error de consistencia entre el ISIN y los datos del punto a), el regulado debe comunicarse con las áreas de supervisión de la Superintendencia General de Valores para analizar el caso.
v) Cuando se trata de una inversión en el mercado de liquidez (Nemotécnico instrumento = ML); se acepta si el “ID_Recompra” es RV. En este caso el precio de mercado (campo 27) debe ser cero.
vi) En el caso de inversiones en valores de participación de fondos abiertos (Tipo de título =4), que no hayan sido adquiridos en el exterior, el nemotécnico del instrumento debe coincidir con el código del fondo, el cual estará disponible en los boletines quincenales de fondos de inversión publicados en la página web de la Superintendencia General de Valores.
vii) Se solicita la serie de la emisión para los títulos que se encuentren en el listado de excepciones que se pondrá a disposición de los regulados en la página web de la Superintendencia General de Valores.
b) En el Anexo 15 de los estados financieros de los fondos de inversión (BG_FONDOS, ER_FONDOS y RA_FONDOS), se adicionan las siguientes cuentas:
ANEXO | CATÁLOGO | No. CUENTA | NOMBRE DE LA CUENTA
15 | BG_FONDOS | 701030010000 | Gastos pagados por anticipado-colones
701030020000 | Gastos pagados por anticipado-otras monedas
701030020100 | Seguros-otras monedas
701030020101 | Seguros - inmuebles-otras monedas
701030020102 | Seguros - proyectos desarrollo-otras monedas
701030020200 | Impuestos-otras monedas
701030020300 | Otros- otras monedas
801004000000 | Valor nominal participaciones
801005000000 | Desembolsos por colocación de participaciones
c) En el Anexo 33 se incorpora la remisión de información sobre el calce de plazos de los fondos de inversión abiertos de largo plazo, que utilicen el esquema de operación dispuesto en el inciso c) del artículo 64 del Reglamento General sobre sociedades administradoras y fondos de inversión y el acuerdo SGV-A-146, se adicionan las siguientes cuentas:
ANEXO | CATÁLOGO | No. CUENTA | NOMBRE DE LA CUENTA
33 | RI_FONDOS | 900000000000 | Índice de Calce de Plazos (Recursos líquidos/Obligaciones)
910000000000 | Recursos Líquidos
911000000000 | Efectivo
912000000000 | Inversiones en fondos del mercado de dinero
913000000000 | Inversiones otros fondos de inversión LP abiertos
914000000000 | Valores de deuda vencimiento a un mes.
915000000000 | Valores estandarizados de deuda de alta y media bursatilidad
916000000000 | Valores del Tesoro, EEUU y de agencias
917000000000 | Mercado de liquidez, recompra a un día hábil BCCR., M. Hacienda.
918000000000 | Letras del tesoro 180 días
919000000000 | Reporto tripartito vendedor a plazo, venc. igual o menor a un mes.
950000000000 | Obligaciones
951000000000 | Sobregiros y comisiones
952000000000 | Cuentas por pagar, sin “sumas recibidas de inversionistas por invertir”
953000000000 | Préstamos de C.P. y pasivos de L.P. con venc. a un mes.
954000000000 | Porción del activo neto exigida a un mes.
d) En seguimiento al Reglamento sobre Gestión de Riesgo, se incorpora el anexo 31 Suficiencia Patrimonial y Control de Límites de conformidad con las siguientes cuentas:
[imagen]
[imagen]
[imagen]
e) En el Anexo 15 de los estados financieros de los fondos de inversión (BG_FONDOS, ER_FONDOS y RA_FONDOS) se modifican los nombres de las siguientes cuentas:
ANEXO | CATÁLOGO | Nº DE CUENTA | NOMBRE ANTERIOR | NOMBRE MODIFICADO
15 | BG_FONDOS | 701030010000 | Gastos pagados por Anticipado | Gastos pagados por anticipado-colones
f) En el Anexo 14 Estados Financieros CO_SAFI se modifican los nombres de las siguientes cuentas:
ANEXO | CATÁLOGO | Nº DE CUENTA | NOMBRE ANTERIOR | NOMBRE MODIFICADO
14 | CO_SAFI | 81909000 | Bienes entregados en Garantía | Bienes entregados en garantía por cuenta propia.
g) En el Anexo 13 Reporte diario de fondos de inversión y en el anexo 33 Indicadores de riesgo se eliminan las siguientes cuentas:
ANEXO | CATÁLOGO | No. CUENTA | NOMBRE DE LA CUENTA
13 | RD_FONDOS | 356500000000, 357000000000, 357500000000, 456500000000, 457000000000, 457500000000, 487000000000, 487500000000, 488000000000, 556500000000, 557000000000, 557500000000, 606500000000, 607000000000, 607500000000, 756500000000, 757000000000, 757500000000, 856500000000, 857000000000, 858500000000 | Código sin Utilizar
33 | RI_FONDOS | 307000000000, 307500000000, 308000000000, 407000000000, 407500000000, 408000000000, 507000000000, 507500000000, 508000000000, 607000000000, 607500000000, 608000000000 | Código sin Utilizar
