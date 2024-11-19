Anexos y Estructuras para la Emisión de
Comprobantes Electrónicos
Version 4.4
Dirección General de Tributación
Noviembre 2024
TABLA DE CONTENIDO
Anexo 1. "Especificaciones Técnicas y Formato de las Estructuras de los Comprobantes Electrónico.....3
I. Introducción ...................................................................................................................................14
II. Especificaciones técnicas y formato de los comprobantes electrónicos ......................................14
a) Datos del Encabezado: ...................................................................................................18
b) Detalle de la mercancía o servicio prestado ....................................................................26
c) Resumen del comprobante /Total de comprobante. Moneda ..........................................49
d) Información de referencia: ...............................................................................................55
e) Otros (Uso comercial, no tributario): ................................................................................57
f) Mecanismo de seguridad: .................................................................................................58
III. Mensajes: .....................................................................................................................................59
IV. Notas sobre el Anexo 1 ................................................................................................................63
Anexo 2. "Mecanismo de seguridad para la autenticación e integridad de los Comprobantes Electrónicos del Ministerio de ..Hacienda"........82
Anexo 3. "Información para la conexión con el API de Comprobantes Electrónicos del Ministerio de Hacienda"........................................94
ANEXO 1. "ESPECIFICACIONES TÉCNICAS Y FORMATO DE LAS ESTRUCTURAS DE LOS COMPROBANTES ELECTRÓNICOS"
Control Histórico de Cambios
VERSIÓN 4.4.
Rige a partir del 01 de junio del 2025, a partir de dicha fecha se deroga la Versión 4.3, esta y versiones anteriores, únicamente se podrán utilizar para generar notas de crédito y débito que ajusten comprobantes emitidos durante su vigencia.
Bitacora 4.4.0
1. Se ajusta la nota 2 incorporando el XML Schema, para los comprobantes "Factura Electrónica de Compra", "Factura Electrónica de Exportación" y "Recibo Electronico de Pago".
Encabezado
2. Se ajusta la descripción del campo "Clave" incluyendo la referencia a la nota 3.
3. Se incluye el campo de "Proveedor de Sistemas" para identificar los sistemas de emisión de comprobantes electrónicos.
4. Se incluye en la nota 3, la codificación correspondiente a los campos de "Clave" y "Consecutivo".
5. Se incluye en la nota 3, el código 10 correspondiente al tipo de comprobante "Recibo Electronico de Pago".
6. Se incluye el campo de "Código de actividad económica del receptor". Se incluye nota al pie sobre la comunicación oportuna para el uso obligatorio de este campo.
7. Se ajusta en el campo "Tipo de identificación del emisor" la descripción de los tipos de identificación, incluyendo el tipo "Extranjero No Domiciliado" para usar únicamente en la factura de compra.
8. Se ajusta en el campo "Tipo de identificación del emisor" la descripción de los tipos de identificación, incluyendo el tipo "No Contribuyente" para usar únicamente en la factura de compra.
9. Se incluye en la nota 4 el código 05 para el tipo de identificación "Extranjero No Domiciliado", junto con nota explicativa al pie de página.
10. Se incluye en la nota 4 el código 06 para el tipo de identificación "No Contribuyente", junto con nota explicativa al pie de página.
11. Se ajusta la descripción y se amplía el tamaño del campo "Número de cédula física/ jurídica/NITE/DIMEX/Extranjero No domiciliado/No contribuyente, del emisor" a 20 caracteres cuando se use el código 05 de la nota 4.
12. Se incluye el campo de "Registro fiscal de bebidas Alcohólicas Ley 8707".
13. Se ajusta la condición del campo "Nombre Comercial Emisor" a Opcional.
14. Se convierte el nodo de "Ubicación" para el emisor en condicional para la Factura Electrónica de Compra cuando en el campo "Tipo de identificación del emisor" se esté utilizando el código 05 y 06 de la nota 4, donde no será obligatorio.
15. Se ajusta la condicionalidad del campo "Barrio" de condicional a opcional y se habilita la escritura.
16. Se incluye el campo "Otras Señas Extranjero" de uso exclusivo en la Factura Electrónica de Compra para cuando en el campo "Tipo de identificación del emisor" se este utilizando el código 05 de la nota 4.
17. Se ajustan descripciones del campo "Número de Teléfono" en el nodo "Teléfono" tanto para el emisor como para el receptor, estableciéndose un mínimo de 8 dígitos y un máximo de 20.
18. Se elimina el nodo de "Fax", tanto para el nodo del emisor como para el nodo del receptor.
19. Se amplía el número de repeticiones del campo "Dirección de correo electrónico del emisor" a cuatro y se ajusta la condición del campo a condicional en factura de compra.
20. Se incluye en la nota 5 de "Condiciones de la Venta", el código 12 para "Venta de Mercancía No Nacionalizada" para el comprobante de factura electrónica, junto con nota explicativa al pie de página.
21. Se incluye en la nota 5 de "Condiciones de la Venta", el código 13 para "Venta Bienes Usados No Contribuyente" para el comprobante de factura electrónica, junto con nota explicativa al pie de página.
22. Se incluye en la nota 5 de "Condiciones de la Venta", el código 14 para "Arrendamiento Operativo", junto con nota explicativa al pie de página.
23. Se incluye en la nota 5 de "Condiciones de la Venta", el código 15 para "Arrendamiento Financiero", junto con nota explicativa al pie de página.
24. Se ajusta en la nota 5 la descripción del pie de página del código 09 "Pago de servicios prestado al Estado".
25. Se ajusta en la nota 5 la descripción del pie de página del código 11 "Pago de venta a crédito en IVA hasta 90 días (Artículo 27, LIVA)".
26. Se ajusta la condición del nodo "Identificación del Receptor" en factura electrónica de exportación a obligatorio.
27. Se ajusta la descripción del campo "Tipo de identificación del receptor" aclarando cuando usar el tipo de identificación "Extranjero No Domiciliado" en cada comprobante; cuando se use el código 05 de la nota 4.
28. Se ajusta la descripción y se amplía el tamaño del campo "Número de cédula física/ jurídica/NITE/DIMEX/Extranjero No domiciliado, del receptor" a 20 caracteres
29. Se elimina el campo "Número de identificación en caso que el Receptor sea Extranjero".
30. Se ajusta condición del campo "Nombre Comercial Receptor" a opcional.
31. Se amplía descripción de la condición del nodo "Ubicación" para el receptor, deshabilitando su uso para el tipo de identificación "Extranjero No Domiciliado" y se pasa a opcional en caso de Tiquete Electrónico.
32. Se ajusta la condición del campo "Otras señas Extranjero" a condicional en el comprobante Factura Electrónica, cuando el tipo de identificación es "Extranjero No Domiciliado" e inexistente para el comprobante Factura Electrónica de Compra.
33. Se ajusta descripción del campo "Condiciones de la Venta" especificando el uso exclusivo del código 12 de la nota 5, en el comprobante Factura Electrónica.
34. Se incluye el campo "Detalle Condición de la Venta OTRO" de uso obligatorio en caso de utilizar el código 99 de "Otros" de la nota 5.
35. Se modifica el campo "Plazo de crédito" a un campo "Interger" de 5 posiciones, debiendo expresarse en días.
36. Se traslada el nodo de "Medio de Pago" al Apartado "Resumen del Comprobante/Total del Comprobante" el nodo de "Medio de Pago".
Detalle de la mercancía o servicio prestado
37. Se ajusta la descripción del nodo "Detalle del Servicio, Mercancía u otro" aclarando la condicionalidad de su uso obligatorio en el comprobante Factura Electrónica, excepto cuando se use se seleccione el código 04, 08, 09 y 10 de la nota 16 en el campo "Tipo de documento otros cargos" y no cuente con una línea de servicio o producto.
38. Se ajusta la descripción del campo "Partida Arancelaria" aclarando su condición obligatoria cuando se utilice un código CAByS de mercancías, en la factura de exportación
39. Se ajusta la etiqueta y descripción del campo "Código de Producto/Servicio", aclarando la condición obligatoria de este campo en las notas de crédito y débito, así como sus excepciones
40. Se ajusta la descripción y la condición del nodo "Código Comercial", a condicional cuando se utilicen códigos CAByS de combos/surtidos/paquetes.
41. Se ajusta la descripción del campo "Tipo de Código de producto/servicio" del nodo "Código Comercial" para cuando se utilicen códigos CAByS de combos/surtidos/paquetes.
42. Se ajusta la descripción del campo "Código" del Nodo "Código Comercial" para cuando se utilicen códigos CAByS de combos/surtidos/paquetes
43. Se ajusta la nota 15, clasificando las unidades de medida para los servicios y las mercancías.
44. Se incluyen en la nota 15, las siguientes unidades de medida: Acv, Fa, Cc, Cu y Qq.
45. Se incluye el campo "Tipo de transacción" de condición condicional, para el caso de transacciones con tratamientos tributarios específicos según la necesidad de las partes.
46. Se incluye la nota 22 para Tipo de Transacción.
47. Se ajusta la condición del campo "Detalle de la mercancía transferida o servicio prestado" a obligatorio en todos los comprobantes.
48. Se incluye el campo de "Número de VIN o Serie" de los vehículos de transporte y se incluye notas explicativas al pie de página.
49. Se incluye el Nodo de "Detalle de Productos del Surtido" que será de condición obligatoria para cuando se utilicen códigos CAByS de combos/surtidos/paquetes, junto con nota explicativa al pie de página. Cuenta con la posibilidad de tener hasta 20 repeticiones.
50. Se ajusta la descripción de campo "Monto de descuentos concedidos", y la condición del campo a obligatorio.
51. Se incluye la nota 20 para los tipos de descuentos a utilizar en el campo de "Código del Descuento".
52. Se incluye el campo "Código del descuento" de condición obligatoria para la identificación de los descuentos detallados en la nota 20.
53. Se incluye el campo "Código del descuento OTRO" de uso obligatorio en caso de utilizar el código 99 de "Otros Descuentos" de la nota 20.
54. Se ajusta la descripción del campo "Naturaleza del Descuento" de uso obligatorio cuando se utilice el código 99 de la nota 20
55. Se incluye el campo denominado "IVA cobrado a nivel de fábrica".
56. Se incluye la nota 21 para el "IVA cobrado a nivel de fábrica"
57. Se ajusta el nombre del campo "Base Imponible Especial" a "Base Imponible".
58. Se ajusta la condición del campo "Base Imponible" a obligatorio y se amplía la descripción para su uso.
59. Se ajusta el número de repeticiones del campo "Impuesto" a {1,1000}, se hace campos obligatorio y se amplia su descripción .
60. Se ajusta la descripción "Código de Impuesto" indicando para el caso de las Regalías y Bonificaciones los campos a usar para el cálculo del IVA .
61. Se incluye el campo "Código de impuesto OTRO" de uso obligatorio en caso de utilizar el código 99 de "Otros" de la nota 8.
62. Se ajusta la etiqueta "Código Tarifa" por "Código Tarifa IVA" y el nombre del Campo "Código de la Tarifa del impuesto" por "Código de la tarifa del Impuesto al Valor Agregado".
63. Se incluye en la nota 8, nota explicativa al pie de página, para el uso del código de impuesto 07 "IVA cálculo especial"
64. Se ajusta la descripción del campo "Código de la tarifa del Impuesto al Valor Agregado".
65. Se modifica en la nota 8.1 el nombre del código 01 de "Tarifa 0% (Exento)" por "Tarifa 0% (Artículo 32, num 1, RLIVA)" junto con nota explicativa al pie de página.
66. Se incluye para la nota 8.1 notas explicativas para el uso exclusivo del código 05 de "Transitorio 0%" y del código 06 de "Transitorio 4%" en notas de crédito y débito
67. Se modifica en la nota 8.1 el nombre del código 07 de "Transitorio 8%" por tarifa transitoria 8%. (Código Inhabilitado)
68. Se incluye en la nota 8.1 el código 09 de "Tarifa reducida 0.5%".
69. Se incluye en la nota 8.1 el código 10 de "Tarifa Exenta" y se incluye notas explicativas al pie de página para el uso exclusivo del código 10.
70. Se incluye en la nota 8.1 el código 11 de "Tarifa 0% sin derecho a crédito" y se incluye nota explicativa al pie de página.
71. Se amplía la descripción del campo "Tarifa del Impuesto" para efectos del uso y condición del campo de acuerdo con cada código de impuesto de la nota 8 que utilice tarifa para su cálculo.
72. Se modifica el nombre del campo "Factor del impuesto" por "Factor Cálculo IVA" y se amplía la descripción sobre el formato de uso decimal.
73. Se incluye el nodo "Datos para Impuestos Específicos" de condición obligatoria, cuando se utilicen los códigos de impuesto 03, 04, 05, 06 de la nota 8 y agrupará los campos requeridos para el cálculo de estos impuestos.
74. Se ajusta la descripción del campo "Monto del Impuesto" explicando el cálculo correspondiente para cada código de impuesto de la nota 8.
75. Se modifica en la nota 10.1 el nombre del código 01 de "Compras autorizadas por la Dirección General de Tributación". (Código Inhabilitado).
76. Se modifica en la nota 10.1 el nombre del código 04 de "Exenciones Dirección General de Hacienda" por "Exenciones Dirección General de Hacienda Autorización Local Genérica".
77. Se modifica en la nota 10.1 el nombre del código 05 de "Transitorio V" por "Exenciones Dirección General de Hacienda Transitorio V (servicios de ingeniería, arquitectura, topografía obra civil)". (Código Inhabilitado)
78. Se modifica en la nota 10.1 el nombre del código 06 de "Transitorio IX" por "Servicios turísticos inscritos ante el Instituto Costarricense de Turismo (ICT)". (Código Inhabilitado)
79. Se modifica en la nota 10.1 el nombre del código 07 de "Transitorio XVII" por "Transitorio XVII (Recolección, Clasificación, almacenamiento de Reciclaje y reutilizable)". (Código Inhabilitado)
80. Se incluye en la nota 10.1 el código 08 de "Exoneración a Zona Franca".
81. Se incluye en la nota 10.1 el código 09 de "Exoneración de servicios complementarios para la exportación según articulo 11 RLIVA".
82. Se incluye en la nota 10.1 el código 10 de "Órgano de las corporaciones municipales".
83. Se incluye para la nota 10.1 el código 11 de "Exenciones Dirección General de Hacienda Autorización de Impuesto Local Concreta" y se incluye notas explicativas al pie de página para el uso exclusivo del código 11.
84. Se ajusta la etiqueta del campo "TipoDocumento" a "TipoDocumentoEX".
85. Se incluye el campo "Tipo de documento de exoneración o de autorización OTRO" de uso obligatorio en caso de utilizar el código 99 de "Otros" de la nota 10.1.
86. Se incluye el campo "Número de artículo que establece la exoneración o autorización" que será de condición obligatoria cuando se usen los códigos 02, 03 o 08 de la nota 10.1.
87. Se incluye el campo "Número de inciso que establece la exoneración o autorización" que será de condición obligatoria cuando se use el campo "Número de artículo que establece la exoneración o autorización".
88. Se ajusta la descripción del campo "Nombre de Institución o dependencia que emitió la exoneración" para aplicar la codificación de la nota 23.
89. Se incluye la nota 23 para el campo "Nombre de Institución o dependencia que emitió la exoneración".
90. Se incluye el campo "Nombre Institución Otros" que será de condición obligatoria en el caso de utilizar el código 99 de "OTRO" de la nota 23.
91. Se ajusta la etiqueta del campo "FechaEmision" a FechaEmisionEX.
92. Se ajusta en la descripción del campo "Monto del Impuesto Exonerado" el cálculo al establecido en la bitácora del 21 de mayo del 2020.
93. Se incluye el campo "Impuestos Asumidos por el Emisor o cobrado a Nivel de Fábrica".
94. Se ajusta descripción del campo "Impuesto Neto" sustituyendo 100% por 13%.
95. Se ajusta la descripción sobre el cálculo del campo "Impuesto Neto" incorporando la resta del monto del campo "Impuestos Asumidos por el Emisor o cobrado a Nivel de Fábrica".
96. Se ajusta la descripción sobre el cálculo del campo "Total por Línea de Detalle" incorporando el campo "Impuestos Asumidos por el Emisor o cobrado a Nivel de Fábrica" en las reglas de cálculo
97. Se ajusta la etiqueta del campo "TipoDocumento" a "TipoDocumentoOC".
98. Se ajusta el nombre del campo a "Tipo de documento otros cargos".
99. Se incluye el campo "Tipo de documento OTRO" de uso obligatorio en caso de utilizar el código 99 de "Otros" de la nota 16.
100. Se crea anidamiento para la identificación del tercero e incluye el campo denominado "Tipo de identificación del Tercero" al nodo de "Otros Cargos".
101. Se ajusta la etiqueta del campo "Porcentaje" a "PorcentajeOC".
102. Se ajusta el nombre del campo "Porcentaje otros cargos".
103. Se incluye en la nota 16 el código 08 de "Depósitos de Garantía"
104. Se incluye en la nota 16 el código 09 de "Multas o Penalizaciones"
105. Se incluye en la nota 16 el código 10 de "Intereses Moratorios"
Resumen del comprobante /Total de comprobante:
106. Se ajusta la condicionalidad del nodo "Código y Tipo de Moneda" a obligatorio en todos los comprobantes.
107. Se ajusta el texto de la nota 13.
108. Se ajusta texto en la nota 13.1 actualizando la versión del documento donde se encuentran los códigos de moneda "Codigodemoneda_V4.4".
109. Se ajusta condicionalidad del campo "Código de la Moneda" a obligatoria en los comprobantes "Nota de Crédito Electrónica" y "Nota de Débito Electrónica".
110. Se ajusta la descripción y condición del campo "Tipo de Cambio" a obligatorio en los comprobantes "Nota de Crédito Electrónica" y Nota de Débito Electrónica".
111. Se ajusta descripción del campo "Total servicios gravados con IVA" ampliando la explicación sobre el cálculo del campo.
112. Se ajusta descripción del campo "Total servicios exentos de IVA" ampliando la explicación sobre el cálculo del campo.
113. Se incluye el campo "Total servicios No Sujetos de IVA" con la explicación sobre el cálculo del campo.
114. Se aclara el cálculo del campo "Total mercancías gravadas con IVA" ampliando la explicación sobre el cálculo de campo.
115. Se ajusta descripción del campo "Total mercancías exentas de IVA" ampliando la explicación sobre el cálculo del campo.
116. Se ajusta descripción del campo "Total mercancías exoneradas de IVA" ampliando la explicación sobre el cálculo del campo.
117. Se incluye el campo "Total mercancías No Sujetas de IVA" con la explicación sobre el cálculo del campo.
118. Se incluye el campo "Total No Sujeto" con la explicación sobre el cálculo del campo.
119. Se ajusta la descripción del campo "Total Venta" ampliando la explicación sobre el cálculo del campo.
120. Se ajusta la descripción del campo "Total de Impuesto" ampliando la explicación sobre el cálculo del campo.
121. Se incluye el nodo "Total Desglose por Impuesto Cobrado" con la explicación sobre el cálculo del campo.
122. Se ajusta el campo "Total de Impuestos Asumidos por el Emisor o cobrado a Nivel de Fábrica" con la explicación sobre el cálculo del campo.
123. Se incluye en la nota 6 de medios de pago el código 6 "SINPE MOVIL", el código 07 "Plataforma Digital".
124. Se incluye el nodo de "Medio de Pago" con la explicación sobre el cálculo del campo.
125. Se amplía la descripción del campo "Total del Comprobante" ajustando la regla del campo para que el resultado del cálculo coincida con la sumatoria de los montos por "Medio de Pago".
Información de Referencia
126. Se amplía la descripción y se ajusta la condicionalidad del apartado de Información de Referencia, en "Factura Electrónica" cuando se utilicé el código 11 de la nota 10.1 en el campo ""Tipo de documento de autorización o exoneración, así como en "Factura Electrónica de Compra".
127. Se ajusta la etiqueta del campo "TipoDoc" a "TipoDocIR".
128. Se incluye el campo "Tipo de documento de referencia OTRO" de uso obligatorio en caso de utilizar el código 99 de "Otros" de la nota 10.
129. Se ajusta la etiqueta del campo "FechaEmision" a "FechaEmisionIR".
130. Se incluye en la nota 9 el código 06 "Devolución de mercancía"
131. Se incluye en la nota 9 el código 07 "Sustituye Comprobante electrónico".
132. Se incluye en la nota 9 el código 08 "Factura Endosada".
133. Se incluye en la nota 9 el código 09 "Nota de crédito financiera".
134. Se incluye en la nota 9 el código 10 "Nota de débito financiera".
135. Se incluye en la nota 9 el código 11 "Proveedor No Domiciliado".
136. Se incluye en la nota 9 el código 12 "Crédito por exoneración posterior a la facturación"
137. Se incluye el campo "Código de referencia OTRO" de uso obligatorio en caso de utilizar el código 99 de la nota 9.
138. Se inhabilita en la nota 10 el código "Devolución mercadería" y se incluye notas explicativas al pie de página.
139. Se ajusta en la nota 10 el nombre del código 10 "Sustituye factura rechazada por el Ministerio de Hacienda" por "Comprobante electrónico rechazado por el Ministerio de Hacienda".
140. Se ajusta en la nota 10 el nombre del código 14 "Comprobante aportado por contribuyente del Régimen de Tributación Simplificado" por "Comprobante aportado por contribuyente de Régimen Especial".
141. Se incluye en la nota 10 el código 16 "Comprobante de Proveedor No Domiciliado".
142. Se incluye en la nota 10 el código 17 "Nota de Crédito a Factura Electrónica de Compra".
143. Se incluye en la nota 10 el código 18 "Nota de Débito a Factura Electrónica de Compra"
Otros ( Uso comercial, no tributario.)
144. Se ajusta el tamaño del campo "Otro Texto" a 500 caracteres.
145. Se ajusta el tipo y tamaño del campo "Otro Contenido" a String y 500 caracteres.
Mecanismo de Seguridad
146. Se ajusta la descripción del nodo de firma actual, ampliando el uso del estándar actual permitiendo la inclusión de la firma de receptor en comprobantes a crédito y las firmas para endoso.
Fin de ajustes versión 4.4
Modificada al 12 de noviembre del 2024 (Aplicación a partir del 01-01-2025)
1. Se incluye el campo de "Registro de medicamento" para incluir el respectivo número de registro del Ministerio de Salud.
2. Se incluye el campo "forma farmacéutica" para agregar código de la presentación del medicamento.
3. Se incluye la nota 19 para "Forma Farmacéutica"
Modificada al 12 de junio del 2023 (Aplicación a partir del 12/09/2023)
1. Se agrega a la nota 5 de condición de la venta el campo "Venta a crédito en IVA hasta 90 días (Artículo 27, LIVA)" código 10, con su respectiva nota al pie explicativa.
2. Se agrega a la nota 5 de condición de la venta el campo "Pago de venta a crédito en IVA hasta 90 días (Artículo 27, LIVA)" código 11, con su respectiva nota pie explicativa.
3. Se agrega a la nota 8.1 de tarifa impuesto Valor Agregado el campo "Tarifa reducida 0.5%" código 09.
4. Se modifica el nombre del campo "Porcentaje de la Exoneración" por "Tarifa exonerada"; asimismo, se ajusta el tipo de campo a "Decimal" y el tamaño a 4,2 (cuatro comas dos) caracteres.
Modificada al 21 de mayo del 2020
1. Se modifica la entrada en vigencia de la obligatoriedad del campo "Código de Producto/servicio" a partir del 01 de diciembre del 2020.
2. Se modifica la fórmula de cálculo del campo denominado "Monto de Impuesto exonerado" a partir del 01 de julio del 2020. La misma se modifica de la siguiente manera se obtiene de la multiplicación del campo "porcentaje de la exoneración" por el campo "Subtotal".
Modificada al 19 de agosto del 2019
1. Incluye códigos en la nota 10, para sustituir la factura electrónica de compra (FEC)
Cambio 22/03/2019 versión 4.3, Rige a partir del 1 de julio del 2019 a partir de dicha fecha se deroga la Versión 4.2.y únicamente se podrá utilizar la versión 4.3.
Condición de Campos
1. Se Incluye en condición de los Campos el código "04 = Inexistente".
2. Se incluye las abreviaturas para los tipos de comprobante "Factura Electrónica de Exportación" y "Factura Electrónica de Compra"
Datos de encabezado
3. Se agrega el campo "Código de la actividad económica".
4. Se amplía el tamaño de los caracteres del nombre tanto para el emisor como para el receptor.
5. Se amplía el tamaño de los caracteres del campo "Otras señas".
6. Se incluye el campo "Otras señas Extranjero".
Detalle de la mercancía o servicio prestado
7. Se modifica el nombre del campo "Detalle de servicio".
8. Se agrega el campo de "Partida Arancelaria", para la Factura de Exportación.
9. Se agrega el campo "Código de Producto/servicio "y se incluye la Nota 17 relacionada a dicho campo.
10. Se amplía el tamaño del campo "Detalle".
11. Se amplía el campo "Descuentos" con el fin de permitir un máximo de 5 repeticiones de descuentos.
12. Se agrega el campo "Base Imponible", para contribuyentes con cálculos especiales.
13. Se modifica el contenido de la nota 8 y se eliminan las exenciones de la tabla.
14. Se convierte en obligatorio el campo de código de impuesto y se incluye la nota 8.1 de "Tarifas y Códigos".
15. Se incluye el campo denominado "Factor del impuesto" para aquellos productos que posean un factor para el cálculo del impuesto.
16. Se amplía la descripción del campo "Monto", para explicar el cálculo del mismo.
17. Se agrega el campo "Monto de impuesto de exportación".
18. Se amplían los tamaños de los campos "Número de documento" y "Nombre de la Institución" para el nodo de exoneraciones.
19. Se modifica el cálculo del campo denominado "Monto del Impuesto Exonerado".
20. Se agrega el campo "Impuesto Neto" para el apartado de exoneración, así como su respectivo cálculo.
21. Se agrega el nodo de "Otros Cargos" y se incluye la Nota 16 relacionada a dicho campo.
Resumen de la factura/Total de la Factura
22. Se convierte el campo "Código de la moneda" y "Tipo de cambio" en un campo complejo denominado "Código y tipo de moneda".
23. Se incluye el campo "Total de servicios exonerados de IVA".
24. Se incluye el campo "Total de mercancías exoneradas de IVA".
25. Se incluye el campo "Total servicios exonerados del IVA."
26. Se incluye el campo "Total IVA Devuelto".
27. Se incluye el campo "Total Otros cargos".
Mensaje del Obligado Tributario para la confirmación.
28. Se agrega el formato de las cédulas.
29. Se incluye el campo "Código de la actividad económica".
30. Se incluye el campo "Condición del IVA", así como la nota 18".
31. se incluye el campo "Monto del impuesto acreditar".
32. se incluye el campo "Monto total del gasto a aplicar".
Otros cambios
33. Se modifica el contenido de las siguientes notas: Nota 5, Nota 8, Nota 10, Nota 10.1, Nota 15.
34. Se agregan las notas: Nota 8.1, Nota 16, Nota 17, Nota 18.
NOTA: Así mismo, se modifica el artículo 4º de la resolución Nº DGT-R-48-2016 de las 08:00 horas del día 7 de octubre de 2016, inciso "c" y se incluyen los siguientes códigos:
Factura electrónica de compra | 08
Factura electrónica de exportación | 09
Cambio 17/07/2017 versión 4.2 (Rige a partir del 1 de octubre del 2017)
1. Se modifica el catálogo de impuestos incluyendo el Impuesto Específico al Cemento.
2. se incluye el uso de caracteres especiales para el correo electrónico.
Se realizan los siguientes ajustes.
. Se incorpora márgenes de error en los decimales, para que aquellos contribuyentes cuyos sistemas funcionan con dos decimales puedan seguir trabajando sin ningún problema aplicando el método de redondeo a dos decimales, tanto para la versión 4.1 como 4.2.
. se permite para la facturación de bonificaciones ingresar en el campo "Subtotal" el valor "0", con el fin de no cobrar el producto al cliente, pero si facturar el impuesto de ventas, tanto para la versión 4.1 como 4.2 y en adelante cualquier otra versión.
Cambios 20/02/2017 (Resolución DGT-R-13-2017) versión 4.1
1. Se modifica el campo de cantidad a 3 decimales.
2. Se ajusta la versión del XAdES EPES a v1.3.2 o superior.
3. Se corrige la cardinalidad del dato tarifa en el ImpuestoType para que sea 1 a 1.
4. Se agrega aclaración para interpretar el anidamiento en las tablas, caracteres >.
Cambios 07/10/2016 (Resolución DGT-R-48-2016) versión 4.0
1. Se unifica en una única tabla las estructuras de los comprobantes electrónicos (Factura, Tiquete, Nota de crédito y Nota de débito).
2. Se amplía las líneas de detalle en el apartado "detalle de la mercancía o servicio prestado" de la factura electrónica a un máximo de 1000 líneas.
3. Se agrega el nodo de clave numérica de 50 dígitos.
4. Se incluye la lista de los códigos de impuesto.
5. Se modifica la estructura del consecutivo de la numeración, a veinte dígitos alfanuméricos.
6. En documentos de referencia se incluye el comprobante emitido en contingencia.
7. Se incluye un nodo para Exoneraciones o Compras Autorizadas.
8. Se incluye la estructura de mensajes de aceptación o rechazo.
9. Se elimina las estructuras XML de la información electrónica de compras y ventas.
10. Se incorpora el nodo de provincia, cantón, distrito y barrio. Se adjunta tabla de la división territorial.
11. Se incorpora la tabla de unidades de medida.
12. Se agrega la columna denominada "Descripción" en la estructura, para una mayor claridad.
13. Se agrega el nodo de plazo del crédito y la nota para dichos plazos.
14. Se agrega el nodo de tipo de identificación.
Cambios 22/07/2011
1. Se introduce el tiquete electrónico para que opere en los puntos de venta.
2. Se limita las líneas de detalle en la factura electrónica a un máximo de 60 líneas y en el tiquete electrónico a un máximo de 1000 líneas de detalle.
3. Se incluye la sección de "firma digital" para hacer obligatorio el uso de la firma digital en la factura electrónica, tiquete electrónico, aceptación y rechazo, información electrónica de ventas, compras y ventas/compras.
4. Se incluye en la sección del receptor el campo opcional de identificación del extranjero en la factura electrónica, tiquete electrónico y en la información electrónica de ventas.
5. Se crea el anexo 3.
I. Introducción
En la definición del contenido del presente documento, se ha considerado tanto la necesidad desde el punto de vista tributario, como comercial. El objetivo es tener un documento que sea un instrumento adecuado para el respaldo de la transacción, desde el punto de vista de las partes y que contenga la información que se requiere para efectos de un control tributario efectivo. En este anexo se describe el formato electrónico de los comprobantes electrónicos definidos en la normativa vigente, así como el formato de los mensajes de confirmación.
II. Especificaciones técnicas y formato de los comprobantes electrónicos
La Dirección General de Tributación (DGT) ha decidido que el formato en que se generarán los documentos tributarios electrónicos sea XML (Extensible Markup Language) o Lenguaje Extensible de "Etiquetado". Este metalenguaje proporciona una forma de aplicar etiquetas para describir las partes que componen un documento, permitiendo además el intercambio de documentos entre diferentes plataformas.
El tipo de información puede ser alfanumérica, en estos tipos de información el tamaño indicado es el largo máximo. En la información alfanumérica, algunos caracteres como '&' y '<' tienen un significado especial para XML y deben ser reemplazados por la secuencia de escape que el estándar define para dichos caracteres. El algoritmo de Canonicalización debe ser de la versión C14n-20010315
En la información de tipo numérica, los decimales se separan con punto y no debe separarse los miles con carácter alguno. Adicionalmente, se debe de utilizar el siguiente método de redondeo:
. Cuando el dígito es menor que 5 y el siguiente decimal es menor que 5, el anterior no se modifica.
Ejemplo: 20.203512. Redondeando a 5 decimales se debe tener en cuenta el sexto decimal: 20.203512 ? 20.20351.
. Cuando el dígito es mayor o igual que 5 y el siguiente decimal es mayor o igual que 5, el anterior se incrementa en una unidad.
Ejemplo: 20.203518. Redondeando a 5 decimales se debe tener en cuenta el sexto decimal: 20.203518 ? 20.20352
La modalidad tecnológica de transmisión del documento electrónico, desde el emisor al receptor electrónico, debe ser acordada entre ambos, respetando el estándar establecido por la DGT.
Toda corrección de un documento electrónico debe ser realizada vía nota de crédito o débito electrónica ya que no se permite la modificación ni la eliminación del mismo.
Los comprobantes electrónicos están constituidos por los siguientes apartados:
a) Datos de Encabezado: corresponden a la versión, numeración e identificación del documento electrónico, condiciones de la venta, información del emisor y la información del receptor.
b) Detalle de la Mercancía o Servicio Prestado: En esta parte se debe detallar una línea por cada artículo, especificando cantidad, valor, impuestos adicionales y valor neto, así como descuentos y recargos que afectan al total del documento y que no se requiere especificar individualmente, así como el monto total de la transacción.
c) Resumen del Comprobante /Total de Comprobante: Corresponde a la totalización de los montos del comprobante electrónico.
d) Información de Referencia: Se deben detallar la razón y/o los documentos de referencia, por ejemplo, se debe identificar la factura que se está modificando con una nota de crédito o de débito; y en el caso de comprobantes electrónicos que sustituyen comprobantes físicos emitidos por contingencia, se debe hacer referencia al comprobante provisional.
e) Otros: comprende la información requerida para las relaciones de comercio electrónico entre las partes, que no contravenga lo establecido en la presente resolución.
f) Mecanismo de Seguridad: En esta sección se debe incluir la firma digital o el método de seguridad emitido por el Ministerio de Hacienda sobre todo el documento, para garantizar la integridad del mismo.
Nota: Solamente se permite el uso de un mecanismo de seguridad a la vez, no obstante, si el obligado tributario por su giro comercial decide pasarse de un método de seguridad a otro puede hacerlo.
El formato para los documentos electrónicos es único, así como en su forma electrónica o impresa, lo que los diferencia es la obligatoriedad de los campos según el tipo de documento. Adicionalmente, este documento contempla el formato de los archivos XML de confirmación (aceptación y rechazo) de los comprobantes electrónicos.
Tipos de Nodos y Campos
. ComplexType: Permite definir elementos de estructuras complejas, estos contienen otros elementos hijos y atributos
. String: Cadena de caracteres estos pueden ser alfanuméricos
. Integer: Número entero que puede ser aproximadamente en el rango de -2,147,483,648 a +2,147,483,648
. Decimal: Número real que permite controlar la cantidad de dígitos enteros y decimales
. DateTime: Tipo de dato para almacenar fecha y hora, su formato es "YYYY-MM-DD HH:MM:SS"
. Alfa Numérico: Es un formato que puede contener letras y números conjuntamente
. PositiveInteger: Es un entero positivo
. AnyOtherType: En este elemento se puedo ingresar cualquier formato que se necesite
. ds:SignatureType: Tipo que se ampara bajo el w3c (http://www.w3.org/Signature/) que permite la firma del documento XML
Condición de los campos
Los códigos de condición que se utilizarán para asignar a cada uno de los campos según el comprobante electrónico a utilizar son los siguientes:
. Condición 1. Campo Obligatorio: El dato debe estar en el documento siempre, independiente de las características de la transacción.
. Condición 2. Campo Condicional: El dato no es obligatorio en todos los documentos, pero pasa a ser obligatorio en determinadas operaciones si se cumple una cierta condición o circunstancia especial que posea la transacción. Por ejemplo:
o Si hay descuento, se volverá obligatorio el campo "detalle de descuento". Cuando se aplica un descuento se debe indicar a que corresponde ese descuento.
o Si el receptor goza de exoneración, se deberán incluir los datos del beneficio en apartado de exoneraciones. Caso contario no llena este apartado.
o Si en la factura se encuentra el dato el mismo debe de existir en las notas de crédito y débito.
. Condición 3. Campo Opcional: Si la persona lo desea puede indicarlo
. Condición 4. Campo Inexistente: No debe de ser utilizado, por ejemplo, exoneraciones en el tipo de comprobante "Factura electrónica de Exportación".
Tipo de Comprobante Electrónico
Para asignar la condición de cada nodo o campo según corresponda, los tipos de comprobantes electrónicos se identificarán en el presente documento de la siguiente manera:
. FE: Factura Electrónica
. FEE: Factura Electrónica Exportación
. FEC: Factura Electrónica Compra
. TE: Tiquete Electrónico
. NC: Nota de Crédito
. ND: Nota de Débito
. REP: Recibo Electrónico de Pago
Cada tipo de comprobante electrónico tiene su respectivo XML Schema y su etiqueta. Ver nota 2.
Validaciones según el nivel:
La plataforma de validación verificará los XML en el siguiente orden:
. Nivel 1. Cumplimiento de la estructura vigente: Que el XML tenga los campos establecidos en la estructura vigente.
No Cumple: Se rechaza XML ? Se emite mensaje con detalle de rechazo al sistema emisor.
Si cumple: Pasa a la siguiente verificación.
. Nivel 2. Cumplimiento con el formato de los campos: Que los campos cuenten con las características y formatos definidos en la estructura vigente.
No Cumple: Se rechaza XML ? Se emite mensaje con detalle de rechazo al sistema emisor.
Si cumple: Pasa a la siguiente verificación.
. Nivel 3. Validación de información en la base de datos del Ministerio de Hacienda: En los campos donde se indique, se verificará que la información del campo en el XML coincida con lo registrado ante la administración de tributaria o en los registros de referencia correspondientes a ese campo.
No Cumple: Se rechaza XML ? Se emite mensaje con detalle de rechazo al sistema emisor.
Si cumple: ? Se acepta XML
? Se emite mensaje de aceptación al sistema emisor.
Validaciones Generales
Con el fin de poder asegurar un mejor control se implementan las validaciones genéricas de las cuales van aplicar en los casos donde en el campo de regla para la validación aparezca: "sin validación" y por lo tanto el campo deberá de realizar la siguiente acción:
1. Cuando en un campo de la estructura hace referencia a una "Nota" del documento de Anexos y estructuras se debe de validar los códigos de esta nota.
2. Debe de validar los códigos CAByS en los campos lo indique.
3. Los campos que llevan "Cálculos" se debe de cumplir con la fórmula planteada en la descripción, caso contrario se rechaza.
a) Datos del Encabezado:
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
Clave | Clave del comprobante | String | 1 | ?Ver notas , 3 y 4. ?Debe cumplir con la estructura con respecto a tamaño y posición de los campos, tal como se establece en las notas 3 y 4. ?Es un campo fiCo de cincuenta posiciones y se tiene que utilizar para la consulta del código QR. ?Solo permite ingresar números. ?Validación: Se verificará que la información en el campo cumpla con las notas Nº , 3 y 4. , caso contrario se rechazará el comprobante. | | | | | | |
Proveedor Sistemas | Proveedor de sistemas para emisión de Comprobantes | String | 2 | ?Se debe indicar el número de cedula de identificación del proveedor de sistemas que esté utilizando para la emisión de comprobantes electrónicos. En caso de ser un desarrollo propio o a la medida, se deberá indicar la Identificación del mismo obligado tributario. ?Validación: se verificará que sea un código valido y que cumpla con el formato del número de identificación establecidos en el campo número de cedula física/ Curídica/ NITE/ DIMEX/ EXTRANJERO NO DOMICILIADO/ NO CONTRIBUYENTE DEL EMISOR. ?El proveedor de sistemas debe estar inscrito ante la Administración Tributaria en el Registro Único Tributario, caso contrario, se realizará la advertencia correspondiente. | | | | | | |
CodigoActividadEmisor | Código de la Actividad Económica del Emisor | String | 6 | ?Se debe de indicar el código de la actividad económica inscrita a la cual corresponde el comprobante que se está generando. ?Validación: Se verificará que sea un código valido (código existente en el padrón del RUT) caso contrario se rechazará. ?Adicionalmente se verificará si se incluye un código diferente al inscrito en el Registro Único Tributario (RUT), en cuyo caso se realizará la advertencia correspondiente. | | | 3 | | | | 4
[imagen] 1 CodigoActividadReceptor | Código de la Actividad Económica del Receptor | String | 6 | ?Se debe de indicar el código de la actividad económica inscrita del receptor a la cual corresponden los bienes o servicios que se le están facturando al receptor en caso de ser requerido para un crédito o un gasto deducible. [imagen] ?Validación: Se verificará que sea un código valido (código existente en el padrón del RUT) caso contrario se rechazará. ?Adicionalmente se verificará si se incluye un código diferente al inscrito en el Registro Único Tributario (RUT), en cuyo caso se realizará la advertencia correspondiente. | 2 | 4 | | 4 | 2 | 2 | 4
[imagen]
1 En el caso del tipo de comprobante "Factura Electrónica", el Ministerio de Hacienda comunicará oportunamente el cambio de este campo a condición obligatoria
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
NumeroConsecutivo | Numeración consecutiva del comprobante | String | 20 | ?Ver notas y 3. Es un campo fijo de veinte posiciones. Solo permite ingresar números. ?Validación: Se verificará que la información en el campo cumpla con las notas Nº y 3 caso contrario se rechazará el comprobante. Adicionalmente se verificará el cumplimiento de la secuencia en la generación de la numeración consecutiva de acuerdo a los parámetros establecidos para la misma. | | | | | | |
FechaEmision | Fecha de Emisión del comprobante | DateTime | | ?Tipo de dato de fecha y hora, basado en el estándar RFC3339 sección 5.6, tipo "date-time". Formato: YYYY-MM-DDThh:mi:ss[Zl(+l-)hh:mm] Ejemplo: 20 6-09-26T 3:00:00+06:00 ?Validación: Se verificará el cumplimiento del formato indicado caso contrario se rechazará el comprobante. No podrán señalarse fechas posteriores ni anteriores a la fecha de generación del comprobante. Fechas anteriores a la validación del comprobante solo se permiten en los comprobantes con situación sin internet según nota Nº 3. , este campo debe de coincidir con la fecha señalada en la clave numérica. | | | | | | |
Emisor | Emisor del comprobante | ComplexType | | ?Tipo complejo que contiene los datos del emisor del comprobante | | | | | | |
>2 Nombre | Nombre o razón social del Emisor | String | 00 | ?Validación: Deberá contener m nimo caracteres y un máximo de 00. | | | | | | |
> Identificación | Identificacion | ComplexType | | ?Tipo complejo que contiene los datos de identificación del emisor | | | | | | |
> >3 Tipo | Tipo de identificación del emisor | String | 2 | ?Ver nota 4. Es un campo fijo de dos posiciones. ?Este campo será de condición obligatoria, cuando se posea información en el nodo "Número de cédula física/ jur dica/NITE/DIMEX del emisor/ Extranjero no domiciliado/ No contribuyente. ?Validación: Se verificará el cumplimiento de la codificación indicada en la nota Nº4, caso contario se rechazará el comprobante. ?El tipo de identificación código 05 de la nota 4 de "E tran ero No Domiciliado" es de uso exclusivo para el tipo de comprobante electrónico "Factura electrónica de compra" por lo que no debe habilitarse en ningún otro tipo de comprobante electrónico. Además, se verificará que este código se complemente con el código de Documento de Referencia 16 "Comprobante de Proveedor No Domiciliado" en el apartado de "Información de Referencia". ?El código del tipo de No Contribuyente: Se permitirá en la FEC, únicamente cuando en el campo "Condición de la Venta" se haya | | | | | | |
[imagen]
[imagen]
2 Cada carácter > se debe interpretar como un nivel de anidamiento. Por ejemplo: nombre es un elemento dentro de Emisor.
3 En este caso, Tipo es un elemento dentro de identificación, el cual a su vez es un nodo de Emisor. Para mayor claridad referirse al schema.
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
| | | | seleccionado el código 13 "Ventas Bienes Usados No Contribuyentes: Caso contrario se rechazará el comprobante. Para el uso de estos códigos, el emisor debe estar inscrito ante la Administración Tributaria en todos los casos, excepto en los códigos de identificación del "Extranjero No Domiciliado" y "No Contribuyente" en la FEC. | | | | | | |
> > Numero | Número de cédula física/jurídica/NITE/DI MEX/EXTRANJERO NO DOMICILIADO/ NO CONTRIBUYENTE DEL EMISOR | String | 20 | ?Este campo será de condición obligatoria, cuando se posea información en el nodo "Tipo de identificación del emisor. ? Formato: La "Cédula física" debe de contener 9 dígitos, sin cero al inicio y sin guiones. La "Cédula de personas Jurídicas" debe contener 10 dígitos y sin guiones. El "Documento de Identificación Migratorio para Extranjeros (DIMEX)" debe contener 11 o 12 dígitos, sin ceros al inicio y sin guiones. El "Documento de Identificación de la DGT (NITE)" debe contener 10 dígitos y sin guiones. El número de identificación del "Extranjero no domiciliado", puede contener hasta un máximo de 20 caracteres (números y letras) en el campo denominado número, de lo contrario se mantienen las longitudes ya establecidas para los números de cédulas. El número de identificación del "No Contribuyente", puede contener hasta un máximo de 20 caracteres (números y letras) en el campo denominado número, de lo contrario se mantienen las longitudes ya establecidas para los números de cédulas. ?Validación: Se verificará que el comprobante cumpla con el formato establecido según el tipo de identificación, caso contrario se rechazará el comprobante ?El contribuyente debe estar inscrito ante la Administración Tributaria en todos los casos, excepto el número de identificación del "Extranjero No Domiciliado" y "No Contribuyente" en la FEC. | 1 | 1 | 1 | 1 | 1 | 1 | 1
> Registrofiscal8707 | Número de Registro Fiscal de bebidas alcohólicas Ley 8707 | String | 12 | ?Campo condicional. Se convierte en carácter obligatorio cuando se estén facturando códigos CAByS de bebidas alcohólicas según la Ley 8707. Contiene los datos del número de registro de bebidas alcohólicas, suministrado por la Dirección General de Aduanas. ?Se permite como máximo 12 dígitos. ?Validación: Se verificará el uso de este campo cuando se utilicen códigos CAByS de Bebidas alcohólicas, de no cumplir con el mismo se generará mensaje de advertencia. | 2 | 2 | 2 | 2 | 2 | 2 | 4
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
> NombreComercial | Nombre comercial emisor | String | 80 | ?En el caso que se cuente con nombre comercial debe indicarse. Es opcional ?Validación: Deberá contener mínimo 3 caracteres y un máximo de 80. | 3 | 3 | 3 | 3 | 3 | 3 | 4
> Ubicacion | Ubicación | ComplexType | | ?Tipo complejo que contiene el detalle de una ubicación, Campo obligatorio en todos los comprobantes, excepto en la Factura Electrónica de Compra cuando se utilice el "códigos 05" de la nota 4 en el Tipo de Identificación del Emisor. En el caso del código 06, de la nota 4, para "No Contribuyentes", de contar con Domicilio en el país, debe indicarlo. | | | 2 | | | | 4
> > Provincia | Provincia | String | | ?Ver nota 4 y 7. Únicamente permite números. ?Validación: Se verificará el cumplimiento de la nota 4 y 7. ?Adicionalmente se verificará la inclusión de códigos diferentes al inscrito en el Registro Único Tributario (RUT), en cuyo caso se generará un mensaje de advertencia. Se exceptúan de esta obligación, los códigos de identificación 05 y 06. | | | | | | | 4
> > Canton | Cantón | String | 2 | ?Ver nota 4 y 7. Únicamente permite números. ?Validación: se verificará el cumplimiento de la nota 4 y 7. ? Adicionalmente se verificará la inclusión de códigos diferentes al inscrito en el Registro Único Tributario (RUT), en cuyo caso se generará un mensaje de advertencia. Se exceptúan de esta obligación, los códigos de identificación 05 y 06. | | | | | | | 4
> > Distrito | Distrito | String | 2 | ?Ver nota 4 y 7. Únicamente permite números. ?Validación: se verificará el cumplimiento de la nota 4. ? Adicionalmente se verificará la inclusión de códigos diferentes al inscrito en el Registro Único Tributario (RUT), en cuyo caso se generará un mensaje de advertencia. Se exceptúan de esta obligación, los códigos de identificación 05 y 06. | | | | | | | 4
> > Barrio | Barrio | String | 50 | ?Debe de detallarse en texto, el nombre del barrio del emisor. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 50 | 3 | 3 | 3 | 3 | 2 | 2 | 4
> > OtrasSenas | Otras señas | String | 250 | ?Debe de indicarse lo más exacta posible. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 250 | | | | | | | 4
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
> Otras Senas Extranjero | Otras señas Extranjero | String | 300 | ?Debe de indicarse lo más exacta posible. Es de uso exclusivo para cuanto se selecciona el código "05" en el campo denominado "Tipo de identificación del emisor.", por lo cual no puede ser utilizado ningún otro tipo de identificación. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 300 cuando se utilice código "05" en el campo denominado "Tipo de identificación del emisor." para FEC. | 4 | 4 | 2 | 4 | 4 | 4 | 4
> Telefono | Telefono | ComplexType | | ?Tipo complejo para un número telefónico. Es opcional. | 3 | 3 | 3 | 3 | 3 | 3 | 4
> > CodigoPais | Código del País | lnteger | 3 | ?En el caso que se cuente con un número de teléfono debe indicarse. ?Validación: Deberá contener mínimo dígito y un máximo de 3. | | | | | | | 4
> > NumTelefono | Número telefónico | lnteger | 20 | ?En el caso que se cuente con un número de teléfono debe indicarse. ?Validación: Deberá contener mínimo 8 dígitos y un máximo de 20. | | | | | | | 4
> CorreoElectronico ,4 | Dirección del correo electrónico del emisor | String | 0 | ?Se puede incluir un máximo de 4 direcciones de correo. ?Debe cumplir con la siguiente estructura: \\\s (([\<>( \\[\\]\\., :\\s \\\ ] (\\.[\<>( \\[\\]\\., :\\s \\\ ] (\\\ . \\\ (([\<>( \\[\\]\\., :\\s \\\ ] \\. [\<>( \\[\\]\\., :\\s \\\ ] 0, \\s $ ?Validación: Deberá Cumplir con el formato indicado, caso contrario se rechazará el comprobante. | | | 2 | | | |
Receptor | Receptor del comprobante | ComplexType | | ?Tipo complejo que contiene los datos del receptor del comprobante | | 2 | | 2 | 2 | 2 |
> Nombre | Nombre o razón social del Receptor | String | 00 | ?Validación: Deberá contener mínimo 3 caracteres y un máximo de 00. | | | | | | |
> ldentificacion | ldentificación | ComplexType | | ?Tipo complejo que contiene los datos de identificación del receptor | | | | 2 | 2 | 2 |
> > Tipo | Tipo de identificación del receptor | String | 2 | ?Ver nota 4. Es un campo fijo de dos posiciones. ?Este campo será de condición obligatoria, cuando se posea información en el nodo "Número de cédula física/ jurídica/NlTE/DlMEX, Extranjero no domiciliado, del receptor. ?Validación: El uso del código para el Extranjero no domiciliado: se permitirá, en la FEE, TE, NC y ND. En FE, se permitirá únicamente cuando la condición de la venta sea código 2 "Venta de Mercancía No Nacionalizada" de la nota 5. En estos casos se deberá indicar en el apartado, "Información de Referencia" los datos del documento de respaldo de no indicarse se rechazará el comprobante electrónico. En la FEC y el REP se rechazará el uso de este código. | | | | | | |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
> > Numero | Número de cédula física jurídica NITE DIMEX Extranjero No Domiciliado, del receptor | String | 20 | ?Este campo será de condición obligatoria, cuando se posea información en el nodo "Tipo de identificación del receptor. ? Formato: La "Cédula física" debe de contener 9 dígitos, sin cero al inicio y sin guiones. La "cédula de personas Jurídicas" debe contener 10 dígitos y sin guiones. El "Documento de Identificación Migratorio para Extranjeros (DIMEX)" debe contener 11 o 12 dígitos, sin ceros al inicio y sin guiones. El "Documento de Identificación de la DGT (NITE)" debe contener 0 dígitos y sin guiones. El número de identificación del "Extranjero No Domiciliado", puede contener hasta un máximo de 20 caracteres (números y letras) en el campo denominado número, de lo contrario se mantienen las longitudes ya establecidas para los números de cédulas ?Validación: Se verificará que el comprobante cumpla con el formato establecido según el tipo de identificación. En FEC, el receptor debe estar inscrito ante la Administración Tributaria En el caso de FE, FEE y TE, de los datos registrados en este campo, se verificará que el número de identificación sea un dato real en los padrones y registros correspondientes, excepto el "Extranjero No Domiciliado" el cual no requiere estar inscrito o empadronado. En el caso de FE, el número de identificación del "Extranjero No Domiciliado" únicamente se permitirá en los Datos del Receptor, cuando en el campo "Condición de la Venta" se haya indicado el código 2 "Venta Mercancía No Nacionalizada" En REP, NC y ND, los datos registrados deben coincidir con el comprobante original. De no cumplirse los puntos anteriores se rechazará el comprobante. | | | | | | |
> NombreComercial | Nombre comercial receptor | String | 80 | ?En el caso que se cuente con nombre comercial debe indicarse. Es opcional ?Validación: Deberá contener mínimo 3 caracteres y un máximo de 80. | 3 | 3 | 3 | 3 | 3 | 3 | 4
> Ubicacion | Ubicacion | ComplexType | | ?Tipo complejo que contiene el detalle de una ubicación. En caso de contar con domicilio en el país, debe indicarse. En caso de Tiquete electrónico queda como opcional. No aplica para el tipo de identificación de Extranjero No Domiciliado | 2 | 4 | 2 | 3 | 2 | 2 | 4
> > Provincia | Provincia | String | | Ver nota 4 y 7. Únicamente permite números. ? Validación: Se verificará el cumplimiento de la nota 4. | | 4 | | | | | 4
> > Canton | Cantón | String | 2 | ?Ver nota 4 y 7. Únicamente permite números. ? Validación: Se verificará el cumplimiento de la nota 4. | | 4 | | | | | 4
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
> > Distrito | Distrito | String | 2 | ?Ver nota 4 y 7. Únicamente permite números. ? Validación: Se verificará el cumplimiento de la nota 4. | | 4 | | | | | 4
> > Barrio | Barrio | String | 50 | ?Debe de detallarse el nombre del barrio del receptor. ?Deberá contener mínimo 5 caracteres y un máximo de 50. | 3 | 4 | 3 | 2 | 2 | 2 | 4
> > OtrasSenas | Otras señas | String | 60 | ?Debe de indicarse lo más exacta posible. ? Validación: Deberá contener mínimo 5 caracteres y un máximo de 60. | | 4 | | | | | 4
> OtrasSenasExtranjero | Otras señas Extranjero | String | 300 | ?Campo para incluir la dirección en el extranjero, en caso de requerirlo. En FE se permitirá estecampo para el tipo de identificación de Extranjero No Domiciliado cuando se utilice el código "05" de la nota 4. en el campo denominado "Tipo de identificación del receptor." ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 300. Cuando se utilice código "05" en el campo denominado "Tipo de identificación del receptor." Este campo se rechazará en FEC. | 2 | 2 | 4 | 3 | 2 | 2 | 4
> Telefono | Telefono | ComplexType | | ?Tipo complejo para un número telefónico. Es opcional. | 3 | 3 | 3 | 3 | 3 | 3 | 4
> > CodigoPais | Código del País | lnteger | 3 | ?En el caso que se cuente con un número de teléfono debe indicarse. ? Validación: Deberá contener mínimo digito y un máximo de 3. | | | | | | | 4
> > NumTelefono | Número telefónico | lnteger | 20 | ?En el caso que se cuente con un número de teléfono debe indicarse. ? Validación: Deberá contener mínimo 8 dígitos y un máximo de 20 | | | | | | | 4
> CorreoElectronico | Dirección del correo electrónico del receptor | String | 60 | ?Este campo será de condición obligatoria, cuando el cliente lo requiera. ?Debe cumplir con la siguiente estructura: A\\s*(([A<>()\\[\\]\\.,;:\\s@\\\"]+(\\.[A<>()\\[\\]\\.,;:\\s@\\\"]+)*)I(\\\".+\\\"))@ (([A<>()\\[\\]\\.,;:\\s@\\\"]+\\.)+[A<>()\\[\\]\\.,;:\\s@\\\"]{0,})\\s*$ ?Validación: Deberá de cumplir con el formato indicado, caso contrario se rechazará el comprobante. | 2 | 2 | 2 | 2 | 2 | 2 | 2
CondicionVenta | Condiciones de la venta | String | 2 | ?Ver notas 5 y 7. Es un campo fijo de dos posiciones ?Validación: Cumplimiento de la Nota 5. ?El código 2 de la nota 5, sobre "Venta de Mercancía No Nacionalizada", únicamente será permitido en el comprobante Factura Electrónica, caso contrario se rechazará el comprobante electrónico. Los códigos, 09 y , de la nota 5, sobre pagos de servicios prestado al Estado y Ventas a Crédito en lVA a 90 días, se utilizarán únicamente en Recibos Electrónicos de Pago. Estos serán los únicos códigos permitidos en dicho Comprobante Electrónico. | | | | | | |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
CondicionVentaOtros | Detalle Condicion de la Venta OTRO | atring | 100 | ?Será obligatorio en caso de utilizar el código 99 de "Otros" de la nota 5. ae debe describir puntualmente la condición de la venta utilizada. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 100. | 2 | 2 | 2 | 2 | 2 | 2 |
PlazoCredito | Plazo del crédito | Integer | 5 | ?Este campo será de condición obligatoria, cuando la condición de la venta del producto o prestación de servicio sea código 02 correspondiente a Crédito, o código 10 correspondiente a "Venta a crédito en IVA hasta 90 días" el mismo se debe de expresar en días. ?Validación: Deberá contener mínimo 1 número entero y un máximo de 5. ? Se deberá incluir un valor mayor a "cero". Caso contrario se rechazará el comprobante. | 2 | 2 | 2 | 2 | 2 | 2 |
b) Detalle de la mercancía o servicio prestado
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
DetalleServicio | Detalle del Servicio, Mercancía u otro. | Complex Type | | ?Tipo complejo que agrupa las líneas del detalle. ?Validación: Deberá de ser de carácter obligatorio en todos los comprobantes, excepto en FE, TE, NC Y ND cuando se utilice el nodo de "Otros Cargos" y se seleccione el código 04, 08, 09 y 10 de la nota 16 en el campo "Tipo de documento otros cargos" y no cuente con una línea de servicio o producto | 2 | | | 2 | 2 | 2 |
> LineaDetalle { , 000} | Línea de detalle | Complex Type | | ?Tipo complejo que representa cada línea del detalle de la mercancía o servicio prestado. ?En el caso del Recibo Electrónico de Pago representa el pago de un comprobante a crédito para las condiciones ya establecidas para los códigos 08 y 0 de la nota 5. | | | | | | |
> > NumeroLinea | NVúmero de la línea | Positivel nteger | | ?De a 000 | | | | | | |
> > PartidaArancelaria | Partida Arancelaria | String | 2 | ?Se convierte en carácter obligatorio cuando se elija el tipo de comprobante "Factura Electrónica de Exportación" para la venta de una mercancía y se seleccione un código CAByS que corresponda a un producto. ? Validación: Deberá incluir al menos 2 dígitos cuando se trate de una FEE, NC o ND que modifiquen una FEE y que el primer digito del código CABYS sea 0, , 2, 3 y 4 (bienes). | 4 | 2 | 4 | 4 | 2 | 2 | 4
4 > > CodigoCABYS | Código de Producto /Servicio | String | 3 | ?Ver nota 7. ?Para las Notas de Crédito y Débito será obligatorio el código CAByS, cuando la misma se encuentre ligada a un Comprobante electrónico que contenga código CAByS. ?No será obligatorio en las Notas de Crédito o Débito cuando en el apartado de "Información de Referencia", el documento de referencia sea un comprobante emitido antes del 0 de diciembre del 2020 o se identifique como una Nota de Crédito Financiera o Nota de Debito Financiera, definidas en la nota 9 "Códigos de Referencia a Utilizar" ?Validación: Se Verificará que el código sea válido en el catálogo vigente publicado en el sitio web del BCCR, salvo en las NC y ND que tengan código de notas de crédito financieras (código 08 y 09 de la nota 9), en el apartado de información de referencia. Adicionalmente, en el caso de aplicarse exoneraciones (códigos 04), el código indicado por el emisor, deberá de encontrarse en la autorización emitida por la Dirección General de Hacienda. Caso contrario se rechazará el comprobante. | | | | | 2 | 2 | 4
[imagen]
4 Rige a partir del 01/12/2020; a partir de la fecha indicada anteriormente dicho campo es "Obligatorio".
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
> > CodigoComercial {0,5} | Código Comercial | Complex Type | | ?Tipo complejo para el código de un producto o servicio. ?Se puede incluir un máximo de 5 repeticiones de códigos de producto/servicio. ?Este será un requisito obligatorio para las líneas de detalle que utilicen uno de los códigos de producto/servicio de "surtidos" que estén habilitados en el CAByS, entendidos como la combinación de más de dos productos con diferentes códigos de producto/servicio. ?Validación: Deberá incluir al menos 3 caracteres cuando se utilice uno de los códigos CAByS habilitados para surtidos. Caso contrario se rechazará el comprobante. | 2 | 2 | 2 | 2 | 2 | 2 | 4
> > > Tipo | Tipo de Código de producto/servicio | String | 2 | ?Ver nota 2. Es un campo fijo de dos posiciones ?Será obligatorio para las líneas de detalle que utilicen uno de los códigos de producto/servicio de "surtidos" que estén habilitados en el CAByS. ?En el caso de la inclusión de paquetes, surtidos o combos, entendidos como la combinación de más de dos productos con diferentes códigos de producto/servicio, se debe seleccionar el código 03 "Código del producto asignado por el fabricante - industriales o importadores" de la nota 12 e incluir en el campo "código" el respectivo código "SKU", GTIN o equivalentes, con el que el paquete este identificado por el fabricante - industria o importador. Estos códigos deben ser verificables en los catálogos disponibles por el fabricante - industria o importador. | | | | | | | 4
> > > Codigo | Código | String | 20 | ?Será obligatorio para las líneas de detalle que utilicen uno de los códigos de producto/servicio de "surtidos" que estén habilitados en el CAByS. ?Cuando se seleccione en el campo "Tipo de Código de producto/servicio" el código 03 "Código del producto asignado por el fabricante - industriales o importadores" de la nota 12, se deberá incluir en el campo "código" el respectivo código "SKU", GTIN o equivalentes, con el que el paquete es identificado por el fabricante - industria o importador. Estos códigos deben ser verificables en los catálogos disponibles por fabricante - industria o importador | | | | | | | 4
> > Cantidad | Cantidad | Decimal | 6,3 | ?Es un número decimal compuesto por 3 enteros y 3 decimales. ?Validación: Se deberá incluir un valor mayor a "cero". Caso contrario se rechazará el comprobante. | | | | | | | 4
> > UnidadMedida | Unidad de Medida | String | 5 | ?Ver nota 5. ?Validación: Se verificará el cumplimiento de la nota 5. | | | | | | | 4
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
5> > TipoTransaccion | Tipo de Transacciones | String | 2 | ?Ver nota 22 ?Este campo se utilizará para identificar el tipo de transacción que se realizará. ?Validación: Se verificará cuando corresponda el cumplimiento de la nota 22. | 2 | 2 | 2 | 4 | 2 | 2 | 4
> > UnidadMedidaComercial | Unidad de Medida Comercial | String | 20 | ?Nodo utilizado para indicar una unidad de medida que nace del propio giro comercial del establecimiento, no es una cantidad estandarizada de una determinada magnitud física, definida y adoptada por convención o por ley ejemplo "1 Tarima" | 3 | 3 | 3 | 3 | 3 | 3 | 4
> > Detalle | Detalle de la mercancía transferida o servicio prestado | String | 200 | ?Es de carácter obligatorio. ?Debe de detallarse el tipo de producto o servicio que se brinde. En el caso del Recibo Electrónico de Pago se detalla el pago al comprobante original, indicando al menos el número de cuata seguido del producto. ?Validación: Deberá contener mínimo 3 caracteres y un máximo de 200. | | | | | | |
6 > > NumeroVINoSerie { , 000} | Número de VIN o Serie del medio de transporte. | String | 7 | ?Se convierte en carácter obligatorio, cuando el código CAByS del producto que se esté comercializando pertenece a un medio de transporte con esta numeración. ?Se pueden utilizar la cantidad de repeticiones que se requieran ?Validación: Se verificará el código CAByS que corresponda a medios de trasporte. Caso contrario se realizará la advertencia correspondiente. | 2 | 2 | 2 | 2 | 2 | 2 | 4
7 > > RegistroMedicamento | Registro de medicamento | String | 00 | ?Se convierte en carácter obligatorio, cuando el código CAByS del producto que se esté comercializando pertenece a un medicamento que posea registro sanitario. ?Validación: Se verificará el código CAByS que corresponda a medicamentos. Caso contrario se realizará la advertencia correspondiente. | 2 | 2 | 2 | 2 | 2 | 2 | 4
5 Cuando se facturen bienes o servicios con tratamientos tributarios específicos según la necesidad de las partes se deberán usar los códigos relacionados a estos según corresponda. Es obligatorio su uso para la aplicación de condiciones especiales según el tipo de transacción en las declaraciones.
6 Deberá de ser utilizado cuando se comercialicen Vehículos, Aeronaves o Embarcaciones indicando su número VIN, Numero de Serie o bien el consecutivo de fabricación.
7 Deberá de ser utilizado cuando se comercialicen medicamentos con registro sanitario.
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
> > FormaFarmaceutica | Forma farmacéutica | String | 3 | ? Se convierte en carácter obligatorio cuando se utilice un código CAByS que corresponda a medicamento que posea registro sanitario. Ver nota 9 ?Este campo se utilizará para incluir el código de la forma farmacéutica ?Validación: Se verificará cuando corresponda el cumplimiento de la nota 9. | 2 | 2 | 2 | 2 | 2 | 2 | 4
8> > DetalleSurtido | Detalle de productos del surtido | Complex Type | | ?Es obligatorio en los casos señalados en la nota al pie número 8, para las líneas de detalle que utilicen uno de los códigos de producto de "surtidos" que estén habilitados en el CAByS. ?Tipo complejo que representa cada línea del detalle de los componentes de un surtido, paquete o combinación de productos. Se debe utilizar cuando en la línea de detalle se está facturando un paquete, surtido o combo, entendido como la combinación de más de dos productos con diferentes códigos de producto. ?No es obligatoria su visualización para la representación gráfica. ?Validación: En caso de utilizarse un código CAByS de surtidos, en donde se combinen bienes con diferentes tarifas del IVA este convierte de carácter obligatorio. | 2 | 2 | 4 | 2 | 2 | 2 | 4
> > > LineaDetalleSurtido { ,20} | Línea de detalle de surtido | Complex Type | | ?Tipo complejo que representa cada línea del detalle del surtido. | | | 4 | | | | 4
> > > > CodigoCABYSSurtido | Código de Producto /Servicio componente de Surtido | String | 3 | ?Ver nota 7. ?Validación: Se Verificará que el código sea válido en el catálogo vigente publicado en el sitio web del BCCR, salvo en las NC y ND que tengan código de notas de crédito financieras (código 08 y 09 de la nota 9), en el apartado de información de referencia. | | | 4 | | | | 4
> > > > CodigoComercialSurtido {0,5} | Código Comercial Surtido | Complex Type | | ?Tipo complejo para el código de un producto o servicio. ?Se puede incluir un máximo de 5 repeticiones de códigos de producto/servicio. Es opcional | 3 | 3 | 4 | 3 | 2 | 2 | 4
8 Este nodo es de uso obligatorio cuando se facturan surtidos, combos o paquetes que contienen bienes sujetos a distintas tarifas del IVA. La conformación de surtidos, combos o paquetes que se facturan como tales y se detallan en este nodo se permite únicamente a fabricantes - industriales o importadores, en los demás casos, los elementos que conforman o están contenidos en los surtidos, combos o paquetes, deben especificarse en las líneas de detalle del comprobante. Estos surtidos, combos o paquetes deben tener asignado un código comercial específico (SKU, GTIN o equivalente) a efecto de permitir su identificación y trazabilidad. La facturación de surtidos, combos o paquetes que no cumplen con estas condiciones, los elementos que lo conforman se deben especificar en las líneas de detalle del comprobante, de manera que no procede la utilización del nodo.
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo |
FE | FEE | FEC | TE | NC | ND | REP |
> > > > > TipoSurtido | Tipo de Código de producto / Servicio componente de surtido | String | 2 | ?Ver nota 2. ?Es un campo fijo de dos posiciones ?Validación: Se verificará el cumplimiento de la nota 2. | | | 4 | | | | 4 |
> > > > > CodigoSurtido | Código componente de surtido | String | 20 | ?Campo que se utiliza internamente por el emisor según la necesidad de su negocio. | | | 4 | | | | 4 |
> > > > CantidadSurtido | Cantidad componente de surtido | Decimal | ,3 | ? Es un número decimal compuesto por 3 enteros y 3 decimales. ?Validación: Se deberá incluir un valor mayor a "cero". Caso contrario se rechazará el comprobante. | | | 4 | | | | 4 |
> > > > UnidadMedidaSurtido | Unidad de Medida componente de surtido | String | 5 | ?Ver nota 5. ?Validación: Se verificará el cumplimiento de la nota 5. | | | 4 | | | | 4 |
> > > > UnidadMedidaComercialSurtido | Unidad de Medida Comercial componente de surtido | String | 20 | ?Nodo utilizado para indicar una unidad de medida que nace del propio giro comercial del establecimiento, no es una cantidad estandarizada de una determinada magnitud física, definida y adoptada por convención o por ley ejemplo: "1 Tarima" | 3 | 3 | 4 | 3 | 2 | 2 | 4 |
> > > > DetalleSurtido | Detalle de la mercancía transferida o servicio prestado incluido en el surtido | String | 200 | ?Es de carácter obligatorio. ?Debe de detallarse el tipo de producto o servicio que se brinde. ?Validación: Deberá contener mínimo 3 caracteres y un máximo de 200. | | | 4 | | | | 4 |
> > > > PrecioUnitarioSurtido | Precio unitario componente de surtido | Decimal | 8,5 | ?Es un número decimal compuesto por 3 enteros y 5 decimales. ?Validación: Se deberá incluir un valor mayor a "cero". | | | 4 | | | | 4 |
> > > > MontoTotalSurtido | Monto total componente surtido | Decimal | 8,5 | ?Se obtiene de la multiplicación del campo "Cantidad componente de surtido" por el campo "Precio unitario componente de surtido". ?Es un número decimal compuesto por 3 enteros y 5 decimales. | | | 4 | | | | 4 |
> > > > DescuentoSurtido {0,5} | Descuento Surtido | Complex Type | | ?Tipo complejo descuento. ?Se puede incluir un máximo de 5 repeticiones de descuentos, cada descuento adicional se calcula sobre la base menos el descuento anterior. | 3 | 3 | 4 | 3 | 2 | 2 | 4 |
> > > > > MontoDescuentoSurtido | Monto de descuentos concedidos al componente de surtido | Decimal | 8,5 | ?Este campo será de condición obligatoria, cuando se indique un descuento, regalía o bonificación en el campo "Código del descuento de componente del surtido" ?Es un número decimal compuesto por 3 enteros y 5 decimales. ?Validación: Se deberá incluir un valor igual o menor al del "Monto total componente surtido". | | | 4 | | | | 4 |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo |
FE | FEE | FEC | TE | NC | ND | REP |
> > > > > CodigoDescuentoSurtido | Código del descuento del componente de surtido | String | 2 | ?Ver Nota 20. Este campo será de condición obligatoria, cuando se incluya información en el campo "Monto de descuentos concedidos al componente de surtido" ?Validación: Se verificará el cumplimiento de la nota 9. | | | 4 | | | | 4 |
> > > > > DescuentoSurtidoOtros | Naturaleza del descuento de componente del surtido | String | 80 | ?Este campo será de condición obligatoria, cuando se utilice el código 99 de la Nota 20 ?Validación: En caso de utilizarse el código 99, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. Además, deberá contener mínimo 3 caracteres y un máximo de 80. | 2 | 2 | 4 | 2 | 2 | 2 | 4 |
> > > > SubTotalSurtido | Subtotal componente del surtido | Decimal | 8,5 | ?Se obtiene de la resta del campo "Monto total componente surtido" menos "Monto de descuentos concedidos al componente de surtido". ?Es un número decimal compuesto por 3 enteros y 5 decimales. | | | 4 | | | | 4 |
> > > > IVACobradoFabricaSurtido | IVA cobrado a nivel de fábrica componente surtido | String | 2 | ?Ver nota 2 ?En este campo se indicará si el Impuesto al Valor Agregado fue cobrado a nivel de fábrica, por lo que deberá ser utilizado únicamente por los obligados tributarios a realizar el pago de esta forma. ?Se convierte en obligatorio cuando el IVA se cobra o se cobró a nivel de fábrica. ?Al hacer uso del presente campo el producto se entenderá exento para el código 02, por lo cual no deberá llenar el subnodo de impuestos para el cálculo del IVA. ?Para el código 0 el emisor puede separar los impuestos que está cobrando en la fábrica. | 2 | 4 | 4 | 2 | 2 | 2 | 4 |
> > > > BaseImponibleSurtido | Base imponible para componente de surtido | Decimal | 8,5 | ?Este campo será de condición obligatoria, cuando el producto este gravado con algún impuesto. Se obtiene de la suma entre el campo "Subtotal componente del surtido", más el impuesto selectivo de consumo (02), el Impuesto específico de Bebidas Alcohólicas (04) y el Impuesto Específico sobre las bebidas envasadas sin contenido alcohólico y jabones de tocador (05), cuando corresponda. ?Este campo se podrá editar cuando se seleccione en el campo "IVA cobrado a nivel de fábrica" el Código 01 o en el campo de "Código del impuesto" el código 07. ?Validación: En caso de utilizarse el código 0 , en el campo de IVA cobrado a nivel de fábrica, se verificará que este | | 4 | 4 | | | | 4 |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo |
FE | FEE | FEC | TE | NC | ND | REP |
| | | | campo se encuentre en el comprobante, caso contrario se rechazará. Además, se deberá incluir un valor mayor a "cero". | | | | | | | |
> > > > ImpuestoSurtido {1,1000} | Impuesto Surtido | Complex Type | | ?Tipo complejo con el detalle del impuesto. ?Este campo será de condición obligatoria en todos los comprobantes. ?Se pueden utilizar para una misma línea la cantidad de códigos de impuestos que se requieran para cada producto. | 1 | 1 | 1 | 1 | 1 | 1 | 4 |
> > > > > CodigoImpuestoSurtido | Código del impuesto para componente de surtido | String | 2 | ?Ver nota 8. Es un campo fijo de dos posiciones. ?Al utilizar el código de Naturaleza del Descuento 01 correspondiente a "Regalías" o 03 de "Bonificaciones" y el código de impuesto 01, se debe utilizar para el cálculo del impuesto el campo denominado "Monto total componente de surtido" y la "Tarifa del Impuesto al Valor Agregado para componente de surtido" ?Validación: Se verificará el cumplimiento de la nota 8. | 1 | 1 | 1 | 1 | 1 | 1 | 4 |
> > > > > CodigoImpuestoOTROSurtido | Código del impuesto OTRO para componente de surtido | String | 100 | Será obligatorio en caso de utilizar el código 99 de "Otros" de la nota 8. Se debe describir puntualmente el impuesto utilizado. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 100. | 2 | 2 | 2 | 2 | 2 | 2 | 4 |
> > > > > CodigoTarifaIVASurtido | Código de la tarifa del Impuesto al Valor Agregado para componente de surtido | String | 2 | ?Ver nota 8.1. Es un campo fijo de dos posiciones. ?Se convierte en obligatorio cuando se usa el código 01 de impuestos de surtido ?Validación: Se verificará el cumplimiento de nota 8.1. cuando se utilice el código 01 de campo código del impuesto. | 2 | 2 | 4 | 2 | 2 | 2 | 4 |
> > > > > TarifaSurtido | Tarifa del Impuesto para componente de surtido | Decimal | 4,2 | ?Este campo es de condición obligatoria, cuando el componente este gravado con alguna tarifa de impuesto, según corresponda. Debe de expresarse el porcentaje como número entero (Ejemplo: la tarifa del 13% se debe de reflejar como 13, la tarifa del 1% como 1, o bien la tarifa del 0.5% como 0.5). ?Para Cálculo del IVA, Ver nota 8.1 ?Para Cálculo del Impuesto Selectivo de Consumo código 02 de la nota 8, la tarifa será editable, según la normativa correspondiente. ?Para Cálculo de "otros impuestos" código 99, la tarifa será editable, según la normativa correspondiente. ?Validación: Cuando se utilice el Código de impuesto 01 la tarifa del impuesto debe de coincidir con el correspondiente | 2 | 2 | 4 | 2 | 2 | 2 | 4 |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo |
FE | FEE | FEC | TE | NC | ND | REP |
| | | | código de impuesto IVA. Si se utiliza código de impuesto 02 o 99 debe de incluirse el porcentaje como un número entero. | | | | | | | |
> > > > > DatosImpuestoEspecíficoSurtido | Datos para Impuestos Específicos para componente de surtido | Complex Type | | ?Tipo complejo con el detalle para calcular impuestos específicos no tarifarios. ?Este campo es de condición obligatoria, cuando se utilicen los códigos de impuesto 04, 05, 06 de la nota 8 y agrupará los campos requeridos para el cálculo de estos impuestos ?Validación: En caso de utilizarse el código 04,05,06 de la nota 8, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. | 2 | 4 | 4 | 2 | 2 | 2 | 4 |
> > > > > > CantidadUnidadMedidaSurtido | Cantidad de la unidad de medida a utilizar para componente de surtido | Decimal | 7,2 | ?Este campo es de condición obligatoria, cuando se utilicen los códigos de impuesto 04, 05 y 06 de la nota 8. ?Validación: En caso de utilizarse el código 04,05,06 de la nota 8, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. | | 4 | 4 | | | | 4 |
> > > > > > PorcentajeSurtido | Porcentaje en componente de surtido | Decimal | 4,2 | ?Este campo es de condición obligatoria, cuando se utilice el código de impuesto 04 de la nota 8. Debe de expresarse el porcentaje como número entero (Ejemplo: la tarifa del 3% se debe de reflejar como 3, la tarifa del % como , o bien la tarifa del 0.5% como 0.5). ?Validación: En caso de utilizarse el código 04 de la nota 8, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. | 2 | 4 | 4 | 2 | 2 | 2 | 4 |
> > > > > > ProporcionSurtido | Proporción en componente de surtido | Decimal | 5,2 | ?Este campo es de condición obligatoria, cuando se utilice el código de impuesto 04 de la nota 8 ?Este campo se obtiene de multiplicar la "Cantidad de la unidad de medida a utilizar" por el "Porcentaje" ?Validación: En caso de utilizarse el código 04 de la nota 8, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. | 2 | 4 | 4 | 2 | 2 | 2 | 4 |
> > > > > > VolumenUnidadConsumoSurtido | Volumen por Unidad de Consumo componente de surtido | Decimal | 7,2 | ?Este campo es de condición obligatoria, cuando se utilice el código de impuesto 05 de la nota 8. ?Validación: En caso de utilizarse el código 05 de la nota 8, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. | 2 | 4 | 4 | 2 | 2 | 2 | 4 |
> > > > > > ImpuestoUnidadSurtido | Impuesto por Unidad componente de surtido | Decimal | 8,5 | ?Este campo es de condición obligatoria, cuando se utilicen los códigos de impuesto 04, 05 y 06 de la nota 8. ?Validación: En caso de utilizarse el código 04,05,06 de la nota 8, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. | | 4 | 4 | | | | 4 |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo |
FE | FEE | FEC | TE | NC | ND | REP |
> > > > MontolmpuestoSurtido | Monto del impuesto para componente de surtido | Decimal | 8,5 | ?Este campo será de condición obligatoria, cuando el componente este gravado con algún impuesto. Es un número decimal compuesto por 3 enteros y 5 decimales. ?Cálculo del IVA: Se obtiene de la multiplicación del campo "Tarifa del Impuesto al Valor Agregado para componente de surtido" por el campo por "Base Imponible del surtido". ?Casos especiales para el cálculo del IVA: Al utilizar el código de Naturaleza del Descuento 0 correspondiente a "Regalías" o 02 de "Bonificaciones" y el código de impuesto 0 , se debe utilizar para el cálculo del impuesto el campo denominado "Monto total componente surtido" y la "Tarifa del Impuesto al Valor Agregado para componente de surtido". En caso de utilizar el campo "Base Imponible Especial para componente de Surtido", este campo se obtiene de la multiplicación "Base Imponible Especial para componente de Surtido" por la "Tarifa del Impuesto al Valor Agregado para componente de surtido". ?Cálculo Impuesto Selectivo de Consumo: Se obtiene de la multiplicación del campo "Tarifa del Impuesto para componente de surtido" por el campo "Subtotal componente del surtido". ?Calculo Impuesto específico a las Bebidas Alcohólicas Se obtiene de la multiplicación del campo "Cantidad componente de surtido" por el campo "Proporción en componente de surtido" por "Impuesto por Unidad componente de surtido". ?Impuesto Específico sobre las bebidas envasadas sin contenido alcohólico y jabones de tocador Para el caso de las bebidas, se obtiene de la multiplicación del campo "Cantidad componente de surtido" por el campo "Cantidad de la unidad de medida a utilizar para componente de surtido" multiplicado por el resultado de dividir el campo "Impuesto por Unidad componente de surtido" entre el campo "Volumen por Unidad de Consumo componente de surtido". Para el caso del jabón de tocador, se obtiene de la multiplicación del campo "Cantidad componente de surtido" | | | 4 | | | | 4 |
| Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
| FE | FEE | FEC | TE | NC | ND | REP
| | | | | por el campo "Volumen por Unidad de Consumo componente de surtido" por "Impuesto por Unidad componente de surtido". ?Impuesto a los productos de Tabaco Se obtiene de la multiplicación del campo "Cantidad componente de surtido" por el campo "Cantidad de la unidad de medida a utilizar para componente de surtido" por "Impuesto por Unidad componente de surtido". | | | | | | |
| > > PrecioUnitario | Precio unitario | Decimal | 8,5 | ?Es un número decimal compuesto por 3 enteros y 5 decimales. ?Validación: Se deberá incluir un valor mayor a "cero". Caso contrario se rechazará el comprobante. | | | | | | | 4
| > > MontoTotal | Monto total | Decimal | 8,5 | ?Se obtiene de la multiplicación del campo "cantidad" por el campo "precio unitario". ?En el caso de Recibo electrónico de Pago se debe incluir el monto a pagar sobre el bien o servicio originalmente facturado sin incluir impuestos. ?Es un número decimal compuesto por 3 enteros y 5 decimales. | | | | | | |
| > > Descuento {0,5} | Descuento | Complex Type | | ?Tipo complejo descuento. Se puede incluir un máximo de 5 repeticiones de descuentos, cada descuento adicional se calcula sobre la base menos el descuento anterior. ?Validación: En caso de notas de crédito y notas de débito cuando en el apartado de información de referencia, tengan código 08 o 09 de la nota 09 correspondientes a las denominadas "Financieras" no se requerirá este nodo. | 3 | 3 | 3 | 3 | 2 | 2 | 4
| > > > MontoDescuento | Monto de descuentos concedidos | Decimal | 8,5 | ?Este campo será de condición obligatoria, cuando se indique un descuento, en el campo "Código del descuento". ?Es un número decimal compuesto por 3 enteros y 5 decimales. ?Validación: Se deberá de incluir un valor igual o menor al del Monto total. Caso contrario se rechazará el comprobante. | | | | | | | 4
| > > > CodigoDescuento | Código del descuento | String | 2 | ?Ver Nota 20. ?Este campo será de condición obligatoria, cuando se incluya información en el campo "monto de descuentos concedidos" ?Validación: Se verificará el cumplimiento de la nota 20. | | | | | | | 4
| > > > CodigoDescuentoOTRO | Código del descuento OTRO | String | 00 | ?Será obligatorio en caso de utilizar el código 99 de "Otros" de la nota 20. Se debe describir puntualmente el descuento utilizado. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 00. | 2 | 2 | 2 | 2 | 2 | 2 | 4
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo |
FE | FEE | FEC | TE | NC | ND | REP |
> > > NaturalezaDescuento | Naturaleza del descuento | String | 80 | ?Este campo será de condición obligatoria, cuando se utilice el código 99 de la Nota 20. ?Validación: En caso de utilizarse el código 99, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. Además, deberá contener mínimo 3 caracteres y un máximo de 80. | 2 | 2 | 2 | 2 | 2 | 2 | 4 |
> > SubTotal | Subtotal | Decimal | 8,5 | ?Se obtiene de la resta del campo "monto total" menos "monto de descuento concedido". ?Es un número decimal compuesto por 3 enteros y 5 decimales. ?En caso del Recibo Electrónico de Pago este campo será editable y corresponderá al monto del pago a registrar para el cálculo del IVA respectivo. | | | | | | | |
> > IVACobradoFabrica | IVA cobrado a nivel de fábrica | String | 2 | ?Ver nota 2 . ?En este campo se indicará si el Impuesto al Valor Agregado fue cobrado a nivel de fábrica, por lo que deberá ser utilizado únicamente por los obligados tributarios a realizar el pago de esta forma. ?Se convierte en obligatorio cuando el IVA se cobra o se cobró a nivel de fábrica. ?Al hacer uso del presente campo el producto se entenderá exento para el código 02, por lo cual no deberá llenar el subnodo de impuestos para el cálculo del IVA. ?Para el código 0 el emisor puede separar los impuestos que está cobrando en la fábrica. | 2 | 4 | 4 | 2 | 2 | 2 | 4 |
> > BaseImponible | Base imponible | Decimal | 8,5 | ?Este campo será de condición obligatoria, cuando el producto/ servicio este gravado con algún impuesto. Se obtiene de la suma entre el campo "Subtotal", más el impuesto selectivo de consumo (02), el Impuesto específico de Bebidas Alcohólicas (04), el Impuesto Específico sobre las bebidas envasadas sin contenido alcohólico y jabones de tocador (05) y el impuesto al cemento ( 2), cuando corresponda. ?Este campo se podrá editar cuando se seleccione en el campo "IVA cobrado a nivel de fábrica" el Código 01 o en el campo de "Código del impuesto" el código 07. ?Validación: En caso de utilizarse el código 0 , en el campo de IVA cobrado a nivel de fábrica, se verificará que este campo se encuentre en el comprobante, y deberá incluirse un valor mayor a "cero". Caso contrario se rechazará. | | 4 | | | | | 4 |
| Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
| FE | FEE | FEC | TE | NC | ND | REP
| > > Impuesto {1,1000} | Impuesto | Complex Type | | ?Tipo complejo con el detalle del impuesto. Este campo será de condición obligatoria en todos los comprobantes. ?Se pueden utilizar para una misma línea la cantidad de códigos de impuestos que se requieran para cada producto. ?En el "Recibo Electrónico de Pago" se volverá obligatorio, cuando la condición de la venta sea códigos "08" y "10" de la nota "5". | 1 | 1 | 1 | 1 | 1 | 1 | 2
| > > > Codigo | Código del impuesto | String | 2 | ?Ver nota 8. Es un campo fijo de dos posiciones. ?Al utilizar el código de Naturaleza del Descuento 01 correspondiente a "Regalías" o 03 de "Bonificaciones" y el código de impuesto 01, se debe utilizar para el cálculo del impuesto el campo denominado "Monto Total" y la tarifa. ?Al utilizar el código 07 se debe de utilizar para el cálculo del impuesto el campo denominado "base imponible "y la tarifa. ?Al utilizar el código 08, se debe utilizar para el cálculo de factor del IVA por el subtotal. ?Validación: Se verificará el cumplimiento de la nota 8. | 1 | 1 | 1 | 1 | 1 | 1 | 1
| > > CodigoImpuestoOTRO | Código de impuesto OTRO | String | 100 | ?Será obligatorio en caso de utilizar el código 99 de "Otros" de la nota 8. Se debe describir puntualmente el impuesto utilizado. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 100. | 2 | 2 | 2 | 2 | 2 | 2 | 2
| > > > CodigoTarifaIVA | Código de la tarifa del Impuesto al Valor Agregado | String | 2 | ?Ver nota 8.1. Es un campo fijo de dos posiciones. ?Se convierte en obligatorio para los Códigos 01, 07. de la nota 8. ?En el caso que se utilice el nodo "Detalle de productos del surtido, paquetes o combos", no se deberá utilizar este campo, ya que el impuesto se calcula como la suma de los montos de impuestos individuales de las líneas de detalle de los componentes del surtido que se deben incluir en estos casos. La eventual validación de la consistencia de los impuestos calculados y aplicación de tarifas se hará sobre las líneas individuales de detalle. ?Validación: Se verificará el cumplimiento de nota 8.1. cuando se utilice el código 01 y 07 de campo código del impuesto. Con la excepción cuando se utilicen códigos CABYS de surtido. | 2 | 2 | 2 | 2 | 2 | 2 | 2
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo |
FE | FEE | FEC | TE | NC | ND | REP |
> > > Tarifa | Tarifa del impuesto | Decimal | 4,2 | ?Este campo es de condición obligatoria, cuando el producto/servicio este gravado con alguna tarifa de impuesto, según corresponda. Debe de expresarse el porcentaje como número entero (Ejemplo: la tarifa del 13% se debe de reflejar como 13, la tarifa del 1% como 1, o bien la tarifa del 0.5% como 0.5). ?Para Cálculo del IVA, Ver nota 8.1 ?En el caso que se utilice el nodo "Detalle de productos del surtido, paquetes o combos", no se deberá utilizar este campo, ya que el impuesto se calcula como la suma de los montos de impuestos individuales de las líneas de detalle de componentes del surtido que se deben incluir en estos casos. ?La eventual validación de la consistencia de los impuestos calculados y aplicación de tarifas se hará sobre las líneas individuales de detalle. ?Para Cálculo del Impuesto Selectivo de Consumo código 02 de la nota 8, la tarifa será editable, según la normativa correspondiente. ?Para Cálculo del Impuesto al Cemento código 12 de la nota 8, la tarifa será del 5%. ?Para Cálculo de "otros impuestos" código 99, la tarifa será editable, según la normativa correspondientes ?Validación: Cuando se utilice el código de impuesto 01 la tarifa del impuesto debe de coincidir con el correspondiente código de impuesto IVA, caso contrario se rechazará. Si se utiliza código de impuesto 02 o 99 debe de incluirse el porcentaje como un número entero. Con la excepción cuando se utilicen códigos CABYS de surtido. | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
> > > FactorCalculoIVA | Factor para Calculo IVA | Decimal | 5,4 | ?Este campo es de condición obligatoria, cuando el producto/servicio posea un factor para su cálculo. ?Cuando en el código de impuesto se defina IVA Bienes Usados se deberá utilizar este campo con el factor establecido por el Ministerio de Hacienda. ?Debe expresarse en formato decimal. ?Validación: En caso de utilizar el código 08 de la nota 08, se verificará que este campo se encuentre en el comprobante, caso contario se rechazará | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo |
FE | FEE | FEC | TE | NC | ND | REP |
9> > > DatosImpuestoEspecifico | Datos para Impuestos Específicos | Complex Type | | ?Tipo complejo con el detalle para calcular impuestos específicos no tarifarios. ?Este campo es de condición obligatoria, cuando se utilicen los códigos de impuesto 03, 04, 05, 06 de la nota 8 y agrupará los campos requeridos para el cálculo de estos impuestos ?Validación: En caso de utilizarse el código 03,04,05,06 de la nota 8, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. | 2 | 4 | 4 | 2 | 2 | 2 | 4 |
10> > > > CantidadUnidadMedida | Cantidad de la unidad de medida a utilizar | Decimal | 7,2 | ?Este campo es de condición obligatoria, cuando se utilicen los códigos de impuesto 03, 04, 05 y 06 de la nota 8 ?En el caso que se utilice el nodo "Detalle de productos del surtido, paquetes o combos", no se deberá utilizar este campo, para los códigos de impuesto 04, 05, 06 de la nota 8, ya que el impuesto se calcula como la suma de los montos de impuestos individuales de las líneas de detalle de componentes del surtido que se deben incluir en estos casos. La eventual validación de la consistencia de los impuestos calculados y aplicación de tarifas se hará sobre las líneas individuales de detalle. ?Validación: En caso de utilizarse el código 03,04,05,06 de la nota 8, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. Con la excepción cuando se utilicen códigos CAByS de surtido. | | 4 | 4 | | | | 4 |
11 > > > > Porcentaje | Porcentaje | Decimal | 4,2 | ?Este campo es de condición obligatoria, cuando se utilice el código de impuesto 04 de la nota 8. ?En el caso que se utilice el nodo "Detalle de productos del surtido, paquetes o combos", no se deberá utilizar este campo, para el código de impuesto 04, de la nota 8, ya que el impuesto se calcula como la suma de los montos de impuestos individuales de las líneas de detalle de componentes del surtido que se deben incluir en estos | 2 | 4 | 4 | 2 | 2 | 2 | 4 |
| | | | | | | | | | | | | | | | | | | | | | | |
9 Este nodo se utilizará exclusivamente para el calculo de los impuestos específicos siguientes: Impuesto a los combustibles (código 03), Impuesto de Bebidas Alcohólicas (código 04), Impuesto Específico sobre las bebidas envasadas sin contenido alcohólico y jabones de tocador (código 05) e Impuesto a los Productos de Tabaco (código 06)
10 Este campo corresponderá a lo siguiente según el tipo de impuesto: código 03: Cantidad de Litros de combustible, códigos 04 y 05: Cantidad de mililitros del envase a vender o unidades de jabón de tocador a vender.
11 Este campo corresponderá a lo siguiente para el tipo de impuesto código 04: porcentaje de alcohol por volumen de la bebida.
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
| | | | casos. La eventual validación de la consistencia de los impuestos calculados y aplicación de tarifas se hará sobre las líneas individuales de detalle. ?Debe de expresarse el porcentaje como número entero (Ejemplo: la tarifa del 13% se debe de reflejar como 13, la tarifa del 1% como 1, o bien la tarifa del 0.5% como 0.5). ?Validación: En caso de utilizarse el código 04 de la nota 8, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. Con la excepción cuando se utilicen códigos CAByS de surtido. | | | | | | |
12> > > > Proporcion | Proporción | Decimal | 5,2 | ?Este campo es de condición obligatoria, cuando se utilice el código de impuesto 04 de la nota 8 ?Este campo se obtiene de multiplicar la "Cantidad de la unidad de medida a utilizar" por el "Porcentaje" ?En el caso que se utilice el nodo "Detalle de productos del surtido, paquetes o combos", no se deberá utilizar este campo, para el código de impuesto 04, de la nota 8, ya que el impuesto se calcula como la suma de los montos de impuestos individuales de las líneas de detalle de componentes del surtido que se deben incluir en estos casos. La eventual validación de la consistencia de los impuestos calculados y aplicación de tarifas se hará sobre las líneas individuales de detalle ?Validación: En caso de utilizarse el código 04 de la nota 8, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. Con la excepción cuando se utilicen códigos CAByS de surtido. | 2 | 4 | 4 | 2 | 2 | 2 | 4
13> > > > VolumenUnidadConsumo | Volumen por Unidad de Consumo | Decimal | 7,2 | ?Este campo es de condición obligatoria, cuando se utilice el código de impuesto 05 de la nota 8 ?En el caso que se utilice el nodo "Detalle de productos del surtido, paquetes o combos", no se deberá utilizar este campo, para el código de impuesto 05, de la nota 8, ya que el impuesto se calcula como la suma de los montos de impuestos individuales de las líneas de detalle de | 2 | 4 | 4 | 2 | 2 | 2 | 4
12 Este es un campo de cálculo, que en el tipo de impuesto código 04: Es la cantidad de mililitros de alcohol absoluto que se calcula multiplicando los campos del porcentaje de alcohol por volumen por la cantidad de mililitros por cada tipo de bebida.
13 Este campo corresponderá a lo siguiente en el tipo de impuesto código 05: Volumen de Referencia en Mililitros o volumen en gramos de jabón de tocador a vender. De acuerdo con el artículo 9 de la Ley número 8114 de fecha 4 de julio de 2001, denominada "Ley de Simplificación y Eficiencia Tributarias" y sus reformas.
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
| | | | componentes del surtido que se deben incluir en estos casos. La eventual validación de la consistencia de los impuestos calculados y aplicación de tarifas se hará sobre las líneas individuales de detalle ?Validación: En caso de utilizarse el código 05 de la nota 8, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. Con la excepción cuando se utilicen códigos CAByS de surtido. | | | | | | |
14> > > > lmpuestoUnidad | lmpuesto por Unidad | Decimal | 8,5 | ?Este campo es de condición obligatoria, cuando se utilicen los códigos de impuesto 03, 04, 05 y 06 de la nota 8 ?En el caso que se utilice el nodo "Detalle de productos del surtido, paquetes o combos", no se deberá utilizar este campo, para los códigos de impuesto 04, 05, 06 de la nota 8, ya que el impuesto se calcula como la suma de los montos de impuestos individuales de las líneas de detalle de componentes del surtido que se deben incluir en estos casos. La eventual validación de la consistencia de los impuestos calculados y aplicación de tarifas se hará sobre las líneas individuales de detalle. ?Validación: En caso de utilizarse el código 03,04,05,06 de la nota 8, se verificará que este campo se encuentre en el comprobante, caso contrario se rechazará. Con la excepción cuando se utilicen códigos CAByS de surtido. | | 4 | 4 | | | | 4
> > > Monto | Monto del impuesto | Decimal | 8,5 | ?Este campo será de condición obligatoria, cuando el producto/servicio este gravado con algún impuesto. Es un número decimal compuesto por 3 enteros y 5 decimales. ?Cálculo del IVA: Se obtiene de la multiplicación del campo "tarifa del impuesto" por "Base Imponible". | | | | | | |
[imagen]
14 En este campo se indicará el monto del impuesto por unidad, según el tipo de impuesto específico, códigos 03, 04, 05 o 06, según corresponda de acuerdo con la normativa que regule cada uno de estos.
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo |
FE | FEE | FEC | TE | NC | ND | REP |
| | | | ?Casos especiales para el cálculo del IVA: Calculo cuando se usa código 10 tarifa exenta: Al utilizar el código de Naturaleza del Descuento 01 correspondiente a "Regalías" o 03 de "Bonificaciones" y el código de impuesto 01, se debe utilizar para el cálculo del impuesto el campo denominado "Monto Total" y la "Tarifa". En caso de utilizar el factor establecido para el régimen de bienes usados, este campo se obtiene de la multiplicación del factor por 100 por el subtotal. En caso de utilizar el campo "Base Imponible Especial", este campo se obtiene de la multiplicación "Base Imponible Especial" por la tarifa. En el caso de utilizar el nodo "Detalle de productos del surtido, paquetes o combos", este campo se calcula como la sumatoria de los montos de IVA individuales de las líneas de detalle del surtido que se deben incluir en estos casos ?Cálculo Impuesto Selectivo de Consumo: Se obtiene de la multiplicación del campo "tarifa del impuesto" por el campo "subtotal" En el caso de utilizar el nodo "Detalle de productos del surtido, paquetes o combos", este campo se calcula como la sumatoria de los montos del Impuesto Selectivo de Consumo individuales de las líneas de detalle del surtido que se deben incluir en estos casos ?Cálculo Impuesto Único a los Combustibles Se obtiene de la multiplicación del campo "Cantidad de la unidad de medida a utilizar" por el campo "Impuesto por Unidad" ?Calculo Impuesto específico a las Bebidas Alcohólicas Se obtiene de la multiplicación del campo "Cantidad" por el campo "Proporción" por "Impuesto por Unidad" En el caso de utilizar el nodo "Detalle de productos del surtido, paquetes o combos", este campo se calcula como la sumatoria de los montos del Impuesto Específico a las Bebidas Alcohólicas individuales de las líneas de detalle del surtido que se deben incluir en estos casos | | | | | | | |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo |
FE | FEE | FEC | TE | NC | ND | REP |
| | | | ?Cálculo del Impuesto Específico sobre las bebidas envasadas sin contenido alcohólico y jabones de tocador Para el caso de las bebidas, se obtiene de la multiplicación del campo "Cantidad" por el campo "Cantidad de la unidad de medida a utilizar" multiplicado por el resultado de dividir el campo "Impuesto por Unidad" entre el campo "Volumen por Unidad de Consumo" Para el caso del jabón de tocador, se obtiene de la multiplicación del campo "Cantidad de la unidad de medida a utilizar" por el campo "Volumen por Unidad de Consumo" por "Impuesto por Unidad" En el caso de utilizar el nodo "Detalle de productos del surtido, paquetes o combos", este campo se calcula como la sumatoria de los montos de los Impuestos Específicos sobre las bebidas envasadas sin contenido alcohólico o jabones de tocador individuales de las líneas de detalle del surtido que se deben incluir en estos casos ?Cálculo del Impuesto a los productos de Tabaco Se obtiene de la multiplicación del campo "Cantidad" por el campo "Cantidad de la unidad de medida a utilizar" por "Impuesto por Unidad" En el caso de utilizar el nodo "Detalle de productos del surtido, paquetes o combos", este campo se calcula como la sumatoria de los montos del Impuesto a los productos de tabaco individuales de las líneas de detalle del surtido que se deben incluir en estos casos ?Impuesto al Cemento Se obtiene de la multiplicación del campo "tarifa del impuesto" por el campo "subtotal" | | | | | | | |
> > > MontoExportacion | Monto de impuesto de exportación. | Decimal | 18,5 | ?Uso exclusivo para exportación de mercancías que apliquen impuestos especiales. ?También podrá ser utilizado en las notas de crédito y débito según corresponda. ?Cuando se utilicen CAByS de servicios no se verificará. | 4 | 2 | 4 | 4 | 2 | 2 | 4 |
> > > Exoneracion | Información de exoneración | Complex Type | | ?Tipo complejo con detalles de la exoneración. Este campo será de condición obligatoria cuando la venta tenga alguna exoneración. | 2 | 4 | 2 | 2 | 2 | 2 | 4 |
> > > > TipoDocumentoEX1 | Tipo de documento de exoneración o de autorización. | String | 2 | ?Es un campo fijo de dos posiciones Ver nota 10.1 y 7. ?Validación: Se verificará el cumplimiento de la nota 10.1 | 1 | 4 | 1 | 1 | 1 | 1 | 4 |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo |
FE | FEE | FEC | TE | NC | ND | REP |
> > > > TipoDocumentoOTRO | Tipo de documento de exoneración o de autorización OTRO | String | 100 | ?Será obligatorio en caso de utilizar el código 99 de "Otros" de la nota 10.1. Se debe describir puntualmente el tipo de documento o autorización utilizado. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 100. | 2 | 2 | 2 | 2 | 2 | 2 | 4 |
> > > > NumeroDocumento | Número de documento de exoneración o de autorización | String | 40 | ?Este campo será de condición obligatoria, cuando se incluya información en el campo "Tipo de documento de exoneración o de autorización" ?Debe de indicarse tal y como se encuentra en el documento otorgado por la institución incluyendo los guiones. ?En caso de utilizar los códigos "02" o "03" y "08" de la nota 10.1 en el tipo de documento debe de indicar el número de la ley que lo autoriza. ?Validación: En caso de utilizarse el código 04 y 11 de la nota 10.1, se verificará que el número de autorización debe de coincidir con el otorgado en el documento de exoneración y que este vigente. Caso contrario se rechazará el comprobante. ?Deberá contener mínimo 3 caracteres y un máximo de 40 | 1 | 4 | 1 | 1 | 1 | 1 | 4 |
> > > > Articulo | Número de artículo que establece la exoneración o autorización | lnteger | 6 | ?Este campo será de condición obligatoria, cuando se elija para "Tipo de documento de exoneración o de autorización" los códigos "02" o "03", "06", "07" y "08, de la nota 10.1 se debe de indicar el número del artículo de la ley. | 2 | 4 | 2 | 2 | 2 | 2 | 4 |
> > > > lnciso | Número de inciso que establece la exoneración o autorización | lnteger | 6 | ?Este campo será de condición obligatoria, cuando el artículo de la ley hace referencia a un inciso de la misma, por lo cual se debe de indicar el número del inciso de la ley. De no existir un inciso, se indicará un cero en el campo. | 2 | 4 | 2 | 2 | 2 | 2 | 4 |
> > > > Nombrelnstitucion | Nombre de institución o dependencia que emitió la exoneración | String | 160 | ? Ver notas 23 y 7. Es un campo fijo de dos posiciones ?Este campo será de condición obligatoria, cuando se incluya información en el campo "Tipo de documento de exoneración o de autorización" ?Validación: Cumplimiento de la Nota 23. | 1 | 4 | 1 | 1 | 1 | 1 | 4 |
> > > > NombrelnstitucionOtros | Detalle Nombre de institución o dependencia que emitió la exoneración OTRO | String | 160 | ?Será obligatorio en caso de utilizar el código 99 de "Otros" de la nota 23. Se debe describir puntualmente la condición de la venta utilizada. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 100. | 2 | 2 | 2 | 2 | 2 | 2 | 4 |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo |
FE | FEE | FEC | TE | NC | ND | REP |
> > > > FechaEmisionEX | Fecha de emisión del documento de exoneración o de autorización | DateTim e | | ?Este campo será de condición obligatoria, cuando se incluya información en el campo "Tipo de documento de exoneración o de autorización". ?Tipo de dato de fecha y hora, basado en el estándar RFC3339 sección 5.6, tipo "date-time". Formato: YYYY-MM-DDThh:mi:ss[Zl(+l-)hh:mm] Ejemplo: 2016-09-26T13:00:00+06:00 ?Validación: En caso de utilizarse el código 04 y 11 de la nota 10.1, se verificará la fecha de emisión del documento de exoneración. En caso de no coincidir se rechazará el comprobante. | 1 | 4 | 1 | 1 | 1 | 1 | 4 |
> > > > tarifaexonerada | Tarifa exonerada | Decimal | 4,2 | ?Este campo será de condición obligatoria, cuando se incluya información en el campo "Tipo de documento de exoneración o de autorización" ?Debe de indicarse los puntos de la tarifa otorgado de exoneración. Debe de expresarse el porcentaje como número entero (Ejemplo: la tarifa del 13% se debe de reflejar como 13, la tarifa del 1% como 1, o bien la tarifa del 0.5% como 0.5). ?Validación: En caso de utilizarse el código 04 y 11 de la nota 10.1, se verificará la tarifa exonerada. En caso de ser un porcentaje mayor se rechazará el comprobante. | 1 | 4 | 1 | 1 | 1 | 1 | 4 |
> > > > MontoExoneracion | Monto del Impuesto Exonerado | Decimal | 18,5 | ?Este campo será de condición obligatoria, cuando se incluya información en el campo "Tipo de exoneración". ?Es un número decimal compuesto por 13 enteros y 5 decimales. ?Dicho monto se obtiene de la multiplicación del campo "Tarifa exonerada" por el campo "Subtotal" | 1 | 4 | 1 | 1 | 1 | 1 | 4 |
> > ImpuestoAsumidoEmisorFabrica | Impuestos Asumidos por el Emisor o cobrado a Nivel de Fábrica | Decimal | 18,5 | ?Es un número decimal compuesto por 13 enteros y 5 decimales. ?Este campo será de condición obligatoria cuando: ?Se facturen productos o servicios, en cuya línea de detalle se indique en el campo "Código del descuento" los códigos 01 de "Regalías" o código 03 de "Bonificaciones". ?Se incluyan en la línea de detalle impuestos específicos a los combustibles, Bebidas Alcohólicas, sin contenido alcohólico, jabón de tocador y cemento. ?Se obtiene de la sumatoria del Monto de los Impuestos calculados a productos definidos como regalías o bonificaciones con IVA cobrado a nivel de fábrica, y se incluyan impuestos específicos a los combustibles, Bebidas | 1 | 4 | 4 | 1 | 2 | 2 | 4 |
| Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
| FE | FEE | FEC | TE | NC | ND | REP
| | | | | Alcohólicas, sin contenido alcohólico, jabón y cemento. En caso de no aplicarse estos impuestos, se deberá agregar el valor "0". ?Validación: En el caso de utilizarse los códigos 0 y 03 de la nota 20 o bien, impuestos cobrados a nivel de fabrica este campo deberá contener un valor mayor a "cero". En caso de no aplicarse estos impuestos, se deberá agregar el valor "0". Caso contrario se rechazará el comprobante. | | | | | | |
| > > lmpuestoNeto | lmpuesto Neto | Decimal | 8,5 | ?Es un número decimal compuesto por 3 enteros y 5 decimales. ?Este monto se obtiene al restar el campo "Monto del Impuesto" menos "Monto del Impuesto Exonerado" o el campo "Impuestos Asumidos por el Emisor o cobrado a Nivel de Fábrica" cuando corresponda. ?En caso de no contar con datos en los campos "Monto del Impuesto Exonerado" o "Impuestos Asumidos por el Emisor o cobrado a Nivel de Fábrica" el monto será el mismo al del impuesto calculado. | | 4 | | | | |
| > > MontoTotallinea | Total, por línea de detalle | Decimal | 8,5 | ?Es un número decimal compuesto por 3 enteros y 5 decimales. ?Se calcula de la siguiente manera: Es la sumatoria de los campos "Subtotal" e "Impuesto Neto". | | | | | | |
| OtrosCargos {0, 5} | lnformacion sobre otros Cargos. | Complex Type | | ?Tipo complejo. ?Se puede incluir un máximo de 5 repeticiones, cuando se posean otros cargos adicionales al apartado de detalle de mercancía o servicio prestado. Únicamente, cuando se seleccione el código 04, 08, 09 y 0 de la nota 16 en el campo "Tipo de documento otros cargos" y no se cuente con una línea de servicio o producto, no es obligatorio usar el nodo "Detalle de la mercancía o servicio prestado". | 2 | 2 | 2 | 2 | 2 | 2 | 4
| > TipoDocumentoOC | Tipo de documento otros cargos | String | 2 | ?Ver nota 6. ?Validación: Se verificará el cumplimiento de la nota 6. Además, cuando se seleccione el código 04, 08, 09 y 0 de la nota 16 en "Tipo de documento otros cargos" y no se cuente con una línea de servicio o producto, no es obligatorio usar el nodo "Detalle de la mercancía o servicio prestado". | | | | | | | 4
| | | | | | | | | | | | | | | | | | | | | | | |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
> TipoDocumentoOTROS | Tipo de documento OTRO | String | 00 | ?Será obligatorio en caso de utilizar el código 99 de "Otros" de la nota 6. Se debe describir puntualmente el tipo de documento utilizado. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 00. | 2 | 2 | 2 | 2 | 2 | 2 | 4
> > 15 IdentificacionTercero | Identificación de un Tercero | Complex Type | | ?Tipo complejo que contiene los datos de identificación del Tercero. ?Este campo será de condición obligatoria, cuando se seleccione en "tipo de documento" el código 04 de la nota 16. ?Validación: En caso de utilizarse el código 04 de la nota 6, se deberá de completar el campo. Caso contrario se rechazará el comprobante. | 2 | 2 | 2 | 2 | 2 | 2 | 4
> > > Tipo | Tipo de identificación del Tercero | String | 2 | ?Ver nota 4. ?Es un campo fijo de dos posiciones. ?Este campo será de condición obligatoria, cuando se posea información en el nodo "Número de cédula física/ jurídica/NITE/DIMEX del emisor/ Extranjero No Domiciliado. | | | | | | | 4
> > > Numero | Número de cédula física/jurídica/NITE/DIM EX/ Extranjero No Domiciliado, del Tercero | String | 20 | ?Este campo será de condición obligatoria, cuando se seleccione en "tipo de documento" el código 04 de la nota 16. ?El tercero debe de estar inscrito como contribuyente. ?Formato: La "Cédula física" debe de contener 9 dígitos, sin cero al inicio y sin guiones. La "cédula de personas Jurídicas" debe contener 10 dígitos y sin guiones. El "Documento de Identificación Migratorio para Extranjeros (DIMEX)" debe contener 11 o 12 dígitos, sin ceros al inicio y sin guiones. El "Documento de Identificación de la DGT (NITE)" debe contener 0 dígitos y sin guiones. ?El número de identificación del "Extranjero No Domiciliado", puede contener hasta un máximo de 20 caracteres (números y letras) en el campo denominado número, de lo contrario se mantienen las longitudes ya establecidas para los números de cédulas. ?Validación: Este campo se verificará cuando se seleccione en "tipo de documento" el código 04 de la nota 16. Deberá | | | | | | | 4
[imagen]
15 Se entenderá como tercero el contribuyente que vende o presta el servicio o mercancía que se está cobrando.
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
| | | | cumplir con el formato establecido según el tipo de identificación, caso contrario se rechazará el comprobante. ?El contribuyente debe estar inscrito ante la Administración Tributaria en todos los casos, excepto el número de identificación del "Extranjero No Domiciliado". | | | | | | |
> NombreTercero | Nombre o razón social del Receptor | String | 00 | ?Este campo será de condición obligatoria, cuando se seleccione en "tipo de documento" el código 04. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 00 | 2 | 4 | 2 | 2 | 2 | 2 | 4
> Detalle | Detalle otros cargos | String | 60 | ?Se debe de indicar la descripción del cargo. | | | | | | | 4
> PorcentajeOC | Porcentaje otros cargos | Decimal | 9,5 | ?En el caso que el cargo posea un porcentaje o monto para su cálculo se debe de indicar el mismo. Debe de expresarse el porcentaje como número entero (Ejemplo: la tarifa del 3% se debe de reflejar como 3, la tarifa del % como , o bien la tarifa del 0.5% como 0.5). | 2 | 2 | 2 | 2 | 2 | 2 | 4
> MontoCargo | Monto del cargo | Decimal | 8,5 | ?Monto total del cargo. ?Validación: Deberá de contener un valor mayor a "cero". Caso contrario se rechazará el comprobante. | | | | | | | 4
c) Resumen del comprobante /Total de comprobante. Moneda
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
ResumenFactura | Resumen de la Factura | ComplexType | | ?Tipo complejo que representa el resumen de la factura. | | | | | | |
> > CodigoTipoMoneda | Código y Tipo de Moneda | ComplexType | | ?Campo obligatorio en todos los comprobantes | | | | | | |
> > > CodigoMoneda | Código de la moneda | String | 3 | ?Ver nota 3 y nota 3. ? Validación: Se verificará el cumplimiento de la nota 3 y nota 3. | | | | | | |
> > > TipoCambio | Tipo de cambio | Oecimal | 8,5 | ?Es un número decimal compuesto por 3 enteros y 5 decimales. ?En caso de utilizar el código de moneda correspondiente a colones (CRC) en este campo será "1". ?En caso de utilizar el código de moneda correspondiente a dólares americanos (USO), se debe de indicar el tipo de cambio de venta de referencia publicado por el Banco Central de Costa Rica, conforme lo establece la Ley 9635. ?En caso de utilizar códigos de monedas, diferentes a los códigos CRC y USO se utilizará, el tipo de cambio respecto a colones. ?Validación: En caso de que en el campo "Código de la moneda" se utilicen colones (CRC) se verificará que el valor del campo sea "1". Caso contrario rechazará el comprobante. | | | | | | |
> TotalServ ravados | Total servicios gravados con IVA | Oecimal | 8,5 | ?Este campo será de condición obligatoria, cuando se seleccionen códigos CAByS que correspondan a un servicio y el servicio este gravado con IVA. ?Es un número decimal compuesto por 3 enteros y 5 decimales. ?En el caso que exista una exoneración Este campo se obtiene de la multiplicación ( aporcentaje de exoneración) por el monto de la venta. ?Porcentaje de exoneración: (Tarifa Exonerada /Tarifa IVA) ?Validación: En caso que en el campo "Código de bien o servicio" se utilicen códigos que empiecen con: 5,6,7,8,9 del CAByS y que este gravado con IVA, deberá de cumplir con el cálculo de este campo. Caso contrario rechazará el comprobante. | | | | | | |
> TotalServExentos | Total servicios exentos de IVA | Oecimal | 8,5 | ?Este campo será de condición obligatoria, cuando se seleccionen códigos CAByS que correspondan a un servicio y el servicio este exento de IVA. ?Es un número decimal compuesto por 3 enteros y 5 decimales. ?Validación: En caso que en el campo "Código de bien o servicio" se utilicen códigos que empiecen con: 5,6,7,8,9 del CAByS y que estén exentos de IVA, deberá de cumplir con el cálculo de este campo. Caso contrario rechazará el comprobante. | | | | | | |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
> TotalServExonerado | Total servicios exonerados del IVA | Decimal | 18,5 | ?Este campo será de condición obligatoria, cuando el servicio esté gravado y se preste a un cliente que goce de exoneración, se debe de indicar el monto equivalente al porcentaje exonerado. ?Se obtiene de la multiplicación del porcentaje de la exoneración por el monto del servicio. ?Es un número decimal compuesto por 13 enteros y 5 decimales. ?Validación: En caso que en el campo "Código de Bien o Servicio" se utilicen códigos que empiecen con: 5,6,7,8,9 del CAByS y que goce de exoneración del IVA, deberá de cumplir con el cálculo de este campo. Caso contrario se rechazará el comprobante. | 2 | 4 | 2 | 2 | 2 | 2 | 4
> TotalServNoSujeto | Total servicios No Sujetos de IVA | Decimal | 18,5 | ?Este campo será de condición obligatoria, cuando se seleccionen códigos CAByS que correspondan a un servicio y el servicio sea No Sujeto de IVA (que se utilicen los códigos de tarifa del IVA 01 y 11 de la nota 8.1) ?Es un número decimal compuesto por 13 enteros y 5 decimales. ?Validación: En caso que en el campo "Código de bien o servicio" se utilicen códigos que empiecen con: 5,6,7,8,9 del CAByS y que este no sujeto de IVA, deberá de cumplir con el cálculo de este campo. Caso contrario se rechazará el comprobante. | 2 | 4 | 2 | 2 | 2 | 2 | 4
> TotalMercanciasGravadas | Total mercancías gravadas con IVA | Decimal | 18,5 | ?Este campo será de condición obligatoria, cuando se seleccionen códigos CAByS que correspondan a una mercancía y la mercancía este gravada con IVA, con excepción de las mercancías que indiquen "IVA cobrado a nivel de fábrica" ?Es un número decimal compuesto por 13 enteros y 5 decimales. ?Este campo se obtiene de la sumatoria de los campos de Monto Total de cada línea de detalle que contenga IVA, menos las líneas de detalle que contengan el código de "IVA cobrado a nivel de Fábrica" ?En el caso que exista una exoneración este campo se obtiene de la multiplicación (1-porcentaje de exoneración) por el monto de la venta. ?Porcentaje de exoneración: (Tarifa Exonerada /Tarifa IVA) ?Validación: En caso que en el campo "Código de bien o servicio" se utilicen códigos que empiecen con: 0,1,2,3,4 del CAByS y que este gravado con IVA, deberá de cumplir con el cálculo de este campo. Caso contrario se rechazará el comprobante. | 2 | 2 | 2 | 2 | 2 | 2 | 4
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
> TotalMercanciasExentas | Total mercancías exentas de IVA | Decimal | 18,5 | ?Este campo será de condición obligatoria, cuando se seleccionen códigos CAByS que correspondan a una mercancía y la mercancía este exenta de IVA. ?Es un número decimal compuesto por 13 enteros y 5 decimales. ?Validación: En caso que en el campo "Código de bien o servicio" se utilicen códigos que empiecen con: O,1,2,3,4 del CAByS y que este exento de IVA, deberá de cumplir con el cálculo de este campo. Caso contrario se rechazará el comprobante. | 2 | 2 | 2 | 2 | 2 | 2 | 4
> TotalMercExonerada | Total mercancías exoneradas del IVA | Decimal | 18,5 | ?Este campo será de condición obligatoria, cuando la mercancía o producto esté gravada y se venda a un cliente que goce de exoneración para la compra de la misma. ?Se obtiene de la multiplicación del porcentaje de la exoneración por el monto del producto. ?Es un número decimal compuesto por 13 enteros y 5 decimales. ?Validación: En caso que en el campo "Código de bien o servicio" se utilicen códigos que empiecen con: O,1,2,3,4 del CAByS y que goce de exoneración del IVA, deberá de cumplir con el cálculo de este campo. Caso contrario se rechazará el comprobante. | 2 | 4 | 2 | 2 | 2 | 2 | 4
> TotalMercNoSujeta | Total mercancías No Sujetas de IVA | Decimal | 18,5 | ?Este campo será de condición obligatoria, cuando se seleccionen códigos CAByS que correspondan a una mercancía y la mercancía sea No Sujeta de IVA(que se utilicen los códigos de tarifa del IVA O1 y 11 de la nota 8.1). ?Es un número decimal compuesto por 13 enteros y 5 decimales. ?Validación: En caso que en el campo "Código de bien o servicio" se utilicen códigos que empiecen con: O,1,2,3,4 del CAByS y que este no sujeto de IVA, deberá de cumplir con el cálculo de este campo. Caso contrario se rechazará el comprobante. | 2 | 4 | 2 | 2 | 2 | 2 | 4
> TotalGravado | Total gravado | Decimal | 18,5 | ?Se obtiene de la suma de los campos "total servicios gravados con IVA" mas "total de mercancías gravadas con IVA". ?Es un número decimal compuesto por 13 enteros y 5 decimales. | 2 | 2 | 2 | 2 | 2 | 2 | 4
> TotalExento | Total exento | Decimal | 18,5 | ?Se obtiene de la suma de los campos "total servicios exentos de IVA" mas "total de mercancías exentas de IVA". ?Es un número decimal compuesto por 13 enteros y 5 decimales. | 2 | 2 | 2 | 2 | 2 | 2 | 4
> TotalExonerado | Total exonerado | Decimal | 18,5 | ?Se obtiene de la suma de los campos "total servicios exonerados de IVA" mas "total de mercancías exoneradas del IVA". ?Es un número decimal compuesto por 13 enteros y 5 decimales. | 2 | 4 | 2 | 2 | 2 | 2 | 4
> TotalNoSujeto | Total No Sujeto | Decimal | 18,5 | ?Se obtiene de la suma de los campos "Total servicios No Sujetos de IVA" mas "Total mercancías No Sujetas de IVA". Es un número decimal compuesto por 13 enteros y 5 decimales. | 2 | 4 | 2 | 2 | 2 | 2 | 4
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
> TotalVenta | Total venta | Decimal | 8,5 | ?Se obtiene de la sumatoria de los campos "total gravado", "total exento", "Total Exonerado" y "Total No Sujeto". ?En caso del "Recibo Electronico de Pago" se obtiene de la suma de los montos totales de las líneas de detalle. ?Es un número decimal compuesto por 3 enteros y 5 decimales. | | | | | | |
> TotalDescuentos | Total descuentos | Decimal | 8,5 | ?Se obtiene de la suma de todos los campos de "monto de descuentos concedidos". ?Es un número decimal compuesto por 3 enteros y 5 decimales. | 2 | 2 | 2 | 2 | 2 | 2 | 4
> TotalVentaNeta | Total venta neta | Decimal | 8,5 | ?Se obtiene de la resta de los campos "total venta" menos "total descuento". ?Es un número decimal compuesto por 3 enteros y 5 decimales. | | | | | | |
> TotalDesgloseImpuesto { , 000} | Total Desglose por Impuesto Cobrado | ComplexType | | ?Tipo complejo que contiene los montos desglosados por impuesto cobrado en el comprobante electrónico. ?Se repetirán la cantidad de códigos de impuestos que se hayan incluido en las líneas de detalles. En el caso de las líneas que contengan "surtidos", se utilizará para este cálculo la información de los campos monto del nodo "Impuesto Surtido". ?Este campo es de condición obligatoria, cuando existen producto/servicio gravados con algún impuesto en las líneas de detalle El mismo se obtiene de la suma de todos los campos denominados "Monto del impuesto" de las líneas que no poseen exoneración más todos los campos "Impuesto Neto" de las líneas que si poseen exoneración, o se calculen el campo "Impuestos Asumidos por el Emisor o cobrado a Nivel de Fábrica". ?Validación: En caso de utilizar líneas de detalles con cálculo de impuesto o monto del impuesto se verificará el cumplimiento de este nodo. Caso contrario se rechazará el comprobante. | 2 | 2 | 2 | 2 | 2 | 2 | 2
> > Codigo | Código de Impuesto | String | 2 | ?Ver nota 8. Es un campo fijo de dos posiciones. ?Indicará los códigos de impuesto registrados en las líneas de detalle. ?Validación: Se verificará el cumplimiento del registro por línea de detalle conforme a la nota 8. | | | | | | |
> > CodigoTarifaIVA | Código de la tarifa del Impuesto al Valor Agregado | String | 2 | ?Ver nota 8. . Es un campo fijo de dos posiciones. ?Se convierte en obligatorio para los Códigos 0 , 07. de la nota 8 ?Validación: Se verificará el cumplimiento del registro por línea de detalle conforme a la nota 8. . | 2 | 2 | 2 | 2 | 2 | 2 | 2
> > TotalMontoImpuesto | Monto por Tipo de Impuesto | Decimal | 8,5 | ?Se obtiene de la sumatoria del monto por código de impuesto cobrado en el comprobante electrónico | | | | | | |
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
> Totallmpuesto | Total de impuesto | Decimal | 18,5 | ?Este campo es de condición obligatoria, cuando existen producto/servicio gravados con algún impuesto en las líneas de detalle. El mismo se obtiene de la suma de todos los campos denominados "Monto del impuesto" de las líneas que no poseen exoneración más todos los campos "Impuesto Neto" de las líneas que si poseen exoneración, o se calculen el campo "Impuestos Asumidos por el Emisor o cobrado a Nivel de Fábrica". ?Es un número decimal compuesto por 13 enteros y 5 decimales. | 2 | 2 | 2 | 2 | 2 | 2 | 2
> TotallmpAsumEmisorFabrica | Total de lmpuestos Asumidos por el Emisor o cobrado a Nivel de Fábrica | Decimal | 18,5 | ?Este campo es de condición obligatoria, cuando existen producto/servicio gravados con algún impuesto en las líneas de detalle que sean asumidos por el emisor, el mismo se obtiene de la suma de todos los campos denominados "Impuestos Asumidos por el Emisor o cobrado a Nivel de Fábrica" ?Es un número decimal compuesto por 13 enteros y 5 decimales ?Validación: Se verificará el cumplimiento del cálculo de este campo cuando se incluyan en las líneas de detalle impuestos asumidos por el emisor o a nivel de fábrica. Caso contrario se rechazará el comprobante. | 2 | 2 | 2 | 2 | 2 | 2 | 4
> TotallVADevuelto | lVA Devuelto | Decimal | 18,5 | ?Este campo será de condición obligatoria cuando se facturen servicios de salud y cuyo método de pago sea "Tarjeta". ?Se obtiene de la sumatoria del Monto de los lmpuestos pagado por los servicios de salud en tarjetas. ?Es un número decimal compuesto por 13 enteros y 5 decimales. ?Validación: Se verificará que el monto indicado corresponda a líneas de detalle con códigos CABy'S de servicios médicos y el medio de pago sea tarjeta. Caso contrario se rechazará el comprobante. | 2 | 4 | 4 | 2 | 2 | 2 | 4
> TotalOtrosCargos | Total Otros Cargos | Decimal | 18,5 | ?Este campo será de condición obligatoria, cuando se posean otros cargos. ?Se obtiene de la suma de todos los campos "Monto del cargo" | 2 | 2 | 2 | 2 | 2 | 2 | 2
> MedioPago {1,4} | Medio de Pago | ComplexType | | ?Tipo complejo que contiene los montos desglosados por cada medio de pago utilizado. Este campo es de carácter obligatorio en todos los casos, excepto cuando se utilice en el campo condición de la venta, los códigos 02, 08 y 10, correspondientes a créditos ?Se puede utilizar hasta 4 tipos de medios de pago. | 2 | 2 | 2 | 2 | 2 | 2 | 1
> > TipoMedioPago | Tipo de Medio de Pago | String | 2 | ?Ver notas 6 y 7. Es un campo fijo de dos posiciones. ?Validación: Se verificará el cumplimiento de las notas 6 y 7. | 2 | 2 | 2 | 2 | 2 | 2 | 1
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
> > MedioPagoOtros | Detalle Medio de pago OTROS | String | 100 | ?Será obligatorio en caso de utilizar el código 99 de "Otros" de la nota 6. Se debe describir puntualmente el medio de pago utilizado. ?Validación: Deberá contener mínimo 3 caracteres y un máximo de 100 | 2 | 2 | 2 | 2 | 2 | 2 | 2
> > TotalMedioPago | Monto Total por Medio de Pago | Decimal | 18,5 | ?Se deberá detallar el monto correspondiente al tipo de pago seleccionado. Se volverá obligatorio cuando se utilice más de un medio de pago. ?Validación: Se deberá incluir un valor mayor a "cero". Caso contrario se rechazará el comprobante. | 2 | 2 | 2 | 2 | 2 | 2 | 2
> TotalComprobante | Total del comprobante | Decimal | 18,5 | ?En todos los comprobantes, se obtiene de la suma de los campos "total venta neta", "monto total del impuesto" y "total otros cargos" menos "total IVA devuelto" en caso de contar con dichos campos. ?En caso de Recibo Electrónico de Pago se obtiene de la suma de los campos "Total de la venta". ?Este monto deberá coincidir con la sumatoria de los montos de los totales por "Medio de Pago" cuando se utilicen dos o más. ?Es un número decimal compuesto por 13 enteros y 5 decimales. ?Validación: Se verificará que el cálculo coincida con la sumatoria de los montos de los totales por "Medio de Pago" cuando se utilicen dos o más. Caso contario se rechazará el comprobante. | 1 | 1 | 1 | 1 | 1 | 1 | 1
d) Información de referencia:
Se puede incluir un máximo de 10 repeticiones de información de referencia.
Las referencias se utilizarán para los siguientes casos:
a) Nota de crédito que elimina un documento de referencia en forma completa.
b) Nota de débito que elimina una nota de crédito en la referencia en forma completa.
c) Notas de crédito o débito que corrigen montos de otro documento.
d) Factura electrónica por contingencia, sustituyendo un comprobante provisional.
e) Cualquier documento relacionado con la factura electrónica.
f) Factura electrónica de compra, respaldando la compra a un no obligado a emitir comprobantes electrónicos.
g) Cualquier documento relacionado con un recibo de pago electrónico.
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
1nformacionReferencia {0,10} | 1nformación de Referencia | ComplexType | | ?Tipo complejo que representa el detalle de la referencia. ?Será obligatorio cuando se genere: 1. En "Factura Electrónica" el código 11 de la nota 10.1 en el campo ""Tipo de documento de autorización o exoneración", ? "Factura Electrónica de Compra", ? "Nota de Crédito Electrónica", ? "Nota de Débito Electrónica y ? "Recibo Electrónico de Pago". | 2 | 3 | 1 | 3 | 1 | 1 | 1
> TipoDoc1R | Tipo de documento de referencia | String | 2 | ?Ver nota 10 y 7. Es un campo fijo de dos posiciones ?El código 16 de "Comprobante de Proveedor No Domiciliado" únicamente podrá ser utilizado en la Factura Electrónica de Compra ?En el Comprobante "Recibo Electrónico de Pago", únicamente podrán ser utilizados los códigos 01, 02, 03, 04 y 08 correspondientes a "Factura Electrónica" Nota de Crédito Electrónica", "Nota de Débito Electrónica, "Tiquete Electrónico" y "Factura Electrónica de Compras". ?Validación: En caso de utilizar el código 16 de la nota 10 en los comprobantes electrónicos con excepción de la factura de compra se rechazará el comprobante. | 1 | 1 | 1 | 1 | 1 | 1 | 1
> TipoDocRefOTRO | Tipo de documento de referencia OTRO | String | 100 | ?Será obligatorio en caso de utilizar el código 99 de "Otros" de la nota 10. Se debe describir puntualmente el tipo de documento utilizado. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 100. | 2 | 2 | 2 | 2 | 2 | 2 | 2
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
>Numero | Clave numérica del comprobante electrónico o consecutivo del documento de referencia. | String | 50 | ?Este campo será de condición obligatoria, cuando se incluya información en el campo "Tipo de documento de referencia", excepto cuando se utilice el código 13 de la nota 10. ?Validación: En los casos que se utilicen los códigos 1,2,3,4,9,11,12,15 de la nota 10, se verificará que el documento de referencia sea una clave numérica valida. Caso contrario se rechazará el comprobante. ?Adicionalmente se verificará que la información incluida corresponda al comprobante de referencia (por ejemplo, tipo de cambio, CAByS, y que el monto del ajuste no supere al monto del comprobante en las notas de crédito). | 2 | 2 | 2 | 2 | 2 | 2 | 1
> FechaEmisionmR | Fecha de emisión del documento de referencia. | DateTime | | ?Este campo será de condición obligatoria, cuando se incluya información en el campo "Tipo de documento de referencia" ?Validación: Se verificará que la fecha de referencia no supere una antigüedad de 10 años. Caso contrario se rechazará el comprobante. | 1 | 1 | 1 | 1 | 1 | 1 | 1
> Codigo | Código de referencia | String | 2 | ?Ver nota 9 y 7. Es un campo fijo de dos posiciones. ?Este campo será de condición obligatoria, cuando se incluya información en el campo "Tipo de documento de referencia", excepto cuando se utilice el código 13 de la nota 10. ?Validación: Se verificará el cumplimiento de la nota 9 y 7. | 2 | 2 | 2 | 2 | 2 | 2 | 2
>CodigoReferenciaOTRO | Código de referencia OTRO | String | 100 | ?Será obligatorio en caso de utilizar el código 99 de "Otros" de la nota 9. Se debe describir puntualmente el código de referencia utilizado. ?Validación: Deberá contener mínimo 5 caracteres y un máximo de 100. | 2 | 2 | 2 | 2 | 2 | 2 | 2
> Razon | Razón de referencia | String | 180 | ?Este campo será de condición obligatoria, cuando se incluya información en el campo "Tipo de documento de referencia" excepto cuando se utilice el código 13 de la nota 10. ?Validación: Deberá contener mínimo 3 caracteres y un máximo de 180. | 2 | 2 | 2 | 2 | 2 | 2 | 2
e) Otros (Uso comercial, no tributario):
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
Otros | Otros | ComplexType | | ?Tipo complejo que agrupa varias definiciones de "Otros" | 3 | 3 | 3 | 3 | 3 | 3 | 4
> OtroTexto {0,?} | Otro Texto | String | 500 | ?Elemento opcional que se puede utilizar para almacenar texto. | 3 | 3 | 3 | 3 | 3 | 3 | 4
> OtroContenido {0,?} | Otro Contenido | String | 500 | ?Elemento opcional que se puede utilizar para almacenar contenido estructurado. | 3 | 3 | 3 | 3 | 3 | 3 | 4
f) Mecanismo de seguridad:
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
FE | FEE | FEC | TE | NC | ND | REP
ds Signature | Nodo par la firmas XadES | ds SignatureType | | ?Firma XadES-EPES v. .3.2. o superior. Este nodo, por medio del estándar de XadES permite realizar varias firmas al documento XML, con el fin que el emisor pueda cumplir con lo estipulado en la normativa vigente, con relación a que todo comprobante debe de ser firmado por el emisor electrónico. ?Todo archivo XML generado por un emisor-receptor electrónico, Emisor electrónico no confirmante y receptor electrónico-no emisor, que se encuentre obligado hacer uso de comprobantes electrónicos debe de ser enviado a la Dirección General de Tributacion para su respectiva validación una vez generado y firmado por el emisor. ?En caso de la Factura de Compra la misma debe de ser firmada por el Receptor que es quien la emite y la envía al validador. ?Adicionalmente en aquellos casos donde el "Emisor-receptor-electrónico" requiera que dicho comprobante cuente con la firma del receptor con el objetivo de cumplir con lo establecido en la Ley 8454 denominada "Ley de certificados, firmas digitales y documentos electrónicos", para que dicho comprobante se convierta en un título ejecutivo tal como lo establece los artículos 460 y 460 bis del código de comercio, debe utilizar el atributo <xades ClaimedRole> indicando la función que está ejerciendo, en este caso del "Receptor" ?En caso de requerirse el endoso de los comprobantes Factura Electrónica o Factura Electrónica de Exportación, tanto el endosante como el endosatario, posteriormente a la emisión del comprobante electrónico, deberán incorporar la firma, la cual debe estar al amparo bajo la Ley 8454 denominada "Ley de certificados, firmas digitales y documentos electrónicos, emitidas por las entidades bancarias. Para esto debe utilizar el atributo <xades ClaimedRole> indicando la función que está ejerciendo, en este caso, si es para el primer endoso, para el endosante el nombre "Endosante1" y para el endosatario el nombre "Endosatario1" y así sucesivamente ?El comprobante electrónico que posea las firmas del receptor o endosante y endosatario, no debe de ser enviado a la Dirección General de Tributacion al ser este comprobante únicamente para fines comerciales, ya que para fines tributarios será válido únicamente el primer archivo enviado por el emisor y aceptado por el Ministerio de Hacienda en el proceso de validación. Los emisores electrónicos que no requieran estas firmas adicionales, no tendrán obligación de utilizar el atributo <xades ClaimedRole> ?Ver Anexo 2 para visualizar el ejemplo de este mecanismo. | | | | | | |
III. Mensajes:
Establece los archivos XML para los mensajes que deben de utilizar los obligados tributarios al momento de la confirmación de aceptación o rechazo de los documentos electrónicos,
así como el mensaje que utilizará la Dirección General de Tributacion para comunicar al obligado tributarios la validación del comprobante electrónico.
Estos mensajes deben estar firmados digitalmente por el receptor del comprobante electrónico o por el Ministerio de Hacienda, según corresponda por el tipo de mensaje.
Para ver el formato de los mensajes hacer referencia a los archivos de Word: MensajeReceptor.doc y MensajeHacienda.doc; y a los XML Schemas: MensajeReceptor.xsd y MensajeHacienda.xsd.
- FORMATO PARA LA CONFIRMACIÓN DE ACEPTACIÓN O RECHAZO DE LOS DOCUMENTOS ELECTRÓNICOS POR PARTE DEL OBLIGADO TRIBUTARIO
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
Clave | Clave numérica del comprobante a confirmar | String | rO | ?Es un campo fijo de cincuenta posiciones. Solo permite ingresar números ?Validación: Deberá de verificar que la clave del comprobante electrónico valido por el Ministerio de Hacienda. | 1
NumeroCedulaEmisor | Número de cédula física/ jurídica/NITE/DIMEX del vendedor | Integer | 12 | ?Formato: La "Cédula física" debe de contener 9 dígitos, sin cero al inicio y sin guiones. La "cédula de personas Jurídicas" debe contener 10 dígitos y sin guiones. El "Documento de Identificación Migratorio para Extranjeros (DIMEX)" debe contener 11 o 12 dígitos, sin ceros al inicio y sin guiones. El "Documento de Identificación de la DGT (NITE)" debe contener 1O dígitos y sin guiones. ?Validación: Deberá de coincidir con el número de cédula del emisor con el comprobante que se esté confirmando. | 1
FechaEmisionDoc | Fecha y hora de Emisión de la confirmación | DateTime | | ?Validación: Se verificará que la fecha de confirmación no supere una antigüedad de 1O años. Caso contrario se rechazará el comprobante. | 1
Mensaje | Mensaje | Integer | 1 | ?Es un campo fijo de una posición Ver nota 11 y 7 ?Validación: Se verificará el cumplimiento de la nota 11y 7. | 1
DetalleMensaje | Detalle del mensaje | String | 16O | ?En los casos que la factura es aceptada no es necesario su uso, pero se convierte en obligatorio cuando la factura es rechazada o aceptada parcialmente, por cuanto se debe de indicar el motivo. ?Validación: Deberá de contener un mínimo de r caracteres y un máximo de 16O. | 2
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
CodigoActividad | Código Actividad Económica receptor | String | r | ?Debe indicar la actividad económica a la que el receptor desea aplicar el crédito. ?En caso de que deba aplicar la roporcionalidad no se debe de utilizar este campo. | 2
CondicionImpuesto | Condición del IVA | String | 2 | ?Ver nota 18. ?Validación: Se verificará el cumplimiento de la nota 18. | 2
MontoTotalImpuestoAcreditar | Monto del Impuesto acreditar | Decimal | 18,5 | ?Se puede utilizar, en los casos que el monto total del impuesto pagado, no forme en su totalidad parte del crédito aplicable. ?Si se elige 05 en la condición del IVA, no es necesario su uso ?En el caso que el mensaje de confirmación es de rechazo no es necesario su uso. | 2
MontoTotalDeGastoAplicable | Monto total del gasto a aplicar | Decimal | 18,5 | ?Se puede utilizar, en los casos que el monto total del comprobante, no forme en su totalidad un gasto o parte del IVA pagado se convierten en gastos. ?Si se elige 05 en la condición del IVA, no es necesario su uso ?En el caso que el mensaje de confirmación es de rechazo no es necesario su uso. | 2
MontoTotalImpuesto | Monto total de impuesto | Decimal | 18,5 | ?Este campo será de condición obligatoria, cuando el comprobante electrónico tenga impuesto ?Validación: Deberá de coincidir con el impuesto del comprobante que se está confirmando. | 2
TotalFactura | Total de la factura | Decimal | 18,5 | Validación: Deberá de coincidir con el total del comprobante que se está confirmando. | 1
NumeroCedulaReceptor | Número de cédula física / jurídica/NITE/DIMEX del comprador | Integer | 12 | ?Debe estar inscrito como contribuyente ante la Administración Tributaria, Formato: La "Cédula física" debe de contener 9 dígitos, sin cero al inicio y sin guiones. La "cédula de personas Jurídicas" debe contener 10 dígitos y sin guiones. El "Documento de Identificación Migratorio para Extranjeros (DIMEX)" debe contener 11 o 12 dígitos, sin ceros al inicio y sin guiones. El "Documento de Identificación de la DGT (NITE)" debe contener 10 dígitos y sin guiones. ?Validación: Deberá de coincidir con el número de cedula del receptor con el comprobante que se esté confirmando | 1
NumConsecutivoReceptor | Numeración consecutiva de los mensajes de confirmación | String | 20 | ?Es un campo fijo de veinte posiciones Ver nota 3 ?Validación: Se verificará el cumplimiento de la nota 3 | 1
ds:Signature | Nodo para las firmas XadES | ds:SignatureType | | ?Firma XadES-E ES v.1.3.2 o superior. Nota Importante: Este nodo debe crearse según ANEXO 2 | 1
- FORMATO DE USO EXCLUSIVO POR PARTE DE LA DIRECCIÓN GENERAL DE TRIBUTACIÓN UNA VEZ TERMINADO EL PROCESO DE VALIDACIÓN
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
Clave | Clave del comprobante electrónico validado | String | 50 | ?Es un campo fijo de cincuenta posiciones. Solo permite ingresar números | 1
NombreEmisor | Nombre o razón social del emisor del comprobante | String | 100 | | 1
TipoIdentificacionEmisor | Tipo de Identificación del Emisor | String | 2 | ?Es un campo fijo de dos posiciones. Este campo será de condición obligatoria, cuando se posea información en el nodo "Número de cédula física/ jurídica/NITE/DIMEX emisor Ver nota 4 | 1
NumeroCedulaEmisor | Número de cédula física/ jurídica/NITE/DIMEX emisor del comprobante electrónico | Integer | 12 | ?El contribuyente debe estar inscrito ante la Administración Tributaria. Este campo será de condición obligatoria, cuando se posea información en el nodo "Tipo de identificación del emisor. Formato: La "Cédula física" debe de contener 9 dígitos, sin cero al inicio y sin guiones. La "cédula de personas Jurídicas" debe contener 10 dígitos y sin guiones. El "Documento de Identificación Migratorio para Extranjeros (DIMEX)" debe contener 11 o 12 dígitos, sin ceros al inicio y sin guiones. El "Documento de Identificación de la DGT (NITE)" debe contener 10 dígitos y sin guiones. | 1
NombreReceptor | Nombre o razón social del receptor del comprobante electrónico | String | 100 | | 2
TipoIdentificacionReceptor | Tipo de Identificación del Receptor | String | 2 | ?Es un campo fijo de dos posiciones. Este campo será de condición obligatoria, cuando se posea información en el nodo "Número de cédula física/ jurídica/NITE/DIMEX/ Extranjero No Domiciliado del receptor. Ver nota 4 | 2
NumeroCedulaReceptor | Número de cédula física/ jurídica/NITE/DIMEX/ Extranjero No Domiciliado receptor del comprobante electrónico | String | 20 | ?Es un campo fijo de hasta veinte posiciones Ver nota 4.1 | 2
Mensaje | Mensaje | Integer | 1 | ?Ver nota 11 y 7 | 1
EstadoMensaje | Estado del mensaje | String | 9 | ?Deberá indicarse el estado del mensaje de acuerdo a lo seleccionado de la nota 11. | 1
DetalleMensaje | Detalle del mensaje | String | ? | | 1
Etiqueta | Nombre | Tipo | Tamaño | Descripción | Condición del Campo
MontoTotallmpuesto | Monto total de impuesto | Decimal | 18,5 | | 2
TotalFactura | Total de la factura | Decimal | 18,5 | | 1
ds:Signature | Nodo para las firmas XadES | ds:SignatureType | | ?Firma XadES-EPES v.1.3.2 o superior. Nota Importante: Este nodo debe crearse según ANEXO 2 | 1
IV. Notas sobre el Anexo 1
Nota 1/ En la representación gráfica los campos "Tipo de documento electrónico", "Clave del comprobante" y "numeración consecutiva" del comprobante deben
quedar juntos.
Nota 2/ Cada tipo de comprobante electrónico tiene su etiqueta y XML Schema.
Tipo de Documento | Etiqueta | XML Schema
Factura electrónica | Factura Electrónica | https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.4/facturaElectronica
Nota de débito electrónica | Nota Debito Electrónica | https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.4/notaDebitoElectronica
Nota de crédito electrónica | Nota Crédito Electrónica | https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.4/notaCreditoElectronica
Tiquete Electrónico | Tiquete Electrónico | https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.4/tiqueteElectronico
Factura Electrónica de Compra | Factura Electrónica Compra | https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.4/facturaElectronicaCompra
Factura Electrónica de Exportación | Factura Electrónica Exportación | https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.4/facturaElectronicaExportacion
Recibo Electrónico de Pago | Recibo Electrónico Pago | https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.4/reciboElectronicoPago
Nota 3/ La numeración de los comprobantes electrónicos y documentos asociados iniciará en 1, en aquellos casos donde el obligado tributario se traslade a utilizar comprobantes electrónicos por primera vez o se encuentre emitiendo los mismos conforme lo estipulado en la resolución Nº DGT-02-09, el sistema lo asignará automáticamente en el momento de la generación.
Para aquellos casos donde el obligado tributario ya se encuentra utilizando comprobantes electrónicos conforme a la resolución vigente, y decida cambiar de plataforma de emisión deberá mantener la numeración consecutiva.
Para generar la numeración consecutiva y la clave numérica del comprobante electrónico, definidas en la resolución vigente de comprobantes electrónicos que regula dicho consecutivo, se debe basar en la siguiente codificación:
Numeración consecutiva de los comprobantes electrónicos
Se conformará de la siguiente manera:
a) Los tres primeros dígitos identifican el local o establecimiento en el que se emitió el comprobante electrónico o documento asociado. El número 001 corresponde a la oficina central, casa matriz o establecimiento principal y los número 002 y subsiguientes identifican cada una de las sucursales.
b) Del cuarto al octavo dígito identificará la terminal o punto de venta de emisión del comprobante electrónico o documento asociado; en los casos que sólo se cuente con una terminal o se posea un servidor centralizado deberá visualizarse de la siguiente manera "00001".
c) Del noveno al décimo espacio corresponderá al tipo de comprobante electrónico o documento asociado; se deben utilizar los siguientes códigos:
Tipo de comprobante o documento asociado | Código
Factura electrónica | 01
Nota de débito electrónica | 02
Nota de crédito electrónica | 03
Tiquete electrónico | 04
Confirmación de aceptación del comprobante electrónico | 05
Confirmación de aceptación parcial del comprobante electrónico | 06
Confirmación de rechazo del comprobante electrónico | 07
Factura electrónica de compras | 08
Factura electrónica de exportación | 09
Recibo Electrónico de Pago | 10
d) Del undécimo al vigésimo dígito le corresponderá al consecutivo de los comprobantes electrónicos o documento asociado iniciando en el número 1, para cada sucursal o terminal según sea el caso.
En caso de que se llegue al tope del uso de la numeración consecutiva, se podrá volver a empezar desde el número 1.
Dicho consecutivo deberá visualizarse de la siguiente manera:
[imagen]
A: Casa matriz, sucursales
B: Terminal o punto de venta
C: Tipo de comprobante de documento asociado
D: Numeración del comprobante electrónico
Clave Numérica de los comprobantes electrónicos
Se conformará de la siguiente manera:
a) Los primeros tres dígitos corresponden al código del país (506).
b) Del cuarto al quinto dígito, corresponde al día en que se genere el comprobante electrónico.
c) Del sexto al séptimo dígito, corresponde al mes en que se genere el comprobante electrónico.
d) Del octavo al noveno dígito, corresponde al año en que se genere el comprobante electrónico.
e) Del décimo al vigésimo primero dígito, corresponde al número de cédula del emisor.
f) Del vigésimo segundo al cuadragésimo primero dígito, corresponde a la numeración consecutiva del comprobante electrónico.
g) El cuadragésimo segundo le corresponde a la situación del comprobante electrónico para el cual se debe de utilizar la siguiente codificación:
Código | Situación del comprobante electrónico | Descripción
1 | Normal | Corresponde a aquellos comprobantes electrónicos que son generados y transmitidos en el mismo acto de compraventa y prestación del servicio al sistema de validación de comprobantes electrónicos de la Dirección General de Tributación, conforme con lo establecido en la norma vigente.
2 | Contingencia | Corresponde a aquellos comprobantes electrónicos que sustituyen al comprobante físico emitido por contingencia, conforme lo establecido en la norma vigente.
3 | Sin internet | Corresponde a aquellos comprobantes que han sido generados y expresados en formato electrónico conforme lo establecido en la norma vigente, pero que no se cuenta con el respectivo acceso a internet.
h) Del cuadragésimo tercero al quincuagésimo dígito, corresponde al código de seguridad, el cual debe ser generado por el sistema del obligado tributario.
El formato de la clave del comprobante electrónico debe visualizarse de la siguiente manera:
[imagen]
Con respecto a los archivos que se generan para envió por correo y almacenamiento se debe acatar el siguiente formato:
- XML del comprobante electrónico: clave.xml (50600000000000000000000000000000000000000000000000.xml)
- XML de respuesta enviado por Hacienda: clave_respuesta.xml (50600000000000000000000000000000000000000000000000_respuesta.xml)
- Pdf del comprobante electrónico: clave.pdf (50600000000000000000000000000000000000000000000000.pdf)
En el caso de los XML de confirmación de los comprobantes electrónicos se debe utilizar el siguiente formato, el cual se encuentra compuesto de la clave del comprobante que se está confirmando guion (-) número de consecutivo del documento de confirmación:
- clave-consecutivo.xml (50600000000000000000000000000000000000000000000000-00100000000000000000.xml)
- clave-consecutivo.pdf (50600000000000000000000000000000000000000000000000-00100000000000000000.pdf)
- clave-consecutivo_respuesta.xml (50600000000000000000000000000000000000000000000000-00100000000000000000_respuesta.xml)
Nota 4/ El formato para el tipo de identificación es el siguiente:
Tipo de identificación | Código
Cédula Física | 01
Cédula Jurídica | 02
DIMEX | 03
NITE | 04
16 Extranjero No Domiciliado | 05
17No Contribuyente | 06
16 Este tipo de identificación estará disponible en los Datos del Emisor de la Factura Electrónica de Compra únicamente para el registro de las adquisiciones de servicios o bienes intangibles a proveedores no domiciliados en Costa Rica, según el artículo 29 inciso d) y el Transitorio XV del Reglamento del IVA.
En Factura Electrónica, estará disponible en los Datos del Receptor, únicamente cuando en el campo "Condición de la Venta" se haya seleccionado el código 12 "Ventas de Bienes No Nacionalizados"
Este código también estará habilitado para su uso en la Factura Electrónica de Exportación y Tiquete Electrónico.
17 Este tipo de identificación estará disponible en los Datos del Emisor de la Factura Electrónica de Compra únicamente para el registro de las adquisiciones de bienes usados vendidos por un no contribuyente para los efectos contables que corresponda. Estará disponible únicamente cuando en el campo "Condición de la Venta" se haya seleccionado el código 13 "Ventas Bienes Usados No Contribuyentes".
Nota 4.1/ El formato a utilizar en el número de identificación para generar la clave numérica es el siguiente:
Tipo de identificación | Nota
Cédula Física | Se debe agregar tres ceros antes de iniciar con el número de cédula con el fin de completar 12 dígitos
Cédula Jurídica | Se debe agregar dos ceros antes de iniciar con el número de cédula con el fin de completar 12 dígitos
DIMEX | En aquellos casos donde la cédula se encuentre compuesta de 11 dígitos se debe agregar un cero al inicio con el fin de completar 12 dígitos
NITE | Se debe agregar dos ceros antes de iniciar con el número de identificación con el fin de completar 12 dígitos
Nota 5/ En las Condiciones de la venta, se debe utilizar la siguiente codificación:
Condiciones de la venta | Código
Contado | 01
Crédito | 02
Consignación | 03
Apartado | 04
Arrendamiento con opción de compra | 05
Arrendamiento en función financiera | 06
Cobro a favor de un tercero | 07
18Servicios prestados al Estado | 08
19Pago de servicios prestado al Estado | 09
20Venta a crédito en IVA hasta 90 días (Artículo 27, IVA) | 10
21Pago de venta a crédito en IVA hasta 90 días (Artículo 27, IVA) | 11
22Venta Mercancía No Nacionalizada | 12
23Venta Bienes Usados No Contribuyente | 13
24Arrendamiento Operativo | 14
25Arrendamiento Financiero | 15
Otros (se debe indicar la condición de la venta en la representación gráfica) | 99
18 Se utiliza dicha condición de venta cuanto el servicio que se le preste al estado, una vez generada la factura no se recibe el pago de forma inmediata.
19 El código 09, Pago de servicios prestado al Estado se utilizará únicamente para efectos de los Recibos Electrónicos de Pago que cancelen una Factura Electrónica original con código 08. Cualquier modificación por medio de NC o ND, debe realizarse a la factura electrónica original, con código 08.
20 Este código se debe de utilizar, cuando el comprobante electrónico que se está generando por la venta de un bien o servicio gravado con IVA es a crédito y además la venta del bien o servicio cumple con las características establecidas en el artículo 3 inciso 8) y 27 de la LIVA.
21 El código 11, Pago de venta a crédito en IVA hasta 90 días (Artículo 27, LIVA) se utilizará. utilizará únicamente para efectos del Recibo Electrónico que cancelen una Factura Electrónica original con código 10. Cualquier modificación por medio de NC o ND, debe realizarse a la factura electrónica original, con código 10.
22 Ventas de una mercancía cuando la misma no se encuentra nacionalizada en Costa Rica, puede ser antes o después de haber presentado la Declaración de Mercancías ante la Autoridad Aduanera del país destino. Ejemplo: Ventas Sucesivas.
23 Ventas de bienes usados por parte un no contribuyente a un Obligado Tributario, que ocupe respaldar en su contabilidad dicha compra. Aplicará únicamente en factura electrónica de compra.
24 Se entiende como arrendamiento operativo, lo definido en las normas tributarias, por ejemplo, el Decreto 32876-H y sus modificaciones.
25 Se entiende como arrendamiento financiero, lo definido en las normas tributarias, por ejemplo, el Decreto 32876-H y sus modificaciones.
Nota 6/ En los medios de pago, se debe de utilizar la siguiente codificación:
Medios de pago | Código
Efectivo | 01
Tarjeta | 02
Cheque | 03
Transferencia - depósito bancario | 04
26Recaudado por terceros | 05
SINPE MOVIL | 06
Plataforma Digital | 07
Otros (se debe indicar el medio de pago en la representación gráfica) | 99
Nota 7/ Para efectos de visualización e impresión se mostrará su descripción.
Nota 8/ El desglose de los Códigos de los impuestos son los siguientes:
Código del Impuesto* | Código
Impuesto al Valor Agregado | 01
Impuesto Selectivo de Consumo | 02
Impuesto Único a los Combustibles | 03
Impuesto específico de Bebidas Alcohólicas | 04
Impuesto Específico sobre las bebidas envasadas sin contenido alcohólico y jabones de tocador | 05
Impuesto a los Productos de Tabaco | 06
27IVA (cálculo especial) | 07
IVA Régimen de Bienes Usados (Factor) | 08
Impuesto Específico al Cemento | 12
Otros | 99
26 El código 06, Recaudado por terceros se utilizará cuando el pago sea recibido por un tercero y no por quien emite el servicio o mercancía ejemplo: pago de recibos telefónicos en supermercados
27 Este código se utilizará cuando se realicen ventas de bienes o servicios donde el cálculo de la base imponible del IVA sea especial, por ejemplo, bienes usados, ventas por catálogo, bebidas alcohólicas o no alcohólicas.
Nota 8.1/ Cuando se trata del IVA las tarifas y códigos a utilizar son las siguientes:
Tarifa Impuesto Valor Agregado | Código
28Tarifa 0% (Artículo 32, num 1, RLIVA) | 01
Tarifa reducida 1% | 02
Tarifa reducida 2% | 03
Tarifa reducida 4% | 04
29Transitorio 0% | 05
30Transitorio 4% | 06
31Tarifa transitoria 8% | 07
Tarifa general 13% | 08
Tarifa reducida 0.5% | 09
32Tarifa Exenta | 10
33Tarifa 0% sin derecho a crédito | 11
28 La tarifa 0% se utilizará únicamente cuando la transacciones que se realicen correspondan a las transacciones definidas en el artículo 32, numeral 1 del Reglamento de la Ley sobre el Impuesto al Valor Agregado, que otorga derecho a crédito pleno, como por ejemplo ventas a la CCSS o a municipalidades, entre otros.
29 El código 05, Transitorio 0% se utilizará únicamente para efectos de las Notas de Crédito y Notas de Débito que lo requieran.
30 El código 06, Transitorio 4% se utilizará únicamente para efectos de las Notas de Crédito y Notas de Débito que lo requieran.
31 El código 07, Transitorio 8% se utilizará únicamente para efectos de las Notas de Crédito y Notas de Débito que lo requieran.
32 El código 10, Tarifa Exenta Ley 9635, Articulo 8.
33 El código 11, se utilizará únicamente en aquellos casos en los que se registre la transacción de un bien o servicio no sujeto pero que no otorga derecho a crédito.
Nota 9/ Los códigos de referencia a utilizar son:
Descripción del campo | Código
Anula Documento de Referencia | 01
Corrige monto | 02
Referencia a otro documento | 04
Sustituye comprobante provisional por contingencia. | 05
Devolución de mercancía | 06
Sustituye comprobante electrónico. | 07
Factura Endosada | 08
Nota de crédito financiera | 09
Nota de débito financiera | 10
Proveedor No Domiciliado | 11
34Crédito por exoneración posterior a la facturación | 12
Otros | 99
34 El código 12, Crédito por exoneración posterior a la facturación se utilizará únicamente para efectos de las notas de crédito que lo requieran cuando se aplique una exoneración concreta de impuestos locales aprobada posterior a la transacción.
Nota 10/ La codificación a utilizar en el campo "Tipo de documento de referencia" es la siguiente, sin embargo, para efectos de impresión y visualización se debe mostrar la descripción del código:
Tipo de Documento Referencia | Código
Factura electrónica | 01
Nota de débito electrónica | 02
Nota de crédito electrónica | 03
Tiquete electrónico | 04
Nota de despacho | 05
Contrato | 06
Procedimiento | 07
Comprobante emitido en contingencia | 08
35Devolución mercadería | 09
Comprobante electrónico rechazado por el Ministerio de Hacienda | 10
Sustituye factura rechazada por el Receptor del comprobante | 11
Sustituye Factura de exportación | 12
36Facturación mes vencido | 13
Comprobante aportado por contribuyente de Régimen Especial. | 14
Sustituye una Factura electrónica de Compra | 15
37Comprobante de Proveedor No Domiciliado | 16
Nota de Crédito a Factura Electrónica de Compra | 17
Nota de Débito a Factura Electrónica de Compra | 18
Otros | 99
35 El código 09, Devolución de mercadería se utilizará únicamente para efectos de las Notas de Crédito y Notas de Débito que lo requieran.
36 El código13 se puede utilizar en los comprobantes electrónicos únicamente cuando el servicio prestado vence el último día del mes, como por ejemplo servicios públicos, los cuales se facturan en los primeros días del mes, pero los ingresos pertenecen al mes anterior; En el campo "fecha de emisión del documento de referencia" del apartado de referencia de debe de indicar la fecha del periodo fiscal que corresponde el ingreso de la factura.
37 El código16 únicamente podrá ser utilizado en la Factura Electrónica de Compra.
Nota 10.1/ La codificación a utilizar en el campo "Tipo de documento de autorización o exoneración" es la siguiente, sin embargo, para efectos de impresión y visualización se debe mostrar la descripción del código:
Tipo de Documento de exoneración o autorización | Código
38Compras autorizadas por la Dirección General de Tributación | 01
Ventas exentas a diplomáticos | 02
Autorizado por Ley especial | 03
Exenciones Dirección General de Hacienda Autorización Local Genérica | 04
39Exenciones Dirección General de Hacienda Transitorio V (servicios de ingeniería, arquitectura, topografía obra civil) | 05
40Servicios turísticos inscritos ante el Instituto Costarricense de Turismo (ICT) | 06
41Transitorio XVII (Recolección, Clasificación, almacenamiento de Reciclaje y reutilizable) | 07
Exoneración a Zona Franca | 08
Exoneración de servicios complementarios para la exportación articulo 11 RLIVA | 09
42Órgano de las corporaciones municipales | 10
43Exenciones Dirección General de Hacienda Autorización de Impuesto Local Concreta | 11
Otros | 99
38 El código 01, Compras autorizadas por la Dirección General de Tributación se utilizará únicamente para efectos de las Notas de Crédito y Notas de Débito que lo requieran.
39 El código 05, Exenciones Dirección General de Hacienda Transitorio V (servicios de ingeniería, arquitectura, topografía obra civil se utilizará únicamente para efectos de las Notas de Crédito y Notas de Débito que lo requieran.
40 El código 06, Servicios turísticos inscritos ante el Instituto Costarricense de Turismo (ICT) se utilizará únicamente para efectos de las Notas de Crédito y Notas de Débito que lo requieran.
41 El código 07, Transitorio XVII (Recolección, Clasificación, almacenamiento de Reciclaje y reutilizable) se utilizará únicamente para efectos de las Notas de Crédito y Notas de Débito que lo requieran.
42 El código 10 la corporación municipal, se entenderá de acuerdo a lo establecido en los artículos 169 y siguientes de la Constitución Política, las Municipalidades son corporaciones de carácter autónomo, cuya competencia es la administración de los intereses y servicios locales en cada cantón en beneficio de la colectividad.
43 El código11 sobre "Autorización de impuesto local concreta" emitida por el Departamento de Gestión de Exenciones es de uso exclusivo cuando el receptor sea un beneficiario que disfrute de un incentivo fiscal para que puedan aplicar o bien puedan solicitar la devolución de impuestos locales, producto de compras en el mercado local.
Nota 11/ Los códigos para la descripción del mensaje son:
Mensaje | Código
Aceptado |
44Aceptación parcial | 2
Rechazado | 3
44 Aceptación parcial: Para uso exclusivo del Obligado Tributario permite aceptar de forma parcial el contenido de un comprobante electrónico, permitiendo con esto la confesión de una nota de crédito que permita ajustar la operación por el monto menor al de la factura originalmente emitida, de forma tal que la suma algebraica de sus importes, sea positivo el de la factura y negativo el de la nota de crédito, dando como resultado el valor neto real de la operación.
Nota 12/ La codificación a utilizar en el campo "Tipo de Código de producto/servicio" es la siguiente, sin embargo, para efectos de impresión y visualización se debe mostrar la descripción del nombre:
Tipo de Código de producto/servicio | Código
Código del producto del vendedor | 01
Código del producto del comprador | 02
45 Código del producto asignado por el fabricante - industriales o importadores | 03
Código uso interno | 04
Otros | 99
45 Cuando se Facturen códigos CAByS, este código hará referencia a los códigos estandarizados SKU, GTIN o equivalentes, con el que el paquete es identificado en la industria
Nota 13/ En todos los comprobantes electrónicos debe indicarse el Tipo de moneda en que se realizó la operación, para efectos de impresión y visualización se debe mostrar del Código de la moneda utilizada.
Nota 13.1/ El Código a utilizar en el nodo " Código y Tipo de Moneda "es el siguiente: Ver documento denominado "Codigodemoneda_V4.4".
Nota 14/ La codificación a utilizar en los campos cantón, provincia y distrito en Tipo de documento es la siguiente: Ver documento denominado "Codificacionubicacion_V4.4"
.Nota 15/ La codificación a utilizar en el campo "Unidad de medida" es la siguiente:
Símbolo | Descripción | Tipo de Unidad
1 | uno (índice de refracción) | Servicio
| minuto | Servicio
| segundo | Servicio
ºC | grado Celsius | Servicio
1/m | 1 por metro | Mercancía
A | Ampere | Servicio
A/m | ampere por metro | Servicio
A/m2 | ampere por metro cuadrado | Servicio
Acv | Activo Virtual | Mercancía
Al | Alquiler de uso habitacional | Servicio
Alc | Alquiler de uso comercial | Servicio
B | bel | Servicio
Bq | Becquerel | Servicio
C | coulomb | Servicio
C/kg | coulomb por kilogramo | Servicio
C/m2 | coulomb por metro cuadrado | Servicio
C/m3 | coulomb por metro cúbico | Servicio
Cc | Cajuela de café | Mercancía
Cd | Candela | Servicio
cd/m2 | candela por metro cuadrado | Servicio
Cm | Comisiones | Servicio
Cm | centímetro | Mercancía
Cu | cuartillos de café | Mercancía
D | día | Servicio
eV | electronvolt | Servicio
F | farad | Servicio
F/m | farad por metro | Servicio
Fa | fanega de café | Mercancía
G | Gramo | Mercancía
Gal | Galón | Mercancía
Símbolo | Descripción | Tipo de Unidad
Gy | gray | Servicio
Gy/s | gray por segundo | Servicio
H | hora | Servicio
H | henry | Servicio
H/m | henry por metro | Servicio
Hz | hertz | Servicio
l | Intereses | Servicio
J | Joule | Servicio
J/(kg·K) | joule por kilogramo kelvin | Servicio
J/(mol·K) | joule por mol kelvin | Servicio
J/K | joule por kelvin | Servicio
J/kg | joule por kilogramo | Servicio
J/m3 | joule por metro cúbico | Servicio
J/mol | joule por mol | Servicio
K | Kelvin | Servicio
Kat | katal | Servicio
kat/m3 | katal por metro cúbico | Servicio
Kg | Kilogramo | Mercancía
kg/m3 | kilogramo por metro cúbico | Mercancía
Km | Kilometro | Servicio
Kw | kilovatios | Servicio
kWh | Kilovatios por hora | Servicio
L | litro | Mercancía
Lm | lumen | Servicio
Ln | pulgada | Mercancía
Lx | lux | Servicio
M | Metro | Mercancía
m/s | metro por segundo | Servicio
m/s2 | metro por segundo cuadrado | Servicio
m2 | metro cuadrado | Mercancía
m3 | metro cúbico | Mercancía
Min | minuto | Servicio
Símbolo | Descripción | Tipo de Unidad
ml | mililitro | Mercancía
Mm | Milímetro | Mercancía
Mol | Mol | Mercancía
mol/m3 | mol por metro cúbico | Mercancía
N | newton | Servicio
N/m | newton por metro | Servicio
N·m | newton metro | Servicio
Np | neper | Servicio
º | grado | Servicio
Os | Otro tipo de servicio | Servicio
Otros | Se debe indicar la descripción de la medida a utilizar | Mercancía
Oz | Onzas | Mercancía
Pa | pascal | Servicio
Pa·s | pascal segundo | Servicio
Qq | Quintal | Mercancía
Rad | radián | Servicio
rad/s | radián por segundo | Servicio
rad/s2 | radián por segundo cuadrado | Servicio
S | Segundo | Servicio
S | siemens | Servicio
Sp | Servicios Profesionales | Servicio
Spe | Servicios personales | Servicio
Sr | estereorradián | Servicio
St | Servicios técnicos | Servicio
Sv | sievert | Servicio
T | tesla | Servicio
T | tonelada | Mercancía
U | unidad de masa atómica unificada | Mercancía
Ua | unidad astronómica | Servicio
Unid | Unidad | Mercancía
V | volt | Servicio
V/m | volt por metro | Servicio
Símbolo | Descripción | Tipo de Unidad
W | Watt | Servicio
W/(m·K) | watt por metro kevin | Servicio
W/(m2·sr) | watt por metro cuadrado estereorradián | Servicio
W/m2 | watt por metro cuadrado | Servicio
W/sr | watt por estereorradián | Servicio
Wb | weber | Servicio
? | ohm | Servicio
Nota 16/ La codificación a utilizar en el campo "Tipo de documento" es la siguiente:
Tipo de documento | Código
Contribución parafiscal | 01
Timbre de la Cruz Roja | 02
Timbre de Benemérito Cuerpo de Bomberos de Costa Rica. | 03
Cobro de un tercero | 04
Costos de Exportación | 05
Impuesto de servicio 10% | 06
Timbre de Colegios Profesionales | 07
Depósitos de Garantía | 08
Multas o Penalizaciones | 09
Intereses Moratorios | 10
Otros Cargos | 99
Nota 17/ La codificación a utilizar en el campo "Código" será la indicada en el catálogo de bienes y servicios (CABYS)
Nota 18/ La condición del impuesto a utilizar es la siguiente:
Condición de impuesto | Código
46Genera crédito IVA | 01
47Genera Crédito parcial del IVA | 02
48Bienes de Capital | 03
49Gasto corriente no genera crédito | 04
50Proporcionalidad | 05
46 Se utiliza, cuando el IVA pagado se utilizará en su totalidad como un crédito en la declaración del Impuesto al Valor Agregado.
47 Se utiliza, cuando el crédito que se aplica es proporcional a la tarifa reducida, ejemplo se adquiere una computadora gravada al 13% para servicios médicos, por lo cual del impuesto pagado me acredito un 4% y el restante 9% se constituye como un costo, o la factura posee líneas para diferentes actividades.
48 Se utiliza, cuando se adquieren bienes utilizados en la producción o fabricación de productos (bienes de consumo) que no están incorporados como componentes o materias primas de estos. ejemplo equipos, inmuebles etc.
49 Se utiliza cuando el IVA pagado no es aplicable en la declaración de Impuesto al Valor Agregado, por el contrario, representa un gasto en la declaración de utilidades.
50 Se utiliza, cuando al momento que la confirmación de la factura se desconoce si el bien o servicio, será utilizado en la producción o prestación de servicio que se encuentren gravados del IVA, o desconozco la tarifa que puedo aplicar como crédito para cada actividad económica.
Nota 19 / El Código a utilizar en campo "forma farmacéutica": Ver documento denominado "Código de forma Farmacéutica".
Nota 20 / Los tipos de descuentos a utilizar en el campo "Código del Descuento" del Descuento son los siguientes:
Tipo Descuentos | Código
Descuento por Regalía | 01
Descuento por Regalía IVA Cobrado al Cliente | 02
Descuento por Bonificación | 03
Descuento por volumen | 04
Descuento por Temporada (estacional) | 05
Descuento promocional | 06
Descuento Comercial | 07
Descuento por frecuencia | 08
Descuento sostenido | 09
Otros descuentos | 99
Nota 21/ La condición del IVA cobrado a nivel de fábrica a utilizar es la siguiente:
IVA cobrado a nivel de fábrica | Código
Venta de bienes con IVA según el sistema especial de determinación de IVA a nivel de fábrica (Se utiliza cuando se está cobrando el IVA a nivel de fábrica. | 01
Ventas exentas según el sistema especial de determinación de IVA a nivel de fábrica, mayorista y aduanas (se utiliza cuando el producto se encuentra exento ya que el bien soporto el cobro de impuestos a nivel de fábrica). | 02
Nota 22/ La codificación a utilizar en el campo "Tipo de Transacción" es la siguiente:
Descripción | Código
Venta Normal de Bienes y Servicios (Transacción General) | 01
Mercancía de Autoconsumo exento | 02
Mercancía de Autoconsumo gravado | 03
Servicio de Autoconsumo exento | 04
Servicio de Autoconsumo gravado | 05
Cuota de afiliación | 06
Cuota de afiliación Exenta | 07
Bienes de Capital para el emisor | 08
Bienes de Capital para el receptor. | 09
Bienes de Capital para para el emisor y el receptor. | 10
51Bienes de capital de autoconsumo exento para el emisor | 11
52Bienes de capital sin contraprestación a terceros exento para el emisor | 12
53Sin contraprestación a terceros | 13
51 Se utiliza cuando se haya retirado bienes de capital para uso o consumo personal del contribuyente (LIVA art. 2, párrafo 1 e inciso 1, subinciso e) y RLIVA art. 1, incisos 4 y 5).
52 Se utiliza cuando se haya retirado bienes de capital para su transferencia sin contraprestación a terceros (LIVA art. 2, párrafo 1 e inciso 1, subinciso e) y RLIVA art. 1, inciso 5).
53 Se utiliza cuando se haya el retiro de bienes para uso o consumo personal del contribuyente o su transferencia sin contraprestación a terceros (LIVA art 2, inciso 1, subinciso e),
Nota 23/ La codificación a utilizar en el campo "Nombre de la Institución o dependencia que emitió la exoneración" es la siguiente:
Nombre de la Institución | Código
Ministerio de Hacienda | 01
Ministerio de Relaciones Exteriores y Culto | 02
Ministerio de Agricultura y Ganadería | 03
Ministerio de Economía, Industria y Comercio | 04
Cruz Roja Costarricense | 05
Benemérito Cuerpo de Bomberos de Costa Rica | 06
Asociación Obras del Espíritu Santo | 07
Federación Cruzada Nacional de protección al Anciano (Fecrunapa) | 08
Escuela de Agricultura de la Región Húmeda (EARTH) | 09
Instituto Centroamericano de Administración de Empresas (INCAE) | 10
Junta de Protección Social (JPS) | 11
Autoridad Reguladora de los Servicios Públicos (Aresep) | 12
Otros | 99
