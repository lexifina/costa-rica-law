DIRECCIÓN GENERAL DE ADUANAS
San José, 17 de agosto del 2006
CIRCULAR ONVVA-007-2006
Señores (as)
Gerentes, Subgerentes y Jefes de Departamento de Aduanas
Directores y Jefes de Departamento de la Dirección General de Aduanas
Asesores y Funcionarios Aduaneros
Agentes y Agencias de Aduanas
Tribunal Aduanero Nacional
Servicio Nacional de Aduanas
S. M
ASUNTO: Directrices para el agrupamiento de las variables correspondientes a la descripción de las mercancías importadas
.
Estimados (as) señores (as):
La Dirección General de Aduanas de conformidad con las potestades y atribuciones que le confieren los artículos 11, 24 y 245 de la Ley General de Aduanas Nº 7557 con sus reformas y modificaciones; artículos 5º y 25 del Reglamento a la Ley General de Aduanas con sus reformas y modificaciones, el Acuerdo sobre Valoración en Aduana de la O.M.C., el Reglamento Centroamericano sobre la Valoración Aduanera de las Mercancías y la Ley Nº 8013: Adición del Título XII a la Ley General de Aduanas Nº 7557, procede a emitir las siguientes directrices relacionadas con el agrupamiento de las variables correspondientes a la descripción de las mercancías importadas:
I. Normativa aplicable al agrupamiento de las variables para la
descripción de las mercancías.
El Reglamento Centroamericano sobre la Valoración Aduanera de las Mercancías, en el Anexo denominado: “Instructivo para el llenado de la Declaración del Valor en Aduana de las mercancías importadas”, en el encabezado del apartado tercero sobre “Descripción de las mercancías” establece:
“Para los efectos del llenado de las casillas del presente apartado, deberá realizarse en el anexo de la declaración del valor, agrupando las mercancías que correspondan a la misma marca, modelo, estilo, origen, clasificación arancelaria, estado, precio unitario y demás características que sean comunes”. (El subrayado no es del original).
De conformidad con lo indicado en el párrafo anterior y lo regulado en la casilla 32 de la declaración del valor, se debe entender como características comunes:
 Tamaño, forma, color, mecanismos de funcionamiento, composición, talla y demás características y especificaciones técnicas que permitan su correcta identificación.
II. Agrupamiento de las variables para la descripción de las mercancías.
A. Para efectos de la transmisión electrónica en el sistema informático TIC@ y para la aplicación de la normativa citada, se seguirá el siguiente procedimiento en estricto orden:
1. Como primer parámetro de agrupamiento, en la declaración por línea del DUA se deben considerar como variables para agrupar siempre y cuando sean iguales, la clasificación arancelaria, el estado y el origen de la mercancía, las cuales se declaran en el “Bloque del Líneas del DUA”.
2. Las demás características de las mercancías agrupadas conforme al primer parámetro: marca, modelo, estilo, precio unitario, cantidades, tamaño, forma, color, mecanismos de funcionamiento, composición, talla y demás características y especificaciones técnicas, se deben declarar en el “Bloque de Datos de Líneas de Factura”. Con excepción de las variables precio unitario y cantidades, las demás características indicadas en este párrafo deberán declararse en los campos de descripción del “Bloque de Líneas del DUA”.
3. En el caso de que las demás características de las mercancías agrupadas conforme al primer parámetro sean diferentes, en cuanto a tamaño, forma, color, mecanismos de funcionamiento, composición, talla y demás características y especificaciones técnicas, se pueden declarar en la misma línea del “Bloque de Líneas de Factura”, siempre y cuando esas diferencias no incidan en la marca, el modelo, el estilo, el precio unitario y la cantidad.
Ejemplo Nº 1: Importación de calzado.
• Clasificación arancelaria: 6403.51.00.00.
• Marca: Barquito.
• Nombre del proveedor: El Barco S. A.: Número de proveedor 1.
• Número de factura: 2530.
• Género: Mujer.
• Tipo: Casual.
• Estilo: Botines.
• Modelo: XR520.
• Cantidad: 20 pares, 25 pares y 30 pares.
• Estado: Nuevo.
• Materia constitutiva: Cuero.
• Medida: De la 35 al 40.
• Color: Café, negro, azul, blanco, vino, rojo, rosado, celeste.
• Código de referencia: 2203050.
• Origen: Brasil.
• Precio Unitario: $40.00, $50.00 y $25.00
De conformidad con el ejemplo anterior corresponde declarar en una sola línea de DUA la siguiente información:
Bloque | Campo | Nombre | Descripción | Datos del ejemplo
Líneas de Mercancías del DUA | 4 | Nume_Serie | Número de la línea | 001
| 5 | Part_Nandi | Partida arancelaria | 6403.51.0000
| 15 | País_Orige | País origen | Brasil
| 12 | Sest_Merca | Condición física De la Mercancía | Nuevo
A esa línea de DUA se deben asociar según el ejemplo, tres líneas del “Bloque de Líneas de Factura”, '65n razón de que los precios unitarios son distintos, declarándose la información de la factura comercial como sigue:
Bloque | Campo | Nombre | Descripción | Datos del ejemplo
Datos de las líneas de factura | 4 | Nume_Serie | Número de línea | 001
| 5 | Num_Prove | Número del proveedor | 1
| 6 | Nume_Factu | Número de la factura | 2530
| 7 | Ítem_Factu | Ítem de factura | 1
| 9 | Produc_Desc | Descripción de la mercancía | Mujer, casual, botines, cuero, café, negro, azul, blanco, vino, rojo, rosado y celeste. Medida: del 35 -37. Código de referencia 2203050
| 10 | Cnt_Produc | Cantidad de mercancía en unidades comerciales | 20 pares
| 11 | Val_Unidad | Precio unitario de la mercancía | $40.00
| 12 | Marca | Marca de la mercancía | Barquito
| 13 | Facmodelo | Modelo de la mercancía | XR520
| | | |
Bloque | Campo | Nombre | Descripción | Datos del ejemplo
Datos de las líneas de factura | 4 | Nume_Serie | Número de línea | 001
| 5 | Num_Prove | Número del proveedor | 1
| 6 | Nume_Factu | Número de la factura | 2530
| 7 | Ítem_Factu | Ítem de factura | 2
| 9 | Produc_Desc | Descripción de la mercancía | Mujer, casual, botines, cuero, café, negro, azul, blanco, vino, rojo, rosado y celeste. Medida: 38-39. Código de referencia 2203050
| 10 | Cnt_Produc | Cantidad de mercancía en unidades comerciales | 25 pares
| 11 | Val_Unidad | Precio unitario de la mercancía | $50.00
| 12 | Marca | Marca de la mercancía | Barquito
| 13 | Facmodelo | Modelo de la mercancía | 13 XR520
Bloque | Campo | Nombre | Descripción | Datos del ejemplo
Datos de las líneas de factura | 4 | Nume_Serie | Número de línea | 001
| 5 | Num_Prove | Número del proveedor | 1
| 6 | Nume_Factu | Número de la factura | 2530
| 7 | Ítem_Factu | Ítem de factura | 2
| 9 | Produc_Desc | Descripción de la mercancía | Mujer, casual, botines, cuero, café, negro, azul, blanco, vino, rojo, rosado y celeste. Medida: 38-39. Código de referencia 2203050
| 10 | Cnt_Produc | Cantidad de mercancía en unidades comerciales | 25 pares
| 11 | Val_Unidad | Precio unitario de la mercancía | $50.00
| 12 | Marca | Marca de la mercancía | Barquito
| 13 | Facmodelo | Modelo de la mercancía | 13 XR520
Al existir una sola línea de mercancía del DUA, esta se podrá asociar solamente con una Línea de la Declaración del Valor (DVA), sin embargo en el caso de líneas del “Bloque de Factura” se podrán asociar “n” cantidad de líneas de una factura comercial a una sola línea del DUA, es decir la relación sería la siguiente:
Línea de DUA | 1. Línea de Factura 2. Línea de Factura 3. Línea de Factura | Primer Proveedor | Primera Línea de la DVA
En el caso de existir facturas de diferentes proveedores asociadas a un mismo DUA se debe declarar la información de esas facturas en líneas distintas, siendo la relación la siguiente:
Tara Línea de DUA | 1. Línea de Factura 2. Línea de Factura 3. Línea de Factura | Segundo Proveedor | Segunda Línea de la DVA
III. Llenado del formulario de la declaración del valor.
Para efectos del agrupamiento de las variables correspondientes a la descripción de las mercancías en el formulario de la Declaración del Valor, se aplicarán las directrices que establece el Reglamento Centroamericano sobre la Valoración Aduanera de las Mercancías y debe adjuntarse debidamente firmado por el importador a la Declaración Aduanera de Importación o a los documentos que amparan el DUA de importación, según corresponda. Rige a partir del 2 de octubre del 2006. Publíquese en el Diario Oficial La Gaceta.
